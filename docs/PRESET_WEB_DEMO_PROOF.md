# PRESET_WEB_DEMO_PROOF

This note helps `web-app` preset users show a minimal proof-of-life demo before the first public push.

## Demo proof loop

1. Run `sh demo/run_demo.sh`.
2. Capture the first visible route or landing-state screenshot.
3. Confirm `docs/landing-page-brief.md` still matches the rendered demo.
4. Add one short maintainer note describing what changed since scaffold generation.

## What counts as enough proof

- one runnable local command
- one visible UI state
- one matching doc link for reviewers
- one sentence explaining why the preset is ready for the next change

## Why it exists

A scaffold feels more real when maintainers can point to a single repeatable demo path instead of only static files.
