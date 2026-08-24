---
name: type-boundary-hardening
description: "Introduce strict types at module boundaries incrementally."
---

# Type-Boundary-Hardening

Introduce strict types at module boundaries incrementally..

## When to Use

Dynamic/loosely-typed modules cause runtime type errors at integration seams.

## Workflow

1. Pick ONE boundary (module edge, API handler, queue consumer).
2. Define the contract types precisely; validate at entry, trust internally.
3. Add parsing/validation at ingress (schema lib) so bad data fails fast with good messages.
4. Propagate inferred types inward; resist annotating internals prematurely.
5. Repeat per boundary; let strictness diffuse naturally.

## Pitfalls

Annotating everything day one (types lie quickly). Validation duplicated at every layer instead of boundaries. Types so complex they're unreadable — the map outgrew the territory.

## Verification

Malformed input tests fail fast at the boundary with clear messages; internal type errors drop measurably in that module.

## Inputs

- Task context: boundary code, representative payloads

## Outputs

- validated boundary contracts + typed module interiors

## Related

refactor-safe-extract, schema-drift-detector
