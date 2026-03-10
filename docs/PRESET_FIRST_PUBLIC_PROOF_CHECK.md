# Preset first public proof check

Use this guide right after scaffold generation and before the first public push.

## Goal

Make sure the generated repo already shows one believable proof of life that matches the selected preset.

## By preset

### `ai-agent`

Look for:

- `prompts/system.txt` customized beyond placeholders,
- `evals/smoke_cases.jsonl` present and readable,
- one short demo brief in `docs/agent-demo-brief.md`.

Fast proof:

```bash
python3 -m json.tool evals/smoke_cases.jsonl >/dev/null || head -n 3 evals/smoke_cases.jsonl
```

### `web-app`

Look for:

- `.env.example` filled with realistic keys,
- `docs/landing-page-brief.md` aligned with the README promise,
- `docs/information-architecture.md` naming the first screen clearly.

Fast proof:

```bash
sh demo/run_demo.sh && sed -n '1,40p' docs/landing-page-brief.md
```

### `python-lib`

Look for:

- import path matches the printed package slug,
- `examples/basic_usage.py` runs,
- `docs/api-surface.md` names the first public API.

Fast proof:

```bash
PYTHONPATH=src python3 -m unittest tests/test_smoke.py && python3 examples/basic_usage.py
```

## Exit question

Before the first public push, ask:

- Would a stranger believe this repo has a real starting direction after reading the README and opening the preset proof file?
