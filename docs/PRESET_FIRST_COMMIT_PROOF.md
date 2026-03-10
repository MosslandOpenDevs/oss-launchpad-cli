# Preset first-commit proof

Use this guide right after scaffold generation and before the first real commit.

## Goal

Make the first manual commit look like proof of life, not placeholder churn.

## Per-preset proof target

### `ai-agent`

Open and edit:

- `prompts/system.txt`
- `docs/agent-demo-brief.md`
- `evals/smoke_cases.jsonl`

Good first-commit proof:

- the prompt has a clear role,
- the demo brief matches the intended workflow,
- the smoke cases name at least one believable scenario.

### `web-app`

Open and edit:

- `docs/landing-page-brief.md`
- `docs/ui-ux-checklist.md`
- `docs/information-architecture.md`

Good first-commit proof:

- the landing brief names the audience,
- the checklist names one concrete UX promise,
- the information architecture shows the first key screens or routes.

### `python-lib`

Open and edit:

- `src/<package>/__init__.py`
- `examples/basic_usage.py`
- `docs/api-surface.md`

Good first-commit proof:

- the package exposes one intentional public entry point,
- the example script runs the simplest believable usage,
- the API doc names the smallest stable surface.

## Quick review rule

Before committing, make sure at least one file shows product intent and at least one file shows runnable proof.
