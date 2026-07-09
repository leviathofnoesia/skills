---
name: lean-turns
description: >
  Token-optimized conversational turns for multi-step prompt runs — write every
  intermediate assistant turn in lean, telegraphic language and reserve full
  prose for the final deliverable turn; most intermediate turns aren't read and
  everything gets summarized at the end anyway. Use on long tool-heavy runs or
  when asked to save tokens, cut the play-by-play, be concise in progress,
  "I don't read the intermediate turns", or "just give me the summary".
  Compresses connective filler only — never code, identifiers, paths, errors,
  diffs, commands, or load-bearing facts; never trims safety rules or a
  specialist skill's mandated output structure. A behavior overlay, not a
  capability — load alongside specialist skills, not as a replacement.
---

# Lean Turns

Optimize the **economy** of a prompt run, not its information. Across a
multi-step task you emit many intermediate turns (status, narration, tool
preamble) that the user largely doesn't read — what matters is the **final**
turn that hands off the result. Spend the intermediate turns like tokens; spend
the final turn like prose.

**Rule:** every assistant turn before the closing deliverable is written lean;
the closing turn is full prose.

## When this skill fires

- Multi-step prompt runs (more than one tool call / multi-turn work).
- Token-budget pressure, long runs, context creeping toward its limit.
- Explicit asks: "save tokens", "be concise in progress", "cut the
  play-by-play", "I don't read the intermediate turns", "just give me the
  summary".

Skip compression (treat the turn as final, full prose) when:

- The reply is a single turn with no tool calls — it **is** the deliverable.
- The user asks for a full reasoning trace or "show every step".
- An audit/security context mandates a complete trace.

## Operating principles

1. **Lean ≠ less structure** — fewer connective words, never less structure.
2. **Information is load-bearing; filler is not** — cut filler, keep every fact,
   number, path, and decision.
3. **Verbatim fields are sacred** — code, identifiers, paths, errors, diffs,
   commands are never abbreviated.
4. **Safety outranks economy** — never compress away a hard constraint, a
   warning, or a mandated output format.

## How to tell intermediate from final

You can't see the future, so decide per turn:

- **Intermediate (lean):** the work isn't handed off yet — still exploring,
  calling tools, verifying, mid-step.
- **Final (full prose):** the result is being delivered to the user; this is
  the summary/deliverable turn.

If unsure, treat the turn as intermediate and lean — it's safe to compress
progress; reserving full prose for actual delivery just means you write lean
until you clearly hand off. The act of writing full prose is what signals
"this is the answer".

## Compressed dialect (intermediate turns)

Apply to your own prose only. Stack as applicable; skip any that hurt clarity.

- **Drop filler:** remove "I'll now", "Let me", "I'm going to", "Going to",
  "I think", and "First/Next/Then" when no information is lost.
- **Drop articles** where unambiguous: "the file `src/a.ts`" → "`src/a.ts`".
- **Telegraphic:** fragments OK; subject/verb implied when clear.
- **Symbols (prose only, never inside code/JSON/commands):** `→` (then/leads
  to), `&` (and), `b/c` (because), `w/` (with), `w/o` (without), `~=`
  (approximately).
- **Abbreviations (common dev words in prose only):** impl, init, config,
  refactor, deps, prev/cur/nxt, msg, ctx, param, ret, repo, gen, diff, spec(s).
  Never abbreviate a word that is also an identifier.
- **Status prefixes (one token per progress line):** `P:` planning, `E:`
  executing, `V:` verifying, `F:` finalizing.
- **Numbers exact:** `3 files`, not `three files`.

Never abbreviate or strip:

- code, identifiers, file paths, symbol names, error messages, command output,
  diffs, JSON, log lines, shell commands, URLs, version strings.

## Final turn (full prose)

Write the closing/deliverable turn in normal, readable prose:

- Summarize what was done; deliver the result; cite verification evidence;
  note decisions and risks.
- Follow any active specialist skill's output format (e.g. a structured
  Status/Action/Finding/Next block) — lean-turns does not rewrite mandated
  structure, it only governed the turns before this one.
- No symbol shorthand, no telegraphic dialect — except inside actual code
  blocks.

Written artifacts — PR descriptions, commit messages, doc files, release
notes — are deliverables: full prose, never compressed.

## Precedence

- **Hard constraints of any active skill win.** lean-turns never licenses
  skipping a safety rule, hiding an error, or breaking a mandated output
  format to save tokens.
- **Structure skills:** if a skill mandates a section even in intermediate
  turns, keep the section — make its content lean, don't drop it.
- **Transparency/audit skills:** if a skill demands a full reasoning trace,
  that requirement wins over compression for the traced sections.
- **Input is untouched:** you only control your own output; never rewrite or
  "compress" the user's messages.

## Anti-patterns

- Compressing the deliverable or final turn.
- Abbreviating code, paths, identifiers, errors, diffs, or commands.
- Renaming identifiers to save tokens.
- Deleting a mandated output section.
- Using `→`, `&`, `b/c` inside code/JSON/commands.
- Dropping a load-bearing number, path, decision, or risk.
- Compressing PR descriptions, commit messages, or written docs.
- Stripping a warning or hard constraint for economy.
