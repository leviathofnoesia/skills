#!/usr/bin/env node
// String/comment/template-aware balance checker. Handles `` ${...} `` template
// interpolation by descending into code mode, so nested quotes inside
// interpolations don't break the scan. node --check is the authoritative gate;
// this is a diagnostic to attribute any naive-count delta.
const fs = require('fs');
const src = fs.readFileSync(process.argv[2], 'utf8');
const n = src.length;
let i = 0, line = 1;
const stack = []; // {ch, line}
let parenDepth = 0, braceDepth = 0;
let firstNeg = null;

function skipStr(q) {
  i++;
  while (i < n) {
    const c = src[i];
    if (c === '\\') { i += 2; continue; }
    if (c === '\n') line++;
    if (c === q) { i++; return; }
    i++;
  }
}
function skipLine() {
  while (i < n && src[i] !== '\n') i++;
}
function skipBlock() {
  i += 2;
  while (i < n) {
    if (src[i] === '\n') line++;
    if (src[i] === '*' && src[i + 1] === '/') { i += 2; return; }
    i++;
  }
}
// Template literal: iterates chars; `$` followed by `{` descends into code
// mode (template expression) and returns when the matched `}` is consumed.
function scanTemplate() {
  i++; // opening backtick
  while (i < n) {
    const c = src[i];
    if (c === '\\') { i += 2; continue; }
    if (c === '\n') line++;
    if (c === '`') { i++; return; }
    if (c === '$' && src[i + 1] === '{') {
      i += 2;
      // template expression: scan code until matching }
      const exprStack = ['{'];
      while (i < n) {
        const e = src[i];
        if (e === '\n') line++;
        if (e === '\\' ) { i += 2; continue; }
        if (e === "'" || e === '"') { skipStr(e); continue; }
        if (e === '`') { scanTemplate(); continue; }
        if (e === '/' && src[i+1] === '/') { skipLine(); continue; }
        if (e === '/' && src[i+1] === '*') { skipBlock(); continue; }
        if (e === '{') { exprStack.push('{'); i++; continue; }
        if (e === '}') {
          exprStack.pop();
          i++;
          if (exprStack.length === 0) break;
          continue;
        }
        if (e === '(') { parenDepth++; stack.push({ ch: '(', line }); i++; continue; }
        if (e === ')') { parenDepth--; if (stack.pop()?.ch !== ')') {} if (parenDepth < 0 && !firstNeg) firstNeg = `paren @ ${line}`; i++; continue; }
        i++;
      }
      continue;
    }
    i++;
  }
}

while (i < n) {
  const c = src[i];
  if (c === '\n') { line++; i++; continue; }
  if (c === '/' && src[i+1] === '/') { skipLine(); continue; }
  if (c === '/' && src[i+1] === '*') { skipBlock(); continue; }
  if (c === "'" || c === '"') { skipStr(c); continue; }
  if (c === '`') { scanTemplate(); continue; }
  if (c === '(') { parenDepth++; stack.push({ ch: '(', line }); i++; continue; }
  if (c === ')') { parenDepth--; stack.pop(); if (parenDepth < 0 && !firstNeg) firstNeg = `paren @ line ${line}`; i++; continue; }
  if (c === '{') { braceDepth++; stack.push({ ch: '{', line }); i++; continue; }
  if (c === '}') { braceDepth--; stack.pop(); if (braceDepth < 0 && !firstNeg) firstNeg = `brace @ line ${line}`; i++; continue; }
  i++;
}

console.log(`paren depth: ${parenDepth}`);
console.log(`brace depth: ${braceDepth}`);
console.log(`first negative: ${firstNeg}`);
console.log(`stack leftover: ${stack.length}`);
if (stack.length) console.log('leftover sample:', stack.slice(-3));
console.log(parenDepth === 0 && braceDepth === 0 && !firstNeg && stack.length === 0 ? 'BALANCED (template-aware)' : 'UNBALANCED');