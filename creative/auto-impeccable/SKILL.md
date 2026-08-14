---
name: auto-impeccable
description: Use when running an auto-impeccable tour of a UI project.
version: 1.1.0
author: Kraken
license: MIT
metadata:
  hermes:
    tags: [design, impeccable, tour, loop, refine, ui, quality-bar]
    related_skills: [impeccable, kraken-engineer, kraken-gauntlet-loop, command-code-cli]
---

# Auto-Impeccable — Guided Skill Tour / Refine Loop

A guided, start-to-finish loop over the **full impeccable command list**. Where
impeccable is a command palette you pick from, this skill is the guided tour:
it boots the project, walks the 23 commands in dependency order, runs each one
**as needed** based on project-state signals, loops the Evaluate → Refine
cycle until the critique score stops improving or the quality bar is met, then
finishes with `polish` and reports the whole journey.

This is a method overlay, not a replacement. **The impeccable skill does the
work; this skill sequences it.** Load both. Every command executed here must
follow its own impeccable reference — this skill never skips a command's
playbook.

It also embeds the **tell sweep** (Command Code's `/design` doctrine, adapted
from `references/tell-sweep.md`): a ten-pattern detector for the AI-generated
look that runs at baseline, names generic tells with file:line evidence, and
feeds the decision rules with concrete signals instead of vibes.

## When to Use

- User asks to "run the full impeccable tour", "auto-impeccable", "guided tour
  through impeccable", "walk the whole command list", or wants an end-to-end
  design pass on a UI.
- User wants a surface refined start-to-finish without hand-picking commands.
- Don't use for: a single explicit command (`/impeccable critique` — just run
  it), backend-only/non-UI work, or when the user wants to pick commands
  interactively (that's impeccable's no-argument menu).

## Setup

1. **Resolve impeccable's base dir once** and reuse the resolved path (below,
   `<imp>`). Try, in order:
   - `skill_view(name='impeccable')` — resolves when the harness loader sees it;
   - filesystem discovery in the harness's skill trees:
     ```bash
     ls -d "$HOME/AppData/Local/hermes/skills/creative/impeccable" \
            "$HOME/AppData/Local/hermes/profiles/"*/skills/creative/impeccable \
            "$HOME/.hermes/skills/creative/impeccable" \
            "$HOME/.claude/skills/impeccable" 2>/dev/null
     ```
     (Windows Hermes home is `AppData\Local\hermes`; macOS/Linux is
     `~/.hermes`. Check the `hermes-agent` skill if unsure.)
   - If neither finds it, stop and tell the user impeccable is not installed
     in any skill tree this machine loads.
2. Run `node <imp>/scripts/context.mjs` once, with `--target <path>` when a
   source file or route is known. Keep cwd at the user's project. Follow its
   directives (`MODE`, `PLATFORM`, `NO_PRODUCT_MD`, `CONTEXT_STALE`) — report
   stale findings, never repair drift as a side effect.
3. If `context.mjs` reports `NO_PRODUCT_MD`, route per Phase 1: `init` first
   only for new-surface or replacement-world builds; scoped refinements proceed
   on the incumbent implementation and offer `init` afterward.

## The Full Command List (the tour's repertoire)

All 23 commands, grouped by category. The tour runs each **as needed** — the
state machine in the next section decides when. Entry references live in
impeccable's `reference/` directory (e.g. `<imp>/reference/critique.md`; some
harness installs rename it `references/`).

