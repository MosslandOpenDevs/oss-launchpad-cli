# Preset first proof diff check

Use this check after the first preset-specific manual edit when you want to confirm that the diff already looks like believable public progress.

## The rule

A convincing first diff should show:

1. one visible proof asset that a visitor can read,
2. one reproducible proof command or test file that a maintainer can rerun,
3. and a clear pairing between the two.

## Preset cues

- `ai-agent` — pair `docs/agent-demo-brief.md` with `evals/smoke_cases.jsonl`
- `web-app` — pair `docs/landing-page-brief.md` with `docs/ui-ux-checklist.md` or `demo/run_demo.sh`
- `python-lib` — pair `docs/api-surface.md` or `examples/basic_usage.py` with `tests/test_smoke.py`

## Maintainer question

If this diff landed on GitHub today, would a first-time visitor immediately see what the project proves and how to rerun that proof?

If not, keep shaping the first manual proof before the first public push.
