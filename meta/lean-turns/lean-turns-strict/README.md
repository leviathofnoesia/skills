# lean-turns-strict

Token-suppressed intermediate turns — the ultra-lean sibling of
[`lean-turns`](../).

## What it does

strict mode collapses the *visible* surface of every intermediate turn to
**exactly one status token**:

| Token | Meaning    |
|-------|------------|
| `P:`  | planning   |
| `E:`  | executing  |
| `V:`  | verifying  |
| `F:`  | finalizing |

All substance — paths, errors, decisions, risks, findings, and the agent's full
reasoning — is retained internally and emitted **only** in the final deliverable
turn (full prose). The agent's own understanding is never reduced; only the
output is suppressed. Nothing is lost, it is deferred.

It is a **behavior overlay, not a capability** — load alongside `lean-turns` and
specialist skills.

## When it fires

- Explicit asks: "strict mode", "ultra lean", "one token per turn", "suppress
  the play-by-play", "I only want the final answer".
- Long tool-heavy runs where the user won't read progress.

A full turn is emitted (suppression skipped) for single-turn deliverables,
explicit reasoning-trace requests, and any active skill that **hard-mandates**
immediate disclosure for the section in question — that mandate wins.

## Hard rules

- Exactly one token visible per intermediate turn; no prose, symbols, or
  abbreviations in between.
- Agent understanding intact — internal reasoning is never reduced.
- Everything deferred surfaces verbatim in the final turn.
- Safety outranks suppression: a mandated disclosure forces a full turn; strict
  mode never hides a mandated fact.

See [`SKILL.md`](./SKILL.md) for the full rules, precedence, and anti-patterns.

## Related

- [`../`](../) — `lean-turns`, the base dialect (intermediate turns stay
  informative rather than one-token).

## Install

```bash
npx skills add leviathofnoesia/skills/meta/lean-turns/lean-turns-strict
```
