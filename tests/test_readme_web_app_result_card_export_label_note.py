from pathlib import Path
import unittest


def test_readme_mentions_web_app_result_card_export_label_note() -> None:
    root = Path(__file__).resolve().parents[1]
    readme = (root / 'README.md').read_text(encoding='utf-8')

    assert 'docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_LABEL_NOTE.md' in readme
    assert (root / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_EXPORT_LABEL_NOTE.md').exists()
