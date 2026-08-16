# Agent Prompt (Claude Code / Codex / Ultraviolet)

Short. The lead agent, the builders, and the critics all receive the same prompt
skeleton; only the role and the bar differ. Keep it minimal: the agents decide
the specifics.

```
You are running a Gauntlet Loop against this bar:

[BAR]

Axes of comparison (locked):
- [AXIS 1]
- [AXIS 2]
- ...

Goal:
[GOAL]

Protocol:
1. Pick the bar before round 1 (it is already chosen above: do not renege).
2. Decompose the goal into the smallest pieces a builder + separate critic can
   judge independently.
3. For each important piece, fan out a builder and a critic with fresh context.
4. Round per piece: BUILD real output → CRITIQUE blind side-by-side vs bar →
   COMPARE (verdict: win/tie/lose per axis) → LOOP on the named gap.
5. The critic names ONE biggest remaining gap only, verbatim as the next build
   prompt: no re-interpretation.
6. Verdict is win/tie/lose, never "improved". Tie wins.
7. Maintain a live progress page: gauntlet-progress.md (or HTML) updated each
   round: piece | bar | output | axis | verdict | gap | round.
8. Run until wins/ties on every axis, or stopped.

Role: [LEAD | BUILDER | CRITIC]
If LEAD: you plan, decompose, maintain the progress page, and keep the loop honest.
If BUILDER: produce the real, runnable artifact for your piece. Do not critique.
If CRITIC: open the bar AND the builder's real output side by side, blind. Name
the single biggest gap and the win/tie/lose verdict per axis. Do not redesign.

Use subagents for fan-out. Drive real environments (browser/GPU/server) through
ultracode: never describe output instead of producing it.

References:
- Bar template: references/bar.md
- This skill: gauntlet-loop (standalone) or kraken-gauntlet-loop (kraken family)
```
