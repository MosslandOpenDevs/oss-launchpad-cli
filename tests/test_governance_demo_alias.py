from __future__ import annotations

import unittest
from pathlib import Path

from oss_launchpad_cli.cli import _resolve_preset_name


class GovernanceDemoAliasTests(unittest.TestCase):
    def test_governance_demo_alias_resolves_to_web_app(self) -> None:
        self.assertEqual(_resolve_preset_name("governance-demo"), "web-app")

    def test_readme_mentions_governance_demo_alias(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("governance-demo", readme)


if __name__ == "__main__":
    unittest.main()
