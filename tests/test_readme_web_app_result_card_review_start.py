from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_REVIEW_START.md"


def test_readme_mentions_web_app_result_card_review_start() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/PRESET_WEB_APP_RESULT_CARD_REVIEW_START.md" in readme


def test_web_app_result_card_review_start_keeps_review_order() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "docs/PRESET_WEB_APP_FORM_READINESS_CHECK.md" in note
    assert "docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_START.md" in note
    assert "docs/PRESET_WEB_APP_PLAYWRIGHT_STABILITY_LANE.md" in note
