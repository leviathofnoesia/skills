# Rendition v2.4 Edition — canonical class definitions

> Verbatim extraction of the v2.4 Edition block from `tokens.css` (the v2.4 Edition
> additions, lines ~331–511). These are the authoritative class definitions for the
> brutalist plate layer. Use `rendition-edition` SKILL.md for behavior; this file is the
> source-of-truth CSS.

```css
:root {
  /* Plate duotone defaults — each plate overrides these */
  --plate-ground: var(--c-onyx);
  --plate-pigment: var(--c-lilac);
  --plate-pigment-soft: oklch(86% 0.05 310);
}

/* Chunky display — Geist Black 900, locked tight, ALL CAPS. The brutalist anchor. */
.t-slab {
  font-family: 'Geist', system-ui, sans-serif;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: -0.045em;
  line-height: 1.0;
  padding-bottom: 0.18em;
  font-feature-settings: "ss01", "cv11";
}

/* Halftone moon — CSS-only dot pattern in a soft-edged moon mask. Two-color duotone, never gradient. */
.halftone {
  aspect-ratio: 1;
  color: var(--plate-pigment);
  background-image: radial-gradient(circle, currentColor 36%, transparent 38%);
  background-size: 7px 7px;
  -webkit-mask-image: radial-gradient(circle at 50% 48%, #000 0%, #000 30%, rgba(0,0,0,0.95) 45%, rgba(0,0,0,0.55) 60%, rgba(0,0,0,0.18) 75%, transparent 86%);
  mask-image: radial-gradient(circle at 50% 48%, #000 0%, #000 30%, rgba(0,0,0,0.95) 45%, rgba(0,0,0,0.55) 60%, rgba(0,0,0,0.18) 75%, transparent 86%);
  position: relative;
}
.halftone.coarse { background-size: 9px 9px; }
.halftone.fine   { background-size: 5px 5px; }
.halftone.cresc::after {
  content: ""; position: absolute; inset: 0;
  background-image: radial-gradient(circle, currentColor 48%, transparent 50%);
  background-size: inherit;
  -webkit-mask-image: radial-gradient(circle at 70% 65%, #000 0%, #000 14%, transparent 35%);
  mask-image: radial-gradient(circle at 70% 65%, #000 0%, #000 14%, transparent 35%);
  opacity: 0.55;
}

/* Grain — fixed full-page noise overlay. Apply as body::after or as a standalone element with this class. */
.grain-overlay {
  position: fixed; inset: 0; z-index: 999; pointer-events: none;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.92' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.55 0'/></filter><rect width='240' height='240' filter='url(%23n)'/></svg>");
  opacity: 0.10; mix-blend-mode: multiply;
}

/* Mono kicker variants — the structural voice on plates */
.t-kick    { font-family: var(--font-mono); font-size: 10px;   font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; }
.t-kick-md { font-family: var(--font-mono); font-size: 11.5px; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; }

/* Spec strip — mono multi-line liner-note block. Used in plate bottoms + folios. */
.spec {
  font-family: var(--font-mono); font-size: 9.5px; line-height: 1.7;
  letter-spacing: 0.14em; text-transform: uppercase;
  max-width: 26ch;
}
.spec b { font-weight: 500; }
.spec .div { display: block; height: 1px; margin: 8px 0; background: currentColor; opacity: 0.35; }

/* Crop marks — corner L brackets, evoke print trim guides */
.crop { position: absolute; width: 14px; height: 14px; pointer-events: none; opacity: 0.55; }
.crop::before, .crop::after { content: ""; position: absolute; background: currentColor; }
.crop::before { width: 14px; height: 1px; top: 0; left: 0; }
.crop::after  { width: 1px; height: 14px; top: 0; left: 0; }
.crop.tr { top: 16px; right: 16px; transform: scaleX(-1); }
.crop.tl { top: 16px; left: 16px; }
.crop.bl { bottom: 16px; left: 16px; transform: scaleY(-1); }
.crop.br { bottom: 16px; right: 16px; transform: scale(-1, -1); }

/* Registration cross — print-shop alignment mark */
.reg {
  width: 22px; height: 22px; border-radius: 50%;
  border: 1px solid currentColor; position: relative; opacity: 0.6;
}
.reg::before, .reg::after { content: ""; position: absolute; background: currentColor; }
.reg::before { width: 32px; height: 1px; top: 50%; left: -5px; transform: translateY(-0.5px); }
.reg::after  { width: 1px; height: 32px; left: 50%; top: -5px; transform: translateX(-0.5px); }

/* Barcode — decorative bars of varying widths. Drop ~22 <i></i> children inside. */
.barcode { display: flex; gap: 1px; height: 28px; align-items: stretch; }
.barcode i { background: currentColor; width: 2px; }
.barcode i:nth-child(2n) { width: 1px; }
.barcode i:nth-child(3n) { width: 3px; }
.barcode i:nth-child(5n) { width: 1px; }
.barcode i:nth-child(7n) { width: 4px; }

/* Marquee — repeating wordmark border, scrolls horizontally. Wrap a .marquee-track inside. */
.marquee {
  overflow: hidden; white-space: nowrap;
  border-top: 1px solid currentColor; border-bottom: 1px solid currentColor;
  opacity: 0.7;
}
.marquee-track {
  display: inline-flex; gap: 28px;
  animation: marquee 60s linear infinite;
  padding: 7px 0;
  font-family: var(--font-mono); font-size: 10.5px; letter-spacing: 0.22em;
  text-transform: uppercase;
}
.marquee-track span::before { content: "+ "; opacity: 0.55; }
@keyframes marquee { to { transform: translateX(-50%); } }
@media (prefers-reduced-motion: reduce) { .marquee-track { animation: none; } }

/* Section strip — editorial framing above body content. Mono code + small barcode. */
.section-strip {
  display: grid; grid-template-columns: 1fr auto auto;
  gap: 24px; align-items: center;
  padding: 10px 14px;
  border: 1px solid var(--border);
  background: oklch(99% 0.003 90);
  font-family: var(--font-mono); font-size: 10px; letter-spacing: 0.22em; text-transform: uppercase;
  color: var(--text-tertiary);
  margin-bottom: 24px;
}
.section-strip .l { color: var(--text-primary); font-weight: 500; }
.section-strip .code { color: var(--c-dusk); }
.section-strip .barcode { height: 14px; width: 60px; }
.section-strip .barcode i { background: var(--text-secondary); }

/* Specimen card — hard corner, pigment border, mono header strip. Brutalist sibling of glass. */
.specimen {
  background: oklch(99% 0.003 90);
  border: 2px solid var(--c-dusk);
  border-radius: 0;
  position: relative; overflow: hidden;
}
.specimen.teal  { border-color: var(--c-teal-deep);  }
.specimen.lilac { border-color: var(--c-lilac-deep); }
.specimen > .strip {
  background: var(--c-dusk); color: var(--c-porcelain);
  padding: 6px 14px;
  display: flex; justify-content: space-between;
  font-family: var(--font-mono); font-size: 10px; letter-spacing: 0.22em; text-transform: uppercase;
}
.specimen > .strip.teal  { background: var(--c-teal-deep);  }
.specimen > .strip.lilac { background: var(--c-lilac-deep); }
.specimen > .body { padding: 20px 18px; }

/* Card strip — standalone mono header bar to drop atop any card (e.g. inside .comp, .ease-card) */
.card-strip {
  padding: 8px 16px;
  display: flex; justify-content: space-between; align-items: center;
  font-family: var(--font-mono); font-size: 10px; letter-spacing: 0.22em; text-transform: uppercase;
  background: var(--c-dusk); color: var(--c-porcelain);
}
.card-strip.teal  { background: var(--c-teal-deep);  }
.card-strip.lilac { background: var(--c-lilac-deep); }
.card-strip.onyx  { background: var(--c-onyx);       }
.card-strip .name { font-weight: 500; }

/* Brutalist quote card — Onyx ground, Cormorant italic body, pigment header strip */
.brutal-quote {
  background: var(--c-onyx); color: var(--c-porcelain);
  padding: 0; border-radius: 0; border: none;
  position: relative; overflow: hidden;
  margin: 0 0 22px;
}
.brutal-quote > .strip {
  padding: 6px 14px;
  display: flex; justify-content: space-between;
  font-family: var(--font-mono); font-size: 10px; letter-spacing: 0.22em; text-transform: uppercase;
  background: var(--c-dusk); color: var(--c-porcelain);
}
.brutal-quote.teal  > .strip { background: var(--c-teal-deep);  }
.brutal-quote.lilac > .strip { background: var(--c-lilac-deep); }
.brutal-quote > .body {
  padding: 28px 28px 24px;
  font-family: var(--font-display); font-style: italic; font-weight: 300;
  font-size: 1.5rem; line-height: 1.3; letter-spacing: -0.015em;
}
.brutal-quote > .body .em { font-style: italic; font-weight: 400; color: var(--c-lilac); }
.brutal-quote.teal  > .body .em { color: var(--c-teal-soft);  }
.brutal-quote.lilac > .body .em { color: var(--c-lilac-soft); }

/* Plate scaffolding — set --plate-ground and --plate-pigment on the plate, then style children freely.
   The duotone variables drive every nested element via color-mix(). */
.plate {
  position: relative; overflow: hidden;
  background: var(--plate-ground); color: var(--plate-pigment);
}
```
