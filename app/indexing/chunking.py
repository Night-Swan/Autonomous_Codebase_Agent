from typing import List, Dict


CODE_LANGUAGES = {"python", "java", "javascript", "typescript", "cpp"}
DOC_LANGUAGES = {"text"}


def classify_file(file: Dict) -> str:
    """
    Classify file into 'code', 'doc', or 'skip'
    """
    language = file["language"]
    path = file["path"].lower()

    # Skip obvious junk
    if any([
        ".git" in path,
        "node_modules" in path,
        "__pycache__" in path,
    ]):
        return "skip"

    # Skip tiny files
    if len(file["content"]) < 50:
        return "skip"

    # Code files
    if language in CODE_LANGUAGES:
        return "code"

    # Documentation files
    if language in DOC_LANGUAGES or path.endswith((".md", ".txt")):
        return "doc"

    return "skip"


def chunk_file(file: Dict, max_lines: int = 80) -> List[Dict]:
    """
    Chunk file into line-based segments with metadata
    """
    file_type = classify_file(file)

    if file_type == "skip":
        return []

    lines = file["content"].splitlines()
    chunks = []

    for i in range(0, len(lines), max_lines):
        chunk_lines = lines[i:i + max_lines]

        if not chunk_lines:
            continue

        chunks.append({
            "content": "\n".join(chunk_lines),
            "path": file["path"],
            "start_line": i,
            "end_line": i + len(chunk_lines),
            "type": file_type,
            "language": file["language"]
        })

    return chunks