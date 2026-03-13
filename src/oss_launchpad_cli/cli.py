from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
TEMPLATES_ROOT = PACKAGE_ROOT.parent.parent / "templates"
BASE_TEMPLATE_ROOT = TEMPLATES_ROOT / "base"
PRESET_TEMPLATE_ROOTS = {
    "ai-agent": TEMPLATES_ROOT / "ai-agent",
    "web-app": TEMPLATES_ROOT / "web-app",
    "python-lib": TEMPLATES_ROOT / "python-lib",
}
PRESET_ALIASES = {
    "agent": "ai-agent",
    "app": "web-app",
    "site": "web-app",
    "website": "web-app",
    "ui-demo": "web-app",
    "frontend": "web-app",
    "landing-page": "web-app",
    "landing": "web-app",
    "showcase": "web-app",
    "result-card-demo": "web-app",
    "result-card-ui": "web-app",
    "web-demo": "web-app",
    "web-ui-demo": "web-app",
    "ui-proof": "web-app",
    "governance-demo": "web-app",
    "governance-ui": "web-app",
    "library": "python-lib",
    "lib": "python-lib",
}

PRESET_SUMMARIES = {
    "ai-agent": "Best when the first believable proof is a prompt, eval, and runnable agent contract.",
    "web-app": "Best when the first believable proof is a landing flow, UI checklist, and demo script.",
    "python-lib": "Best when the first believable proof is an importable package, smoke test, and usage example.",
}
PRESET_FIRST_UI_SLICE = {
    "ai-agent": "System prompt + eval contract + first runnable demo brief.",
    "web-app": "One form, one primary action, and one reviewable result card.",
    "python-lib": "One import path, one smoke test, and one usage example.",
}

PRESET_PLAYWRIGHT_LANE = {
    "ai-agent": "Keep the first prompt/eval proof deterministic before widening the demo surface.",
    "web-app": "Keep browser proof limited to one form, one primary action, and one stable result card before widening flows.",
    "python-lib": "Keep smoke proof focused on one import path and one stable usage example before adding matrix coverage.",
}

PRESET_PLAYWRIGHT_RECOVERY_LANE = {
    "ai-agent": "Re-run the smallest deterministic eval path before widening agent-demo automation.",
    "web-app": "Recover with the smallest form -> primary action -> result-card replay before widening browser flows.",
    "python-lib": "Recover with one import path and one smoke example before adding broader matrix checks.",
}

PRESET_UI_UX_LANE = {
    "ai-agent": "Lead with the smallest believable workflow proof before layering extra controls or dashboards.",
    "web-app": "Lead with intro-first messaging, one form, one primary action, and one reviewable result card before adding secondary navigation.",
    "python-lib": "Lead with the clearest import/use path before widening advanced API surface or packaging detail.",
}

DEFAULT_CONTEXT = {
    "project_tagline": "Bootstrap a public repository with launch-ready documentation and reproducible project scaffolding.",
    "why_section": "Use this repository to explain the project clearly, show a runnable path, and make contribution/release expectations obvious.",
    "setup_section": "- Document install steps.\n- Add the first runnable command.\n- Keep setup instructions short and reproducible.",
}


def _slugify_title(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.strip().lower()).strip("-")
    return slug or "new-project"


def _resolve_preset_name(preset: str) -> str:
    return PRESET_ALIASES.get(preset, preset)


def _load_preset_context(preset: str, title: str) -> dict[str, str]:
    preset = _resolve_preset_name(preset)
    if preset not in PRESET_TEMPLATE_ROOTS:
        raise ValueError(f"Unsupported preset: {preset}")
    context_path = PRESET_TEMPLATE_ROOTS[preset] / "context.json"
    with context_path.open("r", encoding="utf-8") as handle:
        preset_context = json.load(handle)
    title_slug = _slugify_title(title)
    merged = dict(DEFAULT_CONTEXT)
    merged.update(preset_context)
    merged.update(
        {
            "title": title,
            "title_slug": title_slug,
            "package_name": title_slug.replace("-", "_"),
        }
    )
    return merged


