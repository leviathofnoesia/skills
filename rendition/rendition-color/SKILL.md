name: rendition-color
description: >-
  Rendition color system (design language for Nov Pax / Sanctuary) — the Dusk palette
  (Dusk/Teal/Lilac on Porcelain/Onyx) plus OKLCH soft/deep variants and signature gradients.
  Use when choosing brand pigments, building a palette, applying the Dusk→Lilac aurora gradient,
  pairing plate grounds/pigments, or checking AA contrast on light/dark grounds. For exact literals
  and dark-mode overrides, defer to rendition-tokens.
---

# Rendition Color

## The five base tokens

- `--c-dusk #485696` — primary, links, CTAs.
- `--c-teal #689689` — calm, secondary, success.
- `--c-lilac #be95c4` — warmth, italic accents, orb bloom.
- `--c-porcelain #f7f7f2` — light ground.
- `--c-onyx #121113` — dark ground.

Each base has a `-soft` (oklch light) and `-deep` (oklch dark) variant.

## Semantic surfaces

`--bg`, `--surface`/`-muted`/`-deep`, `--fg`, `--text-primary`/`-secondary`/`-tertiary`/`-muted`/`-inverse`,
`--border`/`-subtle`/`-strong`. Light primary; Onyx is the dark room.

## Signature gradient

`--grad-aurora` (Dusk→Lilac) on the orb + one italic accent per plate. Siblings: `--grad-dawn`,
`--grad-iris-sky`, `--grad-sky-mint`, `--grad-iris-coral`, `--grad-spectrum`.

## Per-plate duotone (canonical 8 plates of `Design System.html`)

Set `--plate-ground` × `--plate-pigment` (`:root` defaults onyx×lilac; each plate overrides).

| # | Plate | Ground | Pigment |
|---|---|---|---|
| 01 | Identity | Onyx | Lilac |
| 02 | Type | Porcelain | Dusk |
| 03 | Color | Dusk | Porcelain |
| 04 | Art Direction | Onyx | Teal |
| 05 | Components | Porcelain | Lilac-deep |
| 06 | Product | Onyx | Dusk-soft |
| 07 | Motion | Porcelain | Teal-deep |
| 08 | Voice | Onyx | Porcelain |

(Separately, `preview/brand-identity.html` is an 11-folio brand kit, not a specimen plate.)

## Contrast rule

Target AA on Porcelain (light) and Onyx (dark). Dusk/Teal/Lilac meet AA for large text on grounds;
`-deep` for small text on light, `-soft` on dark. Exact pairs / dark overrides → `rendition-tokens`;
AA commitment + focus order → `rendition-a11y`.

## Anti-patterns

- In authored production never hard-code hex — use tokens (see `rendition-adherence`).
- Never the retired v1 spectrum (biolum `#2DD4BF`, magenta `#E879F9`, solar `#FBB924`).
- Halftone moons are two-color duotone, never gradient.
- Bundled specimens hardcode literals for self-containment — source-fidelity, not a production pattern.
