# Preset first proof commands

Use this page when you want the shortest convincing command to run right after scaffold generation.

## AI agent

```bash
python3 -m json.tool evals/smoke_cases.jsonl >/dev/null || head -n 3 evals/smoke_cases.jsonl
```

Why it helps: proves the eval file exists and is readable before you wire a real harness.

## Web app

```bash
sh demo/run_demo.sh && sed -n '1,40p' docs/landing-page-brief.md
```

Why it helps: proves the demo entry point and landing brief exist before UI implementation starts.

## Python lib

```bash
PYTHONPATH=src python3 -m unittest tests/test_smoke.py && python3 examples/basic_usage.py
```

Why it helps: proves the package imports cleanly and the example script still matches the scaffold.

## Commit rule

Run the repo-level smoke tests before changing template or README claims:

```bash
python3 -m unittest tests/test_cli.py
```