def _iter_template_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("*") if path.is_file() and path.name != "context.json")


def _render_template_group(target: Path, template_root: Path, context: dict[str, str]) -> list[str]:
    created: list[str] = []
    for template_file in _iter_template_files(template_root):
        rel_path = template_file.relative_to(template_root)
        rendered_rel_path = Path(rel_path.as_posix().format(**context))
        file_path = target / rendered_rel_path
        if file_path.exists():
            continue
        file_path.parent.mkdir(parents=True, exist_ok=True)
        rendered = template_file.read_text(encoding="utf-8").format(**context)
        file_path.write_text(rendered, encoding="utf-8")
        if file_path.suffix == ".sh":
            file_path.chmod(0o755)
        created.append(rendered_rel_path.as_posix())
    return created


def init_project(target: Path, title: str, preset: str) -> list[str]:
    preset = _resolve_preset_name(preset)
    context = _load_preset_context(preset, title)
    created = _render_template_group(target, BASE_TEMPLATE_ROOT, context)
    created.extend(_render_template_group(target, PRESET_TEMPLATE_ROOTS[preset], context))
    return created


def _build_smoke_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "python3 -m json.tool evals/smoke_cases.jsonl >/dev/null || head -n 3 evals/smoke_cases.jsonl",
        "web-app": "sh demo/run_demo.sh && sed -n '1,40p' docs/landing-page-brief.md",
        "python-lib": f"PYTHONPATH=src python3 -m unittest tests/test_smoke.py && python3 examples/basic_usage.py",
    }
    return commands[preset]


def _build_validation_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "python3 -m json.tool evals/smoke_cases.jsonl >/dev/null",
        "web-app": "sh demo/run_demo.sh >/dev/null && sed -n '1,20p' docs/landing-page-brief.md",
        "python-lib": "PYTHONPATH=src python3 -m unittest tests/test_smoke.py",
    }
    return commands[preset]


def _build_customize_first_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "sed -n '1,80p' prompts/system.txt && sed -n '1,80p' evals/README.md",
        "web-app": "sed -n '1,80p' docs/landing-page-brief.md && sed -n '1,80p' docs/ui-ux-checklist.md",
        "python-lib": f"sed -n '1,80p' src/{package_name}/__init__.py && sed -n '1,80p' docs/api-surface.md",
    }
    return commands[preset]


def _build_first_pr_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "sed -n '1,120p' docs/agent-demo-brief.md && sed -n '1,120p' evals/README.md",
        "web-app": "sed -n '1,120p' docs/landing-page-brief.md && sed -n '1,120p' docs/information-architecture.md",
        "python-lib": f"sed -n '1,120p' examples/basic_usage.py && sed -n '1,120p' docs/api-surface.md",
    }
    return commands[preset]


def _build_starter_review_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "sed -n '1,80p' README.md && sed -n '1,80p' prompts/system.txt",
        "web-app": "sed -n '1,80p' README.md && sed -n '1,80p' docs/landing-page-brief.md",
        "python-lib": f"sed -n '1,80p' README.md && sed -n '1,80p' src/{package_name}/__init__.py",
    }
    return commands[preset]


def _build_day_zero_review_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "sed -n '1,120p' README.md && sed -n '1,120p' docs/agent-demo-brief.md",
        "web-app": "sed -n '1,120p' README.md && sed -n '1,120p' docs/landing-page-brief.md",
        "python-lib": "sed -n '1,120p' README.md && sed -n '1,120p' examples/basic_usage.py",
    }
    return commands[preset]


def _build_proof_review_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "sed -n '1,120p' docs/launch-plan.md && sed -n '1,120p' docs/agent-demo-brief.md",
        "web-app": "sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' docs/landing-page-brief.md",
        "python-lib": f"sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' examples/basic_usage.py",
    }
    return commands[preset]


def _build_first_release_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "sed -n '1,120p' docs/launch-plan.md && sed -n '1,120p' docs/agent-demo-brief.md",
        "web-app": "sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' docs/landing-page-brief.md",
        "python-lib": f"sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' docs/api-surface.md",
    }
    return commands[preset]


