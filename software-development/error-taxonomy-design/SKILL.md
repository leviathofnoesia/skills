---
name: error-taxonomy-design
description: "Design consistent error types and codes across a codebase."
---

# Error-Taxonomy-Design

Design consistent error types and codes across a codebase..

## When to Use

When error handling is inconsistent (mixed exceptions/codes/strings) or when integrating services that need shared failure vocabulary.

## Workflow

1. Inventory current failure surfaces: raise sites, catch sites, logged strings, HTTP codes.
2. Define layers: user-facing message / machine-readable code / internal cause chain.
3. Assign stable codes by domain (AUTH_*, PAYMENT_*) with documented semantics.
4. Wrap boundaries so internal errors never leak raw internals to clients.
5. Document the taxonomy where contributors will find it.

## Pitfalls

Over-granular codes nobody maintains. Codes that encode implementation details (SQL_TIMEOUT) instead of meaning (DEP_UNAVAILABLE). Swallowing cause chains while wrapping.

## Verification

Every new error site maps to a taxonomy entry; client docs list codes; a grep finds no ad-hoc string errors in new code.

## Inputs

- Task context: codebase access, integration docs if cross-service

## Outputs

- taxonomy doc + refactored error sites + code registry table

## Related

observability-checklist, api-versioning-strategy
