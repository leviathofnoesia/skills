---
name: token-budget-forecast
description: "Estimate token cost of a plan before executing it."
---

# Token-Budget-Forecast

Estimate token cost of a plan before executing it..

## When to Use

Planning agent work where cost/context limits are real constraints.

## Workflow

1. Break the plan into steps; classify each: thinking-heavy, tool-heavy, output-heavy.
2. Estimate per step using historical runs (log actuals!); sum with variance band.
3. Compare against budget: context window per turn AND cumulative cost.
4. Redesign hot spots first: cheaper tools, pruning points, batch operations.
5. During execution, compare actual vs forecast to calibrate future estimates.

## Pitfalls

Forecasts without calibration loops (always wrong forever). Ignoring retry costs on flaky steps. Optimizing tokens while burning wall-clock hours elsewhere.

## Verification

Forecast accuracy improves run-over-run (tracked); expensive runs were redesigned before execution, not after.

## Inputs

- Task context: task plan, historical run logs

## Outputs

- cost forecast with variance + redesign of hot spots

## Related

tool-choice-arbiter, context-pruning-pass
