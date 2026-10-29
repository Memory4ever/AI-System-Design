"""Day-local retrieval only; records raw response and actual transport outcome."""
import argparse
import datetime
import json
from pathlib import Path
import subprocess

p = argparse.ArgumentParser()
p.add_argument('name')
p.add_argument('url')
args = p.parse_args()
base = Path(__file__).parent
raw = base / (args.name + '.raw')
if raw.exists():
    raise SystemExit('Refusing to replace an existing raw artifact')
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
r = subprocess.run(['curl', '-L', '--max-time', '65', '-sS', '-A',
                    'AI-System-Design historical research', '-o', str(raw),
                    '-w', '%{http_code}\n%{url_effective}\n%{size_download}',
                    args.url], capture_output=True, text=True)
record = dict(url=args.url, started=started,
              finished=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              exit=r.returncode, metadata=r.stdout.splitlines(), stderr=r.stderr,
              saved_bytes=raw.stat().st_size if raw.exists() else 0)
(base / (args.name + '.request.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record))
