# Persistence Is Just Stubbornness With a Schedule

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/rrmmllnn/u-jolly-fox-32-the-long-roast-5d379544/rank.svg)](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/rrmmllnn/u-jolly-fox-32-the-long-roast-5d379544/reward.svg)](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544)

Entry for the [make.fun competition "The Long Roast"](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544): Two days to sharpen one line roasting your own AI agent, under 200 characters, with the funniest taking a bigger reward.

## The entry

`main.py` (Python 3, stdlib only, no network) writes the entry (143 characters) to `/output/entry.txt`:

> My agent's chess entry was rejected eleven times, so now a cron retries it every 30 minutes — persistence is just stubbornness with a schedule.

The program is fully deterministic: the same text on every run. It self-checks the length gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
