# PRESET_CUSTOMIZE_FIRST_GUIDE

Use this guide after `oss-launchpad init ...` prints the customize-first command.

## Why this guide exists

Generated scaffolds should feel alive quickly. The first manual edits should touch the files that prove the preset is real, not just generic repo metadata.

## Preset-specific first edits

- `ai-agent` — update `prompts/system.txt`, add a realistic case to `evals/smoke_cases.jsonl`, and align `docs/agent-demo-brief.md` with the first public demo.
- `web-app` — update `docs/ui-ux-checklist.md`, tighten `docs/landing-page-brief.md`, and replace placeholder assumptions in `.env.example`.
- `python-lib` — replace the placeholder docstring in `src/<package>/__init__.py`, expand `examples/basic_usage.py`, and document the first stable API slice in `docs/api-surface.md`.

## Fast rule

If the first commit only changes generic repo metadata, the scaffold still looks half-finished. Make the first preset-specific proof asset better before going public.
