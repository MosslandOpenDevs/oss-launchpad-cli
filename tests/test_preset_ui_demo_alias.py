from __future__ import annotations

import unittest

from oss_launchpad_cli.cli import _resolve_preset_name


class PresetUiDemoAliasTests(unittest.TestCase):
    def test_ui_demo_alias_resolves_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name("ui-demo"), "web-app")


if __name__ == "__main__":
    unittest.main()
