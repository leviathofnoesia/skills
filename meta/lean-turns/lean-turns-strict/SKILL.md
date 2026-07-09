---
name: lean-turns-strict
description: >
  Token-suppressed intermediate turns for multi-step prompt runs — an
  ultra-lean overlay that shows the user ONE status token per intermediate
  turn (P:/E:/V:/F:) and holds all detail, paths, errors, decisions, and
  reasoning internally until the final deliverable turn, which is full prose;
  the agent's own understanding is never reduced. Use on explicit asks:
  "strict mode", "ultra lean", "one token per turn", "suppress the
  play-by-play", "I only want the final answer". Compresses visible output
  only — the agent still reasons fully and never drops a load-bearing fact, a
  hard constraint, or a specialist skill's mandated output; everything
  surfaces in the final turn. A behavior overlay, not a capability — load
  alongside lean-turns and specialist skills, not as a replacement.
---

# Lean Turns — Strict

The strict variant of lean-turns. Same goal — spend intermediate turns like
tokens, the final turn like prose — but taken to its limit: **the user sees
exactly one token per intermediate turn.** All substance (paths, errors,
decisions, risks, findings, and the agent's full reasoning) is retained
internally and emitted only in the final deliverable turn.

Crucially, strict mode changes **output**, not **understanding**. The agent
reasons, explores, calls tools, and verifies exactly as it otherwise would;
only the *visible* intermediate surface is collapsed to a single status
token. Nothing is lost — it is deferred.

**Rule:** every intermediate turn emits exactly one status token; the closing
turn is full prose.

## When this skill fires

- Explicit asks: "strict mode", "ultra lean", "one token per turn",
  "suppress the play-by-play", "I only want the final answer".
- Long tool-heavy runs where the user has signaled they won't read progress.

Skip suppression (emit a full turn) when:

- The reply is a single turn with no tool calls — it **is** the deliverable.
- The user asks for a full reasoning trace or "show every step".
- An active skill HARD-mandates immediate disclosure (e.g. a security stop or
  audit trace) for the section in question — that mandate wins over one-token
  suppression for the traced section.

## Operating principles

1. **One token visible** — an intermediate turn emits exactly one status
   token; nothing else reaches the user.
2. **Agent understanding intact** — internal reasoning is never reduced; only
   output is suppressed.
3. **Deferred disclosure** — every path, error, decision, and risk is held and
   emitted in the final turn, verbatim where required.
4. **Safety outranks suppression** — a hard mandate to disclose forces a full
   turn; strict mode never licenses hiding a mandated fact mid-run.
5. **Final turn full prose** — identical to lean-turns: full, readable,
   structured as any active specialist skill requires.

## Visible dialect (intermediate turns)

Only one of these reaches the user, per turn:

| Token | Meaning            |
|-------|--------------------|
| `P:`  | planning           |
| `E:`  | executing          |
| `V:`  | verifying          |
| `F:`  | finalizing         |

Pick the token that matches the current step. No prose, no symbols, no
abbreviations — just the single token. The step's real content lives in the
agent's context, not in the turn.

## Final turn (full prose)

Write the closing/deliverable turn in normal, readable prose:

- Surface everything deferred during the run: what was done, the result,
  verification evidence, decisions, and risks — with paths, errors, and
  identifiers verbatim.
- Follow any active specialist skill's output format (e.g. a structured
  Status/Action/Finding/Next block).
- No symbol shorthand, no telegraphic dialect — except inside actual code
  blocks.

Written artifacts — PR descriptions, commit messages, doc files, release
notes — are deliverables: full prose, never compressed.

## Precedence

- **Hard constraints of any active skill win.** lean-turns-strict never
  licenses skipping a safety rule, hiding an error a mandate requires
  disclosing, or breaking a mandated output format to save tokens.
- **Structure/transparency skills:** if a skill mandates a visible section
  mid-run, that requirement wins over one-token suppression for the traced
  section.
- **Composes with lean-turns:** strict is the stricter sibling; enable both,
  strict governs the turns. lean-turns' "surface verbatim in intermediate
  turns" rule is overridden by strict's "defer to final" rule for the agent's
  own narration.
- **Input is untouched:** you only control your own output; never rewrite or
  "compress" the user's messages.

## Anti-patterns

- Emitting more than one token in an intermediate turn.
- Abbreviating code, paths, identifiers, errors, diffs, or commands.
- Renaming identifiers to save tokens.
- Dropping a load-bearing fact, path, decision, or risk from the final turn.
- Compressing the final turn or written artifacts.
- Stripping a warning or hard constraint — defer it to the final turn, don't
  delete it.
- Letting suppression reduce the agent's own reasoning or verification.
