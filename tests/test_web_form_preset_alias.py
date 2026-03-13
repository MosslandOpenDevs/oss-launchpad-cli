from oss_launchpad_cli.cli import _resolve_preset_name


def test_web_form_alias_maps_to_web_app() -> None:
    assert _resolve_preset_name("web-form") == "web-app"
