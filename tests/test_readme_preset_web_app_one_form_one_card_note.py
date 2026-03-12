from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppOneFormOneCardNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_one_form_one_card_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_ONE_FORM_ONE_CARD_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_ONE_FORM_ONE_CARD_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
