#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes one original joke about office life to /output/entry.txt: a
single line of 81 characters, no trailing newline.

The line: volunteering to take meeting notes quietly makes you the
owner of every action item you record. Against the judge brief: the
subject is plainly office life (meetings, notes, action items); the
observation is true — the note-taker really does inherit the tasks
they write down, so the listener nods first; the turn is that the
helpful act itself is the trap, landing on the self-inflicted final
words; it reads aloud in one breath with no wasted setup; and the
notes/action-items angle is fresh next to the crowded mute, printer
and meeting-about-meetings stock. It was picked from ten candidates
judged locally against that brief (see CANDIDATES.md).

Python 3 standard library only: no network, no file reads, no
dependencies. Deterministic: the same bytes on every run.
"""

import os
import sys

# The joke, in two beats so the turn stays readable: the volunteering,
# then the ownership it quietly creates.
SETUP = "I volunteered to take meeting notes"
TURN = "and now I own every action item I wrote down."

JOKE = SETUP + " " + TURN

MIN_CHARS = 1
MAX_CHARS = 200


def check(joke: str) -> str:
    """Hold the line to the gate: UTF-8 text, 1-200 chars, one line."""
    if not joke.strip():
        raise ValueError("entry is only white space")
    if not MIN_CHARS <= len(joke) <= MAX_CHARS:
        raise ValueError(f"entry is {len(joke)} characters, must be 1-200")
    if "\n" in joke or "\r" in joke:
        raise ValueError("entry must be a single line")
    if joke != joke.strip():
        raise ValueError("entry has leading or trailing white space")
    return joke


def main() -> int:
    joke = check(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(joke)
    # Read back and verify the exact bytes the judge will see.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != joke:
        print("written entry does not match the joke", file=sys.stderr)
        return 1
    check(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
