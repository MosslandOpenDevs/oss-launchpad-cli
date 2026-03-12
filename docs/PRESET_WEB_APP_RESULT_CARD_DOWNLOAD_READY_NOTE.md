# PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_READY_NOTE

Use this note when the first web-app proof already has a form-to-result-card flow and you are about to add a report download action.

## Rule

Show the download action only after the primary result card has a clear validated state, summary copy, and one obvious next step.

## Why

- Keeps the first interaction focused on one happy path.
- Prevents empty or misleading download affordances.
- Fits the one-card-first UI review lane before broader export tooling.

## Fast check

1. Submit the form.
2. Confirm the primary result card renders.
3. Confirm the download action appears with the validated result state, not before.
