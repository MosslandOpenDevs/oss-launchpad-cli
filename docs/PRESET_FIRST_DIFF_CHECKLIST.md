# Preset first-diff checklist

Use this checklist after `oss-launchpad init` and before the first public commit when you want the generated repository to show one believable preset-specific improvement.

## First-diff checklist

1. Keep the generated README title and preset framing, but replace at least one placeholder sentence with project-specific intent.
2. Edit the preset-specific proof asset first:
   - `ai-agent` -> `evals/smoke_cases.jsonl`
   - `web-app` -> `docs/information-architecture.md`
   - `python-lib` -> `docs/api-surface.md`
3. Update `docs/launch-plan.md` so the audience and first proof asset match the chosen preset.
4. Run the preset-specific smoke command printed by the CLI.
5. Run the preset validation command before the first push.

## Why this matters

A generated scaffold looks generic until the first diff proves the preset is real. This checklist keeps the first commit focused on evidence instead of repo housekeeping.

## Pair with

- `docs/PRESET_FIRST_COMMIT_GUIDE.md`
- `docs/PRESET_FIRST_PROOF_COMMANDS.md`
- `docs/PRESET_VALIDATION_COMMANDS.md`
