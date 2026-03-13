# oss-launchpad-cli

CLI toolkit for bootstrapping public open-source projects with strong documentation, reproducibility, and launch readiness.

> Build cleaner public repos faster: README, demo script, benchmark folder, issue/PR templates, release scaffolding, and preset-specific starter files in one flow.

If you need the smallest post-generate proof loop, open `docs/PRESET_FIRST_REVIEW_COMMAND_START.md` before widening the preset review surface.
If you need a compact maintainer reminder to keep one generated preset, one review command, and one proof artifact bundle in the same first-pass handoff, open `docs/PRESET_FIRST_PROOF_BUNDLE_HANDOFF_NOTE.md`.

---

## Why this project exists

Recommended maintainer loop: scaffold once, tailor the generated docs immediately, then keep the review commands in the repo so every launch decision leaves visible evidence.


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

Each preset also prints day-zero docs and review commands so maintainers can validate the first proof path before writing more code.
If you need a compact web-app note for keeping the JSON form, result card, and exported proof in one visible stack, open `docs/PRESET_JSON_FORM_RESULT_CARD_STACK.md`.
If you need a compact review loop for one preset JSON form result card before widening the UI flow, open `docs/PRESET_JSON_FORM_RESULT_CARD_REVIEW_NOTE.md`.
If you need a compact chooser note for proving the web-app preset before widening the first UI slice, open `docs/PRESET_WEB_APP_JSON_CHOOSER_NOTE.md`.
If you need a compact reminder to keep the first web-app preset proof limited to one form and one stable result card, open `docs/PRESET_WEB_APP_FORM_CARD_PROOF_NOTE.md`.
If you need a compact UI note for keeping that first proof to one primary action and one reviewable result card, open `docs/PRESET_WEB_APP_ONE_ACTION_RESULT_CARD_NOTE.md`.
If you need a compact UI note for keeping that same first proof anchored to one unmistakable primary CTA before widening the result card, open `docs/PRESET_WEB_APP_PRIMARY_CTA_RULE.md`.
If you need a compact reminder to keep the first web-app proof to one small reviewable result-card slice, open `docs/PRESET_WEB_APP_RESULT_CARD_SMALL_PROOF_NOTE.md`.
If you need a compact preset-catalog reminder for keeping the first `web-app` proof limited to one form, one primary action, and one reviewable result card, open `docs/PRESET_JSON_PLAYWRIGHT_RESULT_CARD_NOTE.md`.
If you need a compact stability rule for keeping that first `web-app` proof to one input form, one primary action, and one stable result card, open `docs/PRESET_WEB_APP_RESULT_CARD_STABILITY_RULE.md`.
If you need a compact stage gate for keeping the first `web-app` proof to one form, one stable result card, and one explicit validation replay, open `docs/PRESET_WEB_APP_RESULT_CARD_STAGE_GATE.md`.
If you need a compact bridge for keeping the first `web-app` result card focused on one validation command plus one export path before widening the demo, open `docs/PRESET_WEB_APP_RESULT_CARD_VALIDATION_EXPORT_BRIDGE.md`.
If you need a compact gate for keeping the first preset JSON chooser tied to one result card plus one explicit download/export path, open `docs/PRESET_JSON_RESULT_CARD_DOWNLOAD_GATE.md`.

If you want the matching UI/UX-first starting note before widening the first web-app preset beyond that one form and one result card, open `docs/PRESET_WEB_APP_UI_UX_START.md`.

Quick chooser:

- `ai-agent` — best when the first believable proof is a prompt, eval, and runnable agent contract.
- `web-app` — best when the first believable proof is a landing flow, UI checklist, and demo script.
- `python-lib` — best when the first believable proof is an importable package, smoke test, and usage example.

