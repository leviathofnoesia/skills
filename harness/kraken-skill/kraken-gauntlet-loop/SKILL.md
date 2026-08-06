---
name: kraken-gauntlet-loop
description: >-
  Gauntlet Loop method — the quality-iteration loop that runs inside
  kraken-engineer's PDSA: build→critic→rebuild against a concrete, inspectable
  quality bar until the agent's real output wins or ties the bar in blind A/B,
  never settling for "improved". The bar is chosen first (a real shipped
  comparable, spec, or benchmark — or a measurable property if none exists), then
  the goal is decomposed into the smallest independently-judgeable pieces, each
  fanning out a builder and a separate harsh critic. Part of the kraken-engineer
  mindset family — adopt directly; compose with kraken-engineer for process,
  kraken-scylla for the critic's measurable-criteria gates, and kraken-architect
  for choosing the bar when the reference is a design/trade-off decision.
---

# kraken-gauntlet-loop

Gauntlet Loop composed into the kraken-engineer method family. The quality
loop itself is **inherited verbatim** from [`gauntlet-loop`](../../meta/gauntlet-loop/SKILL.md)
(standalone meta skill) — its [references/bar.md](../../meta/gauntlet-loop/references/bar.md)
and [references/prompt.md](../../meta/gauntlet-loop/references/prompt.md) are shared. This
skill adds only the disciplinary wrapper: how the loop sits inside kraken-engineer's
PDSA cycle and how the kraken family's specialist gates strengthen each phase.

Use this variant when you also want kraken-engineer's process rigor (planning,
evidence-gated completion, cross-validation) applied around the loop. For a lean
standalone run with no process overhead, use `gauntlet-loop` directly.

## How it sits inside kraken-engineer's PDSA

kraken-engineer runs four phases. The Gauntlet Loop is not a phase replacement —
it is the **Study → Act** engine that lives inside the iterative PDSA cycle,
governing how each iteration is judged and what the next iteration attacks.

| PDSA phase | gauntlet role | kraken-family composition |
|---|---|---|
| **Plan** | Choose the bar and the axes of comparison. | `kraken-architect` for bar selection (design/trade-off refs), `kraken-scylla` for measurable acceptance criteria on the bar. |
| **Do** | BUILD — produce real, runnable output per piece. | `kraken-architect` for structural design, `kraken-blitzkrieg-tdd` for test-first within each piece. |
| **Study** | CRITIQUE + COMPARE — blind side-by-side against the bar. | `kraken-nautilus` for systematic evidence gathering, `kraken-pearl` for visual/multimodal bar inspection, `kraken-scylla` for measurable-criteria gates. |
| **Act** | LOOP or escalate — decide win/tie/lose and next gap. | `kraken-scylla` stalemate escalation, `kraken-architect` bar-widening if the gap hasn't moved across rounds. |

## Pre-Planning (kraken-engineer, before the loop fires)

1. **Intent classification** — is this a quality target needing the loop, or just
   correctness against a spec you can TDD? (Wrong choice → use `kraken-blitzkrieg-tdd` alone.)
2. **Bar selection** — a real, inspectable, comparable artifact (shipped
   comparable, published spec/RFC, public benchmark). If none exists, fall back to
   a measurable property per `gauntlet-loop`. When the reference is a
   design/trade-off decision rather than a shipped artifact, adopt
   `kraken-architect` to turn it into an inspectable design reference.
3. **Decomposition** — slice the goal into the smallest pieces that can be
   improved and judged independently. Each piece gets its own builder + critic
   subagent pair with fresh context.

## The loop (inherited from `gauntlet-loop` — no changes to the protocol)

