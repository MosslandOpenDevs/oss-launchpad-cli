# Preset output proof map

Use this map after `oss-launchpad init` prints the scaffold summary and you want the shortest route from generated files to a believable first proof.

## ai-agent

- **Proof command** — validate `evals/smoke_cases.jsonl`
- **Proof files to open first** — `prompts/system.txt`, `docs/agent-demo-brief.md`, `docs/launch-plan.md`
- **Public proof angle** — show prompt contract + tiny eval set + demo narrative

## web-app

- **Proof command** — run `sh demo/run_demo.sh` and preview `docs/landing-page-brief.md`
- **Proof files to open first** — `.env.example`, `docs/ui-ux-checklist.md`, `docs/information-architecture.md`
- **Public proof angle** — show visible user flow + setup contract + page structure

## python-lib

- **Proof command** — run the smoke test and `examples/basic_usage.py`
- **Proof files to open first** — `pyproject.toml`, `src/<package>/__init__.py`, `docs/api-surface.md`
- **Public proof angle** — show importable API + runnable example + minimal tests

## Shared rule

Before the first public push, make at least one preset-specific proof file better than the generated default and record the scope in `docs/launch-plan.md`.