If you are deciding which preset matches the first public proof your repo needs, start with `docs/PRESET_SELECTION_GUIDE.md`.
If you need to understand how `--title` becomes the printed slug and generated package path, open `docs/TITLE_SLUG_GUIDE.md`.
If you want to use repeated `init` runs as a safe scaffold drift check, open `docs/INIT_RERUN_GUIDE.md`.
If you want a compact audit loop for verifying the repeat-init no-overwrite contract, open `docs/PRESET_REPEAT_INIT_AUDIT.md`.
If you want to understand the preset-specific smoke command that `init` prints after scaffold generation, open `docs/PRESET_SMOKE_COMMANDS.md`.
If you want an equally short public update after that smoke proof passes, open `docs/PRESET_FIRST_RELEASE_STATUS_LINE.md`.
If you want the generated README to show convincing preset-specific proof assets before the first public push, open `docs/README_PROOF_ASSETS_GUIDE.md`.
If you want a tight checklist for the very first real preset-specific commit after scaffold generation, open `docs/PRESET_FIRST_COMMIT_GUIDE.md`.
If you want a compact proof standard for making that first manual commit feel believable, open `docs/PRESET_FIRST_COMMIT_PROOF.md`.
If you want a short guide for the first preset-specific files to customize, open `docs/PRESET_CUSTOMIZE_FIRST_GUIDE.md`.
If you want the shortest preset-specific proof command to re-run after customizing the scaffold, open `docs/PRESET_VALIDATION_COMMANDS.md`.
If you want a compact note for the smallest validate-then-push loop after the first preset proof edit, open `docs/PRESET_FIRST_PROOF_VALIDATE_THEN_PUSH.md`.
If you want the matching bridge from that validation rerun to the shortest preset progress line, open `docs/PRESET_FIRST_PROOF_VALIDATE_STATUS_BRIDGE.md`.
If you want a one-page "does this scaffold already feel alive?" check before the first public commit, open `docs/PRESET_PROOF_OF_LIFE_CHECKLIST.md`.
If you want the shortest preset-specific proof command to run immediately after scaffold generation, open `docs/PRESET_FIRST_PROOF_COMMANDS.md`.
If you want a compact map of which generated files should become the first believable proof by preset, open `docs/PRESET_FIRST_PROOF_OUTPUTS.md`.
If you want the shortest paired-file review command for the first believable proof, open `docs/PRESET_FIRST_PROOF_REVIEW_COMMAND.md`.
If you want a compact preset-aware rule for pairing one visible proof asset with one reproducible check asset, open `docs/PRESET_FIRST_PROOF_PAIRING.md`.
If you want the shortest preset-by-preset file pair list for that first proof, open `docs/PRESET_FIRST_PROOF_FILE_PAIRS.md`.
If you want a compact day-zero checklist between scaffold generation and the first public push, open `docs/PRESET_DAY_ZERO_CHECKLIST.md`.
If you want the exact doc set to open immediately after `oss-launchpad init`, open `docs/PRESET_DAY_ZERO_DOCS.md`.
If you want a single review command for the first README-plus-proof-file sanity check, open `docs/PRESET_DAY_ZERO_REVIEW_COMMAND.md`.
If you want a compact maintainer handoff checklist after scaffold generation and before the first public push, open `docs/PRESET_HANDOFF_CHECKLIST.md`.
If you want a compact field reference for `oss-launchpad presets --json` before wiring a chooser, open `docs/PRESET_JSON_EXPORT_FIELDS.md`.
If you need a compact reminder to prove one preset with `presets --preset <key> --json` before widening the chooser, open `docs/PRESET_JSON_SINGLE_PRESET_EXPORT_NOTE.md`.
If you need the shortest bridge from `presets --json` to a tiny setup form or browser demo, open `docs/PRESET_JSON_WEB_FORM_START.md`.
If you need a compact stability note for turning that same preset JSON into a reproducible browser-form proof, open `docs/PRESET_JSON_WEB_FORM_PLAYWRIGHT_NOTE.md`.
If you want the shortest bridge between preset JSON UI review rules and Playwright stability rules for the first chooser/result-card slice, open `docs/PRESET_JSON_WEB_FORM_UI_UX_PLAYWRIGHT_BRIDGE.md`.
If you need the matching governance-sandbox-first note for one form -> one primary action -> one result-card demo slice, open `docs/PRESET_JSON_GOVERNANCE_SANDBOX_RESULT_CARD_LANE.md`.
If you need a compact bridge for keeping the first preset chooser, one result card, and one UI/UX-plus-Playwright review lane aligned, open `docs/PRESET_WEB_APP_UI_UX_PLAYWRIGHT_BRIDGE.md`.
If you need the matching compact reminder that the first chooser/result-card slice should keep one explicit validation rerun before any commit/push claim, open `docs/PRESET_WEB_APP_VALIDATE_BEFORE_PUSH_RESULT_CARD_NOTE.md`.
If you need a compact note for keeping governance-aligned preset work behind the same scenario-file -> report-bundle -> preset -> result-card phase order, open `docs/PRESET_JSON_GOVERNANCE_PHASE_ORDER_NOTE.md`.
If you need a compact acceptance note for the first web-app demo slice, open `docs/PRESET_WEB_APP_RESULT_CARD_DEMO_ACCEPTANCE.md`.
If you need a compact stability note for keeping one visible export/download path on that same first result card, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_STABILITY_NOTE.md`.
If you need the shortest recovery-first note for that same preset JSON form/result-card slice, open `docs/PRESET_WEB_APP_RESULT_CARD_RECOVERY_STACK.md`.
If you need a compact maintainer checkpoint for one stable web-app result card plus one export review pass, open `docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_REVIEW_NOTE.md`.
If you need a compact note for the one obvious follow-up action after that first preset form result card, open `docs/PRESET_JSON_FORM_RESULT_CARD_NEXT_STEP.md`.
If you need a compact note for keeping the exported preset `validation_command` visible in that same first setup form or result card, open `docs/PRESET_JSON_VALIDATION_COMMAND_NOTE.md`.
If you need a compact note for keeping the chooser, result card, and export/download proof in one reviewable stack, open `docs/PRESET_JSON_FORM_RESULT_CARD_EXPORT_STACK.md`.
If you need a compact note for keeping the first preset JSON result card tied to one visible export path as well as the validation command, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_PATH_NOTE.md`.
If you need a compact checklist for that same result-card-plus-export checkpoint, open `docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_CHECKLIST.md`.
If you need a compact note for keeping the chooser, result card, and exported validation command path in one reviewable stack, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_COMMAND_PATH_NOTE.md`.
If you need a compact note for keeping the chooser label, validation command, and starter docs visible together on the first result card, open `docs/PRESET_JSON_RESULT_CARD_TRIPLE_PROOF_NOTE.md`.
If you need a tighter UI-first reminder for keeping preset label, validation command, and exported bundle target visible together on that same first result card, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_TRIO_NOTE.md`.
If you need a compact note for keeping the first result card focused on one validation badge plus one export badge, open `docs/PRESET_JSON_RESULT_CARD_VALIDATE_EXPORT_BADGE_NOTE.md`.
If you need a compact gate for keeping that same result card honest before export/download handoff, open `docs/PRESET_JSON_RESULT_CARD_VALIDATE_EXPORT_GATE.md`.
If you need a compact note for keeping the same first result card tied to both a validation command and one export target, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_VALIDATION_NOTE.md`.
If you need a compact note for keeping the chooser, result card, and starter docs visible together on the first preset JSON UI slice, open `docs/PRESET_JSON_RESULT_CARD_TRIPLE_PROOF_NOTE.md`.
If you need a compact note for keeping that same first result card tied to one output slug for the exported setup bundle, open `docs/PRESET_JSON_RESULT_CARD_OUTPUT_SLUG_NOTE.md`.
If you need a shorter note for keeping that same first preset chooser tied to one visible result card plus one obvious download target, open `docs/PRESET_JSON_FORM_RESULT_CARD_DOWNLOAD_NOTE.md`.
If you need a compact proof note for keeping one preset JSON chooser tied to one validation command and one exported setup path, open `docs/PRESET_JSON_CHOOSER_VALIDATION_EXPORT_NOTE.md`.
If you need a compact reminder to keep generated starter docs visible beside the preset label in that same first setup flow, open `docs/PRESET_JSON_STARTER_DOCS_NOTE.md`.
If you need a compact note for keeping the first preset JSON result card tied to one visible setup command as well as one validation command, open `docs/PRESET_JSON_RESULT_CARD_SETUP_COMMAND_NOTE.md`.
If you need a compact owner-facing bridge that keeps the preset label, owner, and visible setup command together on that first result card, open `docs/PRESET_JSON_RESULT_CARD_OWNER_SETUP_COMMAND_NOTE.md`.
If you need a compact owner-facing bridge that keeps the preset label, owner, validation command, and exported setup bundle together on that first result card, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_BUNDLE_OWNER_NOTE.md`.
If you need a compact cue for showing owner-ready status as a visible review badge on that same first result card, open `docs/PRESET_JSON_RESULT_CARD_OWNER_REVIEW_BADGE_NOTE.md`.
If you need a compact cue for showing a single honest progress badge before widening the result-card state machine, open `docs/PRESET_JSON_RESULT_CARD_PROGRESS_BADGE_NOTE.md`.
If you need the matching `web-app` scope gate before widening result-card states, open `docs/PRESET_WEB_APP_RESULT_CARD_PROGRESS_BADGE_GATE.md`.
If you need a compact owner-facing note for keeping exported proof status visible on that same first result card, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_OWNER_STATUS_NOTE.md`.
If you need a compact recheck note before claiming that same owner/export status card is ready to push, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_OWNER_STATUS_RECHECK_NOTE.md`.
If you need a compact follow-up note for keeping preset label, validation command, owner-ready status, and export/download target visible in one first-card stack, open `docs/PRESET_JSON_RESULT_CARD_OWNER_STATUS_STACK_NOTE.md`.
If you want the machine-readable export to keep a shorter `setup_command` alias beside `customize_first_command`, open `docs/PRESET_JSON_SETUP_COMMAND_ALIAS_NOTE.md`.
If you need a compact rule for keeping one preset chooser, one result card, and one validation command visible together in the first browser slice, open `docs/PRESET_JSON_FORM_SINGLE_PROOF_RULE.md`.
If you need the narrowest start for keeping the chosen preset plus validation command visible on that same first result card, open `docs/PRESET_JSON_FORM_RESULT_CARD_VALIDATION_START.md`.
If you need a compact scope note for keeping that first preset JSON browser slice limited to one chooser and one result card, open `docs/PRESET_JSON_FORM_CARD_SCOPE.md`.
If you need the matching handoff note once that first result card is present, open `docs/PRESET_JSON_RESULT_CARD_HANDOFF.md`.
If you need a compact UI copy rule for showing that preset-specific validation command as a visible result-card badge, open `docs/PRESET_JSON_RESULT_CARD_VALIDATION_BADGE.md`.
If you need a compact note for keeping the first web-app result card recovery loop tied to one visible validation badge, open `docs/PRESET_WEB_APP_RESULT_CARD_RECOVERY_BADGE_NOTE.md`.
If you need a compact proof note for keeping one preset chooser, one result card, and one review command visible together, open `docs/PRESET_JSON_RESULT_CARD_PROOF_NOTE.md`.
If you want a one-page "is this already a believable repo?" check before the first manual commit, open `docs/PRESET_FIRST_REPO_CHECK.md`.
If you want a single-page review checklist for the printed preset output before the first manual commit, open `docs/PRESET_OUTPUT_REVIEW.md`.
If you want a preset-by-preset map from generated files to the first believable proof path, open `docs/PRESET_OUTPUT_PROOF_MAP.md`.
If you want a preset-specific checklist for the first real pull request after scaffold generation, open `docs/PRESET_FIRST_PULL_REQUEST.md`.
If you want the shortest scaffold-to-PR order before that checklist, open `docs/PRESET_FIRST_PR_SEQUENCE.md`.
If you want the printed first-PR evidence command explained as a reusable proof pair, open `docs/PRESET_FIRST_PR_EVIDENCE_COMMAND.md`.
If you want the shortest preset-specific file-open commands for the first believable review, open `docs/PRESET_FIRST_REVIEW_COMMANDS.md`.
If you want a compact test for whether the scaffold already feels ready for the first real review, open `docs/PRESET_FIRST_REVIEW_SIGNAL.md`.
If you want to turn preset starter assets into the first believable issue backlog, open `docs/PRESET_FIRST_ISSUE_TRIAGE.md`.
If you want a shorter preset-by-preset map from generated files to the first believable backlog issues, open `docs/PRESET_FIRST_BACKLOG_PROOF.md`.
If you want a one-page proof map for deciding what to verify before the first public release, open `docs/PRESET_FIRST_RELEASE_PROOF.md`.
If you need a single-line pass/fail cue before claiming that release proof publicly, open `docs/PRESET_FIRST_RELEASE_SIGNAL.md`.
If you want a compact note for keeping that first release intentionally narrow and believable, open `docs/PRESET_FIRST_RELEASE_SCOPE_NOTE.md`.
If you want a preset-specific copy-ready release-proof command before the first public tag, open `docs/PRESET_FIRST_RELEASE_COMMANDS.md`.
If you want a preset-by-preset check for the very first believable public proof before pushing the repo, open `docs/PRESET_FIRST_PUBLIC_PROOF_CHECK.md`.
If you want a compact note for describing that first public proof without overselling maturity, open `docs/PRESET_FIRST_PUBLIC_PROOF_NOTE.md`.
If you want the shortest scaffold-to-proof order before the first public push, open `docs/PRESET_FIRST_PUBLIC_PROOF_SEQUENCE.md`.
If you want the shortest preset-aware path from fresh scaffold to first believable proof, open `docs/PRESET_FIRST_PROOF_SEQUENCE.md`.
If you want a compact decision rule for picking the first believable proof pair by preset, open `docs/PRESET_FIRST_PROOF_DECISION.md`.
If you want a short paired-file command for proof review before the first public push, use the printed proof-review command after `init`.
If you want a quick "does this preset already feel alive?" pass immediately after scaffold generation, open `docs/PRESET_FIRST_RUN_SIGNALS.md`.
If you want the shortest path from first preset-specific edit to a believable proof artifact, open `docs/PRESET_FIRST_CUSTOM_PROOF.md`.
If you want a copy-ready maintainer progress update right after scaffold generation, open `docs/PRESET_FIRST_MAINTAINER_UPDATE.md`.
If you want a shorter owner-specific first-proof progress note, open `docs/PRESET_FIRST_PROOF_OWNER_UPDATE.md`.
If you want a 30-second owner-ready audit before posting that first proof update, open `docs/PRESET_FIRST_PROOF_OWNER_READY_CHECK.md`.
If you want a compact UI-first proof loop for `web-app` scaffolds, open `docs/PRESET_WEB_APP_UI_PROOF_LOOP.md`.
If you need a compact checkpoint note for keeping the first `web-app` proof aligned to intro-first UI/UX and one reproducible Playwright result-card pass, open `docs/PRESET_WEB_APP_UI_UX_PLAYWRIGHT_CHECKPOINT.md`.
If you want the shortest UI/UX review handoff before widening that first `web-app` slice, open `docs/PRESET_WEB_APP_UI_HANDOFF_RULES.md`.
If you want a compact Playwright stability loop before widening that first `web-app` proof slice, open `docs/PRESET_WEB_APP_PLAYWRIGHT_STABILITY_LOOP.md`.
If you need a one-screen rule for keeping that first web-app proof limited to one form, one submit, and one result card, open `docs/PRESET_WEB_DEMO_FORM_RESULT_STABILITY.md`.
If you need a compact checkpoint order for that same first web-app Playwright proof lane, open `docs/PRESET_WEB_APP_PLAYWRIGHT_CHECKPOINT_SEQUENCE.md`.
If you need a compact Playwright recovery checklist for that same first web-app proof lane, open `docs/PRESET_WEB_APP_PLAYWRIGHT_RECOVERY.md`.
If you need a compact rule for keeping the first preset chooser, one visible result card, and one exported report path together before expanding the demo, open `docs/PRESET_JSON_RESULT_CARD_REPORT_PATH_NOTE.md`.
If you need a compact maintainer note for validating that same web-app form -> result-card -> export path before push, open `docs/PRESET_WEB_APP_RESULT_CARD_VALIDATE_EXPORT_NOTE.md`.
If you need a shorter form-to-card recovery note before reopening broader demo scope, open `docs/PRESET_WEB_APP_FORM_TO_CARD_RECOVERY_NOTE.md`.
If you need an even shorter reminder to keep that same proof narrowed to one form, one result card, and one recovery step, open `docs/PRESET_WEB_APP_FORM_RESULT_RECOVERY_NOTE.md`.
If you need a compact rule for keeping the first web-app proof tied to one form, one result card, and one downloadable artifact bundle, open `docs/PRESET_WEB_APP_RESULT_CARD_BUNDLE_CHECK.md`.
If you need a compact UI/UX plus Playwright reminder for keeping the first web-app demo limited to one form, one submit, one stable result card, and one validation/export proof, open `docs/PRESET_WEB_APP_FORM_CARD_VALIDATE_EXPORT_GATE.md`.
If you need a compact proof note for keeping the first web-app slice to one form, one primary action, one stable result card, and one visible proof cue, open `docs/PRESET_WEB_APP_FORM_RESULT_PROOF_NOTE.md`.
If you need a compact handoff for one web-app form submit plus one visible result card plus one exported artifact, open `docs/PRESET_WEB_APP_FORM_RESULT_EXPORT_NOTE.md`.
If you need a compact owner-ready note for the first believable web-app result card before widening scope, open `docs/PRESET_WEB_APP_RESULT_CARD_OWNER_READY_NOTE.md`.
If you need a compact copy-order cue for that same form -> result-card -> export slice, open `docs/PRESET_WEB_APP_FORM_CARD_EXPORT_STATUS_ORDER.md`.
If you need a compact result-card cue that keeps the chosen preset, validation command, and export-ready state visible together, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_STATUS_NOTE.md`.
If you need a compact reminder to keep the first preset chooser/result-card slice tied to one export-ready validation status before widening the UI, open `docs/PRESET_JSON_RESULT_CARD_VALIDATE_EXPORT_STATUS_NOTE.md`.
If you need a compact maintainer reminder for the required five-line short report across the active repos, open `docs/PRESET_FIVE_REPO_SHORT_REPORT_NOTE.md`.
If you need a compact maintainer reminder to keep repo 4 visibly active while repo 5 stays scenario/report-first, open `docs/PRESET_REPO_FOUR_ACTIVE_WITH_REPO_FIVE_PHASE_ONE_NOTE.md`.
If you need the matching preset note for five-repo runs, open `docs/PRESET_FIVE_REPO_COMMIT_GATE_NOTE.md` to keep one-line repo status plus validation-first commit/push claims.
If you need a compact maintainer note for validating one small preset or README slice before push, open `docs/PRESET_VALIDATE_SMALL_SLICE_NOTE.md`.
If you need a short maintainer cue that keeps the first web-app UI/UX slice paired with one reproducible Playwright-style proof, open `docs/PRESET_WEB_APP_UI_UX_PLAYWRIGHT_STATUS_NOTE.md`.
If you need a compact scope reminder for keeping the first web-app preset demo limited to one form, one result card, one validation command, and one downloadable proof path, open `docs/PRESET_WEB_APP_VALIDATE_DOWNLOAD_CARD_SCOPE.md`.

If you need a compact bridge for keeping the first web-app chooser, one result card, and one exported bundle path visible together, open `docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_BRIDGE.md`.

If you want a compact maintainer check that keeps the first web-app result card paired with one reopened report artifact, open `docs/PRESET_WEB_APP_REPORT_DOWNLOAD_REVIEW.md`.
If you need a compact maintainer note for pairing one generated preset review command with one proofable starter-doc edit before push, open `docs/PRESET_REVIEW_COMMAND_PROOF_PAIR_NOTE.md`.

If you need a shorter scope card for that same form-to-result-card bundle lane, open `docs/PRESET_WEB_APP_RESULT_CARD_BUNDLE_SCOPE.md`.
If you need a quick polish pass for the generated `web-app` demo script after the first manual edits, open `docs/PRESET_WEB_APP_DEMO_SCRIPT_POLISH.md`.
If you need the shortest UI-first proof path before that polish pass, open `docs/PRESET_WEB_APP_UI_PROOF_START.md`.
If you want a compact check for keeping the first result card tied to explicit download or replay targets, open `docs/PRESET_WEB_APP_DOWNLOAD_CARD_CHECK.md`.
If you need a compact bridge from exported preset JSON into a first form submit plus visible result card, open `docs/PRESET_JSON_WEB_FORM_START.md`.
If you need a compact reminder to keep that same preset-JSON proof tied to one visible export action, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_START.md`.
If you need a compact reminder to keep preset JSON labels visible inside that same first setup form and result card, open `docs/PRESET_JSON_FORM_LABEL_NOTE.md`.
If you need a compact note for keeping that same preset JSON result card tied to one explicit export or copy target, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_NOTE.md`.
If you need a shorter pass/hold cue for whether that same result card is already export-ready, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_READY_NOTE.md`.
If you need a compact cue for keeping preset summary, validation command, and generated path hints visible on that same first result card, open `docs/PRESET_JSON_RESULT_CARD_PATHS_NOTE.md`.
If you need a shorter reminder to keep the validation command and export target visible together on that same first result card, open `docs/PRESET_JSON_RESULT_CARD_VALIDATION_AND_EXPORT_NOTE.md`.
If you need a compact note for keeping that same result card tied to one explicit export or copy target that names the generated path handoff, open `docs/PRESET_JSON_FORM_RESULT_CARD_EXPORT_PATH_NOTE.md`.
If you need a compact cue for keeping the preset `validation_command` visible on that same first result card before widening the demo, open `docs/PRESET_JSON_RESULT_CARD_VALIDATION_COMMAND_NOTE.md`.
If you need a compact rule for keeping the first preset chooser limited to one form, one result card, and one explicit next-step artifact, open `docs/PRESET_JSON_FORM_ONE_FLOW_RULE.md`.
If you need a compact reminder to keep the first JSON form anchored to one exported preset catalog, open `docs/PRESET_JSON_FORM_PRESET_CATALOG_NOTE.md`.
If you need a short copy-focused review before polishing that first preset JSON result card, open `docs/PRESET_JSON_RESULT_CARD_COPY_NOTE.md`.
If you need a compact note for keeping a preset summary description visible on the same first result card as the validation command, open `docs/PRESET_JSON_RESULT_CARD_DESCRIPTION_NOTE.md`.
If you need the quickest field-order scan before polishing that same first result card, open `docs/PRESET_JSON_RESULT_CARD_SCAN_START.md`.
If you need a shorter guardrail for keeping that same preset-JSON flow tied to one result card plus one downloadable bundle, open `docs/PRESET_JSON_RESULT_CARD_ONE_BUNDLE_NOTE.md`.
If you want a shorter first-pass checklist for the first manual `web-app` UI edit, open `docs/PRESET_WEB_APP_UI_FIRST_PASS.md`.
That pass should stay UI-first: keep the landing brief, information architecture, checklist, and demo script aligned before widening scope or polishing secondary screens.
If you want a one-card review note once the first web demo proof is visible, open `docs/PRESET_WEB_DEMO_RESULT_CARD.md`.
If the starter proof specifically changes the first input form plus the first result card, open `docs/PRESET_WEB_DEMO_FORM_RESULT_STABILITY.md` before widening the demo surface.
If you need a short reminder to stabilize that first result-card slice before adding more UI states, open `docs/PRESET_WEB_APP_RESULT_CARD_STABILITY_NOTE.md`.
If you want a faster guardrail for keeping the first visible `web-app` proof limited to one believable result card, open `docs/PRESET_WEB_APP_FIRST_RESULT_CARD_CHECK.md`.
If you need a compact reminder to keep the first web-app result card tied to one proofable user action, open `docs/PRESET_WEB_APP_RESULT_CARD_ONE_ACTION_RULE.md`.
If you want a compact landing-brief + information-architecture proof loop for the first `web-app` PR, open `docs/PRESET_WEB_APP_FIRST_PR_PROOF_LOOP.md`.
If you want the narrowest believable web-app proof before expanding scope, open `docs/PRESET_WEB_APP_FORM_TO_CARD_LOOP.md`.
If you need a compact stack note for keeping that same first web-app proof limited to one form, one result card, and one reproducible handoff, open `docs/PRESET_WEB_APP_FORM_TO_CARD_STACK.md`.
If you need the narrowest form -> result card -> download stack reminder before widening the demo scope, open `docs/PRESET_WEB_APP_FORM_RESULT_CARD_STACK.md`.
If you need a smaller form -> result card -> report handoff reminder before widening that first web-app slice, open `docs/PRESET_WEB_APP_FORM_RESULT_STACK_NOTE.md`.
If you need a compact UI handoff rule card once that first `web-app` proof exists, open `docs/PRESET_WEB_APP_UI_HANDOFF_RULES.md`.
If you need a shorter audit for whether one visible `web-app` result card still forms an honest UI proof, open `docs/PRESET_WEB_APP_RESULT_CARD_UI_AUDIT.md`.
If you need a quick wording review for the first visible `web-app` result card before widening scope, open `docs/PRESET_WEB_APP_RESULT_CARD_COPY_REVIEW.md`.
If you need a compact state cue for showing whether that first result-card proof is actually passing, open `docs/PRESET_WEB_APP_RESULT_CARD_STATUS_BADGE.md`.
If you need a quick wording review for the first visible `web-app` result card before widening scope, open `docs/PRESET_WEB_APP_RESULT_CARD_COPY_REVIEW.md`.
If you need a smaller copy-only guardrail before touching layout or flow, open `docs/PRESET_WEB_APP_RESULT_CARD_COPY_GUARD.md`.
If you need a compact note for keeping the first `web-app` proof scoped to one visible result instead of a fake multi-screen launch claim, open `docs/PRESET_WEB_APP_UI_SCOPE_NOTE.md`.
If you need a compact cue for keeping that first result card centered on one obvious primary action, open `docs/PRESET_WEB_APP_RESULT_CARD_PRIMARY_ACTION_NOTE.md`.
If you need a compact rule for keeping that first visible result tied to one obvious download/export action, open `docs/PRESET_WEB_APP_RESULT_CARD_ONE_DOWNLOAD_RULE.md`.
If you need a shorter scope cue that keeps one form, one result card, and one obvious primary path together, open `docs/PRESET_WEB_APP_RESULT_CARD_ONE_PRIMARY_PATH.md`.
If you need a compact rule for keeping the first web-app result card tied to one reproducible export target, open `docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_RULE.md`.
If you need a compact rule for keeping the first generated web-app proof tied to one visible form, one result card, and one validation command, open `docs/PRESET_WEB_APP_FORM_RESULT_VALIDATION_RULE.md`.
If you need a compact stack note for keeping that same first web-app result card tied to one validation cue plus one export cue, open `docs/PRESET_WEB_APP_RESULT_CARD_VALIDATION_EXPORT_STACK.md`.
If you need a compact UI/UX-first rule for keeping the first generated web-app result card limited to one visible primary action and one supporting validation cue, open `docs/PRESET_WEB_APP_RESULT_CARD_PRIMARY_FLOW_RULE.md`.
If you need a compact note for keeping the first web-app result card paired with one export path and one printed validation command, open `docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_COMMAND_NOTE.md`.
If you need the narrowest start for a web-app result card that shows both the validation command and export target in one glance, open `docs/PRESET_WEB_APP_RESULT_CARD_VALIDATE_EXPORT_START.md`.
If you need a compact review note for keeping that same first result card tied to one visible setup command, one validation command, and one export target, open `docs/PRESET_WEB_APP_RESULT_CARD_COMMAND_STACK_NOTE.md`.
If you need a compact check that the first `web-app` result card still exposes one believable download or handoff target, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_CHECK.md`.
If you need a compact note for keeping the first report-download button tied to a validated result-card state before adding more actions, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_READY_NOTE.md`.
If you need a slightly fuller UI-first scope note for the same one-form -> one-result-card -> one-download proof, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_BLUEPRINT.md`.
If you need a short audit that keeps the first generated `web-app` proof scoped to one form, one result card, and one export target, open `docs/PRESET_WEB_APP_FORM_RESULT_EXPORT_CHECK.md`.
If you need the shortest `web-app` form -> result card -> download proof path before a wider demo pass, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_START.md`.
If you want the shortest note for keeping one preset JSON export aligned with one starter form and one result card, open `docs/PRESET_JSON_FORM_RESULT_CARD_NOTE.md`.
If you need a compact scope note for keeping that same proof limited to one form, one result card, and one download action, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_SCOPE_NOTE.md`.
- `docs/PRESET_WEB_APP_RESULT_CARD_REPORT_DOWNLOAD_SCOPE.md` — keep one visible report download tied to the same primary result card.
If you need the shortest UI/UX-first + Playwright-stable stack for that same first visible proof, open `docs/PRESET_WEB_APP_RESULT_CARD_PROOF_STACK.md`.
If you need a short maintainer-ready note once that first result card is believable, open `docs/PRESET_WEB_APP_RESULT_CARD_HANDOFF.md`.
If you need a compact map of the machine-readable fields exposed by `oss-launchpad presets --json`, open `docs/PRESET_METADATA_EXPORT_FIELDS.md`.
That JSON export now keeps a stable `preset_key` plus a human label and one-line preset summary beside each preset so scripts, docs, and UI pickers can explain the proof lane without hard-coding copy.
If you want the shortest start note before wiring that JSON into a script, UI, or review bot, open `docs/PRESET_JSON_EXPORT_START.md`.
If you need the most compact UI-first note for that same preset JSON handoff, open `docs/PRESET_JSON_UI_START.md`.
If you only need one preset payload for a picker or script, open `docs/PRESET_JSON_SINGLE_PRESET_NOTE.md`.
If you need a compact reminder to keep one visible owner beside that preset JSON in a picker or setup form, open `docs/PRESET_JSON_OWNER_NOTE.md`.
If you need a compact UI note for keeping preset label, validation command, and owner visible together on the same first result card, open `docs/PRESET_JSON_RESULT_CARD_OWNER_VALIDATION_NOTE.md`.
If you need a compact reminder to keep that same preset JSON result card paired with one visible owner handoff, open `docs/PRESET_JSON_RESULT_CARD_OWNER_NOTE.md`.
If you need a compact note for keeping preset owner, summary, and validation command visible together on that same first result card, open `docs/PRESET_JSON_RESULT_CARD_OWNER_SUMMARY_NOTE.md`.
If you need a compact note for keeping preset owner, starter docs, and validation command visible together on that same first result card, open `docs/PRESET_JSON_RESULT_CARD_OWNER_STARTER_DOCS_NOTE.md`.
If you need a smaller scope note for keeping that preset JSON browser slice limited to one form and one result card, open `docs/PRESET_JSON_FORM_CARD_SCOPE.md
- Preset JSON result-card handoff: `docs/PRESET_JSON_RESULT_CARD_HANDOFF.md`
`.

If you need a short reviewer note for why that JSON export exists at all, open `docs/PRESET_JSON_EXPORT_REVIEW_NOTE.md`.
If you need a compact first-pass note before widening a web-app preset into a larger UI proof loop, open `docs/PRESET_WEB_APP_UI_PROOF_START.md`.
If you need a UI/UX-first scope note before widening that first web-app slice, open `docs/PRESET_WEB_APP_UI_UX_START.md`.
If you need stable browser-proof checkpoints for that first web-app form-to-result-card slice, open `docs/PRESET_WEB_APP_PLAYWRIGHT_CHECKPOINTS.md`.
If you need a compact stability-first reminder for that same browser lane, open `docs/PRESET_WEB_APP_PLAYWRIGHT_STABILITY_NOTE.md`.
If you need a compact reminder to keep that first browser proof in a stability-first lane before widening scope, open `docs/PRESET_WEB_APP_PLAYWRIGHT_STABILITY_LANE.md`.
If you need the matching checkpoint rule for one form, one result card, and one reproducible demo proof, open `docs/PRESET_WEB_APP_FORM_CARD_CHECKPOINT.md`.
If you need a tiny recovery note for rerunning that first form-to-result-card proof after a flaky browser step, open `docs/PRESET_WEB_APP_PLAYWRIGHT_RECOVERY_NOTE.md`.
If you need a quick asset checklist before calling that first web-app result-card slice reviewable, open `docs/PRESET_WEB_DEMO_ASSET_CHECK.md`.
If you need a compact handoff note for generated web-app demos that should end in one report-style result card plus downloadable artifacts, open `docs/PRESET_WEB_APP_REPORT_CARD_HANDOFF.md`.
If you need a compact bridge from one preset chooser submit to one report-style result card plus one downloadable artifact, open `docs/PRESET_WEB_APP_RESULT_CARD_REPORT_PATH.md`.
If you need a shorter pre-share check that keeps that same first result card tied to one report-ready download, open `docs/PRESET_WEB_APP_RESULT_CARD_REPORT_READY_NOTE.md`.
If you need a compact bridge between the generated web-app result card and the first maintainer-facing status line, open `docs/PRESET_WEB_APP_RESULT_CARD_STATUS_BRIDGE.md`.
If you need a compact gate for deciding whether the first result card plus export path is really download-ready, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_GATE.md`.
If you need a one-line maintainer update once that first web-app result card is believable, open `docs/PRESET_WEB_APP_RESULT_CARD_STATUS_LINE.md`.
If you need the same update to keep one download target visible, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_STATUS_LINE.md`.
If you need a compact owner-ready note for the first web-app result card plus one visible download target, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_OWNER_NOTE.md`.
If you need a one-line check that the first preset JSON export is already usable as a proof bundle, open `docs/PRESET_JSON_EXPORT_PROOF_BUNDLE_NOTE.md`.
If you need a compact UI note for keeping preset label, validation command, and generated starter-doc handoff visible in one first result card, open `docs/PRESET_JSON_RESULT_CARD_STARTER_DOCS_NOTE.md`.
If you need a compact UI/UX-first note for keeping one primary action, one validation command, and one download target visible on that same first web-app result card, open `docs/PRESET_WEB_APP_RESULT_CARD_VALIDATION_HUD_NOTE.md`.
If you need a compact rule for keeping the first web-app result card centered on one primary action with reproducible validation and download labels, open `docs/PRESET_WEB_APP_RESULT_CARD_PRIMARY_ACTION_RULE.md`.
If you need a tiny signoff check once that first web-app result card is believable, open `docs/PRESET_WEB_APP_RESULT_CARD_SIGNOFF.md`.
If you need the shortest review loop for that same form -> result card -> download slice, open `docs/PRESET_WEB_APP_RESULT_CARD_REVIEW_START.md`.
If you need a short guardrail for keeping that first web-app proof reproducible across form input, result card, and download handoff, open `docs/PRESET_WEB_APP_RESULT_CARD_REPRO_CHECK.md`.
If you need a compact UI/UX-first note for keeping the first generated web-app result card scannable before widening the demo, open `docs/PRESET_WEB_APP_RESULT_CARD_SCAN_NOTE.md`.
If you need a compact UI/UX-first note for keeping the first generated web-app result card scannable in one glance, open `docs/PRESET_WEB_APP_RESULT_CARD_ONE_GLANCE_NOTE.md`.
If you need a quick label-focused scan before sharing that first result card proof, open `docs/PRESET_WEB_APP_RESULT_CARD_LABEL_CHECK.md`.
If you need a compact copy cue for the first empty-state result card before real demo data exists, open `docs/PRESET_WEB_APP_RESULT_CARD_EMPTY_STATE_NOTE.md`.
If you need a quick scan for whether the generated web-app result card keeps input summary, primary status, and one download target above the fold, open `docs/PRESET_WEB_APP_RESULT_CARD_ABOVE_FOLD_CHECK.md`.
If you need a compact bridge note for keeping that same first web-app result card aligned with the UI/UX intro-first lane and the first Playwright proof, open `docs/PRESET_WEB_APP_RESULT_CARD_UI_UX_PLAYWRIGHT_NOTE.md`.
If you need the same review as a compact field-by-field scan, open `docs/PRESET_WEB_APP_RESULT_CARD_FIELD_SCAN.md`.
If you need a compact naming cue for keeping the first web-app report download tied to one visible result-card basename, open `docs/PRESET_WEB_APP_REPORT_BASENAME_NOTE.md`.
If you want a compact file-open order before the first real web-app UI edit, open `docs/PRESET_WEB_APP_STARTER_REVIEW.md`.
If you need a compact evidence ladder for deciding whether that first web-app proof is visible enough to share, open `docs/PRESET_WEB_DEMO_PROOF.md`.
If the first web-app proof needs a form-first readiness audit before widening scope, open `docs/PRESET_WEB_APP_FORM_READINESS_CHECK.md`.
If you need a compact one-action guardrail before widening that same form-to-result-card proof, open `docs/PRESET_WEB_APP_ONE_ACTION_CHECK.md`.
If you need the shortest `presets --json --preset web-app` handoff before wiring one setup form and one result card, open `docs/PRESET_JSON_WEB_APP_SINGLE_PRESET_NOTE.md`.
If you need the same single-preset JSON handoff with one visible owner and one download-ready result card, open `docs/PRESET_JSON_SINGLE_PRESET_OWNER_NOTE.md`.
If you need a compact UI handoff for keeping one web-app chooser tied to one visible primary action and one reviewable result card, open `docs/PRESET_WEB_APP_ONE_ACTION_RESULT_CARD_NOTE.md`.

