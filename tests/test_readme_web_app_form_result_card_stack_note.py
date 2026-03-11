from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "PRESET_WEB_APP_FORM_RESULT_CARD_STACK.md"


def test_readme_mentions_web_app_form_result_card_stack_note() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "docs/PRESET_WEB_APP_FORM_RESULT_CARD_STACK.md" in readme
    assert "form -> result card -> download stack" in readme


def test_web_app_form_result_card_stack_note_keeps_scope_small() -> None:
    note = NOTE.read_text(encoding="utf-8")

    assert "one reviewable result card" in note
    assert "one visible download or handoff target" in note
