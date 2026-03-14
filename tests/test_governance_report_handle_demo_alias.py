from __future__ import annotations

import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
sys.path.insert(0, str(SRC))

from oss_launchpad_cli.cli import _resolve_preset_name


class GovernanceReportHandleDemoAliasTests(unittest.TestCase):
    def test_governance_report_handle_demo_alias_resolves_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name('governance-report-handle-demo'), 'web-app')


if __name__ == '__main__':
    unittest.main()
