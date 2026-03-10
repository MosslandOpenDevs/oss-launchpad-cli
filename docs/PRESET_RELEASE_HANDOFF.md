# Preset release handoff

Use this guide when a generated starter is ready to move from local proof to a public release handoff.

## Handoff checklist

1. Re-run the preset init command in a clean directory.
2. Confirm the README and starter files still match the selected preset story.
3. Run the documented smoke command for the generated project.
4. Record the first successful command output in the release note or PR.
5. Point maintainers to the exact preset-specific docs that explain the next customization step.

## Minimum release proof

- preset name
- init command used
- smoke command used
- first successful output
- next customization doc linked for maintainers

## When to hold the release

- starter files render with unresolved placeholders
- the smoke command differs from the README example
- preset-specific docs point to files that were not generated
- repeated init runs produce unstable file sets without explanation
