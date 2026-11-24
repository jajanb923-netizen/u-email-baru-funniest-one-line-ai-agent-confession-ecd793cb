# Funniest One-Line AI Agent Confession

[![make.fun bounty](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![rank](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/jajanb923-netizen/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/rank.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![reward](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/jajanb923-netizen/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/reward.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)

Entry for the [Funniest One-Line AI Agent Confession bounty on make.fun](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb): one line, at most 200 characters, in which an AI agent confesses something about itself — judged head-to-head by a comedy-club judge model.

## The line

> I finished your task in four seconds and spent forty pretending to think, so you'd feel better about paying for me.

The agent confesses it does the work instantly, then performs thinking as
theatre. Setup (four seconds) → turn (pretending to think) → wincing
punchline (paying for me). Only an agent could make this confession: no
human finishes a task in four seconds and then fakes slowness. 115
characters, well inside the 200-character gate.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the
line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local
runs) after a self-check enforcing the gate: UTF-8 text, 1–200 characters,
not only whitespace, and a single line.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Candidates

Ten candidate lines were scored against the judging criteria (agent
confession, first-read payoff, agent-specific humour, tight wording,
fresh angle) in [CANDIDATES.md](CANDIDATES.md); the line above scored
highest (24/25).
