"""Read bounded exact-version paragraphs with their source element IDs."""
import html, pathlib, re, sys

raw = pathlib.Path(sys.argv[1]).read_text()
raw = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", raw, flags=re.S)
rows = []
for match in re.finditer(r"<(h[1-6]|p|figcaption|table)\b([^>]*)>(.*?)</\1>", raw, re.S):
    tag, attrs, body = match.groups()
    if tag == "p" and "ltx_p" not in attrs:
        continue
    body = re.sub(r'<math\b([^>]*)>.*?</math>', lambda m: ' [' + (re.search(r'alttext="([^"]+)"', m.group(1)).group(1) if re.search(r'alttext="([^"]+)"', m.group(1)) else 'math') + '] ', body, flags=re.S)
    body = html.unescape(re.sub(r"<[^>]*>", " ", body))
    body = re.sub(r"\s+", " ", body).strip()
    identifier = re.search(r'id="([^"]+)"', attrs)
    if body:
        rows.append((identifier.group(1) if identifier else tag,body,tag))
pattern = re.compile(sys.argv[2], re.I) if len(sys.argv)>2 and not sys.argv[2].startswith('rows:') else None
span = tuple(map(int, sys.argv[2][5:].split(':'))) if len(sys.argv)>2 and sys.argv[2].startswith('rows:') else None
for i,(identifier, body, tag) in enumerate(rows):
    if (len(sys.argv)>2 and sys.argv[2] == "headings" and tag.startswith("h")) or (span and span[0] <= i < span[1]) or (not span and not (len(sys.argv)>2 and sys.argv[2] == "headings") and (pattern is None or pattern.search(body) or identifier == "h2")):
        print(f"[{i}] {identifier}: {body}")
