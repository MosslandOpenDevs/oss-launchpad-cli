from pathlib import Path
import unittest


class ReadmePresetJsonResultCardOwnerExportNoteTest(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_owner_export_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_JSON_RESULT_CARD_OWNER_EXPORT_NOTE.md", readme)
        self.assertTrue(Path("docs/PRESET_JSON_RESULT_CARD_OWNER_EXPORT_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
