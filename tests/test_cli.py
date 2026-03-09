from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from oss_launchpad_cli.cli import init_project


class InitProjectTests(unittest.TestCase):
    def test_init_project_creates_base_scaffold(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample"
            created = init_project(target, "Sample Project", "ai-agent")
            self.assertIn("README.md", created)
            self.assertTrue((target / "CONTRIBUTING.md").exists())
            self.assertTrue((target / "demo" / "run_demo.sh").exists())

    def test_init_project_renders_preset_specific_readme(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample"
            init_project(target, "Library Project", "python-lib")
            readme = (target / "README.md").read_text(encoding="utf-8")
            self.assertIn("Library Project", readme)
            self.assertIn("public Python library repository", readme)

    def test_existing_files_are_not_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample"
            target.mkdir(parents=True)
            existing = target / "README.md"
            existing.write_text("keep me", encoding="utf-8")
            created = init_project(target, "Ignored", "web-app")
            self.assertNotIn("README.md", created)
            self.assertEqual(existing.read_text(encoding="utf-8"), "keep me")


class CliSmokeTests(unittest.TestCase):
    def test_cli_init_prints_preset_and_creates_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "agent-repo"
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "oss_launchpad_cli.cli",
                    "init",
                    str(target),
                    "--title",
                    "Agent Repo",
                    "--preset",
                    "ai-agent",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("Preset: ai-agent", result.stdout)
            self.assertTrue((target / "README.md").exists())
            self.assertTrue((target / ".github" / "pull_request_template.md").exists())


if __name__ == "__main__":
    unittest.main()
