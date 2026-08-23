---
name: env-repro
description: "Reproduce an environment-specific bug by isolating OS, version, and config diffs."
---

# Environment Repro

Reproduce bugs that "only happen on my machine / on the server / in CI" by
systematically diffing the failing environment against a working one, then
building a minimal local reproduction. Turns unreproducible reports into
test cases.

## When to Use

- A bug reproduces in one environment but not another: dev vs CI, Windows
  vs Linux, user's machine vs yours, staging vs prod. Use for "can't
  reproduce", "works locally", "CI-only failure".
- Differentiator: diffs environments along named dimensions instead of
  guessing; ends with a minimal repro that runs anywhere.

## Workflow

1. **Capture both environments** (failing + working), per dimension:
   - Runtime versions (`python --version`, `node -v`, package lock state).
   - OS/arch and relevant kernel/libc traits; container base image.
   - Env vars that the code reads (not the whole environment).
   - Config files, feature flags, timezone/locale, filesystem case
     sensitivity.
2. **Diff the dimensions.** Rank differences by plausibility against the
   failure mode: a case-folding difference matters for path handling; a
   locale difference matters for sorting/parsing; a version skew matters
   for API behavior. One hypothesis per ranked difference.
3. **Test hypotheses cheaply**, cheapest first: set/unset the var, toggle
   the flag, install the exact pinned version, run under the other OS via
   container/VM if available. Change one variable at a time and record the
   outcome.
4. **Minimize.** Once reproduced, shrink to the smallest script/input that
   still fails — this becomes the regression test or issue repro.
5. **Document**: exact failing conditions (versions + settings), minimal
   repro steps, and which dimension was causal.

## Rules

- Never declare "cannot reproduce" without listing which dimensions you
  ruled out with what experiment.
- Respect secrets: capture env-var *names* and config structure, never
  values of credential-looking variables.
- If reproduction requires hardware/OS you lack, deliver the minimal repro
  recipe plus a CI matrix suggestion instead of guessing.

## Failure handling

- No access to the failing environment → work from its captured artifacts
  (logs, crash dumps, `env` dump sanitized) and mark untested hypotheses
  clearly.
- Bug reproduces only under load → say so explicitly and hand off to
  load-shaping rather than looping single-threaded attempts.
