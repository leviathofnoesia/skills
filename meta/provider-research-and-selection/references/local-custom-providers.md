# Local Custom Providers (LM Studio, Ollama, vLLM, llama.cpp)

How to wire local OpenAI-compatible endpoints into Hermes — either as the
primary model or as a fallback provider. Covers the `Unknown provider
'custom:*'` error and the correct configuration for local runtimes.

## The `custom` provider

Hermes has a built-in bare `custom` provider for any OpenAI-compatible
endpoint. It is distinct from the named `custom:<name>` providers that live
under the `providers:` key — those require a `provider_key` and are resolved
through `resolve_custom_provider()`. The bare `custom` provider is resolved
through `resolve_provider()` in `hermes_cli/auth.py`, which accepts `custom`
but **rejects `custom:<anything>` with `Unknown provider`**.

### Common error

```
agent init failed: Unknown provider 'custom:lm-studio-custom'.
  Check 'hermes model' for available providers, or run 'hermes doctor'
  to diagnose config issues.
```

 **Root cause**: `model.provider` (or a fallback entry's `provider`) is set to
 `custom:<name>` but:
1. No matching entry exists under `providers:` in config.yaml, OR
2. The entry exists but lacks a `provider_key`, so `resolve_provider_full()`
   cannot map `custom:<name>` back to it.

### Fix — bare `custom` with `base_url` (simplest)

Set `model.provider: custom` and put the endpoint URL in `model.base_url`:

```yaml
model:
  provider: custom
  default: lfm2.5-2.6b          # model id as the server reports it
  base_url: http://127.0.0.1:1234/v1
  api_key: lm-studio            # non-empty placeholder; LM Studio ignores it
  api_mode: openai_chat
```

### Fix — named `custom:<key>` (durable identity)

Use the `providers:` keyed format with a `provider_key`. The key becomes the
`custom:<key>` identity that `resolve_provider_full()` can find:

```yaml
providers:
  lm-studio-custom:
    name: LM Studio Custom
    base_url: http://127.0.0.1:1234/v1
    api_key: not-needed
    api_mode: openai_chat
    provider_key: lm-studio-custom
    discover_models: false
    tools: false
    models:
      lfm2.5-2.6b:
        name: LFM2.5 2.6B
        tools: false
        contextWindow: 131072
```

Then `model.provider: custom:lm-studio-custom` resolves correctly.

## Fallback providers (local model as backup)

To use a local endpoint as a **fallback** (tried when the primary fails with
429/503/529 or connection errors), add a `fallback_providers` block at the
top level of config.yaml (NOT nested under `model:`):

```yaml
fallback_providers:
  - provider: custom
    model: lfm2.5-2.6b
    base_url: http://127.0.0.1:1234/v1
    api_key: lm-studio
    api_mode: openai_chat
```

Key points:
- **`provider: custom`** — not `custom:<name>`. The fallback chain
  (`hermes_cli/fallback_config.py → get_fallback_chain()`) accepts a
  `provider` + `model` + `base_url` dict; bare `custom` with `base_url` is
  the supported shape for local endpoints.
- **`api_key` must be non-empty** — Hermes needs a value here or auth will
  bail out before reaching the endpoint. LM Studio / Ollama ignore the value.
- **`api_mode: openai_chat`** — tells Hermes to use the OpenAI chat
  completions endpoint, which is what these local servers expose.

### Managing the chain via CLI

```bash
hermes fallback list                    # show current chain
hermes fallback add                     # interactive picker (same as hermes model)
hermes fallback remove                  # remove an entry
hermes fallback clear                   # clear all
```

The `add` subcommand launches the same picker as `hermes model`, then appends
the selection to `fallback_providers`. It snapshots `model` and
`auth.active_provider` before the picker runs and restores them after, so the
primary is not clobbered.

## Common local runtimes

| Runtime    | Default base URL                  | Notes |
|-----------|-----------------------------------|-------|
| LM Studio | `http://127.0.0.1:1234/v1`       | Built-in `lmstudio` provider exists (`hermes_cli/auth.py` → PROVIDER_REGISTRY); bare `custom` also works. |
| Ollama    | `http://127.0.0.1:11434/v1`      | Alias `ollama` maps to `custom` in `resolve_provider()`. |
| vLLM      | `http://127.0.0.1:8000/v1`       | Use bare `custom` with `base_url`. |
| llama.cpp | `http://127.0.0.1:8080/v1`       | Aliases `llamacpp`/`llama.cpp`/`llama-cpp` map to `custom`. |

### Built-in `lmstudio` provider

There is a registered `lmstudio` provider in `PROVIDER_REGISTRY` (auth.py ~line 212):
```python
"lmstudio": ProviderConfig(
    id="lmstudio",
    name="LM Studio",
    auth_type="api_key",
    inference_base_url="http://127.0.0.1:1234/v1",
    api_key_env_vars=("LM_API_KEY",),
    base_url_env_var="LM_BASE_URL",
)
```
Aliases `lm-studio` and `lm_studio` normalize to `lmstudio`. So
`provider: lmstudio` also works without a `base_url` (it defaults to
127.0.0.1:1234). Use bare `custom` when you need a non-default port or want
the same shape as other local runtimes.

## Diagnostic steps

1. **Confirm the local server is running** — `curl -s http://127.0.0.1:1234/v1/models`
   should return a JSON list of model ids.
2. **Check current config** — `cat $HERMES_HOME/profiles/<profile>/config.yaml`
   (or `~/.hermes/config.yaml` for the default profile).
3. **Check fallback chain** — `hermes fallback list`.
4. **Run the health check** — `hermes doctor` (may take 30s+; on some systems
   it can hang — check `~/.hermes/logs/` directly if needed).
5. **Never hand-edit config.yaml directly via a script** — Hermes blocks
   programmatic writes to config.yaml for safety. Use `hermes config set`
   or edit the file by hand in an editor.

## Resolution path (code reference)

- `hermes_cli/auth.py → resolve_provider()` (~line 1937): handles `custom`
  (bare) and registered providers; rejects `custom:<name>` with `Unknown
  provider` unless the name resolves.
- `hermes_cli/auth.py → resolve_provider_full()` (imported into main.py ~line
  3069): resolves `custom:<name>` through `compatible_custom_providers` and
  the `providers:` config block.
- `hermes_cli/fallback_config.py → get_fallback_chain()`: merges
  `fallback_providers` (list) and legacy `fallback_model` (dict) into the
  effective chain.
- `hermes_cli/runtime_provider.py → _auto_detect_local_model()`: when
  `model.base_url` points at localhost and no `model.default` is set, Hermes
  auto-detects the model id from `{base_url}/models`.
