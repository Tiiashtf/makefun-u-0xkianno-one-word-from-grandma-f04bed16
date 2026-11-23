#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word
a grandma would text about AI.

The word:

    ROBUT

She means "robot". She is texting her grandchild about the
clever machine on the telly, and her finger lands one key off —
the same finger that has typed "ROBUT" into every family group
chat since 2019. It is a typo, and it is also the whole joke:
warm, a little baffled, and instantly understood by everyone
who has ever received a text from their grandma.
"""

import os
import shutil

WORD = "ROBUT"
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_word(text: str) -> None:
    """Fail loudly unless the word meets the competition gate.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to
    30 characters, not only whitespace; the brief requires exactly
    one word. Checking here means a bad word can never be written.
    """
    words = text.split()
    if len(words) != 1:
        raise ValueError(f"entry must be exactly one word, got {len(words)}")
    if not text.isalpha():
        raise ValueError("entry must be letters only, no digits or punctuation")
    if not 1 <= len(text) <= 30:
        raise ValueError(f"entry must be 1-30 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def write_word() -> None:
    """Write the word to /output/entry.txt, deterministically."""
    validate_word(WORD)
    # Create the output directory if it is missing, but never remove
    # the directory itself: the grader may run with a root-owned
    # output directory inside a sticky parent, where removing it
    # fails with EPERM. Clear only its contents instead.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


def main() -> None:
    write_word()


if __name__ == "__main__":
    main()
