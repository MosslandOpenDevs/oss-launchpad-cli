# Preset first-pass diff audit

Use this after `oss-launchpad init` generates a scaffold and before the first commit.

## Goal

Make the first diff easy to review so the generated preset feels intentional, not like a pile of placeholders.

## Quick audit

1. Open `README.md` and confirm the project title/tagline are no longer generic.
2. Open the preset-specific starter assets and replace at least one placeholder with real project intent.
3. Run the preset validation command shown by the CLI.
4. Check that the first commit only contains scaffold files you can explain in one short review note.

## Review note template

```text
Generated the {preset} scaffold, replaced the title/tagline placeholders, and validated the preset-specific starter path before the first commit.
```

## Why it helps

A small first-pass audit keeps the generated repo launch-ready for humans reviewing the bootstrap commit, not just for the CLI that created it.
