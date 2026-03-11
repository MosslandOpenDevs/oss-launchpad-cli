from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppUiHandoffRulesTests(unittest.TestCase):
    def test_readme_mentions_web_app_ui_handoff_rules(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_UI_HANDOFF_RULES.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_UI_HANDOFF_RULES.md").exists())


if __name__ == "__main__":
    unittest.main()
