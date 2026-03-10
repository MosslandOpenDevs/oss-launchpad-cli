# Preset first repo check

Use this checklist right after `oss-launchpad init ...` and before the first manual commit.

## First repo check

1. Open the generated `README.md` and verify the tagline sounds specific to the preset.
2. Run the preset smoke command printed by `init`.
3. Open the two proof files most likely to support the first review.
4. Add one repo-specific sentence to `docs/launch-plan.md` so the scaffold stops feeling generic.
5. Confirm rerunning `init` would be safe because the initial scaffold is already committed or reviewed.

## Pass condition

The scaffold passes this check when a stranger could clone the repo and immediately see:

- what the project is,
- what proof of life exists,
- and what the first believable next step should be.
