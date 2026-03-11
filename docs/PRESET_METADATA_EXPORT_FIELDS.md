# PRESET_METADATA_EXPORT_FIELDS

Use `oss-launchpad presets --json` when you need machine-readable preset guidance instead of the human-readable starter-asset list.

## Keep these fields visible

For each preset, the JSON payload should expose:

- `starter_assets`
- `first_proof_assets`
- `day_zero_docs`
- `smoke_command`
- `validation_command`
- `customize_first_command`
- `starter_review_command`
- `day_zero_review_command`
- `first_pr_command`
- `proof_review_command`
- `first_proof_status_command`
- `first_issue_command`
- `first_release_command`

## Why it matters

This keeps preset discovery useful for CLIs, scripts, and agent handoffs that need the same launch guidance the interactive `init` flow prints.
