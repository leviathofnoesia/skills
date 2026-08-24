---
name: abyss-raindrop-observability
version: 0.1.0
author: Hermes
description: "Raindrop.ai-style observability plugin for Hermes agents."
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [Observability, Plugin, Hooks, Tracing, Graphs]
---

# Abyss — Raindrop-Style Observability for Hermes Agents

A Hermes desktop plugin + Python backend implementing **Raindrop.ai**-inspired observability: auto-recording of tool calls, LLM interactions, and session events with **self-diagnostics**, **signal detection**, and **incident clustering**.

## What it does

- Records every tool call, LLM call, and session lifecycle event into SQLite
- Detects **signals** (silent agent failures: errors, timeouts, rate limits, loops, vague replies)
- Clusters signals into **incidents** with shared root cause
- Provides a **self-diagnostic** API for agents to proactively report capability gaps
- Renders a **conversation trace timeline** per session
- Visualizes a **brain graph** (sessions → tools → memories → categories) via DitherKit canvas rendering

## What it does NOT do

- Does not send data to external services (local SQLite only)
- Does not provide distributed tracing across network boundaries
- Does not push fixes to external repos; agent-driven fixes stay on this machine

## Auto-heal (agent-powered resolve + doctor)

Resolve buttons and the health-tab doctor dispatch a **free-Nous Hermes agent**
(`hermes chat -q -s abyss-doctor`) that diagnoses and fixes the root cause on
the backend, then writes a JSON report the plugin uses to mark signals /
incidents resolved. Workflow is documented in the `abyss-doctor` skill.

## When to Use

- Building AI agent workflows needing production monitoring
- You want to catch "silent failures" traditional logging misses
- You need incident clustering and signal detection for debugging
- You want a visual brain graph of agent interactions (like Obsidian/Super Memory)

## Prerequisites

- Hermes Agent desktop app (v3+ recommended)
- Python 3.11+ (for backend API)
- SQLite3 (bundled with Python)
- Backend at `~/.hermes/plugins/abyss/`, UI at `~/.hermes/desktop-plugins/abyss/`

## How to Run

```bash
# Backend auto-loads when Hermes profile loads
# Desktop UI auto-discovers via desktop-plugins folder
# Manual test:
cd ~/.hermes/plugins/abyss && python test_plugin.py
```

## Quick Reference

### API Endpoints (ctx.rest from frontend)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/activity` | List activity (params: limit, category, since) |
| POST | `/activity` | Add activity entry (body: JSON) |
| GET | `/calendar` | List scheduled tasks (params: start, end) |
| GET | `/search` | Global search (params: q, limit) |
| GET | `/stats` | Dashboard summary |
| GET | `/trace` | Session trace (params: session_id, limit) |
| GET | `/graph` | Brain graph data (params: limit) |
| GET | `/signals` | Detected signals (params: session_id, limit) |
| GET | `/incidents` | Clustered incidents (params: status, limit) |
| POST | `/signals/self-diagnostic` | Record self-diagnostic |
| POST | `/incidents/cluster` | Run incident clustering |

### Slash Commands

| Command | Description |
|---------|-------------|
| `/abyss recent [N]` | Show last N activity entries |
| `/abyss stats` | Show summary statistics |
| `/abyss search <q>` | Search across all data sources |
| `/abyss trace <sid>` | Show conversation trace timeline |
| `/abyss signals` | Show detected signals |
| `/abyss incidents` | Show clustered incidents |
| `/abyss diagnostic <cap> <gap>` | Record a self-diagnostic |
| `/abyss clean` | Clear all data (irreversible) |

## Procedure

1. **Create plugin directories**:
```bash
mkdir -p ~/.hermes/plugins/abyss/dashboard
mkdir -p ~/.hermes/desktop-plugins/abyss
```

2. **Deploy backend** (`__init__.py`, `plugin.yaml`, `manifest.json`, `dashboard/plugin_api.py`)

3. **Deploy frontend** (`plugin.js` — single file, all components inlined)

4. **Enable plugin** in `config.yaml`:
```yaml
plugins:
  enabled: ["abyss"]
```

5. **Reload**: `⌘K` → "Reload desktop plugins"

