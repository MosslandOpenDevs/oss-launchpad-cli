import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


class CliPresetsJsonPlaywrightRecoveryLaneTests(unittest.TestCase):
    def test_presets_json_includes_playwright_recovery_lane_for_every_preset(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json"],
            cwd=ROOT,
            env={**dict(__import__("os").environ), "PYTHONPATH": str(SRC)},
            capture_output=True,
            text=True,
            check=True,
        )

        payload = json.loads(result.stdout)
        self.assertTrue(payload)
        for preset, details in payload.items():
            self.assertIn("playwright_recovery_lane", details, preset)
            self.assertTrue(str(details["playwright_recovery_lane"]).strip(), preset)


if __name__ == "__main__":
    unittest.main()
