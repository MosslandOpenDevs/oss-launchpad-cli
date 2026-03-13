from pathlib import Path


def test_readme_mentions_preset_web_app_governance_report_basename_note() -> None:
    root = Path(__file__).resolve().parents[1]
    readme = (root / "README.md").read_text(encoding="utf-8")
    assert "docs/PRESET_WEB_APP_GOVERNANCE_REPORT_BASENAME_NOTE.md" in readme
    assert (root / "docs" / "PRESET_WEB_APP_GOVERNANCE_REPORT_BASENAME_NOTE.md").exists()
