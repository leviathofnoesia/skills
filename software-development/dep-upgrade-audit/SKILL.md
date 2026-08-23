---
name: dep-upgrade-audit
description: "Upgrade a dependency safely: changelog, breaking-change audit, staged bump."
---

# Dependency Upgrade Audit

Perform a dependency upgrade as a verified migration, not a version-number
edit: survey what changed upstream, map it onto how this repo uses the
dependency, bump in stages, and prove nothing broke.

## When to Use

- Bumping any direct dependency past a minor boundary, or anything that
  emits deprecation warnings. Use for "upgrade X", "bump Y", "update
  dependencies", "why is this package pinned".
- Differentiator: reads the upstream changelog/release notes against this
  repo's actual usage sites before touching the lockfile.

## Workflow

1. **Inventory usage first.** Find every import/reference of the package in
   this repo (`grep`/symbol search). Note which APIs are used — this is the
   checklist the changelog gets audited against. Record current pinned
   version from the manifest/lockfile.
2. **Audit upstream.** Read the release notes/changelog for every version
   between current and target. For each entry, classify: breaking change
   affecting a used API · deprecation we hit · new feature we want ·
   irrelevant. List affected `path:line` usage sites.
3. **Stage the bump.**
   - Patch/minor within compatibility range: bump directly, install, run
     the relevant tests.
   - Major (or breaking): bump to the highest intermediate major first if
     multiple majors spanned, fixing each stage's fallout before the next.
4. **Verify.** Run the project's own test suite plus any integration path
   that touches the dependency. Grep for new deprecation warnings in output.
5. **Record.** In the commit message: old→new versions, breaking changes
   encountered and how each was handled, remaining deprecations with links.

## Rules

- Never widen a version constraint just to make resolution succeed; if the
  resolver conflicts, report the conflict graph and stop.
- Transitive-only bumps still get step 4 verification.
- If the changelog is unavailable (unversioned vendored dep), say so and
  rely on the package's own type stubs/tests plus our suite.

## Failure handling

- Tests fail post-bump → attribute each failure: caused by a documented
  breaking change (cite the changelog line) or pre-existing (re-run on the
  base commit to confirm). Fix forward; never silently pin back.
- Lockfile churn explodes (hundreds of unrelated updates) → use the
  ecosystem's targeted upgrade flag (`npm update <pkg>`,
  `uv lock --upgrade-package <pkg>`, `cargo update -p <pkg>`).
