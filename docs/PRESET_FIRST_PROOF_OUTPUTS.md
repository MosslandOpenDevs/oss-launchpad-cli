# PRESET_FIRST_PROOF_OUTPUTS

Use this guide right after `oss-launchpad init ...` when you want to know which generated files should become the first believable proof in a public repo.

## Goal

Turn scaffold output into an immediate proof-of-life pass instead of leaving the repo as a generic template dump.

## First proof by preset

### `ai-agent`

Open these first:

- `prompts/system.txt`
- `evals/smoke_cases.jsonl`
- `docs/agent-demo-brief.md`

Proof idea: show that the system prompt, smoke cases, and demo brief already describe one coherent agent behavior.

### `web-app`

Open these first:

- `.env.example`
- `docs/landing-page-brief.md`
- `docs/ui-ux-checklist.md`

Proof idea: show that setup inputs, landing-page messaging, and UI review checkpoints already agree.

### `python-lib`

Open these first:

- `pyproject.toml`
- `examples/basic_usage.py`
- `tests/test_smoke.py`

Proof idea: show that install metadata, a runnable example, and a smoke test already form one credible first-use path.

## Rule of thumb

If a maintainer can point to these preset-specific files and run the printed smoke command, the scaffold already has a believable first public proof.
