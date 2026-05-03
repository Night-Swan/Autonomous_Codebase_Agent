from pathlib import Path


def parse_file(path: Path) -> dict | None:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return None

    return {
        "path": str(path),
        "content": content,
        "language": detect_language(path),
    }


def detect_language(path: Path) -> str:
    suffix = path.suffix.lower()
    return {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".cpp": "cpp",
        ".h": "cpp",
        ".java": "java",
    }.get(suffix, "text")