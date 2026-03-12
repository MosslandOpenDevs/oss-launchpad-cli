from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppResultCardDownloadOwnerNoteTests(unittest.TestCase):
    def test_readme_mentions_download_owner_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_OWNER_NOTE.md', readme)

    def test_note_mentions_result_card_download_and_owner(self) -> None:
        doc = (ROOT / 'docs' / 'PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_OWNER_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('result card', doc)
        self.assertIn('download target', doc)
        self.assertIn('owner', doc)


if __name__ == '__main__':
    unittest.main()
