# Hermes Plugin Backend — Pitfalls, Real Hook Payloads, and Verification

Session-derived notes from fleshing out the Abyss observability plugin backend
(`~/.hermes/plugins/abyss/`). Applies to any Python plugin backend
(`plugins/<id>/__init__.py` + `dashboard/plugin_api.py`).

## 1. Which copy of a plugin is live? (profile dirs are NEVER loaded)

Hermes discovers plugins only from the Hermes home:

- `hermes_cli/plugins.py::_collect_directory_manifests` scans
  `get_hermes_home()/plugins` (bundled `<repo>/plugins`, then user).
- `web_server.py::_discover_dashboard_plugins` scans
  `get_process_hermes_home()/plugins` for `dashboard/manifest.json`.

Copies under `~/.hermes/profiles/<name>/plugins/` or
`~/.hermes/profiles/<name>/desktop-plugins/` are stale leftovers from a move
or rename — the loader never scans them. **Delete them; never edit or sync
them.** When two copies exist, check the loader source (above) to confirm
which one is live before editing.

Desktop UI is single-file: the loader evaluates `plugin.js` as a Blob URL so
relative imports (`./activity-feed.js`) cannot resolve. Extra split files next
to `plugin.js` are orphans — delete them, don't maintain them.

## 2. FastAPI `request.body()` is a coroutine — must be awaited

The classic silent failure: `dashboard/plugin_api.py` reads the body without
awaiting, so `isinstance(raw, bytes)` is always False and every POST body
parses as `{}`. Endpoints appear to work (they return 200) while dropping all
input.

```python
async def _json_body(request: Request) -> dict:
    try:
        raw = await request.body()
        if isinstance(raw, (bytes, bytearray)) and raw:
            return json.loads(raw.decode("utf-8") or "{}")
    except Exception:
        pass
    return {}
```

Handlers that read the body must be `async def`.

## 3. Real Hermes hook payloads (verified from source)

Design handler signatures from these, not from docstring guesses:

### post_tool_call — `model_tools.py::_emit_post_tool_call_hook`
```python
tool_name, args, result, task_id, session_id, tool_call_id,
turn_id, api_request_id, duration_ms, status, error_type,
error_message, middleware_trace
```
Use `status == "error"` / `error_type` / `error_message` / `duration_ms` for
structured signal detection instead of only grepping result text.

### pre_llm_call
```python
session_id, user_message, conversation_history, is_first_turn, model, platform
```
NOTE: `prompt` is NOT passed — use `user_message`.

### post_llm_call — fired by `agent/turn_finalizer.py`
```python
session_id, task_id, turn_id, user_message, assistant_response,
conversation_history, model, platform
```
NOTE: `result` is NOT passed — use `assistant_response` (for result preview
and vague-reply detection).

### pre_tool_call
```python
tool_name, args, task_id, session_id, tool_call_id, turn_id
```

### on_session_end
```python
session_id, task_id, turn_id, completed, failed, interrupted,
turn_exit_reason, model, platform
```

Always keep `**_: Any` on handlers so extra kwargs never crash the hook.

## 4. Isolated backend test recipe (no live-DB pollution)

The plugin computes its data dir from `HERMES_PROFILE_HOME` at import time.
Point it at a temp dir before importing, then exercise everything:

```python
import os, sys, tempfile
os.environ["HERMES_PROFILE_HOME"] = tempfile.mkdtemp(prefix="plug-test-")
os.environ["ABYSS_RETENTION_DAYS"] = "365"  # disable auto-prune in tests
sys.path.insert(0, str(Path(__file__).resolve().parent))
import __init__
from __init__ import _init_db, handle_request, ...
```

Reset tables between test groups by deleting rows + `sqlite_sequence`.

## 5. Verify the router exactly as Hermes mounts it

The web server imports `dashboard/plugin_api.py` via
`importlib.util.spec_from_file_location` and expects a `router` attribute:

```python
import importlib.util
from pathlib import Path
api_path = Path("dashboard/plugin_api.py").resolve()
spec = importlib.util.spec_from_file_location("abyss_plugin_api", api_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
assert hasattr(mod, "router")
routes = sorted({getattr(r, "path", "?") for r in mod.router.routes})
```

Then hit it in-process with FastAPI TestClient:

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()
app.include_router(mod.router, prefix="/api/plugins/abyss")
client = TestClient(app)
r = client.post("/api/plugins/abyss/activity", json={...})  # proves body path
```

Unknown paths return FastAPI's own HTTP 404 (not a JSON `{"code": 404}`),
because the router has no such route — assert on `r.status_code == 404`.
