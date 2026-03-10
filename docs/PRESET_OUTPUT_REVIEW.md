# Preset output review checklist

Use this quick pass right after `oss-launchpad init ...` prints the scaffold summary.

## 1. Confirm preset identity

- Check `Preset: ...` matches the intended repo type.
- Check `Title slug: ...` matches the public folder or package naming plan.
- For `python-lib`, confirm `Package import path: ...` matches the desired import surface.

## 2. Confirm first proof path

- Review the printed `Smoke command`.
- Review the printed `Validation command`.
- Review the printed `Customize-first command`.

If any command feels surprising, adjust the preset choice or scaffold content before the first public commit.

## 3. Confirm starter assets feel real

Open the printed starter assets and first proof assets before editing random files first.
That keeps the first manual commit tied to the repo's public proof story instead of drifting into generic cleanup.

## 4. Confirm rerun safety

Re-running `oss-launchpad init` on the same target should print `No new files created.` once the scaffold already exists.
Use that behavior as a non-destructive drift check before changing template logic.
