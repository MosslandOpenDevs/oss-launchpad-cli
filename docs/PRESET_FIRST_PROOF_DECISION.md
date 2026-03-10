# Preset first proof decision

Use this page when a freshly generated scaffold has multiple plausible first proof files and you need to pick one path quickly.

## Rule

Choose the first proof pair that shows both:

1. one human-visible product or launch artifact, and
2. one reproducible command or check artifact.

## Preset shortcuts

- `ai-agent` → `docs/agent-demo-brief.md` + `evals/smoke_cases.jsonl`
- `web-app` → `docs/landing-page-brief.md` + `demo/run_demo.sh`
- `python-lib` → `examples/basic_usage.py` + `tests/test_smoke.py`

## When to switch

If the chosen pair does not make the repo feel believable to a first reviewer in one screen, switch to the next pair before opening the PR.
