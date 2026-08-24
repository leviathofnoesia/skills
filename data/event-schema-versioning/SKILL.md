---
name: event-schema-versioning
description: "Version analytics events so downstream queries never break."
---

# Event-Schema-Versioning

Version analytics events so downstream queries never break..

## When to Use

Analytics events evolve freely until downstream queries break or metrics silently shift meaning.

## Workflow

1. Define event contracts: required fields, types, semantic meaning — documented per event.
2. Classify proposed changes: additive (safe), narrowing (breaking), semantic (nuclear).
3. Version breaking changes as NEW events rather than mutating existing ones.
4. Maintain dual-write windows during producer migration; validate consumer cutover before retiring old versions.
5. Enforce contracts at emit-time validation so bad events die at birth.

## Pitfalls

Overloading existing fields with new meanings ('status field now also means...'). Consumers nobody knows about depending on 'deprecated' events. Emit-time validation missing so contract drift ships silently.

## Verification

Schema registry shows versioned contracts; emit-time validation blocks violations in staging; deliberate breaking change gets caught before prod.

## Inputs

- Task context: event inventory, consumer map

## Outputs

- versioned schema registry + validation gates

## Related

contract-test-bootstrap, metric-definition-sheet
