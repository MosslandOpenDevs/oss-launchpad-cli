from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetJsonGovernanceJson5CompatNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_json_governance_json5_compat_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_JSON_GOVERNANCE_JSON5_COMPAT_NOTE.md', readme)

    def test_note_mentions_json5_and_result_card(self) -> None:
        note = (ROOT / 'docs/PRESET_JSON_GOVERNANCE_JSON5_COMPAT_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('.json5', note)
        self.assertIn('result-card', note)


if __name__ == '__main__':
    unittest.main()
