from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePresetWebAppGovernanceReportOutputTagNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_report_output_tag_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        note = (ROOT / 'docs' / 'PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_TAG_NOTE.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_TAG_NOTE.md', readme)
        self.assertIn('report_output_tag', note)
        self.assertIn('stable result card', note)
