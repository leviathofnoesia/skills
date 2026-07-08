# kraken-engineer — effective-agent-skills audit

- **Date / Auditor:** 2026-07-08, HOTE-Play session
- **Rubric used:** `davidondrej/effective-agent-skills` — located at `~/.agents/skills/effective-agent-skills/SKILL.md` (found via grep in `~/.agents/skills`). All axes below map to its sections §4 (anatomy/frontmatter), §3 (progressive disclosure), §6 (how to write effective skills), §7 (anti-patterns), §10 (composition). No fallback was needed.
- **Skill path:** `harness/kraken-skill/kraken-engineer`
- **Method:** Full read of `SKILL.md` (157 lines, 7,983 bytes), all 10 `references/*.md` (33,932 bytes total), and `evals/evals.json` + `evals/Dockerfile`. Duplication block-diffed with `diff` (byte-identical confirmed).

## Summary scorecard

| # | Axis (rubric) | Score | One-line finding |
|---|---------------|-------|-----------------|
| 1 | Frontmatter validity (§4) | PASS | `name` hyphen-case + matches folder; 501-char description; no `<>` |
| 2 | Description as routing contract (§6) | PARTIAL | What + when present, but catch-all "any … task" crowds specialists and lacks a differentiator |
| 3 | Progressive disclosure (§3/§6) | PASS | SKILL.md 158 lines; refs lean; one-level deep; indexed |
| 4 | Duplication / lean (§6/§7) | FAIL | Intent table byte-identical in `SKILL.md:35–42` and `references/constraints.md:13–20` |
| 5 | Behavior specificity / freedom-matching (§6) | PARTIAL | Right rigidity mix, but "adopt that mindset" has no conflict-selection rule vs narrow skills |
| 6 | One skill = one concern (§7 "mega-skill") | PARTIAL | 11 disciplines + evals; walks the "bundle a framework" line but defends it as a method |
| 7 | Reference quality / pointers (§6) | PASS | Each ref has a "Read when…" trigger; no dead cross-links; TOC not needed (<130 lines each) |
| 8 | Token economy (§3) | PASS | ~42 KB total; refs load on demand; pays its weight as a methodology skill |
| 9 | Harness-conflict / blocker potential | PARTIAL | "Skills first" ordering vs harness tool-policy; otherwise constraints align |
| 10 | Packaging & metadata (§4) | PARTIAL | `evals/` is a non-standard top-level dir shipped in the skill zip unnecessarily |
| 11 | Relative paths (§7) | PASS | All references relative; no absolute paths in body |
| 12 | Validation loops documented (§6) | PASS | Verification Discipline + blitzkrieg-tdd evidence gates explicit |

## Rubric axes (one subsection each)

### Ax1 — Frontmatter validity (§4)
- **Score:** PASS
- **Evidence:** `SKILL.md:1–11`. `name: kraken-engineer` (line 2) — lowercase, hyphens only, 1–64 chars, matches parent folder `kraken-engineer/`. `description` (lines 3–10) folds to **501 chars** (under the 1024 cap). No `<` or `>` in frontmatter.
- **Issue:** None.
- **Recommendation:** No change needed.

### Ax2 — Description as routing contract (§6)
- **Score:** PARTIAL
- **Evidence:** `SKILL.md:3–10`. Contains What ("Universal software-engineering methodology …") and When (the catch-all "any non-trivial implementation, refactoring, bug-fix, planning, architecture, codebase-search, external-research, visual/UI, documentation, or test-coverage task"). The rubric demands a **differentiator** ("prevents routing conflicts") and warns: *"Never summarize the full workflow in the description"* and a description that matches everything starves narrower skills.
- **Issue:** (a) The trigger list enumerates task *categories* that already have dedicated specialist skills (`rust-best-practices`, `tauri-v2`, `playwright-best-practices`, `web-design-guidelines`). A universal "use for any …" matcher can win routing over them. (b) No differentiator tells the router *why kraken-engineer instead of* those specialists. It is a methodology overlay, not a capability — but the description does not say "use alongside / before specialists, not instead of."
- **Recommendation:** Add an explicit differentiator clause to `SKILL.md:3–10`, e.g. "…Use to impose a verifiable engineering *method* on any task; load **alongside** specialist skills, not as a replacement for them." Tighten the catch-all so it does not claim exclusive ownership of categories already owned by narrower skills.

