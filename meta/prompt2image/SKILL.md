---
name: prompt2image
description: >-
  Render a text prompt as a compact monospace PNG image that a vision-capable agent can read for far fewer tokens than the raw text. Use when the user says "prompt to image", "turn this prompt into an image", "make this prompt token-cheap", "compress this prompt visually", or wants to send a long prompt to a vision model without paying full text-token cost. Differentiator: lossless visual encoding via OCR-readable monospace render — no QR decoder needed on the receiving side.
---

# Prompt to Image

Renders text as a PNG a vision model can OCR for token savings. For long prompts — compare your provider's image-tile cost to the raw text-token count to decide if it's worth it.

## Prerequisites

Pillow must be installed. Check first, install only if missing:
```bash
python3 -c "import PIL" 2>/dev/null || pip install Pillow --break-system-packages
```

## Quick start

The script is at `scripts/prompt2image.py` inside this skill's folder.
Substitute `<skill_dir>` with this skill's resolved path (e.g. `~/.agents/skills/prompt2image`).

```bash
# From stdin
echo "Your long prompt here" | python3 <skill_dir>/scripts/prompt2image.py --out prompt.png

# From file
python3 <skill_dir>/scripts/prompt2image.py input.txt --out prompt.png
```

Run `<skill_dir>/scripts/prompt2image.py --help` for all flags (`--width`, `--fontsize`).

## Deliverable (required in your final response)

Do NOT just print the path and stop. Surface the image for the user:
1. Print the absolute output path (e.g. `/home/leviath/.../prompt.png`) so the user can open it directly.
2. Display it inline by reading the file with the `read` tool (`read` on a `.png` renders it in the terminal for the user to see):
   ```bash
   # after generating, surface it:
   # read path=/abs/prompt.png
   ```
3. If the render is too large to be useful inline (very tall image), say so and fall back to the path/link only.


## Workflow

1. Write the prompt to a file or pipe via stdin.
2. Run the script; it renders the text as a monospace PNG.
3. Attach or send the resulting PNG to a vision-capable agent.
4. The vision model reads the image — token cost depends on image dimensions per your provider's image-token formula, not character count.

## Failure handling

- Empty or whitespace-only input → prints `No input` to stderr, exits 1.
- Pillow missing → `ImportError`; run the prerequisite check above.
- A single token wider than `--width` (no spaces to break on) is hard-broken; acceptable.

## Limitations

- OCR accuracy depends on the receiving model's vision capability.
- Very long prompts produce very tall images — some providers cap image dimensions.
- Not lossless: OCR can introduce minor transcription errors. For exact transmission, use `prompt2qr` instead.
