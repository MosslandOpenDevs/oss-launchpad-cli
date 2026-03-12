import unittest
from pathlib import Path


class ReadmePresetJsonResultCardStatusExportNoteTests(unittest.TestCase):
    def test_readme_mentions_status_export_note(self) -> None:
        readme = Path(__file__).resolve().parents[1] / 'README.md'
        text = readme.read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_JSON_RESULT_CARD_STATUS_EXPORT_NOTE.md', text)


if __name__ == '__main__':
    unittest.main()
