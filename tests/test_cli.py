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
    _build_quickstart_docs,
    _build_next_steps,
    _build_proof_review_command,
    _build_smoke_command,
    _list_presets,
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


    def test_list_presets_returns_sorted_presets(self) -> None:
        self.assertEqual(_list_presets(), ["ai-agent", "python-lib", "web-app"])

    def test_build_smoke_command_is_preset_specific(self) -> None:
        self.assertIn("evals/smoke_cases.jsonl", _build_smoke_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/landing-page-brief.md", _build_smoke_command("web-app", "web-repo", "web_repo"))
        self.assertIn("tests/test_smoke.py", _build_smoke_command("python-lib", "library-project", "library_project"))

    def test_build_starter_assets_is_preset_specific(self) -> None:
        self.assertIn("prompts/system.txt", _build_starter_assets("ai-agent", "agent_repo"))
        self.assertIn("docs/information-architecture.md", _build_starter_assets("web-app", "web_repo"))
        self.assertIn("demo/run_demo.sh", _build_starter_assets("web-app", "web_repo"))
        self.assertIn("src/library_project/__init__.py", _build_starter_assets("python-lib", "library_project"))

    def test_build_validation_command_is_preset_specific(self) -> None:
        self.assertIn("json.tool", _build_validation_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("landing-page-brief.md", _build_validation_command("web-app", "web-repo", "web_repo"))
        self.assertIn("python3 -m unittest tests/test_smoke.py", _build_validation_command("python-lib", "library-project", "library_project"))

    def test_build_customize_first_command_is_preset_specific(self) -> None:
        self.assertIn("prompts/system.txt", _build_customize_first_command("ai-agent", "agent-repo", "agent_repo"))
        self.assertIn("docs/ui-ux-checklist.md", _build_customize_first_command("web-app", "web-repo", "web_repo"))
        self.assertIn("src/library_project/__init__.py", _build_customize_first_command("python-lib", "library-project", "library_project"))

    def test_build_quickstart_docs_is_preset_specific(self) -> None:
        self.assertEqual(
            _build_quickstart_docs("ai-agent", "agent_repo"),
            ["README.md", "prompts/system.txt", "evals/README.md", "docs/agent-demo-brief.md"],
        )
        self.assertEqual(
            _build_quickstart_docs("web-app", "web_repo"),
            ["README.md", ".env.example", "docs/landing-page-brief.md", "docs/ui-ux-checklist.md"],
        )
        self.assertEqual(
            _build_quickstart_docs("python-lib", "library_project"),
            ["README.md", "src/library_project/__init__.py", "examples/basic_usage.py", "docs/api-surface.md"],
        )

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

    def test_build_first_proof_assets_keeps_web_demo_result_card_for_web_app(self) -> None:
        self.assertIn(
            "docs/landing-page-brief.md",
            _build_first_proof_assets("web-app", "web_repo"),
        )
        self.assertIn(
            "docs/ui-ux-checklist.md",
            _build_first_proof_assets("web-app", "web_repo"),
        )
        self.assertIn(
            "demo/run_demo.sh",
            _build_first_proof_assets("web-app", "web_repo"),
        )

    def test_readme_mentions_web_app_ui_scope_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_UI_SCOPE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_UI_SCOPE_NOTE.md").exists())

    def test_readme_mentions_web_app_result_card_download_check(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_CHECK.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_DOWNLOAD_CHECK.md").exists())

    def test_readme_mentions_web_app_result_card_ui_audit(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_UI_AUDIT.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_UI_AUDIT.md").exists())

    def test_readme_mentions_web_app_form_to_card_loop(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_FORM_TO_CARD_LOOP.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_FORM_TO_CARD_LOOP.md").exists())

    def test_readme_mentions_web_app_form_readiness_check(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_FORM_READINESS_CHECK.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_FORM_READINESS_CHECK.md").exists())

    def test_readme_mentions_web_app_first_result_card_check(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_FIRST_RESULT_CARD_CHECK.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_FIRST_RESULT_CARD_CHECK.md").exists())


    def test_readme_mentions_web_app_result_card_stability_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_STABILITY_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_STABILITY_NOTE.md").exists())

    def test_readme_mentions_web_app_result_card_one_action_rule(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_ONE_ACTION_RULE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_ONE_ACTION_RULE.md").exists())

    def test_build_next_steps_keeps_web_app_bootstrap_handoffs_visible(self) -> None:
        steps = _build_next_steps("web-app", "web-repo", "web_repo")

        self.assertIn("Customize-first command: sed -n '1,80p' docs/landing-page-brief.md && sed -n '1,80p' docs/ui-ux-checklist.md", steps)
        self.assertIn("First-issue command: sed -n '1,120p' docs/ui-ux-checklist.md && sed -n '1,120p' docs/information-architecture.md", steps)
        self.assertIn("Fill .env.example with the minimum local variables required to boot the app.", steps)
        self.assertIn("Review docs/information-architecture.md alongside docs/landing-page-brief.md before the first UI implementation.", steps)
        self.assertIn("Use docs/PRESET_WEB_APP_UI_PROOF_LOOP.md to keep the first landing-page proof tied to docs/ui-ux-checklist.md and demo/run_demo.sh.", steps)
        self.assertIn("Use docs/PRESET_WEB_DEMO_RESULT_CARD.md to keep the first visible UI proof scoped to one reviewable result card before adding secondary screens.", steps)
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

    def test_build_next_steps_keeps_first_proof_handoff_commands_for_ai_agent(self) -> None:
        steps = _build_next_steps("ai-agent", "agent-repo", "agent_repo")

        self.assertIn("First-PR evidence command: sed -n '1,120p' docs/agent-demo-brief.md && sed -n '1,120p' evals/README.md", steps)
        self.assertIn("First proof status command: sed -n '1,80p' docs/agent-demo-brief.md && sed -n '1,40p' evals/smoke_cases.jsonl", steps)
        self.assertIn("First-release command: sed -n '1,120p' docs/launch-plan.md && sed -n '1,120p' docs/agent-demo-brief.md", steps)
        self.assertIn("Update prompts/system.txt with the first system prompt or agent contract.", steps)
        self.assertIn("Add a real evaluation command under evals/README.md before the first public release.", steps)

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

    def test_cli_presets_prints_starter_assets_for_each_preset(self) -> None:
        env = dict(os.environ)
        env["PYTHONPATH"] = str(SRC) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
        result = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets"],
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )
        self.assertIn("ai-agent:", result.stdout)
        self.assertIn("- prompts/system.txt", result.stdout)
        self.assertIn("python-lib:", result.stdout)
        self.assertIn("- src/sample_project/__init__.py", result.stdout)
        self.assertIn("web-app:", result.stdout)
        self.assertIn("- demo/run_demo.sh", result.stdout)

    def test_cli_presets_json_prints_structured_metadata(self) -> None:
        env = dict(os.environ)
        env["PYTHONPATH"] = str(SRC) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
        result = subprocess.run(
            [sys.executable, "-m", "oss_launchpad_cli.cli", "presets", "--json"],
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )
        payload = __import__("json").loads(result.stdout)
        self.assertIn("ai-agent", payload)
        self.assertIn("starter_assets", payload["web-app"])
        self.assertIn("first_proof_assets", payload["python-lib"])
        self.assertIn("smoke_command", payload["web-app"])
        self.assertIn("validation_command", payload["web-app"])
        self.assertIn("customize_first_command", payload["web-app"])
        self.assertIn("starter_review_command", payload["web-app"])
        self.assertIn("day_zero_review_command", payload["web-app"])
        self.assertIn("first_pr_command", payload["web-app"])
        self.assertIn("proof_review_command", payload["web-app"])
        self.assertIn("first_proof_status_command", payload["web-app"])
        self.assertIn("first_issue_command", payload["web-app"])
        self.assertIn("first_release_command", payload["web-app"])
        self.assertIn("next_steps", payload["web-app"])
        self.assertIn("docs/landing-page-brief.md", payload["web-app"]["starter_assets"])
        self.assertIn("demo/run_demo.sh", payload["web-app"]["day_zero_docs"])
        self.assertIn("docs/landing-page-brief.md", payload["web-app"]["first_proof_assets"])
        self.assertIn("docs/information-architecture.md", payload["web-app"]["day_zero_docs"])
        self.assertIn("sh demo/run_demo.sh", payload["web-app"]["smoke_command"])
        self.assertIn("docs/ui-ux-checklist.md", payload["web-app"]["customize_first_command"])
        self.assertIn("docs/information-architecture.md", payload["web-app"]["first_pr_command"])
        self.assertTrue(any(step.startswith("Smoke command:") for step in payload["web-app"]["next_steps"]))
        self.assertTrue(any("PRESET_WEB_DEMO_RESULT_CARD.md" in step for step in payload["web-app"]["next_steps"]))


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

    def test_build_day_zero_docs_keeps_web_app_demo_script_visible(self) -> None:
        docs = _build_day_zero_docs("web-app", "web_repo")

        self.assertIn("docs/information-architecture.md", docs)
        self.assertIn("demo/run_demo.sh", docs)

    def test_readme_links_web_app_ui_handoff_rules_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_UI_HANDOFF_RULES.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_UI_HANDOFF_RULES.md").exists())

    def test_readme_links_first_proof_artifact_bundle_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_FIRST_PROOF_ARTIFACT_BUNDLE.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_FIRST_PROOF_ARTIFACT_BUNDLE.md").exists())

    def test_readme_links_web_app_result_card_bundle_check_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_BUNDLE_CHECK.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_BUNDLE_CHECK.md").exists())

    def test_readme_links_web_demo_result_card_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_DEMO_RESULT_CARD.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_DEMO_RESULT_CARD.md").exists())

    def test_readme_links_web_demo_form_result_stability_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_DEMO_FORM_RESULT_STABILITY.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_DEMO_FORM_RESULT_STABILITY.md").exists())

    def test_readme_links_web_app_result_card_copy_review_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_COPY_REVIEW.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_COPY_REVIEW.md").exists())

    def test_readme_links_web_app_ui_proof_start_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_UI_PROOF_START.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_UI_PROOF_START.md").exists())

    def test_readme_links_web_app_playwright_checkpoints_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_PLAYWRIGHT_CHECKPOINTS.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_PLAYWRIGHT_CHECKPOINTS.md").exists())

    def test_readme_links_web_demo_proof_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_DEMO_PROOF.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_DEMO_PROOF.md").exists())

    def test_readme_links_web_app_starter_review_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_STARTER_REVIEW.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_STARTER_REVIEW.md").exists())

    def test_readme_links_web_app_result_card_handoff_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_RESULT_CARD_HANDOFF.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_RESULT_CARD_HANDOFF.md").exists())

    def test_readme_links_web_app_form_to_card_loop_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_FORM_TO_CARD_LOOP.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_FORM_TO_CARD_LOOP.md").exists())

    def test_readme_links_web_app_playwright_recovery_doc(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_WEB_APP_PLAYWRIGHT_RECOVERY.md", readme)
        self.assertTrue((ROOT / "docs" / "PRESET_WEB_APP_PLAYWRIGHT_RECOVERY.md").exists())


if __name__ == "__main__":
    unittest.main()
