from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonWebFormResultStackNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_web_form_result_stack_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        note = ROOT / "docs" / "PRESET_JSON_WEB_FORM_RESULT_STACK_NOTE.md"

        self.assertIn("docs/PRESET_JSON_WEB_FORM_RESULT_STACK_NOTE.md", readme)
        self.assertTrue(note.exists())
        body = note.read_text(encoding="utf-8")
        self.assertIn("one starter form or preset picker", body)
        self.assertIn("one visible result card", body)
        self.assertIn("one report-style export or handoff target", body)


if __name__ == "__main__":
    unittest.main()
