# Sanctuary — product screens (Nov Pax)

> Summary of `ui_kits/sanctuary/README.md` (four-screen spec + design principles) and the static
> specimen markup in `index.html` / `index.v2.4-light.html`. The product is the calm eye of the storm:
> the brutalist brand chrome frames a quiet, one-room app.

## The product in one paragraph

First routine is the **20-minute screen-rest cycle**: Begin → Sanctuary stays silent → at 20 min a
soft chime + audio-guided meditation ("close your eyes, look away") → dark screen on purpose → cycle
resumes. Repeat.

## Four screens

| # | Screen | Behavior |
|---|---|---|
| 1 | **Home** | Cozy idle room: breathing orb, current routine card, one Begin button. No tabs, no library. |
| 2 | **Focus** | Running silently; soft growing arc; **NO countdown digits**; "We'll let you know"; end-session escape hatch. |
| 3 | **Look Away** | Full-screen dark takeover; audio orb; "Close your eyes"; skip. |
| 4 | **Settings** | Focus interval, voice, soundscape, run-in-background, reduce-motion, placeholder card for future routines. |

## Design principles

- One room, no catalog, no leaderboards, no streaks.
- Quiet by default — "We measure success in how quickly you forget us."
- No visible timer during focus (exact-minute readouts pull users back to the screen they're leaving).
- Audio is the primary surface during rests.
- Expansion is **additive, not branching** (future routines = extra cards in the same room).

## Static specimen markup structure

`ui_kits/sanctuary/index.html` links `../../tokens.css` and lays the four phone screens side-by-side
inside brutalist specimen cards, plus a primitives row. Key anchors:

- Cover plate: `.cover` > `.cover-inner` with `.cover-title` (Geist Black 900), `.halftone` moon,
  `.cover-eclipse` rectangle (Edition chrome around the calm canvas).
- Phone frames use the soft tokens (Porcelain ground, Dusk/Lilac accents); the surrounding chrome is
  Onyx + Lilac duotone.
- Orb: `.orb` with the 6s `--ease-breath` loop (see `rendition-motion`).
- Tab bar (in-app): rounded, Onyx ground, active tab Lilac (see `rendition-components` nav example).

## PWA manifest (`assets/manifest.json`)

Standalone, portrait, `theme_color` / `background_color` `#F5F3EF`, icons `192` / `512` / `maskable`.
Offline via `sw.js` (audio-cache + static-cache, push + dedupe); `workers/pink-noise-processor.js`
is the pink-noise audio worklet; `offline.html` is the fallback. Source files ship in `rendition-kit`.
