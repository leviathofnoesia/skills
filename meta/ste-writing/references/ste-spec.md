# ASD-STE100 Reference Notes

Condensed, sourced reference material for the `ste-writing` skill. Captured from
the official site (asd-ste100.org) and Wikipedia during skill authoring; not a
substitute for the specification itself.

## Two-part structure of ASD-STE100

1. **Writing rules** — grammar and style rules. Issue 9 (Jan 2025) has **53
   rules**. The rules separate two text types: *procedures* (instructions) and
   *descriptions* (explanatory text). Some limits differ by type (see below).
2. **Dictionary** — approximately **900 approved words**, each permitted only
   as a specific part of speech and meaning.

## The dictionary: four columns

Per entry (from the spec's example table):

- **Word (part of speech)** — the word and its allowed part of speech.
  Principle: *"one word, one part of speech, one meaning."* Approved words are
  written UPPERCASE; unapproved words are lowercase with suggested UPPERCASE
  alternatives.
- **Approved meaning / alternatives** — the approved definition. If a meaning is
  not in the dictionary, you cannot use the word in that meaning; use an
  alternative. For unapproved words, gives suggested replacements (usually the
  first suggestion keeps the same part of speech).
- **STE example** — shows one way to use the approved word/alternative. Wording
  is *not mandatory*; other approved constructions may keep the same meaning.
- **Non-STE example** — how the unapproved word is often used in standard
  technical writing, to illustrate the approved alternative. Empty for approved
  words unless a help symbol flags other meanings/restrictions.

## Approved verb forms (use ONLY these)

- infinitive
- imperative
- simple present
- simple past
- simple future
- past participle (only as an adjective)

Do **not** build complex tenses with auxiliary verbs (e.g. "is being",
"will be able to", "has been").

## Technical nouns and verbs NOT in the dictionary

Per the spec's Word section (writing rules 1.5 and 1.12), terms needed to
describe the subject are approved even if absent from the dictionary — e.g.
"grease", "discoloration", "propeller", "aural warning system", "overhead
panel", "to ream", "to drill". These are technical nouns/verbs, not general
vocabulary.

## Worked contrast (from the spec)

- Non-STE: "Before acceptance of unit, do the specified test procedure."
- STE:    "BEFORE YOU ACCEPT THE UNIT, DO THE SPECIFIED TEST PROCEDURE."
- Non-STE: "Rotate the cover until the jacks marked + and − are accessible."
- STE:    "TURN THE COVER UNTIL YOU CAN GET ACCESS TO THE JACKS THAT HAVE +
  AND − MARKS."

## STE is an aid, not a replacement

ASD states in the spec front matter: *"Can STE be used alone? No. It is intended
to be used with other applicable specifications for technical publications,
style guides, and official directives. A high standard of professionalism is
necessary to use the STE specification correctly."*

Checkers (Boeing BSEC, HyperSTE, Congree, TechScribe) only *highlight* suspected
non-STE; they do not write STE or convert non-STE to STE, and are not
fool-proof. The author decides.

## Procuring the specification

Free official copy of the current issue (Issue 9, Jan 2025) from
**asd-ste100.org** via its online form / download page. Copyright and trademark
of ASD, Brussels — the dictionary content must not be redistributed; this skill
therefore links to the source rather than bundling it.

## Sentence limits (rule summary)

- Procedures (instructions): **≤ 20 words** per sentence.
- Descriptive text: **≤ 25 words** per sentence.
- No more than **6 sentences** per paragraph; one topic per paragraph.
- One instruction per sentence; vertical lists for complex text.
- Multi-word nouns: **≤ 3 words**.
- Active voice; passive only in descriptions when the agent is unknown.
- Safety instructions start with a clear command or condition.
