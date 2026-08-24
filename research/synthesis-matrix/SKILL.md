---
name: synthesis-matrix
description: "Merge many sources into a claim-by-source evidence matrix."
---

# Synthesis-Matrix

Merge many sources into a claim-by-source evidence matrix..

## When to Use

Many sources say many things and the pattern across them matters more than any single one.

## Workflow

1. Extract atomic claims per source into rows; sources as columns.
2. Normalize terminology so equivalent claims align (define mapping explicitly).
3. Mark cells: supports / contradicts / silent / qualified-support (with nuance noted).
4. Read columns for source bias patterns; read rows for claim robustness.
5. Synthesize: robust claims (multi-source support), contested (named disagreement), lonely claims (single source).

## Pitfalls

Matrix theater: beautiful tables encoding garbage extraction. False equivalence between source quality levels. Losing qualifiers ('works except under X' becoming 'works').

## Verification

Spot-check five random cells against their sources — all verified accurate; contested claims name their specific disagreeing parties.

## Inputs

- Task context: source corpus, extraction time

## Outputs

- evidence matrix + robustness-ranked claim list

## Related

literature-scan, source-triangulation
