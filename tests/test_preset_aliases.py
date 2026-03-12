from oss_launchpad_cli.cli import _resolve_preset_name


def test_resolve_preset_name_aliases():
    assert _resolve_preset_name("agent") == "ai-agent"
    assert _resolve_preset_name("app") == "web-app"
    assert _resolve_preset_name("lib") == "python-lib"
