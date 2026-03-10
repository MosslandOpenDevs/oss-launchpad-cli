# Preset web-app UI proof loop

Use this after `oss-launchpad init ... --preset web-app` when you want the first UI-facing commit to feel reviewable instead of decorative.

1. Update `docs/landing-page-brief.md` with the real hero, CTA, and happy-path task.
2. Mirror those decisions in `docs/ui-ux-checklist.md` so the UX check is tied to an actual screen promise.
3. Re-run `sh demo/run_demo.sh` and keep the output proofable from the README path.
4. Review `docs/information-architecture.md` before widening scope beyond the first landing flow.
