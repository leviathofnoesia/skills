---
name: abyss-fix-terminal-none-command
description: Fixes terminal errors when command arg is null/non-string.
version: 1.0.0
author: Abyss Doctor
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [abyss, terminal, tool-validation, model-tools]
---

# Abyss Fix: Terminal None/non-string command validation

## When to Use
Use when Abyss reports `terminal.none_arg` ("expected string, got NoneType")
or `tool_error:terminal` signals from `command=None` or `command={}`.

## Problem
When the model emits `terminal(command=None)` or `terminal(command={})`, the
terminal tool receives a non-string argument. Before this fix, this surfaced as
the opaque `exit -1` / `Invalid command: expected string, got NoneType` error
that the model cannot recover from in one shot. The Abyss observability DB
tracked this as the `terminal.none_arg` signature (signal class:
`tool_error:terminal`, 64+ open signals).

## Root Cause
`hermes-agent/model_tools.py` forwarded function arguments directly to the
terminal tool without pre-validating required string fields. The terminal tool
itself (`tools/terminal_tool.py`) rejected the non-string value but produced a
bare `exit -1` with a terse error.

## Fix Applied
Two layers in `hermes-agent/model_tools.py` (around lines 1180-1286):

1. **`_REQUIRED_STR_ARGS`** dict — declares which tools require non-None string
   args (`terminal.command`, `write_file.path/content`,
   `patch.path/old_string/new_string`, `read_file.path`, `search_files.pattern`).

2. **`_repair_none_args()`** — called at the top of `handle_function_call()`
   before dispatch. If a required string field is present but None/non-string,
   it returns a `tool_error()` with a precise message naming the offending key
   and the expected type, so the model can repair the call on the next turn.

3. **`tools/terminal_tool.py`** enhanced error message (line ~2575) — when a
   non-string command is received, the error now explains WHY (null argument
   usually means the key was omitted or passed as an object) and shows the
   correct usage.

## Verification
```bash
cd /path/to/hermes-agent
venv/Scripts/python.exe -m pytest tests/tools/test_terminal_none_command_guard.py -v
# 2 passed

venv/Scripts/python.exe -m pytest evals/abyssbench/test_probes.py -k "term-none-arg" -v
# 1 passed
```

## Reusability
This fix is reusable whenever the terminal tool or any tool in
`_REQUIRED_STR_ARGS` starts producing opaque `exit -1` errors from bad
argument types.
