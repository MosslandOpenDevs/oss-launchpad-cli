from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_readme_mentions_preset_json_result_card_setup_command_alias_note() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "docs/PRESET_JSON_RESULT_CARD_SETUP_COMMAND_ALIAS_NOTE.md" in readme
    note = (ROOT / "docs" / "PRESET_JSON_RESULT_CARD_SETUP_COMMAND_ALIAS_NOTE.md").read_text(encoding="utf-8")
    assert "result_card_setup_command" in note
    assert "oss-launchpad presets --json --preset web-app" in note
