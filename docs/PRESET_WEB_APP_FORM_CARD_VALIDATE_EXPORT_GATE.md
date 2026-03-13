# Web-app form/card validate-export gate

Keep the first believable `web-app` demo intentionally narrow:

1. One preset chooser or setup form
2. One primary submit action
3. One stable result card
4. One visible validation command
5. One visible export/download target

UI/UX rule: the form, result card, and next action should read in one glance.
Playwright rule: verify the same happy path with deterministic input, one state check after submit, and one recovery path if the card does not render.
