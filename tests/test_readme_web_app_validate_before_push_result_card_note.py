from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppValidateBeforePushResultCardNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_VALIDATE_BEFORE_PUSH_RESULT_CARD_NOTE.md", readme)

    def test_note_mentions_validation_and_push(self) -> None:
        note = (ROOT / "docs" / "PRESET_WEB_APP_VALIDATE_BEFORE_PUSH_RESULT_CARD_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("validation command", note)
        self.assertIn("push", note)


if __name__ == "__main__":
    unittest.main()
