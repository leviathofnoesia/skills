# kraken-gauntlet-loop

The original Gauntlet Loop, composed into the kraken-engineer process family.

## What it is

The quality-iteration loop that runs inside `kraken-engineer`'s PDSA cycle:
build → critique (blind A/B) → compare (win/tie/lose) → rebuild, governed by a
concrete, inspectable bar chosen before round 1.

## What it adds over the standalone loop

Where [`gauntlet-loop`](../../meta/gauntlet-loop) is the bare protocol, this
variant composes it with the wider kraken method family:

- **Pre-planning** — `kraken-architect` for bar selection (turns design
  trade-off references into an inspectable bar; picks the right tier of
  comparable when none was supplied).
- **Study phase** — `kragon-nautilus` for systematic evidence, `kraken-pearl`
  for multimodal bar inspection, cross-validation by two independent signals.
- **Critique gates** — `kraken-scylla`'s measurable-criteria gates bite hardest
  here: the critic's win/tie/lose must pass acceptance clarity and ambiguity
  checks, and must cite a number where the bar is quantitative.
- **Stalemate escalation** — if the named "biggest gap" hasn't moved across two
  consecutive rounds, `kraken-scylla` audits the bar+axes and `kraken-architect`
  widens it; the loop never spins blind on a wrong bar.
- **BUILD rigor** — `kraken-blitzkrieg-tdd` enforces test-first within each
  independently-judgeable piece; the builder ships real runnable output, not a
  summary.

## When to use which

| Use | Skill |
|---|---|
| Quality target judged vs a real reference, with full process + cross-validation | `kraken-gauntlet-loop` |
| Same loop, no process overhead; lean standalone run | `gauntlet-loop` |
| Correctness against a spec you can assert → TDD, not the loop | `kraken-blitzkrieg-tdd` |

## Files

- [SKILL.md](./SKILL.md) — method, PDSA mapping, stalemate escalation, gates.
- [references/bar.md](./references/bar.md) — shared bar template + Claude-of-Duty comparison.
- [references/prompt.md](./references/prompt.md) — copy-pasteable agent prompt.

## Related

- [`gauntlet-loop`](../../meta/gauntlet-loop) — standalone version (shared references).
- `kraken-engineer` — the PDSA process.
- `kraken-scylla` — measurable-criteria gates + stalemate audit.
- `kraken-architect` — bar selection for design references.
- `kraken-nautilus` — evidence gathering for the critic's Study phase.
- `kraken-pearl` — multimodal (visual) bar inspection.
- `kraken-blitzkrieg-tdd` — test-first BUILD within each piece.
