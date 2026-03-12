from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_VALIDATION_HUD_NOTE.md"


class WebAppResultCardValidationHudNoteTests(unittest.TestCase):
    def test_readme_mentions_validation_hud_note(self) -> None:
        readme = README.read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_VALIDATION_HUD_NOTE.md", readme)
        self.assertTrue(NOTE.exists())

    def test_note_keeps_primary_action_validation_and_download_visible(self) -> None:
        note = NOTE.read_text(encoding="utf-8")

        self.assertIn("primary action", note)
        self.assertIn("validation command", note)
        self.assertIn("download target", note)


if __name__ == "__main__":
    unittest.main()
