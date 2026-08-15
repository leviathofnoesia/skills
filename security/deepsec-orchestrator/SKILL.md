---
name: deepsec-orchestrator
description: "Loop deepsec+Codex via judge; consolidate and auto-apply."
---

# DeepSec Orchestrator — chain-shaped looping graph

Run **Codex Security and deepsec side by side**, consolidate their findings,
and **apply the fixes automatically** — with an **advisor/judge agent in the
middle** that decides what to trust, what to apply, and whether to loop again.
The workflow is a **chain** (scan → consolidate → judge → apply → verify) shaped
into a **looping graph**: the verify/judge edges route back to the scanner
nodes for the next model/harness/API set.

## When to Use

- Advanced security workflow automation with fine control over models, harnesses, and APIs.
- The user wants multiple model/harness/API sets tried in sequence, findings auto-applied.
- The user says "orchestrate deepsec + codex security", "chain loop", "judge-advised scan".

## 1. Configure (MANDATORY — collect the full set list before anything runs)

Refuse to start until the user provides **all** of:

- **target** — one absolute path.
- **sets** — a list of ≥1 scanner configurations. Each set = `{model id,
  deepsec harness (--agent pi|codex), deepsec api (base URL + key env),
  codex-security provider + api (--provider / --codex + key env)}`. *Multiple
  sets are the point* — e.g. set 1 = v4-flash via gateway A, set 2 = v4-pro via
  gateway B.
- **judge config** — the advisor/judge's own `{model, harness/api}` (may differ
  from the scanner sets; may itself be a list to judge in multiple passes).
- **apply policy** — `auto` (apply every judge-approved fix), `hybrid`
  (auto-apply low-risk, prompt for high-risk), or `manual` (report only).
- **stop criteria** — `max_loops` (default = number of sets), the convergence
  rule (default: a full pass with **no new P0/P1 true-positives**), and whether
  deepsec `--reinvestigate <N>` re-scan waves are allowed.

Missing any field → ask. Never assume a model id, endpoint, provider, or key env.

## 2. The graph

| Node | Runs as | Input | Output |
|---|---|---|---|
| **SCAN·deepsec** | subagent (leaf) | target + set_k | `findings` (md-dir export) |
| **SCAN·codex-security** | subagent (leaf), parallel to the above | target + set_k | `codex-security-results/` (report + json) |
| **CONSOLIDATE** | orchestrator (this agent) | both scanner outputs | one normalized `findings.jsonl`: id, tool, file:line, severity, CWE, evidence, source-set |
| **JUDGE** | subagent (leaf, fresh context — *never* the same context as a scanner) | consolidated list + judge config | per-finding verdict + a pass verdict (`converge` / `continue` / `escalate`) |
| **APPLY** | subagent (leaf, coding agent) | judge-approved findings | fixes on a git branch, one commit per finding, finding→commit map |
| **VERIFY** | orchestrator | applied diffs | re-run affected tests + re-scan changed files; before/after evidence |
| **REPORT** | orchestrator | everything | final consolidated report + applied diff + per-set table |

**Edges (the loop):**

1. `SCAN·deepsec` + `SCAN·codex-security` → `CONSOLIDATE` (parallel fan-in).
2. `CONSOLIDATE` → `JUDGE`.
3. `JUDGE` → `APPLY` (approved findings) and → next-set edge.
4. `APPLY` → `VERIFY` → `JUDGE` (re-judge after fixes; regression → re-scan same set).
5. `JUDGE` → `SCAN` with `set_{k+1}` when sets remain and verdict ≠ `converge`.
6. `JUDGE` → `REPORT` when all sets are exhausted or verdict = `converge`.

See `references/graph.md` for the mermaid diagram.

## 3. The judge (advisor agent)

The judge is a **separate subagent** (fresh context; must not also be a scanner
in the same pass). It:

- Dedupes across tools and sets (deepsec dedupes across its own agents; the
  judge dedupes deepsec-vs-codex and set-vs-set).
- Assigns severity and marks each finding **auto-apply-safe** only when it is a
  confirmed true-positive with a low-risk, mechanical fix (typo'd sink, missing
  validation, hardcoded secret).
- Emits one **pass verdict**: `converge` (no new P0/P1 TP in a full pass),
  `continue` (next set or re-scan), `escalate` (stalemate / needs human).

Use the prompt template in `references/judge-prompt.md`.

## 4. Apply (auto) — safety rails

- All fixes land on a **dedicated git branch**; one commit per finding; never on `main`.
- Every change is a **revertable diff**, recorded in the finding→commit map.
- Prefer `npx @openai/codex-security patch <finding>` for Codex Security
  findings and a coding agent (`codex exec --sandbox workspace-write` or
  `opencode`) for deepsec findings; both on the branch.
- High-risk findings under `hybrid` policy are **prompted**, never silently applied.
- Secrets and `.env` are never committed.

## 5. Loop / stop rules

- Continue while: an un-run set remains, or VERIFY reported a regression, and
  `max_loops` is not hit.
- **Stalemate guard:** if the judge's `escalate` verdict repeats on the same
  finding across **two consecutive passes**, stop and hand to the human (do not spin).
- Stop only on: `converge`, `max_loops` reached, explicit user stop, or stalemate escalation.

## 6. Fine control knobs (surfaced at config time)

- N sets, each with its own model/harness/api.
- Per-set scope: `deepsec-only`, `codex-only`, or `both`.
- Separate judge model/harness (single or list).
- `auto` / `hybrid` / `manual` apply policy.
- deepsec `--thinking-level`, `--reinvestigate <N>`, `--batch-size`.
- `max_loops` and the convergence rule.

## 7. Progress file

Maintain `deepsec-orchestrator-progress.md`, updated after every pass:

| set | tool | findings | judge verdict | applied | round |

## Done when

- A normalized consolidated list exists for every requested set.
- The judge emitted a per-finding verdict AND a pass verdict for every pass.
- Every judge-approved fix is committed on the branch with a finding→commit map.
- The final REPORT + progress file are written, and the loop stopped on an allowed condition.
