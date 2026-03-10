# Preset first proof margin check

Use this check after `oss-launchpad init ... --preset <preset>` when the scaffold looks fine, but you want one more pass before calling the repo believable.

## The rule

Do not stop at "files exist".
Confirm that the preset exposes at least one visible proof asset and one reproducible proof command that clearly fit together.

## Preset-by-preset cue

- `ai-agent` — visible proof: `docs/agent-demo-brief.md`; reproducible proof: inspect `evals/smoke_cases.jsonl`
- `web-app` — visible proof: `docs/landing-page-brief.md`; reproducible proof: inspect `docs/ui-ux-checklist.md`
- `python-lib` — visible proof: `docs/api-surface.md`; reproducible proof: open `tests/test_smoke.py`

## Maintainer question

Can a first-time visitor tell what this repo proves, and can a maintainer rerun that proof without inventing new structure?

If the answer is no, the scaffold is still presentable but not yet convincing.
