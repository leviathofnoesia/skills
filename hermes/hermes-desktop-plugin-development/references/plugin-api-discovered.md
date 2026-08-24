# Mission Control Plugin — API Discovery Notes

## Source Code Paths (Hermes repo)

The desktop plugin SDK surface is defined in these files:

```
apps/desktop/src/contrib/plugin.ts          — PluginContext + HermesPlugin interface
apps/desktop/src/contrib/plugins-store.ts   — pluginActive(), publishPlugin()
apps/desktop/src/contrib/runtime-loader.ts  — loadRuntimePlugin(), scanDiskPlugins()
apps/desktop/src/contrib/plugins.ts         — discoverBundledPlugins(), watchRuntimePlugins()
apps/desktop/src/sdk/runtime.ts             — sdkImportMap() — maps @hermes/plugin-sdk to shim
apps/desktop/src/sdk/index.ts               — the actual SDK exports
apps/desktop/src/hermes.ts                  — pluginRest() — the HTTP bridge to Python backend
```

## PluginContext Interface (from plugin.ts)

```typescript
export interface PluginContext {
  readonly source: string              // e.g. 'plugin:my-plugin'
  register: (c: PluginContribution) => () => void
  registerMany: (cs: PluginContribution[]) => () => void
  onDispose: (fn: () => void) => void
  rest: <T>(path: string, opts?: PluginRestOptions) => Promise<T>      // → /api/plugins/<id><path>
  socket: (path: string, onMessage: (data: unknown) => void) => () => void  // WebSocket, no-op on OAuth
  os: PluginOs                              // notify, openExternal, revealPath, writeClipboard
  storage: PluginStorage                    // namespaced get/set/remove
  i18n: PluginI18n                          // register, t()
}
```

## PluginRestOptions

```typescript
interface PluginRestOptions {
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE'
  body?: string
  upload?: { file: string }                // for file uploads
  timeoutMs?: number
  signal?: AbortSignal
  params?: Record<string, string>          // query string parameters
}
```

## pluginRest() implementation (from hermes.ts)

```typescript
export async function pluginRest<T>(pluginId: string, path: string, opts: PluginRestOptions = {}): Promise<T> {
  const suffix = pluginPathSuffix('pluginRest', path)
  return window.hermesDesktop!.api<T>({
    path: `/api/plugins/${pluginId}${suffix}`,
    method: opts.method,
    body: opts.body,
    upload: opts.upload,
    timeoutMs: opts.timeoutMs,
    ...profileScoped()
  })
}
```

Key insight: `ctx.rest('/activity', { method: 'GET' })` translates to `GET /api/plugins/<id>/activity`.
The Python backend's `handle_request(method, path, params, body)` receives `method='GET'`, `path='/activity'`.

**CRITICAL FIX**: `ctx.rest()` calls with `params` must pass them as `params` key, NOT appended to the URL path. Example:
```js
// CORRECT — params become query string:
ctx.rest('/activity', { method: 'GET', timeoutMs: 5000, params: { category: 'tool', limit: 50 } })

// WRONG — params in path don't work:
ctx.rest('/activity?category=tool', { method: 'GET' })
```

## Python Plugin Manifest Format

Python backend plugins use `manifest.yaml` (not JSON) and need `api` field pointing to the Python file:

```yaml
id: abyss
name: Abyss Dashboard
description: Raindrop-style observability plugin
version: "1.0.0"
api: dashboard/plugin_api.py
entry: ../desktop-plugins/abyss/plugin.js
```

The `entry` field is relative to the `manifest.yaml` location (`~/.hermes/plugins/<id>/`), so `../desktop-plugins/<id>/plugin.js` resolves to `~/.hermes/desktop-plugins/<id>/plugin.js`.

## Enabling Python Backend Plugin

```bash
# Add to config.yaml under plugins.enabled
hermes config set plugins.enabled '["abyss"]'
```

## Runtime Plugin Loading (from runtime-loader.ts)

