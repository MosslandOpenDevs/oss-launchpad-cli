from __future__ import annotations

import contextlib
import io
import unittest
from unittest import mock

from oss_launchpad_cli import cli


class PresetsTextOutputTests(unittest.TestCase):
    def test_presets_text_output_includes_first_ui_slice_and_quickstart_docs(self) -> None:
        buffer = io.StringIO()
        with mock.patch("sys.argv", ["oss-launchpad", "presets", "--preset", "web-app"]):
            with contextlib.redirect_stdout(buffer):
                cli.main()

        rendered = buffer.getvalue()
        self.assertIn("web-app:", rendered)
        self.assertIn("first_ui_slice:", rendered)
        self.assertIn("One form, one primary action, and one reviewable result card.", rendered)
        self.assertIn("quickstart_docs:", rendered)
        self.assertIn("docs/landing-page-brief.md", rendered)


if __name__ == "__main__":
    unittest.main()
