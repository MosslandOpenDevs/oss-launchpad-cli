# PRESET_FIRST_PROOF_REPO_PUSH_CHECK

Use this checklist right before the first public push of a freshly scaffolded repo.

## What to confirm

1. The preset-specific proof asset has real project wording instead of untouched template copy.
2. The matching reproducible check still runs without extra undocumented setup.
3. `docs/launch-plan.md` names the intended audience and launch scope.
4. `docs/launch-scorecard.md` records the current proof status honestly.
5. The first public diff is still small enough to review in one pass.

## Suggested proof pair by preset

- `ai-agent` — `docs/agent-demo-brief.md` + `evals/smoke_cases.jsonl`
- `web-app` — `docs/landing-page-brief.md` + `demo/run_demo.sh`
- `python-lib` — `examples/basic_usage.py` + `tests/test_smoke.py`

## Ready-to-push signal

If one visible proof asset and one reproducible check asset are both customized and reviewed, the repo is ready for the first believable public push.
