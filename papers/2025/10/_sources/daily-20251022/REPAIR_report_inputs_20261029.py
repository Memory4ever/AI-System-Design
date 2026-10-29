"""Read same-day exact titles and existing necessary notes for report assembly."""
import json
import re
import sys
from pathlib import Path

from lxml import html

ROOT = Path(__file__).parent


def sections(name):
    text = (ROOT / name).read_text()
    parts = re.split(r"^## ([AR]\d+)\b[^\n]*\n", text, flags=re.M)
    return dict(zip(parts[1::2], parts[2::2]))


writer_name = "REPAIR_20261029.md"
reader_name = "REPAIR_REVIEW_20261029.md"
writer = sections(writer_name)
reader = sections(reader_name)
allowed = {
    writer_name: {"A7", "A8", "A14", "A15", "A16", "A17", "A19", "A20", "A24", "A28"},
    reader_name: {"R5", "R7", "R8", "R9", "R14", "R15", "R16", "R17", "R23", "R24", "R25", "R26", "R27", "R32", "R33", "R34", "R35", "R36", "R40", "R41"},
}
notes = {}
for name, data in [(writer_name, writer), (reader_name, reader)]:
    for section, body in data.items():
        if section not in allowed[name]:
            continue
        for line in body.splitlines():
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            ids = re.findall(r"(?<!\d)(1[567]\d{3})(?!\d)", cells[0])
            if len(ids) != 1 or len(cells) < 2:
                continue
            key = ids[0]
            score = re.findall(r"[0-3]\+[0-3]\+[0-3]=\d", line)
            notes.setdefault(key, {
                "scope": cells[1] if len(cells) >= 3 else cells[0],
                "evidence": cells[-1], "score": score[0] if score else None,
                "record": name, "section": section,
            })

special = {
    "16123": (writer_name, "A7", "exact-v1 §3–5/C.1", "2+1+2=5"),
    "16664": (writer_name, "A14", "exact-v1 AB/3.1/3.3/4.2", "1+1+2=4"),
    "16870": (writer_name, "A14", "exact-v1 AB/3/4.2/5.3/5.4/6", "1+1+2=4"),
    "16156": (writer_name, "A28", "exact-v1 AB/II-A–E/III", "2+1+2=5"),
    "16219": (reader_name, "R5", "exact-v1 3.2/4.1–4.3/5.1–5.2/6", "2+2+2=6"),
    "16641": (reader_name, "R27", "exact-v1 AB/2/3/5", "2+1+2=5"),
    "17363": (reader_name, "R34", "exact-v1 PDF指定Methods/评价域", "2+1+2=5"),
}
for key, (name, section, scope, score) in special.items():
    body = (writer if name == writer_name else reader)[section]
    paragraphs = [p for p in body.strip().split("\n\n") if p.strip()]
    if key == "16123":
        evidence = "\n\n".join(paragraphs[:2])
    else:
        matching = [p for p in paragraphs if re.search(r"(?<!\d)" + key + r"(?!\d)", p)]
        evidence = matching[-1] if key == "16219" else (matching[0] if matching else "")
    notes[key] = dict(scope=scope, evidence=evidence, score=score, record=name, section=section)

bounds = {x["id"].rsplit(".", 1)[-1]: x for x in json.loads((ROOT / "REPAIR_DISCOVERY_BOUNDS_20261029.json").read_text())}
output = []
for key in sys.argv[1:]:
    files = sorted(ROOT.glob(f"*2510.{key}v1*.html"))
    title = None
    for path in files:
        doc = html.fromstring(path.read_bytes())
        headings = doc.xpath('//h1[contains(concat(" ", normalize-space(@class), " "), " ltx_title ")]')
        value = ""
        if headings:
            heading = headings[0]
            for note in heading.xpath('.//*[contains(concat(" ", normalize-space(@class), " "), " ltx_pubnotes ")]'):
                note.drop_tree()
            for math in heading.xpath('.//*[local-name()="math"]'):
                replacement = html.Element("span")
                replacement.text = math.get("alttext") or math.text_content()
                replacement.tail = math.tail
                math.getparent().replace(math, replacement)
            for br in heading.xpath('.//br'):
                br.tail = " " + (br.tail or "")
            value = " ".join(heading.text_content().split())
        if value:
            title = value
            break
    if not title:
        title = bounds[key]["title"]
    output.append({"id": key, "title": title, **notes.get(key, {}), "bound": bounds[key]})
print(json.dumps(output, ensure_ascii=False))
