from pathlib import Path
import unittest


class ReadmePresetWebAppResultCardExportStackNoteTest(unittest.TestCase):
    def test_note_mentions_form_card_export_stack(self) -> None:
        note = Path("docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_STACK_NOTE.md")
        self.assertTrue(note.exists())
        text = note.read_text(encoding="utf-8")
        self.assertIn("result card", text.lower())
        self.assertIn("export", text.lower())
        self.assertIn("playwright", text.lower())


if __name__ == "__main__":
    unittest.main()
