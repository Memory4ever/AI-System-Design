import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

root = Path(__file__).resolve().parent
name, url = sys.argv[1:]
path = root / name
receipt_path = root / (name + '.receipt.json')
if path.exists() or receipt_path.exists():
    raise FileExistsError('Refusing to overwrite evidence')
receipt = {'author': 'Darwin/Codex Sep02 source resume', 'url': url,
           'started': datetime.now(timezone.utc).isoformat(), 'timeout_seconds': 20}
try:
    try:
        response = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 HistoricalDailyResearch'}), timeout=20)
    except HTTPError as error:
        response = error
    with response:
        content = response.read()
        receipt.update(status=response.status, final_url=response.url, bytes=len(content))
    with path.open('xb') as stream:
        stream.write(content)
except Exception as error:
    receipt['error'] = str(error)
receipt['checked'] = datetime.now(timezone.utc).isoformat()
with receipt_path.open('x') as stream:
    json.dump(receipt, stream, ensure_ascii=False, indent=2)
print(json.dumps(receipt, ensure_ascii=False))
