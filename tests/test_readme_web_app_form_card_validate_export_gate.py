from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppFormCardValidateExportGateTests(unittest.TestCase):
    def test_readme_mentions_web_app_form_card_validate_export_gate(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_FORM_CARD_VALIDATE_EXPORT_GATE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_WEB_APP_FORM_CARD_VALIDATE_EXPORT_GATE.md').exists())


if __name__ == '__main__':
    unittest.main()
