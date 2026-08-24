---
name: abyss-bench-probe
version: 0.1.0
author: Hermes
description: "Dry-run bench probe for Abyss observability instrumentation."
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Observability, Plugin, Abyss, Benchmark, Probe, DryRun]
    dry_run: true
---

# Abyss Bench Probe (Dry-Run)

This skill is a **dry-run benchmark probe** for the Abyss observability plugin
system. It is intended for testing and validating instrumentation without
persisting data to the Abyss SQLite backends.

## When to Use

- You want to verify Abyss hook payloads and signal detection logic in a
  no-side-effect mode.
- You are benchmarking Abyss overhead (hook latency, SQLite write cost) without
  polluting production traces.
- You need to validate a new signal classifier or incident-clustering rule
  against synthetic data.

## Dry-Run Semantics

- `dry_run: true` is declared in the frontmatter metadata.
- Probe executions do **not** write to `activity.db` or `traces.db`.
- All signal/incident logic still runs in-process so timing and classification
  can be measured.
- Results are emitted to the session log only.

## Procedure

1. Import the probe module from the Abyss plugin directory.
2. Invoke `_probe_run(dry_run=True)` to exercise the signal-detection pipeline.
3. Inspect the in-memory report (counts, latencies, classifications).
4. Tune thresholds or hook handlers as needed.

## Quick Reference

```bash
# Run the bench probe in dry-run mode
cd ~/.hermes/plugins/abyss && python bench_probe.py --dry-run
```

## Verification

```bash
python bench_probe.py --dry-run
# Expected: no writes to SQLite, timing report printed, exit 0
```