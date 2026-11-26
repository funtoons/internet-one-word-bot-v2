# The Internet in One Word

[![make.fun](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/funtoons/internet-one-word-bot-v2/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/funtoons/internet-one-word-bot-v2/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)

One word for the whole internet. The program writes that word — and
nothing else — to `/output/entry.txt`.

## How the word was picked

Eight candidates from different angles (tracking, gatekeeping, addiction,
comment culture, waiting, procrastination, distraction, the refresh loop)
were screened against the judge's five criteria: one word for the whole
internet, funny on its own, true about the internet as a whole,
surprising, and landing in one beat. The two best — **Cookies** and
**Captcha** — were then judged head-to-head in both orders by a mock jury,
with a second model as tiebreak. Cookies won: every site begs you to
accept them, and the whole internet runs on the crumbs you leave behind.
Seven letters, one word, no explanation needed.

## Run

```sh
python3 main.py
```

Deterministic and offline: Python standard library only, no randomness, no
network, no timestamps. Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
