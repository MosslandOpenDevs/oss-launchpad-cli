from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppReportCardHandoffTests(unittest.TestCase):
    def test_readme_mentions_report_card_handoff(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_REPORT_CARD_HANDOFF.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_REPORT_CARD_HANDOFF.md").exists())


if __name__ == "__main__":
    unittest.main()
