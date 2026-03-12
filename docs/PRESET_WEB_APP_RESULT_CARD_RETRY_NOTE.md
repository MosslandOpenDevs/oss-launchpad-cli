# Preset web-app result-card retry note

Keep the first `web-app` demo honest: if the primary result card is not visible after submit, do not widen the flow.

## UI/UX-first rule

- Keep one form, one submit, and one result card in the same visible lane.
- Use one retry action with explicit copy instead of adding alternate result surfaces.
- Preserve the export/download affordance on the same card after recovery.

## Playwright-stable rule

- Re-check the same primary locator before treating the run as failed.
- Record the retry state with the same result-card assertion, not a looser fallback.
- Recover step-by-step so the next run can replay the same form-to-card path.
