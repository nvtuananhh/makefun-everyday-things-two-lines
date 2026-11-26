#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation to /output/entry.txt.
"""

import os

ENTRY = """Rain is the sky wringing out a giant sponge it left soaking all morning.
The sponge part is right, because a cloud really does hold water the way a sponge does, but it leaves out the part where nothing squeezes it; the cloud just gets too heavy and lets go."""

# One metaphor only: the sky wrings a giant sponge. Line 2 names both
# what the sponge maps (a cloud holding water) and what it leaves out
# (nothing squeezes it; the cloud just gets too heavy and lets go).
# The sponge is a thing a 10-year-old can hold; the sky is a thing
# they can see. Joined, the picture is new, and the second line keeps
# it honest instead of letting the picture mislead.

assert 1 <= len(ENTRY) <= 400 and ENTRY.count("\n") == 1 and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
