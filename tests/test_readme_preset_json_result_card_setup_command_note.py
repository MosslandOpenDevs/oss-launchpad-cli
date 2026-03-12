from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonResultCardSetupCommandNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_setup_command_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_RESULT_CARD_SETUP_COMMAND_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_RESULT_CARD_SETUP_COMMAND_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
