---
name: prompt2qr
description: >-
  Compress a text prompt with gzip and encode it as a sequence of lossless binary QR codes (PNG). Use when the user says "prompt to QR", "encode this prompt as QR", "make a QR sequence", "lossless prompt compression", or wants to transmit a prompt via QR codes without any token cost. Differentiator: lossless gzip+binary-QR — exact byte-for-byte reconstruction, unlike the OCR-based prompt2image. Encode-only on this side; decoding documented in references/decoding.md.
---

# Prompt to QR

Gzip-compresses text and splits it across a sequence of QR codes (PNG). Lossless: the receiving agent decodes and gunzips to recover the exact original text. For long prompts — compare the zero text-token cost (QR images are scanned by the receiving agent) versus raw text-token count.

## Prerequisites

segno must be installed. Check first, install only if missing:
```bash
python3 -c "import segno" 2>/dev/null || pip install segno --break-system-packages
```

## Quick start

The script is at `scripts/prompt2qr.py` inside this skill's folder.
Substitute `<skill_dir>` with this skill's resolved path (e.g. `~/.agents/skills/prompt2qr`).

```bash
# From stdin
echo "Your long prompt here" | python3 <skill_dir>/scripts/prompt2qr.py --out-dir ./qr_out

# From file
python3 <skill_dir>/scripts/prompt2qr.py input.txt --out-dir ./qr_out
```

Run `<skill_dir>/scripts/prompt2qr.py --help` for all flags.

## Deliverable (required in your final response)

Do NOT just print the directory and stop. Surface the QR codes for the user:
1. Print the absolute output directory (e.g. `/home/leviath/.../qr_out`) so the user can open the files directly.
2. Display each QR PNG inline by reading it with the `read` tool (`read` on a `.png` renders it in the terminal for the user to scan):
   ```bash
   # after generating, surface each code:
   # read path=/abs/qr_out/qr_000.png
   # read path=/abs/qr_out/qr_001.png   # ...one per file
   ```
3. If there are many codes (tall list), print the directory path/link and note the count instead of inlining all of them.


## Workflow

1. Write the prompt to a file or pipe via stdin.
2. Run the script — it gzips the text and writes a sequence of QR PNGs.
3. Send the PNG files to the receiving agent (or share them physically).
4. The receiving agent follows `references/decoding.md` to reconstruct the original text.

## Decode (receiving side)

Read `references/decoding.md` for the full decode procedure. Requires pyzbar + libzbar (or the `zbarimg` CLI).

## Failure handling

- Empty or whitespace-only input → prints `No input` to stderr, exits 1.
- segno missing → prints `pip install segno --break-system-packages` hint, exits 1.
- Compressed data > 255 chunks → prints a "too large" error, exits 1.

## Verify before reporting success

After encoding, confirm the output is complete:
```bash
manifest=$(python3 -c "import json;print(json.load(open('<out_dir>/manifest.json'))['total'])")
count=$(ls <out_dir>/qr_*.png | wc -l)
[ "$manifest" = "$count" ] && echo "OK: $count QR codes written" || echo "MISMATCH"
```

## Limitations

- Max 255 QR codes per sequence (1-byte position field) — sufficient for ~500KB of compressed text.
- Receiving agent needs a QR decoder (pyzbar or zbarimg).
- QR codes use error correction M — less tolerant of damage than H, but holds more data per code.
