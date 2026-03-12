from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppResultCardReportPathTests(unittest.TestCase):
    def test_readme_mentions_web_app_result_card_report_path(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_RESULT_CARD_REPORT_PATH.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_REPORT_PATH.md').exists())


if __name__ == '__main__':
    unittest.main()
