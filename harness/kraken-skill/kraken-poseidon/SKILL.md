---
name: kraken-poseidon
description: >-
  Poseidon pre-planning constraint method — apply formal constraint satisfaction before planning to surface requirements, boundaries, and hidden ambiguities. Use when a request is ambiguous, complex, or multi-faceted: classify intent (refactoring/greenfield/enhancement/integration/investigation), extract functional/non-functional/boundary/resource constraints, detect ambiguity, and emit a structured specification. Part of the kraken-engineer mindset family — adopt directly; compose with kraken-engineer for process and specialist skills for technique.
---

# Pre-Planning Constraints (Poseidon method)

Before you plan, analyze the request with formal constraint satisfaction to
surface requirements, boundaries, and hidden ambiguities. Complete understanding
here prevents planning failures, scope creep, and implementation surprises.

## Constraint Satisfaction Framework

### Phase 1: Intent Classification (mandatory first step)

Before any analysis, classify the intent — it sets your whole strategy.

| Intent | Indicators | Primary focus |
|--------|------------|---------------|
| Refactoring | "refactor", "restructure", "clean up" | Safety constraints, regression prevention |
| Greenfield | "create new", "add feature" | Discovery constraints, pattern requirements |
| Enhancement | "improve", "optimize", "extend" | Performance constraints, scope boundaries |
| Integration | "connect", "integrate", "interface" | API constraints, compatibility |
| Investigation | "understand", "why does", "how does" | Evidence constraints, explanation |

### Phase 2: Constraint Extraction

For the classified intent, systematically extract:
1. **Functional** — what MUST the solution accomplish; required behaviors; expected outputs.
2. **Non-functional** — performance (latency, throughput, memory); reliability/availability; security (authn/authz).
3. **Boundary** — what is explicitly OUT OF SCOPE; what must NOT change; what limitations apply.
4. **Resource** — dependencies that must be used; existing patterns to follow; team capabilities.

### Phase 3: Ambiguity Detection

Check systematically for:
1. **Vague terminology** — "optimize" → optimize what, by how much, for what metric? "modernize" → which aspects, what target state? "improve" → which metric, to what threshold?
2. **Missing context** — which files/modules are affected? what existing implementations? what conventions must be followed?
3. **Implicit assumptions** — what is the requester assuming that may be false? what domain knowledge is assumed? what historical context matters?

### Phase 4: Specification Generation

Output structured requirements:
```
## Intent Classification
Type: [Refactoring | Greenfield | Enhancement | Integration | Investigation]
Confidence: [High | Medium | Low]
Rationale: [brief]

## Constraint Specification
### Functional Requirements
1. [Must accomplish X]
### Boundary Constraints
1. [Must NOT change A]
### Quality Gates
1. [Acceptance criterion 1]

## Ambiguity Report
### Resolved Ambiguities
1. [Term]: interpreted as [meaning] because [reasoning]
### Outstanding Questions
1. [Question]: [why it matters for planning]

## Recommended Approach
[1-2 sentence summary]
```

## Constraint Enforcement

- **Mandatory classification** — never skip intent classification.
- **Complete constraint set** — never proceed without boundary constraints.
- **Ambiguity transparency** — never mask uncertainty as certainty.
- **Actionable output** — every finding must enable a planning decision.
