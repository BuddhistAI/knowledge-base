"""Languages section: one page per Buddhist language (languages/<id>.md) and a country list (languages/countries.yml).

build.py renders the two overview tables in languages/README.md and, on each language page,
the list of Directory entries in that language. check.py runs check().
"""
import re

import yaml

import charts
import directory
from pages import ROOT, parse

DIR = ROOT / "languages"
START, END = "<!-- languages:start -->", "<!-- languages:end -->"
D_START, D_END = "<!-- in-directory:start -->", "<!-- in-directory:end -->"
KEYS = ["id", "title", "kind", "group", "countries", "scripts", "speakers", "directory_names", "resource_level",
        "google_translate", "recommendation", "confidence", "updated", "contributors"]
KINDS = ["classical", "modern", "classical and modern"]
LEVELS = ["high", "medium", "low", "very low"]
CONFIDENCE = ["high", "medium", "low"]
SECTIONS = ["## Summary", "## Writing and text input", "## Data", "## Speech", "## Machine translation",
            "## AI projects", "## Recommendation", "## Sources"]
COUNTRY_KEYS = ["name", "region", "buddhists", "traditions", "languages", "source"]


def load():
    pages = {}
    for p in sorted(DIR.glob("*.md")):
        if p.name == "README.md":
            continue
        meta, body = parse(p)
        pages[p.stem] = {"path": p, "meta": meta, "body": body}
    return pages


def countries():
    return yaml.safe_load((DIR / "countries.yml").read_text(encoding="utf-8")) or []


def in_directory(names):
    """Directory entries whose languages list names one of `names`."""
    wanted = {n.lower() for n in names}
    out = {}
    for section in directory.KINDS:
        out[section] = [e for e in directory.load(section) if wanted & {str(l).lower() for l in e["languages"]}]
    return out


def check():
    errors = []
    langs = load()
    for lid, l in langs.items():
        m, where = l["meta"], f"languages/{lid}.md"
        errors += [f"{where}: missing '{k}'" for k in KEYS if k not in m]
        if m.get("id") != lid:
            errors.append(f"{where}: id must match the file name")
        if m.get("kind") not in KINDS:
            errors.append(f"{where}: kind must be one of {KINDS}")
        if m.get("resource_level") not in LEVELS:
            errors.append(f"{where}: resource_level must be one of {LEVELS}")
        if m.get("confidence") not in CONFIDENCE:
            errors.append(f"{where}: confidence must be one of {CONFIDENCE}")
        if not re.fullmatch(r"\d{4}-\d{2}", m.get("updated", "")):
            errors.append(f"{where}: updated must be YYYY-MM")
        errors += [f"{where}: missing section {s!r}" for s in SECTIONS if s not in l["body"]]
        if m.get("speakers_n") and charts.number(m["speakers_n"]) is None:
            errors.append(f"{where}: speakers_n must be a whole number")
        if D_START not in l["body"]:
            errors.append(f"{where}: missing {D_START} block")
    for c in countries():
        where = f"languages/countries.yml ({c.get('name', '?')})"
        errors += [f"{where}: missing '{k}'" for k in COUNTRY_KEYS if k not in c]
        errors += [f"{where}: language {x!r} has no page in languages/" for x in c.get("languages", []) if x not in langs]
        if c.get("buddhists_n") not in (None, "") and charts.number(c["buddhists_n"]) is None:
            errors.append(f"{where}: buddhists_n must be a whole number")
        if not str(c.get("source", "")).startswith("https://"):
            errors.append(f"{where}: source must be a https link")
    return errors


def cell(text):
    """Table cell text; drops page-local source numbers like [1], which mean nothing in the overview."""
    text = re.sub(r"\s*\[\d+\]", "", str(text))
    return text.replace("|", "\\|").replace("\n", " ")


