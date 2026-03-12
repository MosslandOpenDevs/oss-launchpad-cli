from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / 'README.md'


class ReadmePresetJsonResultCardValidationAndExportNoteTests(unittest.TestCase):
    def test_readme_mentions_validation_and_export_note(self) -> None:
        readme = README_PATH.read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_JSON_RESULT_CARD_VALIDATION_AND_EXPORT_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_JSON_RESULT_CARD_VALIDATION_AND_EXPORT_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
