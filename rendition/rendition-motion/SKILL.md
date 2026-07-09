name: rendition-motion
description: >-
  Rendition motion language (design language for Nov Pax / Sanctuary) — easing curves
  (cosmic/breath/spring/smooth), the 6s breathing cycle on the companion orb, the 60s marquee border
  loop, and first-class reduced-motion handling. Use when animating any Rendition surface, the orb, or
  plates. Enforces prefers-reduced-motion as a required state on every animated element; values come from
  rendition-tokens.
---

# Rendition Motion

## Easings (from `:root`)

- `--ease-cosmic cubic-bezier(0.22,1,0.36,1)` — primary, expo out.
- `--ease-breath cubic-bezier(0.45,0,0.55,1)` — 6s sin in/out, orb.
- `--ease-spring cubic-bezier(0.34,1.56,0.64,1)` — completed moments only.
- `--ease-smooth cubic-bezier(0.4,0,0.2,1)` — ambient drifts.

## Signature motions

- **Orb breath** — 6s `--ease-breath` loop.
- **Marquee borders** — 60s linear loop
  (`@keyframes marquee { to { transform: translateX(-50%) } }`).
- **Spring** on completion only.

## Reduced motion (mandatory)

Every animated element MUST wrap its animation in
`@media (prefers-reduced-motion: reduce) { … animation: none; }`. `.marquee-track` already does this;
replicate for any custom animation. No exceptions. Full a11y commitment in `rendition-a11y`.

## Worked CSS (copy-paste)

The two signature loops plus the mandatory reduced-motion override. Easing values
are pulled from `rendition-tokens/assets/tokens.css`
(`--ease-breath: cubic-bezier(0.45, 0, 0.55, 1)`; `--ease-cosmic: cubic-bezier(0.22, 1, 0.36, 1)`).

```css
/* ─── Companion orb — 6s breathing cycle ─────────────────────────── */
@keyframes orb-breath {
  0%, 100% { transform: scale(1);    opacity: 0.85; }
  50%      { transform: scale(1.06); opacity: 1;    }
}
.orb {
  /* 6s sin-in/out loop, driven by the breath easing token */
  animation: orb-breath 6s var(--ease-breath) infinite;
}

/* ─── Marquee border — 60s linear loop ───────────────────────────── */
@keyframes marquee { to { transform: translateX(-50%); } }
.marquee-track {
  display: inline-flex;
  white-space: nowrap;
  animation: marquee 60s linear infinite;
}

/* ─── MANDATORY: disable every Rendition animation under reduced motion ─ */
@media (prefers-reduced-motion: reduce) {
  .orb,
  .marquee-track {
    animation: none;
  }
}
```

Any custom Rendition animation MUST be added to the reduced-motion block above
(mirroring the `.marquee-track` pattern already present in tokens.css L432).

## Anti-patterns

- No raw `transition` easings other than the four tokens.
- No autoplaying loops that ignore reduced-motion.