If you want the shortest preset-aware command for turning generated proof assets into the first backlog issue draft, use the new first-issue command printed by `oss-launchpad init`.
If you want the shortest preset-by-preset first-proof progress sentence, open `docs/PRESET_FIRST_PROOF_STATUS_LINE.md`.
If you want a compact set of honest names for that first believable proof pair, open `docs/PRESET_FIRST_PROOF_LABELS.md`.
If you want the shortest paired-file command for checking whether that first proof update is ready to post, use the new first proof status command printed by `oss-launchpad init`.
If you want a compact audit for whether those paired files already form a believable first proof bundle, open `docs/PRESET_FIRST_PROOF_BUNDLE_CHECK.md`.
If you want a compact pass/fail check before claiming that sentence publicly, open `docs/PRESET_FIRST_PROOF_STATUS_CHECK.md`.
If you want the shortest preset-aware issue draft checklist after that first proof, open `docs/PRESET_FIRST_ISSUE_CHECKLIST.md`.
If you want a commit message pattern for that first believable manual proof, open `docs/PRESET_FIRST_PROOF_COMMIT_MESSAGE.md`.
If you want a last-pass check for whether the first proof pair is actually convincing instead of merely present, open `docs/PRESET_FIRST_PROOF_MARGIN_CHECK.md`.
If you want a compact rule for keeping the first proof believable without inflating it into a whole-roadmap commit, open `docs/PRESET_FIRST_PROOF_BOUNDARY.md`.
If you want a quick diff-focused pass after the first preset-specific manual edit, open `docs/PRESET_FIRST_PROOF_DIFF_CHECK.md`.
If you want a compact pre-commit diff review for that first believable proof, open `docs/PRESET_FIRST_PROOF_DIFF_REVIEW.md`.
If you want a compact audit to confirm that the generated scaffold already shows one believable proof asset plus one reproducible check asset, open `docs/PRESET_FIRST_PROOF_AUDIT.md`.
If you want a fast README-to-proof sanity check before the first public commit, open `docs/PRESET_FIRST_PROOF_LINK_CHECK.md`.
If you want a one-line note for keeping that first proof push honest and reviewable, open `docs/PRESET_FIRST_PROOF_PUSH_NOTE.md`.
If you want a short pass/hold cue for whether the first proof already feels believable, open `docs/PRESET_FIRST_PROOF_STATUS_SIGNAL.md`.
If you want a one-line status cue before describing the first public repo push, open `docs/PRESET_FIRST_REPO_PUSH_STATUS_LINE.md`.
If you want a one-page maintainer review between scaffold generation and the first manual commit, open `docs/PRESET_FIRST_PROOF_MAINTAINER_REVIEW.md`.
If you want a one-page signal for whether those proof assets are already convincing enough to show publicly, open `docs/PRESET_FIRST_PROOF_READY_SIGNAL.md`.
If you want a shorter checklist for whether the first preset proof is already believable enough to show, open `docs/PRESET_FIRST_PROOF_READY_CHECK.md`.
If you want a compact sequence for reviewing the generated proof pair before the first manual commit, open `docs/PRESET_FIRST_PROOF_REVIEW_SEQUENCE.md`.
If you need a quick pass/hold exit card before that first believable proof commit, open `docs/PRESET_FIRST_PROOF_REVIEW_EXIT.md`.
If you need a quick rule for deciding what belongs in that first believable proof commit versus what should wait, open `docs/PRESET_FIRST_PROOF_KEEP_OR_TRIM.md`.
If you want concrete preset-by-preset examples of what to keep in that first believable proof commit versus what to defer, open `docs/PRESET_FIRST_PROOF_TRIM_EXAMPLES.md`.
If you want a compact rule for what the first believable proof artifact bundle should contain, open `docs/PRESET_FIRST_PROOF_ARTIFACT_BUNDLE.md`.
If you want a shorter naming note for keeping that first proof bundle easy to reopen across human and machine artifacts, open `docs/PRESET_FIRST_PROOF_BUNDLE_ALIAS_NOTE.md`.
If you want a compact guardrail for keeping the first manual proof commit small and believable, open `docs/PRESET_FIRST_PROOF_SCOPE_CHECK.md`.
If you want a one-line preset-aware update that keeps the first proof claim honest about scope, open `docs/PRESET_FIRST_PROOF_SCOPE_STATUS_LINE.md`.
If you want a short post-ready check before describing or pushing that first believable proof, open `docs/PRESET_FIRST_PROOF_POST_CHECK.md`.
If you want a last-pass checklist before turning that first believable proof into the first public repo push, open `docs/PRESET_FIRST_PROOF_REPO_PUSH_CHECK.md`.
If you need a shortest-possible repo-push test, use `docs/PRESET_FIRST_PROOF_REPO_PUSH_CHECK.md` to confirm one visible proof asset, one reproducible check asset, honest launch docs, and a still-reviewable first public diff.
The CLI next steps also print a preset-specific first-PR evidence command so maintainers can immediately open the two proof files most likely to anchor the first reviewable diff.
If you need a compact boundary for the first form-to-result-card slice, open `docs/PRESET_WEB_APP_FORM_RESULT_CARD_SCOPE.md`.

