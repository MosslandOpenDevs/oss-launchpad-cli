from pathlib import Path
import unittest


class ReadmePresetJsonResultCardDownloadBadgeNoteTests(unittest.TestCase):
    def test_readme_mentions_result_card_download_badge_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_JSON_RESULT_CARD_DOWNLOAD_BADGE_NOTE.md', readme)
        self.assertIn('download/export badge beside that same primary status', readme)


if __name__ == '__main__':
    unittest.main()
