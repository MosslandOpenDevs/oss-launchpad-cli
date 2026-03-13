from pathlib import Path


def test_readme_mentions_web_app_result_card_validate_export_recheck() -> None:
    readme = Path('README.md').read_text(encoding='utf-8')

    assert 'docs/PRESET_WEB_APP_RESULT_CARD_VALIDATE_EXPORT_RECHECK.md' in readme
