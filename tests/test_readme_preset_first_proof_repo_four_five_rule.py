import unittest
from pathlib import Path


class ReadmeRepoFourFiveRuleTest(unittest.TestCase):
    def test_readme_mentions_repo_four_five_rule(self) -> None:
        text = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/PRESET_FIRST_PROOF_REPO_FOUR_FIVE_RULE.md", text)


if __name__ == "__main__":
    unittest.main()
