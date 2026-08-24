#!/usr/bin/env node
/**
 * scan-tailwind-classes.js — inventory of Tailwind utilities that ACTUALLY
 * render in the Hermes desktop app, plus a ground-truth class-existence check.
 *
 * WHY: Tailwind v4 compiles utilities at build time. Runtime desktop plugins
 * (plugin.js loaded as a Blob) are never scanned by Tailwind, so a class only
 * renders if it already exists in the host's compiled stylesheet. Classes like
 * `grid-cols-7`, `bg-(--ui-bg-primary)`, `ring-(--ui-accent)` silently do
 * nothing — no error, no warning. Scan first, then write markup only with
 * classes that exist.
 *
 * USAGE:
 *   node scan-tailwind-classes.js <path-to-index-*.css>            # all classes
 *   node scan-tailwind-classes.js <path> | grep -E "grid-cols|bg-" # filter
 *   node scan-tailwind-classes.js <path> --has "hover:bg-(--ui-bg-tertiary)"
 *         # -> LIVE / DEAD (ground-truth check; exit 0/1)
 *   node scan-tailwind-classes.js <path> --has-many "a" "b c" ...
 *         # -> one line per class token (LIVE/DEAD); exit 1 if any DEAD
 *
 * Typical path on Windows:
 *   C:/Users/<user>/AppData/Local/hermes/hermes-agent/apps/desktop/dist/assets/index-*.css
 * (the packaged build also ships one under release/win-unpacked/...).
 *
 * OUTPUT: one line per distinct class selector with its occurrence count,
 * sorted alphabetically, then the --ui-* token utilities separately, then a
 * TOTAL UNIQUE count. Check a class's existence with grep.
 *
 * WHY THE REGEX MATTERS: Tailwind v4 escapes special chars in selectors —
 * `:` -> `\:`, `.` -> `\.`, `(` -> `\(`, `[` -> `\[`, `/` -> `\/`. A regex
 * whose char class omits backslash-paren pairs (the classic
 * /\.([a-zA-Z0-9:_\[\]\/\.-]+)/ pattern) silently MISSES every arbitrary-value
 * utility like .bg-\(--ui-green\) and falsely reports the whole --ui-* family
 * as dead. The scanner below includes the escaped-paren forms explicitly, and
 * --has does the ground-truth substring check: css.includes('.' + escaped).
 */
const fs = require('fs');

const cssPath = process.argv[2];
if (!cssPath) {
  console.error('Usage: node scan-tailwind-classes.js <path-to-index-*.css> [--has "class" | --has-many ...]');
  process.exit(1);
}

let css;
try {
  css = fs.readFileSync(cssPath, 'utf8');
} catch (err) {
  console.error(`Cannot read ${cssPath}: ${err.message}`);
  process.exit(1);
}

// Escape a class token the way Tailwind v4 writes it into a selector.
function escapeCssClass(token) {
  return token.replace(/[:\.[\]()#,>+~%]/g, ch => '\\' + ch);
}
function isLive(token) {
  return css.includes('.' + escapeCssClass(token));
}

// Ground-truth existence check mode.
const mode = process.argv[3];
if (mode === '--has') {
  const token = process.argv[4];
  console.log(isLive(token) ? `LIVE ${token}` : `DEAD ${token}`);
  process.exit(isLive(token) ? 0 : 1);
}
if (mode === '--has-many') {
  const tokens = process.argv.slice(4).flatMap(s => s.split(/\s+/)).filter(Boolean);
  let anyDead = false;
  for (const t of tokens) {
    const ok = isLive(t);
    if (!ok) anyDead = true;
    console.log((ok ? 'LIVE ' : 'DEAD ') + t);
  }
  process.exit(anyDead ? 1 : 0);
}

// All class selectors, INCLUDING escaped parens (arbitrary values):
// .foo, .hover\:x, .bg-\(--ui-green\), .w-\[90\%\]
const re = /\.((?:[a-zA-Z0-9:_\[\]\/\.\\-]|\\\(|\\\)|\\%|\\,|\\#|\\:)+)/g;
const counts = new Map();
let m;
while ((m = re.exec(css))) {
  const key = m[1];
  if (key.length > 60) continue;
  counts.set(key, (counts.get(key) || 0) + 1);
}
const sorted = [...counts.entries()].sort((a, b) => a[0].localeCompare(b[0]));
console.log('=== ALL CLASS SELECTORS (count, class) ===');
for (const [k, v] of sorted) console.log(String(v).padStart(3), k);
console.log('TOTAL UNIQUE:', sorted.length);

// --ui-* token utilities specifically (bg-\(--ui-green\) / text-\(--ui-text-secondary\) ...)
const reTokens = /\.((?:[a-zA-Z:[\]\/.-]+?)-\\\(--ui-[a-z-]+\\\))/g;
const tokenCounts = new Map();
while ((m = reTokens.exec(css))) {
  const key = m[1];
  tokenCounts.set(key, (tokenCounts.get(key) || 0) + 1);
}
console.log('\n=== --ui-* TOKEN UTILITIES ===');
for (const [k, v] of [...tokenCounts.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
  console.log(String(v).padStart(3), k);
}
