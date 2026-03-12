from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


class CliPresetsJsonPrimaryActionTests(unittest.TestCase):
    def test_presets_json_includes_primary_action(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json"],
            cwd=ROOT,
            env={**os.environ, "PYTHONPATH": str(SRC)},
            capture_output=True,
            text=True,
            check=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload["web-app"]["primary_action"], payload["web-app"]["validation_command"])
        self.assertIn("python3 -m unittest", payload["python-lib"]["primary_action"])

    def test_readme_mentions_preset_json_primary_action_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_JSON_PRIMARY_ACTION_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_JSON_PRIMARY_ACTION_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
