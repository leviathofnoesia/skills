---
name: claim-decay-checker
description: "Check if a cited fact is superseded or retracted."
---

# Claim-Decay-Checker

Check if a cited fact is superseded or retracted..

## When to Use

Reusing facts from older documents, slides, or prior research in current work.

## Workflow

1. Extract dated claims from the source artifact with their original citations.
2. Check each: superseded by newer data? retracted? methodology discredited?
3. Re-verify statistics against the CURRENT primary source (numbers get revised).
4. Flag decay type per claim: stale, corrected, retracted, context-changed.
5. Update or quarantine each claim before reuse; record check date.

## Pitfalls

Trusting your own past work without re-verification (sunk credibility). Checking existence of citation but not whether its content changed. Ignoring domain velocity (medical claims decay faster than mathematical ones).

## Verification

Every reused claim carries a freshness stamp; at least one 'known fact' typically gets flagged — if nothing ever flags, the checker is being trusted too much.

## Inputs

- Task context: source document(s), research access

## Outputs

- claim status table + updated/quarantined content

## Related

source-triangulation, reproducibility-audit
