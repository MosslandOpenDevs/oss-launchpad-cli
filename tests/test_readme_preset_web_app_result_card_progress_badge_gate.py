import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ReadmePresetWebAppResultCardProgressBadgeGateTests(unittest.TestCase):
    def test_readme_mentions_gate(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_PROGRESS_BADGE_GATE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_PROGRESS_BADGE_GATE.md").exists())

if __name__ == "__main__":
    unittest.main()
