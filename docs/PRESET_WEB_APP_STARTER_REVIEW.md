# web-app starter review

Use this note right after `oss-launchpad init <dir> --preset web-app` and before the first UI implementation.

Review order:

1. `README.md` — confirm the repo promise matches the first visible product proof
2. `docs/landing-page-brief.md` — confirm the headline, audience, and primary action stay aligned
3. `docs/information-architecture.md` — confirm the first screen only carries the pages and cards you can actually prove
4. `docs/ui-ux-checklist.md` — confirm the happy-path checks match the first visible flow
5. `demo/run_demo.sh` — confirm there is still one reproducible proof command

Why this exists:

- keeps UI scope honest before secondary screens expand
- keeps the README promise tied to one believable first proof
- gives maintainers a compact review lane before Playwright or demo-polish work begins
