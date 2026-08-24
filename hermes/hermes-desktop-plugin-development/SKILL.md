---
name: hermes-desktop-plugin-development
description: Build desktop UI plugins for the Hermes Agent desktop app.
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, plugins, desktop, electron, react, typescript]
    related_skills: [hermes-agent]
---

# Hermes Desktop Plugin Development

Build UI plugins (panes, statusbar chips, palette commands, sidebar nav, full-page routes) that load at runtime into the Hermes desktop app. A plugin is a single plain-JavaScript ESM file under `<hermes home>/desktop-plugins/<name>/plugin.js` — no build step, no repo changes, hot-reloads on save.

## When to Use

- The user asks for a new desktop UI element (a pane, a statusbar widget, a dashboard, a command) without modifying the app itself.
- You want to surface data you compute (via gateway RPC or a Python backend) inside the desktop app.
- Extending Hermes desktop with custom dashboards, widgets, or sidebar panels.

**Don't use for:** CLI-only agent plugins (tools/hooks) — that's the Python `plugins/` directory and `hermes_cli/plugins.py` system. This skill is for the Electron desktop app UI layer only.

## Prerequisites

- The Hermes desktop app must be running (plugins don't load in CLI/gateway-only mode).
- Write access to `~/.hermes/desktop-plugins/<id>/` — this is the **Hermes home** path,
  NOT the profile directory. The runtime loader resolves `desktop.desktopPluginsRoot()`
  to `~/.hermes/`, so profile-level paths like `~/.hermes/profiles/<name>/desktop-plugins/`
  will NOT be discovered. See Pitfalls.
- If using a Python backend: `~/.hermes/plugins/<id>/dashboard/plugin_api.py` with a `manifest.yaml`.

## File Structure

```
~/.hermes/desktop-plugins/<plugin-id>/plugin.js   ← the UI plugin (required)
~/.hermes/plugins/<plugin-id>/                  ← Python backend (optional)
├── manifest.yaml
└── dashboard/
    └── plugin_api.py                            ← handle_request(method, path, params, body)
```

## Key Architecture

There are **two plugin systems** in Hermes:

1. **Desktop UI plugins** (`desktop-plugins/`) — JavaScript ESM files loaded by the Electron renderer. Access via `@hermes/plugin-sdk`.
2. **Python backend plugins** (`plugins/`) — Python packages with `plugin.yaml` + `__init__.py`. Provide tools, hooks, and REST API backends.

A UI plugin can call a Python backend via `ctx.rest('/path', { method, body })` → backend receives at `GET/POST /api/plugins/<id><path>` → Python's `handle_request(method, path, params, body)`.

## Import Surface

Only these specifiers resolve in runtime plugins (everything else fails):
- `@hermes/plugin-sdk` — the SDK shim (host, ctx, UI components, React Query, atoms, i18n)
- `react` — the app's singleton React
- `react/jsx-runtime` — `jsx`/`jsxs` for building UI (NOT JSX syntax — the file loads uncompiled)

You can also use relative imports (`./subcomponent.js`) for multi-file plugins. Both the main file and sub-components import from `@hermes/plugin-sdk`.

## SDK Export Surface (VERIFY against sdk/index.ts, don't guess)

Runtime plugin failures usually come from importing a name the SDK does not export, or passing a variant the component does not accept. The loader rewrites `@hermes/plugin-sdk` to a shim blob that re-exports ONLY the keys that exist on the SDK namespace — importing anything else throws `The requested module 'blob:...' does not provide an export named 'X'` at load time, and the plugin never registers (toast: "Plugin X failed to load").

**Verified export gotchas (from `apps/desktop/src/sdk/index.ts`):**

- `Tabs`, `TabsList`, `TabsTrigger` are exported — **`TabsContent` is NOT**. Do not import it. Render active content yourself via `activeTab === 'x' ? <A/> : <B/>` conditional logic inside a plain div.
- `Badge` variant whitelist: `default | muted | warn | destructive | outline`. **`subtle`, `success`, `warning`, `error` do NOT exist** — they render unstyled (silent, no error). Map: subtle→outline, success→default, warning→warn, error→destructive.
- `Button` variant whitelist: `default | destructive | outline | secondary | ghost | link | text | textStrong`. **`primary` does NOT exist** — use `default` for the primary look.
- `Badge` sizes: `default | xs` (NOT `sm`). `Button` sizes: `default | xs | sm | lg | inline`.
- **`EmptyState` takes ONLY `{title, description, className}` — there is NO `icon` prop.** Passing `icon:` is silently dropped (no error). For an icon + action empty state use `ErrorState` (`{title, description?, icon?, children?}` — children render as an actions row) or build your own centered block.
- `ErrorState` is the canonical error surface (`title`, `description`, optional `icon` node, optional actions as children). `SearchField` (`{placeholder, value, onChange, hints?, ariaLabel?, onClear?}`) is the canonical search input — prefer it over hand-rolled `<input>` + search icon. `Select`/`SelectContent`/`SelectItem`/`SelectTrigger`/`SelectValue` are exported (Radix-style, use `value` + `onValueChange` on the root). `GlyphSpinner` (`{ariaLabel, className, spinner?}`) beats raw `animate-spin` Codicons.
- Full verified export list is in `references/sdk-export-surface.md` — load it with `skill_view(name='hermes-desktop-plugin-development', file_path='references/sdk-export-surface.md')` before writing component code.
- Source-anchored contracts (rest parsed-JSON bridge, params-less options, EmptyState/ErrorState/SearchField props, canvas var() colors, live `--ui-*` class set) are in `references/verified-contracts.md`.

## Plugin Shape

```js
import { cn, host, Button, Codicon } from '@hermes/plugin-sdk'
import { jsx, jsxs } from 'react/jsx-runtime'

export default {
  id: 'my-plugin',           // must match folder name
  name: 'My Plugin',
  defaultEnabled: false,    // opt-in; appears in Settings → Plugins
  register(ctx) {
    ctx.i18n.register({ en: { title: 'My Plugin' } })

    // Layout pane (right sidebar by default, user can drag)
    ctx.register({
      id: 'my-pane',
      area: 'panes',
      title: 'my plugin',
      data: { placement: 'right', width: '300px' },
      render: () => jsx(MyComponent, { ctx })
    })

    // Full-page route
    ctx.register({
      id: 'my-page',
      area: 'routes',
      data: { path: '/my-plugin' },
      render: () => jsx(MyPage, { ctx })
    })

    // Sidebar nav item
    ctx.register({
      id: 'my-nav',
      area: 'sidebarNav',
      data: { path: '/my-plugin', label: 'My Plugin', codicon: 'dashboard' }
    })

    // Command palette entry
    ctx.register({
      id: 'my-cmd',
      area: 'palette',
      data: { label: 'Open My Plugin', icon: 'dashboard' },
      onSelect: () => host.navigate('/my-plugin')
    })

    // Status bar chip
    ctx.register({
      id: 'my-chip',
      area: 'statusBar.right',
      order: 100,
      title: 'My Plugin',
      render: () => jsx(MyChip, { ctx })
    })
  }
}
```

## ctx.rest() — Backend API Calls

When your plugin ships a Python backend (`plugin_api.py`), call it via:

```js
// GET /api/plugins/my-plugin/activity?limit=50
const data = await ctx.rest('/activity?limit=50', { method: 'GET', timeoutMs: 5000 })

// POST /api/plugins/my-plugin/activity
await ctx.rest('/activity', { method: 'POST', body: JSON.stringify({action: 'test'}) })
```

The Python backend receives via `handle_request(method, path, params, body)`.
**CRITICAL — there is NO `params` option on `ctx.rest()`** (verified in `apps/desktop/src/hermes.ts`: `PluginRestOptions` = `method`/`body`/`upload`/`timeoutMs` only). Passing `{ params: { category: 'cron' } }` is silently dropped — the query string never reaches the backend, so filters/limits/session IDs "look wired" but always hit defaults. Encode query strings IN the path: `ctx.rest('/activity?limit=50&category=cron', { method: 'GET' })`; FastAPI routes receive them as normal query params.
**CRITICAL — `ctx.rest()` resolves the PARSED JSON BODY directly, NOT a Response.** The IPC bridge (`electron/main.ts` `fetchJson`) does `JSON.parse(text)` before resolving, so `await ctx.rest('/activity')` returns the array/object itself. Do NOT chain `.json()` — `(await ctx.rest(...)).json()` throws `TypeError: r.json is not a function`, and if that call sits inside a `.catch`-swallowed fetch, the whole view silently renders empty with no error. This is the #1 "UI shows nothing, no error" bug in real plugins. Kanban's own `api.ts` (`call<T>` → `rest<T>`) consumes results directly — copy that pattern. Same for the socket fallback: responses arrive parsed.
**Pitfall:** `ctx.socket()` is a no-op on OAuth remotes — always keep a polling fallback.

## Procedure

1. Create `~/.hermes/desktop-plugins/<id>/plugin.js` (folder name = plugin id).
2. If using a Python backend: create `~/.hermes/plugins/<id>/manifest.yaml` and `~/.hermes/plugins/<id>/dashboard/plugin_api.py`.
3. Enable the Python backend in config: `hermes config set plugins.enabled '["<id>"]'`.
4. Write UI with `jsx()` calls (not JSX syntax). Import only `@hermes/plugin-sdk`, `react`, `react/jsx-runtime`.
5. Save the file — the app hot-reloads on file change. Fallback: click "Rescan" in Settings → Desktop plugins, or `⌘K` → "Reload desktop plugins".
6. **Toggle the plugin ON** in Settings → Desktop plugins (plugins default to disabled/off).
7. Check for error toasts. Fix and re-save.
8. Verify: `ctx.rest()` calls reach the Python backend (check terminal/logs for errors).

## Pane Placement

- `placement: 'left'|'right'|'bottom'|'main'` — semantic role; pane stacks (tabs) with existing panes of that role.
- `dock: { pane: 'workspace'|'sessions'|'terminal'|'files'|'review'|'logs', pos: 'top'|'bottom'|'left'|'right'|'center' }` — land on a specific edge instead of stacking. User can still drag afterward.

## Theming

- Panes already sit on the app's editor background — leave the background alone.
- Use theme variables: `var(--ui-text-secondary)`, `var(--ui-text-tertiary)`, `var(--ui-stroke-secondary)`, `var(--ui-accent)`.
- Tailwind-style classes also work: `text-(--ui-text-tertiary)`, `bg-(--ui-bg-tertiary)`, `border-(--ui-stroke-secondary)`.
- Never hardcode colors (`#000`, `black`, `rgb(...)`).

## Pitfalls

- **JSX syntax won't parse** — the file loads uncompiled. Use `jsx('div', { children: ... })` from `react/jsx-runtime`.
- **Relative imports DON'T work** — the runtime loader (runtime-loader.ts) evaluates plugin.js as a Blob URL via `import()`. The blob has no path context, so specifiers like `./subcomponent.js` fail to resolve at runtime. **Always use a single self-contained plugin.js file** with all components inlined. Only `@hermes/plugin-sdk`, `react`, and `react/jsx-runtime` are allowed.
- **"does not provide an export named 'X'"** — you imported a name the SDK doesn't export (e.g. `TabsContent`). The runtime loader shims `@hermes/plugin-sdk` to only the names that exist on the SDK namespace, so a wrong import throws at load and the plugin silently never appears (toast: `Plugin "X" failed to load`). Fix: check `apps/desktop/src/sdk/index.ts` export list before importing UI components, and never invent variants.
- **Wrong plugin path** — desktop plugins must go in `~/.hermes/desktop-plugins/<id>/plugin.js` (the Hermes home directory). Placing them in `~/.hermes/profiles/<profile>/desktop-plugins/` will NOT be discovered by the runtime loader, which uses `desktop.desktopPluginsRoot()` to resolve to the Hermes home. If your plugin doesn't appear, check the path first, then click "Rescan" in Settings → Desktop plugins.
- **Stale closures in handlers** — read state imperatively (`$atom.get()`) in handlers, never from render closures.
- **Canvas panes need ResizeObserver** — panes resize constantly; track container size and update canvas width/height attributes.
- **Canvas colors: resolve CSS vars to computed values, never pass `var()` strings** — `ctx.fillStyle = 'var(--ui-accent)'` is silently ignored by canvas (it parses the value as a color; var() is not a color). Read real values first: `getComputedStyle(document.documentElement).getPropertyValue('--ui-green').trim()` and cache them (re-read on theme change). Same for strokeStyle and gradients.
- **write_file 8K token limit** — large plugin files (>8K tokens) will time out on write. Split into multiple smaller files and use `patch` for edits.
- **ctx.socket is no-op on OAuth** — remote gateway connections can't use WebSocket plugin APIs; always implement a polling fallback with `ctx.rest()`.
- **Plugin defaults to disabled** — after placing plugin.js, the toggle in Settings → Desktop plugins is OFF by default. You must toggle it ON, or it won't load.
- **Profile plugin dirs are NEVER loaded — delete, don't sync** — plugins are discovered only from the Hermes home: `~/.hermes/plugins/<id>/` (Python backend) and `~/.hermes/desktop-plugins/<id>/plugin.js` (UI). Copies under `~/.hermes/profiles/<name>/plugins/` or `.../desktop-plugins/` are dead weight from a move/rename — the loader never scans them. When you find one, delete it; don't edit or sync it (user-confirmed convention). Before editing, confirm which copy is live: `hermes_cli/plugins.py::_collect_directory_manifests` scans `get_hermes_home()/plugins`; `web_server.py::_discover_dashboard_plugins` scans `get_process_hermes_home()/plugins`.
- **FastAPI `request.body()` is a coroutine — must be awaited** — in `dashboard/plugin_api.py`, `isinstance(await-less request.body(), bytes)` is always False, so every POST body silently parses as `{}` and your endpoints appear "working" while dropping all input. Always `async def` handlers and `await request.body()`.
- **Real hook payloads differ from what you'd assume** — `post_llm_call` carries `assistant_response`/`user_message` (NOT `result`/`prompt`); `post_tool_call` carries structured `status`/`error_type`/`error_message`/`duration_ms`. Design handlers from the real payloads (see `agent/turn_finalizer.py`, `model_tools.py::_emit_post_tool_call_hook`). Full payload table + isolated-test recipe + router-verification snippet: `references/plugin-backend-pitfalls.md`.
- **Plugin classes that "do nothing" — verify against the compiled CSS inventory** — Tailwind v4 compiles utilities at build time and `plugin.js` (runtime Blob) is never scanned, so a class renders ONLY if it already exists in the host's compiled stylesheet (`apps/desktop/dist/assets/index-*.css`). Silent no-ops seen in the wild: `grid-cols-7`, `bg-(--ui-bg-primary)`, `bg-(--ui-bg-secondary)`, `ring-(--ui-accent)`, `bg-blue-500`-style palette dots, `ring-inset`. **Careful — the inverse trap is real too**: `hover:bg-(--ui-bg-tertiary)` and `placeholder:text-(--ui-text-tertiary)` ARE live (the app source uses them); only ~100 `--ui-*` arbitrary classes exist, and they're a fixed set — the color dots `bg-(--ui-blue|purple|orange|cyan|red)` are NOT generated even though `--ui-blue` etc. exist as variables. When a color utility is missing, use inline `style={{ color: 'var(--ui-blue)' }}` — theme-driven and always works. Run `scripts/scan-tailwind-classes.js <path-to-index-*.css>` for the exact inventory before writing markup. A missing `grid-cols-N` class has a distinctive failure mode: the grid falls back to a single column, so e.g. a 7-tab bar renders as a VERTICAL stack that looks like a dead menu — check the class exists before assuming the component is broken.
- **React error #310: hook after early return kills the WHOLE page** — every hook (`useState`/`useEffect`/`useMemo`/`useCallback`/`useRef`) must be declared BEFORE any conditional `return` in a component. A `useMemo` declared after `if (loading) return ...` runs only on the data-loaded render — the hook count changes between renders and React throws #310 "Rendered more hooks than during the previous render". Because plugin views render inside a route error boundary, the symptom is the ENTIRE dashboard page replaced by a generic "failed to render" + Retry screen, not a view-local error. This is the #1 crash pattern in dashboard-style plugins with loading states. When a page "failed to render", scan for hooks after early returns first (brace-aware script: `scripts/check-hook-order.py <plugin.js>`). Same class: never put hooks inside `.map()` callbacks or conditionals.
- **CSS bundle hash changes on self-update — re-verify every session** — the host's compiled stylesheet lives at `apps/desktop/release/win-unpacked/resources/app.asar.unpacked/dist/assets/index-*.css` and the hash in the filename changes whenever the desktop app self-updates (`index-BxUSlQHk.css` → `index-CH_NsZp_.css`). A class inventory verified against an old bundle is worthless after an update; re-locate the current `index-*.css` before trusting any Tailwind utility, and re-check `grid-cols-N`/`--ui-*` classes against the current file. (Also: the plugin's own backend `__init__.py` changes need a gateway/backend restart to serve — the web server imports plugin code at mount time; the UI plugin.js hot-reloads, the Python backend does not.)
- **grep substring checks MISS dead classes — match exact selector boundaries** — `grep 'ml-3' index.css` succeeds if `.ml-3\.5{...}` exists, so plain `ml-3` can be dead while the grep says it's live. The host app drops utilities it stops using (simple spacing classes like `m-1`/`ml-3` have silently vanished between self-updates — found dead in Abyss in Aug 2026), and they render as silent no-ops: intended margin/padding disappears, absolutely-positioned children (canvas glyphs at `left:-19px` etc.) shift. Verify with exact-boundary regex: `grep -oE '\.ml-3[^a-zA-Z0-9_-]' index.css` (empty = dead), and remember Tailwind escapes `.` `(` `)` `:` in selectors (`.gap-1\.5`, `.bg-\(--ui-bg-tertiary\)`). Fix dead simple spacing utilities with inline styles (`style: { margin: 4 }` / `{ marginLeft: 12 }`) per the DESIGN.md inline-style convention.
- **Host `Tabs` root won't grow; pin the tab bar with flex** — the host `Tabs` component is `flex flex-col gap-2` with NO flex-grow, so inside an `h-full` column a tall view (activity feed) pushes the TabsList out of the visible area. Fix: `className: 'flex-1 min-h-0'` on the Tabs root, `flex-1 min-h-0 overflow-hidden` on the content wrapper, and `shrink-0` on the TabsList. Also the base TabsList is `justify-center` — combined with `overflow-x-auto` that's the classic centered-overflow clipping bug (leftmost tabs unreachable). Override with `justify-start`; for equal-specificity utilities the rule appearing LATER in the compiled CSS wins, so verify position if unsure.
- **Full-page routes have no back affordance — add a close button and make chips toggle** — `host.navigate('/abyss')` just sets the hash; a full-page route has no built-in close/back. If a statusbar chip or palette command opens the route, add an explicit ✕ button in the page's masthead calling `host.navigate('/')`, and make the chip itself a toggle: `host.navigate((window.location.hash || '').startsWith('#/abyss') ? '/' : '/abyss')`. Otherwise the user is trapped on the plugin page with no obvious way back.
- **Select value must exist among items or the trigger shows the placeholder** — a drill-in/preset can set a `Select` value that isn't in the fetched item list (e.g. deep/old session outside `/trace?limit=50`). Radix Select logs a dev warning and the trigger renders the `SelectValue` placeholder instead of the selected label, so the operator can't see what they drilled into; with an empty item list the surrounding view may also collapse to its EmptyState even though the preset's own data loaded. Fix: build the item list from state and append a synthetic item carrying the current value (`{ ...item, synthetic: true }`) when it's missing; label it `(drill)` and gate Empty/Error early-returns on "genuinely nothing selected" so a preset keeps the view alive.

