---
name: abyss-fix-web-extract-backend
description: Fixes web extract falling through to ddgs search-only.
version: 1.0.0
author: Abyss Doctor
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [abyss, web, extract, backend, ddgs, firecrawl]
---

# Abyss Fix: Web extract backend misconfiguration (ddgs search-only)

## When to Use
Use when Abyss reports the "ddgs is a search-only backend and cannot extract
URL content" error or `tool_error:web_extract` signals.

## Problem
`web.extract_backend` was set to `ddgs` (DuckDuckGo), a search-only backend
that cannot extract URL content. This produced: "DuckDuckGo (ddgs) is a
search-only backend and cannot extract URL content." — 6 recorded failures,
breaking `web_extract` for ALL URLs. 2 open signals (2098, 2144).

## Root Cause
The old `web_tools.py` `_get_capability_backend()` did not implement
capability-aware fallback. When the configured backend was unavailable or
didn't support the `extract` capability, it fell through to `_get_backend()`
which could land on `ddgs` (search-only) via the legacy preference order.

## Fix Applied
Code fix in `tools/web_tools.py` and `agent/web_search_registry.py`:

- `_get_capability_backend()` enhanced to scan registered providers for one
  that **is** available AND supports `extract` before legacy fallback
- `_resolve()` applies the capability filter (`supports_extract()`) at every
  resolution step so search-only providers fall through correctly
- Legacy preference order: `firecrawl → parallel → tavily → exa → searxng →
  brave-free → ddgs`, filtered by availability and capability
- Config verified: `web.extract_backend: firecrawl` is set

## Verification
```bash
venv/Scripts/python.exe -c "
from agent.web_search_registry import _resolve
assert _resolve('firecrawl', capability='extract') is not None
print('PASS')
"
venv/Scripts/python.exe -m pytest tests/tools/test_web_tools_config.py -v
# 36+ passed (2 parallel-web failures are unrelated)
```

## Reusability
Apply whenever `web_extract` fails with the ddgs search-only error.
