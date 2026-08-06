# Agent Prompt (Claude Code / Codex / Ultraviolet)

Short. The lead agent, the builders, and the critics all receive the same
prompt skeleton; only the **role** and the **bar** differ. Keep it minimal —
the agent decides the decomposition, the axes, the number of rounds.

```prompt
I want you to build <GOAL> to a quality level where a fresh, harsh critic
cannot distinguish your real output from <the real reference bar> when put
side by side blind.

[BAR]
<the bar, as a concrete, inspectable artifact + the comparison axes + the
pass criterion — see references/bar.md>

[OPTIONAL REFERENCES]
<any real references the agent should compare against]

Choose the strongest concrete bar that an agent can actually inspect and
compare its work against. If none was supplied, propose one and say why it
plays the same role for this task that real Call of Duty screenshots play for
Matt Shumer's Claude of Duty.

Give the lead agent the goal and the bar, but let it choose the approach.
Tell it to divide the goal into the smallest pieces that can be improved and
judged independently. For each important piece, it should fan out a builder
and a separate critic with fresh context.

Each critic must inspect the real output, compare it directly with the bar —
using a blind A/B comparison when possible — identify the biggest remaining
gap, and send it back for another round. Keep looping until the output wins or
is stopped.

The lead agent maintains a simple live progress page that shows the work
evolving over time.

Have it use subagents and ultracode. Do not prescribe the architecture,
exact decomposition, or a fixed number of rounds. Keep the final prompt short.
```
