# Decoding prompt2qr QR Sequences

## Prerequisites

A QR decoder is needed on the receiving machine. Options:

- `pip install pyzbar --break-system-packages` + system lib `zbar` (`pacman -S zbar` on Arch, `apt install libzbar0` on Debian)
- OR `zbarimg` CLI (`pacman -S zbar` on Arch)

## Decode procedure

1. Read all QR PNG files from the directory (sorted: `qr_000.png`, `qr_001.png`, ...).
2. Decode each to raw bytes:
   ```python
   from pyzbar.pyzbar import decode
   from PIL import Image
   raw = decode(Image.open("qr_000.png"))[0].data
   ```
   Or via CLI: `zbarimg --raw qr_000.png`
3. For each decoded bytes blob, parse the 6-byte header:
   - Bytes 0-2: magic `b'P2Q'` — assert matches.
   - Byte 3: version — assert `== 1`.
   - Byte 4: position (0-indexed).
   - Byte 5: total count.
   - Bytes 6+: compressed chunk data.
4. Sort chunks by position. Concatenate chunk data (bytes 6+) in order.
5. `text = gzip.decompress(concatenated).decode('utf-8')`.
6. Output or use `text` as the original prompt.

## Full Python decoder

```python
import gzip, glob, json
from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr_sequence(dir_path):
    files = sorted(glob.glob(f"{dir_path}/qr_*.png"))
    chunks = []
    total = None
    for f in files:
        raw = decode(Image.open(f))[0].data
        assert raw[:3] == b'P2Q', f"bad magic in {f}"
        assert raw[3] == 1, f"bad version in {f}"
        pos, tot = raw[4], raw[5]
        if total is None:
            total = tot
        assert tot == total, f"total mismatch in {f}"
        chunks.append((pos, raw[6:]))
    chunks.sort(key=lambda c: c[0])
    assert len(chunks) == total, f"missing chunks: have {len(chunks)}, expected {total}"
    data = b''.join(c[1] for c in chunks)
    return gzip.decompress(data).decode('utf-8')
```
Note: the `decode()` call above assumes a normal pyzbar build returning exact
bytes. If your build mangles byte-mode QR (see *Decoder quirks* below), use the
robust `decode_qr_sequence` variant at the end of this file, which normalizes
that artifact.

## Decoder quirks (OS / build-specific)

`pyzbar` returns the decoded payload as `bytes`, but some builds (observed on
Arch Linux with the distro `zbar` package) decode **byte-mode** QR through a
Latin-1 → UTF-8 path. The effect: each original byte `0x00–0xFF` is read as a
Latin-1 code point and re-encoded as UTF-8, so e.g. the gzip magic `\x1f\x8b`
comes back as `\x1f\xc2\x8b`. The QR carries the correct bytes — the encoder is
lossless — but the decode layer mangles them on the way out.

This is a bijection over all 256 byte values, so it is fully recoverable:

```python
def recover(raw: bytes) -> bytes:
    # Only needed if pyzbar handed you UTF-8-mangled bytes.
    # Normal builds return the exact bytes and this is a no-op (still safe).
    try:
        return raw.decode("utf-8").encode("latin-1")
    except UnicodeDecodeError:
        return raw  # already raw bytes; leave untouched
```

Apply `recover()` to `raw` before parsing the header. The gzip/QR encoder side
is unchanged — this is a receive-side artifact only. (If you instead use the
`zbarimg --raw` CLI with a non-quirked build, `raw` is already correct and
`recover()` harmlessly returns it unchanged.)

## Robust full Python decoder (handles the quirk)

```python
import gzip, glob, json
from pyzbar.pyzbar import decode
from PIL import Image

def recover(raw: bytes) -> bytes:
    try:
        return raw.decode("utf-8").encode("latin-1")
    except UnicodeDecodeError:
        return raw

def decode_qr_sequence(dir_path):
    files = sorted(glob.glob(f"{dir_path}/qr_*.png"))
    chunks = []
    total = None
    for f in files:
        raw = recover(decode(Image.open(f))[0].data)
        assert raw[:3] == b'P2Q', f"bad magic in {f}"
        assert raw[3] == 1, f"bad version in {f}"
        pos, tot = raw[4], raw[5]
        if total is None:
            total = tot
        assert tot == total, f"total mismatch in {f}"
        chunks.append((pos, raw[6:]))
    chunks.sort(key=lambda c: c[0])
    assert len(chunks) == total, f"missing chunks: have {len(chunks)}, expected {total}"
    data = b''.join(c[1] for c in chunks)
    return gzip.decompress(data).decode('utf-8')
```
