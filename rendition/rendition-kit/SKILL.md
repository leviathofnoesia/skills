name: rendition-kit
description: >-
  Rendition UI-kit specimens & page scaffolds — the marketing site (hero / cost / signal / waitlist /
  footer) and the Sanctuary app screens as working HTML, plus brand-identity and component preview pages.
  Use when bootstrapping a Rendition page, copying a real layout, or studying canonical markup. Ships the
  small spec HTMLs; the full 8-plate specimen and token CSS live in rendition-tokens / rendition-edition.
---

# Rendition Kit — specimens & scaffolds

## Specimen root layout

`assets/specimens/tokens.css` is the single tokens.css copy. The preview and ui_kits HTML keep their
original relative folder structure so their `<link>`s resolve:

- `preview/*.html` → `../tokens.css` (= specimens root)
- `ui_kits/{marketing,sanctuary}/*.html` → `../../tokens.css` (= specimens root)
- `Design System.html` → `tokens.css` (same dir)

`Design System.html` is the canonical 8-plate specimen (`folios 01/08…08/08`); read-only reference.

## How to scaffold a page

1. Copy/link `tokens.css` (this skill or `rendition-tokens`).
2. Add the grain overlay (`body::after` SVG-noise data-URI from `tokens.css` `.grain-overlay`).
3. Pick a plate duotone (`rendition-color` / `rendition-edition`).
4. Build with Edition classes (`rendition-edition`).

Fonts: Cormorant/Inter/IBM Plex Mono via the Google Fonts `@import` in `tokens.css`; Geist/GeistPixel
are self-hosted in the source `fonts/` (not bundled here — link or copy from source if needed).

## Marketing kit (`ui_kits/marketing/`)

Hero (full-bleed dark, floating nav, tagline, CTA), cost section (problem framing), signal section
(bento grid), waitlist CTA (gradient glass + email), footer.

## Sanctuary kit (`ui_kits/sanctuary/`)

Four screens side-by-side specimen — see `rendition-product`.

## What's bundled

`assets/specimens/`: `tokens.css`, `preview/` (11 spec pages), `ui_kits/marketing/` + `ui_kits/sanctuary/`,
`Design System.html`, `offline.html`. NOT copied: `assets/brand/*` rasters and `fonts/*` binaries
(size guard; available in the source zip).
