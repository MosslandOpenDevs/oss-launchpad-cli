from oss_launchpad_cli.cli import _resolve_preset_name


def test_dao_demo_alias_resolves_to_web_app() -> None:
    assert _resolve_preset_name('dao-demo') == 'web-app'
