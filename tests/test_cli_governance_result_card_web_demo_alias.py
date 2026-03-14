from __future__ import annotations

import unittest

from oss_launchpad_cli.cli import _resolve_preset_name


class GovernanceResultCardWebDemoAliasTests(unittest.TestCase):
    def test_governance_result_card_web_demo_resolves_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name("governance-result-card-web-demo"), "web-app")


if __name__ == "__main__":
    unittest.main()
