from __future__ import annotations

import unittest

from oss_launchpad_cli.cli import _resolve_preset_name


class GovernanceWebFormAliasTest(unittest.TestCase):
    def test_governance_web_form_alias_points_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name("governance-web-form"), "web-app")


if __name__ == "__main__":
    unittest.main()
