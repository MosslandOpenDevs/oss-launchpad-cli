# Preset day-zero checklist

Use this checklist right after `oss-launchpad init` and before the first public push.

## Day-zero checklist

1. Open `README.md` and replace the placeholder setup path with the first real local run command.
2. Confirm `LICENSE` matches how you intend to publish the project.
3. Fill `docs/launch-plan.md` with the launch audience, proof assets, and release scope.
4. Fill `docs/launch-scorecard.md` so launch readiness is visible before announcement.
5. Run the preset-specific validation command from the CLI output.
6. Capture the preset-specific proof asset named in the CLI output.
7. Make one preset-specific edit so the scaffold stops looking generic.

## Preset-specific first proof

- `ai-agent` — update `prompts/system.txt` and validate `evals/smoke_cases.jsonl`.
- `web-app` — review `docs/landing-page-brief.md` and run `bash demo/run_demo.sh`.
- `python-lib` — edit `src/<package>/__init__.py` and run `PYTHONPATH=src python3 -m unittest tests/test_smoke.py`.

## Use with

- `docs/PRESET_SMOKE_COMMANDS.md`
- `docs/PRESET_CUSTOMIZE_FIRST_GUIDE.md`
- `docs/MAINTAINER_PLAYBOOK.md`
