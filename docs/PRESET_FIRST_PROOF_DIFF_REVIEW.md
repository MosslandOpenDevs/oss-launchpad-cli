# Preset first proof diff review

Use this note after the generated scaffold has been customized once and you want a tiny review pass before the first public commit.

## Goal

Confirm that the first preset-specific diff shows one believable proof asset and one reproducible check asset without turning into a full roadmap rewrite.

## Review order

1. Open the preset's first proof asset.
2. Open the paired reproducible check asset.
3. Verify the diff still matches the preset story in `README.md`.
4. Verify the proof stays small enough to explain in one commit message.
5. Re-run the preset validation command before push.

## What good looks like

- **ai-agent** — prompt/demo proof plus eval/check evidence.
- **web-app** — landing-page/UI proof plus runnable/demo evidence.
- **python-lib** — API/basic-usage proof plus test evidence.

## Copy-ready review note

`The first preset-specific diff is small, believable, and backed by both a visible proof asset and a reproducible check asset.`
