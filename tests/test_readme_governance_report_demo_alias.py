from pathlib import Path


def test_readme_mentions_governance_report_demo_alias() -> None:
    readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8")
    assert "governance-report-demo" in readme
    assert "report-driven demo" in readme
