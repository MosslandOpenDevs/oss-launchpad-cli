from __future__ import annotations

import unittest

from oss_launchpad_cli.cli import _resolve_preset_name


class PresetAliasTests(unittest.TestCase):
    def test_web_app_extended_aliases_resolve_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name("frontend"), "web-app")
        self.assertEqual(_resolve_preset_name("landing-page"), "web-app")
        self.assertEqual(_resolve_preset_name("landing"), "web-app")


if __name__ == "__main__":
    unittest.main()
