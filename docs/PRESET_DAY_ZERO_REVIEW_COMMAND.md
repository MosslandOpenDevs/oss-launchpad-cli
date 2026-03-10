# Preset day-zero review command

After `oss-launchpad init`, open one high-signal generated overview file plus one preset-specific proof file.

## Command pattern

- `ai-agent` → `sed -n '1,120p' README.md && sed -n '1,120p' docs/agent-demo-brief.md`
- `web-app` → `sed -n '1,120p' README.md && sed -n '1,120p' docs/landing-page-brief.md`
- `python-lib` → `sed -n '1,120p' README.md && sed -n '1,120p' examples/basic_usage.py`

## Why this exists

This keeps the first review anchored on:

1. the repo story the public will see first, and
2. the preset-specific proof file that should make the scaffold feel alive.

Use it before the first manual commit if you want a fast sanity check that the generated scaffold already looks believable.
