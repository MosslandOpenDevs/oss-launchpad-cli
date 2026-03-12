from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonResultCardExportReadyStackTests(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_export_ready_stack(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_JSON_RESULT_CARD_EXPORT_READY_STACK.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_JSON_RESULT_CARD_EXPORT_READY_STACK.md').exists())
