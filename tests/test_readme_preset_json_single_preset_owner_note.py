from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonSinglePresetOwnerNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_single_preset_owner_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_SINGLE_PRESET_OWNER_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_SINGLE_PRESET_OWNER_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
