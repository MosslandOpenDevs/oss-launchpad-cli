from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetGovernanceReportFileAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_governance_report_file_alias_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        note = (ROOT / 'docs' / 'PRESET_GOVERNANCE_REPORT_FILE_ALIAS_NOTE.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_GOVERNANCE_REPORT_FILE_ALIAS_NOTE.md', readme)
        self.assertIn('scenario-file input', note)
        self.assertIn('report-file alias', note)


if __name__ == '__main__':
    unittest.main()
