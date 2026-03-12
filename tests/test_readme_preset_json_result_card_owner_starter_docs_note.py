from __future__ import annotations

from pathlib import Path
import unittest


class ReadmePresetJsonResultCardOwnerStarterDocsNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_result_card_owner_starter_docs_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_JSON_RESULT_CARD_OWNER_STARTER_DOCS_NOTE.md', readme)
        self.assertTrue((root / 'docs' / 'PRESET_JSON_RESULT_CARD_OWNER_STARTER_DOCS_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
