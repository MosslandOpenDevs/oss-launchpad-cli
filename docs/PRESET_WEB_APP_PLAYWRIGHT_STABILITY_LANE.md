# Preset web-app Playwright stability lane

Keep the first `web-app` browser proof in a stability-first lane:

1. one form,
2. one result card,
3. one download or handoff artifact,
4. one deterministic replay path.

Do not widen the surface until that narrow slice can be rerun reliably without changing selectors, steps, or evidence expectations.

Use this note together with `docs/PRESET_WEB_APP_PLAYWRIGHT_CHECKPOINTS.md` and `docs/PRESET_WEB_APP_RESULT_CARD_REPRO_CHECK.md` when the first demo proof needs to stay reproducible.
