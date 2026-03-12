from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
NOTE = ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_PRESET_LABEL_NOTE.md'


def test_readme_mentions_preset_web_app_result_card_preset_label_note() -> None:
    readme = README.read_text(encoding='utf-8')
    assert 'docs/PRESET_WEB_APP_RESULT_CARD_PRESET_LABEL_NOTE.md' in readme
    note = NOTE.read_text(encoding='utf-8')
    assert 'selected preset label' in note
    assert 'one primary status' in note
