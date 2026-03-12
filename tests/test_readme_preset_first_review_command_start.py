from pathlib import Path
import unittest


class ReadmePresetFirstReviewCommandStartTests(unittest.TestCase):
    def test_readme_mentions_first_review_command_start(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PRESET_FIRST_REVIEW_COMMAND_START.md", readme)
        self.assertIn("smallest post-generate proof loop", readme)


if __name__ == "__main__":
    unittest.main()