### Ax3 — Progressive disclosure (§3/§6)
- **Score:** PASS
- **Evidence:** `SKILL.md` is 157 lines. §3 defines Level-1 discovery (~100 tok), Level-2 activation (<5,000 tok), Level-3 on-demand refs. References are linked directly from the "Reference Index" (`SKILL.md:143–157`) — one level deep, no nested chains.
- **Issue:** None.
- **Recommendation:** No change needed.

### Ax4 — Duplication / lean body (§6/§7)
- **Score:** FAIL
- **Evidence:** The intent-classification table is **byte-identical** in `SKILL.md:35–42` and `references/constraints.md:13–20` (verified: `diff` reports IDENTICAL). This is the skill-creator anti-pattern the rubric's §6 ("Keep SKILL.md lean") and §7 target: information duplicated across SKILL.md and a reference.
- **Issue:** Two sources of truth for the same table. Editing one (e.g. adding a 6th intent) silently desyncs the other. It also wastes ~300 body tokens re-teaching what the reference already owns.
- **Recommendation:** Delete `SKILL.md:35–42` (the full table). Replace lines 35–42 with a one-line pointer: "Classify intent first — see `references/constraints.md#phase-1-intent-classification` for the 5-intent table and extraction steps." Keep the surrounding Phase-1/Phase-2 prose that is *not* duplicated (the "Apply Phase 2 only if…" rule at `SKILL.md:43–44` is unique and should stay).

### Ax5 — Behavior specificity / freedom-matching (§6)
- **Score:** PARTIAL
- **Evidence:** §6 "Match strictness to task fragility." The skill scales well: strict, non-negotiable rules for fragile work — "Never suppress type errors" (`SKILL.md:116`), "Never commit without explicit request" (`:117`); loose heuristics for methodology ("adopt that mindset", `SKILL.md:18`). Validation loops are explicit (§6 "Build validation loops"): Verification Discipline `SKILL.md:103–112`.
- **Issue:** "When a task calls for a specialist perspective, **adopt that mindset**" (`SKILL.md:18`) and the §2 tool-priority table give no **selection rule for conflicts** — e.g. when both a specialist skill (lower freedom, strict) and kraken-engineer's methodology apply, which governs? The plan flagged this unbounded imperative; it remains unresolved.
- **Recommendation:** Add one sentence at `SKILL.md:18–19` resolving precedence, e.g. "When a dedicated specialist skill is active, its strict rules override kraken-engineer's methodology; kraken-engineer supplies the *process* (plan → TDD → verify), the specialist supplies the *technique*." This removes the ambiguity without adding a new section.

### Ax6 — One skill = one concern (§7 "don't bundle mega-skills")
- **Score:** PARTIAL
- **Evidence:** §7: *"If one skill does design + planning + implementation + testing + deployment, you've built a framework, not a skill. Split it."* kraken-engineer bundles 11 methodologies (planning, constraints, architecture, codebase-search, research, visual-design, documentation, plan-qa, multimedia, TDD, learning) plus an `evals/` suite.
- **Issue:** On its face this is the mega-skill anti-pattern. The mitigation: it is a **Pattern B cognitive-discipline** skill (§5) — one *method* (the PDSA loop + verification discipline) expressed through many *adopted mindsets*, not many independent capabilities. Unlike Pattern A, process-primitive skills are allowed to be broad. But the breadth is real and a reviewer could reasonably reject it as a framework.
- **Recommendation:** Retain as-is (it is defensibly one discipline), but explicitly frame it in `SKILL.md:13–19` as "a single method, many mindsets" so auditors see the Pattern-B intent rather than a bundle. No split required unless the user wants separate installable skills.

