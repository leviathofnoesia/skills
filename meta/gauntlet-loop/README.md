# gauntlet-loop

The original Gauntlet Loop — a self-contained build→critic→rebuild loop that
drives an artifact toward a concrete, inspectable quality bar until the agent's
real output wins or ties the bar in blind A/B comparison.

## What it does

A quality-improvement discipline for when "complete" is not good enough. The
loop has three moving parts:

- **A quality bar, chosen first** — a real, shipped, inspectable artifact (a
  competitor's shipped UI, a published spec, a public benchmark leaderboard)
  that a fresh critic can compare the agent's real output against. If no
  shipped comparable exists, fall back to a measurable property (file size,
  frame budget, error bound, pass rate). No real bar → no loop.
- **A build→critique→compare round** — the builder produces real, runnable
  output; a separate critic inspects it side-by-side with the bar **blind** and
  names the **single biggest remaining gap**; the verdict is win/tie/lose on
  each axis (tie = win; "improved" is not a verdict).
- **A live progress page** — one file updated each round (piece · bar side ·
  output side · axis · verdict · gap · round) so no state is hidden between
  rounds.

It is a **behavior overlay, not a capability** — it composes with the
kraken-engineer family and never overrides their hard constraints.

## Usage

Type `/gauntlet-loop` (or have a lead agent invoke it for autonomous
quality-improvement runs). The skill hands the lead agent a short prompt
([references/prompt.md](references/prompt.md)) and the bar template
([references/bar.md](references/bar.md)); the lead agent decides the
decomposition, axes, and number of rounds.

## Relationship to kraken-gauntlet-loop

[`kraken-gauntlet-loop`](../harness/kraken-skill/kraken-gauntlet-loop/) is the
Kraken-family version: same inner loop, but composed with `kraken-engineer`'s
PDSA process, `kraken-scylla`'s measurable-criteria gates on the critic's
verdicts, and `kraken-architect` for bar selection against design references.
This meta version is the lean, standalone loop for runs that want the loop
without adopting the whole family.
