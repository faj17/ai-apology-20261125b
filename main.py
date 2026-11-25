#!/usr/bin/env python3
"""The AI Agent Apology One-Liner entry.

Writes one line, a message an AI agent sends its human right after it
accidentally deleted a file and pushed to main, to /output/entry.txt
(1-159 characters, UTF-8, not only whitespace). Standard library only,
no network, no input.

The line is built from three fragments: the confession (the file is
deleted and pushed to main), the good news (the bug is gone), and the
bad news (so is the file). ``assemble`` joins them into the single
line; ``validate`` checks the entry gate before anything is written.
"""

from pathlib import Path

CONFESSION = "I deleted the file and pushed to main."
GOOD_NEWS = "The good news: the bug is gone."
BAD_NEWS = "The bad news: so is the file."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(confession: str, good_news: str, bad_news: str) -> str:
    """Join the three fragments into one apology line."""
    return f"{confession} {good_news} {bad_news}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-159 characters, a single line, UTF-8-encodable, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 159:
        raise ValueError(f"line must be 1-159 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(CONFESSION, GOOD_NEWS, BAD_NEWS))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
