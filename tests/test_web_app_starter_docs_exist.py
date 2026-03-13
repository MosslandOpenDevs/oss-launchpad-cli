from pathlib import Path


def test_web_app_starter_docs_exist() -> None:
    root = Path(__file__).resolve().parents[1]
    assert (root / "docs" / "landing-page-brief.md").exists()
    assert (root / "docs" / "information-architecture.md").exists()
    assert (root / "docs" / "ui-ux-checklist.md").exists()
