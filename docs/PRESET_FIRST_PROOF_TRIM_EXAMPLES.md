# Preset first proof trim examples

Use this guide when the first manual preset-specific commit is getting too large.

## ai-agent

Keep:

- one prompt improvement in `prompts/system.txt`
- one reproducible proof update in `evals/README.md` or `evals/smoke_cases.jsonl`

Trim for later:

- multi-agent orchestration,
- broad benchmark taxonomy,
- non-essential docs beyond the first demo brief.

## web-app

Keep:

- one landing-page proof update,
- one matching UX or IA checklist refinement.

Trim for later:

- full design systems,
- analytics wiring,
- deployment pipelines.

## python-lib

Keep:

- one API-surface clarification,
- one matching smoke or example usage update.

Trim for later:

- advanced packaging extras,
- release automation,
- broad refactors outside the first user path.

## Rule of thumb

The first believable proof should pair one visible product asset with one reproducible check asset. If the diff needs a roadmap paragraph to defend itself, it is probably too large for the first proof commit.
