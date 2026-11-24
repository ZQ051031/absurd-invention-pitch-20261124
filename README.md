# One-Sentence Absurd Invention Pitch

Entry for the make.fun competition
`u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a` ($2.50, deadline
2026-11-27 00:15 CST).

[![make.fun](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![Rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/ZQ051031/absurd-invention-pitch-20261124/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![Reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/ZQ051031/absurd-invention-pitch-20261124/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

## The entry

The program writes one sentence to `/output/entry.txt`:

> A key hook that, when you leave the house without your keys, chases you
> down the street waving them and shouting your name in a small, panicked
> voice.

One sentence, well under the 220-character gate: the tiny everyday
annoyance (leaving the house without your keys), the ridiculous invention
(a wall hook that detaches and runs after you), and its silly mechanism
(waving the keys, shouting your name in a panicked voice).

## Why this pitch

Candidates weighed against the judge's brief (funny from the invention
itself, a clever fix that is silly yet weirdly plausible, original, tight):

- **Toothpaste butler** — a tube with a tiny butler dispensing exactly one
  pea-sized squeeze, then judging you silently for wanting more. Fresh, but
  drier wit, and squeezing toothpaste is a smaller annoyance than losing
  your keys.
- **Smoke alarm that replaces its own battery** — whispers a lullaby at
  3 a.m. instead of beeping and leaves a note saying it has handled it.
  Charming, but three mechanisms in one sentence is clutter.
- **Remote control that fires a flare from inside the sofa** and texts you
  its coordinates. The tightest sentence, but find-my-remote gadgets
  already exist, so it is less original, and reporting a loss is a weaker
  fix than preventing one.
- **Shower head that holds the hot water hostage during a flush** — the
  mechanism is muddled (holding hot water back would make the shower
  colder, not fix the shock).
- **Charger cable that retracts like a startled snake** — retraction after
  you trip does not prevent the trip.

First pick was the key hook: the biggest visual gag (a hook sprinting down
the street after you), a complete fix (you never actually leave without
your keys), and a silly-yet-plausible mechanism (a little robot hook).

## Revision pass

Reconsidered the remote-control flare as the main rival — it is the
tightest sentence — but kept the key hook: the gag lands harder on first
read, the annoyance is more universal, and the fix is a prevention rather
than a report. One wording polish from the revision: dropped the comma
after "street" so the chase reads in one breath, per the tightness
criterion.

## How it works

`main.py` (Python standard library only) writes the sentence to
`/output/entry.txt` in binary mode, so the output is byte-exact on any
platform. No network access, no third-party packages.

Run it twice and the two outputs are byte-identical.

## License

MIT — see `LICENSE`.