def _build_first_proof_status_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "sed -n '1,80p' docs/agent-demo-brief.md && sed -n '1,40p' evals/smoke_cases.jsonl",
        "web-app": "sed -n '1,80p' docs/landing-page-brief.md && sed -n '1,80p' docs/information-architecture.md",
        "python-lib": f"sed -n '1,80p' examples/basic_usage.py && sed -n '1,80p' docs/api-surface.md",
    }
    return commands[preset]


def _build_first_issue_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "sed -n '1,120p' docs/agent-demo-brief.md && sed -n '1,120p' evals/README.md",
        "web-app": "sed -n '1,120p' docs/ui-ux-checklist.md && sed -n '1,120p' docs/information-architecture.md",
        "python-lib": f"sed -n '1,120p' docs/api-surface.md && sed -n '1,120p' tests/test_smoke.py",
    }
    return commands[preset]


def _build_next_steps(preset: str, title_slug: str, package_name: str) -> list[str]:
    common_steps = [
        "Review README.md and replace placeholder setup commands with the first real local run.",
        "Fill docs/launch-plan.md with the launch audience, proof assets, and release scope.",
        "Complete docs/launch-scorecard.md so the first public announcement has a visible readiness checklist.",
        "Review RELEASE_CHECKLIST.md before the first tag so launch steps and public proof stay aligned.",
        "Run demo/run_demo.sh and keep the benchmark/README.md evidence path in sync.",
    ]
    preset_steps = {
        "ai-agent": [
            "Update prompts/system.txt with the first system prompt or agent contract.",
            "Add a real evaluation command under evals/README.md before the first public release.",
        ],
        "web-app": [
            "Fill .env.example with the minimum local variables required to boot the app.",
            "Review docs/information-architecture.md alongside docs/landing-page-brief.md before the first UI implementation.",
            "Use docs/PRESET_WEB_APP_UI_PROOF_LOOP.md to keep the first landing-page proof tied to docs/ui-ux-checklist.md and demo/run_demo.sh.",
            "Use docs/PRESET_WEB_DEMO_RESULT_CARD.md to keep the first visible UI proof scoped to one reviewable result card before adding secondary screens.",
            "Use docs/PRESET_WEB_APP_PLAYWRIGHT_STABILITY_LANE.md before widening browser automation so the first form-to-card proof stays reproducible.",
            "Replace docs/ui-ux-checklist.md examples with the actual landing-page and happy-path UX checks.",
        ],
        "python-lib": [
            f"Implement the first public API in src/{package_name}/__init__.py.",
            f"Run python -m unittest tests/test_smoke.py after wiring the package import path for {title_slug}.",
        ],
    }
    return [
        f"Smoke command: {_build_smoke_command(preset, title_slug, package_name)}",
        f"Validation command: {_build_validation_command(preset, title_slug, package_name)}",
        f"Customize-first command: {_build_customize_first_command(preset, title_slug, package_name)}",
        f"Starter-review command: {_build_starter_review_command(preset, title_slug, package_name)}",
        f"Day-zero review command: {_build_day_zero_review_command(preset, title_slug, package_name)}",
        f"First-PR evidence command: {_build_first_pr_command(preset, title_slug, package_name)}",
        f"Proof-review command: {_build_proof_review_command(preset, title_slug, package_name)}",
        f"First proof status command: {_build_first_proof_status_command(preset, title_slug, package_name)}",
        f"First-issue command: {_build_first_issue_command(preset, title_slug, package_name)}",
        f"First-release command: {_build_first_release_command(preset, title_slug, package_name)}",
    ] + common_steps + preset_steps[preset]


