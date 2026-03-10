# Preset report proof loop

Use this note after `init` when you want a tiny but real proof that the generated scaffold is launch-ready enough to show another maintainer.

## Minimal loop

1. Generate a preset scaffold in a temp directory.
2. Run the preset-specific smoke command printed by the CLI.
3. Open the first preset-owned docs file and replace at least one placeholder with repo-specific content.
4. Confirm the scaffold still passes the local smoke test.
5. Share a one-line status update using the first-release wording guide.

## Why it helps

This keeps the project focused on scaffolds that produce evidence quickly instead of templates that only look complete in screenshots.
