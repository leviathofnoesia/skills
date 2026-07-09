# lean-turns

Token-optimized conversational turns for multi-step prompt runs.

## What it does

Across a multi-step task an assistant emits many intermediate turns (status,
narration, tool preamble) that the user largely doesn't read — what matters is
the **final** turn that hands off the result. lean-turns governs the *economy*
of the run:

- **Intermediate turns** → lean, telegraphic language: drop filler/articles, use
  fragments, status prefixes (`P:`/`E:`/`V:`/`F:`), and symbol shorthand
  (`→`, `&`, `b/c`, `w/`) in prose only.
- **Final turn** → full readable prose that delivers the result and cites
  verification.

It is a **behavior overlay, not a capability** — it composes with specialist
skills and never overrides their hard constraints or mandated output structure.

## When it fires

- Multi-step runs (more than one tool call / multi-turn work).
- Token-budget pressure or long runs.
- Explicit asks: "save tokens", "be concise in progress", "cut the
  play-by-play", "I don't read the intermediate turns", "just give me the
  summary".

Compression is skipped (treat the turn as final) for single-turn deliverables,
explicit "show every step" requests, and audit/security contexts mandating a
full trace.

## Hard rules

- Verbatim fields are sacred: code, identifiers, paths, errors, diffs, commands,
  JSON, URLs, versions are **never** abbreviated.
- Safety outranks economy: never strip a constraint, warning, or mandated format.
- Input is untouched — only your own output is governed.

See [`SKILL.md`](./SKILL.md) for the full dialect, precedence, and anti-patterns.

## Related

- [`lean-turns-strict/`](./lean-turns-strict/) — the ultra-lean sibling: one
  status token per intermediate turn, all detail deferred to the final turn.

## Install

```bash
npx skills add leviathofnoesia/skills/meta/lean-turns
```