def _build_starter_assets(preset: str, package_name: str) -> list[str]:
    assets = {
        "ai-agent": [
            "prompts/system.txt",
            "evals/README.md",
            "evals/smoke_cases.jsonl",
            "docs/agent-demo-brief.md",
        ],
        "web-app": [
            ".env.example",
            "docs/ui-ux-checklist.md",
            "docs/landing-page-brief.md",
            "docs/information-architecture.md",
            "demo/run_demo.sh",
        ],
        "python-lib": [
            "pyproject.toml",
            f"src/{package_name}/__init__.py",
            "tests/test_smoke.py",
            "examples/basic_usage.py",
            "docs/api-surface.md",
        ],
    }
    return assets[preset]




def _build_quickstart_docs(preset: str, package_name: str) -> list[str]:
    docs = {
        "ai-agent": ["README.md", "prompts/system.txt", "evals/README.md", "docs/agent-demo-brief.md"],
        "web-app": ["README.md", ".env.example", "docs/landing-page-brief.md", "docs/ui-ux-checklist.md"],
        "python-lib": ["README.md", f"src/{package_name}/__init__.py", "examples/basic_usage.py", "docs/api-surface.md"],
    }
    return docs[preset]


def _build_first_proof_assets(preset: str, package_name: str) -> list[str]:
    assets = {
        "ai-agent": [
            "docs/agent-demo-brief.md",
            "evals/smoke_cases.jsonl",
            "demo/run_demo.sh",
        ],
        "web-app": [
            "docs/landing-page-brief.md",
            "docs/ui-ux-checklist.md",
            "demo/run_demo.sh",
        ],
        "python-lib": [
            "examples/basic_usage.py",
            "tests/test_smoke.py",
            "docs/api-surface.md",
        ],
    }
    return assets[preset]


def _build_day_zero_docs(preset: str, package_name: str) -> list[str]:
    common_docs = [
        "README.md",
        "docs/launch-plan.md",
        "docs/launch-scorecard.md",
        "RELEASE_CHECKLIST.md",
    ]
    preset_docs = {
        "ai-agent": ["docs/agent-demo-brief.md", "evals/README.md"],
        "web-app": ["docs/landing-page-brief.md", "docs/ui-ux-checklist.md", "docs/information-architecture.md", "demo/run_demo.sh"],
        "python-lib": ["docs/api-surface.md", "examples/basic_usage.py", "tests/test_smoke.py"],
    }
    return common_docs + preset_docs[preset]


def _list_presets() -> list[str]:
    return sorted(PRESET_TEMPLATE_ROOTS)


def _list_preset_choices() -> list[str]:
    return sorted(set(_list_presets()) | set(PRESET_ALIASES))


