"""Bounded source capture for the Oct03 omission repair only."""

import argparse
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlencode
from urllib.request import Request, urlopen


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from arxiv_publication_date import publication_date_envelope


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "section", "h1", "h2", "h3", "tr", "li"):
            self.parts.append("\n")
        if tag == "math":
            self.parts.append(dict(attrs).get("alttext", ""))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag in ("p", "section", "h1", "h2", "h3", "tr", "li"):
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def save_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def capture(name, url, as_json=True):
    target = HERE / ("repair-20261026-" + name)
    if target.with_suffix(".raw").exists():
        raise RuntimeError("Refusing to replace existing capture: " + name)
    started = datetime.now(timezone.utc).isoformat()
    request = Request(url, headers={"User-Agent": "AI-System-Design-Research/1.0"})
    with urlopen(request, timeout=75) as response:
        raw = response.read()
        status = response.status
        final_url = response.url
    target.with_suffix(".raw").write_bytes(raw)
    save_json(target.with_suffix(".request.json"), {
        "requested_url": url, "final_url": final_url, "started_at": started,
        "finished_at": datetime.now(timezone.utc).isoformat(), "status": status,
        "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
    })
    return json.loads(raw) if as_json else raw


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["baseline", "doi", "discover", "abstracts", "core", "abs", "model-tail", "rules"])
    parser.add_argument("identity", nargs="?")
    args = parser.parse_args()
    if args.mode == "baseline":
        path = HERE / "repair-20261026-baseline.json"
        if path.exists():
            raise RuntimeError("Baseline already exists")
        files = [ROOT / "papers/2025/10/03/README.md", *sorted(HERE.rglob("*"))]
        hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in files if p.is_file()}
        save_json(path, {"captured_at": datetime.now(timezone.utc).isoformat(), "files": hashes})
        print("Protected", len(hashes), "files")
    elif args.mode == "doi":
        identity = args.identity
        if not identity or not identity.startswith("2510.") or not identity[5:].isdigit():
            raise ValueError("Expected an exact October 2025 arXiv identity")
        raw = capture("doi-" + identity.replace(".", "-"),
                      "https://api.datacite.org/dois/10.48550/arxiv." + identity)
        result = publication_date_envelope(raw, identity + "v1")
        save_json(HERE / ("repair-20261026-envelope-" + identity + ".json"), result)
        print(json.dumps(result, ensure_ascii=False))
    elif args.mode in ("core", "abs"):
        for identity in args.identity.split(","):
            prefix = args.mode + "-" + identity.replace(".", "-")
            endpoint = "html" if args.mode == "core" else "abs"
            raw = capture(prefix, "https://arxiv.org/" + endpoint + "/" + identity + "v1", as_json=False)
            parser = PlainText()
            parser.feed(raw.decode())
            path = HERE / ("repair-20261026-" + prefix + ".txt")
            path.write_text("".join(parser.parts))
            print(path.name, len(raw), "bytes", flush=True)
    elif args.mode == "abstracts":
        identities = args.identity.split(",")
        query = urlencode({"id_list": ",".join(i + "v1" for i in identities),
                           "start": 0, "max_results": len(identities)})
        raw = capture("abstracts-" + identities[0].replace(".", "-"),
                      "https://export.arxiv.org/api/query?" + query, as_json=False)
        tree = ET.fromstring(raw)
        ns = {"a": "http://www.w3.org/2005/Atom"}
        text = []
        for entry in tree.findall("a:entry", ns):
            text += [entry.findtext("a:id", namespaces=ns),
                     entry.findtext("a:published", namespaces=ns),
                     entry.findtext("a:title", namespaces=ns),
                     entry.findtext("a:summary", namespaces=ns), ""]
        path = HERE / ("repair-20261026-abstracts-" + identities[0].replace(".", "-") + ".txt")
        path.write_text("\n".join(text))
        print("\n".join(text))
    elif args.mode == "rules":
        for name, url in {
            "arxiv-rules-20250106": "https://raw.githubusercontent.com/arXiv/arxiv-docs/46793211923f3e84140efe04524a250a93b2577b/source/help/availability.md",
            "datacite-dates": "https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api",
        }.items():
            raw = capture(name, url, as_json=False)
            print(name, len(raw))
    else:
        topics = {
            "model": '("language model" OR "language models" OR LLM OR LLMs OR transformer OR transformers OR "mixture of experts")',
            "systems": '((GPU OR kernel OR inference OR serving OR quantization OR parallel OR cache OR communication) AND ("language model" OR "language models" OR transformer OR transformers OR diffusion))',
            "agent": '((agent OR agents OR RAG OR retrieval OR memory OR tool OR tools OR planning) AND ("language model" OR "language models" OR LLM OR LLMs))',
            "multimodal": '("vision language" OR "vision-language" OR "world model" OR "world models" OR "multimodal model" OR "multimodal models" OR VLA OR "diffusion model" OR "diffusion models")',
        }
        for name, topic in topics.items():
            if args.mode == "model-tail" and name != "model":
                continue
            query = 'registered:[2025-10-01T16:00:00Z TO 2025-10-02T15:59:59Z] AND ' + topic
            params = {"client-id": "arxiv.content", "query": query,
                      "page[size]": 100, "page[number]": 1, "sort": "registered"}
            pages = (2, 3) if args.mode == "model-tail" else (1,)
            for page in pages:
                params["page[number]"] = page
                suffix = "" if page == 1 else "-page" + str(page)
                raw = capture("discover-" + name + suffix,
                              "https://api.datacite.org/dois?" + urlencode(params))
                print(name, "page", page, "returned", len(raw.get("data", [])), "total", raw.get("meta", {}).get("total"),
                      "next", raw.get("links", {}).get("next"))


if __name__ == "__main__":
    main()
