#!/usr/bin/env python3
"""Six Words to a Payday — a six-word story about a first payday.

This program writes one fixed six-word story to /output/entry.txt,
or to $ENTRY_OUTPUT when that variable is set (handy for local runs).

Everything here is deterministic: the story never changes, there is
no randomness, no network access, and no third-party dependency.
Before anything is written, the text is checked against the
competition gate — valid UTF-8, between 1 and 60 characters, more
than just whitespace, and exactly six words — and the program exits
with an error instead of writing a bad entry. The output file gets
no trailing newline.
"""

import os
import sys

STORY = "Payday finally came; I stayed anyway."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(text: str) -> None:
    """Exit with an error unless *text* passes the competition gate."""
    if not text:
        raise SystemExit("invalid entry: text is empty")
    if not text.strip():
        raise SystemExit("invalid entry: text is only whitespace")
    if len(text) > 60:
        raise SystemExit(
            "invalid entry: %d characters, limit is 60" % len(text)
        )
    text.encode("utf-8")  # raises UnicodeEncodeError on bad UTF-8
    words = text.split()
    if len(words) != 6:
        raise SystemExit(
            "invalid entry: %d words, expected exactly 6" % len(words)
        )


def main() -> None:
    """Validate the story, then write it to the output path."""
    validate(STORY)
    folder = os.path.dirname(OUTPUT_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(STORY)
    word_count = len(STORY.split())
    print(
        "wrote %d chars, %d words to %s" % (len(STORY), word_count, OUTPUT_PATH)
    )


if __name__ == "__main__":
    main()