| Command | Category | Purpose | Tour runs it when |
|---|---|---|---|
| `shape` | Build | Plan UX/UI before code; discovery interview → design brief | New feature/surface needs a plan before build |
| `init` | Build | Capture PRODUCT.md (users, brand, principles) | `NO_PRODUCT_MD`, or first tour on a fresh project |
| `document` | Build | Generate DESIGN.md from existing code | Code exists but no DESIGN.md (`setup.hasDesign` false) |
| `extract` | Build | Pull tokens/components into the design system | Detector or audit shows drift / repeated patterns |
| `craft` | Build | Deprecated alias for ordinary new-work | Never — route to `shape`/new-work flow |
| `critique` | Evaluate | UX design review, dual-agent, heuristic score | Baseline and after each refine round |
| `audit` | Evaluate | Technical quality: a11y, perf, responsive | Baseline, and when detector/console shows technical issues |
| `polish` | Refine | Final quality pass before shipping | End of every cycle; reads critique snapshot as backlog |
| `bolder` | Refine | Amplify safe/bland designs | Critique: "generic", "safe", low design-specificity |
| `quieter` | Refine | Tone down aggressive designs | Critique: "too loud", "overwhelming", garish |
| `distill` | Refine | Strip to essence, remove complexity | Critique: clutter, cognitive overload, too many elements |
| `harden` | Refine | Production-ready: errors, i18n, edge cases | Missing states, overflow, i18n, edge cases |
| `onboard` | Refine | First-run flows, empty states, activation | Empty states/onboarding gaps in critique |
| `animate` | Enhance | Purposeful motion and micro-interactions | Motion missing or scattered; want aliveness |
| `colorize` | Enhance | Strategic color for monochrome UIs | Detector: flat/gray palette; critique: dull |
| `typeset` | Enhance | Typography hierarchy and fonts | Type issues: hierarchy, measure, system faces |
| `layout` | Enhance | Spacing, rhythm, visual hierarchy | Spacing/grid/hierarchy issues |
| `delight` | Enhance | Personality and memorable touches | Critique: functional but joyless |
| `overdrive` | Enhance | Push past conventional limits | User wants wow/extraordinary; after basics are solid |
| `clarify` | Fix | UX copy, labels, error messages | Jargon, confusing copy, bad error text |
| `adapt` | Fix | Responsive/devices/screen sizes | Breakpoint/mobile/touch-target issues |
| `optimize` | Fix | UI performance: load, render, animation | Slow, janky, bundle-size findings |
| `live` | Iterate | In-browser visual variants (HMR) | Dev server with HMR running OR a browser-accessible static HTML target, AND user wants visual exploration. Web-only — skip on `ios`/`android`/`adaptive` |

## The Algorithm — start-to-finish loop

A bounded state machine. **Phases 0-2 run once; Phase 3 loops; Phases 4-5
finish.** The whole cycle respects impeccable's core rule: *verify in bounded
passes, not a loop* — build fully, inspect once with a batched round, fix
everything in one batch, confirm with at most one more round, then stop.

### Phase 0 — Boot & Orient
Run Setup. Resolve the target to a concrete file path or route. Determine the
mode (Persuade / Operate / Read / Experience) from the surface. **Reject a
null-slug target now**: if the target stays vague or root-level (so
`critique-storage.mjs slug` would fail), either resolve it to a concrete path
or record that persistence will be skipped and the critique will run with an
in-memory report. **Completion: `context.mjs` directives known; target
resolved (or skip-persistence reason recorded); mode named.**

### Phase 1 — Foundation (Build)
- `NO_PRODUCT_MD`: run `init` before implementation **only** for new-surface
  or replacement-world builds (multi-round discovery, one per project). A
  scoped refinement of existing code proceeds on the incumbent implementation
  as `context.mjs` directs and offers `init` afterward rather than blocking on
  it.
- Code exists, no DESIGN.md → `document`.
- New feature/surface → `shape` before any code. `shape` names the job first:
  pick one of the **seven work patterns** (Monitor / Operate / Compare /
  Configure / Learn / Decide / Explore) and a **register** (`voice` — the
  interface is the experience, for landing/portfolio/editorial · `surface` —
  the interface is the instrument, for dashboards/admin/tools) before any
  composition. Pattern first, pixels second (`references/tell-sweep.md`).
- Known token/component drift → `extract`.
**Completion: PRODUCT.md and DESIGN.md present (or user declined), and the
visual world is committed.**

### Phase 2 — Baseline (Evaluate)
- `critique <target>` — must run Assessments A and B as **two isolated
  sub-agents** (design review + detector/browser evidence). If delegation is
  unavailable, run sequentially and emit the `⚠️ DEGRADED` banner. Record the
  heuristic score (e.g. 24/40) and P0/P1 counts.
- `audit <target>` — a11y, perf, responsive, theming, anti-patterns.
- **Tell sweep** — the smell check (`references/tell-sweep.md`): score the
  target's ten tells backward (0 tells = 10/10 CLEAN … 7+ = 0–2/10 FAILURE),
  each finding with file:line evidence. Record the tell score in the critique
  report. Isolation rule: 1–2 scattered tells are cleanup; **3+ tells
  clustered in one viewport is an identity failure** (a direction problem, not
  a polish backlog) — flag it for the Phase 3 decision gate.
