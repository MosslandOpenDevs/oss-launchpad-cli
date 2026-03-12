from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppPrimaryCtaResultCardNoteTests(unittest.TestCase):
    def test_readme_mentions_primary_cta_result_card_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_PRIMARY_CTA_RESULT_CARD_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_WEB_APP_PRIMARY_CTA_RESULT_CARD_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
