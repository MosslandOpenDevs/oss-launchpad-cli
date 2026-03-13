from __future__ import annotations

import unittest
from pathlib import Path


class ReadmePresetJsonResultCardValidateExportStatusNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_validate_export_status_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_JSON_RESULT_CARD_VALIDATE_EXPORT_STATUS_NOTE.md', readme)


if __name__ == '__main__':
    unittest.main()
