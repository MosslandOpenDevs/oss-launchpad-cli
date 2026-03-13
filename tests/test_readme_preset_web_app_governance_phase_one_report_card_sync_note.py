from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernancePhaseOneReportCardSyncNoteTests(unittest.TestCase):
    def test_readme_mentions_phase_one_report_card_sync_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_GOVERNANCE_PHASE_ONE_REPORT_CARD_SYNC_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_WEB_APP_GOVERNANCE_PHASE_ONE_REPORT_CARD_SYNC_NOTE.md').exists())

    def test_note_mentions_repo5_phase_one_targets(self) -> None:
        doc = (ROOT / 'docs' / 'PRESET_WEB_APP_GOVERNANCE_PHASE_ONE_REPORT_CARD_SYNC_NOTE.md').read_text(encoding='utf-8')

        self.assertIn('scenario-file inputs', doc)
        self.assertIn('markdown/html report downloads', doc)
        self.assertIn('one form, one primary action, one result card', doc)


if __name__ == '__main__':
    unittest.main()
