---
name: stat-claim-decoder
description: "Decode headline statistics into their honest strength."
---

# Stat-Claim-Decoder

Decode headline statistics into their honest strength..

## When to Use

Headline statistics ('3x faster!', '47% of users') arrive destined for decisions or replication.

## Workflow

1. Ask what was MEASURED precisely: population, metric definition, measurement window.
2. Find the denominator and base rate (47% of WHO? 3x faster than WHAT baseline?).
3. Check for selection effects: who was included, who self-selected out, survivorship shapes.
4. Distinguish correlation phrasing from causal claims; flag leap words ('leads to', 'because').
5. Restate the claim at its honest strength; note what evidence WOULD establish the stronger version.

## Pitfalls

Accepting relative improvements without absolutes (50% reduction! ...of a 0.02% base). Missing Simpson's paradox in aggregated slices. Treating survey respondents as populations. Precision signaling importance (decimals on noise).

## Verification

Restated claim survives the original author's review (they agree it's fair); decisions cite the restated version.

## Inputs

- Task context: the statistical claim, source access

## Outputs

- decoded restatement + strength assessment

## Related

source-triangulation, experiment-power-check
