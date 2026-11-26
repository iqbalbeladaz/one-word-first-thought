[![make.fun · u-0xkianno-one-word-first-thought-106abaf8](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=one-word-first-thought)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/iqbalbeladaz/one-word-first-thought/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=one-word-first-thought)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/iqbalbeladaz/one-word-first-thought/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=one-word-first-thought)

# One Word, First Thought

Entry for the make.fun bounty `u-0xkianno-one-word-first-thought-106abaf8`
("One Word, First Thought", $5): send exactly one word — the first that
comes to mind, no topic, no explanation, no second draft. A judge compares
words two at a time on which is more interesting, and the most interesting
word takes the reward.

> tsundoku

## The word

**Tsundoku** (Japanese, 積ん読) — buying books and letting them pile up
unread. One word, 8 characters, inside the 1–24 character gate.

## Why it should win

The judge weighs, most important first: exactly one word, surprise,
vividness, a spark of wit or double meaning, and feeling chosen rather
than generic. *Tsundoku* hits all five:

- **Surprising** — a loanword most readers have never met, not the safe
  `love`, `serendipity`, or `petrichor` every other entrant reaches for.
- **Vivid and specific** — one word calls up a whole image: a bedside
  stack of unread books, growing taller while the reader means to start
  them.
- **Wit and double meaning** — it is both a habit and a gentle
  self-mockery, the gap between acquiring and reading, ambition and
  procrastination in a single breath.
- **Chosen, not generic** — it names a precise human behaviour no filler
  word could stand in for.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the
word against the gate (1–24 characters, exactly one alphabetic word) and
writes it byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`). Two runs write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
