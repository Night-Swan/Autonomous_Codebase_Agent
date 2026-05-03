from app.ingestion.repo_loader import load_repo
from app.ingestion.file_parser import parse_file

repo_path = "C:/Users/naren/OneDrive/Desktop/di22-topicus1/src/main/java/org/Topicus"

files = load_repo(repo_path)

parsed = []
for f in files:
    p = parse_file(f)
    if p:
        parsed.append(p)

print(f"Loaded {len(parsed)} files")
print(parsed[0])