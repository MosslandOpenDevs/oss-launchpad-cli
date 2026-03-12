from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppResultCardStabilityRuleTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_result_card_stability_rule(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_RESULT_CARD_STABILITY_RULE.md', readme)

    def test_note_mentions_form_result_card_and_playwright_style_validation(self) -> None:
        note = (ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_STABILITY_RULE.md').read_text(encoding='utf-8')
        self.assertIn('input form', note)
        self.assertIn('stable result card', note)
        self.assertIn('Playwright-style', note)


if __name__ == '__main__':
    unittest.main()
