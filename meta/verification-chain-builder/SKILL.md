---
name: verification-chain-builder
description: "Chain claims to checks: every assertion gets a verification step."
---

# Verification-Chain-Builder

Chain claims to checks: every assertion gets a verification step..

## When to Use

Reports/plans contain confident claims with no way to check them.

## Workflow

1. Extract every claim from the artifact into a table.
2. For each: classify verifiable-now / verifiable-later / unfalsifiable.
3. Attach the check: command to run, source to cite, metric to observe.
4. Execute the now-checks; annotate results inline.
5. Ship with the chain attached — readers can audit instead of trust.

## Pitfalls

Chains of checks nobody runs (theater). Checks that verify the check (circularity). Treating unfalsifiable claims as fine if worded confidently.

## Verification

A stranger executes the attached checks and reaches the same conclusions; unfalsifiable claims are flagged or removed.

## Inputs

- Task context: draft document/report

## Outputs

- claim table with executed verification results

## Related

assumption-ledger, self-critique-loop
