import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonUiStartTest(unittest.TestCase):
    def test_readme_mentions_preset_json_ui_start(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_UI_START.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_UI_START.md").exists())
