"""Directory of Buddhist AI projects and datasets: load directory/*.yml, check entries, render directory/README.md."""
import re

import yaml

from pages import ROOT

REPO = "https://github.com/BuddhistAI/knowledge-base"
START, END = "<!-- directory:start -->", "<!-- directory:end -->"
KINDS = {
    "projects": ["Translation and dictionaries", "Text libraries and search", "OCR and digitization", "Language tools",
                 "Speech", "AI models", "Chatbots and Q&A", "Agent skills and tools", "Practice and teaching",
                 "Research and community", "Other lists"],
    "datasets": ["Benchmarks", "Texts and corpora", "Parallel texts and translation", "OCR and page layout", "Speech",
                 "Language annotation", "Metadata, outlines and knowledge", "Q&A and instruction data"],
}
FIELDS = ["name", "url", "org", "kind", "what", "languages", "open", "updated"]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load(section):
    path = ROOT / "directory" / f"{section}.yml"
    lines = path.read_text(encoding="utf-8").splitlines()
    entries = yaml.safe_load("\n".join(lines)) or []
    starts = [i + 1 for i, l in enumerate(lines) if l.startswith("- name:")]
    for e, line in zip(entries, starts):
        e["_line"] = line
    return entries


def check(task_ids):
    errors = []
    for section, kinds in KINDS.items():
        seen = set()
        for e in load(section):
            where = f"directory/{section}.yml:{e.get('_line', '?')} ({e.get('name', '?')})"
            errors += [f"{where}: missing '{k}'" for k in FIELDS if k not in e]
            if e.get("kind") not in kinds:
                errors.append(f"{where}: kind must be one of {kinds}")
            if not str(e.get("url", "")).startswith("https://"):
                errors.append(f"{where}: url must start with https://")
            if not isinstance(e.get("languages"), list) or not e.get("languages"):
                errors.append(f"{where}: languages must be a non-empty list")
            if not re.fullmatch(r"(\d{4}(-\d{2})?)?", str(e.get("updated", ""))):
                errors.append(f"{where}: updated must be YYYY-MM, YYYY or empty")
            errors += [f"{where}: task {t!r} has no page in tasks/" for t in e.get("tasks", []) if t not in task_ids]
            key = (e.get("name"), e.get("url"))
            if key in seen:
                errors.append(f"{where}: duplicate entry")
            seen.add(key)
    return errors


def when(updated):
    s = str(updated or "")
    if re.fullmatch(r"\d{4}-\d{2}", s):
        return f"{MONTHS[int(s[5:]) - 1]} {s[:4]}"
    return s or "–"


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def anchor(text):
    return re.sub(r"[^a-z0-9 -]", "", text.lower()).strip().replace(" ", "-")


def table(section, entries, tasks):
    head = "Project" if section == "projects" else "Dataset"
    out = [f"| {head} | Made by | What it does | Languages | How open | Last activity |",
           "| --- | --- | --- | --- | --- | --- |"]
    for e in entries:
        what = cell(e["what"])
        if e.get("tasks"):
            what += " Tasks: " + ", ".join(f"[{tasks[t]}](../tasks/{t}.md)" for t in e["tasks"]) + "."
        edit = f"[✎]({REPO}/blob/main/directory/{section}.yml#L{e['_line']} \"Edit this entry\")"
        out.append(f"| **[{cell(e['name'])}]({e['url']})** {edit} | {cell(e['org'])} | {what} | "
                   f"{cell(', '.join(map(str, e['languages'])))} | {cell(e['open'])} | {when(e['updated'])} |")
    return out


def render(tasks):
    """tasks: {task id: title}. Returns the generated block for directory/README.md."""
    lines = [START]
    for section, kinds in KINDS.items():
        entries = load(section)
        title = section.capitalize()
        lines += ["", f"## {title}", "", f"{len(entries)} {section}. Jump to: " +
                  " · ".join(f"[{k}](#{anchor(k)}{'-1' if section == 'datasets' and k in KINDS['projects'] else ''})"
                             for k in kinds if any(e['kind'] == k for e in entries)), ""]
        for k in kinds:
            group = [e for e in entries if e["kind"] == k]
            if group:
                lines += [f"### {k}", ""] + table(section, group, tasks) + [""]
    lines.append(END)
    return "\n".join(lines)
