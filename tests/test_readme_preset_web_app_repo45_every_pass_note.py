import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppRepo45EveryPassNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_repo45_every_pass_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_REPO45_EVERY_PASS_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_WEB_APP_REPO45_EVERY_PASS_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
