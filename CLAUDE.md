# Notes for agents working in this repo

- This is the BuddhistAI wiki: the shared reference that defines Buddhist tasks (`tasks/<task-id>.md`) and the workflows they come from (`workflows/<id>.md`). Framing is Buddhist tasks, not only texts.
- Task IDs are shared with buddhist-benchmarks `tasks/index.json` and buddhist-skills skill names (`<task>-<language>`). A new task page needs a matching (planned) entry there.
- Workflows have an owner. A `linked` workflow lives in its owner's document: summarize it in our own words and link it, never copy it. A `hosted` workflow's owner reviews changes (CODEOWNERS).
- Never hand-edit the README index tables or the "Found in workflows" blocks. Run `python3 scripts/build.py`, then `python3 scripts/check.py`.
- Credit people in `contributors`. Neutral branding: WeBuddhist is one contributor among others.
- Workflow pages are semver-versioned in `version`; `source_version` is the owner's own version.
