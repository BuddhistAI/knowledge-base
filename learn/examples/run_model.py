#!/usr/bin/env python3
"""Run one AI model on a BuddhistAI benchmark and save predictions.jsonl, ready for the task's scorer.

Used by the tutorial "Evaluate your first model on a Buddhist task":
https://buddhistai.github.io/knowledge-base/learn/evaluate-your-first-model.html

python3 run_model.py --data small.jsonl --model <openrouter-model-id> --out predictions.jsonl
python3 run_model.py --data test.jsonl --dry-run --out predictions.jsonl     # no API call: empty answers

It calls OpenRouter (one API key for many models; set OPENROUTER_API_KEY). Standard library only.
The prompt is for the toc-extraction task; change PROMPT for another task. Token counts from the API are
added up and printed at the end, so you can say what the run cost.
"""
import argparse, json, os, re, sys, time, urllib.request

PROMPT = """You read a Tibetan Buddhist commentary passage and list its outline (sa bcad) headings.
Return only JSON: {"entries": [{"title": "...", "level": 1, "anchor": "..."}]}
- title: the heading's topic, in Tibetan, as written in the text.
- level: 1 for top-level headings, 2 for their subsections, and so on.
- anchor: the first 40 characters of the sentence that introduces the heading, copied exactly from the text.
List the headings in reading order. If there are none, return {"entries": []}.

Passage:
"""


def ask(model, text, key):
    body = json.dumps({"model": model, "temperature": 1.0, "max_tokens": 8000,
                       "messages": [{"role": "user", "content": PROMPT + text}]}).encode()
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body, headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        reply = json.load(r)
    content = reply["choices"][0]["message"]["content"] or ""
    m = re.search(r"\{.*\}", content, re.S)  # the JSON object, even if the model adds words around it
    try:
        output = json.loads(m.group(0)) if m else {"entries": []}
    except json.JSONDecodeError:
        output = {"entries": []}
    return output, reply.get("usage", {})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, help="the benchmark's test.jsonl")
    ap.add_argument("--model", help="a model id copied from https://openrouter.ai/models")
    ap.add_argument("--out", default="predictions.jsonl")
    ap.add_argument("--limit", type=int, default=0, help="only the first N items (start small: it costs money)")
    ap.add_argument("--dry-run", action="store_true", help="do not call the API; write empty answers")
    a = ap.parse_args()
    key = os.environ.get("OPENROUTER_API_KEY")
    if not a.model and not a.dry_run:
        sys.exit("Give --model (copy the id from https://openrouter.ai/models).")
    if not key and not a.dry_run:
        sys.exit("Set OPENROUTER_API_KEY first (or use --dry-run).")
    items = [json.loads(line) for line in open(a.data, encoding="utf-8") if line.strip()]
    if a.limit:
        items = items[:a.limit]
    tokens = {"prompt_tokens": 0, "completion_tokens": 0}
    with open(a.out, "w", encoding="utf-8") as out:
        for i, item in enumerate(items, 1):
            output, usage = ({"entries": []}, {}) if a.dry_run else ask(a.model, item["input"], key)
            for k in tokens:
                tokens[k] += usage.get(k, 0)
            out.write(json.dumps({"id": item["id"], "output": output}, ensure_ascii=False) + "\n")
            print(f"{i}/{len(items)} {item['id']}: {len(output.get('entries', []))} headings", flush=True)
            time.sleep(0 if a.dry_run else 0.5)
    print(f"Wrote {a.out}. Tokens: {tokens['prompt_tokens']} in, {tokens['completion_tokens']} out.")


if __name__ == "__main__":
    main()
