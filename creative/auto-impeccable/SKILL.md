---
name: auto-impeccable
description: Use when running an auto-impeccable tour of a UI project.
version: 1.0.0
author: Kraken
license: MIT
metadata:
  hermes:
    tags: [design, impeccable, tour, loop, refine, ui, quality-bar]
    related_skills: [impeccable, kraken-engineer, kraken-gauntlet-loop]
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
3. If `context.mjs` reports `NO_PRODUCT_MD`, the tour starts at `init` (Phase 1).

## The Full Command List (the tour's repertoire)

All 23 commands, grouped by category. The tour runs each **as needed** — the
state machine in the next section decides when. Entry references live in
impeccable's `references/` (e.g. `<imp>/references/critique.md`).

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
| `live` | Iterate | In-browser visual variants (HMR) | Dev server running AND user wants visual exploration |

## The Algorithm — start-to-finish loop

A bounded state machine. **Phases 0-2 run once; Phase 3 loops; Phases 4-5
finish.** The whole cycle respects impeccable's core rule: *verify in bounded
passes, not a loop* — build fully, inspect once with a batched round, fix
everything in one batch, confirm with at most one more round, then stop.

### Phase 0 — Boot & Orient
Run Setup. Resolve the target to a concrete file path or route. Determine the
mode (Persuade / Operate / Read / Experience) from the surface. **Completion:
`context.mjs` directives known; target resolved; mode named.**

### Phase 1 — Foundation (Build)
- `NO_PRODUCT_MD` → `init` first (multi-round discovery, one per project).
- Code exists, no DESIGN.md → `document`.
- New feature/surface → `shape` before any code.
- Known token/component drift → `extract`.
**Completion: PRODUCT.md and DESIGN.md present (or user declined), and the
visual world is committed.**

### Phase 2 — Baseline (Evaluate)
- `critique <target>` — must run Assessments A and B as **two isolated
  sub-agents** (design review + detector/browser evidence). If delegation is
  unavailable, run sequentially and emit the `⚠️ DEGRADED` banner. Record the
  heuristic score (e.g. 24/40) and P0/P1 counts.
- `audit <target>` — a11y, perf, responsive, theming, anti-patterns.
**Completion: baseline critique snapshot persisted (`.impeccable/critique/`),
audit scored, and the priority-issue list exists.**

### Phase 3 — Refine Loop (bounded, the core)
Each round: **fix the single biggest remaining gap**, then re-evaluate.

1. **Rank the backlog** from critique priority issues + audit findings:
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
   technical). Read the trend via `critique-storage.mjs trend <target> 5`.
   - Score improved → continue the loop with the next gap.
   - Score flat or worse for two consecutive rounds → stop refining; the
     remaining issues are direction, not polish — report and ask the user
     (tonal direction, scope, off-limits areas).
   - P0/P1s all cleared and score ≥ 32/40 (or user's stated bar) → exit loop.
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

### Phase 5 — Iterate (optional)
Only if the dev server is running AND the user wants visual variants: `live`
for in-browser alternatives. Web-only — skip on `ios`/`android`/`adaptive`
platforms. **Completion: user accepted or discarded variants; tour ends.**

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
| Visual alternatives in browser | `live` (web + dev server only) |

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

## Verification Checklist

- [ ] `context.mjs` ran once; `MODE`/`PLATFORM`/`NO_PRODUCT_MD` directives followed
- [ ] Phase 1 artifacts present: PRODUCT.md, DESIGN.md (or user declined)
- [ ] Baseline critique ran dual-agent (A: design review · B: detector), snapshot persisted, trend readable
- [ ] Each Phase 3 command followed its impeccable reference and loaded `craft-floor.md` before UI edits
- [ ] Refine loop exited on a real condition: bar met, flat-for-2, budget spent, or user direction
- [ ] Final `polish` done with one batched verification round; source diff clean
- [ ] Tour report delivered: commands run, score trend with denominators (e.g. 24/40 → 30/40), remaining gaps, next-step suggestion
