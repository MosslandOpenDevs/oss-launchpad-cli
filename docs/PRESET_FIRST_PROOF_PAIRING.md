# PRESET_FIRST_PROOF_PAIRING

Use this page when a new scaffold already has multiple preset starter files and you need the fastest believable proof pair before the first public push.

## Pairing rule

1. Pick one visible proof asset (`README.md`, `docs/landing-page-brief.md`, `docs/agent-demo-brief.md`, or `examples/basic_usage.py`).
2. Pair it with one reproducible check asset (`evals/smoke_cases.jsonl`, `docs/ui-ux-checklist.md`, `docs/api-surface.md`, or `tests/test_smoke.py`).
3. Make one real project-specific edit in the visible asset.
4. Run the printed preset-specific smoke command against the paired proof asset.
5. Mention both files in the first maintainer update or PR so reviewers can verify the repo feels alive.

## Preset-first pairs

- `ai-agent`: `docs/agent-demo-brief.md` + `evals/smoke_cases.jsonl`
- `web-app`: `docs/landing-page-brief.md` + `docs/ui-ux-checklist.md`
- `python-lib`: `examples/basic_usage.py` + `docs/api-surface.md`

## Pass signal

A new maintainer should be able to point to one visible product-facing file and one reproducible proof file that already support the first public review.
