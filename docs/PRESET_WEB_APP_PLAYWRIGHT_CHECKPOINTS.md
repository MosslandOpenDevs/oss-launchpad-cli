# Web-app preset Playwright checkpoints

Use this after the first manual `web-app` UI edit and before widening the demo beyond one form-to-result-card loop.

## Stable checkpoints

1. The landing page renders the primary headline and form.
2. One believable user action submits the form.
3. One result card appears with reviewable proof text.
4. Any download or handoff target is visible from that same card.
5. The smoke/demo script still matches the visible UI proof.

## Keep it narrow

If one checkpoint is flaky, fix the checkpoint before adding another screen, route, or result card.