**Completion: baseline critique delivered as a report — snapshot persisted
(.impeccable/critique/) when the target slug is non-null, otherwise the
skip-persistence reason is recorded and the in-memory report stands; audit
scored; tell sweep scored; priority-issue list exists.**

### Phase 3 — Refine Loop (bounded, the core)
Each round: **fix the single biggest remaining gap**, then re-evaluate.

0. **Capture the critique's decision gate first** (impeccable's critique
   "Ask the User" step): present the priority issues and ask for priority
   direction, scope (top-3 vs all), and off-limits areas — 2-4 targeted
   questions tied to actual findings. **Auto-execute only objective P0/P1
   fixes** (broken paths, a11y, misleading state, missing error/empty states)
   when no direction is captured. Tonal or enhancement commands (`bolder`,
   `quieter`, `distill`, `overdrive`, `delight`, `colorize`, `animate`) run
   **only** with the user's consent and within the captured scope; otherwise
   list them as recommendations and let the user pick.
1. **Rank the backlog** from critique priority issues + audit findings:
   - **Identity first**: if the tell sweep scored STRONG/FAILURE, or 3+ tells
     cluster in the first viewport, rank composition/identity fixes
     (`layout` / `distill` / `bolder` after naming the job) above tonal or
     enhancement work. A new palette on a broken layout is still broken.
   - Fix first: P0/P1 functional, accessibility, broken paths, misleading
     state → `clarify` (copy) / `adapt` (responsive) / `optimize` (perf) /
     `harden` (states/edge cases/i18n).
   - Then Refine: `polish` for system drift and micro-detail; `bolder` /
     `quieter` / `distill` for tonal direction; `onboard` for activation gaps.
   - Then Enhance: `animate` / `colorize` / `typeset` / `layout` / `delight`,
     and `overdrive` only when the user explicitly wants extraordinary.
2. **Run the top command** per impeccable's reference. Load `craft-floor.md`
   before editing UI; act on detector findings instead of re-auditing rules.
3. **Re-evaluate**: re-run `critique` (and `audit` if the change was
   technical). Read the trend via
   `node <imp>/scripts/critique-storage.mjs trend "<resolved target>" 5`. A
   non-zero helper exit (e.g. no snapshot yet) must not stop the workflow —
   print the error and continue with the in-memory report.
   Re-run the tell sweep when the change was visual: a tell counts as fixed
   only when the old pattern is gone from the surface, the replacement is
   specific rather than a different default, and no new tell appeared in its
   place. If the heuristic score moved but the tell score didn't, the fix
   traded one default for another — treat as flat.
   - **Compare normalized scores**: divide each score by its snapshot's
     applicable maximum (`max_score`, default 40 when missing) and compare
     percentages — never raw totals. Raw 24 vs 30 would look like an
     improvement, but 24/32 and 30/40 are both 75% — a tie; and a newly
     applicable heuristic that raises the maximum must not look like a
     regression.
   - Score improved (normalized) → continue the loop with the next gap.
   - Score flat or worse for two consecutive rounds → stop refining; the
     remaining issues are direction, not polish — report and ask the user
     (tonal direction, scope, off-limits areas).
   - P0/P1s all cleared and normalized score ≥ 80% (e.g. 32/40, 26/32) or the
     user's stated bar → exit loop.
4. **Budget**: no more than 3 full refine rounds per tour unless the user
   extends. The critique→fix→critique cadence is the loop; it is never
   open-ended self-QA.

**Completion: one of the exit conditions above, with a trend line reported.**

### Phase 4 — Finish (polish)
Run `polish <target>` as the final pass: read the latest critique snapshot,
triage functional → states → flow/hierarchy → visual → cleanup, fix in one
batch, verify with **one** batched inspection round (desktop + mobile
together), confirm with at most one more round, then stop. Finish with a
source diff — no accidental churn, no orphaned code.

Enforce the **core-rules floor** during the final pass
(`references/tell-sweep.md`): OKLCH color with a 60-30-10 split · body copy at
60–76ch with ≥1.3 hierarchy ratio · 1-4-9 spacing rhythm via `gap`, never
sibling margins · motion on transform+opacity, ease-out, exits ~70%, honoring
`prefers-reduced-motion` · nine interaction states per control with ≥44×44 hit
targets · base-first responsive, never gating functionality behind hover ·
one verb per button, sentence case, no exclamation points.

