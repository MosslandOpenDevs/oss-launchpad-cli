from pathlib import Path
import unittest


class ReadmePresetWebAppGovernanceFormCardUiPlaywrightNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_governance_form_card_ui_playwright_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_WEB_APP_GOVERNANCE_FORM_CARD_UI_PLAYWRIGHT_NOTE.md", readme)
        note = (root / "docs" / "PRESET_WEB_APP_GOVERNANCE_FORM_CARD_UI_PLAYWRIGHT_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("scenario input form", note)
        self.assertIn("Playwright-interactive replay discipline", note)


if __name__ == "__main__":
    unittest.main()
