"""The source python repo."""

import os
from pathlib import Path

os.environ["REPO_DIR"] = str(Path(__file__).resolve().parents[2])

print(os.environ["REPO_DIR"])
