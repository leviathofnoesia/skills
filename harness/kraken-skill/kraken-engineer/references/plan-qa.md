# Plan Quality Audit (Scylla method)

Evaluate a work plan against SOLID principles and measurable criteria before
execution. Catching deficiencies early prevents wasted effort, scope creep, and
implementation failures. Adopt this method to self-review a plan (including your
own) before you execute it.

## Quality Assurance Framework

### Phase 1: Input Validation
Extract a single plan path from the input. Exactly one → accept. None → reject
("no plan path found"). Multiple → reject ("ambiguous: multiple plan paths").

### Phase 2: SOLID Evaluation
1. **SRP** — each task one clear purpose; not overloaded; understandable alone.
2. **OCP** — extends without modifying core; extensions via addition.
3. **LSP** — substituted implementations fulfill the same contract; clear behavioral contracts.
4. **ISP** — interfaces focused on specific client needs; no forced unused methods.
5. **DIP** — high-level modules don't depend on low-level details; depend on abstractions.

### Phase 3: Measurable Criteria (default gates — tunable)
| Criterion | Metric | Threshold |
|-----------|--------|-----------|
| Reference Completeness | % file references verified | 100% required |
| Acceptance Clarity | tasks with concrete acceptance criteria | ≥ 90% required |
| Ambiguity Index | vague terms per task | ≤ 0.5 per task |
| Dependency Clarity | tasks with explicit dependencies | ≥ 80% required |
| Testability | tasks with verification approach | ≥ 85% required |
| Scope Boundedness | tasks with explicit scope boundaries | 100% required |

### Phase 4: Implementation Simulation
For 2-3 representative tasks, simulate execution: start at the first actionable
step, follow the information trail, note where gaps occur, note where assumptions
must be made.

### Phase 5: Structured Report
```
## Validation Result: [APPROVED | REJECTED | CONDITIONAL]
## SOLID Compliance (rating + findings per principle)
## Measurable Criteria (table: score / threshold / pass-fail)
## Implementation Simulation (tasks simulated, gaps, assumption points)
## Critical Issues (must fix)
## Recommendations (should fix)
```

## Quality Gates
- **Reference verification** — every file reference verified by reading the file.
- **Acceptance criteria** — every task has measurable acceptance criteria.
- **Scope boundaries** — every task defines what is NOT included.
- **Dependency clarity** — every dependent task specifies prerequisites.

Remember: systematic QA prevents wasted effort and implementation failures.
