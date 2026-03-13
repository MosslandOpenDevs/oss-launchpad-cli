from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_readme_mentions_preset_web_app_result_card_starter_docs_export_note() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "docs/PRESET_WEB_APP_RESULT_CARD_STARTER_DOCS_EXPORT_NOTE.md" in readme
    assert (ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_STARTER_DOCS_EXPORT_NOTE.md").exists()
