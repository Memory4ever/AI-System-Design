"""Save a named finite set of official versioned abstract pages, without retries."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys

root = Path(__file__).parent
for identity in sys.argv[1:]:
    url = "https://arxiv.org/abs/" + identity + "v1"
    print(url, flush=True)
    try:
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as response:
            data = response.read()
            print(response.status, len(data), flush=True)
        (root / ("RAW_AB_" + identity + "v1_20261015.html")).write_bytes(data)
    except (URLError, HTTPError, TimeoutError, OSError) as error:
        print(type(error).__name__, str(error), flush=True)
