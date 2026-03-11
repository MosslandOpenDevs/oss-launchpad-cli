# Preset JSON form label note

When wiring `oss-launchpad presets --json` into a small setup form:

1. show the human preset label, not just the preset key;
2. keep the one-line preset summary visible near the primary action;
3. echo the same label on the first result card so the chosen proof lane stays obvious.

This keeps the JSON export usable for both scripts and human-facing setup flows.
