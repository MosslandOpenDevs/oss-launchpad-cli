# Preset web-demo asset check

Use this after `oss-launchpad init <repo> --preset web-app` when the scaffold has been customized and you want a compact proof that the repo already feels demo-ready.

## Check order

1. Open `docs/landing-page-brief.md` and confirm the first-screen promise is still explicit.
2. Run `sh demo/run_demo.sh` and record the exit status.
3. Re-open the demo proof assets that changed first (UI notes, screenshots, HTML export, or README demo section).
4. Keep the first public proof narrow: one visible demo asset plus one reproducible command.

## Minimum believable proof pair

- **Visible proof asset** — landing brief screenshot, GIF, or HTML preview
- **Reproducible check asset** — `sh demo/run_demo.sh`

## Hold conditions

Do not claim the scaffold is ready if:

- the demo script passes but the visible asset is stale,
- the README promises a walkthrough that the demo folder does not support,
- the proof needs more than one manual explanation sentence to be believable.
