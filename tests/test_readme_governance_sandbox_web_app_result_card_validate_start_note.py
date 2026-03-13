from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_readme_mentions_governance_sandbox_web_app_result_card_validate_start_note() -> None:
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    assert 'docs/GOVERNANCE_SANDBOX_WEB_APP_RESULT_CARD_VALIDATE_START_NOTE.md' in readme
    assert (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_WEB_APP_RESULT_CARD_VALIDATE_START_NOTE.md').exists()
