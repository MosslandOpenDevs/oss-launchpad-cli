from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppResultCardPrimaryActionRuleTests(unittest.TestCase):
    def test_readme_mentions_web_app_result_card_primary_action_rule(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_PRIMARY_ACTION_RULE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_PRIMARY_ACTION_RULE.md").exists())


if __name__ == "__main__":
    unittest.main()
