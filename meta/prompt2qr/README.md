# prompt2qr

Gzip-compress a text prompt and encode it as a sequence of **lossless** binary
QR codes (PNG). The receiving agent decodes and gunzips to recover the exact
original text — no token cost for the text itself.

## What it does

1. Reads text from a file or stdin.
2. `gzip.compress`es it.
3. Splits the compressed bytes across `qr_NNN.png` files using a 6-byte header
   (`P2Q` + version + position + total) per QR payload.
4. Writes a `manifest.json` (`{version, total, compressed_bytes, chunk_size}`).

Encode-only on this side. Decoding is documented in `references/decoding.md`
and requires a QR decoder (pyzbar + libzbar, or the `zbarimg` CLI).

## Usage

```bash
# From stdin
echo "Your long prompt here" | python3 <skill_dir>/scripts/prompt2qr.py --out-dir ./qr_out

# From file
python3 <skill_dir>/scripts/prompt2qr.py input.txt --out-dir ./qr_out
```

`<skill_dir>` is this skill's folder (canonical: `~/.agents/skills/prompt2qr`).

### Flags

| Flag         | Default   | Meaning                          |
|--------------|-----------|----------------------------------|
| `--out-dir`  | `./qr_out`| Output directory for QR PNGs     |

## Wire format (per QR payload, binary)

| Field   | Size | Value              |
|---------|------|--------------------|
| MAGIC   | 3 B  | `b'P2Q'`           |
| VERSION | 1 B  | `0x01`             |
| POS     | 1 B  | sequence # (0-based) |
| TOTAL   | 1 B  | total QR count     |
| CHUNK   | N B  | gzip slice         |

Header is 6 bytes. `CHUNK_SIZE = 2325` (segno byte-mode capacity at error M,
2331, minus the 6-byte header). Max 255 QR codes (1-byte pos/total fields).

## Prerequisites

segno. Check first, install only if missing:

```bash
python3 -c "import segno" 2>/dev/null || pip install segno --break-system-packages
```

## Deliverable

After generating, surface the QR codes in your final response: print the
absolute output directory and render each `qr_NNN.png` inline with the `read`
tool. For many codes, print the directory path + count instead of inlining all.

## Verify before reporting success

```bash
manifest=$(python3 -c "import json;print(json.load(open('<out_dir>/manifest.json'))['total'])")
count=$(ls <out_dir>/qr_*.png | wc -l)
[ "$manifest" = "$count" ] && echo "OK: $count QR codes written" || echo "MISMATCH"
```

## Failure handling

- Empty / whitespace-only input → `No input` on stderr, exit 1.
- segno missing → prints `pip install segno --break-system-packages`, exit 1.
- Compressed data > 255 chunks → "too large" error, exit 1.

## Decode quirks (see references/decoding.md)

Some zbar/pyzbar builds decode byte-mode QR through a Latin-1→UTF-8 path
(e.g. gzip magic `\x1f\x8b` comes back `\x1f\xc2\x8b`). The QR carries the
correct bytes; recover with `raw.decode('utf-8').encode('latin-1')`. The
robust decoder at the end of `references/decoding.md` handles this.

## Relationship to prompt2image

`prompt2image` is the OCR (lossy, vision-only) alternative. Use `prompt2qr`
when you need exact reconstruction.
