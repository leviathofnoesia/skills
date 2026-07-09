#!/usr/bin/env python3
"""Render text as a compact monospace PNG a vision model can OCR cheaply.

Usage: prompt2image.py [--out PATH] [--width 1200] [--fontsize 14] [INPUT]
  INPUT    : file path, or "-" / omitted for stdin
  --out    : output PNG path (default: ./prompt.png)
  --width  : max image width in px (default 1200)
  --fontsize: font size in px (default 14)
"""
import argparse
import sys

from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/usr/share/fonts/noto/NotoSansMono-Regular.ttf"
PADDING = 10
LINE_SPACING = 1.5


def load_font(fontsize):
    try:
        return ImageFont.truetype(FONT_PATH, fontsize)
    except (OSError, IOError):
        sys.stderr.write(
            f"Warning: font {FONT_PATH} not found; using default font\n"
        )
        return ImageFont.load_default()


def char_width(font, ch):
    bbox = font.getbbox(ch)
    return bbox[2] - bbox[0]


def wrap_line(line, max_width, font):
    """Wrap a single input line to fit max_width px. Preserves original
    short lines verbatim; only physically-too-long lines are wrapped at a
    space boundary, falling back to a hard break for over-long words."""
    if char_width(font, line) <= max_width:
        return [line]

    width_cache = {}
    def w(s):
        total = 0
        for ch in s:
            if ch not in width_cache:
                width_cache[ch] = char_width(font, ch)
            total += width_cache[ch]
        return total

    words = line.split(" ")
    out = []
    cur = ""
    for word in words:
        candidate = word if not cur else cur + " " + word
        if w(candidate) <= max_width:
            cur = candidate
            continue
        # current word doesn't fit on the running line
        if cur:
            out.append(cur)
            cur = ""
        # word alone fits on a fresh line
        if w(word) <= max_width:
            cur = word
            continue
        # hard-break the over-long word
        piece = ""
        for ch in word:
            if w(piece + ch) <= max_width:
                piece += ch
            else:
                if piece:
                    out.append(piece)
                piece = ch
        cur = piece
    if cur:
        out.append(cur)
    return out


def wrap_text(text, max_width, font):
    lines = []
    for raw in text.split("\n"):
        lines.extend(wrap_line(raw, max_width, font))
    return lines


def build_image(text, width, fontsize):
    font = load_font(fontsize)
    lines = wrap_text(text, width - 2 * PADDING, font)
    line_height = int(fontsize * LINE_SPACING)
    height = len(lines) * line_height + 2 * PADDING

    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    y = PADDING
    for line in lines:
        draw.text((PADDING, y), line, font=font, fill="black")
        y += line_height
    return img


def resolve_input(path):
    """Map harness URIs (local://, artifact://, agent://, etc.) to a real
    filesystem path. Harness tools auto-resolve these, but open() needs a real
    path. Falls back to the path as-is if no mapping applies."""
    if "://" not in path:
        return path
    scheme, _, name = path.partition("://")
    name = name.lstrip("/")
    if scheme == "local":
        # Search harness session local/ dirs for the named file.
        roots = [
            os.path.join(os.path.expanduser("~"), ".omp", "agent", "sessions"),
        ]
        for root in roots:
            if not os.path.isdir(root):
                continue
            for session in sorted(os.listdir(root), reverse=True):
                cand = os.path.join(root, session, "local", name)
                if os.path.isfile(cand):
                    return cand
    # Unknown scheme or not found: return original and let open() report it.
    return path


def main():
    parser = argparse.ArgumentParser(description="Render text as a PNG.")
    parser.add_argument("input", nargs="?", default="-",
                        help="file path, or '-' / omitted for stdin")
    parser.add_argument("--out", default="./prompt.png",
                        help="output PNG path (default: ./prompt.png)")
    parser.add_argument("--width", type=int, default=1200,
                        help="max image width in px (default 1200)")
    parser.add_argument("--fontsize", type=int, default=14,
                        help="font size in px (default 14)")
    args = parser.parse_args()

    if args.input == "-" or args.input == "":
        text = sys.stdin.read()
    else:
        text = open(resolve_input(args.input), "r", encoding="utf-8", errors="replace").read()
    if not text.strip():
        sys.stderr.write("No input\n")
        return 1

    img = build_image(text, args.width, args.fontsize)
    img.save(args.out)
    print(args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
