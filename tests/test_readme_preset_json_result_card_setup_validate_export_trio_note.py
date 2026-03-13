from pathlib import Path


def test_readme_mentions_preset_json_result_card_setup_validate_export_trio_note() -> None:
    readme = Path(__file__).resolve().parents[1] / "README.md"
    assert "docs/PRESET_JSON_RESULT_CARD_SETUP_VALIDATE_EXPORT_TRIO_NOTE.md" in readme.read_text(encoding="utf-8")
