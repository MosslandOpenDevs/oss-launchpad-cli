import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonResultCardOneBundleNoteTests(unittest.TestCase):
    def test_readme_mentions_result_card_one_bundle_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_RESULT_CARD_ONE_BUNDLE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_RESULT_CARD_ONE_BUNDLE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
