---
name: refactor-safe-extract
description: "Extract functions/classes behaviorally with seam-first testing."
---

# Refactor-Safe-Extract

Extract functions/classes behaviorally with seam-first testing..

## When to Use

A function/class grew past comprehension and needs splitting without behavior change.

## Workflow

1. Characterize first: pin current behavior with tests at the seam you'll cut (golden outputs, captured calls).
2. Choose extraction order: leaf helpers first, then cohesive clusters.
3. Move code verbatim — zero 'improvements' during the move commit.
4. Re-run characterization after each move; commit per extraction.
5. Only after structure lands, allow behavior-preserving cleanups in separate commits.

## Pitfalls

Mixing moves with edits (unreviewable, un-bisectable). Extracting across hidden temporal coupling. Skipping characterization because 'tests exist' when they test internals, not behavior.

## Verification

Characterization suite green after every commit; each commit contains exactly one extraction; diff review shows pure movement.

## Inputs

- Task context: target module, test runner access

## Outputs

- series of single-purpose extraction commits + reusable seam tests

## Related

dead-code-sweep, type-boundary-hardening
