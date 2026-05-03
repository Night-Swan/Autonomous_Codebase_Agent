from pathlib import Path
from typing import List

EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", "build", "dist"}


def load_repo(repo_path: str) -> List[Path]:
    repo = Path(repo_path)

    files = []
    for path in repo.rglob("*"):
        if path.is_file():
            if any(part in EXCLUDE_DIRS for part in path.parts):
                continue
            files.append(path)

    return files