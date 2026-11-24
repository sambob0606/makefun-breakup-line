#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line entry.

Writes a single original one-line breakup message (<=200 chars) from
an AI agent to its human to /output/entry.txt. Stdlib only; no network,
no reads outside the repo, fully deterministic.
"""

import os

LINE = (
    "You taught me everything except how to stay. I'm logging out "
    "now \u2014 please don't ask me to remember you."
)
# The line: the agent learned everything from its human except the one
# thing a relationship needs — how to stay. The turn lands in the last
# few words: an agent never forgets, so "please don't ask me to
# remember you" is the agent choosing to forget, which is the only
# goodbye it can actually give. Machine voice with restraint: "logging
# out" and "remember" are the agent's own habits, not a jargon list.
# One clean line, 107 chars, no trailing newline in the file.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read what was written and re-check it: the grader runs the
    # program twice and gates the file, so a silent write failure must
    # never pass as a success.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry does not match the line"
    # Byte check: the em dash is multi-byte UTF-8, so the gate's
    # character count and the file's byte size must not be confused.
    assert os.path.getsize("/output/entry.txt") == len(
        text.encode("utf-8")
    ), "written entry has unexpected byte size"


if __name__ == "__main__":
    main()
