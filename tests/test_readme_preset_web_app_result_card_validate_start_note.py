import unittest
from pathlib import Path


class ReadmePresetWebAppResultCardValidateStartNoteTests(unittest.TestCase):
    def test_readme_mentions_result_card_validate_start_note(self) -> None:
        text = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_RESULT_CARD_VALIDATE_START_NOTE.md', text)


if __name__ == '__main__':
    unittest.main()
