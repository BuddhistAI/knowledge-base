"""Open a pull request that adds CLAUDE.md and AGENTS.md to every BuddhistAI repo that has no CLAUDE.md.

Needs ORG_REPOS_TOKEN: a fine-grained token for the BuddhistAI org, all repositories,
with Contents: read and write, Pull requests: read and write, Metadata: read.
Run with --dry-run to only list the repos that need it.
"""
import base64, json, os, sys, urllib.error, urllib.request
from pathlib import Path

ORG, BRANCH = "BuddhistAI", "agent-notes"
API = "https://api.github.com"
TOKEN = os.environ.get("ORG_REPOS_TOKEN") or os.environ.get("GITHUB_TOKEN")
DRY = "--dry-run" in sys.argv
TEMPLATE = (Path(__file__).resolve().parent / "agent-notes" / "CLAUDE.md").read_text()


def call(method, path, body=None, ok404=False):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body is not None else None)
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e:
        if ok404 and e.code == 404:
            return None
        raise SystemExit(f"{method} {path}: {e.code} {e.read().decode()[:300]}")


def repos():
    page = 1
    while True:
        batch = call("GET", f"/orgs/{ORG}/repos?type=all&per_page=100&page={page}")
        if not batch:
            return
        yield from batch
        page += 1


def main():
    missing = []
    for r in repos():
        if r["archived"] or r["fork"]:
            continue
        name, base = r["name"], r["default_branch"]
        if r.get("size", 0) == 0:  # empty repo, nothing to branch from
            continue
        if call("GET", f"/repos/{ORG}/{name}/contents/CLAUDE.md?ref={base}", ok404=True):
            continue
        missing.append(name)
        if DRY:
            continue
        if call("GET", f"/repos/{ORG}/{name}/pulls?state=open&head={ORG}:{BRANCH}")[:1]:
            print(f"{name}: pull request already open")
            continue
        sha = call("GET", f"/repos/{ORG}/{name}/git/ref/heads/{base}")["object"]["sha"]
        if not call("GET", f"/repos/{ORG}/{name}/git/ref/heads/{BRANCH}", ok404=True):
            call("POST", f"/repos/{ORG}/{name}/git/refs", {"ref": f"refs/heads/{BRANCH}", "sha": sha})
        text = TEMPLATE.replace("{repo}", name)
        for f in ("CLAUDE.md", "AGENTS.md"):
            if call("GET", f"/repos/{ORG}/{name}/contents/{f}?ref={BRANCH}", ok404=True):
                continue
            call("PUT", f"/repos/{ORG}/{name}/contents/{f}", {
                "message": f"Add {f}: start here (handbook, Development board, rules)",
                "content": base64.b64encode(text.encode()).decode(), "branch": BRANCH})
        pr = call("POST", f"/repos/{ORG}/{name}/pulls", {
            "title": "Add agent notes (CLAUDE.md, AGENTS.md)", "head": BRANCH, "base": base,
            "body": "Every BuddhistAI repo has a short `CLAUDE.md` / `AGENTS.md` so coding agents read the "
                    "[maintainer handbook](https://buddhistai.github.io/knowledge-base/handbook/) first. "
                    "Please replace the last line with this repo's role and commands, then merge.\n\n"
                    "Opened by the weekly `agent-notes` check in BuddhistAI/knowledge-base."})
        print(f"{name}: opened {pr['html_url']}")
    print("Repos without CLAUDE.md:", ", ".join(missing) or "none")


main()
