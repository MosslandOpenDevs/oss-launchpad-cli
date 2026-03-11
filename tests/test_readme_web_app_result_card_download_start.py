from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_START.md"


def test_readme_mentions_result_card_download_start_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_START.md" in readme
    assert "form -> result card -> download proof path" in readme


def test_result_card_download_start_note_keeps_scope_small() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "one primary input form" in note
    assert "one reviewable result card" in note
    assert "one obvious download/export action" in note
