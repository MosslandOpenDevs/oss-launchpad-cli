from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ReadmePresetWebAppJsonChooserNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_web_app_json_chooser_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_WEB_APP_JSON_CHOOSER_NOTE.md', readme)
        self.assertIn('web-app preset', readme)

    def test_note_mentions_presets_json_command(self) -> None:
        note = (ROOT / 'docs' / 'PRESET_WEB_APP_JSON_CHOOSER_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('oss-launchpad presets --json --preset web-app', note)
        self.assertIn('one form, one primary action, and one result card', note)

if __name__ == '__main__':
    unittest.main()
