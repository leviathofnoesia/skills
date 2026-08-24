---
name: provider-research-and-selection
description: "Research and select the best API provider for any model."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [providers, models, pricing, research, api, deepseek, openrouter, nous, optimization]
    category: mlops
    related_skills: [hermes-agent]
---

# Provider Research & Selection

## Overview

When a user asks "what's the best API for model X?" or "which provider should I use for Y?", follow this structured approach. This skill covers the *technique* of researching model providers and the *knowledge bank* of current pricing/access details.

## When to Use

- User asks which API/provider to use for a specific model
- Comparing costs across providers (official vs OpenRouter vs Nous Portal)
- Evaluating latency, throughput, or feature support
- Setting up a new provider in `hermes setup` / `hermes model`

## Research Methodology

### Step 1: Identify the Model Family and Current Generation

Search for the latest model version. Capture:

- Total parameters vs activated parameters (MoE models)
- Context window length
- Max output length
- Key features: JSON output, tool calling, thinking mode

### Step 2: Gather Official Pricing

From the provider's pricing page or API docs:

| Metric | What to capture |
|--------|----------------|
| Input cost | $/M tokens (cache miss) |
| Output cost | $/M tokens |
| Cache-hit input | $/M tokens (if supported) |
| Context window | tokens |
| Max output | tokens |

### Step 3: Enumerate API Access Paths

For each model family, identify all accessible routes:

1. **Official API** — direct endpoint, billed at official rates
2. **Nous Portal** — `https://inference-api.nousresearch.com/v1`
3. **OpenRouter** — unified API, ~5% surcharge
4. **Other resellers** — Together AI, Fireworks, etc.

Capture for each: base URL, auth method, whether the user has it configured.

### Step 4: Check User's Existing Config

Read the user's `config.yaml` and `auth.json` to see what's already set up. Always check the user's existing setup before recommending. If they already have free access (e.g., Nous Portal tier), that's the default recommendation.

### Step 5: Synthesize Recommendations

Rank paths by: **free access → lowest cost → lowest latency → broadest features**.

### Step 6: Document Findings

Write a `references/<provider>-research-<date>.md` file under this skill's directory with the condensed findings. This becomes a knowledge bank future sessions can consult.

## Integration with Hermes

### Configuring a Provider

```yaml
model:
  provider: openrouter
  default: deepseek/deepseek-v4-pro
```

### Model Aliases

```bash
# Session-scoped
hermes chat -q "/model deepseek/deepseek-v4-pro"

# Persistent alias
hermes config set model.aliases.deepseek_v4_pro "openrouter/deepseek/deepseek-v4-pro"
```

### Checking Access

```bash
hermes model --list
cat ~/.hermes/auth.json | python -c "import sys,json; d=json.load(sys.stdin); print([p for p in d.get('providers',{}).keys()])"
```

## Decision Matrix Template

| Provider | Input $/M | Output $/M | Latency | Throughput | Free Tier | Tool Call | Thinking Mode |
|----------|-----------|------------|---------|------------|-----------|-----------|---------------|
| Official |           |            |         |            |           |           |               |
| Nous     |           |            |         |            |           |           |               |
| OpenRouter |          |            |         |            |           |           |               |

## Pitfalls

- **Pricing changes silently.** Always note the date of research.
- **Free tiers have caps.** Ask if the user has experienced rate limits first.
- **Never assume the provider is configured.** Check `auth.json` and `config.yaml` before recommending.
- **`custom:<name>` is rejected by `resolve_provider()`.** Only bare `custom` (with `model.base_url`) is accepted as a provider string. A named `custom:<name>` identity requires a `providers:` block with a matching `provider_key`, resolved via `resolve_provider_full()`. `Unknown provider 'custom:...'` means the name was never registered (or lacks a `provider_key`). See `references/local-custom-providers.md`.
- **`fallback_providers` goes at the top level of config.yaml** — NOT nested under `model:`. Each entry is a dict with `provider`, `model`, and optionally `base_url`, `api_key`, `api_mode`. Use `provider: custom` with a `base_url` for local OpenAI-compatible endpoints (LM Studio, Ollama, vLLM, llama.cpp). `api_key` must be non-empty even if the server ignores it.
- **Never hand-edit `config.yaml` via a script.** Hermes blocks programmatic writes to config.yaml for safety. Use `hermes config set KEY VAL` or edit the file by hand in an editor. This applies to the fallback chain too — `hermes fallback add` is the CLI for appending entries.

## Knowledge Bank

Condensed research snapshots for specific models and providers:

- `references/deepseek-v4-research.md` — DeepSeek V4 Pro & Flash: pricing, architecture, API access paths, user config analysis
- `references/local-custom-providers.md` — Local OpenAI-compatible endpoints (LM Studio, Ollama, vLLM, llama.cpp): primary and fallback config, `Unknown provider 'custom:*'` diagnosis, resolution-path code references
- `hermes-agent/references/providers-and-models.md` — full provider catalog and auth methods (for general provider reference)