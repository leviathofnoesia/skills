---
name: prompt-contract-authoring
description: "Write explicit input/output contracts for reusable prompts."
---

# Prompt-Contract-Authoring

Write explicit input/output contracts for reusable prompts..

## When to Use

A prompt gets reused across sessions/agents and quality drifts because inputs are implicit.

## Workflow

1. Declare inputs explicitly: required variables, types, constraints, what good looks like.
2. Declare outputs: format, length bounds, forbidden content, success examples.
3. Add negative examples: one bad input + why it fails + expected behavior.
4. Version the contract; note behavior changes between versions.
5. Test with three cases: typical, edge, adversarial before trusting it.

## Pitfalls

Contracts so rigid they break on legitimate variation. Implicit context ('as discussed') leaking in. No failure mode defined, so degradation is silent.

## Verification

Two different agents following the contract produce comparable-quality outputs on the same inputs.

## Inputs

- Task context: existing prompt(s), example interactions

## Outputs

- versioned prompt contract with test cases

## Related

instruction-decompiler, verification-chain-builder
