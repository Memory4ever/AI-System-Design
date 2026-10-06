import datetime
import json
import pathlib
import sys
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).parent


def capture(name, url):
    stem = "SUP_A11_MM_" + name
    record = {"url": url, "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "timeout_seconds": 25}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design-research/1.0"})
        with urllib.request.urlopen(request, timeout=25) as response:
            raw = response.read()
            record.update(status=response.status, final_url=response.url, bytes=len(raw),
                          headers=dict(response.headers.items()))
        (ROOT / (stem + ".raw")).write_bytes(raw)
        if "pdf" not in record["headers"].get("Content-Type", "").lower() and not raw.startswith(b"%PDF"):
            soup = BeautifulSoup(raw, "html.parser")
            for element in soup(["script", "style"]):
                element.decompose()
            (ROOT / (stem + ".txt")).write_text(soup.get_text("\n", strip=True))
    except urllib.error.HTTPError as error:
        raw = error.read()
        (ROOT / (stem + ".raw")).write_bytes(raw)
        record.update(status=error.code, error=str(error), bytes=len(raw))
    except Exception as error:
        record["error"] = str(error)
    (ROOT / (stem + ".request.json")).write_text(json.dumps(record, indent=2))
    print(name, record.get("status", record.get("error")), flush=True)


if __name__ == "__main__":
    for name, url in zip(sys.argv[1::2], sys.argv[2::2]):
        capture(name, url)
