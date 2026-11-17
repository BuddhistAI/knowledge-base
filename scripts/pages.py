"""Read the frontmatter of task and workflow pages (a small YAML subset: key: value and key: [a, b])."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def parse(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: no frontmatter")
    raw, body = text[4:].split("\n---\n", 1)
    meta = {}
    for line in raw.splitlines():
        line = line.split(" #", 1)[0].rstrip()
        if not line.strip():
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip().strip('"') for v in value[1:-1].split(",") if v.strip()]
        else:
            value = value.strip('"')
        meta[key.strip()] = value
    return meta, body


def load(kind):
    pages = {}
    for p in sorted((ROOT / kind).glob("*.md")):
        meta, body = parse(p)
        pages[p.stem] = {"path": p, "meta": meta, "body": body}
    return pages
