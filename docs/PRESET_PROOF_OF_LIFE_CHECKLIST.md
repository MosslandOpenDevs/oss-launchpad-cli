# Preset proof-of-life checklist

After generating a scaffold, run one short proof-of-life check before making the first public commit.
The goal is not full production readiness; it is confirming that the generated preset already looks like a real repo instead of an empty shell.

## Shared checklist

- Open `README.md` and confirm the preset-specific tagline reads naturally.
- Run the preset-specific smoke command printed by `oss-launchpad init`.
- Open `docs/launch-plan.md` and fill the first public audience + proof section.
- Open `docs/launch-scorecard.md` and mark the first missing proof items.

## Preset-specific proof

### `ai-agent`

- Confirm `prompts/system.txt` states the agent role clearly.
- Confirm `evals/smoke_cases.jsonl` contains at least one realistic evaluation case.
- Confirm `docs/agent-demo-brief.md` describes the first public demo scenario.

### `web-app`

- Confirm `.env.example` names the required variables clearly.
- Confirm `docs/landing-page-brief.md` explains the first-screen promise.
- Confirm `docs/information-architecture.md` names the first navigation sections.

### `python-lib`

- Confirm `pyproject.toml` uses the expected package slug.
- Run `PYTHONPATH=src python3 -m unittest tests/test_smoke.py`.
- Run `python3 examples/basic_usage.py` and confirm it prints a plausible usage path.

## Commit heuristic

If the smoke command passes and the checklist answers are not blank, the scaffold is usually ready for a meaningful first preset-specific commit.
If the smoke command fails, fix that before polishing docs or screenshots.