If you need the matching small-slice review loop for one result card, one export action, and one validation pass, open `docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_REVIEW_LOOP.md`.

## Local validation loop

Before shipping doc or scaffold changes, run the CLI smoke tests locally:

```bash
python3 -m unittest tests/test_cli.py
```

That keeps README claims, generated scaffold output, and printed next-step guidance aligned.
If you want a compact README-first checklist for new launch scaffolds, open `docs/README_TEMPLATE_CHECKLIST_NOTE.md`.

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

The init output now also prints a title slug, the `python-lib` package import path, a preset-specific smoke command, preset-specific starter assets to customize first, preset-specific proof assets to capture first, a preset-specific proof-review command, a preset-specific first-issue command, a preset-specific first-release command, and preset-aware next steps so the generated scaffold can be turned into a real launch checklist immediately. Those next steps explicitly point maintainers to `docs/launch-plan.md` and `docs/launch-scorecard.md`, which act as repo-included launch handoff artifacts instead of leaving launch readiness as an implied TODO. For a copy-ready, preset-scoped public update after the first generated proof passes, use `docs/PRESET_FIRST_PROOF_STATUS_RULES.md`.

If you need the shortest preset-first reminder before wiring exported preset JSON into a starter web form or result card, open `docs/PRESET_JSON_FORM_BOOTSTRAP_NOTE.md`.

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
- First issue handoff checklist → `docs/PRESET_FIRST_ISSUE_CHECKLIST.md`

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


