from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonResultCardSubjectNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_subject_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_RESULT_CARD_SUBJECT_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_RESULT_CARD_SUBJECT_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
