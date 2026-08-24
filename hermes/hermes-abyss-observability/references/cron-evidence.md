# Cron job evidence — "completed" is not "did work"

When a cron job (especially an Abyss night-shift) "completes ok", that
only means the run finished without a delivery error. It tells you
nothing about what the agent actually did. To get real evidence:

## Where to look

```
<profile_home>/cron/
├── jobs.json              ← job definitions + last_status / next_run_at
├── executions.db          ← SQLite; one row per tick with start/finish/error
└── output/
    ├── <job_id>_<YYYYMMDD_HHMMSS>.txt   ← per-tick agent transcripts
    └── <job_id>/                       ← some jobs write here instead
```

## Reading executions.db

Columns: `id, job_id, source, process_id, pid, process_started_at, status,
claimed_at, started_at, finished_at, error`.

```python
import sqlite3, os
from datetime import datetime
db = os.path.expanduser("~/AppData/Local/hermes/profiles/<name>/cron/executions.db")
conn = sqlite3.connect(db)
cur = conn.cursor()
for r in cur.execute(
    "SELECT started_at, finished_at, status, error FROM executions "
    "WHERE job_id=? ORDER BY started_at", ("<job_id>",)
):
    s = datetime.fromisoformat(r[0].split("-04:00")[0])
    e = datetime.fromisoformat(r[1].split("-04:00")[0])
    print(f"{r[0][:19]} → {r[1][11:19]} | {str(e-s).split('.')[0]} | {r[2]} | {(r[3] or '')[:80]}")
```

## Reading the per-tick transcripts

`<profile_home>/cron/output/<job_id>_<YYYYMMDD_HHMMSS>.txt` is the agent's
final response — exactly what it would have delivered to the user. This
is the real "what happened" log. Combine it with `git status` / file
mtimes on the plugin tree to corroborate edits.

## Common gotchas

- **HTTP 429 ticks** show `status='failed'` with
  `error: "RuntimeError: HTTP 429..."`. The transcript file may not
  exist (the LLM never ran). Count them separately from "the agent
  decided nothing to do".
- **`no_agent: true` jobs** (like `watch_codex_resets.py`) don't have
  agent transcripts — they only have `last_status` and stdout. Verify
  their work by the script's own side effects (notified, written,
  scraped).
- **Schedule gotcha**: `0 0 * * *` fires ONCE at midnight. For
  sustained overnight work (e.g. "all night between 12-8am"), use
  `*/30 0-7 * * *` so each tick picks up new state and produces a
  fresh delivery.
- **Execution duration > expected**: a tick that "completes" in
  60+ minutes ran an LLM agent on a large prompt. A tick that
  completes in 1-2 minutes after a 429 failed instantly.
- **Profile scoping**: `executions.db` and `cron/output/` are
  **profile-scoped** under `profiles/<name>/cron/`, not global. The
  default profile uses `~/.hermes/cron/` (less common — most setups
  run jobs under a named profile like `kraken`).

## Reporting cadence

When summarizing cron work for the user, structure it as:

1. Total ticks / completed / failed.
2. Substantive shifts (what changed, files touched).
3. Read-only audit shifts (what was verified).
4. Failed ticks with error class (429 vs other).
5. Net delta (tests pass/fail, files added/modified, open issues).
