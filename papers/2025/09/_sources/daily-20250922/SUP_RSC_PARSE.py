import json
import sys
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent


def walk(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)


for name in sys.argv[1:]:
    soup = BeautifulSoup((ROOT / (name + ".raw")).read_text(), "html.parser")
    chunks = []
    for script in soup.find_all("script"):
        text = script.string or script.get_text()
        prefix = "self.__next_f.push("
        if text.startswith(prefix):
            data = json.loads(text[len(prefix):-1])
            if len(data) > 1 and isinstance(data[1], str):
                chunks.append(data[1])
    objects = []
    for line in "".join(chunks).splitlines():
        payload = line.partition(":")[2]
        if payload.startswith(("{", "[")):
            try:
                objects.extend(walk(json.loads(payload)))
            except json.JSONDecodeError:
                continue
    matched = [obj for obj in objects if "hasMore" in obj]
    if not matched:
        stream = "".join(chunks)
        decoder = json.JSONDecoder()
        for match in re.finditer(r'\{"blogsItems":', stream):
            value, _ = decoder.raw_decode(stream[match.start():])
            if "hasMore" in value:
                matched.append(value)
    print(name, "hasMore", [(obj.get("hasMore"), list(obj)) for obj in matched])
    (ROOT / (name + ".rsc.json")).write_text(json.dumps(matched, ensure_ascii=False, indent=2) + "\n")
