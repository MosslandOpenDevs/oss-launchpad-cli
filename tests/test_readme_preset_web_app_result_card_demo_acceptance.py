from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppResultCardDemoAcceptanceTests(unittest.TestCase):
    def test_readme_mentions_result_card_demo_acceptance_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_RESULT_CARD_DEMO_ACCEPTANCE.md', readme)

    def test_note_mentions_result_card_export_and_playwright(self) -> None:
        note = (ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_DEMO_ACCEPTANCE.md').read_text(encoding='utf-8')
        self.assertIn('result card', note)
        self.assertIn('export', note)
        self.assertIn('Playwright', note)


if __name__ == '__main__':
    unittest.main()