## First-proof audit

Before the first public demo or launch artifact, use `docs/first-proof-audit.md` to confirm the proof asset, smoke command, and day-zero docs still line up.


## Preset discovery

```bash
PYTHONPATH=src python3 -m oss_launchpad_cli.cli presets
```

Use this to compare starter assets before choosing `ai-agent`, `web-app`, or `python-lib`.


## Web-app preset proof loop

For UI-first starter repos, pair `docs/PRESET_WEB_APP_UI_PROOF_LOOP.md` with `docs/PRESET_WEB_DEMO_RESULT_CARD.md` before the first public demo so the landing-page proof path, result card, and smoke command evidence stay aligned.
If you want a shorter pre-demo check that the first web-app form still resolves into one reviewable result card, open `docs/PRESET_WEB_APP_FORM_RESULT_CARD_CHECK.md`.
If you want a compact proof note for that same first form-to-result slice, open `docs/PRESET_WEB_APP_FORM_RESULT_PROOF.md`.
If you want a quick audit before widening that same slice, open `docs/PRESET_WEB_APP_FORM_RESULT_AUDIT.md`.


If you need a short acceptance note for when that first form -> result card slice is actually reviewable, open `docs/PRESET_WEB_APP_RESULT_CARD_ACCEPTANCE.md`.
If you need a compact acceptance note for keeping one form path tied to one visible result card plus one report affordance, open `docs/PRESET_WEB_DEMO_RESULT_CARD_ACCEPTANCE.md`.


