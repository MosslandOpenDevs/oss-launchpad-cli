from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonResultCardValidateThenPushMicroNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_JSON_RESULT_CARD_VALIDATE_THEN_PUSH_MICRO_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_RESULT_CARD_VALIDATE_THEN_PUSH_MICRO_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
