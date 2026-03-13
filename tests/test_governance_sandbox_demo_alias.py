from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxDemoAliasTests(unittest.TestCase):
    def test_governance_sandbox_demo_alias_resolves_to_web_app(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json", "--preset", "governance-sandbox-demo"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
            env={"PYTHONPATH": str(ROOT / "src")},
        )

        payload = json.loads(completed.stdout)
        self.assertEqual(list(payload), ["web-app"])


if __name__ == "__main__":
    unittest.main()
