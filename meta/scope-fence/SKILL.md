---
name: scope-fence
description: "Detect and stop scope creep mid-task with a written fence."
---

# Scope-Fence

Detect and stop scope creep mid-task with a written fence..

## When to Use

Tasks that start small and accrete 'while we're here' changes until nothing ships.

## Workflow

1. At task start, write the fence: what IS this task, in one sentence, plus explicit non-goals.
2. Log every out-of-bounds impulse in a parking lot instead of doing it.
3. When blocked, check: is the block actually inside the fence? Escalate, don't expand.
4. At review, ship fence-content; file parked items as their own tasks.
5. Retrospective: measure fence violations and their cost.

## Pitfalls

Fences so broad everything qualifies. Parking lot as guilt graveyard (never revisited). Legitimate discoveries misclassified as creep (real blockers sometimes DO change scope — renegotiate explicitly).

## Verification

The shipped diff contains zero unrelated changes; parked items exist as tracked follow-ups; original one-sentence goal is demonstrably met.

## Inputs

- Task context: task definition

## Outputs

- fence statement + parking lot + focused diff

## Related

decision-record-mini, backlog-triage-grooming
