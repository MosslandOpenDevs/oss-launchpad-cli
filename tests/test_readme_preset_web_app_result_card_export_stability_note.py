from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppResultCardExportStabilityNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_result_card_export_stability_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_STABILITY_NOTE.md', readme)
        note = (ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_EXPORT_STABILITY_NOTE.md').read_text(encoding='utf-8').lower()
        self.assertIn('one form', note)
        self.assertIn('export-ready result card', note)
        self.assertIn('playwright recovery', note)


if __name__ == '__main__':
    unittest.main()
