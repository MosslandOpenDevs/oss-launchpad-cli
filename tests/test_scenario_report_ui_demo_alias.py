import unittest

from oss_launchpad_cli.cli import _resolve_preset_name


class ScenarioReportUiDemoAliasTests(unittest.TestCase):
    def test_scenario_report_ui_demo_alias_resolves_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name('scenario-report-ui-demo'), 'web-app')


if __name__ == '__main__':
    unittest.main()
