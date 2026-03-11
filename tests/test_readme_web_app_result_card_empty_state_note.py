from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_EMPTY_STATE_NOTE.md"


def test_readme_mentions_result_card_empty_state_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/PRESET_WEB_APP_RESULT_CARD_EMPTY_STATE_NOTE.md" in readme
    assert "first empty-state result card" in readme


def test_result_card_empty_state_note_keeps_copy_honest() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "one short status label" in note
    assert "Do not fake success metrics" in note
