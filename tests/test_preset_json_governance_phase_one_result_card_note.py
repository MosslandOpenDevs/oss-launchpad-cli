from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PresetJsonGovernancePhaseOneResultCardNoteTests(unittest.TestCase):
    def test_readme_mentions_phase_one_result_card_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_JSON_GOVERNANCE_PHASE_ONE_RESULT_CARD_NOTE.md', readme)

    def test_note_mentions_one_chooser_one_primary_action_one_result_card(self) -> None:
        note = (ROOT / 'docs' / 'PRESET_JSON_GOVERNANCE_PHASE_ONE_RESULT_CARD_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('one chooser, one primary action, and one reviewable result card', note)
        self.assertIn('scenario-file/report-first', note)


if __name__ == '__main__':
    unittest.main()
