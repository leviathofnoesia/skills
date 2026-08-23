---
name: api-contract-diff
description: "Detect breaking changes between two versions of a public HTTP/API surface."
---

# API Contract Diff

Compare two versions of an API's public contract — OpenAPI specs, route
tables, generated clients, or hand-written route files — and classify every
change as breaking, additive, or behavioral. For release notes, semver
checks, and consumer-impact review.

## When to Use

- Before tagging a release, after refactoring routes/handlers, when a spec
  file changes, or when asked "did we break the API", "is this backwards
  compatible". Works from OpenAPI/AsyncAPI specs or directly from framework
  route definitions.
- Differentiator: classifies against real consumer impact — what a correct,
  existing client would experience — not textual diff similarity.

## Workflow

1. **Extract both contracts.** From each side collect: routes (method +
   path template), request body schema, response status codes + schemas,
   required params/headers, auth requirements, error shapes. Prefer
   machine-readable sources (OpenAPI JSON/YAML) over prose docs.
2. **Classify each difference:**
   - *Breaking*: removed/renamed route or field; field becomes required;
     type change; new required param/header; response code narrowed
     (200→204); enum value removed; auth added or tightened.
   - *Additive*: new optional field/param/route; new enum value (breaking
     only if consumers switch exhaustively); new error code documented.
   - *Behavioral*: changed defaults, limits, pagination semantics,
     idempotency — invisible in schemas, must come from changelog or code
     reading; flag as "needs manual confirmation" when unverifiable.
3. **Map to consumers.** Grep client code/tests in the repo (or linked SDKs)
   for the affected fields/routes to state actual blast radius, not
   theoretical impact.
4. **Verdict.** Output: table of changes with classification and evidence
   (`path:line` on both sides), list of consumers affected, and a semver
   recommendation (major bump if any breaking item stands).

## Rules

- Path-template normalization matters: `/users/{id}` vs `/users/:id` is the
  same contract; don't report format drift as a change.
- Never soften a breaking finding because it looks intentional — intent is
  not compatibility.

## Failure handling

- No spec files exist → derive the contract from route definitions and
  handler signatures; note derived-vs-declared provenance per entry.
- Spec and code disagree → treat code as truth, report the discrepancy as
  its own finding (stale spec is itself a defect).
