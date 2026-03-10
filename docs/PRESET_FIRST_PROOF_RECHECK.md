# Preset first-proof recheck

Use this after the first manual preset-specific edit, when the scaffold exists but you want one quick pass before committing proof-of-life work.

## Recheck order

1. Open one visible proof asset for the selected preset.
2. Open one reproducible check asset that proves the repo is alive.
3. Make sure both files changed for a believable first diff.
4. Re-run the preset validation command before commit.

## Expected proof pair shape

- `ai-agent` → one prompt/demo asset + one eval/check asset
- `web-app` → one UI/landing asset + one demo/check asset
- `python-lib` → one API/example asset + one test/check asset

## Copy-ready maintainer note

`First proof recheck: visible asset updated, reproducible check updated, validation rerun complete.`
