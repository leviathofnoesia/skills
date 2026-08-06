# gauntlet-loop

The original Gauntlet Loop — a self-contained build→critic→rebuild loop that
drives an artifact toward a concrete, inspectable quality bar until the
agent's real output wins or ties the bar in blind A/B comparison. Pick the
bar first; decompose into smallest judgeable pieces; per piece fan out a
builder and a separate harsh critic; critic inspects real output vs bar blind,
names the single biggest remaining gap, verdict win/tie/lose; loop until win or
stop. Lead agent keeps a live progress page. Use when a task needs to get good,
not just done.

## What it is

A lean, standalone quality-improvement protocol. No process scaffolding — just
the loop and its constraints. The lead agent chooses a real, inspectable bar
(shipped comparable, spec, or benchmark — or a measurable property if none
exists), decomposes the goal into the smallest independently-judgeable pieces,
and for each piece fans out a builder + a separate harsh critic. The critic
inspects real output vs the real bar blind, names the single biggest gap, and
verdicts win/tie/lose. Loop until win/tie or stop.

## What it adds compared to kraken-gauntlet-loop

Nothing — it is the *base* protocol. `kraken-gauntlet-loop` is this loop plus the
kraken-engineer PDSA wrapper (pre-planning bar selection via `kraken-architect`,
Study-phase cross-validation via `kraken-nautilus`/`kraken-pearl`, measurable
gates via `kraken-scylla`, stalemate escalation, and `kraken-blitzkrieg-tdd`
test-first BUILD). Use the standalone version when you want the loop with no
process overhead; use the kraken version when you also want process rigor and
cross-validation.

## When to use which

| Use | Skill |
|---|---|
| Quality target judged vs a real reference, no process overhead | `gauntlet-loop` (this skill) |
| Same loop + kraken-engineer PDSA process, cross-validation, stalemate escalation | `kraken-gauntlet-loop` |
| Correctness against a spec you can assert → TDD | `kraken-blitzkrieg-tdd` |

## Files

- [SKILL.md](./SKILL.md) — method: bar-first rule, round protocol, critic constraints, lead-agent duties, quality gates, constraint enforcement.
- [references/bar.md](./references/bar.md) — bar template + the Claude-of-Duty comparison sentence + how to choose when no shipped product exists.
- [references/prompt.md](./references/prompt.md) — copy-pasteable agent prompt (Claude Code / Codex / Ultraviolet style).

## Related

- [`kraken-gauntlet-loop`](../harness/kraken-skill/kraken-gauntlet-loop/SKILL.md) — the kraken-family version with full process composition.
- `kraken-engineer` — the PDSA process.
- `kraken-scylla` — measurable-criteria gates + stalemate audit.
- `kraken-architect` — bar selection for design references.
- `kraken-nautilus` — evidence gathering.
- `kraken-pearl` — multimodal bar inspection.
- `kraken-blitzkrieg-tdd` — test-first BUILD.

The bar sentence (canonical):

> The bar is a real, in-production reference artifact — a shipped comparable
> product for functional quality, a published spec/RFC for correctness, or a
> public benchmark leaderboard for performance — that the critic inspects
> side-by-side with the agent's real output, blind, and judges on the same axes
> until the agent wins or ties, or the run is stopped.
