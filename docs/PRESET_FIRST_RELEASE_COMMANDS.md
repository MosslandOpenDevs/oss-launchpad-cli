# PRESET_FIRST_RELEASE_COMMANDS

Use this guide when you want one believable release-proof command per preset before the first public tag.

## Release-proof commands

- `ai-agent` → `sed -n '1,120p' docs/launch-plan.md && sed -n '1,120p' docs/agent-demo-brief.md && python3 -m json.tool evals/smoke_cases.jsonl >/dev/null`
- `web-app` → `sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' docs/landing-page-brief.md && sh demo/run_demo.sh >/dev/null`
- `python-lib` → `sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' docs/api-surface.md && PYTHONPATH=src python3 -m unittest tests/test_smoke.py`

## What good looks like

- one visible proof asset is present,
- one reproducible command passes,
- the release scope is written down,
- the maintainer can paste the command into a PR or release checklist without editing it first.
