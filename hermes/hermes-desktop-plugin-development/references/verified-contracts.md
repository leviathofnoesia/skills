# Verified Hermes desktop plugin contracts (source-anchored)

Where the hard-won contracts live in source, so a future session can re-verify in
seconds instead of re-deriving from symptoms. All paths relative to
`<hermes-agent repo>/apps/desktop/`.

## ctx.rest() resolves PARSED JSON, not a Response

- `electron/main.ts` — `ipcMain.handle('hermes:api', ...)` (~line 10605) calls
  `fetchJson(url, ...)` and returns its result.
- `fetchJson` (~line 4243) collects chunks and at the end does
  `resolve(JSON.parse(text))` (~line 4316). Errors reject with the HTTP status
  prefixed; a 2xx HTML body rejects with a clear "Expected JSON ... but got
  HTML" diagnostic.
- `src/hermes.ts` `pluginRest()` (~line 297) wraps `window.hermesDesktop.api<T>()`.
- Kanban's own consumer (`src/plugins/kanban/api.ts` `call<T>`) uses the result
  directly — never `.json()`.

Symptom if you get it wrong: `TypeError: r.json is not a function` inside a
`.catch`-swallowed promise → the view renders its empty state with no error.
Confirmed live in the incumbent Abyss plugin (every view was silently empty).

## PluginRestOptions has NO params field

- `src/hermes.ts` ~line 269: `{ method?, body?, upload?, timeoutMs? }` only.
- Query strings belong in the path: `/activity?limit=50&category=cron`.
- Kanban pattern: `withBoard(path, params)` builds `path?qs` via URLSearchParams
  (`src/plugins/kanban/api.ts` ~line 119).

## SDK component prop gaps (silently dropped)

- `EmptyState` (`src/components/ui/empty-state.tsx`): props are exactly
  `{ title, description?, className? }` — NO `icon`.
- `ErrorState` (`src/components/ui/error-state.tsx`): `{ title, description?,
  icon?, children? }` — children render as an actions row; default icon is a
  filled codicon error glyph.
- `SearchField` (`src/components/ui/search-field.tsx`): `{ placeholder, value,
  onChange, hints?, ariaLabel?, onClear? }`.
- `TabsContent` NOT exported (`src/sdk/index.ts` exports Tabs/TabsList/TabsTrigger only).

## Canvas does not resolve var() colors

- Canvas `fillStyle`/`strokeStyle`/gradient color stops parse the string as a
  color; `'var(--ui-green)'` is not a color → silently ignored, keeps previous
  value. Read computed values:
  `getComputedStyle(document.documentElement).getPropertyValue('--ui-green').trim()`.
- Theme vars that exist in `:root` of the compiled CSS (light+dark):
  `--ui-red #cf2d56/#e75e78`, `--ui-orange #db704b`, `--ui-yellow #c08532`,
  `--ui-green #1f8a65/#55a583`, `--ui-cyan #4c7f8c`, `--ui-blue #0053fd`,
  `--ui-purple #9e94d5`, plus `--ui-accent`, `--ui-bg-*`, `--ui-text-*`,
  `--ui-stroke-*`.

## Tailwind class liveness

- Compiled CSS: `apps/desktop/dist/assets/index-*.css`.
- Only ~100 `--ui-*` arbitrary utilities exist, exactly the ones the app source
  uses: `bg-(--ui-bg-tertiary|quaternary|quinary|elevated|chrome|editor)`,
  `text-(--ui-text-primary|secondary|tertiary|quaternary)`,
  `border-(--ui-stroke-secondary|tertiary|quaternary)`, `hover:bg-(--ui-bg-tertiary)`,
  `placeholder:text-(--ui-text-tertiary)`, `divide-(--ui-stroke-tertiary)`,
  `bg-(--ui-green)`(+`/10`,`/70`), `bg-(--ui-yellow)`(+`/10`),
  `text-(--ui-green|red|yellow|accent)`, `hover:text-(--ui-red)`.
- NOT generated as utilities even though the vars exist:
  `bg-(--ui-blue|purple|orange|cyan|red)`, `text-(--ui-blue|cyan|purple|orange)`.
  Use inline `style={{ color: 'var(--ui-blue)' }}` instead — theme-driven.
- Other dead classes confirmed: `grid-cols-7`, `ring-inset`, `last:pb-0`,
  `ml-4`, `m-2`(?) — check with the script, don't trust memory.
- Tool: `scripts/scan-tailwind-classes.js <css> --has-many "cls1" "cls2"`.