## Verification

- **`node --check plugin.js` does NOT validate ESM syntax — use `node --input-type=module --check < plugin.js`.** The file loads in Electron as a Blob-URL ES module (`import()`), but `node --check` on a `.js` file without a `"type":"module"` package.json parses it as CommonJS (or weak auto-detect) and returns exit 0 even on a broken ESM file. Real failure: `node --input-type=module --check < plugin.js` (reproduces what the loader parses) or `node -e "import('file:///<abs>/plugin.js').then(...)"` (syntax-only; `Cannot find package '@hermes/plugin-sdk'` is expected outside Electron and does NOT mean the file is broken). Abyss tick-39: a stray `)` survived every CJS `node --check` and the whole plugin silently failed to load until the ESM check exposed it.
- Before trusting any Tailwind utility in plugin.js, confirm it exists in the compiled host CSS: `node scripts/scan-tailwind-classes.js <hermes-home>/hermes-agent/apps/desktop/dist/assets/index-*.css | grep <class>`.
- Plugin appears in Settings → Desktop plugins list (if not, check path is `~/.hermes/desktop-plugins/`, click "Rescan").
- Toggle is ON (plugins default to disabled after creation).
- No error toast ("Plugin <name> failed to load").
- Plugin's UI appears after reload (hot reload or ⌘K → "Reload desktop plugins").
- For panes: the new zone is visible and draggable.
- `ctx.rest()` calls reach the Python backend (check terminal/logs for errors).
- `/<command>` slash command works if Python backend is enabled.

## Discovery: How to Learn the Real API

When the documentation is incomplete, read the source directly:
- `apps/desktop/src/contrib/plugin.ts` — PluginContext interface (rest, storage, i18n, os, register)
- `apps/desktop/src/contrib/plugins-store.ts` — inventory + activate/deactivate lifecycle
- `apps/desktop/src/contrib/runtime-loader.ts` — how disk plugins load, fs-watching, hot-reload
- `apps/desktop/src/sdk/runtime.ts` — the import shim that maps `@hermes/plugin-sdk` → live SDK
- `apps/desktop/src/hermes.ts` — `pluginRest()` function (the actual HTTP bridge)
- `hermes_cli/plugins.py` — Python plugin system (tools, hooks, middleware registration)
- `hermes_cli/plugins_cmd.py` — CLI subcommands for plugin management
- Built-in example plugins: `apps/desktop/src/plugins/*/plugin.tsx`