> The protocol below is **identical** to `gauntlet-loop`. This skill does not
> re-author it; it composes it with kraken-family gates. Read
> [`gauntlet-loop`'s SKILL.md](../../meta/gauntlet-loop/SKILL.md) for the
> canonical round protocol, critic constraints, and the lead-agent duties.

### Round protocol (per piece)

1. **BUILD** — `kraken-blitzkrieg-tdd` enforces test-first; the builder ships real
   runnable output, not a summary.
2. **CRITIQUE** — `kraken-pearl` (visual/multimodal bar) or `kraken-nautilus`
   (codebase evidence) gives the critic real material to compare. Blind
   side-by-side; one biggest gap only.
3. **COMPARE** — verdict is **win / tie / lose** per axis. "Improved" is a
   non-verdict — send back and re-run the round. This is where
   `kraken-scylla`'s measurable-criteria gates bite hardest.
4. **LOOP** — until wins/ties on every axis, or stopped.

### The critic (kraken-hardened)

- **Harsh.** Default assumption: the latest output still loses.
- **Blind.** Strip labels when the bar supports it (`kraken-pearl` for visuals).
- **Gap-focused.** One gap per round; the builder attacks only that.
- **Measurable.** Where the bar is quantitative, the verdict must cite a number —
  the bar's real figure vs the agent's measured figure (`kraken-nautilus`,
  `kraken-scylla`).

### The lead agent (kraken composition)

- Chooses the bar (with `kraken-architect` when it's a design/trade-off ref).
- Decomposes into independently-judgeable pieces — smallest slices so each has a
  tight loop.
- Maintains the **live progress page** (`gauntlet-progress.md`), updated each
  round with piece | bar | output | axis | verdict | gap | round.
- Does **not** prescribe architecture or a fixed round count — constrains only the
  bar and the protocol; the builder/critic decide within each piece.
- Fans out per-piece builder + critic via subagents; drives real environments
  (browser, GPU, server) through ultracode.

## Study phase: kraken validation (the crux)

This is where the kraken wrapper earns its keep. After the critic names the gap,
kraken-engineer's Study phase adds:

- **Cross-validation** — the verdict is not accepted until two independent
  signals agree (e.g. a `kraken-nautilus` evidence sweep + a `kraken-pearl`
  visual inspection, or a code result + a `kraken-blitzkrieg-tdd` test result).
- **Measurable-criteria gates** (`kraken-scylla`) — reference completeness,
  acceptance clarity, ambiguity index, dependency clarity, testability, scope
  boundedness. The critic's verdict must pass these before the loop proceeds.

## Act phase: kraken escalation (the stalemate handler)

The standalone `gauntlet-loop` says "loop until win or stop." The kraken version
adds a real stop condition the bare loop lacks:

- If the critic's "biggest gap" has not changed across **two consecutive rounds**
  on the same piece, the loop is **stalemated** — escalate:
  1. `kraken-scylla` audits the bar + axes (the bar may be wrong, or the axes
     don't isolate the real difference).
  2. `kraken-architect` widens or reframes the bar (a shipped comparable may be
     too high a bar for a local variant; widen to the right tier of reference).
  3. `kraken-engineer` re-plans — the piece may split into sub-pieces or merge with
     a neighbor.

The run stops only on: a win/tie on every axis, an explicit stop, or a stalemate
escalation that cannot produce a winnable bar (at which point the bar itself is
wrong and the loop should not continue).

## Quality gates (before declaring a piece done)

- [ ] The critic compared **real, runnable** output against a **real** reference
  bar (`kraken-pearl`/`kraken-nautilus` material), not a description of either.
- [ ] The comparison was **blind** where the bar supports it (labels stripped).
- [ ] The critic named **one** biggest remaining gap per round, not a list.
- [ ] The verdict on each axis is **win / tie / lose**, with a number where the
  bar is quantitative (`kraken-scylla` measurable-criteria gate).
- [ ] Verdict was **cross-validated** by two independent signals.
- [ ] The live progress page reflects the latest verdict for every piece.
- [ ] Stop only on win/tie, explicit stop, or a stalemate escalation — never a
  timer.

## Constraint enforcement

- **No hallucinated bars.** The bar must be a real artifact a fresh critic can
  open. `kraken-architect` converts design/trade-off references into inspectable
  form before they're named as a bar.
- **No self-judgment loops.** The builder does not also critique its own work in
  the same round — the critic is separate context.
- **No scope creep per round.** Each round attacks exactly the gap the previous
  critic named.
- **No fake outputs.** The builder ships real, runnable output; the critic
  inspects real output. Mock summaries are not artifacts — `kraken-blitzkrieg-tdd`
  enforces real test evidence.
- **No stalemate spinning.** If the gap hasn't moved in two rounds, the kraken
  stalemate handler fires before another blind rebuild.

## When not to use

- When the goal is correctness against a spec the agent fully understands and can
  assert — use `kraken-blitzkrieg-tdd` alone (the loop's overhead only pays off
  for quality targets).
- When there is no real, inspectable bar and none can be proposed — the loop has
  nothing to converge on.
- When "done" already means "good enough" (the standard task).
- When the standalone loop is sufficient and process overhead is unwanted — use
  `gauntlet-loop` directly.

## See also

- [`gauntlet-loop`](../../meta/gauntlet-loop/SKILL.md) — the standalone loop
  (shared [references/bar.md](../../meta/gauntlet-loop/references/bar.md) and
  [references/prompt.md](../../meta/gauntlet-loop/references/prompt.md)).
- `kraken-engineer` — the PDSA process this composes with.
- `kraken-scylla` — the critic's measurable-criteria gates and stalemate
  escalation.
- `kraken-architect` — bar selection for design/trade-off references.
- `kraken-nautilus` — systematic evidence for the critic's Study phase.
- `kraken-pearl` — visual/multimodal bar inspection.
- `kraken-blitzkrieg-tdd` — test-first BUILD within each piece.
