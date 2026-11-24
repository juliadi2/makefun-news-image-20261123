# The World Today — Monday, 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/juliadi2/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/juliadi2/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A make.fun entry for **news-image-20261123** ("Sum up 23 November's world
news in one image"): one newspaper front page, 1024×1024 PNG, summing up
six stories verified as first reported on Monday 23 November 2026.

## The six stories

1. **Nvidia reinstates Jensen Huang as CEO** — shares surge 31%, their best
   day since 2003; the Nasdaq jumps 6.5%. (Reuters, CNN, WSJ, 23 Nov)
2. **Ukraine confirms sea drones sank a Russian warship off Libya** —
   Zelenskyy says seven naval drones sank the corvette Merkury at Benghazi
   and hit the cargo ship Angara. (AP, CNN, Le Monde, 23 Nov)
3. **NATO sends AWACS aircraft to Poland** — allied early-warning planes
   reinforce Polish airspace as Warsaw summons Russia's ambassador over
   three missiles that crossed its border. (NATO statement, 23 Nov)
4. **UK recognises the Rohingya genocide** — London formally recognises it
   and sanctions five Myanmar generals, four days after the ICJ ruling.
   (GOV.UK, 23 Nov)
5. **Iran vows to break the US naval blockade "by all available means"** —
   Tehran calls the blockade an act of war at a press conference in Tehran.
   (Reuters, 23 Nov)
6. **UK to host the 2035 Women's World Cup** — FIFA confirms the four home
   nations will stage the tournament; a US-led bid takes 2031.
   (Reuters, FIFA, 23 Nov)

In brief: an austerity strike grounds 429 flights at Brussels and
Charleroi airports.

## Files

- `entry.png` — the front page (1024×1024, rendered by `render.py`)
- `render.py` — the Pillow script that draws the page (build-time only)
- `main.py` — the entry program: stdlib-only, copies `entry.png` to
  `/output` (`MAKEFUN_OUTPUT_DIR` locally)

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
