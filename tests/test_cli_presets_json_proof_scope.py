from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


class CliPresetsJsonProofScopeTests(unittest.TestCase):
    def test_presets_json_includes_proof_scope(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json", "--preset", "web-app"],
            cwd=ROOT,
            env={**os.environ, "PYTHONPATH": str(SRC)},
            check=True,
            capture_output=True,
            text=True,
        )

        payload = json.loads(completed.stdout)
        self.assertEqual(
            payload["web-app"]["proof_scope"],
            "One form, one primary action, and one reviewable result card.",
        )


if __name__ == "__main__":
    unittest.main()
