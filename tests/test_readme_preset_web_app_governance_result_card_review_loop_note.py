from pathlib import Path


def test_readme_mentions_preset_web_app_governance_result_card_review_loop_note() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")

    assert "docs/PRESET_WEB_APP_GOVERNANCE_RESULT_CARD_REVIEW_LOOP_NOTE.md" in readme
    assert Path("docs/PRESET_WEB_APP_GOVERNANCE_RESULT_CARD_REVIEW_LOOP_NOTE.md").exists()
