---
name: deepsec-codex-luna
description: >-
  Dual-scan with deepsec and Codex Security on Luna. Use when combining
  deepsec with the open-source Codex Security CLI/plugin, running both
  scanners together, or asking for a Luna dual security scan.
---

# Deepsec + Codex Security on Luna

Run **both** scanners on the same target, both pinned to **Luna**.

## Luna pin

| Tool | Flag |
|------|------|
| deepsec (`process` / `revalidate` / `triage`) | `--model gpt-5.6-luna` (leave `--agent` unset) |
| Codex Security (`scan`) | `--model gpt-5.6-luna` |

## Steps

### 1. Resolve target

Pick one absolute path: the codebase under review (deepsec project `root`, or cwd).

**Done when:** that path is fixed for the rest of the run.

### 2. Deepsec pass

From the deepsec workspace (`.deepsec/`):

```bash
pnpm deepsec scan
pnpm deepsec process --model gpt-5.6-luna
pnpm deepsec revalidate --model gpt-5.6-luna
pnpm deepsec export --format md-dir --out ./findings
```

Skip `revalidate` only if the user asks for a faster pass.

**Done when:** `./findings` exists (or `process` finished if export was skipped).

### 3. Codex Security pass

Uses the open-source `@openai/codex-security` CLI (same scanner as the Codex Security plugin):

```bash
npx @openai/codex-security scan "$TARGET" \
  --model gpt-5.6-luna \
  --output-dir "$OUT/codex-security-results"
```

When deepsec `data/<id>/INFO.md` exists, pass it as scan context:

```bash
  --knowledge-base "$DEEPSEC/data/<id>/INFO.md"
```

Auth: `npx @openai/codex-security login`, or `OPENAI_API_KEY` / `CODEX_API_KEY`.

**Done when:** `$OUT/codex-security-results/report.md` exists.

### 4. Cross-read

Compare deepsec export vs Codex Security `findings.json` / `report.md`.

Bucket every notable issue as **both**, **deepsec-only**, or **Codex-only**.

**Done when:** the summary lists all three buckets (empty buckets named as empty).
