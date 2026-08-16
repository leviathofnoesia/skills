# Clean Agile: Back to Basics

Distilled from Robert C. Martin, *Clean Agile* (2020, Pearson); Ch. 7 by
Sandro Mancuso. Chapter refs in headings. Synthesized notes; for the full
text use the book.

## Ch. 1: Introduction to Agile
- **History**: Agile was born at Snowbird (2001) from the frustrations of
  the waterfall era: the analysis/design/implementation/**death-march**
  phases and the "iron cross".
- **The Iron Cross**: scope, quality, time, cost. You can only trade three;
  a team that "does it all" is lying to someone.
- **Iteration Zero**: the initial iteration that prepares infrastructure,
  stories, and backlog before the first delivery iteration.
- **Agile produces data**: empirical evidence from each iteration beats
  hope; management by hope is the enemy.
- **Managing the iron cross**: prioritize by business value; the circle of
  life: deliver, measure, adjust.

## Ch. 2: The Reasons for Agile
- Professionalism; software is everywhere ("we rule the world"); the
  disaster of software failure is moral, not just economic.
- **Reasonable expectations** and the slogan **"We will not ship shyt!"**: 
  the team's refusal to deliver garbage is the root of agile.
- The goals: **continuous technical readiness**, **stable productivity**,
  **inexpensive adaptability**, **continuous improvement**,
  **fearless competence**.
- **QA should find nothing**; **test automation**; **we cover for each
  other**; **honest estimates**; **you need to say "No"**; **continuous
  aggressive learning**; **mentoring**.
- **The Bill of Rights**:
  - *Customer*: an overall plan, progress every iteration, communication,
    a priority-driven backlog, changeable scope.
  - *Developer*: clear requirements, quality work, change, realistic
    commitment, and respect.

## Ch. 3: Business Practices
- **Planning**: trivariate analysis (scope, date, cost: pick two, trade
  the third); the plan is a stake in the ground, not a contract.
- **Stories and points**: small user stories, estimated in points, sized by
  the team; the ATM story example shows a story decomposed into
  testable slices.
- **Managing the iteration**: plan → work → **demo** (show real working
  software, not slides) → measure **velocity** → adjust.
- **Small releases**: ship often; the history of source-code control (tapes
  → SCCS → Subversion → **Git and tests**) is a story about enabling small
  releases.
- **Acceptance tests** and **Behavior-Driven Development** are the
  requirement language; **whole team** + **co-location** beat handoffs.

## Ch. 4: Team Practices
- **Metaphor** (a shared name for the system's shape) and
  **Domain-Driven Design** (model the domain).
- **Sustainable pace**: no death-march overtime; sleep is a productivity
  tool; dedication is not measured in hours.
- **Collective ownership** (no "the X files": no code is one person's);
  **Continuous Integration** (build every change, immediately).
- **Standup meetings**: short, daily; "pigs and chickens" (committed vs
  involved); the shout-out: announce what you'll do today.

## Ch. 5: Technical Practices
- **TDD** as **double-entry bookkeeping**: the test is the credit, the code
  is the debit: they must balance.
- **The Three Rules of TDD**: red (write a failing test), green (make it
  pass), refactor: in that order, one rule at a time.
- Debugging is minimized by tests; documentation lives in tests; fun and
  completeness come from tests; design emerges; **courage** to refactor.
- **Simple design**: the four rules (runs tests, no duplication, expresses
  intent, minimal); design weight: don't add architecture before you need
  it.
- **Pair programming**: two at one machine: continuous review, knowledge
  transfer; "just two?": pairing is the review mechanism.

## Ch. 6: Becoming Agile
- **Agile values**: courage, communication, feedback, simplicity.
- **Transformation** vs **subterfuge**: the lion-cubs story: doing agile
  to *look* agile is failure; **faking it** is common and corrosive.
- Success in smaller organizations; individual success and migration;
  coaching (real coaches, not just Scrum Masters); certification is a
  warning sign, not a guarantee.
- **Agile in the large**: scale by keeping the small (focus on small
  teams and iterations); tools should support the practice, not replace it.

## Ch. 7: Craftsmanship (Sandro Mancuso)
- The **agile hangover**: after the process, the craft was lost;
  expectation mismatch between methodology and delivery.
- **Software craftsmanship**: a mindset of responsibility: clean code,
  professionalism, continuous learning; **ideology vs methodology**: 
  values over ceremony.
- Does craftsmanship have practices? Focus on the **value**, not the
  practice; discuss practices openly.
- Impact: on individuals (pride in work), on the industry (raising the
  bar), on companies (quality as an economic driver). Craftsmanship and
  agile are complementary: agile is the process, craftsmanship is the
  attitude.
