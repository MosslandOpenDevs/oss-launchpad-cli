import unittest
from pathlib import Path


class ReadmePresetGovernanceReportAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_governance_report_alias_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('docs/PRESET_GOVERNANCE_REPORT_ALIAS_NOTE.md', readme)


if __name__ == '__main__':
    unittest.main()
