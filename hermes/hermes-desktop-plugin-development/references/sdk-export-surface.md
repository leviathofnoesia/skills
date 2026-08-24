# @hermes/plugin-sdk — Verified Export Surface

Source of truth: `apps/desktop/src/sdk/index.ts` (Hermes source tree). Verified
during a live debugging session (Aug 2026) against the failing error
`The requested module 'blob:file:///...' does not provide an export named
'TabsContent'`.

The runtime loader (`apps/desktop/src/contrib/runtime-loader.ts`) rewrites
`@hermes/plugin-sdk` imports to a shim blob that re-exports ONLY keys present
on the SDK namespace (`apps/desktop/src/sdk/runtime.ts`). A name that isn't
exported throws at load time — the plugin fails to register and you get a
`Plugin "X" failed to load` toast. This is a HARD failure, not a warning.

## Core

- `host` — object: `host.state.*` (readonly atoms: activeSessionId, cwd,
  gateway, model, profile, viewport), `host.notify`, `host.notifyError`,
  `host.logs`, `host.navigate(path)`, `host.onEvent(type, cb)`,
  `host.restartGateway`, `host.status`, `host.request(method, params)`
- `ctx` — PluginContext (from `apps/desktop/src/contrib/plugin.ts`):
  `ctx.rest(path, {method, body, timeoutMs})`, `ctx.register(contrib)`,
  `ctx.register_command`, `ctx.register_hook`, `ctx.storage`, `ctx.i18n`,
  `ctx.os`
- `cn` — classname util
- `icons` — `export * as icons` (lucide icon set)

## State / data layer

- `atom`, `computed` (nanostores), `useValue` (nanostores/react)
- `useQuery`, `useMutation`, `useQueryClient` (TanStack Query, shared client)
- `queryClient`

## UI components (verified exports)

Button, Badge, Checkbox, Codicon, ConfirmDialog, ContextMenu (+ Content, Item,
Separator, Trigger), CopyButton, DecodeText, Dialog (+ Content, Description,
Footer, Header, Title, Trigger), DropdownMenu (+ Content, Item, Separator,
Trigger), EmptyState, ErrorState, FadeScroll, GlyphSpinner, Input, Kbd,
KbdGroup, Loader, LogView, Popover (+ Content, Trigger), ScrollArea,
SearchField, SegmentedControl, Select (+ Content, Item, Trigger, Value),
Separator, Skeleton, StatusDot, Switch, **Tabs, TabsList, TabsTrigger**,
Textarea, Tip, Tooltip (+ Content, Provider, Trigger), ModelCatalogMenu,
Contribute, useGrabScroll.

**NOT exported:** `TabsContent` (biggest trap — render active content
conditionally yourself), `StatusbarItem`/`TitlebarTool` (types only).

## Variant whitelists (cva-defined, unknown values render UNSTYLED silently)

### Badge
- variants: `default | muted | warn | destructive | outline`
- sizes: `default | xs`
- Common mistaken values: `subtle`, `success`, `warning`, `error`, `sm`.
  Map: subtle→outline, success→default, warning→warn, error→destructive.

### Button
- variants: `default | destructive | outline | secondary | ghost | link | text | textStrong`
- sizes: `default | xs | sm | lg | inline`
- Common mistaken value: `primary` (use `default`).

## Contribution areas (ctx.register `area` values)

- `'panes'` — dockable layout pane (`data: { placement: 'left'|'right'|'bottom'|'main', width }`)
- `'routes'` — full-page route (`data: { path }`)
- `'sidebarNav'` — sidebar nav item (`data: { path, label, codicon }`)
- `'palette'` — command palette entry (`data: { label, icon }`, `onSelect`)
- `'statusBar.left'` / `'statusBar.right'` — statusbar chips (render fn)
- `'titleBar.left'` / `'titleBar.center'` / `'titleBar.right'`
- `'themes'` (THEMES_AREA), keybinds (KEYBINDS_AREA), composer areas

Constants: `PANES_AREA = 'panes'`, `STATUSBAR_AREAS = {left, right}`,
`TITLEBAR_AREAS = {center, left, right}`, `PALETTE_AREA`, `ROUTES_AREA`,
`SIDEBAR_NAV_AREA`, `KEYBINDS_AREA`, `THEMES_AREA`.

## Import discipline

Runtime plugins may import ONLY:
- `@hermes/plugin-sdk`
- `react` (app singleton React — hooks: useEffect, useState, useMemo,
  useCallback, useRef)
- `react/jsx-runtime` (`jsx`, `jsxs` — JSX syntax does NOT compile)

Anything else bare (e.g. `lodash`) throws
`unsupported import: X — runtime plugins may only import @hermes/plugin-sdk and react`
at load time. Relative imports of local files also fail (Blob URL has no path
context) — inline everything into one `plugin.js`.

## Load-time failure symptoms

| Symptom | Cause | Fix |
|---|---|---|
| `does not provide an export named 'X'` | Imported name not on SDK namespace | Check sdk/index.ts; drop/rename the import |
| `unsupported import: X — ...` | Bare import other than SDK/react | Remove or inline the dependency |
| Plugin missing from Settings list | Wrong folder (profile path vs hermes home) | Move to `~/.hermes/desktop-plugins/<id>/`, click Rescan |
| Toast `Plugin "X" failed to load` + blob URL | Any load-time throw (import, syntax, bad export) | Read the toast's second line for the real error |

## Verification commands

```bash
# ESM syntax check without executing (catches syntax errors before reload)
node --input-type=module --check < path/to/plugin.js

# List all variant literals used in a plugin (audit against whitelists)
grep -oE "variant: '[^']+'" plugin.js | sort | uniq -c
```
