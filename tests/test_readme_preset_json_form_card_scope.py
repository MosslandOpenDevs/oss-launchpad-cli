from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "PRESET_JSON_FORM_CARD_SCOPE.md"


def test_readme_mentions_preset_json_form_card_scope_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/PRESET_JSON_FORM_CARD_SCOPE.md" in readme


def test_preset_json_form_card_scope_keeps_first_slice_small() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "one preset picker or starter form" in note
    assert "one reviewable result card" in note
    assert "one obvious next action" in note
