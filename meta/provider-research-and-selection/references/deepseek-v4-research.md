# DeepSeek V4 Provider Research (2026-08-01)

## Current Models

As of August 2026, the official DeepSeek model catalog (via api-docs.deepseek.com) shows two active API models:

### DeepSeek V4 Pro
- **Architecture**: 1.6T total params / 49B activated (Mixture-of-Experts)
- **Context window**: 1M tokens
- **Max output**: 384K tokens
- **Features**: JSON output, tool calling, thinking mode (both thinking and non-thinking)

### DeepSeek V4 Flash
- **Architecture**: 284B total params / 13B activated (Mixture-of-Experts)
- **Context window**: 1M tokens
- **Max output**: 384K tokens
- **Features**: JSON output, tool calling, non-thinking mode (efficiency-optimized)

## Pricing (from deepseek.ai/pricing, confirmed via OpenRouter catalog + tokenrate.dev)

| Model | Input $/M | Output $/M | Cache-hit input $/M |
|-------|-----------|------------|---------------------|
| V4 Pro | $0.435 | $0.87 | $0.0036 |
| V4 Flash | $0.14 | $0.28 | $0.0028 |

**Note**: As of May 23, 2026, DeepSeek permanently cut V4-Pro pricing by ~75% from pre-31 May 2026 rates ($1.74/$3.48 → $0.435/$0.87). Flash remained at $0.14/$0.28.

## API Access Paths

### 1. Official DeepSeek API
- **Endpoint**: `https://api.deepseek.com/v1` (OpenAI-compatible)
- **Auth**: `DEEPSEEK_API_KEY`
- **Billed at**: Official rates (table above)
- **Compliance note**: Direct access to a Chinese entity — some orgs restrict this

### 2. Nous Portal (user's current setup)
- **Endpoint**: `https://inference-api.nousresearch.com/v1`
- **Auth**: OAuth device flow (`hermes auth add nous`) or `NOUS_API_KEY`
- **Billed at**: Free tier available via user's poolside/laguna-s-2.1:free allocation
- **User config**: Already configured in `~/.hermes/profiles/kraken/config.yaml`
  ```yaml
  model:
    provider: nous
    default: poolside/laguna-s-2.1:free
    aliases:
      dsv4: custom:deepseek-v4-flash/deepseek-ai/DeepSeek-V4-Flash-0731
    base_url: https://inference-api.nousresearch.com/v1
  ```
- **Status**: User already uses DeepSeek V4 Flash via Nous Portal free tier

### 3. OpenRouter
- **Endpoint**: `https://openrouter.ai/api/v1`
- **Auth**: `OPENROUTER_API_KEY`
- **Billed at**: Official rates + ~5% surcharge (+ possible routing markup from Together/Fireworks)
- **Model paths**: `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash`
- **Status**: Not currently configured in user's Hermes (not in auth.json)

### 4. Other Resellers
- Together AI, Fireworks, Novita, etc. all route to DeepSeek but add their own markup
- Less relevant when Nous Portal free tier is available

## User's Current Setup Analysis

The user is **already optimally configured** for DeepSeek V4 Flash:

```yaml
# From config.yaml
model:
  provider: nous
  default: poolside/laguna-s-2.1:free
  aliases:
    dsv4: custom:deepseek-v4-flash/deepseek-ai/DeepSeek-V4-Flash-0731
```

- **Cost**: $0 (free tier via Nous Portal)
- **Model**: DeepSeek V4 Flash (284B MoE, 1M context)
- **Access**: Via `dsv4` alias or `/model dsv4` in any session
- **Default model**: poolside/laguna-s-2.1:free (also free)

## Recommendation

**Stay with Nous Portal** (current setup). The user already has free access to DeepSeek V4 Flash. Adding V4 Pro as an alias is recommended if the user wants higher quality at the cost of using Nous Portal credits (or setting up OpenRouter as fallback).

### V4 Pro Alias to Add

```bash
hermes config set model.aliases.dsv4p "openrouter/deepseek/deepseek-v4-pro"
```

(Requires setting up OpenRouter auth — but the user's Nous Portal may also expose V4 Pro under the same `custom` path pattern.)

## Knowledge Sources (2026-08-01)
- https://deepseek.ai/deepseek-v4 (model specifications)
- https://deepseek.ai/pricing (official pricing)
- https://openrouter.ai/deepseek/deepseek-v4-pro (OpenRouter catalog + pricing)
- https://openrouter.ai/deepseek/deepseek-v4-flash (OpenRouter catalog + pricing)
- https://api-docs.deepseek.com/ (official API docs)
- https://www.swfte.com/api-pricing/deepseek (pricing verification)
- https://andrew.ooo/answers/openrouter-vs-together-vs-fireworks-deepseek-v4-2026 (provider comparison)