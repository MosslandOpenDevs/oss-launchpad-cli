# Title slug guide

`oss-launchpad init` derives a `title slug` from `--title` and prints it after scaffold generation.

## Why it matters

The slug feeds multiple generated paths and identifiers:

- Python package folders for the `python-lib` preset
- README placeholders
- demo/project naming cues
- smoke-command output shown after `init`

## Current behavior

- Lowercases the title
- Replaces non-alphanumeric runs with `-`
- Trims leading/trailing `-`
- Falls back to `new-project` if the title contains no slug-safe characters

## Examples

- `My Agent` -> `my-agent`
- `Launchpad CLI!!!` -> `launchpad-cli`
- `***` -> `new-project`

## Why the fallback exists

The fallback keeps scaffold generation deterministic even when a placeholder title is punctuation-only, copied from chat, or intentionally blank-ish.
