"""Summarize embedded official list metadata without turning it into a review queue."""
import json
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).parent / "supplement-20261007"


class Scripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.active = True
            self.data.append("")

    def handle_endtag(self, tag):
        if tag == "script":
            self.active = False

    def handle_data(self, data):
        if self.active:
            self.data[-1] += data


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def flight_objects(name):
    parser = Scripts()
    parser.feed((BASE / (name + ".raw")).read_text())
    decoder = json.JSONDecoder()
    for script in parser.data:
        marker = "self.__next_f.push("
        start = 0
        while (start := script.find(marker, start)) >= 0:
            start += len(marker)
            try:
                payload, used = decoder.raw_decode(script[start:])
            except ValueError:
                continue
            start += used
            if isinstance(payload, list) and len(payload) > 1 and isinstance(payload[1], str):
                for line in payload[1].splitlines():
                    _, _, body = line.partition(":")
                    try:
                        yield json.loads(body)
                    except ValueError:
                        continue


if __name__ == "__main__":
    for name in ("anthropic-research", "zai-page2", "minimax-en", "minimax-cn"):
        records = []
        for obj in flight_objects(name):
            records.extend(walk(obj))
        print("\n", name)
        if name == "anthropic-research":
            posts = {row.get("slug", {}).get("current", row.get("title", "")): row
                     for row in records if row.get("publishedOn") and row.get("title")}
            print("Dated title records", len(posts))
            for key, row in posts.items():
                if "2025-09" <= row["publishedOn"][:7] <= "2025-10":
                    print(row["publishedOn"], row["title"], key)
        elif name == "zai-page2":
            for row in records:
                if "hasMore" in row:
                    print("hasMore", row["hasMore"], "nextPage", row.get("nextPage"))
            posts = {row.get("id", row.get("title_en", "")): row for row in records
                     if row.get("createAt") and row.get("title_en")}
            print("Dated title records", len(posts))
            for row in sorted(posts.values(), key=lambda row: row["createAt"])[0:3]:
                print(row["createAt"], row["title_en"])
        else:
            for row in records:
                if any(k in row for k in ("total", "hasMore", "totalPages")):
                    print({k: row[k] for k in ("total", "hasMore", "totalPages") if k in row})
