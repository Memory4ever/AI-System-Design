"""Inspect this day's finite identity set; bounds do not assign contribution."""
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "supplement-20261012"
NY = ZoneInfo("America/New_York")
BJT = ZoneInfo("Asia/Shanghai")


class Text(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.meta = {}
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and "name" in attrs:
            self.meta.setdefault(attrs["name"], []).append(attrs.get("content", ""))

    def handle_data(self, data):
        self.parts.append(data)

    def value(self):
        return " ".join(" ".join(self.parts).split())


class Blocks(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.block = None
        self.tags = []
        self.math_depth = 0
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in {"br", "img", "meta", "link", "input", "hr"}:
            self.tags.append((tag, attrs.get("id", "")))
        if tag == "math":
            self.math_depth += 1
            if self.block is not None:
                self.block[2].append(" $" + attrs.get("alttext", "") + "$ ")
        if self.block is None and tag in {"p", "h1", "h2", "h3", "h4", "figcaption", "tr"}:
            anchor = "/".join(i for _, i in self.tags[-3:] if i)
            self.block = (tag, anchor, [])

    def handle_endtag(self, tag):
        if tag == "math":
            self.math_depth = max(0, self.math_depth - 1)
        if self.block is not None and self.block[0] == tag:
            self.blocks.append((self.block[1], " ".join(" ".join(self.block[2]).split())))
            self.block = None
        for index in range(len(self.tags) - 1, -1, -1):
            if self.tags[index][0] == tag:
                del self.tags[index:]
                break

    def handle_data(self, data):
        if self.block is not None and not self.math_depth:
            self.block[2].append(data)


def identities():
    text = (ROOT / "SUP_DATE_20261013.md").read_text()
    sections = re.findall(r"```text\n(.*?)\n```", text, re.S)
    result = []
    for section in sections[:2]:
        for item in re.split(r"[/\s]+", section.strip()):
            result.append(item if "." in item else "2510." + item)
    return result + ["2510.06175"]


def lower(submitted):
    local = submitted.astimezone(NY)
    date = local.date()
    # Friday's cutoff is announced Sunday; the rest of the weekend waits Monday.
    for offset in range(8):
        cutoff = datetime.combine(date + timedelta(days=offset), datetime.min.time(), NY).replace(hour=14)
        if cutoff <= local or cutoff.weekday() > 4:
            continue
        announcement = cutoff.replace(hour=20)
        if cutoff.weekday() == 4:
            announcement += timedelta(days=2)
        return announcement.astimezone(timezone.utc)
    raise ValueError("No cutoff found")


def inspect(paper):
    paths = [RAW / ("repair-abs-" + paper + "v1.raw"), RAW / ("abs-" + paper + "v1.raw")]
    path = next((path for path in paths if path.exists()), None)
    if path is None:
        return paper, "MISSING_V1"
    text = Text(path.read_text()).value()
    history = text.split("Submission history", 1)[1].split("Access Paper:", 1)[0]
    matches = re.findall(r"\[v1\]\s+([A-Za-z]{3}, \d{1,2} [A-Za-z]{3} \d{4} \d{2}:\d{2}:\d{2} UTC)", history)
    if len(matches) != 1:
        return paper, "INVALID_V1", history
    submitted = datetime.strptime(matches[0], "%a, %d %b %Y %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    earliest = lower(submitted)
    result = [paper, submitted.isoformat(), earliest.isoformat(), earliest.astimezone(BJT).date().isoformat()]
    doi_path = RAW / ("repair-doi-" + paper + ".raw")
    if doi_path.exists():
        data = json.loads(doi_path.read_text())["data"]
        attrs = data["attributes"]
        client = data["relationships"]["client"]["data"]["id"]
        exact = data["id"].lower() == "10.48550/arxiv." + paper
        registered = datetime.fromisoformat(attrs["registered"].replace("Z", "+00:00"))
        valid = exact and client == "arxiv.content" and attrs["state"] == "findable" and earliest <= registered
        same_day = valid and earliest.astimezone(BJT).date() == registered.astimezone(BJT).date()
        result.extend([attrs["registered"], client, attrs["state"], attrs["url"], "JOINT_DAY=" + str(same_day)])
    return tuple(result)


def fetch(paper, kind):
    name = "repair-" + kind + "-" + paper + ("v1" if kind == "abs" else "")
    if (RAW / (name + ".raw")).exists():
        return
    if kind == "abs" and (RAW / ("abs-" + paper + "v1.raw")).exists():
        return
    spec = importlib.util.spec_from_file_location("capture", ROOT / "SUP_CAPTURE_20261012.py")
    capture = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(capture)
    if kind == "abs":
        url = "https://arxiv.org/abs/" + paper + "v1"
    elif kind == "core":
        url = "https://arxiv.org/html/" + paper + "v1"
    else:
        url = "https://api.datacite.org/dois/10.48550/arXiv." + paper
    capture.fetch(name, url)


def discovery_delta():
    old = set()
    names = [prefix + theme for prefix in ("arxiv-", "arxiv-target-")
             for theme in ("model", "systems", "agent", "multimodal", "hardware")]
    names += ["titles-" + theme for theme in ("cllg", "systems", "cvro")]
    for name in names:
        document = ET.fromstring((RAW / (name + ".raw")).read_text())
        for entry in document.findall("{http://www.w3.org/2005/Atom}entry"):
            identity = entry.findtext("{http://www.w3.org/2005/Atom}id", "")
            match = re.search(r"(\d{4}\.\d{4,5})(?:v\d+)?$", identity)
            if match:
                old.add(match.group(1))
    found = {}
    appearances = 0
    for path in sorted(RAW.glob("repair-root-discover-*-20261026.raw")):
        for item in json.loads(path.read_text())["data"]:
            appearances += 1
            identity = item["id"].lower().removeprefix("10.48550/arxiv.")
            found.setdefault(identity, item)
    delta = {identity: item for identity, item in sorted(found.items()) if identity not in old}
    print("DISCOVERY_COUNTS", appearances, len(found), len(old), len(found.keys() & old), len(delta))
    return delta


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode in {"discovery", "discoveryabstract"}:
        delta = discovery_delta()
        if mode == "discoveryabstract":
            for identity in sys.argv[2:]:
                attrs = delta[identity]["attributes"]
                print(identity, attrs["titles"], "CURRENT_VERSION", attrs["version"])
                print("ABSTRACT", attrs["descriptions"])
                print("DATES", attrs["dates"], "REGISTERED", attrs["registered"], flush=True)
            sys.exit(0)
        start, end = map(int, sys.argv[2:4])
        for index, (identity, item) in enumerate(delta.items(), 1):
            if start <= index <= end:
                print(index, identity, item["attributes"]["titles"][0]["title"])
        sys.exit(0)
    if mode == "readcore":
        document = Blocks((RAW / ("repair-core-" + sys.argv[2] + ".raw")).read_text())
        start, end = map(int, sys.argv[3:5])
        for index, (anchor, text) in enumerate(document.blocks, 1):
            if start <= index <= end:
                print(index, anchor, text)
        print("TOTAL_BLOCKS", len(document.blocks))
        sys.exit(0)
    papers = sys.argv[2:] or identities()
    for paper in papers:
        if mode == "core":
            fetch(paper, "core")
            continue
        if mode == "abstract":
            paths = [RAW / ("repair-abs-" + paper + "v1.raw"), RAW / ("abs-" + paper + "v1.raw")]
            path = next((path for path in paths if path.exists()), None)
            if path:
                document = Text(path.read_text())
                print(paper, document.meta.get("citation_title"), document.meta.get("citation_abstract"), flush=True)
                body = document.value()
                if "Comments:" in body:
                    print("Comments:", body.split("Comments:", 1)[1].split("Subjects:", 1)[0], flush=True)
                print("History:", body.split("Submission history", 1)[1].split("Access Paper:", 1)[0], flush=True)
            continue
        if mode == "recover":
            fetch(paper, "abs")
            observation = inspect(paper)
            if len(observation) >= 4 and observation[3] == "2025-10-07":
                fetch(paper, "doi")
        print("\t".join(inspect(paper)), flush=True)