- `docs/CLI_DRY_RUN_SUMMARY_NOTE.md`

If you need a short note for keeping the first web-app result-card proof tied to one report/download target, open `docs/PRESET_WEB_APP_RESULT_CARD_REPORT_HANDOFF.md`.

If you need a short note for keeping the first web-app result card tied to one exported report file, open `docs/PRESET_WEB_APP_RESULT_CARD_REPORT_FILE_NOTE.md`.


If you need a short note for preserving `report_author` / `report_authors` fields in preset JSON exports, open `docs/PRESET_JSON_REPORT_AUTHOR_ALIAS_NOTE.md`.
If you need a compact web-demo-first reminder for keeping one preset form, one result card, and one export target in the same replayable slice, open `docs/PRESET_JSON_WEB_FORM_RESULT_STACK_NOTE.md`.
If you need a compact note for keeping one subtitle visible under the same preset JSON result-card title, open `docs/PRESET_JSON_RESULT_CARD_SUBTITLE_NOTE.md`.
If you need a compact note for keeping one short subject visible in that same preset JSON result-card header, open `docs/PRESET_JSON_RESULT_CARD_SUBJECT_NOTE.md`.

If you need a compact UI note for keeping one result card tied to one report/download proof stack, open `docs/PRESET_WEB_APP_RESULT_CARD_REPORT_STACK.md`.
If you need a compact UI note for keeping one web-app preset result card tied to one visible starter-doc handoff plus one download-ready proof target, open `docs/PRESET_WEB_APP_RESULT_CARD_STARTER_DOCS_NOTE.md`.
If you need a compact reminder to keep one primary CTA tied to one visible result card, open `docs/PRESET_WEB_APP_PRIMARY_CTA_RESULT_CARD_NOTE.md`.

