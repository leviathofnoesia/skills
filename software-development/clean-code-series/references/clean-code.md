# Clean Code — A Handbook of Agile Software Craftsmanship

Distilled from Robert C. Martin, *Clean Code* (2008, Pearson). Chapter refs in
headings. Synthesized notes; for the full text use the book.

## Ch. 1 — Clean Code
- **The total cost of owning a mess**: unmanaged technical debt grows
  super-linearly; the "grand redesign in the sky" rarely succeeds — the team
  spends a decade on it and the mess re-appears.
- **Attitude**: "leaving a mess is not OK" — a schedule squeeze is not an
  excuse for bad code; bad code is a professional failure.
- **What clean code means** (per the masters quoted): runs all tests, has no
  duplication, expresses intent, minimal, readable in ~3 seconds, obvious
  (Bjarne); "readable, but also GAIN" (Grady); no duplication, one thing,
  minimal (Dave Thomas); close to the data, dependent only on the public API
  (Michael Feathers).
- **We are authors** — writing prose for readers; the ratio of time spent
  reading vs writing code is ~10:1, so readability dominates.
- **The Boy Scout Rule**: leave the code cleaner than you found it.

## Ch. 2 — Meaningful Names
- Use intention-revealing names; avoid disinformation; make meaningful
  distinctions; pronounceable; searchable.
- Avoid encodings (Hungarian, member prefixes); avoid mental mapping
  (single-letter variables except i/j/k in tight loops); class names =
  nouns; method names = verbs.
- Don't be cute; pick ONE word per concept (never mix get/fetch/retrieve);
  don't pun (add vs append); use solution domain names then problem domain
  names; add meaningful context, don't add gratuitous context.

## Ch. 3 — Functions
- **SMALL** — first rule; blocks/indenting max ~2 levels.
- **Do One Thing** — the function does the one thing you can't extract
  another function from; one level of abstraction per function; read top to
  bottom (the Stepdown Rule).
- Switch statements: bury in an abstract factory, never repeat the switch.
- Descriptive names; small number of arguments (0 > 1 > 2 > 3+); flag args
  are a smell; argument objects; no side effects; output args avoided.
- **Command Query Separation**; prefer exceptions to error codes; extract
  try/catch blocks; **DRY** (Don't Repeat Yourself); structured programming
  (single exit) at the function level.

## Ch. 4 — Comments
- Comments do NOT make up for bad code; explain yourself in code.
- GOOD: legal, informative, intent-explaining, clarification, warning of
  consequences, TODO, amplification, public-API Javadocs.
- BAD: mumbling, redundant, misleading, mandated, journal, noise, scary
  noise, position markers, closing-brace, attributions, commented-out code,
  HTML, nonlocal info, too much info, inobvious connection, function headers.

## Ch. 5 — Formatting
- Newspaper metaphor: name → high-level → low-level; vertical openness
  between concepts; vertical density; vertical distance (related code near);
  vertical ordering (dependent on the one above).
- Horizontal openness and density; alignment is a myth; indentation;
  dummy scopes are bad; **team rules** — pick one style, everyone follows it.

## Ch. 6 — Objects and Data Structures
- Data abstraction: expose behavior, hide data (not just getters/setters).
- **Law of Demeter** — talk to friends, not strangers; train wrecks are bad.
- **Data/Object antisymmetry**: procedural code (data structures + functions)
  vs OO code (objects hiding data) — each is right for its job; hybrid
  classes are the worst.
- Objects expose behavior and hide data; data structures expose data with no
  behavior — keep them cleanly separated.

## Ch. 7 — Error Handling
- Use exceptions, not return codes; write try-catch-finally first (TDD);
  don't return null; don't pass null.
- **Don't Repeat Yourself** applies to error handling too; define exceptions
  in terms of a caller's needs (one wrapper translating third-party
  exceptions).

## Ch. 8–9 — Boundaries, Unit Tests
- Third-party code: wrap it at a boundary (an adapter) so it can't leak;
  learning tests pin vendor behavior.
- Tests: one assert per test ideal, one concept per test; FIRST — Fast,
  Independent, Repeatable, Self-validating, Timely.

## Ch. 10 — Classes
- Small: single responsibility (one reason to change); open-closed; cohesion
  (methods manipulating the same instance variables); organize for change:
  isolate from change via interfaces.

## Ch. 11 — Systems
- Separate construction from use (main → dependency injection); separate
  main; use factories; AOP-like cross-cutting (proxy/DI frameworks) — but
  keep frameworks as details.

## Ch. 12 — Emergence
- Four rules of simple design: (1) runs all tests, (2) no duplication,
  (3) expresses intent, (4) minimizes classes/methods.
- Duplication is the primary enemy; expressiveness via names; keep methods
  small, classes small.

## Ch. 13 — Concurrency
- Concurrency is a decoupling strategy (what runs vs when); it's hard:
  single responsibility for concurrency; limit scope of shared data; use
  copies; use independent threads where possible; know the library (threads,
  executors, locks, atomic); never hold a lock while waiting.

## Ch. 14–15 — Successive Refinement; Smells and Heuristics
- The argument for iterative cleanup: the book shows a working-but-messy
  program refined through tests into a clean design — cleanup is a normal
  part of coding, not a separate phase.
- Heuristics catalog (short names): comments (C1–C5), environment (E1–E2),
  functions (F1–F7), general (G1–G32), Java (J1–J4), names (N1–N7), tests
  (T1–T8). Use the catalog as a review checklist, not a dogma.
