# Preset first custom proof

After `oss-launchpad init`, make one small preset-specific edit and capture one believable proof before opening the first real PR.

## Suggested first proof by preset

- `ai-agent`: edit `prompts/system.txt`, then show the first few lines of `evals/smoke_cases.jsonl`.
- `web-app`: edit `docs/landing-page-brief.md`, then run `sh demo/run_demo.sh`.
- `python-lib`: edit `examples/basic_usage.py`, then run `PYTHONPATH=src python3 examples/basic_usage.py`.

## Why this matters

The generated scaffold should look alive after one maintainer edit. A first custom proof helps reviewers see that the preset is not only generated correctly, but also easy to turn into a real project.
