"""Bounded Sep15 recovery. Raw captures and snapshots are append-only."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[4]
REPORT = ROOT / "papers/2025/09/16/README.md"


def save(path, value):
    with path.open("x") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def capture(name, url, accept="application/vnd.api+json"):
    run_date = datetime.now(timezone.utc).strftime("%Y%m%d")
    raw = BASE / ("REPAIR_" + name + "_" + run_date + ".raw")
    meta = BASE / ("REPAIR_" + name + "_" + run_date + ".request.json")
    if raw.exists() or meta.exists():
        raise FileExistsError(name)
    record = {"url": url, "method": "GET", "checked_utc": datetime.now(timezone.utc).isoformat(),
              "headers": {"User-Agent": "AI-System-Design Sep15 bounded recovery", "Accept": accept}}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=record["headers"]), timeout=45) as response:
            body = response.read()
            record.update(status=response.status, final_url=response.url)
    except urllib.error.HTTPError as error:
        body = error.read()
        record.update(status=error.code, error=str(error))
    except Exception as error:
        body = b""
        record["error"] = str(error)
    with raw.open("xb") as stream:
        stream.write(body)
    record.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest(), finished_utc=datetime.now(timezone.utc).isoformat())
    save(meta, record)
    print(name, record.get("status"), len(body), record.get("error", ""), flush=True)


def baseline():
    report = REPORT.read_bytes()
    with (BASE / "REPAIR_BASELINE_README_20261022.md").open("xb") as stream:
        stream.write(report)
    paths = [str(REPORT.relative_to(ROOT)), str(BASE.relative_to(ROOT))]
    result = {"checked_utc": datetime.now(timezone.utc).isoformat(), "report_bytes": len(report),
              "report_sha256": hashlib.sha256(report).hexdigest()}
    for name, command in {
        "head": ["git", "rev-parse", "HEAD"], "status": ["git", "status", "--short"],
        "working": ["git", "diff", "--", *paths], "cached": ["git", "diff", "--cached", "--", *paths],
    }.items():
        output = subprocess.run(command, cwd=ROOT, capture_output=True, check=True).stdout
        target = BASE / ("REPAIR_BASELINE_" + name + "_20261022.txt")
        with target.open("xb") as stream:
            stream.write(output)
        result[name] = {"file": target.name, "sha256": hashlib.sha256(output).hexdigest()}
    save(BASE / "REPAIR_BASELINE_20261022.json", result)
    print(json.dumps(result, ensure_ascii=False))


def old_dates():
    first = (BASE / "SUP_FIRST_20261012.md").read_text().split("### 精确日期保留身份", 1)[1]
    first = first.split("这83个P", 1)[0]
    recent = set("2509." + item for item in re.findall(r"(?<!\d)(\d{5})(?:v\d+)?", first))
    if len(recent) != 83:
        raise ValueError(("expected old83", len(recent)))
    old = set(re.findall(r"arxiv.org/abs/(\d{4}\.\d{5})", (BASE / "DISCOVERY_SCREENING.md").read_text()))
    identities = sorted(recent | old)
    save(BASE / "REPAIR_OLD_DATE_IDS_20261022.json", {"old83": sorted(recent), "original_discovery": sorted(old), "union": identities})
    for start in range(0, len(identities), 50):
        query = "doi:(" + " OR ".join("10.48550/arxiv." + identity for identity in identities[start:start + 50]) + ")"
        url = "https://api.datacite.org/dois?" + urllib.parse.urlencode({"query": query, "page[size]": 100, "page[number]": 1})
        capture("DATE_" + str(start), url)


def discover():
    themes = {
        "MODEL": (["cs.CL", "cs.LG"], ['"language model"', '"language models"', "LLM", "LLMs", "transformer", "transformers", '"mixture of experts"', '"mixture-of-experts"', "MoE", '"foundation model"', '"foundation models"', '"long context"', '"long-context"']),
        "SYSTEMS": (["cs.DC", "cs.AR", "cs.PL", "cs.OS", "cs.PF"], ["GPU", "GPUs", '"language model"', '"language models"', "LLM", "LLMs", "transformer", "transformers", "inference", '"model training"', "kernel", "kernels", "compiler", "compilers", "compilation", "accelerator", "accelerators"]),
        "MULTIMODAL": (["cs.CV", "cs.RO"], ['"vision language"', '"vision-language"', '"vision-language model"', '"vision-language models"', '"world model"', '"world models"', '"foundation model"', '"foundation models"', "diffusion", '"flow matching"', "VLA", "VLAs", "VLM", "VLMs", "MLLM", "MLLMs", "multimodal"]),
        "AGENTS": (["cs.AI", "cs.IR", "cs.MA"], ['"language model"', '"language models"', "LLM", "LLMs", "agent", "agents", "agentic", '"retrieval augmented"', '"retrieval-augmented"', '"tool use"', '"tool calling"', "tool", "tools"]),
    }
    specs = []
    for name, (categories, terms) in themes.items():
        lexical = "(" + " OR ".join(terms) + ")"
        query = "subjects.subject:(" + " OR ".join('"' + category + '"' for category in categories) + ")"
        query += " AND (titles.title:" + lexical + " OR descriptions.description:" + lexical + ")"
        query += " AND registered:[2025-09-14T16:00:00Z TO 2025-09-15T16:00:00Z]"
        specs.append({"name": name, "categories": categories, "terms": terms, "query": query})
    save(BASE / "REPAIR_DISCOVERY_SPEC_20261022.json", specs)
    for spec in specs:
        url = "https://api.datacite.org/dois?" + urllib.parse.urlencode({
            "client-id": "arxiv.content", "query": spec["query"], "page[size]": 200, "page[number]": 1, "sort": "registered"})
        capture("DISCOVER_" + spec["name"] + "_P1", url)


def inventory():
    sys.path.insert(0, str(ROOT / "scripts"))
    from arxiv_publication_date import publication_date_envelope
    records = {}
    themes = []
    for name in ("MODEL", "SYSTEMS", "MULTIMODAL", "AGENTS"):
        payload = json.loads((BASE / ("REPAIR_DISCOVER_" + name + "_P1_20261022.raw")).read_text())
        themes.append({"theme": name, "total": payload["meta"]["total"], "returned": len(payload["data"]),
                       "next": payload.get("links", {}).get("next")})
        if payload["meta"]["total"] != len(payload["data"]) or payload.get("links", {}).get("next"):
            raise ValueError((name, "pagination incomplete"))
        for record in payload["data"]:
            records.setdefault(record["id"], record)
    rows = []
    for record in sorted(records.values(), key=lambda item: item["id"]):
        identity = record["id"].split("arxiv.")[1]
        attrs = record["attributes"]
        rows.append({"identity": identity, "title": attrs["titles"][0]["title"],
                     "abstract": "\n".join(item["description"] for item in attrs.get("descriptions", []) if item.get("descriptionType") == "Abstract"),
                     "date_envelope": publication_date_envelope(record, identity), "record": record})
    save(BASE / "REPAIR_DISCOVERY_INVENTORY_20261022.json", {"themes": themes, "rows": rows})
    old_rows = []
    for path in sorted(BASE.glob("REPAIR_DATE_*_20261022.raw")):
        for record in json.loads(path.read_text())["data"]:
            old_rows.append(publication_date_envelope(record, record["id"].split("arxiv.")[1]))
    save(BASE / "REPAIR_OLD_DATE_ENVELOPES_20261022.json", sorted(old_rows, key=lambda item: item["arxiv_id"]))
    print(json.dumps({"themes": themes, "unique": len(rows), "old_date_records": len(old_rows)}, ensure_ascii=False))


def read_abstracts(start, stop):
    rows = json.loads((BASE / "REPAIR_DISCOVERY_INVENTORY_20261022.json").read_text())["rows"]
    for index, row in enumerate(rows[start:stop], start):
        print(index, row["identity"], row["date_envelope"]["bounded_bjt_date"], row["date_envelope"]["reasons"])
        print(row["title"])
        print(row["abstract"])
        print("related:", json.dumps(row["record"]["attributes"].get("relatedIdentifiers"), ensure_ascii=False))


def controls():
    specs = json.loads((BASE / "REPAIR_DISCOVERY_SPEC_20261022.json").read_text())
    choices = {"MODEL": "2509.09782", "SYSTEMS": "2509.10371", "MULTIMODAL": "2509.09828", "AGENTS": "2509.10446"}
    for spec in specs:
        query = spec["query"] + ' AND doi:"10.48550/arxiv.' + choices[spec["name"]] + '"'
        url = "https://api.datacite.org/dois?" + urllib.parse.urlencode({"client-id": "arxiv.content", "query": query, "page[size]": 10})
        capture("CONTROL_THEME_" + spec["name"], url)
    lexical = [("LLMS", "LLMs", "2509.09782"), ("LANGUAGE_MODELS", '"language models"', "2509.09782"),
               ("FOUNDATION_MODELS", '"foundation models"', "2509.09790"), ("TRANSFORMERS", "transformers", "2509.09955"),
               ("AGENTS", "agents", "2509.09853"), ("AGENTIC", "agentic", "2509.09864"),
               ("GPUS", "GPUs", "2509.10371"), ("KERNELS", "kernels", "2509.09774"), ("TOOLS", "tools", "2509.09774")]
    for name, term, identity in lexical:
        query = "(titles.title:" + term + " OR descriptions.description:" + term + ")"
        query += ' AND doi:"10.48550/arxiv.' + identity + '"'
        query += " AND registered:[2025-09-14T16:00:00Z TO 2025-09-15T16:00:00Z]"
        url = "https://api.datacite.org/dois?" + urllib.parse.urlencode({"client-id": "arxiv.content", "query": query, "page[size]": 10})
        capture("CONTROL_FORM_" + name, url)


def html_blocks(path, start, stop):
    class Blocks(HTMLParser):
        def __init__(self):
            super().__init__()
            self.depth = 0
            self.buffer = []
            self.rows = []

        def handle_starttag(self, tag, attrs):
            if tag in ("p", "h1", "h2", "h3", "h4", "table"):
                if not self.depth:
                    self.buffer = []
                self.depth += 1

        def handle_endtag(self, tag):
            if tag in ("p", "h1", "h2", "h3", "h4", "table") and self.depth:
                self.depth -= 1
                if not self.depth:
                    self.rows.append(" ".join(" ".join(self.buffer).split()))

        def handle_data(self, text):
            if self.depth:
                self.buffer.append(text)

    parser = Blocks()
    parser.feed((BASE / path).read_text())
    for index, row in enumerate(parser.rows[start:stop], start):
        print(index, row)


def gates():
    note = (BASE / "SUP_FIRST_20261012.md").read_text().split("## REPAIR3.", 1)[1]
    decisions = {}
    for match in re.finditer(r"^\|(\d{5})\|([^|]+)\|$", note, re.M):
        reason = match[2]
        kind = "N" if reason.startswith("最小N") else "P" if reason.startswith(("P", "窄P")) else "C" if reason.startswith(("C", "范围C")) else None
        if kind is None:
            raise ValueError((match[1], reason))
        decisions["2509." + match[1]] = {"gate": kind, "reason": reason}
    # Reader13 calibrated only these two admission decisions.
    decisions["2509.09848"] = {"gate": "N", "reason": "Zeno13: table/tree文本化/条件保持与直接消融最小核"}
    decisions["2509.09852"] = {"gate": "P", "reason": "Zeno13: topic alignment reward已给明确训练目标增量"}
    rows = json.loads((BASE / "REPAIR_DISCOVERY_INVENTORY_20261022.json").read_text())["rows"]
    if set(decisions) != {row["identity"] for row in rows}:
        raise ValueError(("incomplete admission", len(decisions), len(rows)))
    counts = {}
    for row in rows:
        row.update(decisions[row["identity"]])
        key = row["gate"] + ("_bounded" if row["date_envelope"]["bounded_bjt_date"] else "_cross")
        counts[key] = counts.get(key, 0) + 1
    save(BASE / "REPAIR_ADMISSION_20261022.json", {"counts": counts, "rows": rows})
    print(json.dumps(counts))


def exact_batch(start, size):
    rows = json.loads((BASE / "REPAIR_ADMISSION_20261022.json").read_text())["rows"]
    pending = [row["identity"] for row in rows if row["gate"] != "C" and row["identity"] not in {"2509.09782", "2509.09852"}]
    ids = pending[start:start + size]
    if not ids:
        raise ValueError("empty exact batch")
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ",".join(identity + "v1" for identity in ids), "max_results": len(ids)})
    capture("EXACT_AB_" + str(start), url)


def pdf_pages(path, first, last):
    from pypdf import PdfReader
    reader = PdfReader(BASE / path)
    print("PAGES", len(reader.pages))
    for index in range(first - 1, min(last, len(reader.pages))):
        content = reader.pages[index].extract_text().encode("utf-16", "surrogatepass").decode("utf-16", "backslashreplace")
        print("\nPAGE", index + 1, "\n", content)


def exact_entries(path, start, stop):
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    entries = ET.parse(BASE / path).getroot().findall("a:entry", ns)
    entries.sort(key=lambda item: item.findtext("a:id", namespaces=ns))
    for index, entry in enumerate(entries[start:stop], start):
        print(index, entry.findtext("a:id", namespaces=ns), entry.findtext("a:published", namespaces=ns))
        for tag in ("a:title", "a:summary", "x:comment", "x:journal_ref"):
            print(tag, entry.findtext(tag, namespaces=ns))


if __name__ == "__main__":
    if sys.argv[1] == "baseline":
        baseline()
    elif sys.argv[1] == "old-dates":
        old_dates()
    elif sys.argv[1] == "get":
        capture(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "application/vnd.api+json")
    elif sys.argv[1] == "discover":
        discover()
    elif sys.argv[1] == "inventory":
        inventory()
    elif sys.argv[1] == "abstracts":
        read_abstracts(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == "controls":
        controls()
    elif sys.argv[1] == "html":
        html_blocks(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    elif sys.argv[1] == "gates":
        gates()
    elif sys.argv[1] == "exact":
        exact_batch(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == "pdf":
        pdf_pages(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    elif sys.argv[1] == "exact-read":
        exact_entries(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
