from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


class PresetsJsonMetadataTests(unittest.TestCase):
    def test_presets_json_includes_catalog_count(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json"],
            capture_output=True,
            check=True,
            cwd=Path(__file__).resolve().parents[1],
            text=True,
            env={"PYTHONPATH": "src"},
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["ai-agent"]["preset_count"], 3)
        self.assertEqual(payload["web-app"]["preset_count"], 3)
        self.assertEqual(payload["python-lib"]["preset_count"], 3)


if __name__ == "__main__":
    unittest.main()
