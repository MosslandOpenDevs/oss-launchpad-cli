# oss-launchpad-cli

CLI toolkit for bootstrapping public open-source projects with strong documentation, reproducibility, and launch readiness.

> Build cleaner public repos faster: README, demo script, benchmark folder, issue/PR templates, release scaffolding, and preset-specific starter files in one flow.

---

## Why this project exists

Many open-source repositories fail early for reasons that have nothing to do with code quality:

- unclear README structure,
- missing demo flow,
- weak issue/PR hygiene,
- no benchmark layout,
- inconsistent release notes.

`oss-launchpad-cli` focuses on the boring but high-leverage parts of shipping a public repository well.

---

## What it generates today

Version `0.1.0` generates a launch-ready baseline scaffold:

- `README.md`
- `.editorconfig`
- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/pull_request_template.md`
- `benchmark/README.md`
- `demo/run_demo.sh`
- `docs/launch-plan.md`
- `docs/launch-scorecard.md`
- `CHANGELOG.md`
- `RELEASE_CHECKLIST.md`

It now also adds preset-differentiated starter assets so the repo feels useful before the first manual commit:

- `ai-agent` → `prompts/system.txt`, `evals/README.md`, `evals/smoke_cases.jsonl`, `docs/agent-demo-brief.md`
- `web-app` → `.env.example`, `docs/ui-ux-checklist.md`, `docs/landing-page-brief.md`, `docs/information-architecture.md`
- `python-lib` → `pyproject.toml`, `src/<package>/__init__.py`, `tests/test_smoke.py`, `examples/basic_usage.py`, `docs/api-surface.md`
- all presets → `docs/launch-plan.md` so maintainers capture audience, proof assets, and release scope before going public

---

## Project presets

Current presets:

- `ai-agent`
- `web-app`
- `python-lib`

Each preset keeps the same public-repo scaffold, but changes the README framing, setup guidance, and starter files so the generated repository feels more specific on day one.
If you are deciding which preset matches the first public proof your repo needs, start with `docs/PRESET_SELECTION_GUIDE.md`.
If you need to understand how `--title` becomes the printed slug and generated package path, open `docs/TITLE_SLUG_GUIDE.md`.
If you want to use repeated `init` runs as a safe scaffold drift check, open `docs/INIT_RERUN_GUIDE.md`.
If you want to understand the preset-specific smoke command that `init` prints after scaffold generation, open `docs/PRESET_SMOKE_COMMANDS.md`.
If you want the generated README to show convincing preset-specific proof assets before the first public push, open `docs/README_PROOF_ASSETS_GUIDE.md`.
If you want a tight checklist for the very first real preset-specific commit after scaffold generation, open `docs/PRESET_FIRST_COMMIT_GUIDE.md`.
If you want the shortest preset-specific proof command to re-run after customizing the scaffold, open `docs/PRESET_VALIDATION_COMMANDS.md`.
If you want a one-page "does this scaffold already feel alive?" check before the first public commit, open `docs/PRESET_PROOF_OF_LIFE_CHECKLIST.md`.

## Local validation loop

Before shipping doc or scaffold changes, run the CLI smoke tests locally:

```bash
python3 -m unittest tests/test_cli.py
```

That keeps README claims, generated scaffold output, and printed next-step guidance aligned.

---

## Example usage

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

oss-launchpad init my-agent --title "My Agent" --preset ai-agent
oss-launchpad init my-webapp --title "My Web App" --preset web-app
oss-launchpad init my-library --title "My Library" --preset python-lib
```

The init output now also prints a title slug, the `python-lib` package import path, a preset-specific smoke command, preset-specific starter assets to customize first, preset-specific proof assets to capture first, and preset-aware next steps so the generated scaffold can be turned into a real launch checklist immediately. Those next steps explicitly point maintainers to `docs/launch-plan.md` and `docs/launch-scorecard.md`, which act as repo-included launch handoff artifacts instead of leaving launch readiness as an implied TODO.

### Generated tree

```text
my-project/
├─ README.md
├─ CONTRIBUTING.md
├─ CHANGELOG.md
├─ RELEASE_CHECKLIST.md
├─ benchmark/
│  └─ README.md
├─ demo/
│  └─ run_demo.sh
└─ .github/
   ├─ ISSUE_TEMPLATE/
   │  ├─ bug_report.md
   │  └─ feature_request.md
   └─ pull_request_template.md
```

### Why the output is more convincing than a bare repo

- the README starts with a project-specific tagline,
- setup guidance is preset-aware,
- demo and benchmark folders exist from day one,
- contribution and release files are already in place,
- `.editorconfig` gives the repo a consistent text-formatting baseline before the first manual edit,
- preset-specific files make the first repo-specific commit easier to shape,
- init now prints a preset-specific smoke command so the maintainer knows the first proof step immediately.
- rerunning `init` against an existing scaffold keeps files untouched and prints `No new files created.` so teams can treat repeat runs as a safe drift check instead of a destructive rewrite.

### Example smoke commands printed by `init`

- `ai-agent` → `python3 -m json.tool evals/smoke_cases.jsonl >/dev/null || head -n 3 evals/smoke_cases.jsonl`
- `web-app` → `sh demo/run_demo.sh && sed -n '1,40p' docs/landing-page-brief.md`
- `python-lib` → `PYTHONPATH=src python3 -m unittest tests/test_smoke.py && python3 examples/basic_usage.py`

---

## Long-term Project Direction

This project is intended as a long-lived public infrastructure tool for open-source launches.

### 1) Reproducibility first

Every generated repository should be easier to clone, understand, run, and evaluate.

### 2) Documentation as product surface

README, examples, benchmarks, contribution docs, and release notes are treated as first-class outputs.

### 3) Opinionated but extensible

The default scaffolding should be useful out of the box, while still allowing teams to customize templates later.

### 4) Public-repo operating discipline

This project should help maintainers create repositories that are easy for strangers to trust.
That means:

- strong first impression,
- explicit setup steps,
- validation guidance,
- contributor affordances,
- clean release habits.

### 5) Sustainable maintenance

The CLI should remain small, auditable, and easy to extend. Prefer incremental template evolution over heavy platform complexity.

---

## MVP scope

Version `0.1.0` focuses on:

- baseline scaffold generation,
- preset-aware README/setup rendering,
- preset-specific starter file generation,
- no-overwrite initialization,
- CLI help and init flow,
- validation through automated tests.

---

## Repository structure

```text
oss-launchpad-cli/
├─ src/oss_launchpad_cli/
├─ templates/
├─ tests/
├─ docs/
├─ .github/workflows/
└─ README.md
```

---

## License

MIT
