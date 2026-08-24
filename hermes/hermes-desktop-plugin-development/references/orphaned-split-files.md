# Orphaned Split Files Next to plugin.js (verified Aug 2026, Abyss plugin)

## Discovery

The Abyss desktop plugin folder contained `plugin.js` plus seven split files
(`activity-feed.js`, `calendar-view.js`, `global-search.js`, `tracing-view.js`,
`brain-view.js`, `signals-incidents.js`, `ditherkit.js`). Only `plugin.js`
ever loaded. The split files were duplicates of components that had been
inlined into `plugin.js` when the plugin was consolidated to the single-file
format.

## Why they're dead

The runtime loader evaluates `plugin.js` as a Blob URL via `import()`. A blob
has no path context, so relative imports (`./activity-feed.js`) cannot
resolve. A multi-file layout therefore never loads — the manifest/entry is
`plugin.js`, and that file is self-contained. The split files are referenced
by nothing (grep the whole plugin folder + manifests; the only matches are
comments mentioning them).

## The trap

They still "look" maintained: fresh timestamps, real code, sensible names. A
future session that needs to change e.g. the signals view will find
`signals-incidents.js`, edit IT, and the change never appears — silent hours
of wasted work because the live code is the inlined copy in `plugin.js`.

## The fix

1. Before editing any component, confirm where it lives:
   `grep -n "function SignalsIncidentsView" plugin.js` — if present there,
   that's the live definition.
2. Delete the orphaned split files (`rm` them) so nobody edits the dead
   copy. Keep only `plugin.js`.
3. Verify nothing referenced them first: `grep -rn "signals-incidents" --include="*.js" --include="*.json" --include="*.yaml" .`
4. ESM-check the surviving file: `node --input-type=module --check < plugin.js`.

## Related

- SKILL.md pitfall "Relative imports DON'T work" — root cause.
- SDK variant audit: `grep -oE "'primary'|'subtle'|variant: '[a-z]+'" plugin.js | sort | uniq -c`
  (invalid variants like `primary`/`subtle` render unstyled silently; map to
  `default`/`outline`).
