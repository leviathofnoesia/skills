name: rendition-a11y
description: >-
  Rendition accessibility contract — AA contrast targets on Porcelain/Onyx grounds, first-class
  prefers-reduced-motion on every animated element, visible focus rings, HIG-calm interaction for the
  Sanctuary product, and the no-visible-timer principle. Use when building or reviewing any Rendition
  surface for accessibility, motion sensitivity, or focus order. Pair with rendition-color (contrast
  pairs) and rendition-motion (the reduced-motion mechanics).
---

# Rendition Accessibility

## Contrast

Target AA on Porcelain (light) and Onyx (dark). Dusk/Teal/Lilac meet AA for large text on their grounds;
`-deep` for small text on light, `-soft` on dark. Dark-mode overrides → `rendition-tokens`; the pairing
rationale → `rendition-color`. Never use retired v1 colors.

## Reduced motion (first-class)

Every animated element MUST honor `prefers-reduced-motion: reduce` by disabling the animation (the
`.marquee-track` pattern). No autoplaying loops that ignore it; orb breath / marquee / spring all gated.
Mechanics → `rendition-motion`.

## Focus-visible

Every interactive element has a visible focus ring using `--c-dusk` (light) / `--c-lilac` (dark); never
`outline: none` without a replacement.

## HIG-calm product interaction

Sanctuary stays calm: no visible countdown during focus (exact-minute readouts pull users back to the
screen they're leaving), no notifications beyond the gentle 20-min chime, audio is the primary surface
during rests, the dark "Look Away" screen is intentional (you're not meant to look at it). Product
details → `rendition-product`.

## Typography

Sentence case for display, UPPERCASE only in mono kickers / Geist Black slabs; one italic accent word
per heading. (Readability, not contrast — details in `rendition-type`.)

## What to check

Before marking a Rendition surface done:

- [ ] AA contrast pairs chosen (Porcelain/Onyx grounds).
- [ ] Reduced-motion handled on every animated element.
- [ ] Focus-visible present (no bare `outline: none`).
- [ ] No forced timers / on-screen countdowns in the product.
- [ ] Brand-vs-product loudness split respected.