### Ax7 — Reference quality / explicit pointers (§6)
- **Score:** PASS
- **Evidence:** Every reference has a "Read when…" trigger in the Reference Index (`SKILL.md:147–157`) and most in the tool/method table (`:90–101`). §6 requires "Tell the agent exactly when to read each referenced file" — satisfied. No cross-reference points to a missing file. §6 also says add a TOC to refs >100 lines; the largest (`planning.md`, 130 lines / 6,445 bytes) is borderline but sectioned with `###` headers, acceptable.
- **Issue:** `references/planning.md` is 130 lines — a one-line TOC would marginally help, but not required.
- **Recommendation:** Optional: add a 2-line TOC to `references/planning.md` (Quantitative Rigor + Output Format anchors). Not blocking.

### Ax8 — Token economy (§3)
- **Score:** PASS
- **Evidence:** `SKILL.md` 7,983 bytes + references 33,932 bytes ≈ **42 KB**. Per §3, references are Level-3 (on-demand) and don't consume context until loaded. As a methodology skill it earns its footprint: the body is dense instruction, not filler (no Python tutorials, no "what is git" — passes §7 "don't re-teach the model").
- **Issue:** None material.
- **Recommendation:** No change needed. (Recovers further once Ax4 dedup lands.)

### Ax9 — Harness-conflict / blocker potential
- **Score:** PARTIAL
- **Evidence:** Hard constraints (`SKILL.md:114–122`) mostly align with the harness: "Never commit without explicit request" matches the harness "NEVER ask for what tools/repo context can provide" + commit-only-on-request posture. "Never suppress type errors" matches the project's Rust/TS correctness stance.
- **Issue:** "**Skills first** — if a skill matches, invoke it before anything else" (`SKILL.md:77`) asserts an ordering the harness tool-policy does not mandate and could conflict with in-session tool precedence. More importantly it interacts with Ax2: if kraken-engineer itself is the "always-first" skill, it compounds the over-trigger risk (it would fire, then re-delegate to specialists).
- **Recommendation:** Soften `SKILL.md:77` to "If a *specialist* skill matches the task technique, prefer it; kraken-engineer governs the overall method." This both de-conflicts ordering and reinforces the Ax2 differentiator.

### Ax10 — Packaging & metadata (§4)
- **Score:** PARTIAL
- **Evidence:** Standard skill layout is `SKILL.md` + `scripts/` + `references/` + `assets/` (§1). kraken-engineer adds a top-level `evals/` (3 eval cases + Dockerfile, 3,552 bytes). `package_skill.py`-style validators only check `SKILL.md`, so it would *accept* the dir — but `evals/` would ship inside the distributed `.skill` zip, bloating every install with test scaffolding irrelevant to runtime behavior.
- **Issue:** Non-standard top-level dir; not part of the open AgentsSkills spec layout. Not a blocker, but untidy packaging.
- **Recommendation:** Move `evals/` outside the skill root (e.g. `harness/kraken-skill/evals-kraken-engineer/`) so the distributable skill contains only `SKILL.md` + `references/`. Out of scope to apply now (audit only); flag for follow-up.

### Ax11 — Relative paths (§7)
- **Score:** PASS
- **Evidence:** §7 "Don't use absolute paths. Always relative." All references cited as `references/<file>.md` (`SKILL.md:147–157`, `:90–101`). `references/planning.md` internally links `../research.md` / `../architecture.md` (relative) — correct.
- **Issue:** None.
- **Recommendation:** No change needed.

### Ax12 — Validation loops documented (§6)
- **Score:** PASS
- **Evidence:** §6 "The single biggest output quality improvement: state a verify → fix → re-verify loop." Kraken's Verification Discipline (`SKILL.md:103–112`) mandates run-it, cross-validate (≥2 signals), evidence-over-assertion. `references/blitzkrieg-tdd.md:34–53` adds explicit evidence-gated completion checklists.
- **Issue:** None.
- **Recommendation:** No change needed.

## Prioritized recommendations

### Critical
- **C1 — De-duplicate the intent table.** `SKILL.md:35–42` is byte-identical to `references/constraints.md:13–20`. Delete the table from `SKILL.md` and replace with a pointer to `references/constraints.md#phase-1-intent-classification` (keep the unique "Apply Phase 2 only if…" rule at `SKILL.md:43–44`). Fixes FAIL on Ax4.

