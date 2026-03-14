from __future__ import annotations

import unittest
from pathlib import Path


class ReadmeGovernanceReportHandleDemoAliasTests(unittest.TestCase):
    def test_readme_mentions_governance_report_handle_demo_alias(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('governance-report-handle-demo', readme)
        self.assertIn('PRESET_WEB_APP_GOVERNANCE_REPORT_OUTPUT_HANDLE_NOTE.md', readme)


if __name__ == '__main__':
    unittest.main()
