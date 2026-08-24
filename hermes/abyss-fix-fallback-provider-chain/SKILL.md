---
name: abyss-fix-fallback-provider-chain
description: Fixes fallback chain when config stores it as YAML string.
version: 1.0.0
author: Abyss Doctor
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [abyss, provider, fallback, resilience, config, lm-studio]
---

# Abyss Fix: Fallback provider chain resilience

## Problem
The fallback provider chain was silently disabled because `fallback_providers`
in `config.yaml` was stored as a single-quoted YAML **string** rather than a
proper YAML list. `get_fallback_chain()` in `hermes_cli/fallback_config.py`
only handled `dict` and `list` inputs — a string returned an empty list `[]`.
This meant:
- `empty_stream` signals (37 open) cascaded with no failover
- `rate_limit` signals (29 open) retried against the same exhausted provider
- `api_error` signals on `opencode-go` (5 open) had no alternate path
- 13 `loop_detected` signals resulted from retry storms

## Root Cause
Two issues:
1. **`config.yaml`** stored `fallback_providers` as a YAML string:
   `fallback_providers: '[{provider: custom, ...}]'`
   This is valid YAML (the value is a string), but `get_fallback_chain()`
   expected a list of dicts.

2. **`hermes_cli/fallback_config.py`** `_iter_fallback_entries()` did not
   handle the string case — it only checked `isinstance(raw, dict)` and
   `isinstance(raw, list)`, silently returning `[]` for any other type.

## Fix Applied
Two changes:

### 1. Code fix: `hermes_cli/fallback_config.py`
Extended `_iter_fallback_entries()` to handle string inputs by attempting JSON
then YAML parsing. This is a defensive fix that handles configs where
`fallback_providers` was serialized as a string (common with older config
writers or manual edits).

### 2. Config fix: `config.yaml` (via `hermes_cli/config.py` save_config)
Converted the string value to a proper YAML list:
```yaml
fallback_providers:
  - provider: custom
    model: lfm2.5-2.6b
    base_url: http://127.0.0.1:1234/v1
    api_key: lm-studio
    api_mode: openai_chat
```

## How It Works
The fallback chain flows through:
1. `cli.py` — `self._fallback_model = get_fallback_chain(CLI_CONFIG)` (line ~4677)
2. `cli_agent_setup_mixin.py` — `_fb_chain` used in `_ensure_runtime_credentials()`
   for auth-failure failover
3. `agent/agent_init.py` — `fallback_model` param sets `agent._fallback_chain`
4. `agent/chat_completion_helpers.py` — `try_activate_fallback()` walks the
   chain on `rate_limit`, `billing`, `upstream_rate_limit`, `empty_stream`, etc.
5. `run_agent.py` / `hermes_cli/oneshot.py` — both pass `fallback_model=_fb or None`
   to AIAgent

Rate-limit backoff escalates: 60s → 2m → 4m → 8m → ... → 4h cap
(#11314, #13636). Chain-exhausted cooldown prevents cross-turn replay storms
(#24996).

## Verification
```bash
cd /path/to/hermes-agent
venv/Scripts/python.exe -c "
import yaml
from hermes_cli.fallback_config import get_fallback_chain
with open('config.yaml') as f:
    cfg = yaml.safe_load(f)
chain = get_fallback_chain(cfg)
assert any(e.get('provider')=='custom' and '127.0.0.1:1234' in e.get('base_url','') for e in chain)
print('PASS: fallback chain includes LM Studio')
"

venv/Scripts/python.exe -m pytest tests/gateway/test_fallback_chain_reload.py tests/run_agent/test_provider_fallback.py -v
# 18 passed
```

## Trigger Conditions
- Abyss signals: `empty_stream`, `rate_limit`, `api_error`, `loop_detected`
- Config inspection: `get_fallback_chain(cfg)` returns `[]`
- `hermes config get fallback_providers` shows a string instead of a list

## Reusability
Apply whenever the fallback chain appears configured but doesn't activate on
provider failures. Check both config format and `_iter_fallback_entries`.
