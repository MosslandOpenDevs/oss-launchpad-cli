from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernancePhaseOneProgressSyncNoteTests(unittest.TestCase):
    def test_readme_mentions_phase_one_progress_sync_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_GOVERNANCE_PHASE_ONE_PROGRESS_SYNC_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PRESET_WEB_APP_GOVERNANCE_PHASE_ONE_PROGRESS_SYNC_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
