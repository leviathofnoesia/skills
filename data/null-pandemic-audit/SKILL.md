---
name: null-pandemic-audit
description: "Quantify and root-cause null inflation across tables/columns."
---

# Null-Pandemic-Audit

Quantify and root-cause null inflation across tables/columns..

## When to Use

Data quality complaints cluster around missing values; dashboards show gaps nobody trusts.

## Workflow

1. Quantify nulls per column over time — WHEN did null rates jump? Correlate with deploys/migrations.
2. Distinguish null semantics: missing-never-existed vs missing-failed-to-capture vs default-disguised-as-null.
3. Trace worst offenders to ingestion root cause: upstream API change, parser bug, backfill gone wrong.
4. Decide per column: backfill from source, accept-and-document, or fix-and-regenerate.
5. Add null-rate monitors so future pandemics page someone.

## Pitfalls

Backfilling without fixing the capture bug (nulls return). Treating zeros as nulls or vice versa in sources that conflate them. Fixing symptoms downstream while upstream keeps leaking.

## Verification

Null-rate trend lines flatten post-fix; monitoring would catch a recurrence within one cycle; documentation records chosen semantics per column.

## Inputs

- Task context: database access, deploy history

## Outputs

- root-caused audit + remediation + monitors

## Related

schema-drift-detector, metric-definition-sheet
