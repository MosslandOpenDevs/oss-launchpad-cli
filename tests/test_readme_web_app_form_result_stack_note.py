from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "PRESET_WEB_APP_FORM_RESULT_STACK_NOTE.md"


class WebAppFormResultStackNoteReadmeTests(unittest.TestCase):
    def test_readme_mentions_web_app_form_result_stack_note(self) -> None:
        readme = README.read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_FORM_RESULT_STACK_NOTE.md", readme)
        self.assertTrue(NOTE.exists())

    def test_web_app_form_result_stack_note_keeps_scope_small(self) -> None:
        note = NOTE.read_text(encoding="utf-8")

        self.assertIn("one form submission", note)
        self.assertIn("one result card", note)
        self.assertIn("one report handoff", note)


if __name__ == "__main__":
    unittest.main()
