# preset JSON web form start

Use `oss-launchpad presets --json` when a lightweight setup form or browser demo needs preset metadata without scraping human-readable CLI text.

Keep the first UI slice small:

1. load one preset catalog payload
2. render preset label + summary
3. show starter assets and validation command
4. let the user copy the preset-specific next step

This keeps UI work aligned with the existing machine-readable contract before adding richer flows.
