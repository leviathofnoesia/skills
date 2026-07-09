name: rendition-product
description: >-
  Rendition product app — Sanctuary, Nov Pax's "quiet companion for the screened life." Covers the
  20-minute screen-rest cycle, the four screens (Home / Focus / Look Away / Settings), the one-room
  model, no visible countdown during focus, audio-first rests, and the PWA manifest. Use when building
  or reviewing the Sanctuary app or any calm "quiet companion" surface in the Rendition system.
---

# Rendition Product — Sanctuary

Sanctuary is Nov Pax's "quiet companion for the screened life." It is the soft eye of the storm; the
brutalist brand world exists so the product can whisper.

## The product in one paragraph

The first routine is the **20-minute screen-rest cycle**: Begin → Sanctuary stays silent → at 20 min a
soft chime + audio-guided meditation ("close your eyes, look away") → dark screen on purpose → cycle
resumes. Repeat.

## Four screens

- **Home** — cozy idle room: breathing orb, current routine card, one Begin button. No tabs, no library.
- **Focus** — running silently, soft growing arc, **NO countdown digits**, "We'll let you know",
  end-session escape hatch.
- **Look Away** — full-screen dark takeover, audio orb, "Close your eyes", skip.
- **Settings** — focus interval, voice, soundscape, run-in-background, reduce-motion, placeholder card
  for future routines.

## Design principles

One room, no catalog, no leaderboards, no streaks; quiet by default; no visible timer during focus;
audio is the primary surface during rests; expansion is additive, not branching (future routines =
extra cards in the same room).

## HIG-aligned calm & PWA

Ships as a PWA: `assets/manifest.json` (standalone, portrait, theme/bg `#F5F3EF`, icons
`192/512/maskable`), offline via `sw.js` (audio-cache + static-cache, push + dedupe), pink-noise
worker `workers/pink-noise-processor.js`, `offline.html` fallback.

Screen markup + principles → `references/sanctuary-screens.md`. Voice/copy → `rendition-voice`;
calm a11y → `rendition-a11y`.
