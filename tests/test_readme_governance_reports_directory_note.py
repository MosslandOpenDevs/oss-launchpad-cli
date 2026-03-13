from __future__ import annotations

import unittest
from pathlib import Path


class ReadmeGovernanceReportsDirectoryNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_reports_directory_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_GOVERNANCE_REPORTS_DIRECTORY_NOTE.md', readme)
        self.assertTrue((root / 'docs' / 'PRESET_WEB_APP_GOVERNANCE_REPORTS_DIRECTORY_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
