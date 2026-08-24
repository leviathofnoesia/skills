---
name: translation-handoff-kit
description: "Package copy for translators: context, glossary, constraints."
---

# Translation-Handoff-Kit

Package copy for translators: context, glossary, constraints..

## When to Use

Copy heads to translators/locales and context-free strings come back wrong.

## Workflow

1. Package source copy with per-string context: where it appears, character limits, what it acts on.
2. Build the glossary: canonical terms with approved translations or keep-as-is marks.
3. Flag culture-sensitive content: dates, currency, humor, idioms (usually rewrite, don't translate).
4. Provide visual references: screenshots showing each string in situ.
5. Define the QA loop: in-context review before ship, native-speaker spot check on critical flows.

## Pitfalls

String files without context (translators guess). Hard-coded concatenation breaking word order in other languages. Assuming English length; German overflows buttons. Idioms translated literally into nonsense.

## Verification

Translator asks zero 'where does this appear' questions; localized UI passes in-context review on critical flows; no truncated/truncated-overflow strings.

## Inputs

- Task context: source copy, string files, screenshots

## Outputs

- context-complete translation package + glossary

## Related

terminology-consistency, style-guide-distiller
