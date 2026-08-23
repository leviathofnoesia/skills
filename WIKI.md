# Skills Wiki

A guided tour of this repository: what lives here, how the skill families
relate, how to install each skill into your harness, and how the generated
index works. For a flat catalog, see [`index.md`](./index.md); for the
marketing view, see [`README.md`](./README.md).

---

## What is a skill here?

Every skill is a self-contained folder with at minimum a `SKILL.md` whose
YAML frontmatter carries two fields:

```yaml
---
name: my-skill          # the slug used for installation
description: "..."      # one line; also what agents match against
---
```

Optional additions: `scripts/` (executable helpers), `references/`
(load-on-demand knowledge), `assets/`, `human.md` (a plain-language guide
for people, not agents), and a per-skill `README.md`.

Layout rule: skills are grouped by topic to avoid name collisions as the
collection grows.

```
TOPIC/SKILL-NAME/SKILL.md
```

Topics: `harness/` (Kraken family), `meta/` (prompt/token utilities),
`security/` (deepsec scanning workflows), `software-development/`
(knowledge bases + engineering methods), `creative/` (UI quality loops).

---

## Skill families

### ⚙️ Kraken (`harness/kraken-skill/`) — engineering methodology

A process overlay: load it *alongside* specialist skills, not instead of
them. `kraken-engineer` is the universal method (verifiable steps, TDD,
evidence gates); every other member is a phase or discipline spun out of it:

| Role | Skills |
|---|---|
| Universal method | kraken-engineer |
| Plan | kraken-poseidon (constraints) → kraken-cartographer (planning) → kraken-scylla (plan audit) |
| Explore | kraken-nautilus (codebase search), kraken-abyssal (external research, cited & pinned) |
| Build | kraken-blitzkrieg-tdd, kraken-gauntlet-loop (quality iteration) |
| Review/record | kraken-architect, kraken-siren (docs), kraken-pearl (multimedia analysis), kraken-learning (memory), kraken-git-verify (safe git writes) |

### 🧭 Meta (`meta/`) — prompt economy and agent operations

Utilities about *how* an agent spends its budget:

- **Token transport**: [prompt2image](./meta/prompt2image/) renders text as
  OCR-readable PNG; [prompt2qr](./meta/prompt2qr/) is the lossless QR
  variant. [lean-turns](./meta/lean-turns/) /
  [lean-turns-strict](./meta/lean-turns/lean-turns-strict/) compress
  intermediate conversation turns.
- **Run hygiene**: [context-budget](./meta/context-budget/) plans long tasks
  around the context window; [log-mining](./meta/log-mining/) extracts
  signal from large logs.
- **Quality & text**: [gauntlet-loop](./meta/gauntlet-loop/) (build → blind
  critic → rebuild), [ste-writing](./meta/ste-writing/) (ASD-STE100 prose
  rules).

### 🔐 Security (`security/`) — deepsec + Codex Security

Scanning workflows around [deepsec](https://github.com/leviathofnoesia)
with Luna model pins and DeepSeek V4 variants. Pick by matrix — single vs
dual scanner × model pin:

| | deepsec only | deepsec + Codex |
|---|---|---|
| V4 Flash | deepsec-v4-flash | deepsec-codex-v4-flash |
| V4 Pro | deepsec-v4-pro | deepsec-codex-v4-pro |
| Luna pin | deepsec-luna | deepsec-codex-luna |

[deepsec-orchestrator](./security/deepsec-orchestrator/) automates the whole
scan → judge → fix → verify loop. The four DeepSeek skills never hardcode a
harness/API — they ask you first.

### 📚 Software Development (`software-development/`)

Knowledge bases and engineering methods:
[clean-code-series](./software-development/clean-code-series/) (the four
Clean books as load-on-demand references),
[agent-sanctuary](./software-development/agent-sanctuary/) (lifecycle
skills marketplace), plus review-and-repro methods:
[diff-explain](./software-development/diff-explain/),
[api-contract-diff](./software-development/api-contract-diff/),
[dep-upgrade-audit](./software-development/dep-upgrade-audit/),
[flaky-test-triage](./software-development/flaky-test-triage/),
[env-repro](./software-development/env-repro/).

### 🎨 Creative (`creative/`)

[auto-impeccable](./creative/auto-impeccable/) — guided UI-quality tours
that drive a surface toward a committed visual bar.

---

## Installing

The repo publishes through the [`skills`](https://www.npmjs.com/package/skills)
CLI, which reads each `SKILL.md`'s frontmatter:

```bash
# Everything in the repo
npx skills add leviathofnoesia/skills

# One skill by slug (= the name: field)
npx skills add https://github.com/leviathofnoesia/skills --skill prompt2image

# User scope instead of project scope, specific harnesses
npx skills add leviathofnoesia/skills -g --agent claude-code cursor
```

Manual fallback — symlink the folder into whatever directory your harness
scans for skills:

```bash
ln -s "$PWD/meta/prompt2image" ~/.claude/skills/prompt2image
```

Because each skill is just a folder with frontmatter, any harness that can
read markdown can use them; the CLI exists to place files correctly and
keep them updatable.

---

## The generated index

[`index.md`](./index.md) is **generated** — do not edit its managed section.
It compresses every `SKILL.md` into a fixed record shape:

```
[name Skill]|source:leviathofnoesia/skills
|path:<relative path>
|<description line>
|<first lines of body>
|FULL: ./path/SKILL.md
```

An agent reads `index.md` as a map (cheap overview), then loads the linked
`SKILL.md` when one matches the task. Regenerate locally with
[`skill-compiler`](https://github.com/leviathofnoesia/skill-compiler):

```bash
npx --yes github:leviathofnoesia/skill-compiler marketplace --dir . --out index.md

# CI-style checks
... marketplace --dir . --check
```

GitHub Actions regenerates the index on every push touching a `SKILL.md`
and commits the result if it changed — so a stale index should never be
fixed by hand, only by re-running the compiler.

---

## Conventions for contributors

1. One skill per folder under a topic directory; `name:` must equal the
   folder name so slugs stay predictable.
2. Write the description as a trigger ("Use when…") — it doubles as the
   matching string agents see.
3. Ship a `human.md` for anything non-obvious; guides use plain language.
4. Re-run the marketplace command before committing so `index.md` travels
   with your new skill.
5. Regression check: `python tests/check_skill_frontmatter.py` verifies the
   `skills` CLI discovers all skills from their frontmatter.
