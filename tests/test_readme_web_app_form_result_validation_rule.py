from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_readme_mentions_web_app_form_result_validation_rule() -> None:
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')

    assert 'docs/PRESET_WEB_APP_FORM_RESULT_VALIDATION_RULE.md' in readme
    assert (ROOT / 'docs' / 'PRESET_WEB_APP_FORM_RESULT_VALIDATION_RULE.md').exists()
