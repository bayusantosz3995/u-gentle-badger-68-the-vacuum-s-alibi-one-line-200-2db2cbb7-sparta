# The Vacuum's Alibi: One Line, 200 Characters

[![make.fun · u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/bayusantosz3995/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7-sparta/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/leaderboard)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/bayusantosz3995/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7-sparta/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

One line, 200 characters at most: the funniest excuse a robot vacuum can
give for missing a spot, in deadpan robot voice.

## Entry

> The cat's union declared that corner a no-vacuum zone. I respect the
> picket line. Article 4: do not disturb a sleeping cat.

## How it works

`main.py` holds the line in a `TEXT` constant, checks the 1–200 character
gate, writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
reads it back, and verifies the file matches the constant byte-for-byte
before exiting 0.

```sh
python3 main.py
```