def main() -> None:
    parser = argparse.ArgumentParser(prog="oss-launchpad")
    sub = parser.add_subparsers(dest="command", required=True)

    init_cmd = sub.add_parser("init", help="Initialize a public OSS launch scaffold")
    init_cmd.add_argument("directory", help="Target directory")
    init_cmd.add_argument("--title", help="Project title", default="New Project")
    init_cmd.add_argument(
        "--preset",
        choices=_list_preset_choices(),
        default="ai-agent",
        help="Project preset to render into the scaffold",
    )

    presets_cmd = sub.add_parser("presets", help="List scaffold presets and starter assets")
    presets_cmd.add_argument("--json", action="store_true", help="Print preset metadata as JSON")
    presets_cmd.add_argument("--preset", choices=_list_preset_choices(), help="Show metadata for one preset only")

    args = parser.parse_args()

    if args.command == "presets":
        preset_map = {}
        preset_names = [_resolve_preset_name(args.preset)] if args.preset else _list_presets()
        for preset in preset_names:
            package_name = 'sample_project'
            preset_map[preset] = {
                "preset_count": len(_list_presets()),
                "preset_key": preset,
                "label": preset.replace("-", " ").title(),
                "summary": PRESET_SUMMARIES[preset],
                "first_ui_slice": PRESET_FIRST_UI_SLICE[preset],
                "result_card_focus": PRESET_FIRST_UI_SLICE[preset],
                "report_download_checkpoint": PRESET_FIRST_UI_SLICE[preset],
                "proof_scope": PRESET_FIRST_UI_SLICE[preset],
                "ui_ux_lane": PRESET_UI_UX_LANE[preset],
                "primary_action": _build_validation_command(preset, "sample-project", package_name),
                "playwright_lane": PRESET_PLAYWRIGHT_LANE[preset],
                "playwright_recovery_lane": PRESET_PLAYWRIGHT_RECOVERY_LANE[preset],
                "starter_assets": _build_starter_assets(preset, package_name),
                "quickstart_docs": _build_quickstart_docs(preset, package_name),
                "first_proof_assets": _build_first_proof_assets(preset, package_name),
                "day_zero_docs": _build_day_zero_docs(preset, package_name),
                "smoke_command": _build_smoke_command(preset, "sample-project", package_name),
                "validation_command": _build_validation_command(preset, "sample-project", package_name),
                "proof_validation_command": _build_validation_command(preset, "sample-project", package_name),
                "result_card_validation_command": _build_validation_command(preset, "sample-project", package_name),
                "setup_command": _build_customize_first_command(preset, "sample-project", package_name),
                "customize_first_command": _build_customize_first_command(preset, "sample-project", package_name),
                "starter_review_command": _build_starter_review_command(preset, "sample-project", package_name),
                "day_zero_review_command": _build_day_zero_review_command(preset, "sample-project", package_name),
                "first_pr_command": _build_first_pr_command(preset, "sample-project", package_name),
                "proof_review_command": _build_proof_review_command(preset, "sample-project", package_name),
                "first_proof_status_command": _build_first_proof_status_command(preset, "sample-project", package_name),
                "first_issue_command": _build_first_issue_command(preset, "sample-project", package_name),
                "first_release_command": _build_first_release_command(preset, "sample-project", package_name),
                "next_steps": _build_next_steps(preset, "sample-project", package_name),
            }
        if args.json:
            print(json.dumps(preset_map, indent=2))
            return
        for preset, details in preset_map.items():
            print(f"{preset}: {details['summary']}")
            print(f"  first_ui_slice: {details['first_ui_slice']}")
            print(f"  result_card_focus: {details['result_card_focus']}")
            print(f"  proof_scope: {details['proof_scope']}")
            print(f"  ui_ux_lane: {details['ui_ux_lane']}")
            print(f"  primary_action: {details['primary_action']}")
            print(f"  playwright_lane: {details['playwright_lane']}")
            print(f"  playwright_recovery_lane: {details['playwright_recovery_lane']}")
            print("  starter_assets:")
            for asset in details["starter_assets"]:
                print(f"  - {asset}")
            print("  quickstart_docs:")
            for doc in details["quickstart_docs"]:
                print(f"  - {doc}")
        return

    if args.command == "init":
        resolved_preset = _resolve_preset_name(args.preset)
        target = Path(args.directory).resolve()
        target.mkdir(parents=True, exist_ok=True)
        created = init_project(target, args.title, resolved_preset)
        title_slug = _slugify_title(args.title)
        package_name = title_slug.replace("-", "_")
        print(f"Initialized scaffold in: {target}")
        print(f"Preset: {resolved_preset}")
        print(f"Title slug: {title_slug}")
        if resolved_preset == "python-lib":
            print(f"Package import path: {package_name}")
        if created:
            print(f"Created {len(created)} file(s):")
            for item in created:
                print(f"- {item}")
        else:
            print("No new files created.")
        print("Starter assets to customize first:")
        for item in _build_starter_assets(resolved_preset, package_name):
            print(f"- {item}")
        print("Quickstart docs to open first:")
        for item in _build_quickstart_docs(resolved_preset, package_name):
            print(f"- {item}")
        print("First proof assets to capture:")
        for item in _build_first_proof_assets(resolved_preset, package_name):
            print(f"- {item}")
        print("Day-zero docs to open:")
        for item in _build_day_zero_docs(resolved_preset, package_name):
            print(f"- {item}")
        print("Next steps:")
        for step in _build_next_steps(resolved_preset, title_slug, package_name):
            print(f"- {step}")


if __name__ == "__main__":
    main()
