from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_readme_mentions_preset_web_app_result_card_replay_lane() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "docs/PRESET_WEB_APP_RESULT_CARD_REPLAY_LANE.md" in readme
    assert (ROOT / "docs/PRESET_WEB_APP_RESULT_CARD_REPLAY_LANE.md").exists()
