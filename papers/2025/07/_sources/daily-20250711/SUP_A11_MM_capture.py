import datetime
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).parent


def identity(entry):
    return re.sub(r"v\d+$", "", entry["id"].split("/")[-1])


def unique_entries():
    data = json.loads((ROOT / "SUP_A11_NARROW.json").read_text())
    other = {identity(e) for group in ("model", "agents", "systems", "hardware")
             for e in data[group]["entries"]}
    return [e for e in data["multimodal"]["entries"] if identity(e) not in other]


def capture(paper_id, version):
    suffix = "v1" if version == "v1" else "current"
    stem = f"SUP_A11_MM_{paper_id}_{suffix}"
    url = "https://arxiv.org/abs/" + paper_id + ("v1" if version == "v1" else "")
    record = {"url": url, "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "timeout_seconds": 20}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design-research/1.0"})
        with urllib.request.urlopen(request, timeout=20) as response:
            raw = response.read()
            record.update(status=response.status, final_url=response.url, bytes=len(raw))
            record["headers"] = dict(response.headers.items())
        (ROOT / (stem + ".html")).write_bytes(raw)
        soup = BeautifulSoup(raw, "html.parser")
        fields = {}
        for key, selector in (("title", "h1.title"), ("abstract", "blockquote.abstract"),
                              ("comments", "td.comments"), ("history", ".submission-history"),
                              ("notice", ".withdrawal")):
            element = soup.select_one(selector)
            fields[key] = element.get_text(" ", strip=True) if element else ""
        fields["signals"] = [line.strip() for line in soup.get_text("\n", strip=True).splitlines()
                             if re.search(r"withdraw|correct|errat|retract|removed", line, re.I)]
        record.update(fields)
    except urllib.error.HTTPError as error:
        raw = error.read()
        (ROOT / (stem + ".html")).write_bytes(raw)
        record.update(status=error.code, error=str(error), bytes=len(raw))
    except Exception as error:
        record["error"] = str(error)
    (ROOT / (stem + ".request.json")).write_text(json.dumps(record, ensure_ascii=False, indent=2))
    print(paper_id, suffix, record.get("status", record.get("error")), flush=True)


if __name__ == "__main__":
    entries = unique_entries()
    manifest = {"rule": "multimodal minus union(model,agents,systems,hardware), version-stripped identity",
                "source": "SUP_A11_NARROW.json", "unique_count": len(entries),
                "entries": [{"id": identity(e), "discovery_title": e["title"]} for e in entries]}
    target = ROOT / "SUP_A11_MM_unique.json"
    if not target.exists():
        target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    for paper_id in sys.argv[1:]:
        for version in ("v1", "current"):
            capture(paper_id, version)
