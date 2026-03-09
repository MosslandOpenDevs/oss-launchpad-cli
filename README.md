# oss-launchpad-cli

CLI toolkit for bootstrapping public open-source projects with strong documentation, reproducibility, and launch readiness.

> Build cleaner public repos faster: README, demo script, benchmark folder, issue/PR templates, and release scaffolding in one flow.

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

Version `0.1.0` will generate:

- `README.md`
- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/pull_request_template.md`
- `benchmark/README.md`
- `demo/run_demo.sh`
- `CHANGELOG.md`
- `RELEASE_CHECKLIST.md`

---

## Example usage

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

oss-launchpad init my-project --title "My Project"
```

---

## Roadmap

### Phase 1
- Baseline scaffold generation
- Template validation
- CLI help and init command

### Phase 2
- Presets by project type (library, CLI, AI agent, web app)
- Better README variants
- Release note templates

### Phase 3
- GitHub metadata generation
- Benchmark skeleton presets
- Demo verification helpers

### Phase 4
- Team-level policy packs
- Template composition system
- Community template registry

---

## Repository structure

```text
oss-launchpad-cli/
├─ src/oss_launchpad_cli/
├─ templates/
├─ docs/
├─ .github/workflows/
└─ README.md
```

---

## License

MIT
