# Preset first-PR evidence command

`oss-launchpad init` prints a preset-specific **First-PR evidence command** so maintainers can open the two files most likely to anchor the first believable review.

## Why this matters

The first public pull request usually stalls when the repo has code or docs, but not both in the same reviewable slice. The printed command fixes that by surfacing a proof pair immediately.

## Current command pairs

- `ai-agent` → `docs/agent-demo-brief.md` + `evals/README.md`
- `web-app` → `docs/landing-page-brief.md` + `docs/information-architecture.md`
- `python-lib` → `examples/basic_usage.py` + `docs/api-surface.md`

## Maintainer rule

Use the first-PR evidence command after the first manual edit and before opening the first public PR. If the two files no longer represent the most believable proof pair for that preset, update the CLI output and tests together.

## Validation loop

```bash
python3 -m unittest tests/test_cli.py
```

That test pass keeps the printed command, README guidance, and scaffold expectations aligned.
