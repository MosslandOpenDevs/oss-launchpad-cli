from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernanceResultCardUiPlaywrightBridgeTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_governance_result_card_ui_playwright_bridge(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_GOVERNANCE_RESULT_CARD_UI_PLAYWRIGHT_BRIDGE.md", readme)

    def test_note_mentions_ui_ux_and_playwright(self) -> None:
        note = (ROOT / "docs" / "PRESET_WEB_APP_GOVERNANCE_RESULT_CARD_UI_PLAYWRIGHT_BRIDGE.md").read_text(encoding="utf-8")
        self.assertIn("UI/UX", note)
        self.assertIn("Playwright", note)
        self.assertIn("result card", note)


if __name__ == "__main__":
    unittest.main()
