---
name: contract-test-bootstrap
description: "Stand up consumer-driven contract tests between two services."
---

# Contract-Test-Bootstrap

Stand up consumer-driven contract tests between two services..

## When to Use

Two teams/services share an HTTP or event contract and breakage is found in integration instead of CI.

## Workflow

1. Pick the contract source of truth (OpenAPI, protobuf, JSON schema).
2. Consumer writes expectations as executable examples against a mock provider.
3. Provider verifies those examples against its real implementation in its own CI.
4. Wire broker or repo-based pact storage; fail provider CI on unmet expectations.
5. Add can-i-deploy check to release flow.

## Pitfalls

Contracting implementation details instead of the interface. Letting contracts rot (no owner). Testing every field when only breaking-change fields matter.

## Verification

A deliberately incompatible provider change fails provider CI before deploy; consumer sees no integration surprises for covered endpoints.

## Inputs

- Task context: both services' repos, contract schema if it exists

## Outputs

- consumer expectation suites + provider verification jobs wired into CI

## Related

api-contract-diff, api-versioning-strategy
