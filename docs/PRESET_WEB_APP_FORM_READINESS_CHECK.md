# Preset web-app form readiness check

Use this before expanding a generated `web-app` scaffold beyond the first form and result-card loop.

## Ready when

- the landing-page brief names one primary form action
- the first visible result card is tied to that same action
- the demo script still proves the happy path without extra setup narration
- the UI checklist mentions one success state and one obvious failure state

## Hold when

- the first PR claims multiple screens without one believable form proof
- the result card is not yet tied to a concrete submit/download/handoff action
- the demo script and docs disagree on the first proof path

## Fast review command

```bash
sed -n '1,120p' docs/landing-page-brief.md && sed -n '1,120p' docs/ui-ux-checklist.md && sed -n '1,120p' demo/run_demo.sh
```
