# Preset first changeset check

Use this check before you publish the first non-template changeset created from a preset.

## Goals

- Confirm the scaffold produced a useful starting diff.
- Keep the first maintainer-facing commit small and reviewable.
- Make sure preset-specific proof files are still coherent after customization.

## Checklist

1. Review the generated README placeholders and replace any project-specific gaps.
2. Keep the first custom diff focused on one theme, such as naming, scope, or release metadata.
3. Re-run the documented smoke command for the chosen preset.
4. Verify at least one preset-specific proof asset still matches the customized project layout.
5. Capture the exact command set that produced the proof so a maintainer can repeat it.

## Output

A good first changeset should leave the repo in a state where a second contributor can understand the preset choice, the initial customization, and the validation command history without reading hidden context.
