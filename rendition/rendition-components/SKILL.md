name: rendition-components
description: >-
  Rendition component vocabulary — buttons (pill + breath press), cards (glass / specimen / brutal-quote),
  floating nav, and primitives. Use when implementing UI components in the Rendition system (Nov Pax /
  Sanctuary surfaces): exact class names, anatomy, interaction states, and token-driven styling. Companion
  to rendition-edition (chrome) and rendition-tokens (values); defer to rendition-adherence for lint.
---

# Rendition Components

## Buttons

Pill (`--radius-full`), Dusk fill or outline, hover lift via `--shadow-md`, press uses a subtle
"breath" scale on `--ease-breath`. Never raw hex in production; bg from `--c-dusk` / surface tokens.
(Specimens hardcode literals for self-containment.)

- Pill tier — `btn btn-pill btn-pill-primary|secondary|tertiary` (Geist 600, 14px, soft).
- Slab tier — `btn btn-slab btn-slab-primary|onyx|dusk|teal|ghost` (Geist 700, 11px, 2px radius, 0.18em uppercase).
- Mini — `btn btn-mini dusk|lilac|teal|outline` (mono tag).

## Cards

Three siblings:
- `.glass` — soft watercolor surface, primary over imagery, translucent.
- `.specimen` — hard-corner pigment-bordered brutalist card w/ mono `.strip` header (`.teal`/`.lilac`).
- `.brutal-quote` — Onyx-ground Cormorant italic quote, pigment `.strip`.

Glass for atmosphere, specimen for structure.

## Nav

Concrete nav structures: the sticky running header `.nav-run` (hairline-divided cells, `+ 0X` mono
codes, single CTA) and the in-app tab bar `.tabbar` (rounded, Onyx ground, active tab Lilac with a
glow). The "floating pill nav" is a *design intent* — glassmorphic, Dusk border, grid texture, single
primary CTA, Lucide-style icons from `assets/icons/` — composed from `.glass` + `.nav-run`, not a
single bundled class. Lift the full floating nav from `rendition-kit` (`preview/components-nav.html`).

## Primitives

`.divider-edit` (thin line + diamond accent), `.diamond` bullet, `.orb` (companion dusk+lilac glow),
`.t-aurora` gradient text, `.t-display`/`.t-display-it` Cormorant, `.t-kicker`/`.t-marker`/`.t-pixel`
editorial type utilities.

## Where the CSS lives

This skill is the class **vocabulary** (names, anatomy, states). The visual CSS for `.btn*`, `.glass`,
`.specimen`, `.nav-run`, `.tabbar`, and the primitives is defined in `rendition-tokens`
`assets/tokens.css` and the fully-styled components in `rendition-kit` (`preview/components-*.html`).
Copy a working styled component from the kit; this skill tells you the correct class names.

## State & a11y

Focus-visible rings from `--c-dusk`; reduced-motion disables breath/marquee; AA contrast commitment +
focus order live in `rendition-a11y`. Copy working markup (button/card/nav) from
`references/component-examples.md`.
