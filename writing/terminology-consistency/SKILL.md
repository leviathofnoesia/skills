---
name: terminology-consistency
description: "Enforce one term per concept across a doc set."
---

# Terminology-Consistency

Enforce one term per concept across a doc set..

## When to Use

Docs/UI use multiple words for the same concept (user/account/customer) confusing readers and translators.

## Workflow

1. Extract candidate terms per concept across all surfaces (docs, UI strings, code identifiers).
2. For each concept, choose canonical term by: user mental model fit, existing dominance, translation friendliness.
3. Build the canonical glossary: term, definition, forbidden synonyms, rationale.
4. Sweep surfaces: exact-match replacement plus fuzzy variants (pluralization, casing).
5. Install guards: lint rule or CI grep preventing regression.

## Pitfalls

Renaming public-facing terms users already know (migration cost > consistency win). Code identifiers forced into user terminology when domain terms differ legitimately. Glossary written once, abandoned.

## Verification

Glossary exists at point-of-writing; synonym scan returns only justified exceptions; translators confirm reduced ambiguity.

## Inputs

- Task context: docs corpus, UI strings, code search

## Outputs

- canonical glossary + swept surfaces + regression guard

## Related

style-guide-distiller, translation-handoff-kit
