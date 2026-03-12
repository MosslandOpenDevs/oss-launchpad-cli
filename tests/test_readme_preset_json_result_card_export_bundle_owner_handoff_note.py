from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonResultCardExportBundleOwnerHandoffNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_export_bundle_owner_handoff_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_JSON_RESULT_CARD_EXPORT_BUNDLE_OWNER_HANDOFF_NOTE.md', readme)
        note = ROOT / 'docs' / 'PRESET_JSON_RESULT_CARD_EXPORT_BUNDLE_OWNER_HANDOFF_NOTE.md'
        self.assertTrue(note.exists())
        note_text = note.read_text(encoding='utf-8').lower()
        self.assertIn('export bundle', note_text)
        self.assertIn('owner handoff', note_text)


if __name__ == '__main__':
    unittest.main()
