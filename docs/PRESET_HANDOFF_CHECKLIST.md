# Preset handoff checklist

Use this checklist after running `oss-launchpad init` so a fresh scaffold moves from generated files to an actual launch-ready repo.

## AI agent preset

- Confirm `prompts/system.txt` matches the intended operator or product surface.
- Replace placeholder smoke cases in `evals/smoke_cases.jsonl` with at least one real scenario.
- Fill `docs/agent-demo-brief.md` with a realistic demo path.
- Update `docs/launch-scorecard.md` with the first success criteria.

## Web app preset

- Rewrite `docs/landing-page-brief.md` for the real product and audience.
- Review `docs/information-architecture.md` against the first-launch navigation.
- Replace `.env.example` placeholders with real variable names.
- Update the README quickstart with the local dev command you expect people to run first.

## Python library preset

- Rename exported placeholders in `src/<package>/__init__.py` if the starter API is too generic.
- Expand `docs/api-surface.md` with the first public functions or classes.
- Replace `tests/test_smoke.py` assertions with one meaningful library behavior.
- Add a real usage snippet to `examples/basic_usage.py`.

## Final pass

- Run the preset-specific smoke command shown by the CLI.
- Update the generated README with concrete product wording before the first push.
- Keep `RELEASE_CHECKLIST.md` and `docs/launch-plan.md` aligned with the first milestone.
