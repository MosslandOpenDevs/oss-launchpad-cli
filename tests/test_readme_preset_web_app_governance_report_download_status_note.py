from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernanceReportDownloadStatusNoteTest(unittest.TestCase):
    def test_readme_mentions_governance_report_download_status_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        note = (ROOT / 'docs' / 'PRESET_WEB_APP_GOVERNANCE_REPORT_DOWNLOAD_STATUS_NOTE.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_GOVERNANCE_REPORT_DOWNLOAD_STATUS_NOTE.md', readme)
        self.assertIn('one JSON/YAML scenario file entry', note)
        self.assertIn('one explicit report download/status cue', note)


if __name__ == '__main__':
    unittest.main()