1. Scans `<hermes home>/desktop-plugins/<name>/` for `plugin.js`
2. Reads file content, rewrites import specifiers (`@hermes/plugin-sdk` → shim blob URL)
3. Validates: only imports `@hermes/plugin-sdk`, `react`, and `react/jsx-runtime` are allowed — relative imports (`./sub.js`) are NOT supported because the plugin source is evaluated as a Blob URL with no path context. All plugin code must be in a single `plugin.js` file.
4. Blob URL → dynamic `import()` → validate default export has `.id` and `.register()`
5. Creates `PluginContext` via `createPluginContext(pluginId, onDispose)`
6. Calls `plugin.register(ctx)` — this is where you wire contributions
7. Hot-reloads on file save (fs.watch via Electron)

## Desktop Plugin File Location — THE #1 ISSUE

**The desktop plugins directory is at `~/.hermes/desktop-plugins/`, NOT at the profile level.**

The runtime loader uses `desktop.desktopPluginsRoot?.()` (an Electron IPC call) which resolves to the **Hermes home directory** (`~/.hermes/`), not the profile directory (`~/.hermes/profiles/<profile-name>/`).

```
WRONG (profile-level — plugins won't appear):
  ~/.hermes/profiles/kraken/desktop-plugins/<id>/plugin.js

CORRECT (Hermes home — plugins auto-discover):
  ~/.hermes/desktop-plugins/<id>/plugin.js
```

The settings pane (Settings → Desktop plugins) shows plugins found at the Hermes home level. The description text confirms: "Bundled or dropped into the desktop-plugins folder."

**If your plugin doesn't appear after creating files:**
1. Verify the file is at `~/.hermes/desktop-plugins/<id>/plugin.js`
2. Click the **"Rescan"** button in Settings → Desktop plugins
3. Or use `⌘K` → "Reload desktop plugins"
4. Toggle the plugin ON in the settings UI (default is disabled/off)

## Python Backend File Location

The Python backend goes at `~/.hermes/plugins/<id>/`:
```
~/.hermes/plugins/<id>/
├── __init__.py           ← register(ctx) + handle_request()
├── plugin.yaml           ← declares hooks + commands
├── manifest.yaml         ← api path + desktop entry path
└── dashboard/
    └── plugin_api.py     ← REST layer
```

## Available SDK Exports

From `sdk/index.ts`, the `@hermes/plugin-sdk` provides:
- **State**: `host`, `host.state.*` (activeSessionId, cwd, gateway, model, profile, viewport)
- **Data**: `useQuery`, `useMutation`, `useQueryClient`, `queryClient`, `atom`, `computed`
- **UI components**: Button, Input, Textarea, Select*, Switch, Checkbox, SegmentedControl,
  Tabs*, Dialog*, DropdownMenu*, ContextMenu*, Popover*, Tip/Tooltip*, Badge, Kbd, SearchField,
  ScrollArea, Separator, Skeleton, GlyphSpinner, EmptyState, ErrorState, CopyButton, StatusDot,
  LogView, Codicon, DecodeText
- **Utils**: `cn`, `haptic`, `useValue`, `usePluginI18n`, `icons.*`
- **Area constants**: Need to check if `STATUSBAR_AREAS`, `PALETTE_AREA`, `KEYBINDS_AREA`,
  `ROUTES_AREA`, `SIDEBAR_NAV_AREA` are exported as constants or use string literals

## Area Names (from template + source)

Looking at the example plugins in `apps/desktop/src/plugins/*/`, areas use string literals:
- Panes: `area: 'panes'` with `data: { placement: 'right'|'left'|'bottom'|'main', width?, height? }`
- Status bar: `area: 'statusBar.right'` or `'statusBar.left'` with `order?: number`
- Palette: `area: 'palette'` with `data: { label, icon?, keywords?, run? }`
- Sidebar nav: `area: 'sidebarNav'` with `data: { path, label, codicon? }`
- Routes: `area: 'routes'` with `data: { path: '/my-plugin' }`
- Keybinds: `area: 'keybinds'`

