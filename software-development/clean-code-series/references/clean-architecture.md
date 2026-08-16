# Clean Architecture: A Craftsman's Guide to Software Structure and Design

Distilled from Robert C. Martin, *Clean Architecture* (2018, Pearson). Part /
chapter refs in headings. Synthesized notes; for the full text use the book.

## Part I: Introduction (Ch. 1-2)
- **What is design/architecture?** The same thing: the shape of the system,
  its high-level structure. Good architecture delays decisions and makes
  change cheap; bad architecture makes change expensive and drives the death
  march.
- **A Tale of Two Values**: behavior (what the system does now) vs
  architecture (how easy it is to change). Behavior is urgent, architecture
  is important. **The greater value is architecture**: a system with no
  behavior is still usable if it can change; a system that can't change is
  doomed.
- Eisenhower's matrix: important/urgent → architecture is important,
  rarely urgent; fight for it.

## Part II: Starting with the Bricks: Programming Paradigms (Ch. 3-6)
- Three paradigms, three constraints:
  - **Structured programming**: discipline on direct transfer of control
    (no unrestrained goto); enables provable decomposition.
  - **OOP**: discipline on indirect transfer of control (polymorphism via
    interfaces); enables plugins and dependency inversion.
  - **Functional**: discipline on assignment (immutability); enables
    concurrency safety and event sourcing.
- Paradigms are about WHAT NOT TO DO; they shape architecture by removing
  capabilities.

## Part III: Design Principles: SOLID (Ch. 7-11)
- **SRP**: a module has one, and only one, reason to change. The real
  definition: one *actor* (group of users) who would request the change.
  Symptoms of violation: accidental duplication, merge conflicts.
- **OCP**: open for extension, closed for modification: add behavior by
  adding new code, not editing old; achieved via dependency inversion +
  abstraction, not base-class editing.
- **LSP**: subtypes must be substitutable for their base types without
  breaking invariants (the Square/Rectangle problem; the "licensed
  vs unlicensed" example). Architecture must not be tripped by the
  substitution rule.
- **ISP**: no client should depend on methods it doesn't use; fat
  interfaces create coupling.
- **DIP**: depend on abstractions, not concretions; source dependencies
  point at abstract interfaces; concrete details are owned by the
  higher-level policy. Stable abstractions + factories.

## Part IV: Component Principles (Ch. 12-14)
- **Component cohesion**: the tension triangle:
  - REP: Reuse/Release Equivalence: things reused together are released
    together.
  - CCP: Common Closure: things that change together belong together.
  - CRP: Common Reuse: don't depend on things you don't use.
- **Component coupling**:
  - ADP: Acyclic Dependencies: no cycles in the dependency graph.
  - SDP: Stable Dependencies: depend in the direction of stability
    (stability = many incoming deps, few outgoing).
  - SAP: Stable Abstractions: stable components are abstract; the
    stability/abstractness correlation (the "main sequence").

## Part V: Architecture (Ch. 15-29)
- **What is architecture?** Development, deployment, operation,
  maintenance: the four concerns an architect maximizes, especially
  **keeping options open**: delay decisions (DB, framework, web) until the
  last responsible moment. Architecture = the decisions you want to delay.
- **Independence (Ch. 16)**: use cases are the backbone; decouple layers,
  decouple use cases, decouple modes; independent develop-ability and
  deployability; "duplication" that is real vs accidental.
- **Boundaries: drawing lines (Ch. 17)**: draw lines where the change rate
  differs; plugin architecture: the GUI is a plugin to the business rules,
  the database is a plugin; the boundary is crossed by dependencies pointing
  against the flow of control.
- **Boundary anatomy (Ch. 18)**: monolith → deployment components →
  threads → local processes → services; each form is a stronger boundary
  with a cost.
- **Policy and level (Ch. 19)**: policy = business rules; level = distance
  from I/O. Low-level policies (I/O) depend on high-level policy (business);
  the dependency rule makes the direction explicit.
- **Business rules (Ch. 20)**: **Entities** (critical business rules, no
  dependencies) and **Use Cases** (application-specific rules, orchestrate
  entities); request/response models are data, not business objects.
- **Screaming architecture (Ch. 21)**: an architecture should *scream* its
  use case (a "health-care system" shape, not a "framework" shape); the web
  is a delivery mechanism, frameworks are tools not ways of life;
  testable architectures (no framework in the tests' path).
- **The Clean Architecture (Ch. 22)**: concentric circles: Entities →
  Use Cases → Interface Adapters → Frameworks & Drivers. **The Dependency
  Rule**: source code dependencies point inward, never outward; inner
  circles know nothing of outer.
- **Presenters and Humble Objects (Ch. 23)**: split hard-to-test views from
  logic: the Presenter formats data, the View is a dumb Humble Object;
  database gateways, data mappers, service listeners.
- **Partial boundaries (Ch. 24)**: skip-the-last-step, one-dimensional
  boundaries, facades: cheaper partial boundaries when a full one is
  overkill.
- **Layers and boundaries (Ch. 25)**: the "Hunt the Wumpus" example: real
  architecture across language/thread boundaries.
- **The Main component (Ch. 26)**: Main is the ultimate detail: a plugin
  that wires the concrete components, builds the dependency graph, and
  hands control to the policy.
- **Services (Ch. 27)**: services are just one boundary form; the "kitty
  problem": distributed objects break encapsulation; prefer
  component-based services and handle cross-cutting concerns.
- **The test boundary (Ch. 28)**: tests are system components; design for
  testability; the Testing API: a narrow interface the tests use.
- **Clean embedded architecture (Ch. 29)**: app-titude (the software's
  attitude, not the hardware's); the target-hardware bottleneck is a detail
  to isolate behind firmware layers.

## Part VI: Details (Ch. 30-34)
- **The database is a detail (Ch. 30)**: a storage detail; the data model
  is not the object model; don't let the DB dictate architecture.
- **The web is a detail (Ch. 31)**: the endless pendulum (client-server
  vs terminal); the upshot: keep the web as a plugin.
- **Frameworks are details (Ch. 32-33)**: frameworks constrain; don't
  marry them; keep them behind boundaries.
- **Case study (Ch. 34)**: the video sales example: an architecture that
  grew a use-case layer, boundaries, and kept the framework peripheral.
