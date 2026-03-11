# PRESET_WEB_APP_FIRST_PR_PROOF_LOOP

Use this when a generated `web-app` scaffold needs a small but believable first PR.

## Goal

Keep the first PR anchored to one visible UI asset and one reproducible review artifact.

## Minimal loop

1. Open `docs/landing-page-brief.md` and tighten the primary landing promise.
2. Open `docs/information-architecture.md` and confirm the first happy-path structure still matches the landing promise.
3. Run the generated proof pair:

```bash
sed -n '1,120p' docs/landing-page-brief.md && sed -n '1,120p' docs/information-architecture.md
```

4. In the PR description, state which user-facing promise changed and which review command proves it.

## Why this exists

A `web-app` scaffold feels more real when the first PR updates both the UI promise and the structure behind it, instead of changing a single placeholder file in isolation.
