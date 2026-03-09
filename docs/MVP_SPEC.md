# MVP Spec

## Goal
Generate a clean public repository starter with high-value operational files.

## CLI command

```bash
oss-launchpad init <directory> [--title "Project Title"]
```

## Expected behavior

- create target directory if missing
- create baseline public-repo files
- avoid overwriting existing files unless explicitly forced in future versions
- print a summary of generated files

## Out of scope for MVP

- remote GitHub repo creation
- CI language detection
- advanced template presets
- benchmark execution logic
