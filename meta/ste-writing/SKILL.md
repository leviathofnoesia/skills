---
name: ste-writing
description: "Rewrite and check technical text against ASD-STE100 rules."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    tags: [Writing, Documentation, Controlled-English, Aerospace, STE]
---

# ASD-STE100 Technical Writing

Apply the ASD-STE100 Simplified Technical English (STE) writing rules when you
draft or revise technical documentation — procedures, descriptions, warnings,
and instructions — especially for audiences that include non-native English
readers. This skill encodes the rule set and a stdlib-only structural linter;
it does NOT ship the copyrighted approved-word dictionary (~900 words) and does
NOT auto-convert text. STE compliance still requires the official specification
plus human judgement.

## When to Use

- "Write this in STE" / "make this ASD-STE100 compliant"
- "Rewrite this procedure as Simplified Technical English"
- "Check this documentation against STE rules"
- "Simplify this technical text for non-native English readers"
- Drafting aircraft/maintenance/DOC instructions that must read unambiguously

## Prerequisites

- Python 3 (for the optional structural linter). No pip installs — stdlib only.
- The official spec is free from **asd-ste100.org** (Issue 9, Jan 2025: 53
  writing rules + ~900-word dictionary). Download it for authoritative
  dictionary lookups; this skill cannot redistribute the dictionary.
- Treat STE as an aid used *with* a style guide, not a replacement for one.

## How to Run

When writing or revising, apply the rules in the Procedure section directly.
For a mechanical sanity check of structural rules (length, voice, -ing, noun
strings), invoke the linter through the `terminal` tool:

```bash
python3 <skill_dir>/scripts/ste_check.py path/to/doc.md
# or pipe via stdin:
cat doc.md | python3 <skill_dir>/scripts/ste_check.py
```

Substitute `<skill_dir>` with this skill's resolved path (e.g.
`meta/ste-writing`). The linter is advisory only — it cannot check dictionary
compliance.

## Quick Reference

**The two parts of ASD-STE100**

1. Writing rules (grammar + style).
2. The dictionary (approved words with fixed parts of speech and meanings).

**Approved verb forms** (use only these; do not build complex tenses with
auxiliaries): infinitive, imperative, simple present, simple past, simple
future, past participle (only as an adjective).

**The writing rules (non-exhaustive core set)**

- Use approved words only as the part of speech and meaning given in the dictionary.
- Make instructions as clear and specific as possible.
- Do not write multi-word nouns that have more than three words.
- Use the approved forms of the verb only (see above).
- Do not use auxiliary verbs to make complex verb constructions.
- Use the "-ing" form of a verb only as a technical noun or as a modifier in a technical noun.
- Use the active voice. In descriptive writing, use the passive voice only when the agent is unknown.
- Write short sentences: no more than 20 words in instructions (procedures) and 25 words in descriptive texts.
- Do not omit parts of the sentence (verb, subject, article) to make text shorter.
- Use vertical lists for complex text.
- Write one instruction per sentence.
- Write only one topic per paragraph.
- Do not write more than six sentences in each paragraph.
- Start safety instructions with a clear command or condition.

**Dictionary columns** (per entry): Word (part of speech) · Approved meaning /
alternatives · STE example · Non-STE example. Principle: "one word, one part of
speech, one meaning." Approved words are UPPERCASE; unapproved words are
lowercase with suggested UPPERCASE alternatives.

## Procedure

1. **Identify text type.** Mark each block as a *procedure* (instruction/step)
   or a *description* (explanatory). Sentence limits differ (20 vs 25 words).
2. **One instruction per sentence; one topic per paragraph** (≤6 sentences).
   Break compound or run-on sentences into vertical lists where complex.
3. **Use approved verb forms only.** Prefer imperative ("REMOVE THE COVER") or
   simple present for procedures. Strip auxiliaries ("is being", "has been",
   "will be able to") down to an approved tense.
4. **Active voice.** Rewrite passives to active unless the doer is genuinely
   unknown. "The pin is installed by the technician" → "INSTALL THE PIN."
5. **Cap multi-word nouns at three words.** "hydraulic pump bearing assembly
   cover" → split or shorten ("bearing cover of the hydraulic pump assembly").
6. **Restrict "-ing" verbs.** "Checking the pressure" → "CHECK THE PRESSURE"
   (use -ing only as a technical noun, e.g. "drilling", or as a noun modifier).
7. **Replace unapproved words with dictionary alternatives.** If a word is not
   in the dictionary, use the suggested approved alternative or a different
   approved word — never invent a meaning for an approved word.
8. **Keep technical nouns/verbs.** Terms not in the dictionary but needed to
   describe the subject (e.g. "grease", "propeller", "to drill", "overhead
   panel") are permitted as technical nouns/verbs per the spec's Word section.
9. **Lead safety/cautions with a command or condition.** "TO PREVENT
   ACCIDENTS, INSTALL THE PINS." not "Accidents can be prevented by…"
10. **Run the linter** (`terminal`) for length/voice/-ing/long-noun flags, then
    fix and re-read for dictionary compliance against the official spec.

## Pitfalls

- **Dictionary is not included.** This skill guides rules; approved-word
  lookup needs the free official download. Never guess an approved meaning.
- **Checkers don't convert.** No tool (including this linter) turns non-STE into
  STE or guarantees grammar — it only flags likely mechanical violations.
- **Active vs passive.** Passive is allowed in *descriptions* only when the
  agent is unknown; in procedures, always active.
- **Sentence limits differ by type.** 20 words for procedures, 25 for
  descriptive text — don't apply one limit blindly.
- **One word, one meaning.** "close" (v) means move-together OR operate-a-
  breaker, never "close a meeting/business" (use END/FINISH). Adjective "close"
  → NEAR.
- **STE is not a standalone grammar guide.** ASD states it must be used with
  applicable specifications, style guides, and directives.
- **Linter is heuristic.** It flags -ing words and auxiliaries with simple
  rules and will have false positives/negatives; treat output as a checklist,
  not proof of compliance.

## References

- `references/ste-spec.md` — condensed sourced notes on the two-part structure,
  the dictionary's four columns, approved verb forms, technical-noun exceptions,
  the "STE is an aid" caveat, and where to download the free official spec.

## Verification

Run the structural linter and confirm it reports no length/voice/noun-string
flags on your revised text:

```bash
python3 <skill_dir>/scripts/ste_check.py revised.md
# expected: "OK: no mechanical STE violations detected ..."
```

Then self-audit manually: every sentence ≤20 words (procedure) or ≤25
(description), one instruction per sentence, active voice, no auxiliary-built
tenses, multi-word nouns ≤3 words, and all content words traceable to the
approved dictionary or a permitted technical term.
