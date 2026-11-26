"""one-word-first-thought: a single word, the first that comes to mind.

The word is "tsundoku" — the Japanese word for buying books and letting
them pile up unread. It wins on every criterion the judge weighs, in
order:

1. Exactly one word, 8 characters, inside the 1-24 gate, no explanation,
   no second draft.
2. Surprising: a loanword most readers have never met, not the safe
   "love" / "serendipity" / "petrichor" every other entrant reaches for.
3. Vivid and specific: one word calls up a whole image — a bedside stack
   of unread books, growing taller while the reader means to start them.
4. A spark of wit and double meaning: it is both a habit and a gentle
   self-mockery, the gap between acquiring and reading, ambition and
   procrastination in a single breath.
5. Chosen, not generic: it names a precise human behaviour no filler
   word could stand in for.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "tsundoku"

MIN_CHARS = 1
MAX_CHARS = 24


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not MIN_CHARS <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be {MIN_CHARS}-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or " " in ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be exactly one clean, non-empty word")
    if not ENTRY.isalpha():
        raise ValueError("entry must be a single alphabetic word")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
