---
name: deepsec-luna
description: >-
  Pin deepsec AI runs to Luna. Use when running deepsec process, revalidate,
  triage, or sandbox AI commands, or when the user mentions Luna, 5.6-luna,
  or gpt-5.6-luna for a scan.
---

# Deepsec Luna

Every deepsec AI invocation runs on **Luna**.

## Pin

On `process`, `revalidate`, and `triage` (including under `sandbox`), always pass:

```bash
--model gpt-5.6-luna
```

Leave `--agent` unset so deepsec keeps its default backend.

Example:

```bash
pnpm deepsec process --model gpt-5.6-luna
pnpm deepsec revalidate --model gpt-5.6-luna
```

Non-AI commands (`scan`, `export`, `report`, `status`, `metrics`, `enrich`) need no model flags.

## Done when

Every AI deepsec command in the turn includes `--model gpt-5.6-luna` and no `--agent` override.
