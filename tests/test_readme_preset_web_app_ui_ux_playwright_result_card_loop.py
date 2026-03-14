from pathlib import Path


def test_readme_preset_web_app_ui_ux_playwright_result_card_loop() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "PRESET_WEB_APP_UI_UX_PLAYWRIGHT_RESULT_CARD_LOOP.md" in readme
