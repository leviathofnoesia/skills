---
name: sample-before-model
description: "Profile distributions and leakage before any modeling."
---

# Sample-Before-Model

Profile distributions and leakage before any modeling..

## When to Use

Modeling/prediction work begins before anyone has looked at the actual data distributions.

## Workflow

1. Profile univariate distributions: ranges, modes, missingness patterns, impossible values (age 900).
2. Check pairwise relationships against domain expectations; investigate surprising zeros or perfect correlations (leakage suspects).
3. Examine target balance and its collection mechanism (missing-not-at-random poisons everything).
4. Split BEFORE feature engineering; verify split integrity (no temporal leakage, group leakage).
5. Write findings as constraints on modeling choices before any model runs.

## Pitfalls

Looking only at summary stats (means hiding bimodality). Leakage discovered via suspiciously good results instead of inspection. Imputing before understanding WHY values are missing. Testing on the tuning set by accident of repetition.

## Verification

Written profile document exists with anomalies explained (not just listed); leakage checks documented; splits provably clean.

## Inputs

- Task context: raw dataset, domain knowledge access

## Outputs

- data profile + leakage audit + modeling constraint list

## Related

experiment-power-check, dataset-provenance
