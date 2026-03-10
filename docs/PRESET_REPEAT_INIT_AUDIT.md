# PRESET_REPEAT_INIT_AUDIT

Use this note when you want to treat a second `oss-launchpad init` run as a safe scaffold audit instead of a rewrite.

## Audit loop

1. Run `oss-launchpad init <dir> --title "..." --preset <preset>` once to create the scaffold.
2. Make a few manual edits that represent the repo's first real customization.
3. Run the same `init` command again.
4. Confirm the CLI prints `No new files created.` when nothing new should be added.
5. Use the printed validation/customize-first/first-PR commands to inspect the scaffold after the rerun.

## Why it helps

- proves the no-overwrite contract stays intact,
- turns repeat init into a quick drift check,
- and gives maintainers a safe audit path before the first public push.

## Pair with

- `docs/INIT_RERUN_GUIDE.md`
- `docs/PRESET_OUTPUT_REVIEW.md`
- `docs/PRESET_VALIDATION_COMMANDS.md`
