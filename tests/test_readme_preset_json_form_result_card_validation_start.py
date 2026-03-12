from pathlib import Path
import unittest


class ReadmePresetJsonFormResultCardValidationStartTest(unittest.TestCase):
    def test_readme_mentions_result_card_validation_start_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_JSON_FORM_RESULT_CARD_VALIDATION_START.md', readme)


if __name__ == '__main__':
    unittest.main()