### High
- **H1 — Add a differentiator + tighten triggers in the description.** `SKILL.md:3–10`. State that kraken-engineer is a *method overlay* to load **alongside** specialist skills, not a replacement, so it stops competing with `rust-best-practices`/`tauri-v2`/`playwright-best-practices`/`web-design-guidelines` for routing. Fixes the over-trigger risk (Ax2).
- **H2 — Resolve mindset-vs-specialist precedence.** `SKILL.md:18–19`. One sentence: when a dedicated specialist skill is active, its strict rules govern technique; kraken-engineer governs process. Removes the unbounded imperative (Ax5).
- **H3 — Soften "Skills first" ordering.** `SKILL.md:77`. Reword to prefer specialist skills for technique; kraken-engineer owns method. De-conflicts harness tool-policy and reinforces H1 (Ax9).

### Medium
- **M1 — Frame as one method / many mindsets.** `SKILL.md:13–19`. Add a sentence making the Pattern-B (cognitive discipline) intent explicit so reviewers don't read it as the §7 mega-skill anti-pattern (Ax6).
- **M2 — Move `evals/` out of the skill root.** `evals/` → `harness/kraken-skill/evals-kraken-engineer/`. Keeps the distributed `.skill` zip clean (Ax10).

### Low
- **L1 — Optional TOC in `references/planning.md`.** 130 lines; a 2-line anchor list (Quantitative Rigor, Output Format) satisfies §6's >100-line guidance.

## Quick wins (≤10 min each)
- Delete the duplicated table block `SKILL.md:35–42` and insert a one-line pointer (C1).
- Append a differentiator sentence to `SKILL.md:10` (H1).
- Add one precedence sentence at `SKILL.md:18–19` (H2).
- Reword `SKILL.md:77` "Skills first" → specialist-technique preference (H3).
- Add the Pattern-B framing sentence at `SKILL.md:13–19` (M1).
## Reference coverage (all 10 files)

Every `references/*.md` is accounted for below (persona, size, whether SKILL.md duplicates it). No reference is unreferenced.

| Reference file | Persona | Size (bytes / words) | SKILL.md duplication? | Primary axis |
|----------------|---------|----------------------|----------------------|--------------|
| `references/planning.md` | Cartographer | 6,445 / 959 | No — SKILL.md only *points* to it (`SKILL.md:99`, `:110`, `:147`); body keeps PDSA distinct from Cartographer's 4-phase plan | Ax7, Ax8 |
| `references/constraints.md` | Poseidon | 2,971 / 391 | **YES** — intent table byte-identical to `SKILL.md:35–42` (see Ax4/C1) | Ax4 |
| `references/architecture.md` | Atlas/Maelstrom/Leviathan | 4,703 / 657 | No — distinct decision-matrix + structural-audit content; SKILL.md:95 only points | Ax6, Ax7 |
| `references/codebase-search.md` | Nautilus | 3,086 / 414 | No — search framework; SKILL.md:92 pointer only | Ax7 |
| `references/research.md` | Abyssal | 2,477 / 349 | No — citation framework; SKILL.md:93 pointer only | Ax7 |
| `references/visual-design.md` | Coral | 2,270 / 282 | No — design system; SKILL.md:94, `:120–121` (hard-constraint adoption) | Ax7, Ax9 |
| `references/documentation.md` | Siren | 2,001 / 264 | No — docs framework; SKILL.md:96 pointer only | Ax7 |
| `references/plan-qa.md` | Scylla | 2,529 / 372 | No — SOLID plan audit; SKILL.md:97 pointer only | Ax7 |
| `references/multimedia.md` | Pearl | 2,483 / 333 | No — media extraction; SKILL.md:98 pointer only | Ax7 |
| `references/blitzkrieg-tdd.md` | Blitzkrieg | 3,435 / 479 | No — TDD discipline; SKILL.md:100, `:106` pointers only | Ax12 |
| `references/learning.md` | (learning habit) | 1,532 / 229 | No — learning-memory practice; SKILL.md:73, `:101` pointers only | Ax7 |