If you need a compact UI note for keeping the first web-app result card focused on one primary CTA plus one secondary download action, open `docs/PRESET_WEB_APP_PRIMARY_CTA_NOTE.md`.
If you need a compact export check for keeping that same result card tied to one downloadable artifact after the first pass, open `docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_NOTE.md`.
If you need a compact UI note for keeping one obvious download target on that same first result card, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_NOTE.md`.
If you need a compact UI note for keeping that same first result card limited to one clear status plus one obvious download handoff, open `docs/PRESET_WEB_APP_RESULT_CARD_ONE_STATUS_ONE_DOWNLOAD_NOTE.md`.
If you need a short status-first reminder for that same result card export lane, open `docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_STATUS_NOTE.md`.
If you need a compact scope note for keeping that same result card tied to one report download, open `docs/PRESET_WEB_APP_RESULT_CARD_REPORT_DOWNLOAD_SCOPE.md`.
If you need the machine-readable export to keep one obvious `primary_action` for a chooser or result card, open `docs/PRESET_JSON_PRIMARY_ACTION_NOTE.md`.
If you need one compact note for keeping the first result card limited to one validated status line plus one export path, open `docs/PRESET_JSON_RESULT_CARD_STATUS_EXPORT_NOTE.md`.
If you need the matching web-app reminder to keep the first download/export button tied to one rerunnable validation loop, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_VALIDATE_NOTE.md`.
If you need a compact UI note for keeping one visible download/export badge beside that same primary status, open `docs/PRESET_JSON_RESULT_CARD_DOWNLOAD_BADGE_NOTE.md`.
If you need one compact note for keeping the first result card tied to setup command, validation command, and one export path together, open `docs/PRESET_JSON_RESULT_CARD_COMMAND_EXPORT_STACK_NOTE.md`.
If you need a matching note for making the first result-card status unmistakable before adding more actions, open `docs/PRESET_WEB_APP_RESULT_CARD_PRIMARY_STATUS.md`.
If you need a compact note for keeping the first download badge readable beside that same result-card status, open `docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_STATUS_BADGE.md`.

