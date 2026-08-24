---
name: hermes-buzz-multi-profile-setup
description: Set up the native Buzz (Nostr) gateway platform for multiple Hermes profiles under gateway multiplexing, so each profile connects to a Buzz community with its own identity (nsec). Use when (re)configuring Buzz on Hermes, migrating off the old buzz-acp/relay-bridge workaround, or adding Buzz to several profiles.
---

# Hermes Buzz multi-profile setup (native gateway platform)

Connect each Hermes profile to a Buzz community as its own Buzz agent identity,
using the bundled native `buzz` platform plugin + `gateway.multiplex_profiles`.
No relay-bridge (`buzz-acp`) needed — full Hermes (memory, skills, approvals,
cron, sessions) stays intact per profile.

## When this applies
- You run Hermes as your agent and want Buzz as another messaging channel.
- You have several profiles and want each to be a distinct Buzz identity.
- The repo has `plugins/platforms/buzz/` (native adapter). If it doesn't, you
  are on an old build — update Hermes first.

## How it works (verified in source)
- `gateway.multiplex_profiles: true` (default profile's config.yaml) makes one
  gateway process serve the default profile + EVERY named profile dir under
  `profiles/`. See `hermes_cli/profiles.py::profiles_to_serve(multiplex=True)`.
- The multiplex loop adds `("default", _get_default_hermes_home())` (i.e.
  `~/.hermes`) PLUS every real named profile dir. It explicitly SKIPS any
  `profiles/default/` folder — `default` is reserved and maps to `~/.hermes`,
  not to `profiles/default/`. So do NOT create a `profiles/default/` directory;
  the "default" entry is the root home.
- Each profile's Buzz adapter reads that profile's own `profiles/<name>/.env`
  via scoped secrets (`gateway/run.py::_profile_runtime_scope`), and a scoped
  lock on `relay_url:pubkey` (`plugins/platforms/buzz/adapter.py`) prevents two
  profiles from driving one Buzz identity.
- Inbound = persistent NIP-42 WebSocket (BIP-340 signing, stdlib, no extra
  deps) with CLI-poll fallback. Outbound = `buzz` CLI. The `buzz` binary is at
  `hermes-agent/venv/Scripts/buzz.exe` on this host.

## Prerequisites
- `buzz` CLI binary on PATH or set via `cli_path` (pin to the venv binary).
- A Buzz community relay URL (BASE URL, `https://...`). The adapter derives the
  `wss://` WebSocket URL itself — do NOT put `wss://` in the relay value; the
  CLI rejects it.
- One Nostr private key (nsec or hex) per profile, each already a MEMBER of the
  community. Mint fresh keys if needed (see below).

## Steps

### 1. Enable multiplexing (default/root profile)
In `~/.hermes/config.yaml` (the DEFAULT profile's root config):
```yaml
multiplex_profiles: true
```
Top-level OR `gateway.multiplex_profiles` both accepted.

### 2. Per profile: enable buzz platform + display defaults
In each `profiles/<name>/config.yaml` (for every named profile you want on Buzz):
```yaml
gateway:
  platforms:
    buzz:
      enabled: true
      extra:
        relay_url: https://yourcommunity.communities.buzz.xyz   # BASE url, https://
        cli_path: C:/Users/billy/AppData/Local/hermes/hermes-agent/venv/Scripts/buzz.exe
        poll_interval: 4
        require_mention: true
        allow_all_users: false
display:
  platforms:
    buzz:
      interim_assistant_messages: false
      tool_progress: off
```

### 3. Per profile: secrets in `.env`
In each `profiles/<name>/.env`:
```
BUZZ_RELAY_URL=https://yourcommunity.communities.buzz.xyz
BUZZ_PRIVATE_KEY=nsec1...        # the only secret; unique per profile
BUZZ_ALLOW_ALL_USERS=true        # community mode; false for private
```
`BUZZ_PRIVATE_KEY` must NEVER be in config.yaml. The adapter reads it from the
env only and passes it to the CLI via subprocess env (never argv/logs).

### 4. Restart + verify
```
hermes gateway restart
hermes gateway status            # Buzz: connected per profile
```

## Minting keys (if you don't have pre-made nssecs)
Use the repo's own crypto so keys match the adapter's signing:
```python
import sys, secrets
sys.path.insert(0, r"hermes-agent/plugins/platforms/buzz")
import nostr_auth
priv = secrets.token_hex(32)          # 32-byte hex
nsec = nostr_auth.privkey_to_nsec(priv)   # NOTE: implement per nostr_auth helpers
pub  = nostr_auth.public_key_hex(nsec)
assert nostr_auth.decode_private_key(nsec) == int(priv, 16)   # roundtrip check
```
Write `nsec` only to `.env` (never print it). Keep `pub` for the enrollment sheet.
To convert pubkey hex -> npub for community UIs, reuse `hex_to_npub` from
`plugins/platforms/buzz/adapter.py` (it is in the adapter module, not nostr_auth).

## Pitfalls (learned the hard way)
- **Relay must be `https://`, not `wss://`.** kraken's old value was
  `wss://...` and the CLI/adapter need the base URL to derive WS.
- **YAML `x = cfg.setdefault(k, {}) or {}` is a BUG** -- an empty dict is falsy,
  so pre-existing `gateway: {}` / `display: {}` / `platforms: {}` blocks get
  their mutations silently dropped. Always mutate the loaded dict in place and
  re-dump; or replace the flow-style `{}` lines with explicit nested blocks.
- **The `gateway_lifecycle_guard` in this Hermes build crashes** (embedded-null
  path error) on terminal commands that reference a `.py` script path. Prefer
  `write_file`/`patch` for config edits, or run python with a bare absolute-path
  invocation and no `cd` prefix. If a `python script.py` terminal call fails
  with "embedded null character in path", that's the guard, not your script.
- **`search_files` tool is unreliable on MSYS `/c/...` paths** in this env --
  use `terminal` with `grep` instead.
- **The active profile in this deployment is `kraken`** (in `~/.hermes/active_profile`),
  but the desktop app spawns agent sessions under the built-in `default` home
  (`~/.hermes`), so a skill/tool writing into `profiles/kraken/...` from an
  agent session trips the cross-profile soft guard. Write profile-specific
  files with `cross_profile=True`, or place shared skills under the kraken
  profile dir explicitly. Do NOT create `profiles/default/` -- it is not a real
  profile and is ignored by multiplex (and confused the setup).
- Each new identity must be ENROLLED as a community member server-side, or the
  adapter logs "users get returned no profile -- is the key a member?" and fails
  connect. The private key alone is not enough.

## Verification checklist
- [ ] `~/.hermes/active_profile` says `kraken` (your real active profile)
- [ ] `~/.hermes/config.yaml` has `multiplex_profiles: true`
- [ ] every real `profiles/<name>/config.yaml` has `gateway.platforms.buzz.enabled: true`
- [ ] every real `profiles/<name>/config.yaml` has `display.platforms.buzz` (NOT `display: {}`)
- [ ] every `profiles/<name>/.env` has `BUZZ_RELAY_URL` (https) + `BUZZ_PRIVATE_KEY`
- [ ] `hermes gateway status` shows Buzz connected per profile after restart
- [ ] each pubkey enrolled in the community

## Enrollment sheet
The per-profile pubkeys (public, safe to share) are saved at
`~/.hermes/profiles/BUZZ_ENROLLMENT_SHEET.md`. Add new profiles there as you
expand.
