# preset web-app playwright checkpoint sequence

Use this note when the first `web-app` proof needs a stability-first browser pass that stays limited to one form, one result card, and one report/download confirmation.

## Sequence

1. Open the generated `web-app` scaffold and confirm the form renders above the fold.
2. Fill one deterministic path only; avoid mixing exploratory clicks into the proof run.
3. Verify the first result card before checking any download/export affordance.
4. Confirm exactly one report/download action so the replay stays easy to reproduce.
5. If a checkpoint fails, repair that checkpoint first before widening coverage.

## Maintainer reminder

Keep the first Playwright proof reproducible: one scenario, one primary path, one result card, one export check.
