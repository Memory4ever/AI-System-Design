"""Read exact-v1 abstracts only for the narrowed queries and named release."""
import datetime as dt
import json
import pathlib
import subprocess
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).parent
IDS = ["2511.18936", "2511.18670", "2511.19269", "2511.17775", "2511.19229", "2511.17729", "2511.21759", "2511.18661"]


class Abstract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.capture = None
        self.title = []
        self.abstract = []
        self.visible = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1" and "title" in attrs.get("class", ""):
            self.capture = "title"
        elif tag == "blockquote" and "abstract" in attrs.get("class", ""):
            self.capture = "abstract"

    def handle_data(self, text):
        self.visible.append(text)
        if self.capture:
            getattr(self, self.capture).append(text)

    def handle_endtag(self, tag):
        if tag == "h1" and self.capture == "title" or tag == "blockquote" and self.capture == "abstract":
            self.capture = None


for pid in IDS:
    url = "https://arxiv.org/abs/" + pid + "v1"
    target = ROOT / (pid + "v1-abstract.html")
    run = subprocess.run(["curl", "--max-time", "15", "-L", "-sS", url, "-o", str(target), "-w", "%{http_code}"],
                         capture_output=True, text=True)
    receipt = {"url": url, "executed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
               "http_status": run.stdout, "exit_code": run.returncode, "error": run.stderr,
               "bytes": target.stat().st_size if target.exists() else 0, "stop": "exact v1 abstract and local history only"}
    (ROOT / (target.name + ".receipt.json")).write_text(json.dumps(receipt, indent=2))
    if run.returncode or run.stdout != "200":
        print(json.dumps(receipt), flush=True)
        continue
    parser = Abstract()
    parser.feed(target.read_text())
    visible = " ".join(" ".join(parser.visible).split())
    start = visible.find("Submission history")
    end = visible.find("Full-text links", start)
    result = {"id": pid + "v1", "title": " ".join(" ".join(parser.title).split()),
              "abstract": " ".join(" ".join(parser.abstract).split()), "history": visible[start:end],
              "withdrawal_signal": "withdrawn" in visible.lower(), "date_role": "submission history is not first-public proof"}
    (ROOT / (pid + "v1-abstract.json")).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False), flush=True)
