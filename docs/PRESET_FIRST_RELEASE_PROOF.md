# First release proof map

Use this page after scaffold generation and before the first public release.
It compresses the preset-specific "what should I prove first?" question into one short checklist.

## ai-agent

- Proof files: `prompts/system.txt`, `evals/smoke_cases.jsonl`, `docs/agent-demo-brief.md`
- Proof command: `python3 -m json.tool evals/smoke_cases.jsonl >/dev/null`
- Release-ready signal: the system prompt, demo brief, and sample eval cases all describe the same first public agent behavior.

## web-app

- Proof files: `.env.example`, `docs/landing-page-brief.md`, `docs/information-architecture.md`
- Proof command: `sh demo/run_demo.sh >/dev/null && sed -n '1,20p' docs/landing-page-brief.md`
- Release-ready signal: the demo script, landing brief, and IA doc all point to the same first user journey.

## python-lib

- Proof files: `src/<package>/__init__.py`, `tests/test_smoke.py`, `docs/api-surface.md`
- Proof command: `PYTHONPATH=src python3 -m unittest tests/test_smoke.py`
- Release-ready signal: the documented API surface, the import path, and the smoke test all prove the same first public function.

## One-line maintainer rule

Ship the first release only after the preset proof files and the preset proof command tell the same story.
