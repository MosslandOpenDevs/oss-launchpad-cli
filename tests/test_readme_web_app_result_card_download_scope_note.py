from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebAppResultCardDownloadScopeNoteTests(unittest.TestCase):
    def test_readme_links_download_scope_note(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_SCOPE_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_SCOPE_NOTE.md').exists())

    def test_note_mentions_form_result_download(self):
        note = (ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_SCOPE_NOTE.md').read_text(encoding='utf-8').lower()
        self.assertIn('form', note)
        self.assertIn('result card', note)
        self.assertIn('download', note)


if __name__ == '__main__':
    unittest.main()
