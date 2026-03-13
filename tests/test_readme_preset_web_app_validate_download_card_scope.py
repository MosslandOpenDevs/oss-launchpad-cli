from pathlib import Path


def test_readme_mentions_preset_web_app_validate_download_card_scope() -> None:
    text = Path("README.md").read_text(encoding="utf-8")
    assert "docs/PRESET_WEB_APP_VALIDATE_DOWNLOAD_CARD_SCOPE.md" in text
    assert Path("docs/PRESET_WEB_APP_VALIDATE_DOWNLOAD_CARD_SCOPE.md").exists()
