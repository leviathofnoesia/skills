---
name: context-budget
description: "Plan long agent tasks around the context window: checkpoint, reload, compact."
---

# Context Budget

Treat the agent's context window as a budgeted resource on long tasks:
measure what you spend, checkpoint state outside the window, and reload
only what the next phase needs. Prevents the two failure modes of long
runs — silent truncation mid-task and degraded reasoning from an
overstuffed window.

## When to Use

- Any task expected to exceed ~10 tool-heavy steps: large refactors, big
  data crawls, multi-file audits, long test-and-fix loops. Use when the
  user says "this will take a while", when earlier tool outputs already no
  longer fit mentally, or when a run has been interrupted by compaction
  before.
- Differentiator: a planning overlay, not a capability — load alongside the
  specialist skills actually doing the work.

## Workflow

1. **Budget at plan time.** After forming the task plan, estimate phases
   and mark each phase's inputs: which files/data it needs in-context and
   roughly how large. Flag any phase whose inputs alone approach the
   window; that phase needs streaming/aggregation, not bulk reads.
2. **Checkpoint outside the window.** Persist durable progress to files
   (workspace notes, JSON/CSV accumulators, TODO state) as you go — never
   hold accumulating results only in conversation. Rule of thumb: any fact
   needed by a later phase gets written to disk when first learned.
3. **Read narrow.** Prefer targeted extraction (grep, offset/limit reads,
   structured queries) over whole-file loads. Summarize large sources into
   a scratch digest file and read the digest afterward.
4. **Reload at phase boundaries.** At each phase start, re-read only the
   checkpoint + current-phase inputs. Do not re-read prior phases' raw
   material; their conclusions live in the checkpoint.
5. **Recover from compaction.** If the session was truncated, rebuild state
   from checkpoints first, then verify against reality (re-stat files,
   re-run cheap commands) before continuing. Never trust remembered
   numbers over a fresh read.

## Rules

- Checkpoint writes are cheap; lost context is not. Write early, write often.
- Keep one canonical progress file per task; append, don't fork.
- Aggregation happens in code (scripts, loops), not by pulling everything
  into the conversation and counting manually.

## Failure handling

- No filesystem write access → keep checkpoints in the most durable channel
  available and shrink phase size so less survives between boundaries.
- Task too large even phased → propose splitting into separate sessions
  with an explicit handoff document rather than pushing one run past its
  limits.
