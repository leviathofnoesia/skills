# Tell Sweep — the AI-slop detector for the impeccable tour

Adapted from Command Code's `/design` doctrine (full mechanics live in the
`command-code-cli` skill: `references/design-tells.md` and
`references/design-modes.md`). This is the detection layer the tour runs at
baseline and after visual fixes: name the generic pattern with evidence, score
it backward, then let the decision rules route it to an impeccable command.

## Why this exists

- Generated UI is recognizable in ~2 seconds. ~9/10 of that signal sits in ten
  patterns ("the ten tells") that co-occur.
- Each tell is defensible alone — a gradient is not a crime, centered is
  sometimes right. **The co-occurrence is the tell**: the ten safest answers
  chosen together, on every surface.
- Root cause: the model can write any CSS but has no *policy of when*. Absent a
  policy it picks the median answer — and the median of every landing page is
  indigo, centered, three tiles.
- Taste is low-dimensional: a finite set of principles applied consistently,
  plus a short catalogue of common violations. Small enough to write down.

## The ten tells (detect with file:line evidence)

| # | Tell | Detection |
|---|------|-----------|
| 1 | tech gradient | Hero panel filled with blue-violet→magenta gradient |
| 2 | generic tech hue | Solid indigo block; giveaway hex `#6366F1` ("indigo because software") |
| 3 | feature tile grid | Three identical feature tiles side by side, equal weight, no priority |
| 4 | accent rail | Cards with a coloured stripe down the left edge (decoration posing as organization) |
| 5 | unearned blur | Frosted glass panel floating over two coloured blobs (glassmorphism with no depth system) |
| 6 | stat monument | Oversized statistics dominating the panel (`10x`, `99%`) where the product story belongs |
| 7 | icon topper | A square icon above every heading (template filler) |
| 8 | bounce everywhere | Ball bouncing on a floor line in decaying arcs; elastic easing with no purpose |
| 9 | default type | Generic sans-serif specimen with no scale (Inter, whatever the distribution ships) |
| 10 | center stack | Every element centred on one axis — no composition decision made |

## Backward scoring

| Tells found | Score | Verdict |
|-------------|-------|---------|
| 0 | 10/10 | CLEAN |
| 1–2 | 7–8/10 | FAINT |
| 3–4 | 5–6/10 | PRESENT |
| 5–6 | 3–4/10 | STRONG |
| 7+ | 0–2/10 | FAILURE |

Scoring runs backwards: finding zero tells is the perfect result (10/10),
never 0/10.

## Isolation vs clustering (the decision rule)

Severity is about **clustering**, not count:

- 1–2 scattered tells → cleanup, route each to its command (decision table
  below).
- **3+ tells clustered in one viewport** (e.g. gradient hero + three equal
  tiles + centered stack) → **identity failure**: swap the logo and headline
  and the page fits any B2B SaaS. This is a direction problem, not a patch
  queue — surface it in the Phase 3 decision gate, then fix composition before
  colour before decoration.

## Fix ripple order (deslop order)

Structure before colour before decoration — a new palette on a broken layout is
still broken:

1. composition (center stack, tiles)
2. colour (gradient, tech hue)
3. type (default family)
4. depth (blur, stat monument)
5. motion (bounce)
6. decoration (icon topper)

A tell counts as fixed only when: the old pattern is gone from the surface, the
replacement is specific rather than a different default, and no new tell
appeared in its place.

## Seven work patterns — name the job before the pixels

A centered hero with three feature cards is not a layout decision, it is the
absence of one. `shape` names the surface's job first; composition follows the
work, never habit:

1. **Monitor** — status, alerts, live metrics, priority at a glance
2. **Operate** — command bars, canvas, inspectors, direct action
3. **Compare** — tables, matrices, ranked lists, stable scan lanes
4. **Configure** — grouped settings, forms, safe commit areas
5. **Learn** — article flow, walkthrough rhythm, progression
6. **Decide** — focused pitch, proof, one dominant action
7. **Explore** — search, filters, maps, reversible discovery

A centered hero with three equal cards is allowed *when that pattern answers
the work*. It is not the house style.

## Registers — voice or surface

| Register | Surfaces | Mindset | Bar |
|----------|----------|---------|-----|
| `voice` | landing, campaign, portfolio, product story | The interface is the experience | committed colour, typographic risk, ambitious motion/art direction; the first 1.5 seconds is the deliverable |
| `surface` | dashboards, admin, settings, tools, app UI | The interface is the instrument | consistency, density, speed, real data, every state; the 11th visit today with no hesitation |

Name the register before designing. The request's own language wins first, then
the surface being worked on.

## Core rules (the floor — enforced in Phase 4 polish)

- **Colour**: OKLCH-first. Pick a commitment level — whisper, statement,
  conversation, flood — before picking a hue. 60-30-10 split. Never default to
  indigo.
- **Typography**: body at 60–76ch. Minimum 1.3 ratio between hierarchy steps.
  Three fonts only when each has a role: display, body, UI.
- **Layout**: 1-4-9 rhythm (4px, 16px, 36px). Use `gap`, never sibling margins.
  A card inside a card is never right.
- **Motion**: animate `transform` and `opacity`. Ease out, never bounce. Exits
  run at ~70% of entrance duration. `prefers-reduced-motion` is not optional.
- **Interaction**: nine states per control (idle, hover, active, focused,
  loading, empty, error, disabled, overflow). Touch targets ≥44×44px. Labels
  always visible; a placeholder is not a label.
- **Responsive**: base experience first, more structure as space earns it.
  Never gate functionality behind hover. Adapt the interface, never amputate
  the feature.
- **Copy**: one verb per button. Sentence case. No exclamation points. Errors
  are recovery paths, not blame.

## Loop rules borrowed from /design

- **Report modes only report** — the tour's audit modes (`critique`, `audit`,
  tell sweep) never edit a file behind your back; fixing is a separate,
  explicit command.
- **Treatment reads reports first** — any fixing mode checks the critique
  report + tell sweep before deciding what to change, applies the findings,
  then verifies the result visibly.
- **Truthful completion** — a pass may only claim "added/fixed/changed" when
  the change is visible in the rendered result; looked-at-but-not-altered is
  "inspected", never "fixed".

## Tell → impeccable command mapping

| Tell | Command |
|------|---------|
| tech gradient / generic tech hue (`#6366F1`) | `colorize` (OKLCH-first, 60-30-10, never default indigo) |
| feature tile grid / center stack | `layout` (name the job first; one focal point leads) |
| icon topper / stat monument | `distill` / `polish` |
| unearned blur | `distill` (depth only where an elevation system earns it) |
| bounce everywhere | `animate` (transform + opacity, ease-out, exits ~70%) |
| default type (Inter, no scale) | `typeset` (hook/bridge/detail steps, 60–76ch) |
| accent rail | `extract` / `polish` |
| clustering (3+ in one viewport) | direction question → `layout` / `distill` / `bolder` |
