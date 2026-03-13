from pathlib import Path


def test_readme_mentions_web_app_result_card_report_ready_note() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")

    assert "docs/PRESET_WEB_APP_RESULT_CARD_REPORT_READY_NOTE.md" in readme
