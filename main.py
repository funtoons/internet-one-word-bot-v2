#!/usr/bin/env python3
"""The Internet in One Word -- make.fun entry.

Writes one word describing the whole internet to /output/entry.txt.
Deterministic and offline: Python standard library only, no randomness,
no network, no timestamps. Two runs produce byte-identical output.
"""

import os

WORD = "Cookies"
OUTPUT_PATH = "/output/entry.txt"

# The gate requires UTF-8 text of 1 to 30 characters, not only whitespace,
# and the judge wants a single word. Fail loudly instead of writing junk.
assert WORD and len(WORD) <= 30 and WORD.split() == [WORD]


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
