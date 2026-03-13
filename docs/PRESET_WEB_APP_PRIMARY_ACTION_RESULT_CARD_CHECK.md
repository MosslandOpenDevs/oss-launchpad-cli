# Web-app preset primary action + result-card check

Keep the first governance-style web demo to one input form, one unmistakable primary action, and one reviewable result card.

UI/UX-first rule: the form should answer one job, the CTA should say what happens next, and the result card should expose the exported proof path without extra navigation.

Playwright-interactive rule: verify the same smallest flow step by step, keep selectors stable, and recover by rerunning the smallest form -> action -> result-card replay before widening the browser surface.
