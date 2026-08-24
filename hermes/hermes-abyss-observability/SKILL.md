---
name: hermes-abyss-observability
description: "Agent observability with Raindrop-style tracing for Hermes."
version: 0.1.0
author: Hermes
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [observability, monitoring, raindrop, signals, incidents, tracing, hooks]
    related_skills: [hermes-desktop-plugin-development]
---

# Hermes Abyss — Raindrop-Style Agent Observability

Build observability into Hermes plugins using patterns inspired by Raindrop.ai
("the Sentry for AI Agents"). Records tool calls, LLM interactions, and session
events; detects silent agent failures (errors, timeouts, rate limits, loops,
vague replies); clusters signals into incidents; and surfaces traces via
desktop UI. Use alongside `hermes-desktop-plugin-development`.

## When to Use

- The user wants "monitoring" or "observability" for an AI agent
- Building a dashboard that records and displays agent behavior over time
- User asks for "tracing", "signals", "incidents", or "self-diagnostics"
- Need to detect silent agent failures that traditional logs miss
- Want to auto-record tool calls and LLM calls via hooks

## Prerequisites

- Hermes desktop app running
- Write access to `~/.hermes/plugins/<id>/` and `~/.hermes/desktop-plugins/<id>/`

## Key Insight

Raindrop.ai's core observation: traditional logs and APM miss the failure
modes of LLMs and agents — silent tool errors, "forgetting", vague replies,
persona drift, hallucinations, loops, and broken tools. Three layers:
1. Activity recording — hooks auto-log into SQLite
2. Signal detection — classifiers flag anomalies in results
3. Incident clustering — groups related signals into trackable incidents

## Quick Reference

### File Structure
```
~/.hermes/plugins/<id>/              ← Python backend
├── plugin.yaml                      ← declares hooks
├── manifest.yaml                    ← api path + desktop entry
├── __init__.py                      ← hook handlers + handle_request()
└── dashboard/plugin_api.py          ← REST layer

~/.hermes/desktop-plugins/<id>/      ← Desktop UI
├── plugin.js, activity-feed.js, calendar-view.js
├── global-search.js, tracing-view.js, brain-view.js
├── signals-incidents.js, ditherkit.js
```

### Slash Commands
```
/abyss recent [N]                  Show last N activity entries
/abyss stats                       Summary statistics
/abyss search <query>              Search all data sources
/abyss trace <session_id>          Trace timeline for a session
/abyss signals                     Show detected signals
/abyss incidents                   Show clustered incidents
/abyss diagnostic <cap> <gap>      Record self-diagnostic signal
/abyss clean                       Clear all data
```

### REST API Endpoints
```
GET  /activity   POST /activity   GET /calendar
GET  /search     GET /stats       GET /trace?session_id=...
GET  /graph      GET /signals     GET /incidents
POST /signals/self-diagnostic  POST /incidents/cluster
```

### Hook Registration (Python)
```python
def register(ctx):
    ctx.register_hook("pre_tool_call", _on_pre_tool_call)
    ctx.register_hook("post_tool_call", _on_post_tool_call)
    ctx.register_hook("post_llm_call", _on_post_llm_call)
    ctx.register_hook("on_session_start", _on_session_start)
    ctx.register_hook("on_session_end", _on_session_end)
    ctx.register_command("abyss", handler=_handle_slash, ...)
```

## Signal Types

| Type | Severity | Detection |
|------|----------|-----------|
| `tool_error` | error | Result text contains "error" or "exception" |
| `timeout` | warning | Result text contains "timeout" |
| `rate_limit` | warning | Result mentions "rate limit" or "429" |
| `loop_detected` | error | Same tool called 3+ times with identical args |
| `vague_reply` | warning | LLM result under 20 chars |
| `self_diagnostic` | variable | Agent self-reports via `/abyss diagnostic` |

## Incident Clustering

- Same session + 2+ signals → cluster into one incident
- Highest severity wins (critical > error > warning > info)
- Auto-cluster on new signal via `_cluster_incidents()`

## Procedure

