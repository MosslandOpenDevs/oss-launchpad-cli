# Preset first-template touchpoints

Use this guide when reviewing whether a preset gives a believable first-run scaffold.

## Core touchpoints

- `README.md` explains what was generated and what to edit first.
- `docs/` contains at least one preset-specific direction file.
- `evals/` or smoke assets exist when the preset promises automated checks.
- A maintainer can identify the first customization file in under 30 seconds.
- Generated placeholders use project title and slug consistently.

## Fast review question

If a user runs `oss-launchpad init --preset <preset>`, can they identify the first proof-of-life edit without reading the source code?

## Pass signal

A preset passes this check when the first generated files make the next edit obvious and the smoke command can be found from the scaffold itself.
