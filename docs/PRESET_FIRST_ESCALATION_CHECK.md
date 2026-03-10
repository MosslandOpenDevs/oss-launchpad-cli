# Preset First Escalation Check

Use this guide when a generated scaffold looks healthy at first glance, but the maintainer needs a quick rule for when to escalate the issue instead of making another local tweak.

## Escalate when

- `oss-launchpad init` fails for more than one preset with the same symptom,
- the generated repository is missing proof assets that should come from the selected preset,
- a smoke command fails before any user customization,
- the title or slug inputs produce broken paths or placeholders,
- rerunning `init` changes tracked files unexpectedly.

## Keep the fix local when

- the problem is isolated to one preset,
- the scaffold is complete and only docs need clarification,
- the smoke command reveals a single missing dependency,
- the rerun output is stable.

## Suggested maintainer note

`Escalate preset generation failures that survive one clean rerun or appear in more than one preset path.`
