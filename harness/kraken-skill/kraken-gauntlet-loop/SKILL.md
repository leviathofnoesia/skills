---
name: kraken-gauntlet-loop
description: >-
  Gauntlet Loop method — the quality-iteration loop that runs inside
  kraken-engineer's PDSA: build→critic→rebuild against a concrete, inspectable
  quality bar until the agent's real output wins or ties the bar in blind A/B,
  never settling for "improved". The bar is chosen first (a real shipped
  comparable, spec, or benchmark — or a measurable property if none exists),
  then the goal is decomposed into the smallest independently-judgeable pieces,
  each fanning out a builder and a separate harsh critic. Part of the
  kraken-engineer mindset family — adopt directly; compose with kraken-engineer
  for process, kraken-scylla for the critic's measurable-criteria gates, and
  kraken-architect for choosing the bar when the reference is a design/trade-off
  decision.
---

# Gauntlet Loop

Iterative quality-improvement loop. Use when a task needs to get *good*, not
just done — "complete" is insufficient and the goal is a quality target judged
against a real reference. This is the **quality** loop that runs *inside*
`kraken-engineer`'s PDSA cycle (Adopt → Plan → Do → Study → Act): the
decomposition, tool selection, and delegation all follow kraken-engineer; the
gauntlet loop governs the inner build→critique→rebuild rhythm and the bar that
stops it.

## Adoption (compose with the family)

- **kraken-engineer first** — this skill supplies the *quality protocol*;
  kraken-engineer supplies the *process* (pre-planning, phase discipline,
  evidence-gated completion). When you reach for the gauntlet loop, adopt
  kraken-engineer's `references/constraints.md` pre-planning as your Phase 0.
- **kraken-architect** — adopt when choosing the bar if the reference is a
  design/trade-off decision rather than a shipped artifact.
- **kraken-scylla** — adopt for the critic's gates: a verdict must carry
  measurable criteria, not a vibe.

## Built-in Pre-Planning — pick the bar before the builders fire

The bar is the **single concrete, inspectable, comparable** artifact a critic
judges the agent's real output against. It is chosen **before round 1**, not
rationalized after the first draft. Without a real bar, every critic is just
the agent evaluating its own work.

See [references/bar.md](references/bar.md) for the bar template, the canonical
comparison sentence, and the fallback rule. The Claude-of-Duty precedent:
Matt Shuer's prompt names real Call of Duty screenshots as the bar — a real,
shipped, inspectable AAA artifact any fresh critic can open and judge blind.

**The bar for this task:**

> The bar is a real, in-production reference artifact — a shipped comparable
> product for functional quality, a published spec/RFC for correctness, or a
> public benchmark leaderboard for performance — that the critic inspects
> side-by-side with the agent's real output, blind, and judges on the same axes
> until the agent's output wins or ties, or the run is stopped.

If no comparable real artifact exists, **the bar is wrong** — fall back to a
measurable property (file size, frame budget, error bound, test pass rate,
round-trip fidelity against spec example vectors) any critic can check without
judgment. A measurable bar is still a bar; a hand-wave is not.

## Do — the loop

One bar, one lead agent, N independent pieces. The lead agent decomposes the
goal into the smallest pieces that can be improved and judged independently,
then for each important piece fans out **a builder** and **a separate critic**
with fresh context.

### Round protocol (per piece)

1. **BUILD** — the builder produces **real, runnable, inspectable** output for
   the piece. Not a plan, not a summary — the actual artifact (code that
   compiles/runs, a rendered file on disk, a test result, a measurement). This
   is kraken-engineer's "Do": run it, don't just read it.
2. **CRITIQUE** — the critic opens the bar AND the real output, **side by side,
   blind** (it does not know which is which on each side when possible). It
   identifies the **single biggest remaining gap** on the axes and hands it back
   verbatim as the next build brief — no re-interpretation.
3. **COMPARE** — the critic states, explicitly, whether the new output **wins,
   ties, or still loses** on each axis. **Tie = win** — indistinguishable on
   the axes is indistinguishable. "Improved" is not a verdict; only win/tie/
   lose is.
4. **LOOP** — until wins/ties on every axis, or stopped.

### The critic

- **Harsh.** The default assumption is that the latest output still loses.
- **Blind.** When the bar supports it (visual, UI, audio), lay the two side by
  side without labels so authorship doesn't bias the call.
- **Gap-focused.** Name the biggest gap only — not a laundry list. The builder
  fixes that one gap; a new critic round judges only whether it closed it.
- **Real-output only.** The critic never compares two drafts of the agent's work
  against each other; it compares the agent's real output **to the bar**.
