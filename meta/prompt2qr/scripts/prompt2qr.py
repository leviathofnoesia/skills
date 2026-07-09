#!/usr/bin/env python3
"""Gzip-compress text and encode it as a sequence of lossless binary QR codes.

Usage: prompt2qr.py [--out-dir DIR] [INPUT]
  INPUT    : file path, or "-" / omitted for stdin
  --out-dir: output directory for QR PNGs (default: ./qr_out)

Wire format (per QR payload, binary):
  MAGIC   : 3 bytes  b'P2Q'
  VERSION : 1 byte   0x01
  POS     : 1 byte   sequence number (0-indexed)
  TOTAL   : 1 byte   total number of QR codes
  CHUNK   : N bytes  raw gzip-compressed text slice

CHUNK_SIZE is the max per-QR byte capacity at error=M (2331, probed against
segno) minus the 6-byte header. The one-pass build and reassemble are pure and
importable without segno so the framing round-trip can be tested on stdlib alone.
"""
import argparse
import gzip
import json
import os
import sys

MAGIC = b"P2Q"
VERSION = 1
HEADER_SIZE = 6  # 3 magic + 1 version + 1 pos + 1 total
MAX_CHUNK = 2331  # segno byte-mode capacity at error=M, version 40-M (probed)
CHUNK_SIZE = MAX_CHUNK - HEADER_SIZE  # payload bytes per QR code
MAX_FRAMES = 255  # 1-byte pos/total fields


def build_frames(data, chunk_size=CHUNK_SIZE):
    """One-pass: split `data` into framed QR payloads (pure, no segno)."""
    if not data:
        return [MAGIC + bytes([VERSION, 0, 1])]
    total = (len(data) + chunk_size - 1) // chunk_size
    frames = []
    for j in range(total):
        chunk = data[j * chunk_size:(j + 1) * chunk_size]
        frames.append(MAGIC + bytes([VERSION, j, total]) + chunk)
    return frames


def parse_frame(frame):
    """Parse one framed payload into (magic, version, pos, total, chunk)."""
    assert frame[:3] == MAGIC, f"bad magic: {frame[:3]!r}"
    version = frame[3]
    pos = frame[4]
    total = frame[5]
    chunk = frame[6:]
    return MAGIC, version, pos, total, chunk

def reassemble(frames):
    """Sort frames by POS and concatenate chunk data (pure, no segno)."""
    chunks = []
    for f in frames:
        _, version, pos, total, chunk = parse_frame(f)
        assert version == VERSION, f"bad version: {version}"
        chunks.append((pos, chunk))
    chunks.sort(key=lambda c: c[0])
    return b"".join(c[1] for c in chunks)


def resolve_input(path):
    """Map harness URIs (local://, etc.) to a real filesystem path. Harness
    tools auto-resolve these, but open() needs a real path. Falls back to the
    path as-is if no mapping applies."""
    if "://" not in path:
        return path
    scheme, _, name = path.partition("://")
    name = name.lstrip("/")
    if scheme == "local":
        root = os.path.join(os.path.expanduser("~"), ".omp", "agent", "sessions")
        if os.path.isdir(root):
            for session in sorted(os.listdir(root), reverse=True):
                cand = os.path.join(root, session, "local", name)
                if os.path.isfile(cand):
                    return cand
    return path


def main():
    parser = argparse.ArgumentParser(description="Encode text as QR codes.")
    parser.add_argument("input", nargs="?", default="-",
                        help="file path, or '-' / omitted for stdin")
    parser.add_argument("--out-dir", default="./qr_out",
                        help="output directory for QR PNGs (default: ./qr_out)")
    args = parser.parse_args()

    if args.input == "-" or args.input == "":
        text = sys.stdin.read()
    else:
        with open(resolve_input(args.input), "r", encoding="utf-8", errors="replace") as f:
            text = f.read()

    if not text.strip():
        sys.stderr.write("No input\n")
        return 1

    try:
        import segno
    except ImportError:
        sys.stderr.write("segno not installed: pip install segno --break-system-packages\n")
        return 1

    data = gzip.compress(text.encode("utf-8"))
    total = (len(data) + CHUNK_SIZE - 1) // CHUNK_SIZE
    if total > MAX_FRAMES:
        sys.stderr.write(
            f"Compressed data too large for 255 QR codes "
            f"(got {len(data)} bytes compressed). "
            f"Try error='L' or shorten the prompt.\n"
        )
        return 1

    os.makedirs(args.out_dir, exist_ok=True)
    frames = build_frames(data, CHUNK_SIZE)
    for j, frame in enumerate(frames):
        q = segno.make_qr(frame, error="M")  # bytes forces byte mode
        q.save(os.path.join(args.out_dir, f"qr_{j:03d}.png"), scale=10, border=4)

    manifest = {
        "version": 1,
        "total": len(frames),
        "compressed_bytes": len(data),
        "chunk_size": CHUNK_SIZE,
    }
    with open(os.path.join(args.out_dir, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Wrote {len(frames)} QR codes to {args.out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
