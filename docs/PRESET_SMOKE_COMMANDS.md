# Preset Smoke Commands

`oss-launchpad init` prints one preset-specific smoke command so maintainers know the first proof step immediately after scaffold generation.

This document explains what each command is checking and when to replace it with a stronger project-specific validation step.

## ai-agent

Printed smoke command:

```bash
python3 -m json.tool --json-lines < evals/smoke_cases.jsonl >/dev/null
```

What it proves:

- the generated eval file exists,
- every line is valid JSON, so the file stays parseable as more eval cases are added,
- and the maintainer has an obvious first artifact to customize.

(The file is read via stdin redirection because `json.tool --json-lines <file>` is broken on some Python versions.)

Upgrade later to a real eval runner once the repo has a model or agent loop.

## web-app

Printed smoke command:

```bash
bash demo/run_demo.sh && sed -n '1,40p' docs/landing-page-brief.md
```

(The script uses bash-only options such as `pipefail`, so it is invoked with `bash` rather than `sh`.)

What it proves:

- the demo script is runnable,
- the maintainer can inspect the landing-page brief quickly,
- and the scaffold already includes a first product-surface artifact.

Upgrade later to a real frontend build, test, or screenshot step.

## python-lib

Printed smoke command:

```bash
PYTHONPATH=src python3 -m unittest tests/test_smoke.py && PYTHONPATH=src python3 examples/basic_usage.py
```

(`PYTHONPATH=src` is repeated because a `VAR=value` prefix only applies to the first command in a `&&` chain.)

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
