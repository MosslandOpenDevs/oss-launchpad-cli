from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppUiUxPlaywrightBridgeTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_ui_ux_playwright_bridge(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_UI_UX_PLAYWRIGHT_BRIDGE.md', readme)

    def test_note_mentions_chooser_result_card_and_playwright(self) -> None:
        note = (ROOT / 'docs' / 'PRESET_WEB_APP_UI_UX_PLAYWRIGHT_BRIDGE.md').read_text(encoding='utf-8')
        self.assertIn('preset chooser', note)
        self.assertIn('result card', note)
        self.assertIn('Playwright', note)


if __name__ == '__main__':
    unittest.main()
