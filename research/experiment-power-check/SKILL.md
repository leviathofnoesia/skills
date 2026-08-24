---
name: experiment-power-check
description: "Sanity-check sample size and effect size before running tests."
---

# Experiment-Power-Check

Sanity-check sample size and effect size before running tests..

## When to Use

Before running A/B tests or experiments where underpowered results waste weeks.

## Workflow

1. State minimum effect worth detecting (business-relevant, not statistical trivia).
2. Estimate baseline variance from historical data (not assumptions).
3. Compute required N; compare against achievable traffic/duration honestly.
4. If underpowered: redesign (bigger change, better metric, sequential design) rather than run-and-pray.
5. Pre-register the analysis to prevent post-hoc fishing.

## Pitfalls

Detecting tiny effects nobody cares about (statistical significance ≠ business matter). Peeking early and stopping on noise. Assuming variance instead of measuring it. Running multiple metrics and cherry-picking survivors.

## Verification

Written pre-registration exists: hypothesis, N, primary metric, analysis method — created BEFORE first data point.

## Inputs

- Task context: baseline metrics, traffic capacity

## Outputs

- power analysis + go/no-go recommendation + preregistration doc

## Related

metric-definition-sheet, survey-question-design
