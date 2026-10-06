"""Read-only URL extraction for bounded historical source inspection, not coverage proof."""
import datetime
from html.parser import HTMLParser
import json
import re
import subprocess
import sys


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.lines = []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.lines.append(data.strip())


url = sys.argv[1]
result = subprocess.run(['curl', '-L', '--max-time', '30', '-sS', '-w', '\nHTTP_STATUS:%{http_code}\nFINAL_URL:%{url_effective}', url], capture_output=True, text=True)
raw = result.stdout
parser = Text()
parser.feed(raw)
lines = parser.lines
date_re = re.compile(r'2026[-./]0?5|May.{0,16}2026|2026.{0,8}May|2026年5月', re.I)
selected = set()
for i, line in enumerate(lines):
    if date_re.search(line):
        selected.update(range(max(0, i-3), min(len(lines), i+6)))
snippets = []
for match in list(date_re.finditer(raw))[:60]:
    snippets.append(raw[max(0, match.start()-120):match.end()+280])
print(json.dumps({'url': url, 'checked_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'curl_code': result.returncode, 'stderr': result.stderr, 'footer': raw[-150:], 'total_bytes': len(raw.encode()), 'rendered_line_count': len(lines), 'may_lines': [{'line': i, 'text': lines[i]} for i in sorted(selected)], 'head_text': lines[:24], 'tail_text': lines[-24:], 'raw_date_contexts': snippets}, ensure_ascii=False, indent=2))
