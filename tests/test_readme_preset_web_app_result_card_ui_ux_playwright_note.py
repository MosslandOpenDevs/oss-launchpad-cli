from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppResultCardUiUxPlaywrightNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_result_card_ui_ux_playwright_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_UI_UX_PLAYWRIGHT_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_UI_UX_PLAYWRIGHT_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
