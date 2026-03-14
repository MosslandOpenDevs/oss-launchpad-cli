from oss_launchpad_cli.cli import _resolve_preset_name


def test_report_card_demo_alias_maps_to_web_app() -> None:
    assert _resolve_preset_name("report-card-demo") == "web-app"
