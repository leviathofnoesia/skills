# The Clean Coder — A Code of Conduct for Professional Programmers

Distilled from Robert C. Martin, *The Clean Coder* (2011, Pearson). Chapter
refs in headings. Synthesized notes; for the full text use the book.

## Ch. 1 — Professionalism
- **Take responsibility** — own the outcome, not just the effort; a
  professional is responsible for defects even if the bug was "not theirs".
- **First, do no harm** — do not damage functionality (write tests, TDD) and
  do not damage structure (refactor continuously so the code stays clean).
- **Work ethic** — 40+ hours/week of *focused* work; professional
  development is scheduled, not opportunistic.

## Ch. 2 — Saying No
- Adversarial roles: the professional and the stakeholder have different
  goals; "yes" under impossible constraints is lying.
- **The cost of saying yes**: false promises destroy trust; the most
  professional answer to an impossible deadline is "no" (or "I cannot do
  that in that time").
- Being a "team player" is not a license to accept the unacceptable; no
  "code impossible" (writing code you know can't work to prove a point).

## Ch. 3 — Saying Yes
- **A language of commitment**: "I will", "I won't", "I can", "I can't",
  "yes", "no" — and the rule: don't commit to what you can't deliver; when
  you say yes, make the commitment concrete.
- Learn to recognize commitment vs wishful thinking in your own words.

## Ch. 4 — Coding
- **Preparedness**: don't code while mentally blocked; fix the blocker first.
- The Flow Zone is not the goal — it is a hazard; professionals don't
  "get into the zone", they stay disciplined.
- Writer's block: get creative input (read, practice) to unblock.
- **Debugging time is coding time** — it costs the business the same.
- Pace yourself: don't work 70-hour weeks to make up schedule; fatigue
  destroys quality.
- Help others: "I'll get back to you" for a question, then give it full
  attention; know the answer to "what do you need?".

## Ch. 5 — Test Driven Development
- **The jury is in**: TDD is a professional discipline, not a fad.
- **The Three Laws**: (1) write a failing test before production code,
  (2) don't write more of a test than is needed to fail, (3) don't write
  more production code than is needed to pass.
- What TDD is not: it does not guarantee perfect designs or remove the need
  for architecture; it is a floor, not a ceiling.

## Ch. 6 — Practicing
- **The Coding Dojo**: practice kata — repeat small, well-understood
  exercises to build discipline (the "hour of power": 20 min problem,
  20 min solution, 20 min refactor).
- Broadening experience: learn new languages, new paradigms, beyond the
  day job.

## Ch. 7 — Acceptance Testing
- **Communicating requirements**: acceptance tests ARE the requirements —
  written by the team with the customer, in a language both understand.
- The "Given/When/Then" shape; tests that fail on the behavior, not the
  implementation; the team owns the tests, QA reviews.

## Ch. 8 — Testing Strategies
- **QA should find nothing** — if QA finds a bug, the team failed, not QA.
- **The Test Automation Pyramid**: unit tests (base, many, fast) →
  component tests → integration tests (few, slow); each layer has a budget
  and a purpose; GUI tests are the most brittle, keep them at the top.

## Ch. 9 — Time Management
- Meetings are a cost; focus-manna is depleted by context switches.
- **Time boxing and tomatoes** (Pomodoro): 25-min focused blocks, then a
  break; makes time visible and interrupts negotiable.
- Avoidance, blind alleys, and swamps: recognize when you're stuck and
  change approach (debugging by breakpoint vs by reasoning; ask for help).

## Ch. 10 — Estimation
- **What is an estimate?** A probability distribution, not a promise. "By
  Friday" is not an estimate, it's a commitment.
- **PERT**: three-point estimates (optimistic, nominal, pessimistic) →
  expected = (O + 4N + P)/6, standard deviation ≈ (P−O)/6.
- Estimating tasks: small tasks estimate well; break big ones down.
- **The Law of Large Numbers**: estimates on many small tasks are more
  accurate than on one big task.

## Ch. 11 — Pressure
- Avoiding pressure: commit to the practices (TDD, refactoring) so pressure
  has less to feed on; stay clean.
- Handling pressure: don't panic, don't cut corners silently — communicate
  the trade-off, keep the disciplines, do your best but be honest about it.

## Ch. 12 — Collaboration
- Programmers versus people: the job includes the humans. Schedules,
  requirements, and conflicts are collaboration problems.
- Cerebellums (pairing, mentoring) build shared competence; work with
  others; teach and be taught.

## Ch. 13 — Teams and Projects
- "Does it blend?" — a team of programmers who don't communicate like a
  team fails; projects are won or lost by collaboration and ownership.

## Ch. 14 — Mentoring, Apprenticeship, and Craftsmanship
- **Degrees of failure** for training: doing nothing is the worst; the
  apprentice model (mentor → apprentice → journeyman → master) works.
- Craftsmanship = responsibility + discipline + practice; the profession is
  young and its practitioners must act like professionals.

## Appendix A — Tooling
- Source code control, IDE/editor, issue tracking, continuous build, unit
  test tools, component test tools, integration test tools, UML/MDA — the
  professional's kit; each has a discipline attached.
