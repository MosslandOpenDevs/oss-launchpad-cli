# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.0] - 2026-07-13

### Added

- `--version` flag.
- Generated scaffolds now include a `LICENSE` (MIT, rendered with the current year) and a `.gitignore`.
- Generated `CHANGELOG.md` is seeded in Keep-a-Changelog form with the generation date.
- `init` reports skipped existing files (`Skipped N existing file(s)`), making the no-overwrite contract visible.
- `init` warns when a non-ASCII title falls back to the generic `new-project` slug; accented titles are transliterated (`Café Über` -> `cafe-uber`).
- Titles that would produce an invalid Python package name (for example `3D Render Kit`) now get a valid `pkg_`-prefixed import path instead of an unimportable one.
- `init` records scaffold state in `.oss-launchpad.json` (generator version, preset, title, per-file hashes); reruns classify skipped files as customized or untouched, and warn when the directory was previously scaffolded with a different preset.
- Rendering refuses to write through symlinks that resolve outside the target directory, and compile-checks rendered `.py` files before writing.
- Titles containing quotes no longer produce syntactically invalid generated Python (code-context templates now use slug/package placeholders); control characters in titles are stripped.
- `init` reports a clean error instead of a traceback when the target path is an existing file.
- Repo-level test suite rebuilt around CLI behavior: scaffolding, rendering integrity, alias resolution, JSON schema, and generated projects passing their own printed validation commands.

### Changed

- **Packaging fix**: templates moved into the package (`src/oss_launchpad_cli/templates/`) and registered as package data — non-editable installs (`pip install .`, wheels) previously crashed on every `init` because templates were not shipped.
- **Template rendering** switched from `str.format` to substitution of known context keys only; literal braces (JSON, shell `${VAR}`, CI `${{ ... }}`) in templates no longer crash rendering.
- `presets --json` now returns a versioned envelope (`schema_version`, `presets`, `aliases`) and drops the duplicated synonym keys of the 0.1.x export; see `docs/PRESET_JSON_EXPORT_FIELDS.md` for the migration map.
- Preset aliases curated from ~40 accreted names down to a documented set of 13; `--help` now shows the three canonical presets instead of a 40+ item choices list.
- ai-agent smoke/validation now validates `evals/smoke_cases.jsonl` line-by-line (`json.tool --json-lines` via stdin), so adding a second eval case no longer breaks the command.
- web-app smoke/validation invokes the demo script with `bash` (it uses `pipefail`, which `sh` on Debian/Ubuntu rejects).
- python-lib smoke command repeats `PYTHONPATH=src` for the example step, which previously failed with `ModuleNotFoundError`.
- Generated python-lib project: distribution name uses the hyphenated slug, version is single-sourced from `__init__.__version__`, and the smoke test is a real `unittest.TestCase` (it previously collected zero tests under the printed `unittest` command).
- Generated `demo/run_demo.sh` now prints an explicit PLACEHOLDER warning instead of passing silently.
- `init` next steps no longer reference documents that are not part of the generated scaffold.
- CI now tests against a Python matrix and installs the built package non-editable before running the scaffold smoke test.

### Removed

- 425 near-duplicate note files in `docs/` (consolidated into `docs/MAINTAINER_PLAYBOOK.md` and the seven remaining guides).
- 336 test files that asserted README prose instead of CLI behavior.
- The README's accumulated 300+ note-link lines; the README now documents the tool itself.

## [0.1.0]

### Added

- Initial release: `init` and `presets` commands, `ai-agent` / `web-app` / `python-lib` presets, base public-repo scaffold.
