# Preset validation commands

Use these commands after the first scaffold edit when you want the shortest proof that the generated preset still boots in a believable way.

## ai-agent

```bash
python3 -m json.tool evals/smoke_cases.jsonl >/dev/null
```

Confirms the committed smoke cases remain valid JSON before you wire a real evaluation runner.

## web-app

```bash
sh demo/run_demo.sh >/dev/null && sed -n '1,20p' docs/landing-page-brief.md
```

Confirms the demo script still runs and the landing brief remains presentable after the first copy/UX edit.

## python-lib

```bash
PYTHONPATH=src python3 -m unittest tests/test_smoke.py
```

Confirms the package import path and the generated smoke test still pass after the first API edit.
