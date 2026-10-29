import datetime as dt
import json
import re
from html.parser import HTMLParser
from pathlib import Path
import urllib.request
from zoneinfo import ZoneInfo

from repair_discovery_20261029 import BASE, fetch, save_json


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"script", "style"}:
            self.skip += 1
        if tag in {"a", "script"}:
            self.links.append((tag, attrs.get("href") or attrs.get("src")))

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())


def extract(name):
    parser = Text()
    parser.feed((BASE / name).read_text())
    output = BASE / (name + ".txt")
    output.write_text("\n".join(parser.parts) + "\n")
    save_json(BASE / (name + ".links.json"), parser.links)
    print("\nFILE", name, "\n", "\n".join(parser.parts)[-18000:], flush=True)


def request_html(name, url):
    meta = {"url": url, "checked_at": dt.datetime.now(dt.timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read()
            (BASE / name).write_bytes(body)
            meta.update(status=r.status, final_url=r.url, bytes=len(body))
        extract(name)
    except Exception as error:
        meta["error"] = repr(error)
        print(name, repr(error), flush=True)
    save_json(BASE / (name + ".request.json"), meta)


def date_rows():
    sources = {"2510.20956": "abs-self-jailbreak.txt", "2510.21236": "abs-agentbound.txt",
               "2510.21885": "abs-forgetting.txt", "2510.21144": "abs-neurogen.txt",
               "2510.21524": "abs-eu-agent.txt", "2510.20963": "abs-debate.txt",
               "2510.21339": "abs-multiturn.txt", "2510.21270": "REPAIR_PBS_ABSv1_20261029.html"}
    rows = []
    for identity, source in sources.items():
        text = (BASE / source).read_text()
        if source.endswith(".html"):
            parser = Text()
            parser.feed(text)
            text = "\n".join(parser.parts)
        records = re.findall(r"\[v1\]\s*\n([^\n]+ UTC)", text)
        assert len(records) == 1 and identity in text, (identity, records)
        submitted = dt.datetime.strptime(records[0], "%a, %d %b %Y %H:%M:%S UTC").replace(tzinfo=dt.timezone.utc)
        eastern = submitted.astimezone(ZoneInfo("America/New_York"))
        assert dt.datetime(2025, 10, 23, 14, tzinfo=eastern.tzinfo) < eastern < dt.datetime(2025, 10, 24, 14, tzinfo=eastern.tzinfo)
        lower = dt.datetime(2025, 10, 26, 20, tzinfo=ZoneInfo("America/New_York")).astimezone(dt.timezone.utc)
        name = "REPAIR_DC_CONTROL_EXACT_20261029.raw" if identity == "2510.21270" else "REPAIR_DC_EXACT_" + identity.replace(".", "_") + "_20261029.raw"
        data = json.loads((BASE / name).read_text())["data"]
        a = data["attributes"]
        assert a["doi"].lower() == "10.48550/arxiv." + identity and a["state"] == "findable"
        assert data["relationships"]["client"]["data"]["id"] == "arxiv.content"
        upper = dt.datetime.fromisoformat(a["registered"].replace("Z", "+00:00"))
        assert lower <= upper
        bjt_lower = lower.astimezone(ZoneInfo("Asia/Shanghai"))
        bjt_upper = upper.astimezone(ZoneInfo("Asia/Shanghai"))
        row = {"id": identity, "v1_source": source, "v1_raw": records[0],
               "eastern_v1": eastern.isoformat(), "doi_source": name, "created": a["created"],
               "registered": a["registered"], "lower_bjt": bjt_lower.isoformat(),
               "upper_bjt": bjt_upper.isoformat(),
               "arxiv_day": str(bjt_lower.date()) if bjt_lower.date() == bjt_upper.date() else None,
               "supplement_2025_10_26_excluded_by_lower": bjt_lower.date() > dt.date(2025, 10, 26)}
        rows.append(row)
    save_json(BASE / "REPAIR_DATE_BOUNDS_20261029.json", rows)
    print(json.dumps(rows, ensure_ascii=False, indent=2))


class PubNav(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current = None
        self.rows = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "row-card__heading" in attrs.get("class", "").split():
            self.current = {"url": attrs.get("href"), "title": ""}

    def handle_data(self, value):
        if self.current is not None:
            self.current["title"] += value

    def handle_endtag(self, tag):
        if tag == "a" and self.current is not None:
            self.current["title"] = " ".join(self.current["title"].split())
            self.rows.append(self.current)
            self.current = None


def source_summary():
    config = json.loads((BASE / "REPAIR_QWEN_RESEARCH_CONFIG_20261029.raw").read_text())
    qwen = {"config_count": len(config), "config": [{k: r.get(k) for k in ["id", "date", "title"]} for r in config]}
    for language in ["EN", "ZH"]:
        result = json.loads((BASE / f"REPAIR_QWEN_RETRIEVAL_{language}_20261029.raw").read_text())
        assert result["success"] is True
        rows = result["data"]["articles"]
        qwen[language] = [{"path": r["path"], "date": r["extra"]["date"], "title": r["title"]} for r in rows]
        print("QWEN", language, "rows", len(rows), "data_keys", list(result["data"]))
    assert {r["path"] for r in qwen["EN"]} == {r["path"] for r in qwen["ZH"]}
    dates = []
    for row in qwen["config"] + qwen["EN"]:
        value = dt.datetime.fromisoformat(row["date"].replace("Z", "+00:00")).astimezone(ZoneInfo("Asia/Shanghai"))
        dates.append((value, row["title"]))
    hits = [row for row in dates if row[0].date() == dt.date(2025, 10, 26)]
    qwen["bjt_2025_10_26_hits"] = [(str(d), title) for d, title in hits]
    qwen["nearest_before"] = str(max(row for row in dates if row[0].date() < dt.date(2025, 10, 26)))
    qwen["nearest_after"] = str(min(row for row in dates if row[0].date() > dt.date(2025, 10, 26)))
    qwen["unique_paths_config_plus_en"] = len({r["id"] for r in config} | {r["path"] for r in qwen["EN"]})
    save_json(BASE / "REPAIR_QWEN_NAVIGATION_20261029.json", qwen)
    print("QWEN", {k: v for k, v in qwen.items() if k not in ["config", "EN", "ZH"]})
    pubs = []
    for name in ["REPAIR_GOOGLE_PUBS_LM_20261029.html", "REPAIR_GOOGLE_PUBS_LM_PAGE2_20261029.html", "REPAIR_GOOGLE_PUBS_LM_PAGE3_20261029.html"]:
        parser = PubNav()
        parser.feed((BASE / name).read_text())
        print("PUBS", name, len(parser.rows))
        pubs.extend(parser.rows)
    save_json(BASE / "REPAIR_GOOGLE_PUBS_NAVIGATION_20261029.json", pubs)
    print("PUBS titles", json.dumps(pubs, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    for name in ["REPAIR_GOOGLE_PUBS_LM_20261029.html", "REPAIR_DEEPMIND_BLOG_PAGE5_20261029.html"]:
        extract(name)
    request_html("REPAIR_QWEN_BLOG_20261029.html", "https://qwen.ai/blog")
    for identity in ["2510.20956", "2510.21236", "2510.21885", "2510.21144", "2510.21524", "2510.20963", "2510.21339"]:
        data = fetch("REPAIR_DC_EXACT_" + identity.replace(".", "_") + "_20261029", "https://api.datacite.org/dois/10.48550/arxiv." + identity)
        if data:
            a = data["data"]["attributes"]
            print("EXACT", identity, a.get("created"), a.get("registered"), a.get("state"), data["data"].get("relationships", {}).get("client"), flush=True)
