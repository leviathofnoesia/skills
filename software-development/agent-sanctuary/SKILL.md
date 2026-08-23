---
name: agent-sanctuary
description: Use when installing, browsing, or applying engineering-lifecycle skills from Agent Sanctuary (LivingLimes/agent-sanctuary) — spec, plan, build, test, review, ship workflows.
version: 0.1.0
author: Hermes
license: MIT
---

# Agent Sanctuary

Connect to **Agent Sanctuary** (`https://github.com/LivingLimes/agent-sanctuary`) —
a curated collection of production-grade software-engineering skills covering the
full development lifecycle:

```
DEFINE (/spec) → PLAN (/plan) → BUILD (/build) → TEST (/test) → REVIEW (/review) → SHIP (/ship)
```

## What Sanctuary is (research findings)

- A Claude Code plugin marketplace (`marketplace.json` name: `addy-agent-skills`,
  owner Addy Osmani) distributed as plain `skills/*/SKILL.md` files.
- 24 lifecycle skills under `skills/`: spec-driven-development,
  planning-and-task-breakdown, incremental-implementation, api-and-interface-design,
  frontend-ui-engineering, context-engineering, source-driven-development,
  doubt-driven-development, test-driven-development, debugging-and-error-recovery,
  code-review-and-quality, code-simplification, security-and-hardening,
  performance-optimization, git-workflow-and-versioning, ci-cd-and-automation,
  deprecation-and-migration, documentation-and-adrs, observability-and-instrumentation,
  shipping-and-launch, interview-me, idea-refine, browser-testing-with-devtools,
  using-agent-skills.
- Plus subagents (`agents/code-reviewer.md`, `security-auditor.md`,
  `test-engineer.md`, `web-performance-auditor.md`) and slash commands
  (`commands/*.toml`, `.claude/commands/*.md`).
- **No MCP server and no HTTP API exist** as of research time. Connection is
  therefore git/raw-HTTP based — do not invent an MCP endpoint.

## Workflow

1. **Resolve what the user needs.** Map their task to a phase:
   - Unknown requirements → `interview-me`, then `spec-driven-development`
   - Have a spec → `planning-and-task-breakdown`
   - Implementing → `incremental-implementation` (+ domain skill)
   - Broken → `debugging-and-error-recovery`; reviewing → `code-review-and-quality`
   - Releasing → `shipping-and-launch`
2. **Fetch the skill content** (raw HTTPS, no auth needed):

   ```
   curl -sSL https://raw.githubusercontent.com/LivingLimes/agent-sanctuary/main/skills/<skill-name>/SKILL.md
   ```

   List the full catalog first if unsure:
   ```
   curl -sSL "https://api.github.com/repos/LivingLimes/agent-sanctuary/git/trees/main?recursive=1"
   ```
3. **Apply it like any local skill**: follow its workflow sections against the
   user's repo. Sanctuary skills are process documentation — they need no
   runtime; the value is in executing the gates they describe.
4. **Persistent install (optional).** If the user wants it locally, download the
   chosen `SKILL.md` folders into this repo under `software-development/`
   (or the matching bucket), keeping original author/license attribution
   (MIT © Addy Osmani / LivingLimes), then regenerate the index with
   `skill-compiler marketplace`.

## Rules

- Prefer fetching only the specific SKILL.md needed; don't clone the whole repo
  unless installing multiple skills.
- Preserve attribution: upstream is MIT-licensed; keep license + copyright
  headers when copying content into local skill files.
- If raw fetch fails (network, rename), re-list the tree via the GitHub API to
  find the current path before giving up.
- Do not fabricate skill names — verify against the live tree listing.
