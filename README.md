# skills

[![skills.sh](https://skills.sh/b/leviathofnoesia/skills)](https://skills.sh/leviathofnoesia/skills)

Agent skills by [leviathofnoesia](https://github.com/leviathofnoesia).

## Skills

Skills are grouped by topic to avoid collisions as the collection grows. Each
skill lives at `TOPIC/SKILL-NAME/` and is a self-contained package
(`SKILL.md` + optional `scripts/`, `references/`, `assets/`).

### Rendition

The Nov Pax / Sanctuary design system — tokens, components, motion, voice,
brand, and accessibility. Load any subset that applies to a UI or brand task;
the kit ships working HTML and the `tokens.css` source of truth.

| Skill | Description |
|-------|-------------|
| [rendition-tokens](./rendition/rendition-tokens/) | Design-language tokens — color, type, spacing, radius, shadow, motion; ships `tokens.css` as source of truth. |
| [rendition-color](./rendition/rendition-color/) | Dusk palette (Dusk/Teal/Lilac on Porcelain/Onyx), OKLCH variants, aurora gradient, per-plate duotones, AA contrast. |
| [rendition-type](./rendition/rendition-type/) | Typography — Cormorant Garamond, Geist Black 900 anchor, IBM Plex Mono; v2.4 display scale and tracking rules. |
| [rendition-edition](./rendition/rendition-edition/) | v2.4 brutalist layer — plates, halftone moons, Geist Black slabs, marquee borders, crop marks, specimen cards. |
| [rendition-components](./rendition/rendition-components/) | Component vocabulary — pill buttons, glass/specimen/brutal-quote cards, floating nav, token-driven interaction states. |
| [rendition-motion](./rendition/rendition-motion/) | Motion — cosmic/breath/spring easings, 6s orb breath, 60s marquee, mandatory `prefers-reduced-motion` handling. |
| [rendition-voice](./rendition/rendition-voice/) | Voice & copy — calm, second-person, present-tense; no exclamations; em-dash breath; one italic word per heading. |
| [rendition-product](./rendition/rendition-product/) | Sanctuary app — 20-min screen-rest cycle, four screens, one-room model, no visible countdown, audio-first PWA. |
| [rendition-kit](./rendition/rendition-kit/) | UI-kit specimens & scaffolds — marketing + Sanctuary HTML, brand-identity and component preview pages. |
| [rendition-adherence](./rendition/rendition-adherence/) | ESLint enforcement of token-only colors/spacing/fonts; warns on raw hex, raw px, non-DS fonts in authored CSS/JSX. |
| [rendition-brand](./rendition/rendition-brand/) | Nov Pax brand identity — logo marks, wordmark, aurora gradients, philosophy, 28-image brand kit. |
| [rendition-a11y](./rendition/rendition-a11y/) | Accessibility contract — AA contrast on Porcelain/Onyx, first-class reduced-motion, focus-visible rings, HIG-calm interaction. |

### Kraken

Engineering methodology family. A process overlay — load alongside
specialists, not instead. `kraken-engineer` is the universal method; the rest
are specialists (architecture, planning, search, research, design, docs,
constraints, audit, TDD, multimedia analysis, learning-memory).

| Skill | Description |
|-------|-------------|
| [kraken-engineer](./harness/kraken-skill/kraken-engineer/) | Universal engineering method — plan with verifiable steps, TDD, evidence-gated completion. The process overlay for the whole family. |
| [kraken-architect](./harness/kraken-skill/kraken-architect/) | Architecture method — first-principles analysis (Mode 1) and structural codebase audit (Mode 2); every claim backed by code evidence. |
| [kraken-cartographer](./harness/kraken-skill/kraken-cartographer/) | Planning method — correct, complete, verifiable plans; think before formatting, prove before claiming. |
| [kraken-nautilus](./harness/kraken-skill/kraken-nautilus/) | Codebase-search method — systematic cross-validated exploration; picks the right tool per intent, runs parallel, cross-validates. |
| [kraken-abyssal](./harness/kraken-skill/kraken-abyssal/) | External-research method — evidence-based answers about external libraries/frameworks, every claim version-pinned and cited. |
| [kraken-coral](./harness/kraken-skill/kraken-coral/) | Visual/UI-design method — requirements to accessible, design-system-compliant interfaces; AA/AAA contrast, 60fps motion. |
| [kraken-siren](./harness/kraken-skill/kraken-siren/) | Documentation method — clear, comprehensive, actionable docs; content mapping, audience assessment, quality checklist. |
| [kraken-poseidon](./harness/kraken-skill/kraken-poseidon/) | Pre-planning constraint method — constraint satisfaction before planning to surface requirements, boundaries, hidden ambiguities. |
| [kraken-scylla](./harness/kraken-skill/kraken-scylla/) | Plan-quality-audit method — evaluate plans against SOLID and measurable gates before execution. |
| [kraken-blitzkrieg-tdd](./harness/kraken-skill/kraken-blitzkrieg-tdd/) | TDD & evidence-gated completion — test plan before code, red→green→refactor, ≥80% coverage, violation checklist. |
| [kraken-pearl](./harness/kraken-skill/kraken-pearl/) | Multimedia-analysis method — structured evidence-bound extraction from PDF, image, diagram, screenshot, presentation, chart. |
| [kraken-learning](./harness/kraken-skill/kraken-learning/) | Learning-memory habit — persist and compound decisions/outcomes after meaningful work; experience store, knowledge graph, spaced repetition. |

### Meta

Prompt utilities and token economy — keep intermediate turns cheap and move
long prompts onto cheaper transports.

| Skill | Description |
|-------|-------------|
| [lean-turns](./meta/lean-turns/) | Token-optimized conversational turns — lean intermediate turns, full prose reserved for the final deliverable. |
| [lean-turns-strict](./meta/lean-turns/lean-turns-strict/) | Token-suppressed intermediate turns — one status token per turn (P:/E:/V:/F:), all detail held until the final deliverable. |
| [prompt2image](./meta/prompt2image/) | Render a text prompt as a compact monospace PNG a vision model can OCR for fewer tokens (lossy; for exact bytes use prompt2qr). |
| [prompt2qr](./meta/prompt2qr/) | Gzip-compress a prompt into a sequence of lossless binary QR codes (PNG); exact byte-for-byte reconstruction on decode. |

## Install

Use the [`skills`](https://www.npmjs.com/package/skills) CLI to install from
this repo:

```bash
# Install every skill in the repo
npx skills add leviathofnoesia/skills

# Install a single skill by slug
npx skills add https://github.com/leviathofnoesia/skills --skill <slug>
```

`<slug>` is the skill's `name:` from its `SKILL.md` (e.g. `rendition-tokens`,
`kraken-engineer`, `lean-turns`, `prompt2qr`).

Flags:

- Install for the user (not the project): add `-g`.
- Target specific agents: add `--agent claude-code cursor`.

Manual fallback (symlink into your harness skills path):

```bash
ln -s "$PWD/rendition/rendition-tokens" ~/.claude/skills/rendition-tokens
```

## License

Unless noted otherwise in a skill folder, content is available for use with AI
coding agents. Attribution appreciated.
