# Preset first proof status rules

When a generated scaffold is only partially customized, keep the public status line honest and preset-specific.

## Status line template

`First proof status: <preset> is ready because <visible artifact> pairs with <proof command>, scoped to <smallest believable launch claim>.`

## Rules

1. name one visible artifact reviewers can open immediately
2. pair it with one reproducible proof command
3. keep the scope to the smallest believable launch claim
4. expand the status only after the next preset proof also passes

## Examples

- `First proof status: ai-agent is ready because docs/agent-demo-brief.md pairs with python3 -m json.tool evals/smoke_cases.jsonl >/dev/null, scoped to a minimal prompt-and-eval story.`
- `First proof status: web-app is ready because docs/landing-page-brief.md pairs with python3 -m json.tool docs/ui-ux-checklist.json >/dev/null, scoped to one landing-page launch review.`
- `First proof status: python-lib is ready because tests/test_smoke.py pairs with PYTHONPATH=src python3 -m unittest tests/test_smoke.py, scoped to a minimal import-and-usage story.`
