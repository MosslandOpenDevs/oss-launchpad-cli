# Preset first-run signals

Use this guide right after `oss-launchpad init` when you want the shortest possible proof that the generated scaffold already feels alive.

## Expected first-run signals by preset

### ai-agent

- `prompts/system.txt` exists and names the agent contract.
- `evals/smoke_cases.jsonl` parses cleanly.
- `docs/agent-demo-brief.md` explains the first believable demo.

### web-app

- `.env.example` exposes the minimum local variables.
- `docs/landing-page-brief.md` describes the first page and CTA.
- `docs/information-architecture.md` lists the first navigation surface.

### python-lib

- `src/<package>/__init__.py` exposes a public symbol.
- `tests/test_smoke.py` passes with `PYTHONPATH=src`.
- `docs/api-surface.md` states the first import path and example.

## Maintainer rule

If a preset cannot show all three first-run signals yet, customize the preset-specific starter assets before the first public push.
