from pathlib import Path
import unittest


class ReadmePresetJsonResultCardValidateExportGateTest(unittest.TestCase):
    def test_readme_mentions_result_card_validate_export_gate(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_JSON_RESULT_CARD_VALIDATE_EXPORT_GATE.md', readme)
        self.assertTrue(Path('docs/PRESET_JSON_RESULT_CARD_VALIDATE_EXPORT_GATE.md').exists())


if __name__ == '__main__':
    unittest.main()
