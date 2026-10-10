"""Read requested exact-version HTML sections only; stdout, no file mutation."""
import html
import re
import sys
import urllib.request

url = sys.argv[1]
page = urllib.request.urlopen(url, timeout=30).read().decode()
for section_id in sys.argv[2:]:
    match = re.search(r'<section\b[^>]*\bid="' + re.escape(section_id) + r'"[^>]*>', page)
    if not match:
        print(section_id, "NOT FOUND")
        continue
    depth = 1
    end = None
    for token in re.finditer(r'</?section\b[^>]*>', page[match.end():]):
        depth += -1 if token.group().startswith('</') else 1
        if depth == 0:
            end = match.end() + token.end()
            break
    if end is None:
        raise ValueError("Unclosed HTML section " + section_id)
    excerpt = page[match.start():end]
    excerpt = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', excerpt, flags=re.S)
    clean = html.unescape(re.sub(r'<[^>]+>', ' ', excerpt))
    print(section_id, re.sub(r'\s+', ' ', clean).strip())
