---
name: log-mining
description: "Extract signal from large logs: triage, window around errors, correlate."
---

# Log Mining

Pull actionable findings out of large or streaming logs without reading
them end to end. Works on application logs, CI output, server journals,
and crash dumps with text layers.

## When to Use

- "Why did the build/CI/server fail", "find errors since X", "what happened
  around 14:32", "summarize this 100MB log". Any log too big to read
  linearly.
- Differentiator: windows and correlates instead of grepping for ERROR and
  calling it done — most root causes appear *before* the error line, not
  in it.

## Workflow

1. **Shape first.** Determine format (plain/JSON lines/syslog), timestamp
   format, and time span covered — `head`/`tail` a few hundred lines plus a
   line count. Note rotation boundaries if multiple files exist; sort by
   timestamp across files before analysis.
2. **Triage pass.** Count occurrences by severity/keyword pattern
   (`ERROR|WARN|panic|exception|failed`) with counts per type, not full
   lines. This ranks what deserves windows.
3. **Window around hits.** For each significant hit, extract N context
   lines *before* the match (root causes precede symptoms) and fewer after.
   Read windows in timestamp order.
4. **Correlate across sources.** When several logs cover one incident,
   align by timestamp: client↔server, app↔infra, build↔test. The first
   anomaly in causal order is usually the culprit, not the loudest error.
5. **Report** with: timeline of the incident (few events, timestamped),
   root-cause hypothesis with cited `file:line`, and the exact commands to
   reproduce your extraction so others can verify.

## Rules

- Never report an error's message as its cause without reading its window.
- Quote timestamps verbatim; do not normalize them silently.
- For JSON-lines logs, parse programmatically (jq/script) rather than
  eyeballing — filter by field, aggregate counts, then window.

## Failure handling

- Timestamps missing/unparseable → use line offsets and file order, and
  say correlation confidence is lower.
- Log truncated mid-incident → state what span you actually have; do not
  extrapolate beyond the edges.
- Binary/compressed files → decompress to scratch first (`zcat`, `zstd -d`),
  never grep compressed bytes.