6. **Verify**: `/abyss stats` returns data, sidebar shows "Abyss"

## Raindrop.ai Concepts Implemented

| Raindrop Concept | Abyss Implementation |
|-----------------|---------------------|
| **Signals** | Classifiers detect: error, timeout, rate_limit, loop, vague_reply |
| **Incidents** | 2+ signals in same session → clustered incident with severity |
| **Self Diagnostics** | `/abyss diagnostic <cap> <gap>` — agents report gaps directly |
| **Real failures** | Catches: wrong replies, loops, tool errors, persona drift |
| **Trace reading** | Full conversation timeline per session with event types |
| **Issue triage** | In-product view with acknowledge/resolve status |

## Pitfalls

- **Single-file UI plugin**: Runtime loader evaluates plugin.js as a Blob URL — relative imports won't resolve. All components must be inlined.
- **ctx.rest() returns PARSED JSON, not a Response**: `hermesDesktop.api` (electron/main.ts `fetchJson`) resolves with `JSON.parse(text)`. Never call `.json()` on the result — the incumbent UI silently swallowed `TypeError: r.json is not a function` in every view and showed empty data everywhere.
- **No `params` option in ctx.rest**: `PluginRestOptions` is `{method, body, upload, timeoutMs}` only. Query strings go in the PATH (`/activity?limit=50&category=cron`) — kanban's `withBoard()` is the reference pattern. The incumbent's filters never applied because `params` was silently dropped.
- **Dead Tailwind classes**: plugin.js is a Blob URL so Tailwind never scans its class strings. Only classes present in the host's compiled CSS (dist/assets/index-*.css) render. Verify every className against the compiled CSS; inline `style={{color:'var(--ui-*)'}}` for theme colors that lack compiled classes (most `--ui-blue/purple/orange/cyan` classes are NOT generated; only `bg-(--ui-green)`, `bg-(--ui-yellow)`, `text-(--ui-red/green/yellow)` exist). Canvas fillStyle/strokeStyle must use computed colors via `getComputedStyle`, never `var()` strings.
- **EmptyState has no icon prop** (title/description/className only); **TabsContent is not exported** — render views conditionally on activeTab.
- **Backend mount requires the plugin in the profile-scoped home + proper YAML**: `pluginRest` is profile-scoped, so the desktop backend (`--profile <name> serve`) discovers plugins from `profiles/<name>/plugins/<plugin>/dashboard/manifest.json` — the global `~/.hermes/plugins/` copy alone is NOT enough for a profile-scoped backend. Also `plugins.enabled` in the profile's config.yaml must be a real YAML list (`enabled:\n  - abyss`), not a quoted string (`'["abyss"]'`) — a string makes `_get_enabled_set()` return `set()` and the user plugin is filtered from API mounting (404 "Plugin not found"). After changing config or plugin files, restart the backend (`⌘K` → Restart gateway, or kill the `--profile <name> serve` python process so it respawns). Verify with `grep "Mounted plugin API routes" profiles/<name>/logs/gui.log` — an abyss line must appear.
- **SQLite concurrent access**: Backend uses thread locks for DB writes.
- **Signal false positives**: Vague reply detector may trigger on short-but-valid LLM responses. Tune the 20-char threshold as needed.
- **Graph performance**: Force-directed layout is CPU-bound. For >500 nodes, increase iterations or limit data.
- **Windows paths**: The plugin data path uses `Path.home()` which resolves correctly on Windows.

## Verification

```bash
cd ~/.hermes/plugins/abyss && python test_plugin.py
```

Expected:
```
Self-diagnostic signal #1 recorded
Incidents clustered: 0

=== API Endpoint Tests ===
[PASS] GET /activity -> list: 1 items
[PASS] GET /signals -> list: 1 items
[PASS] GET /incidents -> list: 0 items
[PASS] GET /trace -> list: 2 items
[PASS] GET /graph -> dict: 3 nodes, 2 edges
[PASS] GET /stats -> 1 total activities

All Abyss plugin tests passed!
```

Then in Hermes desktop:
1. "Abyss" appears in sidebar nav (codicon: eye)
2. `/abyss stats` returns data
3. Activity Feed updates after using tools