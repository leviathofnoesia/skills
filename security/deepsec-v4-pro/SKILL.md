---
name: deepsec-v4-pro
description: "Scan with deepsec on DeepSeek V4 Pro; ask harness/api."
---

# DeepSec — DeepSeek V4 Pro

Run deepsec (the Vercel Labs AI vulnerability scanner) with the **DeepSeek V4
Pro** model. The harness (`--agent` backend) and API (endpoint + key) are
**never hardcoded** — you must ask the user for them before running anything.

## When to Use

- Run a deepsec `process` / `revalidate` / `triage` with DeepSeek V4 Pro.
- The user says "scan with v4 pro", "deepsec pro", or names a DeepSeek V4 Pro
  endpoint or gateway.

```mermaid
flowchart LR
    A[Ask: target, model id, harness, api] --> B[Run process]
    B --> C[Revalidate and triage]
    C --> D[Export findings]
    D --> E[Done]
```

> **For humans:** read `human.md` for a full guide with diagrams.

## 1. Ask the user (MANDATORY — stop and ask before any command)

DeepSeek is not a first-class deepsec backend, and model ids differ by
endpoint. Collect all four before running, in this shape:

1. **target** — absolute path to the codebase (the deepsec project `root`, or cwd).
2. **model id** — the exact DeepSeek V4 Pro identifier for *their* endpoint
   (e.g. `deepseek-reasoner`, `deepseek-ai/DeepSeek-V4-Pro-<date>`, or a gateway id).
3. **harness** — which deepsec backend reaches DeepSeek: `pi` or `codex`.
4. **api** — base URL + the env var name holding the key (e.g.
   `https://api.deepseek.com/v1` + `DEEPSEEK_API_KEY`).

If any of the four is missing, ask again. Never assume a base URL, a key env,
or a model id.

## 2. Run

From the deepsec workspace (`.deepsec/`, where `deepsec.config.ts` and `pnpm`
live). Substitute the user's values for `<id>`, `<model-id>`, `<base-url>`,
`<KEY_ENV>`.

- **Harness = `pi`** (generic OpenAI-compatible provider override — the
  documented path for arbitrary endpoints):

  ```bash
  pnpm deepsec process --project-id <id> \
    --agent pi \
    --model "<model-id>" \
    --ai-provider openai \
    --ai-base-url "<base-url>" \
    --ai-api-key-env <KEY_ENV>
  ```

- **Harness = `codex`** (OpenAI SDK, env override):

  ```bash
  OPENAI_BASE_URL="<base-url>" OPENAI_API_KEY="$<KEY_ENV>" \
    pnpm deepsec process --project-id <id> --agent codex --model "<model-id>"
  ```

## 3. Revalidate & triage (same harness/api)

```bash
# pi harness
pnpm deepsec revalidate --project-id <id> --agent pi --model "<model-id>" \
  --ai-provider openai --ai-base-url "<base-url>" --ai-api-key-env <KEY_ENV>

# codex harness: export OPENAI_BASE_URL / OPENAI_API_KEY, then
pnpm deepsec revalidate --project-id <id> --agent codex --model "<model-id>"

# triage (cheap; same model)
pnpm deepsec triage --project-id <id> --model "<model-id>"
```

## 4. Export

```bash
pnpm deepsec export --format md-dir --out ./findings
```

## Done when

- `./findings` exists (or `process` finished if export was skipped).
- Every AI command in the turn carried the user's harness + api, and no command
  hardcoded them.
