from __future__ import annotations

import contextlib
import io
import json
import unittest
from unittest import mock

from oss_launchpad_cli import cli


class PresetsPlaywrightLaneTests(unittest.TestCase):
    def test_presets_json_output_includes_playwright_lane_for_web_app(self) -> None:
        buffer = io.StringIO()
        with mock.patch("sys.argv", ["oss-launchpad", "presets", "--preset", "web-app", "--json"]):
            with contextlib.redirect_stdout(buffer):
                cli.main()

        payload = json.loads(buffer.getvalue())["web-app"]
        self.assertEqual(payload["preset_key"], "web-app")
        self.assertIn("playwright_lane", payload)
        self.assertIn("one form, one primary action, and one stable result card", payload["playwright_lane"].lower())


if __name__ == "__main__":
    unittest.main()
