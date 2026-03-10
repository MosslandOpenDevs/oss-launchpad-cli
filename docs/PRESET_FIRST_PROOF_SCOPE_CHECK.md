# Preset first-proof scope check

Use this guide when the generated scaffold already looks believable, but you want to keep the first manual proof commit small and preset-specific.

## Goal

Turn scaffold output into one reviewable proof commit without accidentally expanding into roadmap work.

## Scope rule

Keep the first proof commit to:

1. one preset-specific visible asset,
2. one reproducible validation asset,
3. one README or launch-plan update that explains the proof.

## Preset examples

- `ai-agent` — update `docs/agent-demo-brief.md` + refine `evals/smoke_cases.jsonl` + note the proof in `docs/launch-plan.md`
- `web-app` — update `docs/landing-page-brief.md` + refine `docs/ui-ux-checklist.md` + note the proof in `docs/launch-plan.md`
- `python-lib` — update `examples/basic_usage.py` + refine `tests/test_smoke.py` + note the proof in `docs/launch-plan.md`

## Stop rule

If the diff starts creating multiple new features instead of making one believable public proof, split the work before opening the PR.
