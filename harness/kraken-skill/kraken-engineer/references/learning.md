# Learning Habit (collapsed from Kraken's learning-memory)

Kraken persisted learning in a SQLite-backed knowledge system (experience store,
knowledge graph, pattern detection, spaced repetition). That implementation is
runtime-bound and not portable — but the **habit** is. After finishing a
non-trivial task, spend a moment on these four practices. They compound.

## 1. Experience store
Record: the decision you made, its outcome, and any reusable pattern. One or two
sentences each. Keep it searchable (a short summary + tags).

## 2. Knowledge graph
Link related decisions into a lightweight graph: nodes (decisions/facts) +
edges (relation, e.g. "contradicts", "enables", "depends-on") with a strength.
This turns isolated notes into navigable context.

## 3. Pattern detection
When the same signal recurs across tasks (a recurring bug class, a library
quirk, a project convention), record it as a **pattern** with a confidence level
and the evidence that supports it. High-confidence patterns become defaults you
apply without re-deriving.

## 4. Spaced repetition
Schedule periodic review of high-value nodes (e.g. decisions that changed your
mental model, non-obvious project constraints). Re-surface them before similar
future work so they actually inform new tasks.

## Practical form
You don't need a database. A notes file, a markdown log, or your memory tool
suffices — as long as it is (a) written down, (b) linked, (c) tagged with
confidence, and (d) revisited. The point is to stop re-learning the same lesson.
