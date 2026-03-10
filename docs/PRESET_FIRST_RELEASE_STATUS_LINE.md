# Preset first release status line

Use this line when a generated project has passed its first smoke proof and you want a tiny release-ready update that stays believable.

## Template

```text
First release status: <preset> is <ready|waiting|blocked> because <visible proof asset> pairs with <release check>, next step <single launch action>.
```

## Examples

- `First release status: ai-agent is ready because evals/smoke_cases.jsonl pairs with python3 -m json.tool evals/smoke_cases.jsonl >/dev/null, next step publish the first prompt-and-eval demo.`
- `First release status: web-app is waiting because docs/ui-ux-checklist.json pairs with python3 -m json.tool docs/ui-ux-checklist.json >/dev/null, next step capture the first landing-page screenshot review.`
- `First release status: python-lib is blocked because tests/test_smoke.py pairs with PYTHONPATH=src python3 -m unittest tests/test_smoke.py, next step restore the failing import before tagging.`
