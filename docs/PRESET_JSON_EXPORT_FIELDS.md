# Preset JSON export fields

`oss-launchpad presets --json` is the machine-readable interface for CI scripts, preset choosers, and small web forms. Since v0.2.0 it returns one versioned envelope:

```json
{
  "schema_version": 1,
  "presets": { "<preset_key>": { ... } },
  "aliases": { "<alias>": "<preset_key>" }
}
```

`--preset <name-or-alias>` narrows `presets` to a single entry; the envelope shape stays the same.

## Per-preset fields

| Field | Meaning |
| --- | --- |
| `preset_key` | Stable identifier (`ai-agent`, `web-app`, `python-lib`). |
| `label` | Human-readable name for pickers. |
| `summary` | One-line "best when..." description. |
| `first_ui_slice` | The smallest believable first proof for the preset. |
| `ui_ux_lane` | Guidance for the first UI/UX pass. |
| `playwright_lane` | Guidance for the first browser-automation proof. |
| `playwright_recovery_lane` | Guidance for recovering a flaky browser proof. |
| `starter_assets` | Preset files to customize first. |
| `quickstart_docs` | Files to open first after generation. |
| `first_proof_assets` | Files that form the first believable proof. |
| `day_zero_docs` | Docs to complete before the first public push. |
| `commands` | Map of preset-specific commands (see below). |
| `next_steps` | Ordered post-generation checklist. |

## `commands` keys

`smoke`, `validation`, `customize_first`, `starter_review`, `day_zero_review`, `first_pr`, `proof_review`, `first_issue`, `first_release`.

Each value is a shell command relative to the generated project root. `{package_name}`-dependent commands (python-lib) are rendered with a sample package name in this export; the `init` output renders them with the real one.

## Migration from the 0.1.x export

The 0.1.x export duplicated most values under several synonym keys. Mapping to the current schema:

- `result_card_focus`, `report_download_checkpoint`, `proof_scope` -> `first_ui_slice`
- `primary_action`, `proof_validation_command`, `result_card_validation_command`, `validation_command` -> `commands.validation`
- `setup_command`, `result_card_setup_command`, `customize_first_command` -> `commands.customize_first`
- `smoke_command`, `*_review_command`, `first_pr_command`, `first_issue_command`, `first_release_command` -> the matching `commands.*` key
- `first_proof_status_command` -> removed without replacement (its file pairs are covered by `first_proof_assets`)
- per-entry `preset_count` -> removed (count entries in `presets` instead)
