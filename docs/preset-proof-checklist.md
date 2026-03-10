# Preset Proof Checklist

Use this checklist before publishing changes to scaffold presets.

## Verify each preset

- `ai-agent` generates a usable starter README and docs folder
- `web-app` includes environment example and information architecture note
- `python-lib` includes packaging metadata and contribution guidance

## Smoke expectations

- init command finishes without manual file edits
- generated tree contains the preset-specific proof files promised in the README
- rerunning generation into a fresh directory produces the same key files

## Release note prompt

When a preset changes, mention:

- which preset changed
- which proof file was added or updated
- which test or smoke command passed
