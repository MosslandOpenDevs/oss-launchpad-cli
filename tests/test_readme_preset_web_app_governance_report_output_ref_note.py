from pathlib import Path
import unittest


class ReadmePresetWebAppGovernanceReportOutputRefNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_report_output_ref_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        note = Path('docs/PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_REF_NOTE.md').read_text(encoding='utf-8')

        self.assertIn('docs/PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_REF_NOTE.md', readme)
        self.assertIn('report_output_ref', note)
        self.assertIn('JSON/Markdown/HTML bundle', note)


if __name__ == '__main__':
    unittest.main()
