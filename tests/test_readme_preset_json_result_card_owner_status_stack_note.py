from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "PRESET_JSON_RESULT_CARD_OWNER_STATUS_STACK_NOTE.md"


class ReadmePresetJsonResultCardOwnerStatusStackNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        text = README.read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_JSON_RESULT_CARD_OWNER_STATUS_STACK_NOTE.md", text)

    def test_note_mentions_owner_status_export_stack(self) -> None:
        text = NOTE.read_text(encoding="utf-8")
        self.assertIn("owner-ready status", text)
        self.assertIn("export/download target", text)


if __name__ == "__main__":
    unittest.main()
