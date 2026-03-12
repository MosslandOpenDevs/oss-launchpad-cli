from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"


class ReadmePresetJsonResultCardOwnerSummaryNoteTests(unittest.TestCase):
    def test_readme_mentions_owner_summary_note(self) -> None:
        readme = README_PATH.read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_RESULT_CARD_OWNER_SUMMARY_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_RESULT_CARD_OWNER_SUMMARY_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
