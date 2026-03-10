# PRESET_FIRST_PROOF_LINK_CHECK

Use this checklist before the first public proof commit so the generated README links to a believable preset-specific asset.

## Goal

Make the first manual proof feel connected, not ornamental.

## Check

For the chosen preset, confirm the README points to at least one real proof asset:

- `ai-agent` → prompt or eval asset
- `web-app` → UX or information-architecture brief
- `python-lib` → API surface or runnable example

## Pass

Pass when one visible README link and one reproducible check asset both exist in the diff.

## Hold

Hold when the README claims proof that the scaffold does not yet link or demonstrate.
