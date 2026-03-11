# Preset web-app demo script polish

Use this note after the first manual `web-app` scaffold edits when the demo flow needs to feel believable to a public visitor.

## What to verify

1. `demo/run_demo.sh` still runs without extra unpublished setup steps.
2. The script output matches the current `docs/landing-page-brief.md` promise.
3. The README quickstart points to the same first visible user flow as the demo script.
4. The generated demo stays small enough to review in one pass and does not pretend the app is more complete than it is.

## Good first polish moves

- tighten the opening line so the value proposition appears in the first terminal output,
- keep one clear happy path instead of branching into multiple unfinished journeys,
- and pair any new demo copy with one reproducible command or file check.
