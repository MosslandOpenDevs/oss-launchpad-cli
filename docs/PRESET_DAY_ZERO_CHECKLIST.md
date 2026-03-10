# Preset day-zero checklist

Use this checklist right after `oss-launchpad init` and before the first public push.

## Day-zero checklist

1. Open `README.md` and replace the placeholder setup path with the first real local run command.
2. Fill `docs/launch-plan.md` with the launch audience, proof assets, and release scope.
3. Fill `docs/launch-scorecard.md` so launch readiness is visible before announcement.
4. Run the preset-specific validation command from the CLI output.
5. Capture the preset-specific proof asset named in the CLI output.
6. Make one preset-specific edit so the scaffold stops looking generic.

## Preset-specific first proof

- `ai-agent` — update `prompts/system.txt` and validate `evals/smoke_cases.jsonl`.
- `web-app` — review `docs/landing-page-brief.md` and run `demo/run_demo.sh`.
- `python-lib` — edit `src/<package>/__init__.py` and run `python3 -m unittest tests/test_smoke.py`.

## Use with

- `docs/PRESET_FIRST_PROOF_COMMANDS.md`
- `docs/PRESET_VALIDATION_COMMANDS.md`
- `docs/PRESET_FIRST_COMMIT_GUIDE.md`
- `docs/PRESET_PROOF_OF_LIFE_CHECKLIST.md`
