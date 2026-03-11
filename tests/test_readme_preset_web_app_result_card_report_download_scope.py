from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
NOTE = ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_REPORT_DOWNLOAD_SCOPE.md'


def test_readme_mentions_preset_web_app_result_card_report_download_scope() -> None:
    readme = README.read_text(encoding='utf-8')
    assert 'docs/PRESET_WEB_APP_RESULT_CARD_REPORT_DOWNLOAD_SCOPE.md' in readme
    note = NOTE.read_text(encoding='utf-8')
    assert 'one visible result card' in note
    assert 'one report-style download target' in note
