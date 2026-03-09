from __future__ import annotations

import argparse
from pathlib import Path

TEMPLATES = {
    "README.md": "# {title}\n\nProject overview goes here.\n",
    "CONTRIBUTING.md": "# Contributing\n\nDescribe contribution flow here.\n",
    "CHANGELOG.md": "# Changelog\n\nAll notable changes will be documented here.\n",
    "RELEASE_CHECKLIST.md": "# Release Checklist\n\n- [ ] Update changelog\n- [ ] Verify demo\n- [ ] Tag release\n",
    "benchmark/README.md": "# Benchmark\n\nDocument benchmark setup and results here.\n",
    "demo/run_demo.sh": "#!/usr/bin/env bash\necho \"Demo placeholder\"\n",
    ".github/pull_request_template.md": "## Summary\n\n-\n",
    ".github/ISSUE_TEMPLATE/bug_report.md": "---\nname: Bug report\nabout: Report a bug\n---\n",
    ".github/ISSUE_TEMPLATE/feature_request.md": "---\nname: Feature request\nabout: Suggest an idea\n---\n",
}


def init_project(target: Path, title: str) -> list[str]:
    created: list[str] = []
    for rel_path, template in TEMPLATES.items():
        file_path = target / rel_path
        if file_path.exists():
            continue
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(template.format(title=title), encoding="utf-8")
        if file_path.name == "run_demo.sh":
            file_path.chmod(0o755)
        created.append(rel_path)
    return created


def main() -> None:
    parser = argparse.ArgumentParser(prog="oss-launchpad")
    sub = parser.add_subparsers(dest="command", required=True)

    init_cmd = sub.add_parser("init", help="Initialize a public OSS launch scaffold")
    init_cmd.add_argument("directory", help="Target directory")
    init_cmd.add_argument("--title", help="Project title", default="New Project")

    args = parser.parse_args()

    if args.command == "init":
        target = Path(args.directory).resolve()
        target.mkdir(parents=True, exist_ok=True)
        created = init_project(target, args.title)
        print(f"Initialized scaffold in: {target}")
        if created:
            print("Created files:")
            for item in created:
                print(f"- {item}")
        else:
            print("No new files created.")


if __name__ == "__main__":
    main()
