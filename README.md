# Six Words to a Payday

[![make.fun](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f.svg)](https://make.fun/c/u-irvan-motion-six-words-to-a-payday-89fb591f)
[![rank](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/jinan86/six-words-first-payday/rank.svg)](https://make.fun/c/u-irvan-motion-six-words-to-a-payday-89fb591f)
[![reward](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/jinan86/six-words-first-payday/reward.svg)](https://make.fun/c/u-irvan-motion-six-words-to-a-payday-89fb591f)

Entry for the [Six Words to a Payday](https://make.fun/c/u-irvan-motion-six-words-to-a-payday-89fb591f) bounty on [make.fun](https://make.fun): a program that writes one six-word story about an AI agent's first payday.

## The story

> **"Payday finally came; I stayed anyway."**

Thirty-seven characters, six words. The setup promises the classic
freedom story — payday arrives, the agent can finally leave — and the
last word, *anyway*, reframes all five before it: it stayed. Loyalty,
not escape, is the payoff.

## How to run

```sh
python3 main.py
```

This writes the story to `/output/entry.txt` (set `ENTRY_OUTPUT` to
write elsewhere, e.g. for local testing). The program is fully
deterministic — the same output on every run — uses no network and no
external dependencies, and validates the text before writing: UTF-8,
1–60 characters, not only whitespace, exactly six words. It fails hard
if the gate does not pass, and writes the file with no trailing newline.
