# Preset first pull request guide

Use this guide after `oss-launchpad init ...` and before opening the first real pull request in the generated repository.

## Goals for the first PR

- replace placeholder setup text with the first runnable command
- customize the preset-specific starter assets
- capture one proof artifact that shows the repo is alive
- keep the launch docs aligned with the code surface

## Preset-specific checklist

### ai-agent

- update `prompts/system.txt` with the first real agent contract
- add a realistic command to `evals/README.md`
- keep `evals/smoke_cases.jsonl` runnable as a tiny proof set
- record the first demo path in `docs/agent-demo-brief.md`

### web-app

- fill `.env.example` with the minimum local variables
- replace placeholder UX checks in `docs/ui-ux-checklist.md`
- update `docs/landing-page-brief.md` with the first public proof flow
- keep `docs/information-architecture.md` consistent with the README promise

### python-lib

- implement the first public function in `src/<package>/__init__.py`
- make `tests/test_smoke.py` prove the import path works
- update `examples/basic_usage.py` so the example matches the public API
- fill `docs/api-surface.md` with the first stable functions or classes

## Shared proof before merge

- run the printed smoke command
- run the printed validation command
- fill `docs/launch-plan.md`
- update `docs/launch-scorecard.md`
- confirm `RELEASE_CHECKLIST.md` still matches the first release story
