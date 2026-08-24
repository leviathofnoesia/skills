# "The Abyss dashboard is completely broken" — diagnosis recipe

Session-proven workflow from a user report that the Abyss dashboard was
"completely broken and unusable". The backend was actually healthy the whole
time; the UI was lying. This is the order of investigation that found it fast.

## 1. Prove the backend first (do NOT trust the screenshot)

The API is auth-gated over HTTP (port 8789 returned `{"ok":false,"error":"unauthorized"}`).
Call the plugin core directly instead:

```bash
cd <HERMES_HOME>/plugins/abyss   # the LIVE copy — the global one, not profiles/<name>/plugins
HERMES_PROFILE_HOME=<profile home> python -c "
import sys; sys.path.insert(0, '.')
import __init__ as abyss
print(abyss.list_activity(limit=3))
"
```

Run the shipped suite with the profile env var set:

```bash
HERMES_PROFILE_HOME=<profile home> python test_plugin.py   # 75 checks, all must pass
```

Result in this case: all 8 API endpoints + all 75 tests passed → backend healthy.

## 2. Inspect the SQLite DB directly

Data dir (profile-scoped): `<HERMES_HOME>/profiles/<name>/abyss-data/`
- `activity.db` — tables `activity`, `signals`, `incidents`
- `traces.db` — table `traces`

Key queries (found the whole story):
- `SELECT COUNT(*) FROM activity` — 1368 rows; UI showed "1352 ACT" (close)
- `SELECT category, COUNT(*) FROM activity GROUP BY category` → only `tool/llm/session`
  (the UI's `cron/task/command` filters matched zero rows)
- `SELECT session_id, COUNT(*) FROM activity GROUP BY session_id ORDER BY 2 DESC`
  → top 10 sessions were ALL `cron_ce4be41ffbde_*` (a watcher cron job)
- `SELECT severity, COUNT(*) FROM signals WHERE resolved=0 GROUP BY severity`
  → 704 error / 142 warning / 9 info OPEN signals
- `SELECT COUNT(*) FROM signals WHERE resolved=0 AND session_id LIKE 'cron_%'`
  → 708 of 826 open signals came from cron sessions

## 3. Find the noise source

`<HERMES_HOME>/profiles/<name>/cron/jobs.json` — the culprit was
"Watch Tibo for Codex Limit Resets": `no_agent: true`, interval 5m, 306 runs,
scraping X → timeouts/rate_limits/tool_errors → 708 signals + 29 incidents.
`no_agent` cron jobs don't emit hook activity, so it stopped flooding the DB
once switched — but the Aug 8-9 backlog stayed and pinned health at critical.

## 4. The four UI defects found (and their fixes)

1. **Health pinned at critical (32.5)** — `get_health()` counted ALL open
   signals (826) with threshold 20 → `signal_score` always 0. Fix: window
   signals/incidents to last 7 days; soften thresholds (signal 0→25 pts,
   100+ open→0; incident 0→25, 20+ open→0). Result: 32.5 critical → 61.9 degraded.
2. **Status bar undercount (50 SIG / 43 critical)** — `StatusStrip` fetched
   `/signals?limit=50` and presented the sample as totals. Fix: extend
   `get_status()` with `signals_open/total/critical/error/warning/info` and have
   the UI read those.
3. **No auto-refresh** — `StatusStrip`/`ActivityFeed` fetched once on mount.
   Fix: `useEffect(() => { fetchAll(); const t = setInterval(fetchAll, 30000);
   return () => clearInterval(t) }, [fetchAll])`.
4. **Dead filter buttons** — filter list must match real categories
   (`['all','tool','llm','session','system']`), not `cron/task/command`.

## 5. Data cleanup (with backup)

```bash
mkdir -p <data>/backup && cp activity.db traces.db backup/   # ALWAYS first
```

Then resolve stale cron signals + close their incidents via the plugin's own
triage semantics:

```sql
UPDATE signals SET acknowledged=1, resolved=1, acknowledged_at=?, resolved_at=?
  WHERE resolved=0 AND session_id LIKE 'cron_%';
UPDATE incidents SET status='closed', resolved_at=?
  WHERE status IN ('open','acknowledged') AND (session_ids LIKE '%cron_%' OR title LIKE '%cron_ce4%');
```

Result: 708 signals resolved, 29 incidents closed → 170 open signals / 5 open
incidents remaining (real recent ones).

## 6. Make the changes take effect

- Frontend `plugin.js` hot-reloads (runtime-loader watches the file). Verify with
  `node --check plugin.js`.
- Backend `__init__.py` requires a restart: ⌘K → Restart gateway, or kill the
  `hermes_cli.main serve --host 127.0.0.1 --port 0` python process so it respawns.
  Confirm with `grep "Mounted plugin API routes" profiles/<name>/logs/gui.log`.

## 7. Windows-specific tooling notes

- `patch` tool's auto-lint mangles Windows paths (`C:\c\Users\...` MODULE_NOT_FOUND)
  — that lint error is a false positive on this host; verify JS with
  `node --check plugin.js` instead.
- `patch`/`write_file` on the GLOBAL `<HERMES_HOME>/plugins/abyss` (which belongs
  to the 'default' profile scope) trips the cross-profile soft guard from a
  named-profile session — pass `cross_profile=true` after user direction to
  proceed; the plugin's live copy IS the global one.
- `vision_analyze` may reject images on some models ("unknown variant image_url")
  — fall back to the user's attached description + code reading, don't block on it.
- Packaged Hermes.exe has CDP closed; `computer_use` capture of a minimized
  window returns only window chrome. Ground truth = on-disk files + DB, not the
  live window.
