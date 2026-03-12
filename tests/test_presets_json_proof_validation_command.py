from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


class PresetsJsonProofValidationCommandTests(unittest.TestCase):
    def test_presets_json_includes_proof_validation_command_alias(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json"],
            capture_output=True,
            check=True,
            cwd=Path(__file__).resolve().parents[1],
            text=True,
            env={"PYTHONPATH": "src"},
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["web-app"]["proof_validation_command"], payload["web-app"]["validation_command"])
        self.assertEqual(payload["ai-agent"]["proof_validation_command"], payload["ai-agent"]["validation_command"])
        self.assertEqual(payload["python-lib"]["proof_validation_command"], payload["python-lib"]["validation_command"])


if __name__ == "__main__":
    unittest.main()
