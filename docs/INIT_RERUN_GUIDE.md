# Init rerun guide

`oss-launchpad init` is intentionally safe to rerun.
This guide explains what maintainers should expect when they use it as a non-destructive scaffold check.

## What rerun-safe means here

A second run against the same directory should:

- keep existing files untouched,
- print `No new files created.` when the scaffold is already complete,
- preserve preset-specific starter files,
- and still print the title slug, smoke command, and next steps.

## Recommended maintainer workflow

1. Run `oss-launchpad init <path> --preset <preset>` once to create the scaffold.
2. Make your repo-specific edits.
3. Rerun the same command before opening the repo publicly.
4. Confirm the CLI reports that no new files were created.
5. Re-run the preset smoke command printed by the CLI.

## Why this matters

Safe reruns make the CLI useful as a launch-readiness drift check.
Teams can confirm the repo still contains the expected baseline files without worrying about template overwrite behavior.

## Good release note wording

When documenting the behavior in a generated repo, prefer language like:

> The launch scaffold was rechecked with `oss-launchpad init` and no baseline files required regeneration.

That keeps the tool framed as a repeatable public-repo hygiene check, not just a one-time bootstrap script.
