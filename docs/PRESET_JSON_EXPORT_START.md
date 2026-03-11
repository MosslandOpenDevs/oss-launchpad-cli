# PRESET_JSON_EXPORT_START

Use `oss-launchpad presets --json` when a script, UI, or review bot needs the preset catalog without scraping human-readable CLI output.

Quick replay:

```bash
PYTHONPATH=src python3 -m oss_launchpad_cli.cli presets --json
```

Minimum expectation:
- one top-level object keyed by preset name
- starter assets for each preset
- quickstart docs, first-proof assets, and day-zero docs
- preset-specific validation and review commands

Use this export before wiring preset choosers, result-card copy, or maintainer handoff automation.
