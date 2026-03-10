# Preset first-commit guide

Use this guide right after `oss-launchpad init ...` when the scaffold exists, but the repository still needs a convincing first real commit.

## Goal

Turn the generated scaffold into a repo that shows one preset-specific proof point before the first public push.

## First-commit checklist by preset

### `ai-agent`

- Replace `prompts/system.txt` with the first real system contract.
- Add one meaningful example row to `evals/smoke_cases.jsonl`.
- Fill `docs/agent-demo-brief.md` with the first happy-path demo and one failure mode.

### `web-app`

- Fill `.env.example` with the minimum boot variables.
- Replace placeholder UX notes in `docs/ui-ux-checklist.md`.
- Add one real landing-page proof point to `docs/landing-page-brief.md`.

### `python-lib`

- Export one real symbol from `src/<package>/__init__.py`.
- Update `examples/basic_usage.py` so the example imports and runs.
- Keep `tests/test_smoke.py` aligned with that first public API.

## One good first-commit message pattern

```text
Add first preset-specific proof assets
```

## Validation before commit

Use the preset-specific validation command printed by `init`, then confirm the smoke command still works.
