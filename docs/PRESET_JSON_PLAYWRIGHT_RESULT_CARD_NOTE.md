# Preset JSON result-card Playwright lane

Keep the first exported `web-app` preset proof aligned with one browser-stable form, one primary action, and one reviewable result card before widening demo scope.

## Why it matters

- The JSON preset catalog should stay usable by browser demos without adding multi-screen ambiguity.
- The first proof should be replayable with one form-to-card checkpoint, not a broad navigation story.
- UI wording can expand later, but the first visible result card should stay deterministic.

## Maintainer cue

If preset metadata, README wording, or demo hooks change together, re-check that `presets --json` still describes a form-to-card slice clearly enough for stable browser proof.
