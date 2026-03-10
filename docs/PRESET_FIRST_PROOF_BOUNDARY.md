# Preset first-proof boundary

Use this guide when the generated scaffold already looks good, but the first public proof still needs a narrow and believable scope.

## Goal

Pick one visible proof asset and one reproducible check asset without turning the first manual commit into a full roadmap dump.

## Boundary rule

For the first proof, keep the change set to:

1. one preset-specific artifact that a reviewer can inspect quickly, and
2. one command or file that proves the artifact is not decorative.

## Examples

- `ai-agent`: `docs/agent-demo-brief.md` + `evals/smoke_cases.jsonl`
- `web-app`: `docs/landing-page-brief.md` + `demo/run_demo.sh`
- `python-lib`: `docs/api-surface.md` + `tests/test_smoke.py`

## Copy-ready maintainer note

```text
First proof scope: customize <visible artifact> and validate it with <check asset> before expanding into broader backlog work.
```

## Expand later, not now

Defer roadmap items, polish passes, and broad repo cleanup until the first proof pair feels reviewable on its own.
