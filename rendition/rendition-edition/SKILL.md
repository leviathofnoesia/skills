name: rendition-edition
description: >-
  Rendition v2.4 "Edition" brutalist layer — plates, CSS-only halftone moons, Geist Black 900 slab
  titles, scrolling marquee borders, crop marks, registration cross, barcode strips, mono spec strips,
  specimen/brutal-quote cards, and the grain overlay. Use when building plate-driven layouts or applying
  surrealist-brutalist chrome over the calm product. Pair with rendition-tokens (values) and
  rendition-components (cards).
---

# Rendition Edition (v2.4 brutalist layer)

## Philosophy

Quiet brutalism: hard edges + surreal scale. Plates carry structure; Cormorant carries breath. The
brand world yells QUIET so the product can whisper.

## Plate scaffolding

`.plate` is a full-bleed section; set `--plate-ground` and `--plate-pigment` on it; nested elements
derive color via `color-mix()`. Every plate carries a marquee border, top-row mono codes, corner crop
marks, a bottom-row spec strip + barcode + registration cross, and folio `P. 0X / 08`
(verified in `Design System.html`: `01/08…08/08`).

## Class vocabulary

Verbatim class definitions live in `references/edition-classes.md` (canonical). One-line behavior:

- `.t-slab` — Geist Black 900 all-caps anchor.
- `.halftone` + `.coarse/.fine/.cresc` — CSS moon (two-color duotone, never gradient).
- `.grain-overlay` — fixed SVG noise, ~10% multiply.
- `.t-kick`/`.t-kick-md` — mono kickers.
- `.spec` — mono liner-note block.
- `.crop` + `.tl/.tr/.bl/.br` — corner brackets.
- `.reg` — registration cross.
- `.barcode` — drop ~22 `<i></i>` children.
- `.marquee`/`.marquee-track` — 60s scroll, reduced-motion respected.
- `.section-strip` — editorial framing above body.
- `.specimen` + `.teal/.lilac` — brutalist card + mono header strip.
- `.card-strip` + `.teal/.lilac/.onyx` — standalone header bar.
- `.brutal-quote` + `.teal/.lilac` — Onyx-ground Cormorant italic quote card.
- `.plate` — full-bleed section using `--plate-ground`/`--plate-pigment`.

## Signature composition

Geist Black title overlapping a halftone moon overlapping a hard eclipse rectangle; one italic
Cormorant accent word per plate in `--grad-aurora`.

## The 8 plates (canonical specimen)

01 Identity cover · 02 Type specimen · 03 Color chart · 04 Art Direction mood board ·
05 Components inventory · 06 Product reveal · 07 Motion diagrams · 08 Voice manifesto.
(`preview/brand-identity.html` is a separate 11-folio brand kit — `FOLIO 01 / 11` — not one of these 8.)
