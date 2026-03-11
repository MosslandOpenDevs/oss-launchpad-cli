from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppReportDownloadReviewTests(unittest.TestCase):
    def test_readme_mentions_web_app_report_download_review(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_REPORT_DOWNLOAD_REVIEW.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_REPORT_DOWNLOAD_REVIEW.md").exists())


if __name__ == "__main__":
    unittest.main()
