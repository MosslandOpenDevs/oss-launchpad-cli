from pathlib import Path
import unittest


class ReadmePresetJsonSinglePresetExportNoteTests(unittest.TestCase):
    def test_readme_mentions_single_preset_export_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_SINGLE_PRESET_EXPORT_NOTE.md", readme)
        self.assertTrue((root / "docs" / "PRESET_JSON_SINGLE_PRESET_EXPORT_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
