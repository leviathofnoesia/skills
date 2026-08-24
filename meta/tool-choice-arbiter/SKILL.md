---
name: tool-choice-arbiter
description: "Pick the cheapest sufficient tool for each subtask step."
---

# Tool-Choice-Arbiter

Pick the cheapest sufficient tool for each subtask step..

## When to Use

Agents burn tokens using heavyweight tools where lightweight ones suffice, or flail between equivalent options.

## Workflow

1. Inventory available tools with cost profile: latency, token weight, side effects.
2. Define the ladder: cheapest sufficient first (read > search > browse > execute).
3. Attach decision rules: file known → read directly; unknown location → search; cross-page → browse.
4. Log choices for a run; review escalations that shouldn't have happened.
5. Refine rules from evidence, not vibes.

## Pitfalls

Ladders that ignore correctness for cost (wrong-but-cheap). Rules written once and never revisited. Punishing exploration that was actually needed.

## Verification

Task completion cost drops with no rise in failures; escalation log shows each heavy-tool use had justification.

## Inputs

- Task context: task description, tool inventory

## Outputs

- decision ladder + per-run choice audit

## Related

token-budget-forecast, retry-policy-designer
