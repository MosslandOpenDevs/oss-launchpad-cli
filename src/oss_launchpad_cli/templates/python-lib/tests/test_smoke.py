import unittest

from {package_name} import __version__


class SmokeTests(unittest.TestCase):
    def test_version_is_present(self) -> None:
        self.assertIsInstance(__version__, str)
        self.assertTrue(__version__)


if __name__ == "__main__":
    unittest.main()
