# Preset first smoke proof

Use this checklist when you want one small proof-of-life commit immediately after `oss-launchpad init`.

## Goal
Show that the selected preset is not just generated, but also reviewable with one preset-specific smoke artifact.

## Proof recipe by preset
- `ai-agent` — run the smoke command, then review `evals/smoke_cases.jsonl` and `docs/agent-demo-brief.md` together.
- `web-app` — review `docs/landing-page-brief.md` and `docs/ui-ux-checklist.md`, then record one small landing change.
- `python-lib` — run `PYTHONPATH=src python3 -m unittest tests/test_smoke.py`, then review `examples/basic_usage.py` and `docs/api-surface.md`.

## Commit shape
Keep the first smoke-proof commit small: one generated scaffold check, one preset-specific artifact review, and one note in the README or docs about what was verified.
