from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from oss_launchpad_cli.cli import (
    _build_customize_first_command,
    _build_day_zero_docs,
    _build_day_zero_review_command,
    _build_first_proof_status_command,
    _build_first_issue_command,
    _build_first_release_command,
    _build_first_pr_command,
    _build_first_proof_assets,
    _build_next_steps,
    _build_proof_review_command,
    _build_smoke_command,
    _build_starter_assets,
    _build_starter_review_command,
    _build_validation_command,
    init_project,
)


class InitProjectTests(unittest.TestCase):
    def test_slugify_title_falls_back_for_punctuation_only_titles(self) -> None:
        from oss_launchpad_cli.cli import _slugify_title

        self.assertEqual(_slugify_title("***"), "new-project")
        self.assertEqual(_slugify_title("  ---  "), "new-project")

    def test_slugify_title_collapses_mixed_separators_into_single_dashes(self) -> None:
        from oss_launchpad_cli.cli import _slugify_title

        self.assertEqual(_slugify_title("My_Library v2"), "my-library-v2")
        self.assertEqual(_slugify_title(" Agent---CLI   Demo "), "agent-cli-demo")

    def test_build_smoke_command_is_preset_specific(self) -> None:
        self.assertIn("evals/smoke_cases.jsonl", _build_smoke_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/landing-page-brief.md", _build_smoke_command("web-app", "web-repo", "web_repo"))
        self.assertIn("tests/test_smoke.py", _build_smoke_command("python-lib", "library-project", "library_project"))

    def test_build_starter_assets_is_preset_specific(self) -> None:
        self.assertIn("prompts/system.txt", _build_starter_assets("ai-agent", "agent_repo"))
        self.assertIn("docs/information-architecture.md", _build_starter_assets("web-app", "web_repo"))
        self.assertIn("src/library_project/__init__.py", _build_starter_assets("python-lib", "library_project"))

    def test_build_validation_command_is_preset_specific(self) -> None:
        self.assertIn("json.tool", _build_validation_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("landing-page-brief.md", _build_validation_command("web-app", "web-repo", "web_repo"))
        self.assertIn("python3 -m unittest tests/test_smoke.py", _build_validation_command("python-lib", "library-project", "library_project"))

    def test_build_customize_first_command_is_preset_specific(self) -> None:
        self.assertIn("prompts/system.txt", _build_customize_first_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/ui-ux-checklist.md", _build_customize_first_command("web-app", "web-repo", "web_repo"))
        self.assertIn("src/library_project/__init__.py", _build_customize_first_command("python-lib", "library-project", "library_project"))

    def test_build_first_proof_assets_is_preset_specific(self) -> None:
        self.assertEqual(
            _build_first_proof_assets("ai-agent", "agent_repo"),
            ["docs/agent-demo-brief.md", "evals/smoke_cases.jsonl", "demo/run_demo.sh"],
        )
        self.assertEqual(
            _build_first_proof_assets("web-app", "web_repo"),
            ["docs/landing-page-brief.md", "docs/ui-ux-checklist.md", "demo/run_demo.sh"],
        )
        self.assertEqual(
            _build_first_proof_assets("python-lib", "library_project"),
            ["examples/basic_usage.py", "tests/test_smoke.py", "docs/api-surface.md"],
        )

    def test_build_first_pr_command_is_preset_specific(self) -> None:
        self.assertIn("docs/agent-demo-brief.md", _build_first_pr_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/information-architecture.md", _build_first_pr_command("web-app", "web-repo", "web_repo"))
        self.assertIn("examples/basic_usage.py", _build_first_pr_command("python-lib", "library-project", "library_project"))

    def test_build_day_zero_docs_is_preset_specific(self) -> None:
        self.assertIn("README.md", _build_day_zero_docs("ai-agent", "agent_repo"))
        self.assertIn("evals/README.md", _build_day_zero_docs("ai-agent", "agent_repo"))
        self.assertIn("docs/information-architecture.md", _build_day_zero_docs("web-app", "web_repo"))
        self.assertIn("tests/test_smoke.py", _build_day_zero_docs("python-lib", "library_project"))

    def test_build_starter_review_command_is_preset_specific(self) -> None:
        self.assertIn("README.md", _build_starter_review_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/landing-page-brief.md", _build_starter_review_command("web-app", "web-repo", "web_repo"))
        self.assertIn("src/library_project/__init__.py", _build_starter_review_command("python-lib", "library-project", "library_project"))

    def test_build_day_zero_review_command_is_preset_specific(self) -> None:
        self.assertIn("docs/agent-demo-brief.md", _build_day_zero_review_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/landing-page-brief.md", _build_day_zero_review_command("web-app", "web-repo", "web_repo"))
        self.assertIn("examples/basic_usage.py", _build_day_zero_review_command("python-lib", "library-project", "library_project"))

    def test_build_proof_review_command_is_preset_specific(self) -> None:
        self.assertIn("docs/launch-plan.md", _build_proof_review_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/launch-scorecard.md", _build_proof_review_command("web-app", "web-repo", "web_repo"))
        self.assertIn("examples/basic_usage.py", _build_proof_review_command("python-lib", "library-project", "library_project"))

    def test_build_first_release_command_is_preset_specific(self) -> None:
        self.assertIn("docs/agent-demo-brief.md", _build_first_release_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/landing-page-brief.md", _build_first_release_command("web-app", "web-repo", "web_repo"))
        self.assertIn("docs/api-surface.md", _build_first_release_command("python-lib", "library-project", "library_project"))

    def test_build_first_proof_status_command_is_preset_specific(self) -> None:
        self.assertIn("evals/smoke_cases.jsonl", _build_first_proof_status_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/information-architecture.md", _build_first_proof_status_command("web-app", "web-repo", "web_repo"))
        self.assertIn("examples/basic_usage.py", _build_first_proof_status_command("python-lib", "library-project", "library_project"))

    def test_build_first_issue_command_is_preset_specific(self) -> None:
        self.assertIn("docs/agent-demo-brief.md", _build_first_issue_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/ui-ux-checklist.md", _build_first_issue_command("web-app", "web-repo", "web_repo"))
        self.assertIn("tests/test_smoke.py", _build_first_issue_command("python-lib", "library-project", "library_project"))

    def test_build_next_steps_keeps_web_app_bootstrap_handoffs_visible(self) -> None:
        steps = _build_next_steps("web-app", "web-repo", "web_repo")

        self.assertIn("Customize-first command: sed -n '1,80p' docs/landing-page-brief.md && sed -n '1,80p' docs/ui-ux-checklist.md", steps)
        self.assertIn("First-issue command: sed -n '1,120p' docs/ui-ux-checklist.md && sed -n '1,120p' docs/information-architecture.md", steps)
        self.assertIn("Fill .env.example with the minimum local variables required to boot the app.", steps)
        self.assertIn("Replace docs/ui-ux-checklist.md examples with the actual landing-page and happy-path UX checks.", steps)

    def test_build_next_steps_keeps_release_checklist_and_command_handoffs(self) -> None:
        steps = _build_next_steps("python-lib", "library-project", "library_project")

        self.assertIn("Smoke command: PYTHONPATH=src python3 -m unittest tests/test_smoke.py && python3 examples/basic_usage.py", steps)
        self.assertIn("Validation command: PYTHONPATH=src python3 -m unittest tests/test_smoke.py", steps)
        self.assertIn("Day-zero review command: sed -n '1,120p' README.md && sed -n '1,120p' examples/basic_usage.py", steps)
        self.assertIn("Proof-review command: sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' examples/basic_usage.py", steps)
        self.assertIn("First proof status command: sed -n '1,80p' examples/basic_usage.py && sed -n '1,80p' docs/api-surface.md", steps)
        self.assertIn("First-issue command: sed -n '1,120p' docs/api-surface.md && sed -n '1,120p' tests/test_smoke.py", steps)
        self.assertIn("First-release command: sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' docs/api-surface.md", steps)
        self.assertIn("Review RELEASE_CHECKLIST.md before the first tag so launch steps and public proof stay aligned.", steps)
        self.assertIn("Implement the first public API in src/library_project/__init__.py.", steps)

    def test_init_project_creates_base_scaffold(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample"
            created = init_project(target, "Sample Project", "ai-agent")
            self.assertIn("README.md", created)
            self.assertIn("docs/launch-plan.md", created)
            self.assertTrue((target / "CONTRIBUTING.md").exists())
            self.assertTrue((target / ".editorconfig").exists())
            self.assertTrue((target / "demo" / "run_demo.sh").exists())
            self.assertTrue((target / "docs" / "launch-plan.md").exists())
            self.assertTrue((target / "docs" / "launch-scorecard.md").exists())
            self.assertTrue((target / "docs" / "agent-demo-brief.md").exists())
            self.assertTrue((target / "evals" / "smoke_cases.jsonl").exists())

    def test_init_project_renders_preset_specific_readme(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample"
            init_project(target, "Library Project", "python-lib")
            readme = (target / "README.md").read_text(encoding="utf-8")
            self.assertIn("Library Project", readme)
            self.assertIn("public Python library repository", readme)

    def test_init_project_adds_preset_specific_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample"
            created = init_project(target, "My Library", "python-lib")
            self.assertIn("pyproject.toml", created)
            self.assertIn("src/my_library/__init__.py", created)
            self.assertIn("tests/test_smoke.py", created)
            self.assertIn("examples/basic_usage.py", created)
            self.assertIn("docs/api-surface.md", created)
            self.assertTrue((target / "src" / "my_library" / "__init__.py").exists())
            self.assertTrue((target / "docs" / "api-surface.md").exists())

    def test_existing_files_are_not_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample"
            target.mkdir(parents=True)
            existing = target / "README.md"
            existing.write_text("keep me", encoding="utf-8")
            created = init_project(target, "Ignored", "web-app")
            self.assertNotIn("README.md", created)
            self.assertEqual(existing.read_text(encoding="utf-8"), "keep me")

    def test_second_init_run_reports_no_new_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "agent-repo"
            env = dict(os.environ)
            env["PYTHONPATH"] = str(SRC) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")

            first = subprocess.run(
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
                env=env,
            )
            self.assertIn("Created ", first.stdout)
            self.assertIn("file(s):", first.stdout)

            second = subprocess.run(
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
                env=env,
            )
            self.assertIn("No new files created.", second.stdout)

    def test_web_app_preset_adds_information_architecture_doc(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample"
            created = init_project(target, "My Web App", "web-app")
            self.assertIn("docs/information-architecture.md", created)
            self.assertTrue((target / "docs" / "information-architecture.md").exists())

    def test_init_project_marks_demo_shell_script_executable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample"
            init_project(target, "My Web App", "web-app")
            demo_script = target / "demo" / "run_demo.sh"
            self.assertTrue(demo_script.exists())
            self.assertTrue(demo_script.stat().st_mode & 0o111)


class CliSmokeTests(unittest.TestCase):
    def test_cli_init_prints_preset_and_creates_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "agent-repo"
            env = dict(os.environ)
            env["PYTHONPATH"] = str(SRC) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
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
                env=env,
            )
            self.assertIn("Preset: ai-agent", result.stdout)
            self.assertRegex(result.stdout, r"Created \d+ file\(s\):")
            self.assertIn("Title slug: agent-repo", result.stdout)
            self.assertIn("Starter assets to customize first:", result.stdout)
            self.assertIn("prompts/system.txt", result.stdout)
            self.assertIn("First proof assets to capture:", result.stdout)
            self.assertIn("Starter-review command: sed -n '1,80p' README.md && sed -n '1,80p' prompts/system.txt", result.stdout)
            self.assertIn("Day-zero review command: sed -n '1,120p' README.md && sed -n '1,120p' docs/agent-demo-brief.md", result.stdout)
            self.assertIn("docs/agent-demo-brief.md", result.stdout)
            self.assertIn("Day-zero docs to open:", result.stdout)
            self.assertIn("docs/launch-plan.md", result.stdout)
            self.assertIn("Next steps:", result.stdout)
            self.assertIn("Smoke command:", result.stdout)
            self.assertIn("Validation command:", result.stdout)
            self.assertIn("Customize-first command:", result.stdout)
            self.assertIn("Day-zero review command:", result.stdout)
            self.assertIn("Starter-review command:", result.stdout)
            self.assertIn("First-PR evidence command:", result.stdout)
            self.assertIn("Proof-review command:", result.stdout)
            self.assertIn("First-issue command:", result.stdout)
            self.assertIn("First-release command:", result.stdout)
            self.assertEqual(result.stdout.count("Starter-review command:"), 1)
            self.assertIn("evals/smoke_cases.jsonl", result.stdout)
            self.assertIn("docs/launch-plan.md", result.stdout)
            self.assertIn("RELEASE_CHECKLIST.md", result.stdout)
            self.assertTrue((target / "README.md").exists())
            self.assertTrue((target / ".github" / "pull_request_template.md").exists())
            self.assertTrue((target / "prompts" / "system.txt").exists())
            self.assertIn("docs/launch-scorecard.md", result.stdout)

    def test_cli_init_prints_python_package_import_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "library-project"
            env = dict(os.environ)
            env["PYTHONPATH"] = str(SRC) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "oss_launchpad_cli.cli",
                    "init",
                    str(target),
                    "--title",
                    "Library Project",
                    "--preset",
                    "python-lib",
                ],
                check=True,
                capture_output=True,
                text=True,
                env=env,
            )
            self.assertIn("Preset: python-lib", result.stdout)
            self.assertIn("Title slug: library-project", result.stdout)
            self.assertIn("Package import path: library_project", result.stdout)
            self.assertIn("src/library_project/__init__.py", result.stdout)


    def test_cli_init_python_lib_prints_starter_and_proof_assets(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "library-project"
            env = dict(os.environ)
            env["PYTHONPATH"] = str(SRC) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "oss_launchpad_cli.cli",
                    "init",
                    str(target),
                    "--title",
                    "Library Project",
                    "--preset",
                    "python-lib",
                ],
                check=True,
                capture_output=True,
                text=True,
                env=env,
            )
            self.assertIn("Starter assets to customize first:", result.stdout)
            self.assertIn("src/library_project/__init__.py", result.stdout)
            self.assertIn("First proof assets to capture:", result.stdout)
            self.assertIn("examples/basic_usage.py", result.stdout)
            self.assertIn("First-issue command:", result.stdout)
            self.assertIn("First-release command:", result.stdout)


if __name__ == "__main__":
    unittest.main()
