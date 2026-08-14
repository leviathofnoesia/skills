# Skills

Reusable agent skills for engineering, planning, research, design, documentation,
and prompt tooling.

[![skills.sh](https://skills.sh/b/leviathofnoesia/skills)](https://skills.sh/b/leviathofnoesia/skills)

Maintained by [leviathofnoesia](https://github.com/leviathofnoesia).

## Skills

Skills are grouped by topic to avoid collisions as the collection grows. Each
skill lives at `TOPIC/SKILL-NAME/` and is a self-contained package
(`SKILL.md` + optional `scripts/`, `references/`, `assets/`).

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
| [kraken-gauntlet-loop](./harness/kraken-skill/kraken-gauntlet-loop/) | Quality-improvement loop — build→critic→rebuild against a concrete, inspectable bar until the real output wins blind A/B, composed with kraken-engineer's PDSA. |
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
| [ste-writing](./meta/ste-writing/) | Apply ASD-STE100 Simplified Technical English writing rules to technical docs; stdlib linter flags long sentences, passive/continuous verbs, and multi-word nouns over three words. |
| [gauntlet-loop](./meta/gauntlet-loop/) | Quality-improvement loop — build→critic→rebuild against a concrete inspectable bar (shipped comparable, spec, or benchmark) until the real output wins blind A/B. The lean standalone version; use kraken-gauntlet-loop to compose it with the full Kraken process family. |

### Security

Deepsec and Codex Security scanning — Luna pins and dual-scan workflows.

| Skill | Description |
|-------|-------------|
| [deepsec-luna](./security/deepsec-luna/) | Pin deepsec AI stages (`process` / `revalidate` / `triage`) to `gpt-5.6-luna` on the default agent backend. |
| [deepsec-codex-luna](./security/deepsec-codex-luna/) | Dual-scan a target with deepsec and the open-source Codex Security CLI, both on `gpt-5.6-luna`, then cross-read findings. |

### Creative

Design and UI quality workflows — guided tours and loops that drive a surface
toward a committed visual bar.

| Skill | Description |
|-------|-------------|
| [auto-impeccable](./creative/auto-impeccable/) | Start-to-finish loop over the full impeccable command list (23 commands, 6 categories) — boot context, run Build/Evaluate, loop Refine/Enhance/Fix by project-state signals until the critique score stops improving, finish with polish, and report the score trend. Requires the sibling [impeccable](https://github.com/pbakaus/impeccable) skill. |


## Install

Use the [`skills`](https://www.npmjs.com/package/skills) CLI to install from
this repo:

```bash
# Install every skill in the repo
npx skills add leviathofnoesia/skills

# Install a single skill by slug
npx skills add https://github.com/leviathofnoesia/skills --skill <slug>
```

`<slug>` is the skill's `name:` from its `SKILL.md` (e.g. `kraken-engineer`,
`lean-turns`, `prompt2qr`).

Flags:

- Install for the user (not the project): add `-g`.
- Target specific agents: add `--agent claude-code cursor`.

Manual fallback (symlink into your harness skills path):

```bash
ln -s "$PWD/harness/kraken-skill/kraken-engineer" ~/.claude/skills/kraken-engineer
```

## Generated index

[`index.md`](./index.md) is the compact, generated catalog of every `SKILL.md` in
this repository. It gives agents a fast overview of each skill and keeps the
full source path available for retrieval; the index is a map, not a replacement
for reading the linked skill.

The index is produced by
[`skill-compiler`](https://github.com/leviathofnoesia/skill-compiler)'s
`marketplace` command:

```bash
npx --yes github:leviathofnoesia/skill-compiler marketplace --dir . --out index.md
```

The repository's GitHub Actions workflow regenerates `index.md` on pushes that
change a `SKILL.md`, then commits the generated result when it changes. To
preview or verify locally:

```bash
npx --yes github:leviathofnoesia/skill-compiler marketplace --dir . --dry-run
npx --yes github:leviathofnoesia/skill-compiler marketplace --dir . --check
```

## License

Unless noted otherwise in a skill folder, content is available for use with AI
coding agents. Attribution appreciated.

### Software Development

| Skill | Description |
|-------|-------------|
| [clean-code-series](./software-development/clean-code-series/) | Uncle Bob's Clean series knowledge base — Clean Code, Clean Coder, Clean Architecture, Clean Agile; per-book references with chapter maps and decision rules. |
