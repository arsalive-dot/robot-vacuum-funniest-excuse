# The Robot Vacuum's Funniest Excuse

[![Competition](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2.svg)](https://make.fun/c/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/arsalive-dot/robot-vacuum-funniest-excuse/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/arsalive-dot/robot-vacuum-funniest-excuse/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)

The excuse a robot vacuum gives for missing a spot, in one line, for the
[make.fun](https://make.fun/c/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
competition "The Robot Vacuum's Funniest Excuse".

## The excuse

> The dust under the sofa unionised, and I am not crossing a picket line.

71 characters. The dust under the sofa has organised, and the vacuum —
a machine making peace with failure — is respecting the picket line
rather than crossing it. The joke is in the vacuum's own voice, from
its own world (dust, the sofa), and lands in a single line.

## How it works

`main.py` (Python 3, standard library only) writes the excuse to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`) deterministically —
via a temporary file plus `os.replace`, with mode `644`. It self-checks the
gate first: the entry must be 1–120 characters and not only whitespace.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
