import unittest

from oss_launchpad_cli.cli import _resolve_preset_name


class GovernanceReportBundleDemoAliasTest(unittest.TestCase):
    def test_governance_report_bundle_demo_alias_maps_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name("governance-report-bundle-demo"), "web-app")


if __name__ == "__main__":
    unittest.main()
