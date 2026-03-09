# Preset selection guide

Pick the preset that matches the first public proof you want a stranger to understand.

## `ai-agent`

Choose this when the repository's first proof is prompt behavior, evaluation cases, or a system-contract style demo.

Generated emphasis:

- `prompts/system.txt`
- `evals/README.md`
- `evals/smoke_cases.jsonl`
- `docs/agent-demo-brief.md`

Best for:

- agent repos
- prompt/evals packages
- workflow automation demos

## `web-app`

Choose this when the first proof is a visible product surface or a guided happy-path demo.

Generated emphasis:

- `.env.example`
- `docs/ui-ux-checklist.md`
- `docs/landing-page-brief.md`
- `docs/information-architecture.md`

Best for:

- landing pages
- dashboards
- SaaS/product MVPs

## `python-lib`

Choose this when the first proof is importable API shape, local tests, and code examples.

Generated emphasis:

- `pyproject.toml`
- `src/<package>/__init__.py`
- `tests/test_smoke.py`
- `examples/basic_usage.py`
- `docs/api-surface.md`

Best for:

- SDKs
- utility libraries
- reusable internal packages being prepared for public release

## Fast decision rule

- If strangers should judge the repo by behavior and evals first -> `ai-agent`
- If strangers should judge the repo by UI and flow first -> `web-app`
- If strangers should judge the repo by API and importable code first -> `python-lib`
