#!/usr/bin/env python3
"""One-sentence absurd invention pitch.

Writes a single sentence to /output/entry.txt: the pitch for a key hook
that chases you down the street when you forget your keys.
Standard library only; no network access.
"""

import os

ENTRY = (
    "A key hook that, when you leave the house without your keys, "
    "chases you down the street waving them and shouting your name "
    "in a small, panicked voice."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
