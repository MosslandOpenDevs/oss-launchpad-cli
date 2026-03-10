# Preset first proof ready signal

Use this page to decide whether a freshly customized scaffold already shows a believable first proof.

## Ready signal

A preset is first-proof ready when it shows:

1. one visible proof asset,
2. one reproducible check asset,
3. one short maintainer explanation tying them together.

## By preset

### ai-agent

- Visible proof asset: `docs/agent-demo-brief.md` or `prompts/system.txt`
- Reproducible check asset: `evals/smoke_cases.jsonl`
- Maintainer explanation: a README or launch-plan note that says what the first agent demo proves

### web-app

- Visible proof asset: `docs/landing-page-brief.md` or `docs/ui-ux-checklist.md`
- Reproducible check asset: `demo/run_demo.sh`
- Maintainer explanation: a README or launch-plan note that says what the demo flow proves

### python-lib

- Visible proof asset: `docs/api-surface.md` or `examples/basic_usage.py`
- Reproducible check asset: `tests/test_smoke.py`
- Maintainer explanation: a README or launch-plan note that says what the library smoke path proves

## Fast no-go signs

Do not call the scaffold first-proof ready yet if:

- both files are present but neither has repo-specific content,
- the proof command still fails,
- the README cannot explain what strangers should look at first.

## Next docs

- `docs/PRESET_FIRST_PROOF_AUDIT.md`
- `docs/PRESET_FIRST_PROOF_DIFF_CHECK.md`
- `docs/PRESET_FIRST_PUBLIC_PROOF_CHECK.md`
