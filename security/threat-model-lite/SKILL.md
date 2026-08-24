---
name: threat-model-lite
description: "Lightweight STRIDE threat modeling sized to project stakes."
---

# Threat-Model-Lite

Lightweight STRIDE threat modeling sized to project stakes..

## When to Use

Designing features/systems where abuse matters but full formal threat modeling outweighs the stakes.

## Workflow

1. Enumerate assets worth protecting and trust boundaries they cross.
2. For each boundary, walk STRIDE briefly: Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation.
3. Rate each finding: likelihood × impact; kill the bottom half honestly.
4. Assign mitigations to survivors: built-now, ticketed, or accepted-with-owner.
5. Date-stamp the model; revisit when boundaries move (new integrations = new model).

## Pitfalls

Modeling only external attackers (insiders and dependencies bite more often). Infinite STRIDE depth on trivial surfaces. Mitigations listed but never assigned owners. One-time models fossilizing as systems evolve.

## Verification

Each surviving threat has an owner and a tracked disposition; the model updates when architecture does; a pen-test finds nothing outside your list (or it feeds the next revision).

## Inputs

- Task context: architecture diagram, data flow knowledge

## Outputs

- rated threat list with dispositions + revisit trigger

## Related

failure-mode-catalog, pii-scanner
