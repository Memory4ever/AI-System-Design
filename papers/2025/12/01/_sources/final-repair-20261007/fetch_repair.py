import datetime
import hashlib
import json
import pathlib
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent


def fetch(name, url):
    raw = ROOT / (name + '.raw')
    record_path = ROOT / (name + '.request.json')
    if raw.exists() or record_path.exists():
        raise RuntimeError('Refusing to overwrite ' + name)
    record = {'url': url, 'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    request = urllib.request.Request(url, headers={'User-Agent': 'AI-System-Design historical research'})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            data = response.read()
            record.update(status=response.status, final_url=response.url, headers=dict(response.headers))
    except urllib.error.HTTPError as error:
        data = error.read()
        record.update(status=error.code, final_url=error.url, headers=dict(error.headers))
    except Exception as error:
        data = b''
        record['error'] = repr(error)
    record.update(ended_at=datetime.datetime.now(datetime.timezone.utc).isoformat(), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    raw.write_bytes(data)
    record_path.write_text(json.dumps(record, indent=2), encoding='utf-8')
    print(json.dumps(record, ensure_ascii=False))


class Reader(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1

    def handle_data(self, value):
        if not self.skip and value.strip():
            self.parts.append(value.strip())


if __name__ == '__main__':
    if sys.argv[1] == 'fetch':
        fetch(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'read':
        reader = Reader()
        reader.feed((ROOT / sys.argv[2]).read_text(errors='replace'))
        for i, line in enumerate(reader.parts, 1):
            print(str(i) + ': ' + line)
