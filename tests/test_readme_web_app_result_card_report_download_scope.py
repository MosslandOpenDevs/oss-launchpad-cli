from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppResultCardReportDownloadScopeTests(unittest.TestCase):
    def test_readme_mentions_result_card_report_download_scope(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_RESULT_CARD_REPORT_DOWNLOAD_SCOPE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_REPORT_DOWNLOAD_SCOPE.md').exists())


if __name__ == '__main__':
    unittest.main()
