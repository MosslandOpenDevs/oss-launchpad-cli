import unittest
from pathlib import Path


class ReadmePresetJsonResultCardDownloadGateTest(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_download_gate(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_JSON_RESULT_CARD_DOWNLOAD_GATE.md', readme)


if __name__ == '__main__':
    unittest.main()
