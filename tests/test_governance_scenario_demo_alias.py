from oss_launchpad_cli.cli import _resolve_preset_name


def test_governance_scenario_demo_alias_maps_to_web_app() -> None:
    assert _resolve_preset_name("governance-scenario-demo") == "web-app"
