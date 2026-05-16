from app.ingestion.repo_loader import load_repo
from app.ingestion.file_parser import parse_file
from app.indexing.chunking import chunk_file

repo_path = "C:/Users/naren/OneDrive/Desktop/di22-topicus1/src/main/java/org/Topicus"

files = load_repo(repo_path)

parsed = []
for f in files:
    p = parse_file(f)
    if p:
        parsed.append(p)

print(f"Parsed {len(parsed)} files")

chunks = []
for f in parsed:
    chunks.extend(chunk_file(f))

print(f"Total chunks: {len(chunks)}")

# Count types
from collections import Counter
types = Counter([c["type"] for c in chunks])
print(types)

example = chunks[0]
print(example["type"])
print(example["path"])
print(example["content"][:200])