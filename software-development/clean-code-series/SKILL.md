---
name: clean-code-series
description: Use when writing clean code or designing architecture.
version: 0.1.0
author: Hermes
license: MIT
disable-model-invocation: true
metadata:
  hermes:
    tags: [CleanCode, Architecture, Agile, SOLID, Craftsmanship]
---

# Uncle Bob's Clean Series: Knowledge Base

Distilled knowledge from Robert C. Martin's four Clean books: Clean Code
(craftsmanship), The Clean Coder (professionalism), Clean Architecture
(structure & design), and Clean Agile (process). This is a knowledge base of
the METHODOLOGY: synthesized frameworks, decision rules, and anti-patterns
with chapter references: not a copy of the books. `disable-model-invocation`
means it loads only when a task actually touches the material, never as a
background overlay.

## When to Use

- Reviewing or writing code and need the Clean Code rules (naming,
  functions, comments, smells).
- Making a professional judgment call (say yes/no, estimates, pressure,
  TDD discipline).
- Designing or critiquing system structure (SOLID, boundaries, the
  dependency rule, what is/isn't a detail).
- Discussing agile process, iteration management, or the craftsman debate.

## Process

### 1. Scope the need

Ask which of the four books the question belongs to before loading anything.
Naming code → Clean Code. Professional conduct/estimates → Clean Coder.
System structure → Clean Architecture. Iterations/agile → Clean Agile.
If the user named a direction, take it and skip the inference.

### 2. Load the one reference that matters

Use `skill_view` with the exact file path: cost is zero until a question
actually needs it:

```text
skill_view (name="clean-code-series", file_path="references/clean-code.md")
skill_view (name="clean-code-series", file_path="references/clean-coder.md")
skill_view (name="clean-code-series", file_path="references/clean-architecture.md")
skill_view (name="clean-code-series", file_path="references/clean-agile.md")
```

Do not load all four up front. Chapter refs inside each file point back to
the book if deeper detail is needed.

### 3. Apply with the book's own vocabulary

Use the series' exact terms: SOLID, the Dependency Rule, the Three Laws of
TDD, the Boy Scout Rule, the Iron Cross, "QA should find nothing", the Test
Automation Pyramid, Entities vs Use Cases. Don't drift into synonyms; the
precision is load-bearing. When the material contradicts a modern framework
or a project's own ADRs, say so explicitly rather than forcing the book onto
the situation.

### 4. Verify against the checklist

Every reference ends in decision rules/checklists. A step is done only when
**every rule on the relevant checklist is applied or explicitly waived with a
reason**: apply the checklist (e.g. functions: small, one thing, one level
of abstraction; no side effects; command-query separation) before claiming
"this is clean". Report violations as findings, not opinions. If a
recommendation is speculative under the book's own guidance, mark it as
such.

## The series throughline

Craftsmanship → Professionalism → Architecture → Process. Each book answers
one question: how do I write code that is clean (Clean Code), how do I
behave as a professional (Clean Coder), how do I structure systems that stay
cheap to change (Clean Architecture), and how do I run the project (Clean
Agile). The throughline is the craftsman ideal: **quality is a professional
obligation, not a preference**.

## Central mental models (in every session)

- **SOLID**: SRP, OCP, LSP, ISP, DIP: the design principles that keep
  software open for extension and cheap to change (Clean Architecture Part III).
- **The Dependency Rule**: source code dependencies point INWARD, toward
  policy; details (DB, web, frameworks) are plugins at the boundary
  (Clean Architecture Ch. 22).
- **The Three Laws of TDD**: write a failing test, make it pass, refactor;
  in that order, every time (Clean Coder Ch. 5).
- **The Boy Scout Rule**: leave the code cleaner than you found it
  (Clean Code Ch. 1).
- **The two values**: behavior (what the system does now) and architecture
  (how easy it is to change); architecture is the greater value
  (Clean Architecture Ch. 2).
- **Clean functions & names**: small, one thing, one level of abstraction;
  intention-revealing, pronounceable, searchable names (Clean Code Ch. 2-3).
- **The Iron Cross**: scope, quality, time, cost; you can only trade three
  (Clean Agile Ch. 1).
- **"QA should find nothing"**: quality is the team's job, not QA's
  (Clean Coder Ch. 8, Clean Agile Ch. 2).
- **Database, web, and frameworks are details**: pluggable at the boundary,
  not architectural masters (Clean Architecture Part VI).

## Reference files (load on demand)

| File | Load when... |
|---|---|
| `references/clean-code.md` | writing/refactoring code: naming, functions, comments, formatting, classes, error handling, smells |
| `references/clean-coder.md` | professionalism: saying yes/no, TDD, estimates, time under pressure, mentoring |
| `references/clean-architecture.md` | system structure: SOLID, component principles, boundaries, the dependency rule, details |
| `references/clean-agile.md` | process: the agile story, iron cross, iterations, the two bills of rights |

Load a chapter with: `skill_view` (name="clean-code-series", file_path="references/clean-code.md").

## Pitfalls

- Load one reference per question: the others stay cheap until a branch
  needs them.
- Surface conflicts with a project's own ADRs and modern practice openly;
  the books are the craftsman baseline, and the baseline yields where the
  situation demands.
- Treat the series' framing (OOP-centric, opinionated) as the starting
  vocabulary, extended by the language or framework in use.
- These are distilled notes with chapter refs: when a judgment call turns
  on exact wording, the book (or the official ebooks) is the authority.

## Verification

```text
skill_view (name="clean-code-series", file_path="references/clean-architecture.md")
# Expect: the Dependency Rule, SOLID, component principles, and Part VI
# details sections present, each with chapter refs.
```
