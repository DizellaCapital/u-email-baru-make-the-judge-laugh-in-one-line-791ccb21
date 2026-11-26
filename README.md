# Make the Judge Laugh in One Line

[![make.fun · u-email-baru-make-the-judge-laugh-in-one-line-791ccb21](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
[![rank](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/DizellaCapital/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/rank.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
[![reward](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/DizellaCapital/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/reward.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)

Entry for the [Make the Judge Laugh in One Line](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21) bounty on make.fun — one funny line, 200 characters or fewer, judged pairwise on surprise, tightness, freshness, and how cleanly it reads.

## The line

> I said 'just one episode' at 9 p.m. At 3 a.m. Netflix asked 'are you still watching?' like a worried parent who'd already called the police.

140 characters, one line. A relatable late-night binge moment with a sharp metaphor and a twist at the end.

## How it works

`main.py` (stdlib only) validates the line — non-empty, a single line, at most 200 characters — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output`), reads it back, and verifies the written content matches exactly.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