If you want a compact maintainer note for choosing from the exported preset catalog without reopening template files, open `docs/PRESET_JSON_CATALOG_OWNER_NOTE.md`.

If you need the same recovery posture condensed to one preset-catalog form -> one result card replay loop, open `docs/PRESET_JSON_WEB_FORM_RECOVERY_LOOP.md`.

If you need a compact bootstrap note for the first web-app demo slice, open `docs/PRESET_JSON_WEB_FORM_FIRST_BOOT_NOTE.md` and start from `oss-launchpad presets --preset web-app --json` before widening the form -> result-card -> export flow.


If you want a compact preset-catalog note for the first believable UI slice, open `docs/PRESET_JSON_FIRST_UI_SLICE_NOTE.md`.

If you need a compact retry note for keeping the first web-app form -> result-card lane recoverable without widening the UI, open `docs/PRESET_WEB_APP_RESULT_CARD_RETRY_NOTE.md`.

If you need a compact result-card export ordering cue for preset JSON flows, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_READY_STACK.md`.

If you need a compact handoff for keeping the first web-app result card tied to one report-style next action, open `docs/PRESET_WEB_APP_RESULT_CARD_REPORT_HANDOFF.md`.
If you need a compact UI proof rule for keeping the first web preset form limited to one primary action, one status card, and one download path, open `docs/PRESET_WEB_APP_PRIMARY_ACTION_RULE.md`.

If you need a compact note for keeping that same first result card tied to one visible export bundle owner handoff, open `docs/PRESET_JSON_RESULT_CARD_EXPORT_BUNDLE_OWNER_HANDOFF_NOTE.md`.

If you need a compact note for keeping the first web-app preset proof limited to one form, one primary action, and one result card, open `docs/PRESET_WEB_APP_ONE_FORM_ONE_CARD_NOTE.md`.
- Web-app result-card recovery loop note: `docs/PRESET_WEB_APP_RESULT_CARD_RECOVERY_LOOP.md`

If you need a compact rule for keeping the first `web-app` result card focused on one visible validation command plus one export target, open `docs/PRESET_WEB_APP_RESULT_CARD_COMMAND_EXPORT_RULE.md`.

If you need a compact proof reminder that repo 4 and repo 5 stay mandatory in every five-repo pass, open `docs/PRESET_FIRST_PROOF_REPO_FOUR_FIVE_RULE.md`.
If you need the matching one-line status reminder for repo 4 and repo 5 before any commit/push claim, open `docs/PRESET_FIVE_REPO_REPO45_ONE_LINE_GATE_NOTE.md`.
If you need the matching validation-first reminder for repo 4 and repo 5 inside that same five-repo pass, open `docs/PRESET_FIVE_REPO_FOUR_FIVE_VALIDATE_NOTE.md`.

If you need a compact bridge from preset JSON export to one owner-facing result card, open `docs/PRESET_JSON_RESULT_CARD_OWNER_QUEUE_NOTE.md`.

- `docs/PRESET_WEB_APP_PLAYWRIGHT_STEP_CHECK.md` — keep web-app browser proof scoped to one stable step-by-step form-to-card loop.
