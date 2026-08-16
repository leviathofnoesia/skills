---
name: kraken-prompt-gauntlet
description: "Use when upgrading a raw brief into a build-grade prompt."
version: 1.0.0
author: kraken
license: MIT
metadata:
  hermes:
    tags: [prompting, planning, gauntlet, quality-loop, spec-writing]
    related_skills: [kraken-gauntlet-loop, kraken-cartographer, kraken-scylla]
---

# kraken-prompt-gauntlet

Upgrade a raw user brief/prompt into a build-grade prompt (spec) using the
kraken-gauntlet-loop quality loop composed with kraken-cartographer planning.
The artifact under iteration is the PROMPT itself; the bar is buildability
(completeness, specificity, executability, coherence, low ambiguity). Proven
on the Solar Glide → "Solar Glide: Aurora" 404-minigame prompt (2026-08-14).

## When to Use
- User asks to "upgrade/overhaul this prompt", "make this brief build-ready",
  "/plan this prompt", or hands a paragraph and wants a spec a builder can
  execute without inventing design decisions.
- Any non-trivial prompt that will be handed to a builder agent.

## Workflow (PDSA + gauntlet)

### 1. Pre-Plan (cartographer Phase 1-2)
- Classify intent (enhancement / greenfield / integration).
- Extract every constraint: hard numbers, named references (games,
  aesthetics), boundaries (bundle budget, platform, entry point).
- **Ground in the real target**: read the actual codebase/target BEFORE
  drafting v1 (module list, constants, entry points, test pattern, repo
  AGENTS.md). The prompt's "executability" axis is judged against the real
  tree: never invent file names or quote constants you didn't read.
- List ambiguities; note them for the critic.

### 2. Define the Bar (before any drafting)
Five axes, each scored 0-10 by the critic:
1. COMPLETENESS: every intent of the original brief present, nothing diluted.
2. SPECIFICITY: every pacing/mechanic constant is a VALUE, not a name.
3. EXECUTABILITY: maps onto real modules/files/constraints; TDD-shaped tests.
4. COHERENCE: the loop(s) compose into ONE design; no axis fights another.
5. LOW AMBIGUITY: builder can start without asking questions.
Win = all axes ≥ 8 with no placeholder; tie = gap structurally closed but some
axis < 8 or an internal contradiction; lose = a named gap blocks building.

### 3. Build v1
Draft the full prompt: design pillars (non-negotiable), run loop, meta loop,
world/progression with an explicit rule set for the spine mechanic, controls,
aesthetic, constraints, test plan, module map, and a single-source constants
table. Every constant gets a value. Write it to the project's plan location
(e.g. `docs/plans/YYYY-MM-DD-<slug>-build-prompt.md`) so critics can read it.

### 4. Critic Round (blind, harsh, ONE gap)
Dispatch a leaf subagent with: original brief verbatim, artifact path, the 5
axes, verified code facts, instructions to return axes+scores, builder
questions, and THE SINGLE BIGGEST GAP + concrete fix. Require it to verify
grounding claims against the real tree.

### 5. Phase 4 Arithmetic Pass (MANDATORY, before/after every rebuild)
Recompute every claim from the constants table yourself:
- Reachability: can the player actually reach the new layer (equilibrium math
  vs engine constants: e.g. thermal equilibrium vs ceiling sink)?
- Economy: do earn rates and costs support the stated pacing promises (first
  upgrade by run N, meta goal by run M)? Sum every cost column.
- Time: does the run length match the intended cadence (flight time =
  distance / speed, not vibes)?
- Cross-check prose against the table after ANY constant change: stale prose
  numbers are the #1 source of "tie" verdicts.
Pitfall: a critic's suggested numbers may themselves be unverified (e.g. a
30km gate at 5.4 u/s = 92 min of flight): re-derive, don't copy.

### 6. Rebuild → Confirm
Apply the critic's fix verbatim + your Phase 4 corrections. Then dispatch a
CONFIRMATION critic (fresh context) that must re-derive the arithmetic
independently and declare win/tie/lose with PASS/FAIL per check. On tie:
apply its prescribed closing fix, re-verify, declare win. Stop only on
win/tie: never a timer; escalate (stalemate) only if the same gap persists
two rounds.

### 7. Deliver
- Report the honest verdict ledger (lose → tie → win) with what moved.
- Point to the file AND embed the full final prompt in the reply for
  copy/paste when the user asks.

## Pitfalls
- Never trust your own prose after changing a constant: recompute every
  dependent number (net per cycle, ride count, run length, totals).
- Verify terrain/physics facts against the code comments, not your memory
  (e.g. terrain height range).
- Scan the constants table for placeholders: "tune", "small", "~", "etc",
  "adjust": every one is a builder decision in disguise.
- Make the spine mechanic an explicit, testable rule set (regimes, spawn
  bands, gates, handoffs): vagueness there is what loses rounds.
- Keep 404/surface constraints hard requirements, not suggestions.
- Economic promises need mechanical levers (a hangar upgrade that shortens
  the story path), not hopes ("3-5 runs" must follow from the numbers).
