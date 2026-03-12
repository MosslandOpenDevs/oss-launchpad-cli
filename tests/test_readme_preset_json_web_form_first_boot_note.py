from __future__ import annotations

from pathlib import Path
import unittest


class ReadmePresetJsonWebFormFirstBootNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_web_form_first_boot_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_WEB_FORM_FIRST_BOOT_NOTE.md", readme)
        self.assertIn("oss-launchpad presets --preset web-app --json", readme)
        self.assertTrue((root / "docs" / "PRESET_JSON_WEB_FORM_FIRST_BOOT_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
