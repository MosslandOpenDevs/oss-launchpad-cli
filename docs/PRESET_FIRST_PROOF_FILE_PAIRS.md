# PRESET_FIRST_PROOF_FILE_PAIRS

Use these paired files when you want the first believable proof to show one visible asset and one reproducible check.

## ai-agent

- Visible proof: `docs/agent-demo-brief.md`
- Check asset: `evals/smoke_cases.jsonl`

## web-app

- Visible proof: `docs/landing-page-brief.md`
- Check asset: `demo/run_demo.sh`

## python-lib

- Visible proof: `docs/api-surface.md`
- Check asset: `tests/test_smoke.py`

## Rule of thumb

Open or edit both files in the same first PR so the scaffold looks alive and verifiable at the same time.
