from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ReadmePresetWebAppResultCardExportRecoveryNoteTest(unittest.TestCase):
    def test_readme_mentions_result_card_export_recovery_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_RESULT_CARD_EXPORT_RECOVERY_NOTE.md', readme)
        note = (ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_EXPORT_RECOVERY_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('one form, one primary action, one stable result card, and one visible export/download target', note)
        self.assertIn('Validate the preset output again before commit/push.', note)

if __name__ == '__main__':
    unittest.main()