### Phase 5 — Iterate (optional)
Only if the dev server with HMR is running — or the target is a
browser-accessible static HTML file — AND the user wants visual variants:
`live` for in-browser alternatives. Web-only — skip on
`ios`/`android`/`adaptive` platforms. **Completion: user accepted or
discarded variants; tour ends.**

## Decision Rules (finding → command)

| Finding / signal | Command |
|---|---|
| P0/P1 functional, a11y, broken path | `clarify` / `adapt` / `optimize` / `harden` |
| Missing loading/empty/error/success/disabled states | `harden` / `onboard` |
| Bland, generic, "safe", low specificity | `bolder` (then `colorize` if palette is gray) |
| Too loud, overwhelming, garish | `quieter` |
| Cluttered, cognitive overload, too many options | `distill` |
| Type hierarchy, measure, font choices | `typeset` |
| Spacing, rhythm, grid, alignment | `layout` |
| Flat/gray palette | `colorize` |
| No motion or scattered motion | `animate` (one authored moment, not many) |
| Functional but joyless | `delight` |
| Slow, janky, big bundle | `optimize` |
| Confusing copy, jargon, bad errors | `clarify` |
| Breakpoints, touch targets, cross-device | `adapt` |
| System drift, repeated patterns | `extract` |
| Onboarding/empty-state/activation gaps | `onboard` |
| Final pass / pre-ship | `polish` |
| Visual alternatives in browser | `live` (dev server with HMR or static HTML target; web-only) |
| Tell: tech gradient / generic tech hue (`#6366F1`) | `colorize` (OKLCH-first, 60-30-10, never default indigo) |
| Tell: feature tile grid / center stack | `layout` (name the job first; one focal point leads) |
| Tell: icon topper / stat monument | `distill` / `polish` |
| Tell: unearned blur | `distill` (depth only where an elevation system earns it) |
| Tell: bounce everywhere | `animate` (transform + opacity, ease-out, exits ~70%) |
| Tell: default type (Inter, no scale) | `typeset` (hook/bridge/detail steps, 60–76ch) |
| Tell: accent rail | `extract` / `polish` |
| Tell clustering (3+ in one viewport) | direction question → `layout` / `distill` / `bolder` |

## Common Pitfalls

1. **Running a command without loading its reference.** Every executed command
   must follow impeccable's own playbook (e.g. critique's dual-agent rule,
   polish's triage order). The tour sequences; impeccable executes.
2. **Open-ended self-QA.** The whole point of the bounded rule is to stop.
   One batched inspection round, one fix batch, one confirmation round.
3. **Critique without sub-agent separation.** Assessments A and B must be
   isolated; a silent single-context critique is a failed critique. Emit the
   degraded banner if you had to fall back.
4. **Repairing drift as a side effect.** `CONTEXT_STALE` is reported, not
   acted on, unless the user asks.
5. **`live` and `detect` on native platforms.** They're web-only; skip on
   `ios`/`android`/`adaptive`.
6. **Running `craft`.** It's a deprecated alias; route new-work through
   `shape` / new-work flow.
7. **Refining past the direction problem.** If two rounds don't move the
   score, the issue is direction, not polish — stop and ask the user, don't
   keep polishing the wrong world.
8. **Forgetting the tour is a loop, not a checklist.** Only run commands the
   signals justify; never run all 23 for the sake of completeness.
9. **Treating a clustered-tell identity failure as a polish backlog.** 3+ tells
   in one viewport (gradient hero + three equal tiles + centered stack) is a
   direction problem, not a patch queue — run `layout` / `distill` / `bolder`
   after naming the job and surface the direction question to the user.

## Verification Checklist

- [ ] `context.mjs` ran once; `MODE`/`PLATFORM`/`NO_PRODUCT_MD` directives followed
- [ ] Phase 1 artifacts present: PRODUCT.md, DESIGN.md (or user declined)
- [ ] Baseline critique ran dual-agent (A: design review · B: detector); snapshot persisted, or skip-persistence reason recorded for a null-slug target; trend readable when persisted
- [ ] Tell sweep scored at baseline (backward: 10/10 = clean) with file:line evidence recorded in the report
- [ ] Each Phase 3 command followed its impeccable reference and loaded `craft-floor.md` before UI edits
- [ ] Refine loop exited on a real condition: bar met, flat-for-2, budget spent, or user direction
- [ ] Final `polish` done with one batched verification round; source diff clean
- [ ] Tour report delivered: commands run, score trend with denominators (e.g. 24/40 → 30/40), remaining gaps, next-step suggestion
