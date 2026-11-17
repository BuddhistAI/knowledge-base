"""Charts for the Languages page: a speakers-by-AI-support chart (static SVG) and a map of Buddhists by country.

The chart is plain SVG built here, so it works without JavaScript. Colors are the design-system
variables (--lapis, --saffron, ...), so light and dark mode follow the site. The map is drawn in the
browser by assets/buddhist-map.js from the JSON block this module writes.
"""
import html
import json
import math

LEVELS = ["high", "medium", "low", "very low"]           # top to bottom
GAP = {"low", "very low"}                                 # rows drawn as "AI gap"
W, LEFT, RIGHT, TOP, ROW = 760, 118, 24, 64, 84
XMIN, XMAX = 4, 9.4                                       # log10 range: 10K to about 2.5 billion
TICKS = [(4, "10K"), (5, "100K"), (6, "1M"), (7, "10M"), (8, "100M"), (9, "1B")]


def x_of(n):
    return LEFT + (math.log10(n) - XMIN) / (XMAX - XMIN) * (W - LEFT - RIGHT)


def compact(n):
    for size, unit in ((1e9, " billion"), (1e6, " million"), (1e3, ",000")):
        if n >= size:
            v = n / size
            if unit == ",000":
                return f"{n:,.0f}"
            return f"{v:.1f}".rstrip("0").rstrip(".") + unit
    return str(n)


def number(value):
    try:
        return int(str(value).replace(",", "").replace("_", ""))
    except ValueError:
        return None


def speakers_chart(langs):
    """langs: {id: meta}. Returns (svg html, list of titles without a number)."""
    rows = {lvl: [] for lvl in LEVELS}
    missing = []
    for lid, m in langs.items():
        n = number(m.get("speakers_n", ""))
        if n:
            rows[m["resource_level"]].append((n, lid, m))
        else:
            missing.append(m["title"])
    height = TOP + ROW * len(LEVELS) + 40
    out = [f'<svg class="chart" viewBox="0 0 {W} {height}" role="img" aria-labelledby="sp-title sp-desc" '
           f'xmlns="http://www.w3.org/2000/svg" font-family="var(--f-body)">',
           '<title id="sp-title">Speakers of each Buddhist language, by how much AI support the language has</title>',
           '<desc id="sp-desc">Each dot is a language. Left to right: number of speakers, on a log scale. '
           'Top to bottom: AI resources, from high to very low. Languages in the lower right have many speakers and little AI support.</desc>']
    # opportunity zone: low and very low rows, 500,000 speakers or more
    zx, zy = x_of(5e5), TOP + ROW * 2
    out.append(f'<rect x="{zx:.1f}" y="{zy}" width="{W - RIGHT - zx:.1f}" height="{ROW * 2}" rx="8" class="zone"/>')
    out.append(f'<text x="{W - RIGHT - 10}" y="{zy + ROW * 2 - 10}" text-anchor="end" class="zone-label">'
               'Many speakers, little AI support</text>')
    # legend
    out.append(f'<circle cx="{LEFT + 6}" cy="20" r="6" class="dot ok"/><text x="{LEFT + 18}" y="24" class="lab">'
               'High or medium AI support</text>')
    out.append(f'<circle cx="{LEFT + 226}" cy="20" r="6" class="dot gap"/><text x="{LEFT + 238}" y="24" class="lab">'
               'Low or very low AI support (AI gap)</text>')
    # grid and x axis
    base = TOP + ROW * len(LEVELS)
    for v, label in TICKS:
        x = x_of(10 ** v)
        out.append(f'<line x1="{x:.1f}" y1="{TOP}" x2="{x:.1f}" y2="{base}" class="grid"/>')
        out.append(f'<text x="{x:.1f}" y="{base + 18}" text-anchor="middle" class="tick">{label}</text>')
    out.append(f'<text x="{W - RIGHT}" y="{base + 36}" text-anchor="end" class="tick">Speakers (log scale)</text>')
    for i, lvl in enumerate(LEVELS):
        cy = TOP + ROW * i + ROW / 2
        out.append(f'<line x1="{LEFT}" y1="{TOP + ROW * (i + 1)}" x2="{W - RIGHT}" y2="{TOP + ROW * (i + 1)}" class="grid"/>')
        out.append(f'<text x="{LEFT - 12}" y="{cy + 4}" text-anchor="end" class="axis">{lvl.capitalize()}</text>')
        # labels alternate above and below; move further out when they would overlap
        placed = []
        for n, lid, m in sorted(rows[lvl]):
            x = x_of(n)
            name = m.get("short_title") or m["title"]
            w = 7 * len(name) + 6
            for dy in (-14, 22, -30, 38):
                if all(abs(x - px) > (w + pw) / 2 or dy != pdy for px, pw, pdy in placed):
                    break
            placed.append((x, w, dy))
            kind = "gap" if lvl in GAP else "ok"
            # a thin leader line ties a far label to its dot
            lead = "" if abs(dy) < 20 else (f'<line x1="{x:.1f}" y1="{cy + (8 if dy > 0 else -8)}" x2="{x:.1f}" '
                                            f'y2="{cy + dy + (-12 if dy > 0 else 4)}" class="lead"/>')
            basis = f", {m['speakers_basis']}" if m.get("speakers_basis") else ""
            tip = (f"{m['title']}: about {compact(n)} speakers ({m.get('speakers_year', '')}{basis}). AI resources: {lvl}. "
                   f"To translate into it: {m['recommendation']}.")
            out.append(f'<a href="{lid}.html" tabindex="0" class="pt"><title>{html.escape(tip)}</title>'
                       f'<circle cx="{x:.1f}" cy="{cy}" r="12" class="hit"/>'
                       f'<circle cx="{x:.1f}" cy="{cy}" r="6" class="dot {kind}"/>'
                       f'<text x="{x:.1f}" y="{cy + dy}" text-anchor="middle" class="lab">{html.escape(name)}</text>{lead}</a>')
    out.append(f'<text x="{LEFT - 12}" y="{TOP - 10}" text-anchor="end" class="tick">AI resources</text>')
    out.append("</svg>")
    return "".join(out), missing


def map_data(countries):
    rows = []
    for c in countries:
        n = number(c.get("buddhists_n", ""))
        if c.get("iso") and n:
            rows.append({"iso": str(c["iso"]).zfill(3), "name": c["name"], "n": n, "label": c["buddhists"]})
    return json.dumps(rows, ensure_ascii=False)


def map_block(countries):
    return ('<figure class="chart-fig"><div id="buddhist-map" class="map" aria-hidden="true"></div>'
            f'<script type="application/json" id="buddhist-map-data">{map_data(countries)}</script>'
            '<figcaption>Number of Buddhists by country (mostly Pew Research Center, 2020). A stronger blue means more Buddhists. Counts marked as our estimate are the Pew share times the Pew population. '
            'Regions inside a country, such as Tibet, Inner Mongolia, Buryatia, Kalmykia and Tuva, are not shown separately; '
            'see the table below. The same numbers are in the table "Countries and regions".</figcaption></figure>')
