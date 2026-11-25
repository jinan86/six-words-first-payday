#!/usr/bin/env python3
"""Six Words to a Payday.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).

The story is a fixed, deterministic constant: no randomness, no network,
no external dependencies. Before writing, the program validates the text
against the competition gate -- UTF-8, 1-60 characters, not only
whitespace, exactly six words -- and fails hard if it does not pass.
The file is written with no trailing newline.
"""

import os
import sys

STORY = "Payday finally came; I stayed anyway."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(text: str) -> None:
    """Fail hard unless the text passes the competition gate."""
    if not text:
        raise SystemExit("invalid entry: empty text")
    if text.strip() == "":
        raise SystemExit("invalid entry: only whitespace")
    if len(text) > 60:
        raise SystemExit(
            f"invalid entry: {len(text)} characters, over the 60 limit"
        )
    words = text.split()
    if len(words) != 6:
        raise SystemExit(
            f"invalid entry: {len(words)} words, expected exactly 6"
        )
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(STORY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    print(f"wrote {len(STORY)} chars, {len(STORY.split())} words to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
