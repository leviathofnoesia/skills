# The Quality Bar

The bar is the single concrete, inspectable thing an agent can compare its work
against. It exists so the loop has a north star that is **not** the agent's own
opinion of its work. Without one, every round just shuffles the same judgment.

## How to choose

A good bar is:

1. **Concrete** — it names a specific, observable artifact or measurable.
2. **Inspectable** — a fresh critic can open it and form an opinion in one
   read, with no inference.
3. **Comparable** — the agent's output and the bar can be put side by side and
   judged on the same axes.

## Template (fill before round 1)

```
## Bar
<one sentence naming the artifact + the comparison frame>

## Axes of comparison
- <observable axis 1>
- <observable axis 2>
- <observable axis 3>

## Pass criterion
<precise condition that counts as "won">
```

## Example: a ThreeJS FPS (mirrors Claude-of-Duty)

> Build a first-person shooter at the level of the most recent Call of Duty
> games — visually beautiful, every system at AAA quality — and fan out
> sub-agents with a separate harsh critic per system, comparing each directly
> against real current Call of Duty screenshots in a blind A/B until the
> agent's version wins or is indistinguishable.

**Bar sentence:** The bar is a real, in-production AAA reference artifact —
current Call of Duty screenshots for visual fidelity, or a shipped comparable
product for functional quality — that the critic inspects side-by-side with the
agent's real output, blind, and judges on the same axes until the agent wins or
you stop the run.

**Why this bar works:** current CoD is not aspirational — it is a real,
shipped, inspectable artifact any fresh critic can open and judge. The agent
cannot argue with it; it can only close the gap. The bar is therefore
*comparative* (A/B), *blind* (no bias toward authorship), and *converging*
(loop until the agent wins, not just until it "looks good").

## When the goal has no shipped product to compare against

Pick the **closest real reference** and state the gap explicitly:

- A shipped competitor's UI → visual/interaction bar.
- A published API spec / RFC → correctness bar (the output must round-trip
  the spec's example vectors).
- A benchmark suite with a public leaderboard → performance/size bar.
- A human-produced exemplar → quality/fidelity bar.

**If no comparable real artifact exists, the bar is wrong.** Fall back to a
measurable property (file size, frame budget, error bound, test pass rate)
that any critic can check without judgment.

## Pass / no-pass

The run ends when **either**:

- the critic declares the agent's real output **wins or ties** the bar on every
  axis (blind A/B), or
- you stop the run.

A "tie" is a win: indistinguishable-on-the-axes is indistinguishable-on-the-axes.
