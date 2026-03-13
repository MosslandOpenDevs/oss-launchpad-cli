from oss_launchpad_cli.cli import _resolve_preset_name


def test_governance_report_demo_alias_resolves_to_web_app() -> None:
    assert _resolve_preset_name("governance-report-demo") == "web-app"
