name: rendition-type
description: >-
  Rendition typography (design language for Nov Pax / Sanctuary) — Cormorant Garamond (display/italic
  soul), Geist Black 900 (v2.4 brutalist anchor), Geist/Inter (UI/body), IBM Plex Mono (kickers/spec
  strips), GeistPixel (poster moments). Use when assigning type roles, applying the v2.4 display scale,
  setting tracking, or enforcing the one-italic-Cormorant-word-per-heading rule. Exact literals live in
  rendition-tokens.
---

# Rendition Type

## Type roles

| Role | Family | Weight | Use |
|---|---|---|---|
| Display | Cormorant Garamond | 300/400 italic | headlines, ledes, one italic accent word/line |
| Anchor | **Geist Black 900** | 900 | plate titles, slab moments, `clamp()` to 14vw, all caps, lh 1.0, ls -0.045em |
| UI / Body | Geist 300–700 | 300–700 | buttons, forms, running text |
| Mono kicker | IBM Plex Mono 400/500 | 400/500 | `+ KICKERS`, spec strips, 0.22em tracking |
| Tech | Geist Mono | — | timestamps / data |
| Pixel | GeistPixel | — | poster moments, single-word headlines only |

## v2.4 display scale

`--type-display-2xl clamp(4rem,11vw,8rem)`, `-xl clamp(3rem,8vw,6rem)`,
`-lg clamp(2.25rem,5.5vw,4rem)`, `-md clamp(1.75rem,3.5vw,2.5rem)`,
`-sm clamp(1.375rem,2.5vw,1.75rem)`; body `--type-body-md 1rem`;
mono `--type-mono-sm 0.8125rem`, etc.

## Tracking & rules

- Sentence case for display.
- UPPERCASE in mono kickers (0.22em) and Geist Black slabs (-0.045em).
- **One italic Cormorant word per heading max.**
- lowercase `nov pax` in body lockups (company name).
- em dashes for breath.

## Font invariants (enforcement)

Allowed families exactly: Cormorant Garamond, Geist, Geist Mono, GeistPixel, GeistPixel-Grid,
IBM Plex Mono, Inter. Any other `font-family` violates adherence — see `rendition-adherence`.