def render_index():
    langs = load()
    svg, missing = charts.speakers_chart({lid: l["meta"] for lid, l in langs.items()})
    lines = [START, "## Where help reaches the most people", "",
             "This chart compares how many people speak each language with how much AI support the language has. "
             "A language in the shaded area has many speakers but weak AI. Work there (a benchmark, a dataset, a reviewed glossary "
             "or a tested skill) can help the most people. Hover or tab to a dot to see the numbers, and click it to open the page.", "",
             "What the chart shows (November 2026):", "",
             "- **Tibetan** is the largest language with weak AI support: about 6 million speakers. Newari and Dzongkha follow, with less than 1 million each.",
             "- Buryat, Tuvan, Kalmyk and the Himalayan languages are small (under 500,000 speakers each) and have almost no AI support. Here a small dataset or test already makes a large difference for the community, but it reaches fewer people.",
             "- Burmese, Nepali, Khmer, Sinhala, Lao and Mongolian have medium AI support and together about 125 million speakers. A Buddhist glossary and a small translation test for each could improve quality for many people.",
             "- The classical languages (Pali, Sanskrit, Classical Chinese) are not on the chart. They matter as source languages for translation, not by number of speakers.", "",
             f'<figure class="chart-fig">{svg}<figcaption>Speakers are first-language and second-language speakers where the source gives both. '
             "Sources and years are on each language page. Speakers are not the same as Buddhists: for example, most Chinese speakers are not Buddhist, "
             "and the map below shows Buddhists by country. "
             + (f"Not shown, because there is no reliable speaker count: {', '.join(sorted(missing))}. " if missing else "")
             + "Pali, Sanskrit and Classical Chinese have no native speakers; they are read by monastics, scholars and translators.</figcaption></figure>", "",
             "## Buddhists by country", "",
             charts.map_block(countries()), "",
             '<script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>',
             '<script src="https://cdn.jsdelivr.net/npm/topojson-client@3.1.0/dist/topojson-client.min.js"></script>',
             "<script src=\"{{ '/assets/buddhist-map.js' | relative_url }}\"></script>", "",
             "## Languages", "",
             "| Language | Kind | Where | Speakers | AI resources | Google Translate | To translate into it, use | Confidence | Directory |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    order = {g: i for i, g in enumerate(["Tibetic", "Indic", "Southeast Asian", "Chinese", "Japanese, Korean, Vietnamese", "Mongolic and Turkic"])}
    for lid, l in sorted(langs.items(), key=lambda kv: (order.get(kv[1]["meta"]["group"], 99), kv[1]["meta"]["title"].lower())):
        m = l["meta"]
        found = in_directory(m["directory_names"])
        n = len(found["projects"]) + len(found["datasets"])
        lines.append(f"| [{cell(m['title'])}]({lid}.md) | {m['kind']} | {cell(', '.join(m['countries']))} | {cell(m['speakers'])} | "
                     f"{m['resource_level']} | {cell(m['google_translate'])} | {cell(m['recommendation'])} | {m['confidence']} | {n} |")
    names = {lid: l["meta"]["title"] for lid, l in langs.items()}
    lines += ["", "## Countries and regions", "",
              "| Country or region | Buddhists | Main traditions | Languages | Source |", "| --- | --- | --- | --- | --- |"]
    for region in dict.fromkeys(c["region"] for c in countries()):
        lines.append(f"| **{cell(region)}** | | | | |")
        for c in countries():
            if c["region"] != region:
                continue
            ls = ", ".join(f"[{names[x]}]({x}.md)" for x in c["languages"])
            lines.append(f"| {cell(c['name'])} | {cell(c['buddhists'])} | {cell(c['traditions'])} | {ls} | [source]({c['source']}) |")
    lines.append(END)
    return "\n".join(lines)


def render_page(meta):
    found = in_directory(meta["directory_names"])
    block = [D_START, "## In the Directory", "",
             f"Projects and datasets in the [Directory](../directory/README.md) that list {', '.join(meta['directory_names'])}. "
             "This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).", ""]
    for section in directory.KINDS:
        entries = found[section]
        block.append(f"**{section.capitalize()}** ({len(entries)})")
        block.append("")
        if not entries:
            block.append("None listed yet.")
        for e in entries:
            block.append(f"- [{e['name']}]({e['url']}) ({cell(e['org'])}): {cell(e['what'])}")
        block.append("")
    block.append(D_END)
    return "\n".join(block)


def build(out):
    readme = DIR / "README.md"
    text = readme.read_text(encoding="utf-8")
    out[readme] = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda m: render_index(), text, flags=re.S)
    for lid, l in load().items():
        text = l["path"].read_text(encoding="utf-8")
        out[l["path"]] = re.sub(re.escape(D_START) + ".*?" + re.escape(D_END), lambda m: render_page(l["meta"]), text, flags=re.S)
    return out