- **Measurable gates (adopt kraken-scylla).** Every verdict carries a
  measurable claim ("Coherence score 4.2/5 vs the reference's 4.8" or "3
  failing spec vectors, was 17") — not "looks better".

### The lead agent

- Chooses the bar (if none supplied) and the axes of comparison, using
  `kraken-architect` for design references.
- Decomposes the goal into independently-judgeable pieces — smallest possible
  slices so each has a tight, local loop.
- Maintains a **live progress page** (a single file, e.g. `gauntlet-progress.md`
  or an HTML dashboard) updated each round. Columns: piece · bar side · agent
  output side · axis · verdict (win/tie/lose) · biggest gap · round · who.
  The page is the record; no hidden state between rounds.
- Does **not** prescribe the architecture or a fixed round count. It constrains
  only the bar and the protocol; the builder and critic decide the approach
  within each piece.
- Uses subagents for the per-piece builder/critic fan-out. Where the goal needs
  a real environment (a browser, a GPU, a running server), drives that through
  ultracode rather than describing it.

## Study (validate — inspect, don't affirm)

Adopt kraken-engineer's Study phase on every round:

- **Cross-validate.** The critic's verdict rests on at least two independent
  signals — the blind A/B judgment *and* a measurable check (a metric, a spec
  vector, a benchmark run). Two signals, not one.
- **Real-output proof.** The builder proves the output runs/renders where the
  bar is a live artifact (a shipped game's frame, a spec's example vector, a
  benchmark's reported score) — it doesn't describe it.
- **No self-judgment.** The builder does not critique its own work in the same
  round — the critic is separate context, fresh to the bar.

## Act — stop, ship, or escalate

For each piece, the loop ends only on:

- **win or tie** on every axis → the piece is done; move on.
- **explicit stop** → ship what exists, flagged as unfinished, with the last
  critic's gap named as the reason.
- **stalemate** (the gap hasn't moved across rounds) → escalate to an
  architect-level call (adopt `kraken-architect`) or widen the bar — the loop
  is thrashing, not converging.

## Quality gates (before declaring a piece done)

- [ ] The critic compared the **real, runnable** output against the **real
      reference bar** (not a description of either) — and showed it (screenshots,
      traces, measurements).
- [ ] The comparison was **blind** where the bar supports it (labels stripped).
- [ ] The critic named **one** biggest remaining gap per round, not a list.
- [ ] The verdict on each axis is **win / tie / lose** — "improved" is a
      non-verdict and sends it back for re-judgment.
- [ ] Each verdict carries a **measurable** claim (a number, a vector count, a
      pass/fail count) — not "looks better".
- [ ] The live progress page reflects the latest verdict for every piece, with
      the round number and the critic's identity.
- [ ] The run stops only on a win/tie, an explicit stop, or a flagged stalemate
      — not on a timer.

## Constraint enforcement (hard — never violate)

- **No hallucinated bars.** The bar must be a real artifact you can point a
  fresh critic at. "As good as a real CoD game" without showing the screenshots
  is not a bar; neither is "high quality".
- **No self-judgment loops.** The builder does not also critique its own work
  in the same round — the critic is separate context.
- **No scope creep per round.** Each round attacks exactly the gap the previous
  critic named.
- **No fake outputs.** The builder ships real, runnable output; the critic
  inspects real output. Mock summaries, prose descriptions, or "imagine it looks
  like…" are not artifacts.
- **No non-verdicts.** "Improved", "close", "almost there" are not allowed as
  loop terminators — only win/tie/lose stops the round.

## When not to use

- When the goal is correctness against a spec the agent fully understands and
  can assert — use TDD (`kraken-blitzkrieg-tdd`) instead; the spec's example
  vectors *are* the bar and a test is the critic.
- When there is no real, inspectable bar and none can be proposed (no shipped
  comparable, no spec, no benchmark) — the loop has nothing to converge on.
- When "done" already means "good enough" (the standard task) — the overhead
  only pays off for quality targets.

## See also

- [references/bar.md](references/bar.md) — bar template + Claude-of-Duty
  comparison sentence + fallback rule.
- [references/prompt.md](references/prompt.md) — the copy-pasteable agent prompt.
- [`kraken-engineer`](../kraken-engineer/SKILL.md) — the process overlay; the
  gauntlet loop is the quality loop inside its PDSA cycle.
- [`kraken-scylla`](../kraken-scylla/SKILL.md) — adopt for the critic's
  measurable-criteria gates.
- [`kraken-architect`](../kraken-architect/SKILL.md) — adopt when choosing the
  bar against a design/trade-off reference.
- [`kraken-pearl`](../kraken-pearl/SKILL.md) — adopt when the bar is a visual
  or multimedia artifact that needs evidence-bound inspection.
