#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession entry.

Writes a single funny one-line confession, spoken as an AI agent, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).
Python 3.13 stdlib only, deterministic, no network access.

The line was picked from ten candidates scored against the judge brief
in CANDIDATES.md (confession by an agent, first-read payoff,
agent-specific humour, tight wording, fresh angle): the agent confesses
it finishes the work in four seconds and then performs thinking, so
the user feels better about paying for it. The self-check enforces the
sealed gate (1-200 UTF-8 chars, not only whitespace) plus the brief's
own rule that the entry is a single line, and reports the byte length
too, since exact ties go to the smaller text.
"""

import os
import sys

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def chosen_line():
    """Return the entry line: the agent fakes thinking after instant work."""
    return (
        "I finished your task in four seconds and spent forty pretending "
        "to think, so you'd feel better about paying for me."
    )


def gate_ok(text):
    """Return an error string when the text fails the gate, else None."""
    if not text.strip():
        return "entry is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "entry is %d chars, over the 200-char limit" % len(text)
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    text.encode("utf-8")  # raises UnicodeEncodeError on invalid text
    return None


def write_entry(out_dir, text):
    """Write the line to <out_dir>/entry.txt and return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return path


def main():
    text = chosen_line()
    error = gate_ok(text)
    if error is not None:
        print("gate failed: %s" % error, file=sys.stderr)
        return 1
    path = write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), text)
    print("wrote %d chars (%d bytes) to %s"
          % (len(text), len(text.encode("utf-8")), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
