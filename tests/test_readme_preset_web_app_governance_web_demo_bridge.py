from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernanceWebDemoBridgeTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_governance_web_demo_bridge(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_GOVERNANCE_WEB_DEMO_BRIDGE.md", readme)

    def test_note_mentions_web_app_json_result_card_and_playwright(self) -> None:
        note = (ROOT / "docs" / "PRESET_WEB_APP_GOVERNANCE_WEB_DEMO_BRIDGE.md").read_text(encoding="utf-8")
        self.assertIn("oss-launchpad presets --json --preset web-app", note)
        self.assertIn("result card", note)
        self.assertIn("Playwright", note)


if __name__ == "__main__":
    unittest.main()
