---
name: api-versioning-strategy
description: "Choose and implement an API versioning scheme that ages well."
---

# Api-Versioning-Strategy

Choose and implement an API versioning scheme that ages well..

## When to Use

External consumers exist (or will) and breaking changes loom.

## Workflow

1. Classify surface: URL-path, header, or payload versioning fits which consumer behavior?
2. Define compatibility promise explicitly (what changes are non-breaking).
3. Set deprecation policy: notice period, sunset headers, usage telemetry.
4. Implement negotiation early even if v1 is the only version.
5. Track per-consumer version adoption to know when retirement is safe.

## Pitfalls

Versioning everything including bugfixes. Breaking payload semantics without bumping the number. No telemetry, so 'nobody uses v1' is folklore.

## Verification

Documented policy page exists; a breaking change simulation shows detection (telemetry + contract tests); deprecation comms template ready.

## Inputs

- Task context: API spec, consumer inventory

## Outputs

- versioning decision record + deprecation policy + adoption dashboard

## Related

contract-test-bootstrap, sdk-design-review
