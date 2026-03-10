# Preset readiness signal

Use this checklist before presenting a preset as ready for first use.

## A preset is ready when
- `oss-launchpad init --preset <name>` generates files without manual patching
- the generated README explains the first command and first edit
- at least one preset-specific doc exists under `docs/`
- tests cover the preset output that differs from the base scaffold

## Release note template
- Preset: `<name>`
- First-run command: `<command>`
- First meaningful edit: `<file>`
- Validation command: `<command>`
