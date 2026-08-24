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

---

# Skills Library v2 — expansion families

88 additional skills across six families (added 2026-08-24). Each has a
`human.md` guide alongside its `SKILL.md`.


## Software development (`software-development/`)

Engineering discipline extensions: code health, delivery safety, API care.


- [dead-code-sweep](./software-development/dead-code-sweep/) — Find and safely remove dead code with call-graph evidence.
- [error-taxonomy-design](./software-development/error-taxonomy-design/) — Design consistent error types and codes across a codebase.
- [contract-test-bootstrap](./software-development/contract-test-bootstrap/) — Stand up consumer-driven contract tests between two services.
- [perf-budget-guardian](./software-development/perf-budget-guardian/) — Set and enforce performance budgets in CI with regression alerts.
- [feature-flag-lifecycle](./software-development/feature-flag-lifecycle/) — Manage feature flags: naming, expiry, cleanup, kill switches.
- [migration-planner](./software-development/migration-planner/) — Plan zero-downtime schema migrations with reversible steps.
- [api-versioning-strategy](./software-development/api-versioning-strategy/) — Choose and implement an API versioning scheme that ages well.
- [code-archaeology](./software-development/code-archaeology/) — Reconstruct why legacy code exists using git history and docs.
- [refactor-safe-extract](./software-development/refactor-safe-extract/) — Extract functions/classes behaviorally with seam-first testing.
- [test-data-builder-pattern](./software-development/test-data-builder-pattern/) — Replace brittle test fixtures with composable builder factories.
- [chaos-drill-lite](./software-development/chaos-drill-lite/) — Run small controlled failure drills against your own service.
- [observability-checklist](./software-development/observability-checklist/) — Audit a service for metrics, logs, traces before it ships.
- [dependency-license-audit](./software-development/dependency-license-audit/) — Inventory dependency licenses and flag copyleft/commercial risk.
- [monorepo-split-plan](./software-development/monorepo-split-plan/) — Plan extracting a package from a monorepo without breaking CI.
- [sdk-design-review](./software-development/sdk-design-review/) — Review a public SDK/API surface for ergonomics and stability.
- [incident-postmortem-writer](./software-development/incident-postmortem-writer/) — Write blameless postmortems with timelines and action items.
- [backlog-triage-grooming](./software-development/backlog-triage-grooming/) — Turn a stale issue backlog into a ranked, actionable queue.
- [pr-description-forge](./software-development/pr-description-forge/) — Write PR descriptions reviewers actually need: intent, risk, test.
- [type-boundary-hardening](./software-development/type-boundary-hardening/) — Introduce strict types at module boundaries incrementally.
- [load-test-from-logs](./software-development/load-test-from-logs/) — Build realistic load profiles by replaying production traffic shapes.


## Meta / agent operations (`meta/`)

How agents spend attention and tokens: scoping, verification, self-review.


- [prompt-contract-authoring](./meta/prompt-contract-authoring/) — Write explicit input/output contracts for reusable prompts.
- [context-pruning-pass](./meta/context-pruning-pass/) — Drop stale conversation context before long tasks to save budget.
- [tool-choice-arbiter](./meta/tool-choice-arbiter/) — Pick the cheapest sufficient tool for each subtask step.
- [verification-chain-builder](./meta/verification-chain-builder/) — Chain claims to checks: every assertion gets a verification step.
- [assumption-ledger](./meta/assumption-ledger/) — Track assumptions explicitly and revisit them before shipping.
- [scope-fence](./meta/scope-fence/) — Detect and stop scope creep mid-task with a written fence.
- [failure-mode-catalog](./meta/failure-mode-catalog/) — Enumerate how this task can fail before starting it.
- [progress-heartbeat](./meta/progress-heartbeat/) — Emit structured progress notes during long autonomous runs.
- [self-critique-loop](./meta/self-critique-loop/) — Adversarially review own output against the original ask.
- [instruction-decompiler](./meta/instruction-decompiler/) — Rewrite vague requests into explicit, checkable instructions.
- [artifact-lineage](./meta/artifact-lineage/) — Record which files/artifacts produced which outputs and why.
- [decision-record-mini](./meta/decision-record-mini/) — Lightweight ADRs: decision, options considered, why, revert path.
- [token-budget-forecast](./meta/token-budget-forecast/) — Estimate token cost of a plan before executing it.
- [retry-policy-designer](./meta/retry-policy-designer/) — Choose retry/backoff/timeout policies per external dependency.
- [checklist-compiler](./meta/checklist-compiler/) — Compile recurring workflows into executable checklists.


## Research (`research/`)

Evidence discipline: finding, verifying, synthesizing claims that survive scrutiny.


