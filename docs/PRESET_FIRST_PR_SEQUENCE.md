# Preset first PR sequence

Use this sequence after scaffold generation and before opening the first real pull request in the generated repository.

1. Customize one preset-specific starter file.
2. Run the printed preset smoke command.
3. Open the printed proof-review file pair.
4. Update `docs/launch-plan.md` with the first public proof story.
5. Update `docs/launch-scorecard.md` with the same proof status.
6. Open the PR only after the smoke command and proof pair still agree.

## Preset anchor choices

- `ai-agent` — start with `prompts/system.txt` + `evals/smoke_cases.jsonl`
- `web-app` — start with `docs/landing-page-brief.md` + `demo/run_demo.sh`
- `python-lib` — start with `src/<package>/__init__.py` + `tests/test_smoke.py`

## Why this exists

The first PR should show one visible proof asset and one reproducible check asset. That is the smallest believable signal that the generated repo is turning into a real project instead of staying a scaffold.
