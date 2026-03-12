from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonResultCardScanStartTests(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_scan_start(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_RESULT_CARD_SCAN_START.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_RESULT_CARD_SCAN_START.md").exists())


if __name__ == "__main__":
    unittest.main()
