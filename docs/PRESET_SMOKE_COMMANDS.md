# Preset Smoke Commands

`oss-launchpad init` prints one preset-specific smoke command so maintainers know the first proof step immediately after scaffold generation.

This document explains what each command is checking and when to replace it with a stronger project-specific validation step.

## ai-agent

Printed smoke command:

```bash
python3 -m json.tool evals/smoke_cases.jsonl >/dev/null || head -n 3 evals/smoke_cases.jsonl
```

What it proves:

- the generated eval file exists,
- the JSONL content is visible immediately,
- and the maintainer has an obvious first artifact to customize.

Upgrade later to a real eval runner once the repo has a model or agent loop.

## web-app

Printed smoke command:

```bash
sh demo/run_demo.sh && sed -n '1,40p' docs/landing-page-brief.md
```

What it proves:

- the demo script is runnable,
- the maintainer can inspect the landing-page brief quickly,
- and the scaffold already includes a first product-surface artifact.

Upgrade later to a real frontend build, test, or screenshot step.

## python-lib

Printed smoke command:

```bash
PYTHONPATH=src python3 -m unittest tests/test_smoke.py && python3 examples/basic_usage.py
```

What it proves:

- import paths work,
- the generated package can pass a tiny unit test,
- and the example script runs as the first public usage proof.

Upgrade later to a fuller test suite and package build step.

## Maintenance rule

Keep the printed smoke command:

- fast,
- dependency-light,
- and obviously tied to the generated preset.

It should prove the scaffold is alive, not pretend the project is production-complete.
