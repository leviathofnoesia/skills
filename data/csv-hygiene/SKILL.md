---
name: csv-hygiene
description: "Repair encoding, quoting, and type-coercion issues in CSVs."
---

# Csv-Hygiene

Repair encoding, quoting, and type-coercion issues in CSVs..

## When to Use

CSVs arrive from vendors/exports/legacy systems encoding chaos: mixed encodings, quoting lies, type-coercion surprises.

## Workflow

1. Detect encoding empirically (BOM check, invalid-byte mapping); convert to UTF-8 explicitly.
2. Validate structure: consistent column counts, quote pairing, delimiter sanity (commas inside fields handled?).
3. Type-audit each column: leading-zero ZIP codes, dates in five formats, floats that were currency, IDs coerced to scientific notation.
4. Normalize deliberately: document every coercion applied; never let parsers guess silently.
5. Emit a clean canonical version + a violations report for upstream feedback.

## Pitfalls

Excel's date auto-mangling already baked into the file. 'It opened fine' in one tool while another parsed differently. Assuming headers exist/are unique. Silent row skips from parse errors shrinking your dataset unnoticed.

## Verification

Row count matches source declaration; type audit table documents every column's coercion; round-trip through strict parser loses nothing.

## Inputs

- Task context: suspect CSV files

## Outputs

- canonical cleaned CSV + violation report + coercion log

## Related

timezone-normalizer, dataset-provenance
