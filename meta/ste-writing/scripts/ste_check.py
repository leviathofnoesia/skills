#!/usr/bin/env python3
"""Advisory ASD-STE100 structural linter (heuristic, stdlib-only).

Checks the mechanical STE writing rules that are derivable from plain text:
  - Sentence length (flag >20 words; note >25 descriptive limit)
  - Auxiliary/linking-verb misuse (passive & continuous constructions)
  - "-ing" words used as verbs
  - Multi-word noun strings longer than 3 capitalized words

Does NOT check the approved dictionary (copyrighted, ~900 words) or semantics.
This is an aid, not a spec substitute. Treat flags as a checklist.

Usage:
    python3 ste_check.py file.md
    cat file.md | python3 ste_check.py
"""
import argparse
import re
import sys
from pathlib import Path

# Auxiliary / modal / linking verbs that, combined with a participle or -ing,
# signal a non-approved complex or passive construction in STE.
AUX = {
    "am", "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "have", "has", "had",
    "will", "would", "shall", "should", "can", "could",
    "may", "might", "must",
}

# Common -ing words that are usually nouns, not verbs — skip them.
# Common -ing words that are technical/ordinary nouns, not verbs (avoid false
# positives in STE text, e.g. "bearing" in "pump bearing cover assembly").
ING_NOUNS = {
    "thing", "things", "something", "anything", "nothing",
    "during", "morning", "evening", "training", "testing",
    "building", "warning", "opening", "ceiling", "meeting",
    "painting", "clothing", "fishing", "housing",
    "bearing", "covering", "drilling", "seating", "fitting",
    "lining", "mounting", "piping", "tubing", "wiring",
    "handling", "cabling", "framing", "timing",
    "cooling", "heating", "lighting", "masking", "shielding",
}

# Words that may precede an -ing word legally as a noun modifier context.
DETERMINERS = {
    "the", "a", "an", "this", "that", "these", "those",
    "your", "each", "any", "no", "some", "its", "their",
    "our", "my", "one", "all",
}


def split_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def tokens(sentence):
    return re.findall(r"[A-Za-z0-9\-]+", sentence)


def check(text):
    report = []
    for idx, sent in enumerate(split_sentences(text), 1):
        toks = tokens(sent)
        n = len(toks)
        if n > 20:
            note = "over 20 words (procedure limit)"
            if n > 25:
                note += "; also over 25 (descriptive limit)"
            report.append((idx, f"LONG SENTENCE ({n} words): {note}", sent))

        lowered = [w.lower() for w in toks]

        # Auxiliary + participle (passive or continuous) => non-approved
        # complex construction. Catches "was installed" (past passive),
        # "is being checked", "will be checking", etc.
        flagged_aux = False
        for j, w in enumerate(lowered):
            if w in AUX:
                nxt = lowered[j + 1] if j + 1 < len(lowered) else ""
                if nxt.endswith("ing") or nxt.endswith("ed") or nxt in ("been", "being"):
                    report.append(
                        (idx, f"AUXILIARY + '{nxt}' — passive/continuous; "
                              f"prefer active or an approved verb form", sent)
                    )
                    flagged_aux = True
                    break

        # -ing word used as a verb (not a known noun, not after a determiner).
        if not flagged_aux:
            for j, w in enumerate(toks):
                wl = w.lower()
                if wl.endswith("ing") and wl not in ING_NOUNS:
                    prev = lowered[j - 1] if j > 0 else ""
                    if prev not in AUX and prev not in DETERMINERS:
                        report.append(
                            (idx, f"'-ing' word '{wl}' — use only as a "
                                  f"technical noun or modifier, not a verb", sent)
                        )
                        break

        # Long multi-word noun: a run of >=4 consecutive capitalized words
        # (a true noun string), broken by connectors/prepositions. Free-floating
        # caps words (e.g. "CHECK THE PRESSURE OF THE HYDRAULIC PUMP") should NOT
        # trip this — only adjoined noun clusters should.
        connectors = {
            "the", "of", "to", "a", "an", "for", "and", "or", "with",
            "on", "in", "at", "by", "from", "that", "this", "your",
            "into", "onto", "before", "after", "between", "near",
        }
        max_run = run = 0
        for w in toks:
            if re.match(r"^[A-Z][A-Za-z0-9]*$", w) and w.lower() not in connectors:
                run += 1
                max_run = max(max_run, run)
            else:
                run = 0
        if max_run >= 4:
            report.append(
                (idx, f"LONG NOUN STRING ({max_run} adjoined caps words) — "
                      f"keep multi-word nouns <=3 words", sent)
            )
    return report


def main():
    ap = argparse.ArgumentParser(description="Advisory ASD-STE100 linter.")
    ap.add_argument("path", nargs="?", help="file to check (default: stdin)")
    args = ap.parse_args()
    text = (
        Path(args.path).read_text(encoding="utf-8")
        if args.path else sys.stdin.read()
    )
    rep = check(text)
    if not rep:
        print("OK: no mechanical STE violations detected (heuristic; "
              "dictionary not checked).")
        return 0
    for idx, msg, sent in rep:
        print(f"[sentence {idx}] {msg}")
        print(f'    "{sent[:160]}"')
    print(f"\n{len(rep)} advisory flag(s). Review against ASD-STE100; "
          "dictionary compliance not checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
