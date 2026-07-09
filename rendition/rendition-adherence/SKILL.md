name: rendition-adherence
description: >-
  Rendition design-system adherence — enforce token-only colors, spacing, and fonts via the bundled
  ESLint config (_adherence.oxlintrc.json, ESLint-shaped) that warns on raw hex literals, raw px values,
  and non-DS font-family declarations. Use before committing Rendition CSS/JSX, or when reviewing a PR
  for DS violations. Companion to rendition-tokens (the allowed token list) and rendition-type (allowed
  font families).
---

# Rendition Adherence

## Scope (the carve-out, load-bearing)

These rules govern **authored production CSS/JSX**, not the bundled illustrative specimens under
`rendition-kit` / `rendition-brand` (which hardcode literals for self-containment and source-fidelity —
they are references, not patterns to copy into production).

## What it enforces

Three `no-restricted-syntax` rules (from `assets/_adherence.oxlintrc.json`, an ESLint-shaped config):

1. raw hex color literal → "use a design-system color token via var()".
2. raw `Npx` literal → "use a design-system spacing token via var()".
3. A string-literal `font-family` whose value is NOT in {Geist, Geist Mono, GeistPixel,
   GeistPixel-Grid, Cormorant Garamond, Inter, IBM Plex Mono} → banned.

Rule 3 matches the quoted CSS-string form (`font-family: "Geist"`), which is what the bundled
specimens use. It does NOT catch the camelCase JS-object form `fontFamily: "Geist"`; for that,
keep fonts out of literals and use the design-system classes (`.t-display`, `.t-kicker`, etc.)
which set `--font-*`. This is a detection gap, not a change in policy.

Plus `no-restricted-imports` warns on importing component internals (`sw.js`, `workers/**`) — import
from `index.js` instead. `**/index.js` is exempt.

## How to run

Run the bundled ESLint runner (do NOT use oxlint — it cannot parse this config: no `no-restricted-syntax`,
and it rejects the `x-omelette` tooling field that is stripped from the shipped copy):

```bash
bash scripts/check.sh path/to/file.css
```

The runner loads ESLint (installed locally in `node_modules/`) with a generated wrapper config that
reuses the shipped rules and adds `parserOptions` so `const`/JSX/TS parse. Rules are `warn`, not `error`,
so CI can gate on warnings.

```bash
bash scripts/check.sh path/to/file.css
```

## Allowed tokens

Point to `rendition-tokens` `assets/tokens.css` for the full `--c-*`, `--space-*`, `--radius-*`,
`--type-*` list (the config's `x-omelette.tokens` enumerates exactly these). Allowed fonts →
`rendition-type`.

## Back-compat note

Legacy aliases (`--c-iris` etc.) still resolve; raw hex in legacy vendored files is expected and out of
scope. Reference wiring of tokens + components: `assets/_standalone_src.html`.
