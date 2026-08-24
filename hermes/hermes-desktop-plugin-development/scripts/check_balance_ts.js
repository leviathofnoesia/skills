#!/usr/bin/env node
// Cross-verify parse validity with the TypeScript compiler (real second
// parser, independent of V8's --check). Also reports token-level paren/brace
// balance from the TS scanner.
const ts = require('C:/Users/billy/AppData/Local/hermes/hermes-agent/node_modules/typescript');
const fs = require('fs');
const src = fs.readFileSync(process.argv[2], 'utf8');

const sf = ts.createSourceFile('plugin.js', src, ts.ScriptTarget.Latest, true, ts.ScriptKind.JS);
const diags = ts.getPreEmitDiagnostics ? [] : [];
function collect(node, out) {
  const d = ts.getDiagnostics ? [] : [];
  ts.forEachChild(node, (c) => collect(c, out));
  if (node.kind === ts.SyntaxKind.ParseError) out.push('ParseError node at ' + node.pos);
}
const errors = [];
ts.forEachChild(sf, (c) => collect(c, errors));

// parse diagnostics (TS 5+ style):
const parseDiags = (sf.parseDiagnostics || []).map(d => d.messageText);
console.log('TS parse diagnostics:', parseDiags.length ? parseDiags.slice(0, 5) : 'none');

const scanner = ts.createScanner(ts.ScriptTarget.Latest, true, ts.LanguageVariant.Standard, src);
let paren = 0, brace = 0, bracket = 0, firstNeg = null;
let tok = scanner.scan();
let lineNum = 1;
while (tok !== ts.SyntaxKind.EndOfFileToken) {
  const t = scanner.getToken();
  if (t === ts.SyntaxKind.OpenParenToken) paren++;
  else if (t === ts.SyntaxKind.CloseParenToken) { paren--; if (paren < 0 && !firstNeg) firstNeg = `paren at ${scanner.getLine()}`; }
  else if (t === ts.SyntaxKind.OpenBraceToken) brace++;
  else if (t === ts.SyntaxKind.CloseBraceToken) { brace--; }
  else if (t === ts.SyntaxKind.OpenBracketToken) bracket++;
  else if (t === ts.SyntaxKind.CloseBracketToken) { bracket--; }
  tok = scanner.scan();
}
console.log(`TS scanner balance: paren ${paren}, brace ${brace}, bracket ${bracket}, firstNeg ${firstNeg}`);
console.log(paren === 0 && brace === 0 && bracket === 0 && !firstNeg ? 'BALANCED' : 'UNBALANCED');
console.log('result:', parseDiags.length === 0 && paren === 0 && brace === 0 && bracket === 0 && !firstNeg ? 'OK' : 'CHECK FAILED');