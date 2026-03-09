from {package_name} import __version__


def test_version_smoke() -> None:
    assert __version__ == "0.1.0"
