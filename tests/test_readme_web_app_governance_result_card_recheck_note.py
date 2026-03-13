from pathlib import Path


def test_readme_mentions_web_app_governance_result_card_recheck_note() -> None:
    readme = Path('README.md').read_text(encoding='utf-8')

    assert 'docs/PRESET_WEB_APP_GOVERNANCE_RESULT_CARD_RECHECK_NOTE.md' in readme


def test_web_app_governance_result_card_recheck_note_mentions_governance_alignment() -> None:
    doc = Path('docs/PRESET_WEB_APP_GOVERNANCE_RESULT_CARD_RECHECK_NOTE.md').read_text(encoding='utf-8')

    assert 'one form' in doc
    assert 'one primary action' in doc
    assert 'result card' in doc
    assert 'governance-sandbox' in doc
