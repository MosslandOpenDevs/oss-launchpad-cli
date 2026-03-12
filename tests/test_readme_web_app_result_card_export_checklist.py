from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeWebAppResultCardExportChecklistTests(unittest.TestCase):
    def test_readme_mentions_web_app_result_card_export_checklist(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_CHECKLIST.md", readme)
        self.assertTrue((root / "docs" / "PRESET_WEB_APP_RESULT_CARD_EXPORT_CHECKLIST.md").exists())
