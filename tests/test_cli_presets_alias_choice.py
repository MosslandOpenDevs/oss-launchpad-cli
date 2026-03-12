from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CliPresetsAliasChoiceTests(unittest.TestCase):
    def test_presets_json_accepts_alias_choice(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json", "--preset", "app"],
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
