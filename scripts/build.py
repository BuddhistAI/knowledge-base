"""Regenerate the index tables in README.md and the "Used in workflows" list on each task page."""
import re
import sys

from pages import ROOT, load

START, END = "<!-- index:start -->", "<!-- index:end -->"
U_START, U_END = "<!-- used-in:start -->", "<!-- used-in:end -->"


def plural(n, word):
    return f"{n} {word}" + ("" if n == 1 else "s")


def build():
    tasks, flows = load("tasks"), load("workflows")
    used = {t: [] for t in tasks}
    for fid, f in flows.items():
        for t in f["meta"].get("tasks", []):
            used.setdefault(t, []).append(fid)

    out = {}
    lines = [START, "## Tasks", "",
             "| Task | Area | Benchmark | Best skills | Found in |", "| --- | --- | --- | --- | --- |"]
    for tid, t in sorted(tasks.items(), key=lambda kv: kv[1]["meta"]["title"].lower()):
        m = t["meta"]
        bench = "yes" if m.get("benchmarks") else "none yet, help build one"
        skills = ", ".join(m.get("skills", [])) or "none yet"
        lines.append(f"| [{m['title']}](tasks/{tid}.md) | {m['area']} | {bench} | {skills} | {plural(len(used.get(tid, [])), 'workflow')} |")
    lines += ["", "## Workflows", "",
              "| Workflow | Area | Owner | Kept | Status | Steps with a benchmark |", "| --- | --- | --- | --- | --- | --- |"]
    for fid, f in sorted(flows.items(), key=lambda kv: kv[1]["meta"]["title"].lower()):
        m = f["meta"]
        ft = m.get("tasks", [])
        measured = sum(1 for t in ft if t in tasks and tasks[t]["meta"].get("benchmarks"))
        kept = "linked (owner's document)" if m.get("mode") == "linked" else "here"
        lines.append(f"| [{m['title']}](workflows/{fid}.md) | {m['area']} | {m['owner']} | {kept} | {m['status']} | {measured} of {plural(len(ft), 'task')} |")
    lines.append(END)
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    out[readme] = re.sub(re.escape(START) + ".*?" + re.escape(END), "\n".join(lines), text, flags=re.S)

    for tid, t in tasks.items():
        text = t["path"].read_text(encoding="utf-8")
        fl = used.get(tid, [])
        block = [U_START, "## Found in workflows", ""]
        block += [f"- [{flows[f]['meta']['title']}](../workflows/{f}.md) ({flows[f]['meta']['owner']})" for f in fl] or \
                 ["No workflow page uses this task yet. [Share a workflow](https://github.com/BuddhistAI/wiki/issues/new?template=share-workflow.yml) that does."]
        block.append(U_END)
        out[t["path"]] = re.sub(re.escape(U_START) + ".*?" + re.escape(U_END), "\n".join(block), text, flags=re.S)
    return out


if __name__ == "__main__":
    check = "--check" in sys.argv
    stale = []
    for path, text in build().items():
        if path.read_text(encoding="utf-8") != text:
            stale.append(path.relative_to(ROOT))
            if not check:
                path.write_text(text, encoding="utf-8")
    if check and stale:
        sys.exit("Out of date, run python3 scripts/build.py: " + ", ".join(map(str, stale)))
    print("built" if not check else "up to date")
