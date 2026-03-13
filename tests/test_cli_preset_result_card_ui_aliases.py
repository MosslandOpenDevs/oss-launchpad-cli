import unittest

from oss_launchpad_cli.cli import _resolve_preset_name


class CliPresetResultCardUiAliasTests(unittest.TestCase):
    def test_result_card_ui_aliases_map_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name("result-card-ui"), "web-app")
        self.assertEqual(_resolve_preset_name("web-ui-demo"), "web-app")


if __name__ == "__main__":
    unittest.main()
