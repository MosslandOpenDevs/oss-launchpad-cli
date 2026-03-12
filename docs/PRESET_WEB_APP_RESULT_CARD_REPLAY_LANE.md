# Preset Web App Result Card Replay Lane

When extending the `web-app` preset, keep the first proof loop narrow:

1. one form,
2. one primary action,
3. one reviewable result card,
4. one replayable validation command.

## Why this lane matters

- It matches the UI-first starter promise in the preset catalog.
- It keeps the first browser automation target stable before secondary routes appear.
- It gives maintainers a single visible artifact to review during day-zero setup.

## Preferred proof bundle

- `docs/landing-page-brief.md`
- `docs/ui-ux-checklist.md`
- `demo/run_demo.sh`
- one short replay command or smoke command in README/docs
