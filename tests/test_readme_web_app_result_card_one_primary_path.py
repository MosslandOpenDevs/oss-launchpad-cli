from pathlib import Path
import unittest


class ReadmeWebAppResultCardOnePrimaryPathTest(unittest.TestCase):
    def test_readme_mentions_one_primary_path_note(self) -> None:
        readme = Path('README.md').read_text()
        self.assertIn(
            'docs/PRESET_WEB_APP_RESULT_CARD_ONE_PRIMARY_PATH.md',
            readme,
        )


if __name__ == '__main__':
    unittest.main()
