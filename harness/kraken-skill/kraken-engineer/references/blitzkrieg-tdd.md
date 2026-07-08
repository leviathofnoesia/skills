# TDD & Evidence-Gated Completion (Blitzkrieg discipline)

In Kraken these were enforced by OpenCode lifecycle hooks that intercepted tool calls. A standalone skill can't intercept your tool calls — so adopt
them as **self-enforced discipline**. The thresholds below are the recommended
defaults Kraken shipped with; treat them as tunable per project.

## 1. Test plan before implementation

Before writing implementation code, write a test plan:
- List the test cases (happy-path, edge-case, error-path, integration).
- State a coverage target.
- Implementation may begin only once the plan exists and is adequate.

Recommended default `TestPlanRequirements`:
- `requiredBeforeImplementation: true`
- `minTestCases`: enough to cover happy + edge + error paths (not zero)
- `coverageThresholdPercent`: 80
- `requireCoverageThreshold: true`

## 2. TDD: red → green → refactor

For behavior changes:
- **Write the failing test first.** Do not edit implementation without a
  corresponding test.
- Make it pass (green) with the minimal change.
- Then refactor, keeping tests green.
- **Refactors** (extract/rename/restructure that preserve behavior) are allowed
  without new tests — but confirm behavior is preserved (tests still green).

Test vs implementation file detection (apply the same convention):
- Test files: `*.test.{ts,tsx,js,jsx}`, `*.spec.*`, `/__tests__/`, `/test/`, `/tests/`.
- Everything else (outside `node_modules`/`dist`/`build`) is implementation.

## 3. Evidence-gated completion

Before you claim a task is done, require ALL of:
- A **green build** (exit 0, no errors).
- **Tests executed** with real assertions (not just present).
- **Coverage ≥ target** (default 80%); if below, add tests or justify.
- **Edge cases** covered (at least the obvious null/empty/boundary/error paths).
- Evidence presented (build output, test output) — not a promise.

Recommended default `VerificationOptions`: `coverageThreshold: 80`,
`minAssertions: 1`, `minEdgeCases: 1`, and an overall confidence score ≥ 70
(`passed && confidenceScore >= 70`).

Pre-completion violation checklist — if any is true, you are NOT done:
- `build-failed` — build did not exit 0.
- `no-test-execution` — no test run occurred.
- `no-assertions` — tests ran but assert nothing.
- `insufficient-coverage` — coverage below target.
- `no-edge-cases` — obvious edge cases untested.
- `missing-evidence` — no build/test output to show.

## 4. Planner constraints

Break work into atomic, verifiable steps. Recommended defaults:
- Every plan with implementation steps must include a **test step** and a
  **verification step**.
- Cap implementation-step complexity (default max 3 on a 1–10 scale); if a step
  exceeds it, split it.
- Each step has: a concrete action, dependencies, and a verification method.

Step-type inference heuristic (for self-auditing your plan):
- contains verify/validate/review/check/confirm/approve → **verification**
- contains plan/design/architect/outline → **planning**
- contains test/spec/assert/mock/stub → **test**
- otherwise → **implementation**

## How to use this file

On any implementation task, run the discipline mentally (or as a checklist):
test plan exists → write failing test → implement → green → refactor →
run build+tests+coverage → present evidence → only then claim done. If you
can't satisfy a gate, say so explicitly rather than claiming success.
