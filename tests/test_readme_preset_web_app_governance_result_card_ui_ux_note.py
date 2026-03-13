from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernanceResultCardUiUxNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_governance_result_card_ui_ux_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_GOVERNANCE_RESULT_CARD_UI_UX_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_GOVERNANCE_RESULT_CARD_UI_UX_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
