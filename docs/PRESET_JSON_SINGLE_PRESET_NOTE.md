# Preset JSON single-preset note

Use `oss-launchpad presets --json --preset <name>` when a script or UI only needs one preset payload instead of the full catalog.

- Good for preset pickers that lazy-load detail on selection.
- Keeps JSON fixtures smaller during review and browser-demo work.
- Re-run `python3 -m unittest tests/test_cli.py` after changing preset metadata.
