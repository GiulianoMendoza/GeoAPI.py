import os
import sys


def pytest_sessionstart(session):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    src = os.path.join(root, "src")
    if src not in sys.path:
        sys.path.insert(0, src)