1. Create Python backend: `~/.hermes/plugins/<id>/` with `plugin.yaml`, `__init__.py`
2. Create `dashboard/plugin_api.py` — REST layer delegating to `__init__.handle_request()`
3. Create desktop UI: `~/.hermes/desktop-plugins/<id>/plugin.js` + sub-components
4. Enable: `hermes config set plugins.enabled '["<id>"]'`
5. Reload: cmd+K → "Reload desktop plugins" or hot reload on save
6. Verify: `/abyss stats`

## Pitfalls

- **Real hook payloads use different kwargs than you'd assume** — `post_llm_call` fires with `assistant_response`, `user_message`, `model`, `platform`, `turn_id` (NOT `result`/`prompt`); `post_tool_call` fires with structured `status`, `error_type`, `error_message`, `duration_ms` alongside `result`. Design handlers from `agent/turn_finalizer.py` (post_llm_call) and `model_tools.py::_emit_post_tool_call_hook` (post_tool_call). Prefer the structured fields over grepping result text for signal detection.
- **Desktop UI is single-file `plugin.js`** — the loader evaluates it as a Blob URL, so relative imports fail. The multi-file layout shown above (activity-feed.js, brain-view.js, etc.) is legacy/orphaned; if those files exist next to plugin.js they are NOT loaded and should be deleted. All components live inlined in plugin.js.
- `ctx.rest()` resolves PARSED JSON directly — `hermesDesktop.api` (`fetchJson`) returns `JSON.parse(text)`, so `await ctx.rest('/status', {method:'GET'})` already gives the object. NEVER call `.json()` on it (`r.json is not a function`). (Corrected: this skill previously said the opposite; `abyss-raindrop-observability` has the right call.)
- **The backend imports plugin code at mount time, not per request** — `_mount_plugin_api_routes()` does `importlib.util.spec_from_file_location` at startup. Editing `__init__.py` takes effect only after a backend restart (⌘K → Restart gateway, or kill the `hermes_cli.main serve --port 0` python process so it respawns). Frontend `plugin.js` DOES hot-reload via the runtime-loader file watch. Verify mount with `grep "Mounted plugin API routes" profiles/<name>/logs/gui.log`.
- **Packaged desktop builds close CDP** (`apps/desktop/electron/dev-cdp.ts`: packaged = always closed). You cannot read the live DOM on a packaged Hermes.exe. Ground-truth the UI by reading on-disk plugin.js + the SQLite DB + calling `handle_request()` directly — not by inspecting the running window. When a screenshot's layout doesn't match on-disk plugin.js, suspect a stale/cached alternate copy rather than assuming the file is what renders.
- **"Dashboard looks broken" is often data/UX, not a broken backend** — all endpoints can return healthy data while the UI lies (stale snapshot, sample-derived totals, dead filters). Diagnose backend first with `test_plugin.py` + direct `handle_request()` calls, then inspect the DB, then read the UI code. See `references/dashboard-lies-diagnosis.md` for the full recipe from a real "completely broken" report.
- **Verify every Tailwind class against the host's compiled CSS** — the plugin runs as a Blob URL so Tailwind never scans it; a class missing from the bundle silently falls back and breaks layout. Real case: tab bar used `grid-cols-7`, which does NOT exist in the compiled CSS (only `grid-cols-1/2/4/6` do) → the 7 tabs rendered as a broken **vertical stack** the user called "a random vertical tab list that does nothing". Check the packaged bundle: `grep -o '\.grid-cols-[0-9]*' release/win-unpacked/resources/app.asar.unpacked/dist/assets/index-*.css`. Gotcha: paren classes like `bg-(--ui-bg-quaternary)` ARE present but escaped (`bg-\(--ui-bg-quaternary\)`) — a naive grep for the paren form misses them; search for the inner token (`ui-bg-quaternary`) instead. Also, adding `flex` may LOSE to the host base class `inline-flex` (whichever rule comes later in the stylesheet wins) — that's still a horizontal row, so it's fine; the real bug was the grid.
- **User reports "UI broken"? Check the interaction model first, then data** — a user saying a dashboard is broken usually means navigation: can I close it, can I switch tabs, why is there a stray list. Data fixes (real totals, polling) are necessary but the visible complaints were: (1) no way to close the full-page `/abyss` route → add a ✕ close button in the Masthead (`host.navigate('/')`) and make the bottom-bar chip a toggle (`isOpen()` on `window.location.hash`); (2) tab bar hidden/broken → the `grid-cols-7` vertical stack above; (3) fix the tab row as `flex w-full items-center overflow-x-auto` with `shrink-0` triggers so all 7 tabs are reachable and scroll horizontally. Also: the auto-generated screenshot description can mislead (it described an unrelated overlay and misread per-row labels) — verify layout claims against code, not the description.
- **RUN THE THREE SCRIPT-STYLE TESTS VIA SUBSET ISOLATION, NOT IN-PROCESS** — `test_plugin.py`, `test_wave.py`, and `dashboard/test_api.py` are self-executing scripts: each sets `os.environ["HERMES_PROFILE_HOME"]` at module level and imports `__init__` (whose `ACTIVITY_DB`/`TRACE_DB` constants are fixed at first import). Importing them in the SAME pytest process makes later files silently read/write an EARLIER file's temp DB (observed: `dashboard/test_api.py` saw `test_plugin.py`'s pre-seeded rows and failed `GET /activity` exact-count). conftest.py now detects `_run_script` and forces subprocess isolation + dedups the normal `test_runner()` items (`pytest_collection_modifyitems`) — don't regress that. Direct `python test_X.py` is always safe; `python -m pytest test_plugin.py test_wave.py dashboard/test_api.py` should report **3 passed** (one isolated item per file).
- **Signal totals must come from `/status`, never from `/signals?limit=N`** — deriving "open/critical" counts by sampling a 50-row list undercounts badly (826 open signals displayed as "50 SIG / 43 critical"). Add a severity breakdown to `get_status()` and have the UI read it.
- **Health score needs a recency window** — `get_health()` counting ALL open signals/incidents with a threshold of 20/5 pins the score at "critical" forever after one noisy cron job floods signals (708 of 826 signals from one watcher session). Window signal/incident counts to the last 7 days and soften thresholds (signal 0→25pts / 100+ open→0; incident 0→25 / 20+ open→0).
- **Every "live:" dashboard pane needs polling** — `StatusStrip`/`ActivityFeed` fetch once on mount; without `setInterval` the pane shows a frozen snapshot and users report it "broken" even though the backend records fine.
- **Filter buttons must match categories the backend actually records** — `cron/task/command` match zero rows when hooks only write `tool/llm/session/system`; clicking them always shows an empty state.
- **Abyss data lives profile-scoped**: `PROFILE_HOME/abyss-data/` (`activity.db`, `traces.db`) when `HERMES_PROFILE_HOME` is set; the global `HERMES_HOME/abyss-data` may be empty. Run `test_plugin.py` and direct checks with `HERMES_PROFILE_HOME=<profile home>` exported.
- **Data cleanup is reversible with a backup**: before bulk-resolving stale signals (`UPDATE signals SET resolved=1 WHERE session_id LIKE 'cron_%'`) or closing incidents, copy `activity.db`/`traces.db` to `abyss-data/backup/`. Use the plugin's own triage semantics (resolved=1 + acknowledged=1, status='closed').
- `ctx.socket()` is no-op on OAuth remotes — use polling fallback
- SQLite on Windows — use `str(path)` not Path objects
- Don't import from `dashboard/plugin_api.py` in `__init__.py` (circular)
- Don't call `_add_activity` inside signal detection (recursion)
- `write_file` ~8K token limit — split large files, use `patch`

## Verification
```bash
cd ~/.hermes/plugins/<id> && python -c "from __init__ import _init_db; _init_db(); print('OK')"
python test_plugin.py
# Then: /abyss stats
```

## Related References
- `hermes-desktop-plugin-development` — full desktop plugin architecture
- `hermes-agent` — Hermes CLI, configuration
- `references/raindrop-concepts.md` — Raindrop.ai mental model
- `references/dashboard-lies-diagnosis.md` — full recipe for "dashboard is completely broken" reports (backend-first diagnosis, DB inspection, UI defects, cleanup with backup)
- `references/ui-layout-diagnosis.md` — "tab bar is a broken vertical list / can't close the page": missing Tailwind class in compiled CSS (grid-cols-7), verifying classes against the packaged bundle, close/toggle affordances for full-page routes
