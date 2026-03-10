# Preset first-issue triage

Use this guide right after scaffold generation when you want to turn the generated repo into its first reviewable issue list.

## Goal

Convert preset-specific starter assets into the smallest believable issue backlog.

## By preset

### ai-agent
- Turn `docs/agent-demo-brief.md` into the first demo-proof issue.
- Turn `evals/smoke_cases.jsonl` into the first evaluation-coverage issue.
- Turn `prompts/system.txt` into the first prompt-hardening issue.

### web-app
- Turn `docs/landing-page-brief.md` into the first landing-copy issue.
- Turn `docs/ui-ux-checklist.md` into the first UX polish issue.
- Turn `docs/information-architecture.md` into the first navigation-structure issue.

### python-lib
- Turn `docs/api-surface.md` into the first API-shaping issue.
- Turn `examples/basic_usage.py` into the first example-quality issue.
- Turn `tests/test_smoke.py` into the first baseline-test issue.

## Good issue wording

Use issue titles that keep the preset proof visible, for example:

- `ai-agent: tighten smoke eval coverage before first public demo`
- `web-app: align landing brief and demo script before preview PR`
- `python-lib: validate API surface against basic usage example`
