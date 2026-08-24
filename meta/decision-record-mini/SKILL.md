---
name: decision-record-mini
description: "Lightweight ADRs: decision, options considered, why, revert path."
---

# Decision-Record-Mini

Lightweight ADRs: decision, options considered, why, revert path..

## When to Use

Any decision with a revert path worth remembering: library choice, schema shape, architecture tilt.

## Workflow

1. Capture in under 200 words: context, options considered (including do-nothing), choice, primary reason.
2. Add the kill criteria: what evidence would reverse this decision?
3. Note the revert mechanics: how would we actually go back?
4. Commit it next to the code it governs, linked from the PR that made it real.
5. Revisit only when kill criteria trip — not on calendar guilt.

## Pitfalls

ADR bureaucracy (500-line essays nobody reads). Missing kill criteria so decisions become immortal. Records that state WHAT without WHY (history without reasoning).

## Verification

A new team member reading the record understands the constraint space; a tripped kill criterion actually triggers reversal discussion.

## Inputs

- Task context: the decision at hand

## Outputs

- committed mini-ADR

## Related

code-archaeology, assumption-ledger
