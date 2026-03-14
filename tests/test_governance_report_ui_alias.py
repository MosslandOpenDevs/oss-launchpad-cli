from __future__ import annotations

import unittest

from oss_launchpad_cli.cli import _resolve_preset_name


class GovernanceReportUiAliasTests(unittest.TestCase):
    def test_governance_report_ui_maps_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name("governance-report-ui"), "web-app")


if __name__ == "__main__":
    unittest.main()
