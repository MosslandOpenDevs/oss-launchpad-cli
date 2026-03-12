# Preset JSON single-preset export note

If a setup form, chooser, or tiny browser demo only needs one preset at a time, start with a single-preset export before widening the flow.

Recommended first pass:

```bash
python3 -m oss_launchpad_cli.cli presets --preset web-app --json
```

That keeps the first UI/UX slice constrained to one obvious preset, one visible summary, and one reproducible validation lane before broader catalog wiring.
