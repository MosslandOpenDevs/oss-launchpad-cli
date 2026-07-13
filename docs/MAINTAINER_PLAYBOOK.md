# Maintainer playbook

The consolidated launch playbook for repositories generated with `oss-launchpad-cli`. It replaces the several hundred single-topic note files that previously lived in this directory; everything still worth keeping is here.

## The proof-first loop

Every launch decision should leave visible evidence. The loop the CLI is built around:

1. **Scaffold once** — `oss-launchpad init <dir> --title "..." --preset <preset>`.
2. **Customize first** — edit the preset starter assets before any generic metadata, so the repo stops looking like a template ([PRESET_CUSTOMIZE_FIRST_GUIDE.md](PRESET_CUSTOMIZE_FIRST_GUIDE.md)).
3. **Prove it** — run the printed smoke command ([PRESET_SMOKE_COMMANDS.md](PRESET_SMOKE_COMMANDS.md)).
4. **Validate, then push** — re-run the printed validation command before every public push; a proof that isn't re-runnable isn't a proof.
5. **Recheck for drift** — rerun `init` any time; it never overwrites and reports what already exists ([INIT_RERUN_GUIDE.md](INIT_RERUN_GUIDE.md)).

Keep the first proof deliberately narrow. For a web-app that means one form, one primary action, one reviewable result card; for an ai-agent one prompt and one deterministic eval; for a python-lib one import path, one smoke test, one usage example. Widen only after the narrow slice is stable.

## What each generated file is for

| File | Job |
| --- | --- |
| `README.md` | Explain the project and the first successful run in under a minute. |
| `LICENSE` | MIT by default — confirm it matches how you intend to publish. |
| `docs/launch-plan.md` | Audience, proof assets, and release scope before going public. |
| `docs/launch-scorecard.md` | Visible readiness checklist for the first announcement. |
| `demo/run_demo.sh` | The reproducible walkthrough; ships as a loud placeholder until replaced. |
| `benchmark/README.md` | Where repeatable evaluation evidence lives. |
| `CHANGELOG.md` / `RELEASE_CHECKLIST.md` | Keep releases auditable from the first tag. |
| `.github/` templates | Issue/PR hygiene from day one. |

Preset starter assets are listed by `oss-launchpad presets` and in the README.

## Web-app UI discipline

Consolidated from the result-card note series; these still apply to any first web demo built from the scaffold:

- One primary call-to-action per screen; secondary actions wait until the first proof is stable.
- A result card should answer "did it work?" at one glance: one status label, one artifact reference, one next step.
- Show a download/export action only after the result it points to actually exists — no dead buttons in the happy path.
- Empty states need one status line, one sentence about what's missing, and one recovery action.
- Keep browser automation (Playwright or similar) pinned to the smallest form -> action -> result-card path before widening coverage; when it flakes, recover by replaying that smallest path first.

## When generation itself misbehaves

If a scaffold looks wrong, rerun `init` once against a clean directory. If the problem survives a clean rerun, or reproduces across more than one preset, file an issue against `oss-launchpad-cli` instead of patching the generated files locally — local patches hide template bugs from every future user.

## Release discipline

- Keep `CHANGELOG.md` in Keep-a-Changelog form; move entries out of `Unreleased` at tag time.
- Scope the first release narrowly and describe it without overselling maturity: name what is proven, not what is planned.
- Before the first tag, walk `RELEASE_CHECKLIST.md` top to bottom and re-run the validation command one last time.
