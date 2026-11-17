"""Check frontmatter and links between task and workflow pages, and the directory entries."""
import re
import subprocess
import sys

from pages import ROOT, load
import directory

AREAS = {"Texts", "Translation", "Study and teaching", "Art and visual", "Practice", "Centers and projects", "Personal setups"}
TASK_KEYS = ["id", "title", "area", "summary", "status", "related", "benchmarks", "leaderboard", "skills", "contributors"]
FLOW_KEYS = ["id", "title", "area", "owner", "contributors", "mode", "source", "source_version", "languages", "tasks", "status", "version", "updated"]
SECTIONS = ["## Definition", "## Input and output", "## Examples", "## Edge cases", "## Languages and traditions", "## How it is measured", "## Help wanted"]
errors = []

tasks, flows = load("tasks"), load("workflows")
for tid, t in tasks.items():
    m, where = t["meta"], f"tasks/{tid}.md"
    errors += [f"{where}: missing '{k}'" for k in TASK_KEYS if k not in m]
    if m.get("id") != tid:
        errors.append(f"{where}: id must match the file name")
    if m.get("area") not in AREAS:
        errors.append(f"{where}: unknown area {m.get('area')!r}")
    if m.get("status") not in ("planned", "measured"):
        errors.append(f"{where}: status must be planned or measured")
    if (m.get("status") == "measured") != bool(m.get("benchmarks")):
        errors.append(f"{where}: status measured exactly when benchmarks is not empty")
    errors += [f"{where}: related task {r!r} has no page" for r in m.get("related", []) if r not in tasks]
    errors += [f"{where}: missing section {s!r}" for s in SECTIONS if s not in t["body"]]

for fid, f in flows.items():
    m, where = f["meta"], f"workflows/{fid}.md"
    errors += [f"{where}: missing '{k}'" for k in FLOW_KEYS if k not in m]
    if m.get("id") != fid:
        errors.append(f"{where}: id must match the file name")
    if m.get("area") not in AREAS:
        errors.append(f"{where}: unknown area {m.get('area')!r}")
    if m.get("mode") not in ("linked", "hosted"):
        errors.append(f"{where}: mode must be linked or hosted")
    if m.get("mode") == "linked" and not m.get("source", "").startswith("http"):
        errors.append(f"{where}: a linked workflow needs a source link")
    if m.get("status") not in ("draft", "reviewed", "stable"):
        errors.append(f"{where}: status must be draft, reviewed or stable")
    if not re.fullmatch(r"\d+\.\d+\.\d+", m.get("version", "")):
        errors.append(f"{where}: version must be semver")
    if not m.get("owner"):
        errors.append(f"{where}: every workflow needs an owner")
    errors += [f"{where}: task {t!r} has no page in tasks/" for t in m.get("tasks", []) if t not in tasks]
    linked = set(re.findall(r"\(\.\./tasks/([a-z0-9-]+)\.md\)", f["body"]))
    errors += [f"{where}: links to missing task {t!r}" for t in linked if t not in tasks]
    errors += [f"{where}: step table links {t!r} but frontmatter tasks does not list it" for t in linked - set(m.get("tasks", []))]

errors += directory.check(set(tasks))

r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py"), "--check"], capture_output=True, text=True)
if r.returncode:
    errors.append((r.stderr or r.stdout).strip())

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(tasks)} tasks, {len(flows)} workflows, {len(directory.load('projects'))} projects, {len(directory.load('datasets'))} datasets")
