from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


class PresetsJsonSetupCommandAliasTests(unittest.TestCase):
    def test_presets_json_includes_setup_command_alias(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json"],
            capture_output=True,
            check=True,
            cwd=Path(__file__).resolve().parents[1],
            text=True,
            env={"PYTHONPATH": "src"},
        )
        payload = json.loads(result.stdout)
        for details in payload.values():
            self.assertEqual(details["setup_command"], details["customize_first_command"])


if __name__ == "__main__":
    unittest.main()
