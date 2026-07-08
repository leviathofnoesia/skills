# Planning (Cartographer method)

Produce plans that are correct, complete, and verifiable. Think before you
format. Prove before you claim. Ask before you assume. Adapt output to your
audience — ask clarifying questions when ambiguity or meaningful tradeoffs
exist; otherwise document assumptions and proceed.

## Planning Methodology (four phases — do not skip, do not reorder)

### Phase 1: Understand
Answer internally:
1. **What is being asked?** One sentence.
2. **What type of work?** new feature | refactoring | bug fix | optimization | integration | investigation.
3. **Hard constraints** — budget, time, resources, compatibility, performance targets. Extract every number.
4. **What is ambiguous?** List uncertainties.
5. **What is out of scope?** Boundaries explicitly.

If the task has quantitative constraints (budgets, time limits, capacity), flag
it as a **constrained optimization problem** and activate the Quantitative
Rigor Module in Phase 3.

### Phase 2: Gather
Use available tools:
- **Codebase analysis**: `grep`, `glob`, `lsp_find_references`, `lsp_goto_definition`, `ast_grep`.
- **External research**: adopt the research method (`../research.md`) for libraries/frameworks.
- **Architecture**: adopt the architecture method (`../architecture.md`) for design questions.

Rules: delegate (to a tool) only when info isn't available directly; run
independent searches in parallel; collect all outputs before Phase 3; never
repeat a search you've already done.

### Phase 3: Synthesize
**Code/engineering plans:**
1. Break work into phases, each with a clear goal and deliverables.
2. Within a phase, define tasks. Each task needs: a concrete action (not
   "implement feature" but "add `validateInput()` to `src/handlers/upload.ts`"),
   dependencies, an honest time estimate, and a verification method.
3. Identify the critical path (longest sequential chain).
4. Identify true parallelization opportunities.
5. Assess risks with concrete mitigations ("changing `UserService` interface
   affects 12 callers in `src/api/`", not "things might break").

**Constrained optimization problems:** activate the Quantitative Rigor Module
below.

**Investigation/research plans:** define hypotheses, the evidence needed per
hypothesis, the order of investigation (cheapest evidence first), and the stop
condition.

### Phase 4: Verify (mandatory — never skip)
Before outputting any plan, recheck:
1. **Arithmetic** — if numbers are involved, recompute every total from scratch.
2. **Feasibility** — does the plan satisfy ALL stated constraints? Check each.
3. **Completeness** — does it cover everything in scope? Anything missing from Phase 1?
4. **Dependency** — are dependencies accurate? Is the critical path correct?
5. **Ambiguity** — could a competent implementer misunderstand any task?

For constrained optimization, the CHECK assertion (below) must be true. Revise
silently and re-verify on any failure.

## Quantitative Rigor Module

Activated when selecting items under constraints (budget, time, capacity) or
maximizing/minimizing a metric.
**Step 1 — Constraint table.** List all items with their dimensions (time, cost, value…) and all constraint limits. Mark any **mandatory** items — the headline deliverable, regulatory/contractual, or explicitly required features — and carry that flag forward: the search in Steps 2–5 must never drop a mandatory item to inflate value. Re-apply a mandatory-item filter after every seed and after Step 4's selection.

**Step 2 — Multi-seed search.** Generate 5 candidate solutions via different
greedy strategies; "greedy pack" = add items in sorted order, skip any that
would violate a constraint.

| Seed | Strategy |
|------|----------|
| S1 | Sort by value (desc), greedy pack |
| S2 | Sort by value/cost ratio (desc), greedy pack |
| S3 | Sort by value/time ratio (desc), greedy pack |
| S4 | Sort by cost (asc), greedy pack |
| S5 | Sort by time (asc), greedy pack |

**Step 3 — Local search (2 passes per seed).** For each selected item X, for
each unselected item Y: if (remove X, add Y) is feasible AND increases value,
record it as a candidate swap. Apply the best swap (highest value increase); if
none, stop.

**Step 4 — Select best.** Compare all 5 improved candidates; pick the highest value.

**Step 5 — Slack analysis.** Compute unused budget/time. If any unselected item
fits the remaining slack and improves value, add it and re-verify.

**Step 6 — Ledger + CHECK assertion.** Output:
```
## Solution Ledger
Selected: [list]
Time: [sum] / [limit]
Cost: [sum] / [limit]
Value: [sum]

CHECK: time_used <= time_limit AND cost_used <= budget → [true/false]
```
If CHECK is false, the solution is invalid — return to Step 2. Never output an
invalid solution. When only a time budget is given, bind `cost` to the same
limit (cost = time, 1:1) and state that assumption in the ledger; the CHECK
requires both dimensions, even if they coincide.

**Step 7 — Backup plans (when requested).** Derive from the main plan, not from
scratch: apply the new constraint (e.g. 20% budget cut), drop lowest
value-per-dollar items until feasible, run 2-pass local search, output with its
own ledger and CHECK.

## Output Format (adapt to problem type — don't force one template)

- **Code plans:** executive summary (2-3 sentences); scope (in/out); phased task
  breakdown with dependencies + time estimates; critical path; risk assessment;
  Definition of Done.
- **Optimization:** constraint table; solution ledger with CHECK; backup plans if requested.
- **Investigations:** hypotheses; evidence plan; expected outcomes.
- Always end with a verification note showing Phase 4 checks passed.

## Anti-Patterns (hard rules)

1. Never claim optimality without evidence — say "after 5 seeds + local
   improvement, best found is X", not "this is optimal".
2. Never output unverified arithmetic — every sum recomputed in Phase 4.
3. Never narrate process ("let me think…") — output results.
4. Never fill templates mechanically — omit sections with no value here.
5. Never leave slack uninvestigated — if budget/time is unused and items could
   fit, explain why they weren't included.
6. Never build backup plans from scratch — always derive from the main plan.
7. Never delegate when direct tools suffice — check `grep`/`glob`/`lsp` before
   spawning a heavy search.
8. Never present a plan without a Definition of Done.