- [source-triangulation](./research/source-triangulation/) — Verify a claim against three independent source classes.
- [literature-scan](./research/literature-scan/) — Rapid structured scan of a field: key papers, authors, debates.
- [claim-decay-checker](./research/claim-decay-checker/) — Check if a cited fact is superseded or retracted.
- [competitive-teardown](./research/competitive-teardown/) — Systematic product teardown: positioning, pricing, moat, gaps.
- [primary-source-hunter](./research/primary-source-hunter/) — Trace claims back to primary sources instead of aggregators.
- [survey-question-design](./research/survey-question-design/) — Design survey questions that avoid bias and leading frames.
- [dataset-provenance](./research/dataset-provenance/) — Document where data came from and what licenses apply.
- [experiment-power-check](./research/experiment-power-check/) — Sanity-check sample size and effect size before running tests.
- [citation-graph-walk](./research/citation-graph-walk/) — Follow citation chains forward/backward to map a topic's core.
- [expert-interview-prep](./research/expert-interview-prep/) — Prepare interview scripts with open questions and probes.
- [market-sizing-sanity](./research/market-sizing-sanity/) — TAM/SAM/SOM estimates with stated assumptions and ranges.
- [patent-landscape-lite](./research/patent-landscape-lite/) — Sketch the patent landscape around a mechanism or domain.
- [reproducibility-audit](./research/reproducibility-audit/) — Check whether published results can be reproduced from artifacts.
- [synthesis-matrix](./research/synthesis-matrix/) — Merge many sources into a claim-by-source evidence matrix.
- [unknown-unknowns-scan](./research/unknown-unknowns-scan/) — List what the research plan is NOT covering and why that matters.


## Writing & communication (`writing/`)

Turning knowledge into docs people actually read and use.


- [style-guide-distiller](./writing/style-guide-distiller/) — Extract a project's voice rules from existing copy samples.
- [changelog-narrator](./writing/changelog-narrator/) — Turn diff sets into user-facing changelog entries.
- [api-doc-sketcher](./writing/api-doc-sketcher/) — Draft reference docs from real signatures and call sites.
- [tutorial-scaffolder](./writing/tutorial-scaffolder/) — Structure tutorials: promise, steps, checkpoints, payoff.
- [release-note-editor](./writing/release-note-editor/) — Edit raw notes into scannable release communications.
- [blog-post-outline](./writing/blog-post-outline/) — Outline posts with argument flow and evidence slots.
- [email-brevity-pass](./writing/email-brevity-pass/) — Compress professional email while keeping asks explicit.
- [onboarding-doc-audit](./writing/onboarding-doc-audit/) — Audit onboarding docs against a newcomer's actual first day.
- [terminology-consistency](./writing/terminology-consistency/) — Enforce one term per concept across a doc set.
- [readme-doctor](./writing/readme-doctor/) — Diagnose READMEs: missing promise, install friction, stale bits.
- [interview-story-framer](./writing/interview-story-framer/) — Shape experience into STAR-format stories with metrics.
- [translation-handoff-kit](./writing/translation-handoff-kit/) — Package copy for translators: context, glossary, constraints.


## Data engineering (`data/`)

Data trust: schemas, quality audits, honest metrics.


- [schema-drift-detector](./data/schema-drift-detector/) — Detect silent schema drift between environments or snapshots.
- [null-pandemic-audit](./data/null-pandemic-audit/) — Quantify and root-cause null inflation across tables/columns.
- [join-cardinality-check](./data/join-cardinality-check/) — Verify expected row counts before/after joins to catch fan-out.
- [timezone-normalizer](./data/timezone-normalizer/) — Find and fix mixed timezone storage and rendering bugs.
- [pii-scanner](./data/pii-scanner/) — Locate PII leaking into logs, fixtures, and exports.
- [backfill-planner](./data/backfill-planner/) — Plan safe historical backfills with idempotent batches.
- [metric-definition-sheet](./data/metric-definition-sheet/) — One canonical definition per metric with formula and owner.
- [dashboard-critique](./data/dashboard-critique/) — Review dashboards: question first, chart honesty, load speed.
- [csv-hygiene](./data/csv-hygiene/) — Repair encoding, quoting, and type-coercion issues in CSVs.
- [sample-before-model](./data/sample-before-model/) — Profile distributions and leakage before any modeling.
- [event-schema-versioning](./data/event-schema-versioning/) — Version analytics events so downstream queries never break.
- [anomaly-context-pack](./data/anomaly-context-pack/) — Pair each anomaly alert with the context needed to triage it.


## DevOps & reliability (`devops/`)

Operating production: runbooks, capacity, cost, recovery drills.


- [runbook-author](./devops/runbook-author/) — Write runnable runbooks: symptoms, checks, actions, rollback.
- [ci-flake-quarantine](./devops/ci-flake-quarantine/) — Quarantine flaky CI jobs without losing signal.
- [env-parity-audit](./devops/env-parity-audit/) — Diff dev/staging/prod config and surface drift.
- [secret-rotation-playbook](./devops/secret-rotation-playbook/) — Rotate credentials with zero downtime and verified cutover.
- [cost-anomaly-hunt](./devops/cost-anomaly-hunt/) — Trace cloud bill spikes to specific services and causes.
- [deploy-freeze-discipline](./devops/deploy-freeze-discipline/) — Implement freeze windows with exception tracking.
- [log-retention-tuner](./devops/log-retention-tuner/) — Right-size log retention vs cost vs debugging need.
- [health-endpoint-design](./devops/health-endpoint-design/) — Design liveness/readiness endpoints that tell the truth.
- [capacity-headroom-check](./devops/capacity-headroom-check/) — Measure headroom before traffic events; set scaling triggers.
- [backup-restore-drill](./devops/backup-restore-drill/) — Actually restore from backup and time it; prove RTO/RPO.
- [infra-tagging-standard](./devops/infra-tagging-standard/) — Enforce resource tagging for ownership and cost allocation.
- [oncall-transition-kit](./devops/oncall-transition-kit/) — Structured handoffs: open incidents, risks, quiet wins.
- [config-change-journal](./devops/config-change-journal/) — Journal every manual infra change with who/why/revert.
- [local-dev-bootstrap](./devops/local-dev-bootstrap/) — Make 'clone to running' under 10 minutes with one command.

