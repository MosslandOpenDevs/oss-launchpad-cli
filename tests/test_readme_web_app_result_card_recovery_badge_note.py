from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_RECOVERY_BADGE_NOTE.md"


class ReadmeWebAppResultCardRecoveryBadgeNoteTests(unittest.TestCase):
    def test_readme_mentions_web_app_result_card_recovery_badge_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_RECOVERY_BADGE_NOTE.md", readme)
        self.assertTrue(NOTE.exists())

    def test_note_mentions_validation_badge_and_retry_path(self) -> None:
        note = NOTE.read_text(encoding="utf-8")

        self.assertIn("validation badge", note)
        self.assertIn("retry", note)


if __name__ == "__main__":
    unittest.main()
