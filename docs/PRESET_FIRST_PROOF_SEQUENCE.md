# PRESET_FIRST_PROOF_SEQUENCE

Use this page when a freshly generated scaffold needs the shortest believable proof path before the first public push.

## Sequence

1. Run the printed preset-specific smoke command.
2. Open the two files from the printed proof-review command.
3. Replace one placeholder with a real project detail in the highest-signal preset asset.
4. Re-run the validation command so the first proof is reproducible.
5. Capture the proof asset pair in the first PR or maintainer update.

## Preset hints

- `ai-agent`: start with `docs/agent-demo-brief.md` and `evals/smoke_cases.jsonl`.
- `web-app`: start with `docs/landing-page-brief.md` and `docs/ui-ux-checklist.md`.
- `python-lib`: start with `examples/basic_usage.py` and `docs/api-surface.md`.

## Pass signal

A first-time maintainer should be able to point to one real preset-specific edit plus one reproducible proof command without inventing extra process.
