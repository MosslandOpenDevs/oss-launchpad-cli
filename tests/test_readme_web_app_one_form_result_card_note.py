from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppOneFormResultCardNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_ONE_FORM_RESULT_CARD_NOTE.md", readme)

    def test_note_mentions_form_action_result_card(self) -> None:
        note = (ROOT / "docs" / "PRESET_WEB_APP_ONE_FORM_RESULT_CARD_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("one form", note)
        self.assertIn("one primary action", note)
        self.assertIn("validator-backed result card", note)


if __name__ == "__main__":
    unittest.main()
