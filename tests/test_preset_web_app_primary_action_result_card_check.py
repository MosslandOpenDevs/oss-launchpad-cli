from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PresetWebAppPrimaryActionResultCardCheckTest(unittest.TestCase):
    def test_readme_mentions_primary_action_result_card_check(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_PRIMARY_ACTION_RESULT_CARD_CHECK.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_PRIMARY_ACTION_RESULT_CARD_CHECK.md").exists())


if __name__ == "__main__":
    unittest.main()
