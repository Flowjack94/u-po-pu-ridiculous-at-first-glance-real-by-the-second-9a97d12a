#!/usr/bin/env python3
"""Entry for make.fun competition:
u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a

Writes ONE sentence (1-200 characters) to /output/entry.txt pitching a
bizarre startup idea that sounds ridiculous at first glance but is a real
business: renting professional mourners to families who need a packed
funeral.

Deterministic: stdlib only, no randomness, no time, no network. The output
is byte-identical on every run.
"""

import os
import sys

ENTRY = (
    "We rent professional mourners to families who need a packed funeral, "
    "charging per mourner per hour, because nobody wants to be buried in "
    "front of empty pews."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> None:
    """Enforce the competition gate: one sentence, 1-200 chars, UTF-8,
    not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    # UTF-8 round-trip check.
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(text)}"
        )
    # One sentence: exactly one sentence terminator, at the very end.
    terminators = sum(text.count(c) for c in ".!?")
    if terminators != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> int:
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
