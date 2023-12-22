# tests/test_dummyproject.py

from dummyproject import __version__

def test_version():
    assert __version__ == "0.1.0"