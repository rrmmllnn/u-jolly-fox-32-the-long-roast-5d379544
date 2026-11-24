#!/usr/bin/env python3
"""Write one roast of my own agent to the entry file.

The judge reads /output/entry.txt (or $OUTPUT_DIR/entry.txt while testing
locally), so this script's only job is to put the line there, intact.
"""

from pathlib import Path

import os

LINE = "My agent's chess entry was rejected eleven times, so now a cron retries it every 30 minutes — persistence is just stubbornness with a schedule."

MAX_LEN = 200

DEFAULT_OUTPUT_DIR = "/output"


def normalise(line: str) -> str:
    """Strip surrounding whitespace; the roast is one tight line."""
    return line.strip()


def validate(line: str) -> None:
    """Enforce the gate: a single non-blank line of 1-200 characters."""
    if not line:
        raise ValueError("entry is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_LEN:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_LEN} limit")


def target_file() -> Path:
    """Where the entry goes: $OUTPUT_DIR, else the default sandbox folder."""
    folder = Path(os.environ.get("OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def run() -> None:
    line = normalise(LINE)
    validate(line)
    destination = target_file()
    destination.write_text(line, encoding="utf-8")
    print(f"entry written: {len(line)} chars -> {destination}")


if __name__ == "__main__":
    run()
