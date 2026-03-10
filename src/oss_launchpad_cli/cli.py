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
DEFAULT_CONTEXT = {
    "project_tagline": "Bootstrap a public repository with launch-ready documentation and reproducible project scaffolding.",
    "why_section": "Use this repository to explain the project clearly, show a runnable path, and make contribution/release expectations obvious.",
    "setup_section": "- Document install steps.\n- Add the first runnable command.\n- Keep setup instructions short and reproducible.",
}


def _slugify_title(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.strip().lower()).strip("-")
    return slug or "new-project"


def _load_preset_context(preset: str, title: str) -> dict[str, str]:
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


def _build_proof_review_command(preset: str, title_slug: str, package_name: str) -> str:
    commands = {
        "ai-agent": "sed -n '1,120p' docs/launch-plan.md && sed -n '1,120p' docs/agent-demo-brief.md",
        "web-app": "sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' docs/landing-page-brief.md",
        "python-lib": f"sed -n '1,120p' docs/launch-scorecard.md && sed -n '1,120p' examples/basic_usage.py",
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
        f"First-PR evidence command: {_build_first_pr_command(preset, title_slug, package_name)}",
        f"Proof-review command: {_build_proof_review_command(preset, title_slug, package_name)}",
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


def main() -> None:
    parser = argparse.ArgumentParser(prog="oss-launchpad")
    sub = parser.add_subparsers(dest="command", required=True)

    init_cmd = sub.add_parser("init", help="Initialize a public OSS launch scaffold")
    init_cmd.add_argument("directory", help="Target directory")
    init_cmd.add_argument("--title", help="Project title", default="New Project")
    init_cmd.add_argument(
        "--preset",
        choices=sorted(PRESET_TEMPLATE_ROOTS),
        default="ai-agent",
        help="Project preset to render into the scaffold",
    )

    args = parser.parse_args()

    if args.command == "init":
        target = Path(args.directory).resolve()
        target.mkdir(parents=True, exist_ok=True)
        created = init_project(target, args.title, args.preset)
        title_slug = _slugify_title(args.title)
        package_name = title_slug.replace("-", "_")
        print(f"Initialized scaffold in: {target}")
        print(f"Preset: {args.preset}")
        print(f"Title slug: {title_slug}")
        if args.preset == "python-lib":
            print(f"Package import path: {package_name}")
        if created:
            print("Created files:")
            for item in created:
                print(f"- {item}")
        else:
            print("No new files created.")
        print("Starter assets to customize first:")
        for item in _build_starter_assets(args.preset, package_name):
            print(f"- {item}")
        print("First proof assets to capture:")
        for item in _build_first_proof_assets(args.preset, package_name):
            print(f"- {item}")
        print("Next steps:")
        for step in _build_next_steps(args.preset, title_slug, package_name):
            print(f"- {step}")
        print(f"Starter-review command: {_build_starter_review_command(args.preset, title_slug, package_name)}")


if __name__ == "__main__":
    main()
