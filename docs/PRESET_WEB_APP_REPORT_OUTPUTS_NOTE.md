# Preset web app report outputs note

When the first preset web app slice starts exporting downloadable artifacts, keep the form-to-card path stable and predictable:

- one input form,
- one result card,
- one visible download lane,
- one shared bundle basename for JSON/Markdown/HTML outputs.

That keeps browser proof small enough for step-by-step replay and makes Playwright recovery easier when a flaky download check appears.

Suggested metadata shape for later wiring:

```yaml
report:
  outputs:
    directory: exports/bundles
    output_name: launch-readiness-pack
```

Prefer adding richer paths only after the first result-card proof remains stable.
