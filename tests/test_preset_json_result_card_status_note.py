from pathlib import Path
import unittest


class PresetJsonResultCardStatusNoteTest(unittest.TestCase):
    def test_note_exists_with_result_card_status_guidance(self) -> None:
        note = Path("docs/PRESET_JSON_RESULT_CARD_STATUS_NOTE.md")
        self.assertTrue(note.exists())
        text = note.read_text(encoding="utf-8")
        self.assertIn("result card", text)
        self.assertIn("validation command", text)


if __name__ == "__main__":
    unittest.main()
