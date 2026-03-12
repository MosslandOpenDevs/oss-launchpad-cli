import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppResultCardPrimaryStatusTest(unittest.TestCase):
    def test_readme_mentions_preset_web_app_result_card_primary_status(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_PRIMARY_STATUS.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_PRIMARY_STATUS.md").exists())
