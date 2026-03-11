from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonWebAppSinglePresetNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_web_app_single_preset_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_WEB_APP_SINGLE_PRESET_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_WEB_APP_SINGLE_PRESET_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