## write_file Limitation

The `write_file` tool has an ~8K token limit on content size. Files larger than this will time out.
**Workaround**: Split large plugin files into smaller modules and use `patch` for incremental edits.

## Python Backend Plugin — Hooks + REST API

The Python backend plugin system (in `plugins/<id>/`) uses hooks via `ctx.register_hook()`:

```python
# plugins/<id>/__init__.py
def register(ctx):
    ctx.register_hook("pre_tool_call", on_pre_tool_call)
    ctx.register_hook("post_tool_call", on_post_tool_call)
    ctx.register_hook("pre_llm_call", on_pre_llm_call)
    ctx.register_hook("post_llm_call", on_post_llm_call)
    ctx.register_hook("on_session_start", on_session_start)
    ctx.register_hook("on_session_end", on_session_end)
    ctx.register_command("my-cmd", handler=handler_fn, description="...")
```

Hook handler signatures:
```python
def on_post_tool_call(tool_name="", args=None, result=None, 
                      task_id="", session_id="", tool_call_id="", **_):
    # Auto-record tool calls into your database
    ...

def on_session_start(session_id="", source="", **_):
    # Log session lifecycle
    ...
```

## Combined Desktop + Python Plugin Pattern

A single plugin can have BOTH a desktop UI (`desktop-plugins/<id>/plugin.js`)
AND a Python backend with hooks (`plugins/<id>/__init__.py`).
The desktop UI calls `ctx.rest()` → Python backend, while the Python hooks
automatically record activity. This is the recommended pattern for dashboard
plugins that need to auto-track agent behavior.

## plugin.yaml for Python Backend (with hooks)

```yaml
name: abyss
version: "1.0.0"
description: Raindrop-style observability plugin
hooks:
  - pre_tool_call
  - post_tool_call
  - pre_llm_call
  - post_llm_call
  - on_session_start
  - on_session_end
api: dashboard/plugin_api.py
```

## ctx.rest() Response Handling

**Important:** `ctx.rest()` returns a `Response` object (the Fetch API Response),
NOT a parsed JSON object. You must call `.json()` on it:

```js
// CORRECT:
const response = await ctx.rest('/activity', { method: 'GET', timeoutMs: 5000 })
const data = await response.json()

// WRONG (data is a Response, not parsed):
const data = await ctx.rest('/activity', { method: 'GET' })
```

## manifest.yaml vs plugin.yaml

- **Python backend**: `plugins/<id>/plugin.yaml` (YAML, declares hooks)
  + `manifest.yaml` (JSON or YAML, has `api` field for the Python file path)
- **Desktop UI only**: needs just `desktop-plugins/<id>/plugin.js`

## Enabling Both Layers

1. Place `plugin.js` in `desktop-plugins/<id>/` — auto-discovered by Electron
2. Place `plugin.yaml` + `__init__.py` in `plugins/<id>/` — enable with `hermes config set plugins.enabled '["<id>"]'`
3. The desktop UI calls `ctx.rest()` which bridges to the Python `handle_request()`
4. Click "Rescan" in Settings → Desktop plugins to force reload
5. Toggle the plugin ON in the settings UI (plugins default to disabled/off)

## Debugging Plugin Load Failures

If the plugin doesn't appear or fails to load:
1. Check Settings → Desktop plugins — is it listed? Is the toggle ON?
2. Look for error toasts: "Plugin <name> failed to load"
3. Check `runtime-loader.ts` validation:
   - Plugin must be a single `plugin.js` file (no relative imports)
   - Only `@hermes/plugin-sdk`, `react`, `react/jsx-runtime` allowed
   - Default export must have `.id` and `.register(ctx)` function
4. If editing files, hot-reload should trigger — if not, click "Rescan"
5. For Python backend: check terminal output for `handle_request()` errors
