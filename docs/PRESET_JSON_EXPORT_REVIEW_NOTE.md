# PRESET_JSON_EXPORT_REVIEW_NOTE

Use this note when `oss-launchpad presets --json` is already available and you need a quick reviewer-facing explanation of what the export is for.

## Review note

`presets --json` is the machine-readable inventory for scaffold-aware tooling. It keeps starter assets, day-zero docs, and proof commands in one stable payload so CLIs, web forms, and bots do not have to hard-code preset copy.

## Minimum fields to keep visible

- `starter_assets`
- `quickstart_docs`
- `first_proof_assets`
- `day_zero_docs`
- `smoke_command`
- `validation_command`
- `first_proof_status_command`

If a workflow only needs one preset, slice the JSON downstream instead of maintaining a second preset map by hand.
