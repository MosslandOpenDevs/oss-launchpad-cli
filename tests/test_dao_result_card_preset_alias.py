from oss_launchpad_cli.cli import _resolve_preset_name


def test_dao_result_card_alias_maps_to_web_app() -> None:
    assert _resolve_preset_name("dao-result-card") == "web-app"
