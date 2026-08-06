---
name: gauntlet-loop
description: >-
  The original Gauntlet Loop — a self-contained build→critic→rebuild loop that
  drives an artifact toward a concrete, inspectable quality bar until the
  agent's real output wins or ties the bar in blind A/B comparison. Pick the
  bar first; decompose into smallest judgeable pieces; per piece fan out a
  builder and a separate harsh critic; critic inspects real output vs bar blind,
  names the single biggest remaining gap, verdict win/tie/lose; loop until win
  or stop. Lead agent keeps a live progress page. Use when a task needs to get
  good, not just done.
---

# Gauntlet Loop

Iterative quality-improvement loop. Use when a task needs to get *good*, not
just done — "complete" is insufficient and the goal is a quality target judged
against a real reference.

## Core rule: pick the bar before the builders fire

The bar is the **single concrete, inspectable, comparable** artifact a critic
judges the agent's real output against. It is chosen **before round 1**, not
rationalized after the first draft. Without a real bar, every critic is just the
agent evaluating its own work.

See [references/bar.md](references/bar.md) for the bar template, the canonical
comparison sentence, and how to choose when no shipped product exists. The
Claude-of-Duty precedent: Matt Shumer's prompt names real Call of Duty
screenshots as the bar — a shipped, inspectable AAA artifact any fresh critic can
open and judge blind.

The bar sentence for this task:

> The bar is a real, in-production reference artifact — a shipped comparable
> product for functional quality, an published spec/RFC for correctness, or a
> public benchmark leaderboard for performance — that the critic inspects
> side-by-side with the agent's real output, blind, and judges on the same axes
> until the agent wins or ties, or the run is stopped.

If no comparable real artifact exists, **the bar is wrong** — fall back to a
measurable property (file size, frame budget, error bound, test pass rate,
round-trip fidelity against spec example vectors) any critic can check without
judgment.

## The loop

One bar, one lead agent, N independent pieces. The lead agent decomposes the
goal into the smallest pieces that can be improved and judged independently,
then for each important piece fans out **a builder** and **a separate critic**
with fresh context.

### Round protocol (per piece)

1. **BUILD** — the builder produces real, runnable, inspectable output for the
   piece. Not a plan, not a summary — the actual artifact (code, a rendered
   file, a test result, a measurement).
2. **CRITIQUE** — the critic opens the bar AND the real output, **side by side,
   blind** (it does not know which is which on each side when possible). It
   identifies the **single biggest remaining gap** on the axes and sends it back
   verbatim as the prompt for the next build round — no re-interpretation.
3. **COMPARE** — the critic states, explicitly, whether the new output wins,
   ties, or still loses on each axis. Tie = win (indistinguishable on the axes
   is indistinguishable).
4. **LOOP** — until wins/ties on every axis, or stopped.

### The critic

- **Harsh.** The default assumption is that the latest output still loses.
- **Blind.** When the bar is visual, lay the two side by side without labels so
  authorship doesn't bias the call.
- **Gap-focused.** Name the biggest gap only — not a laundry list. The builder
   fixes that one gap; a new critic round judges only whether it closed it.
- **Real-output only.** The critic never compares two drafts of the agent's
work against each other; it compares the agent's real output **to the bar**.

### The lead agent

- Chooses the bar (if none supplied) and the axes of comparison.
- Decomposes the goal into independently-judgeable pieces — smallest possible
   slices so each has a tight, local loop.
- Maintains a **live progress page** (a single file, e.g. `gauntlet-progress.md`
   or an HTML dashboard) updated each round: piece | bar side | agent output
   side | axis | verdict (win/tie/lose) | biggest gap | round. The page is the
   record; no hidden state between rounds.
- Does **not** prescribe the architecture or a fixed round count. It constrains
   only the bar and the protocol; the builder and critic decide the approach
   within each piece.
- Uses subagents for the per-piece builder/critic fan-out. Where the goal needs
   a real environment (a browser, a GPU, a running server), drives that through
   ultracode rather than describing it.

## Quality gates (before declaring a piece done)

- [ ] The critic compared the **real, runnable** output against the **real
      reference bar** (not a description of either).
- [ ] The comparison was **blind** where the bar supports it (labels stripped).
- [ ] The critic named **one** biggest remaining gap per round, not a list.
- [ ] The verdict on each axis is **win / tie / lose**, not "improved".
- [ ] The live progress page reflects the latest verdict for every piece.
- [ ] The run stops only on a win/tie or on explicit stop — not on a timer.

## Constraint enforcement

- **No hallucinated bars.** The bar must be a real artifact you can point a
   fresh critic at. "As good as a real CoD game" without showing the screenshots
   is not a bar.
- **No self-judgment loops.** The builder does not also critique its own work
   in the same round — the critic is separate context.
- **No scope creep per round.** Each round attacks exactly the gap the previous
   critic named.
- **No fake outputs.** The builder ships real, runnable output; the critic
   inspects real output. Mock summaries are not artifacts.

## When not to use

- When the goal is correctness against a spec the agent fully understands and
   can assert — use TDD instead.
- When there is no real, inspectable bar and none can be proposed — the loop
   has nothing to converge on.
- When "done" already means "good enough" (the standard task) — the overhead
   only pays off for quality targets.

## See also

- [references/bar.md](references/bar.md) — bar template + Claude-of-Duty
   comparison sentence.
- [references/prompt.md](references/prompt.md) — the copy-pasteable agent prompt.
- [`kraken-gauntlet-loop`](../harness/kraken-skill/kraken-gauntlet-loop/SKILL.md)
   — the Kraken-family version that composes this loop with kraken-engineer's
   PDSA process, kraken-scylla's measurable-criteria gates, and kraken-architect
   for bar selection.
