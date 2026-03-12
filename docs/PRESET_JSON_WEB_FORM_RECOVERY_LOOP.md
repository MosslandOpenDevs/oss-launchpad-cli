# Preset JSON web form recovery loop

For the first preset-catalog web form slice, keep the loop boring and reproducible:

1. Load one preset JSON catalog.
2. Fill one form path.
3. Verify one result card.
4. If the UI proof flakes, recover the same path before adding new interactions.

This keeps UI/UX polish and Playwright-style stability checks pointed at the same smallest believable demo.
