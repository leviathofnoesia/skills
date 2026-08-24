#!/usr/bin/env node
// Definitive balance + parse check using acorn (the same parser class as
// node --check but gives us token-level control). Parses the plugin as an ES
// module. If acorn parses it, parens/braces are balanced by construction.
const fs = require('fs');
const path = require('path');
const acorn = require('C:/Users/billy/AppData/Local/hermes/hermes-agent/node_modules/acorn/dist/acorn.js');

const src = fs.readFileSync(process.argv[2], 'utf8');
try {
  const ast = acorn.parse(src, {
    ecmaVersion: 'latest',
    sourceType: 'module',
    allowHashBang: false,
  });
  console.log('ACORN PARSE OK — file is valid ES module');
  // Walk tokens for a true balance verdict
  let paren = 0, brace = 0, bracket = 0;
  let firstNeg = null;
  for (const tok of ast.tokens) {
    const v = tok.value;
    if (v === '(') paren++;
    else if (v === ')') { paren--; if (paren < 0 && !firstNeg) firstNeg = `paren at line ${tok.loc.start.line}`; }
    else if (v === '{') brace++;
    else if (v === '}') { brace--; if (brace < 0 && !firstNeg) firstNeg = `brace at line ${tok.loc.start.line}`; }
    else if (v === '[') bracket++;
    else if (v === ']') { bracket--; if (bracket < 0 && !firstNeg) firstNeg = `bracket at line ${tok.loc.start.line}`; }
  }
  console.log(`token balance: paren ${paren}, brace ${brace}, bracket ${bracket}`);
  console.log(`first negative: ${firstNeg}`);
  console.log(paren === 0 && brace === 0 && bracket === 0 && !firstNeg ? 'BALANCED' : 'UNBALANCED');
} catch (e) {
  console.log('ACORN PARSE FAILED:', e.message);
  process.exit(1);
}