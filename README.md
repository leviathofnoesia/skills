# skills

[![skills.sh](https://skills.sh/b/leviathofnoesia/skills)](https://skills.sh/leviathofnoesia/skills)

Agent skills by [leviathofnoesia](https://github.com/leviathofnoesia).

Skills are grouped by topic to avoid collisions as the collection grows. Each
skill lives at `TOPIC/SKILL-NAME/` and is a self-contained package
(`SKILL.md` + optional `scripts/`, `references/`, `assets/`).

## Skills

| Topic | Skill | Description |
|-------|-------|-------------|
| meta | [lean-turns](./meta/lean-turns/) | **Token-optimized conversational turns** — write intermediate turns lean, reserve full prose for the final deliverable turn |
| meta | [lean-turns-strict](./meta/lean-turns/lean-turns-strict/) | **Token-suppressed intermediate turns** — one status token per intermediate turn, full prose reserved for the final deliverable; agent understanding unchanged |
| rendition | [rendition-tokens](./rendition/rendition-tokens/) | Rendition design-language token reference for Nov Pax / Sanctuary — exact color, type, spacing, radius, shadow, gradient, motion tokens, OKLCH/hex literals, Onyx dark overrides, and v2.0→v2.4 legacy aliases. Ships tokens.css as source of truth |
| rendition | [rendition-color](./rendition/rendition-color/) | Rendition color system — the Dusk palette (Dusk/Teal/Lilac on Porcelain/Onyx) plus OKLCH soft/deep variants, signature aurora gradient, per-plate duotones, and AA contrast guidance |
| rendition | [rendition-type](./rendition/rendition-type/) | Rendition typography — Cormorant Garamond, Geist Black 900 anchor, Geist/Inter, IBM Plex Mono, GeistPixel; v2.4 display scale, tracking, and the one-italic-word-per-heading rule |
| rendition | [rendition-edition](./rendition/rendition-edition/) | Rendition v2.4 "Edition" brutalist layer — plates, CSS halftone moons, Geist Black 900 slabs, marquee borders, crop marks, registration cross, barcode strips, specimen/brutal-quote cards, grain overlay |
| rendition | [rendition-components](./rendition/rendition-components/) | Rendition component vocabulary — pill buttons, glass/specimen/brutal-quote cards, floating nav, and primitives, with token-driven styling and interaction states |
| rendition | [rendition-motion](./rendition/rendition-motion/) | Rendition motion — cosmic/breath/spring/smooth easings, 6s orb breath, 60s marquee loop, and mandatory prefers-reduced-motion handling on every animated element |
| rendition | [rendition-voice](./rendition/rendition-voice/) | Rendition voice & copy — calm, second-person, present-tense; no exclamation marks; em-dash breath; paradox philosophy; one italic Cormorant word per heading; lowercase nov pax lockups |
| rendition | [rendition-product](./rendition/rendition-product/) | Sanctuary app — 20-minute screen-rest cycle, four screens (Home/Focus/Look Away/Settings), one-room model, no visible countdown, audio-first rests, PWA manifest |
| rendition | [rendition-kit](./rendition/rendition-kit/) | Rendition UI-kit specimens & scaffolds — marketing + Sanctuary HTML, brand-identity and component preview pages; ships the spec HTMLs and tokens.css |
| rendition | [rendition-adherence](./rendition/rendition-adherence/) | Rendition adherence — ESLint enforcement of token-only colors/spacing/fonts; warns on raw hex, raw px, and non-DS font-family in authored production CSS/JSX |
| rendition | [rendition-brand](./rendition/rendition-brand/) | Nov Pax brand identity — logo marks, wordmark, aurora gradients, philosophy, social, and the 28-image brand kit; art-direction mood boards |
| rendition | [rendition-a11y](./rendition/rendition-a11y/) | Rendition accessibility contract — AA contrast on Porcelain/Onyx, first-class reduced-motion, focus-visible rings, HIG-calm product interaction, no-visible-timer |

## Install

Use the [`skills`](https://www.npmjs.com/package/skills) CLI to install a
skill straight from this repo:

```bash
# Install one skill by topic/name path
npx skills add leviathofnoesia/skills/meta/lean-turns

# Or install the whole repo's skills
npx skills add leviathofnoesia/skills
```

Manual fallback (symlink into your harness skills path):

```bash
ln -s "$(pwd)/meta/lean-turns" ~/.claude/skills/lean-turns
```

## License

Unless noted otherwise in a skill folder, content is available for use with AI
coding agents. Attribution appreciated.
