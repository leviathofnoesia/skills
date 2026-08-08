# The Quality Bar

The bar is the single concrete, inspectable, comparable artifact a critic judges
the agent's real output against. It is chosen **before round 1**, not rationalized
after the first draft. Without a real bar, every critic is just the agent
evaluating its own work.

## The canonical comparison sentence (Claude-of-Duty precedent)

> The bar is a real, in-production reference artifact — a shipped comparable
> product for functional quality, a published spec/RFC for correctness, or a
> public benchmark leaderboard for performance — that the critic inspects
> side-by-side with the agent's real output, blind, and judges on the same axes
> until the agent wins or ties, or the run is stopped.

This mirrors how Matt Shumer's Claude-of-Duty prompt names real Call of Duty
screenshots as the bar: a shipped, inspectable AAA artifact any fresh critic can
open and judge blind. The bar must be something a completely fresh set of eyes
(or a fresh critic agent with clean context) can open and call a winner on.

## How to choose the bar

1. **Look for a real shipped comparable first.** A product, design, spec, or
   benchmark that already exists in production and that the critic can open and
   look at directly (a live URL, a real screenshot, a published document, a
   public leaderboard row).
2. **Define the axes of comparison up front.** Functional parity? Visual
   fidelity? Output size? Latency? Correctness vs spec? Name 1–3 axes and lock
   them — the critic judges only on these.
3. **If no comparable real artifact exists, the bar is wrong.** Fall back to a
   **measurable property** any critic can check without judgment:
   - File size, line count, token count.
   - Frame budget / render time / memory.
   - Error bound, tolerance, accuracy threshold.
   - Test pass rate against spec example vectors.
   - Round-trip fidelity (encode → decode → diff against original).
4. **When the reference is a design/trade-off decision** (vs a shipped product),
   it is not yet an inspectable bar — adopt `kraken-architect` to turn it into one
   (a design doc, a reference implementation, a benchmark) before naming it the
   bar.

## What the critic does with the bar

- Opens the bar AND the agent's real output, side by side, blind (strips labels
  where the bar supports it).
- Names the single biggest remaining gap on the locked axes.
- States the verdict on each axis as win / tie / lose (tie = win).
- "Improved" is a non-verdict — send back and re-run the round.

## Anti-patterns

- ❌ Naming "as good as [product]" without pointing at a real, openable artifact.
- ❌ Judging the agent's output against a *description* of the bar instead of the
  bar itself.
- ❌ Comparing two drafts of the agent's own work against each other (that is not
  a bar comparison).
- ❌ Changing the axes mid-run to suit the latest output.
