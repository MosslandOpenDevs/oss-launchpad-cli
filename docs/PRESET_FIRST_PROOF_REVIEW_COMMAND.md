# Preset first proof review command

Use this guide when a maintainer already generated a scaffold and wants the shortest command pair to review the first believable proof files before the first public push.

## Goal

Turn the preset starter assets into a tiny review ritual instead of an open-ended manual browse.

## Review command pattern

```bash
printf '%s\n' <proof-file-1> <proof-file-2> | xargs -I{} sh -c 'echo "== {} ==" && sed -n "1,120p" "{}"'
```

## Suggested proof file pairs

- `ai-agent` → `prompts/system.txt` + `docs/agent-demo-brief.md`
- `web-app` → `.env.example` + `docs/landing-page-brief.md`
- `python-lib` → `examples/basic_usage.py` + `docs/api-surface.md`

## Done signal

The proof review is good enough when both files read like project-specific assets instead of untouched placeholders.
