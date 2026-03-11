from pathlib import Path


def test_readme_mentions_web_app_playwright_stability_loop() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/PRESET_WEB_APP_PLAYWRIGHT_STABILITY_LOOP.md" in readme
    assert "compact Playwright stability loop" in readme
