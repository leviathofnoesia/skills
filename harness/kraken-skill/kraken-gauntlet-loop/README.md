# Kraken Gauntlet Loop

Iterative build→critic→rebuild loop that drives an artifact toward a concrete
quality bar. Used when a task needs to get *good*, not just done.

## User-invoked

Reachable when you type `/kraken-gauntlet-loop`, or when a lead agent invokes
it for autonomous quality-improvement runs.

## Files

- `SKILL.md` — the method (bar selection, loop protocol, A/B inspection).
- `references/bar.md` — the canonical bar template + the Claude-of-Duty
  comparison sentence.
- `references/prompt.md` — the short agent prompt (Claude Code / Codex /
  Ultraviolet style) used to seed each builder + critic.

## Related

- [`kraken-engineer`](../kraken-engineer/SKILL.md) — process overlay; the
  gauntlet loop is the *quality* loop that runs inside kraken-engineer's PDSA.
- [`kraken-scylla`](../kraken-scylla/SKILL.md) — plan/artifact audit; the
  critic role adopts scylla's measurable-criteria gates.
