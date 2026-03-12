from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppResultCardAcceptanceTests(unittest.TestCase):
    def test_readme_links_web_demo_result_card_acceptance(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        note = ROOT / "docs" / "PRESET_WEB_DEMO_RESULT_CARD_ACCEPTANCE.md"

        self.assertTrue(note.exists())
        self.assertIn("docs/PRESET_WEB_DEMO_RESULT_CARD_ACCEPTANCE.md", readme)
        self.assertIn("one visible result card", note.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
