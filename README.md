# oss-launchpad-cli

CLI toolkit for bootstrapping public open-source projects with strong documentation, reproducibility, and launch readiness.

> Build cleaner public repos faster: README, LICENSE, demo script, benchmark folder, issue/PR templates, release scaffolding, and preset-specific starter files in one flow.

Many repositories fail early for reasons unrelated to code quality: unclear README, missing demo flow, weak issue/PR hygiene, inconsistent release notes. `oss-launchpad-cli` handles those boring but high-leverage parts, so the first public commit already looks intentional.

## Quickstart

Requires Python 3.10+.

```bash
pip install .            # or: pip install -e . for development
oss-launchpad init my-project --title "My Project" --preset python-lib
cd my-project
```

`init` prints the generated files, the starter assets to customize first, and preset-specific smoke/validation commands so you can prove the scaffold works before writing more code.

It is also safe to rerun: existing files are never overwritten, and each run records the scaffold state in `.oss-launchpad.json` (preset, title, per-file hashes) so reruns report which generated files you customized and which are untouched — a real drift check. See [docs/INIT_RERUN_GUIDE.md](docs/INIT_RERUN_GUIDE.md).

## Presets

| Preset | Best when the first believable proof is... | Preset starter assets |
| --- | --- | --- |
| `ai-agent` | a prompt, eval, and runnable agent contract | `prompts/system.txt`, `evals/README.md`, `evals/smoke_cases.jsonl`, `docs/agent-demo-brief.md` |
| `web-app` | a landing flow, UI checklist, and demo script | `.env.example`, `docs/ui-ux-checklist.md`, `docs/landing-page-brief.md`, `docs/information-architecture.md`, `demo/run_demo.sh` |
| `python-lib` | an importable package, smoke test, and usage example | `pyproject.toml`, `src/<package>/__init__.py`, `tests/test_smoke.py`, `examples/basic_usage.py`, `docs/api-surface.md` |

All presets share the same base scaffold: `README.md`, `LICENSE` (MIT), `CONTRIBUTING.md`, `CHANGELOG.md`, `RELEASE_CHECKLIST.md`, `.gitignore`, `.editorconfig`, issue/PR templates, `benchmark/README.md`, `demo/run_demo.sh`, and `docs/launch-plan.md` / `docs/launch-scorecard.md`.

Accepted aliases: `agent` → `ai-agent`; `app`, `site`, `website`, `frontend`, `landing`, `landing-page`, `showcase`, `web-demo`, `governance-demo`, `dao-demo` → `web-app`; `lib`, `library` → `python-lib`.

## Machine-readable preset metadata

```bash
oss-launchpad presets            # human-readable summary
oss-launchpad presets --json     # versioned envelope for scripts and UI pickers
oss-launchpad presets --preset web-app --json
```

Field reference and 0.1.x migration notes: [docs/PRESET_JSON_EXPORT_FIELDS.md](docs/PRESET_JSON_EXPORT_FIELDS.md).

## Documentation

- [docs/MVP_SPEC.md](docs/MVP_SPEC.md) — scope and expected CLI behavior
- [docs/PRESET_SELECTION_GUIDE.md](docs/PRESET_SELECTION_GUIDE.md) — choosing a preset
- [docs/PRESET_CUSTOMIZE_FIRST_GUIDE.md](docs/PRESET_CUSTOMIZE_FIRST_GUIDE.md) — the first files to edit after `init`
- [docs/PRESET_SMOKE_COMMANDS.md](docs/PRESET_SMOKE_COMMANDS.md) — what each printed smoke command proves
- [docs/PRESET_DAY_ZERO_CHECKLIST.md](docs/PRESET_DAY_ZERO_CHECKLIST.md) — between `init` and the first public push
- [docs/INIT_RERUN_GUIDE.md](docs/INIT_RERUN_GUIDE.md) — rerunning `init` as a drift check
- [docs/MAINTAINER_PLAYBOOK.md](docs/MAINTAINER_PLAYBOOK.md) — the consolidated launch playbook
- [docs/PRESET_JSON_EXPORT_FIELDS.md](docs/PRESET_JSON_EXPORT_FIELDS.md) — `presets --json` field reference

## Development

```bash
pip install -e .
python3 -m unittest discover -s tests
```

Templates live in `src/oss_launchpad_cli/templates/` (packaged with the wheel). Rendering substitutes known `{placeholder}` keys only, so literal braces (JSON, shell, CI syntax) are safe, and rendered `.py` files are compile-checked before being written.

## Roadmap

Next minor version explores readiness *checking*, not just generation: `audit` (first-stranger readiness of an existing repo), `fix --dry-run` (proposed changes as a diff), and `verify` (run the repo's declared proof commands). `init` stays as the bootstrap path.

## License

MIT — see [LICENSE](LICENSE).
