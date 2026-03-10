# Preset first proof status check

Use this before claiming that a freshly generated preset already has a believable first proof.

## Four-point check

1. **Visible proof asset exists** — a preset-specific file already shows what the repo is about.
2. **Reproducible check exists** — a command or test can verify the proof without manual storytelling.
3. **Scope is narrow** — the first proof is one believable slice, not an entire roadmap.
4. **Public wording is ready** — you can describe the proof in one sentence for a PR or maintainer update.

## Status sentence template

`First proof status: <preset> is ready because <visible asset> pairs with <check command>, scoped to <single believable claim>.`

## Example

`First proof status: python-lib is ready because docs/api-surface.md pairs with python3 -m unittest tests/test_cli.py, scoped to a minimal import-and-usage story.`

## Quick fail cue

If you cannot name both a visible proof asset and a reproducible check, the preset is not first-proof ready yet.
