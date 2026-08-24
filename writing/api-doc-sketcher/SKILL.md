---
name: api-doc-sketcher
description: "Draft reference docs from real signatures and call sites."
---

# Api-Doc-Sketcher

Draft reference docs from real signatures and call sites..

## When to Use

API endpoints exist but docs lag, drift, or don't exist.

## Workflow

1. Extract ground truth from code: routes, methods, parameters, response shapes (from real serialization).
2. Document the happy path per endpoint with a REAL request/response pair captured from execution.
3. Document error responses from the error taxonomy — every code a client can see.
4. Add authentication/rate-limit context where relevant.
5. Wire doc examples into CI so drift fails builds.

## Pitfalls

Docs written from intention instead of execution (types drift). Missing error documentation until clients hit them blind. Examples with fake data that would never validate. Auth documented separately from everything it affects.

## Verification

Every documented example executes successfully against a real instance in CI; undocumented-endpoint scanner returns empty.

## Inputs

- Task context: running API instance, route source code

## Outputs

- executable-example docs + drift protection

## Related

sdk-design-review, error-taxonomy-design
