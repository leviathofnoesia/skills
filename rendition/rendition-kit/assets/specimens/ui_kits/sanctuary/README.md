# Nov Pax Sanctuary — App UI Kit (v2.1)

Sanctuary is **one cozy companion**, not a library of practices.
It runs quietly in the background while you use your screens, and gently pulls you out of them at healthy intervals.

## The product, in one paragraph
The first and primary routine is the **20-minute screen-rest cycle**.
You begin a session. Sanctuary stays out of your way. After twenty minutes of screen time, a soft chime arrives and Sanctuary takes over with a short **audio-guided meditation** asking you to close your eyes and look away. The screen is dark on purpose — you're not meant to look at it.

When the rest is over, the focus cycle resumes silently. Repeat.

## Screens (v2.1)
1. **Home** — single cozy room: breathing orb, current routine card, one Begin button. No tabs, no library.
2. **Focus, running silently** — soft growing arc, no countdown digits (intentionally invisible), "We'll let you know" message, end-session escape hatch.
3. **Look Away** — full-screen dark take-over, audio-guidance mark, "Close your eyes," skip button.
4. **Settings** — focus interval, voice, soundscape, run-in-background, reduce-motion, plus a placeholder card for future routines.

## Design principles
- **One room.** No catalog. No leaderboards. No streaks.
- **Quiet by default.** Sanctuary measures success in how quickly you forget it.
- **No visible timer during focus** — exact-minute readouts pull users back to the screen they were trying to look away from.
- **Audio is the primary surface during rests.** Visuals support but never demand attention.
- **Expansion is additive, not branching.** Future routines (evening wind-down, posture nudges, walking rests) appear as additional cards in the same single room.

## Tokens
All values resolve from the v2 root `tokens.css` — Iris/Sky/Mint/Coral/Lilac OKLCH spectrum, Cormorant + Geist + IBM Plex Mono.

## Usage
Open `index.html` — a static specimen with all four screens side-by-side, plus a primitives row.
