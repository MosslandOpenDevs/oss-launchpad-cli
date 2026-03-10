# Preset Init Rerun Behavior

`oss-launchpad init` is intentionally additive.

If a rendered file already exists in the target directory, the command skips it instead of overwriting local edits. This keeps the scaffold useful after the first run because teams can re-run the command to pick up any still-missing starter assets without clobbering customized files.

## Expected operator workflow

1. Run `oss-launchpad init ...` in an empty or mostly empty directory.
2. Customize the generated README, launch plan, and preset-specific starter assets.
3. Re-run `oss-launchpad init ...` later if you want to backfill files that were deleted or were never generated in the first pass.
4. Review the `Created files:` or `No new files created.` section in the CLI output to confirm what happened.

## Why it matters

This rerun-safe behavior makes the tool friendlier for:

- iterative bootstrap work,
- partial scaffold adoption inside existing repositories,
- and template upgrades where the team wants a visible file-by-file audit before editing by hand.
