---
name: self-critique-loop
description: "Adversarially review own output against the original ask."
---

# Self-Critique-Loop

Adversarially review own output against the original ask..

## When to Use

Before delivering consequential output produced without external review.

## Workflow

1. Restate the ORIGINAL ask verbatim (not what you remember it being).
2. Critique dimensions: correctness, completeness against ask, hidden assumptions, failure to follow format.
3. Attack as adversary: find the strongest case this output is wrong/insufficient.
4. Fix findings; re-critique once (diminishing returns past two passes).
5. Deliver with known-limitations section listing what critique found but couldn't fix.

## Pitfalls

Critiquing your framing instead of the ask. Rubber-stamp passes ('looks good'). Infinite loops polishing past usefulness. Hiding limitations to seem stronger.

## Verification

Second-pass finds materially fewer issues than first; delivered artifact carries honest limitation notes; downstream complaints drop.

## Inputs

- Task context: draft output, original request

## Outputs

- revised output + limitations list

## Related

verification-chain-builder, assumption-ledger
