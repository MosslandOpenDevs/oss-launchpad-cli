from pathlib import Path


def test_readme_mentions_governance_report_output_title_note() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_TITLE_NOTE.md" in readme


def test_note_mentions_report_output_title_and_ui_playwright_rules() -> None:
    note = Path("docs/PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_TITLE_NOTE.md").read_text(encoding="utf-8")
    assert "report_output_title" in note
    assert "UI/UX-first" in note
    assert "Playwright" in note
