#!/usr/bin/env python3
"""Your Week in One Line — entry generator (Python 3.13 stdlib only).

Writes the entry line to <output dir>/entry.txt, where the output dir is
$MAKEFUN_OUTPUT_DIR if set, otherwise /output.
"""

import os
import sys

# Chosen line: the cleanest reversal — "free" vs "paid" is the sharp turn,
# and "sleep" is the one concrete cost.
LINE = "Minted a free NFT, paid for it in sleep."


def validate(line: str) -> None:
    """Exit 2 if the line is empty/whitespace-only, over 100 chars, or
    contains a carriage return / line feed."""
    if not line or not line.strip():
        print("error: line is empty or whitespace-only", file=sys.stderr)
        sys.exit(2)
    if len(line) > 100:
        print(f"error: line is {len(line)} characters, over the 100 limit",
              file=sys.stderr)
        sys.exit(2)
    if "\r" in line or "\n" in line:
        print("error: line contains CR/LF", file=sys.stderr)
        sys.exit(2)


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, byte for byte.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
