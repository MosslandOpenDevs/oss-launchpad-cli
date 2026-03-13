from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernanceUiPlaywrightResultCardNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_governance_ui_playwright_result_card_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_GOVERNANCE_UI_PLAYWRIGHT_RESULT_CARD_NOTE.md', readme)

    def test_note_mentions_ui_ux_and_playwright(self) -> None:
        note = (ROOT / 'docs' / 'PRESET_WEB_APP_GOVERNANCE_UI_PLAYWRIGHT_RESULT_CARD_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('UI/UX-first', note)
        self.assertIn('Playwright-interactive', note)


if __name__ == '__main__':
    unittest.main()
