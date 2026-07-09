name: rendition-tokens
description: >-
  Rendition design-language token reference, governing the visual system for Nov Pax / Sanctuary.
  Use for exact color, type, spacing, radius, shadow, gradient, and motion-token values, their
  OKLCH/hex literals, dark-mode (Onyx) overrides, and v2.0→v2.4 legacy aliases (--c-iris, --c-sky,
  --c-mint, --c-coral, --c-charcoal). Ships tokens.css as source of truth. Pair with
  rendition-adherence to lint usage and rendition-color / rendition-type for domain guidance.
---

# Rendition Tokens

Rendition is the design language governing **Nov Pax** (company) and **Sanctuary** (product). This
skill is the token source-of-truth.

## Source of truth

Read `assets/tokens.css` (this skill) for the full v2.4 token set. It is the canonical file; lift
hex/OKLCH literals directly when writing production code. Rendition governs Nov Pax and Sanctuary.

## Quick reference (most-used tokens)

| Token | Value | Role |
|---|---|---|
| `--c-dusk` | `#485696` | primary / links / CTAs |
| `--c-teal` | `#689689` | calm / secondary / success |
| `--c-lilac` | `#be95c4` | warmth / italic accents / orb bloom |
| `--c-porcelain` | `#f7f7f2` | light ground |
| `--c-onyx` | `#121113` | dark ground |
| `--bg` | `#f7f7f2` | page ground |
| `--surface` | `oklch(99% 0.003 90)` | raised surface |
| `--fg` | `#1b1a1d` | base text |
| `--grad-aurora` | `linear-gradient(135deg, var(--c-dusk), var(--c-lilac))` | signature gradient |
| `--ease-cosmic` | `cubic-bezier(0.22,1,0.36,1)` | primary expo-out |
| `--ease-breath` | `cubic-bezier(0.45,0,0.55,1)` | 6s orb breath |
| `--ease-spring` | `cubic-bezier(0.34,1.56,0.64,1)` | completed moments |
| `--ease-smooth` | `cubic-bezier(0.4,0,0.2,1)` | ambient drifts |

Radii: `--radius-xs 2px … --radius-2xl 32px`. Spacing: `--space-1 4px … --space-10 128px` (4px base).
Type: `--type-display-2xl clamp(4rem,11vw,8rem) … --type-body-md 1rem`.

## Dark mode

`.dark` / `[data-theme='dark']` lifts `--c-dusk #6c7cc0`, `--c-teal #7eb0a3`, `--c-lilac #cea8d4`;
ground → `--bg #121113`, `--fg #f7f7f2`.

## Legacy aliases (deprecated but live)

`--c-iris`/`--c-sky` → `--c-dusk`, `--c-mint` → `--c-teal`, `--c-coral` → `--c-lilac`,
`--c-stone` → `--c-porcelain`, `--c-charcoal`/`--c-void` → `--c-onyx`, plus `--spectrum-1/2/3`.

## Other skills

Color → `rendition-color` · Type → `rendition-type` · Lint → `rendition-adherence` ·
Brand kit → `rendition-brand` · A11y → `rendition-a11y`.
