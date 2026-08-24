---
name: pii-scanner
description: "Locate PII leaking into logs, fixtures, and exports."
---

# Pii-Scanner

Locate PII leaking into logs, fixtures, and exports..

## When to Use

Before shipping logs, fixtures, exports, or datasets anywhere outside the trust boundary.

## Workflow

1. Define PII classes relevant to jurisdiction (emails, names, IDs, free-text leak potential, quasi-identifiers).
2. Scan targets with pattern matching PLUS entropy analysis (catch base64'd secrets, hashed-but-guessable).
3. Check the sneaky vectors: error messages echoing payloads, debug flags dumping objects, fixture files copied from prod.
4. Grade findings: direct identifier / quasi-identifier / false positive.
5. Remediate: redact at source, mask in transit, or justify-and-document retention.

## Pitfalls

Regex-only scanning missing encoding tricks. Free-text fields ignored ('just notes'). Scanning once without CI enforcement. Confusing pseudonymization with anonymization.

## Verification

Scanner wired into CI blocks new leaks; deliberate seeded PII planted in test target gets caught; zero unjustified direct identifiers remain.

## Inputs

- Task context: target artifacts, jurisdiction requirements

## Outputs

- scan report + remediation + CI guard

## Related

secret-rotation-playbook, dataset-provenance
