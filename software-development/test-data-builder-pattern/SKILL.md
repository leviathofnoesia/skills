---
name: test-data-builder-pattern
description: "Replace brittle test fixtures with composable builder factories."
---

# Test-Data-Builder-Pattern

Replace brittle test fixtures with composable builder factories..

## When to Use

Tests break in cascade because one fixture changed, or every test hand-builds objects with 15 fields.

## Workflow

1. Pick the noisiest fixture type; write a builder with sane defaults per field.
2. Expose chainable overrides only for fields tests actually vary (grep to learn which).
3. Replace fixtures test-by-test; delete shared mutable fixture files as coverage grows.
4. Keep builders in test code only; never import into production paths.
5. Add a builder-conventions note so new builders stay consistent.

## Pitfalls

Builders that grow 30 optional params (moved the noise, not removed it). Shared builders importing production ORM sessions. Overriding everything in one test = builder with no defaults.

## Verification

Fixture-file churn drops over the next N PRs; a deliberately added required field breaks only builders, then fixes in one place.

## Inputs

- Task context: test suite access

## Outputs

- builder factories + retired fixture files + conventions note

## Related

contract-test-bootstrap, flaky-test-triage
