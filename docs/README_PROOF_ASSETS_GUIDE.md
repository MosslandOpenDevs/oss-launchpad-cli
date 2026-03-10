# README proof assets guide

Use this guide after scaffold generation to make the generated README feel credible before the first public push.

## What "proof assets" means here

A launch-ready README should show at least one concrete proof that the project is real:

- a runnable command,
- a realistic demo path,
- a benchmark or evaluation pointer,
- or an API/example snippet that matches the preset.

## Preset-specific proof assets

### AI agent

- Point to `prompts/system.txt` as the first artifact to inspect.
- Mention `evals/smoke_cases.jsonl` so visitors see an evaluation surface immediately.
- Summarize the demo flow from `docs/agent-demo-brief.md`.

### Web app

- Show the first local run command near the top.
- Mention the user journey documented in `docs/landing-page-brief.md`.
- Point readers to `docs/information-architecture.md` if the app structure matters for evaluation.

### Python library

- Include the shortest useful snippet from `examples/basic_usage.py`.
- Mention the first public API surface from `docs/api-surface.md`.
- Keep the smoke test command visible so maintainers can verify the package quickly.

## Quick README check

Before the first push, confirm the README answers:

1. What does this project help someone do?
2. What is the first command to run?
3. What file proves the repo is more than a placeholder scaffold?
4. Which preset-specific asset should a contributor edit first?
