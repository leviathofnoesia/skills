---
name: assumption-ledger
description: "Track assumptions explicitly and revisit them before shipping."
---

# Assumption-Ledger

Track assumptions explicitly and revisit them before shipping..

## When to Use

Plans rest on unspoken beliefs about users, systems, or timelines that could silently invalidate the work.

## Workflow

1. List assumptions as testable statements: 'X is true because we observed Y'.
2. Rate each: blast radius if wrong × likelihood wrong.
3. Assign cheapest possible test for high-risk entries; schedule before dependent work.
4. Review ledger at milestones: which assumptions got confirmed/killed?
5. Kill or promote: killed assumptions trigger plan revision, not sadness.

## Pitfalls

Ledgers written then never revisited (cargo ritual). Vague assumptions that can't fail ('users want quality'). Testing comfortable assumptions while dangerous ones ride along.

## Verification

Every high-blast-radius assumption has either a completed test result or a scheduled date; at least one assumption died and changed the plan (proves the loop works).

## Inputs

- Task context: plan/design doc

## Outputs

- living ledger + scheduled validation tasks

## Related

verification-chain-builder, decision-record-mini
