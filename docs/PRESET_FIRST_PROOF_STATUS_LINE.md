# Preset first proof status line

Use this when you need a short maintainer update immediately after generating or customizing a preset scaffold.

## Include four cues

1. the preset name,
2. the first proof files now present,
3. the validation command you ran,
4. the next public-proof step.

## Copy-ready pattern

`<preset>: first proof files are in place (<file pair>), the preset validation command passed, and the next public-proof step is <next proof action>.`

## Preset file-pair cues

- `ai-agent` — `prompts/system.txt` + `evals/smoke_cases.jsonl`
- `web-app` — `docs/landing-page-brief.md` + `docs/information-architecture.md`
- `python-lib` — `examples/basic_usage.py` + `tests/test_smoke.py`

## Pair with

- `docs/PRESET_FIRST_MAINTAINER_UPDATE.md`
- `docs/PRESET_FIRST_PROOF_FILE_PAIRS.md`
- `docs/PRESET_FIRST_PUBLIC_PROOF_CHECK.md`
