# "The tab bar is a broken vertical list / I can't close it" — UI-layout diagnosis

Follow-up to `dashboard-lies-diagnosis.md`. The backend/data fixes were done;
the user then reported the REAL visible problems:
1. Can't close the dashboard after opening it via the bottom-bar Abyss chip.
2. Top tab bar "completely hidden" — can't change tab.
3. "A random vertical tab list that does nothing" and shouldn't be there.

## Root cause: a Tailwind class missing from the compiled CSS

The plugin is evaluated as a Blob URL, so Tailwind never scans its class
strings. Any class absent from the host's compiled stylesheet silently falls
back (unknown class → no rule → default layout). The tab bar used
`grid-cols-7`; the packaged bundle only defines `grid-cols-1/2/4/6`, so the
`display:grid` with no template columns stacked all 7 TabsTriggers **vertically**
— exactly the "random vertical tab list that does nothing".

### Verification: grep the packaged CSS bundle

```bash
CSS="<HERMES_HOME>/hermes-agent/apps/desktop/release/win-unpacked/resources/app.asar.unpacked/dist/assets/index-*.css"
grep -o '\.grid-cols-[0-9]*' "$CSS"          # which grid-cols-* exist?
for cls in "flex" "flex-row" "flex-col" "overflow-x-auto" "shrink-0" "w-full"; do
  grep -q "\.$cls[^a-zA-Z-]" "$CSS" && echo "FOUND: $cls" || echo "MISSING: $cls"
done
```

Gotchas:
- **Paren classes ARE present but escaped.** `bg-(--ui-bg-quaternary)` appears
  in the CSS as `bg-\(--ui-bg-quaternary\)`. A naive grep for the literal
  `bg-(--ui-bg-quaternary)` finds nothing → you'd wrongly conclude the class is
  missing. Search for the inner token instead:
  `grep -c 'ui-bg-quaternary' "$CSS"`.
- **Base-class cascade order matters.** The host `TabsList` already has
  `inline-flex`; adding `flex` in the plugin may LOSE if `.inline-flex` appears
  later in the stylesheet. `inline-flex` is still a horizontal flex row, so
  that's acceptable — the failure was the grid, not flex vs inline-flex.
  When checking "which class wins", compare rule positions in the file, not
  plugin intent.

### The fix (plugin.js)

```js
// Was: className: 'grid w-full grid-cols-7 ...'  →  vertical stack
jsx(TabsList, {
  className: 'flex w-full items-center overflow-x-auto bg-(--ui-bg-quaternary) border-b border-(--ui-stroke-tertiary)',
  children: tabs.map(tab =>
    jsx(TabsTrigger, { key: tab.value, value: tab.value,
      className: 'text-xs h-8 abyss-mono shrink-0', children: tab.label })
  )
})
```

## "I can't close it" — full-page plugin routes need an exit

The status-chip contributed `host.navigate('/abyss')`, which opens the
full-page route with no back affordance. Two fixes:

1. **Close button in the Masthead** — navigate back to chat:
```js
jsx(Button, { variant: 'ghost', size: 'sm', className: 'h-6 w-6 px-0',
  onClick: () => { try { host.navigate('/') } catch { } },
  title: 'Close Abyss dashboard',
  children: jsx(Codicon, { name: 'close', className: 'text-(--ui-text-tertiary)' }) })
```
2. **Make the bottom-bar chip a toggle** — check the hash route:
```js
const isOpen = () => { try { return (window.location.hash || '').startsWith('#/abyss') } catch { return false } }
onClick: () => host.navigate(isOpen() ? '/' : '/abyss')
```

## Lesson for future sessions

- When the user says a dashboard is broken, they usually mean NAVIGATION/LAYOUT
  (close it, switch tabs, stray elements), not data correctness. Fix the data
  (real totals, polling) AND the interaction model.
- The auto-generated screenshot description is unreliable for layout claims —
  it described an unrelated overlay and misread tab labels as per-row content.
  Ground-truth layout against the code and the compiled CSS, not the image.
- `host.navigate('/')` returns to the chat root — the generic "close the
  extension page" escape hatch.
