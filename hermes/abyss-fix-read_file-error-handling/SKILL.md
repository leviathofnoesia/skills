---
name: abyss-fix-read_file-error-handling
description: Fixes read_file errors with clear not-found and IO guidance.
version: 1.0.0
author: Abyss Doctor
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [abyss, read_file, file-tools, error-handling, windows-paths]
---

# Abyss Fix: read_file error/timeout handling

## When to Use
Use when Abyss reports `tool_error:read_file` or `timeout:read_file` signals,
especially on Windows with absolute paths or binary files.

## Problem
40 open `tool_error:read_file` signals and 9 open `timeout:read_file` signals.
On this Windows host, absolute-path reads and large-file reads fail with opaque
errors. The generic `except Exception` handler in `read_file_tool` swallowed
the specific error type and returned a bare string, making it impossible for
the model to diagnose.

## Root Cause
`tools/file_tools.py` `read_file_tool()` had a catch-all
`except Exception as e: return tool_error(str(e))` that lost the error type
and context. No specific handling for `FileNotFoundError`,
`PermissionError`, or `OSError`.

## Fix Applied
Added specific exception handlers in `tools/file_tools.py` (around line 1983):
- `FileNotFoundError` → "File not found: {e.filename or path}"
- `PermissionError` → "Permission denied: {e.filename or path} (check file
  permissions or that the path is accessible to this process)"
- `OSError` → "I/O error reading {path}: {e.strerror or str(e)}"
- Generic `Exception` → "Unexpected error reading '{path}': {type}: {e}"

## Verification
```bash
cd /path/to/hermes-agent
venv/Scripts/python.exe -c "
import json
from tools.file_tools import read_file_tool
result = json.loads(read_file_tool('/nonexistent/path'))
assert 'File not found' in result.get('error', '')
print('PASS: clear not-found error')
"

venv/Scripts/python.exe -m pytest tests/tools/test_file_tools.py -k "not_found or read" -v
# 7 passed
```

## Reusability
Apply whenever `read_file` produces opaque errors. The pattern of
type-specific exception handling can be extended to other file tools.
