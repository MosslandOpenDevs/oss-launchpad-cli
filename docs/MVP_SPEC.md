# Spec

## Goal

Generate a clean public repository starter with high-value operational files, differentiated by preset.

## CLI surface

```bash
oss-launchpad init <directory> [--title "Project Title"] [--preset <preset-or-alias>]
oss-launchpad presets [--json] [--preset <preset-or-alias>]
oss-launchpad --version
```

## Expected behavior

- create the target directory if missing; fail with a clean error when the path is an existing file
- render the shared base scaffold plus preset-specific starter files
- never overwrite existing files; report skipped files explicitly, classified as customized or untouched via `.oss-launchpad.json` hashes
- warn when the directory was previously scaffolded with a different preset
- print a summary of generated files, starter assets, day-zero docs, and next steps
- resolve documented aliases (for example `library` -> `python-lib`) before rendering
- derive an ASCII title slug and a valid Python import name from `--title`, warning when the slug falls back to `new-project`; control characters in titles are stripped
- leave literal braces in templates untouched (only known context keys are substituted)
- refuse to write through symlinks that escape the target directory
- compile-check rendered `.py` files before writing them

## Out of scope

- remote GitHub repo creation
- CI language detection
- overwrite/force mode
- benchmark execution logic
