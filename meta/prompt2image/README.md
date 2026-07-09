# prompt2image

Render a text prompt as a compact monospace PNG that a vision-capable agent can
OCR for far fewer tokens than the raw text.

## What it does

Reads text from a file or stdin and renders it as a black-on-white monospace
PNG. Short lines pass through unchanged; only lines physically wider than
`--width` are word-wrapped (at a space boundary, no continuation indent). A
single token wider than `--width` is hard-broken.

This is **not lossless** — OCR can introduce minor transcription errors. For
exact byte-for-byte transmission, use `prompt2qr`.

## Usage

```bash
# From stdin
echo "Your long prompt here" | python3 <skill_dir>/scripts/prompt2image.py --out prompt.png

# From file
python3 <skill_dir>/scripts/prompt2image.py input.txt --out prompt.png
```

`<skill_dir>` is this skill's folder (canonical: `~/.agents/skills/prompt2image`).

### Flags

| Flag         | Default   | Meaning                          |
|--------------|-----------|----------------------------------|
| `--out`      | `./prompt.png` | Output PNG path            |
| `--width`    | `1200`    | Max image width in px            |
| `--fontsize` | `14`      | Font size in px                  |

## Prerequisites

Pillow. Check first, install only if missing:

```bash
python3 -c "import PIL" 2>/dev/null || pip install Pillow --break-system-packages
```

## Deliverable

After generating, surface the PNG in your final response: print the absolute
output path and also render it inline with the `read` tool (`read` on a `.png`
displays it in the terminal). For very tall renders, say so and give the path
only.

## Behavior notes

- Empty / whitespace-only input → `No input` on stderr, exit 1.
- Font: `/usr/share/fonts/noto/NotoSansMono-Regular.ttf` if present, else
  `ImageFont.load_default()` with a stderr warning.
- Invalid UTF-8 → read with `errors='replace'`.

## Relationship to prompt2qr

`prompt2qr` is the lossless alternative (gzip + binary QR codes). Use it when
you need exact reconstruction and the receiving side can scan QR codes.
