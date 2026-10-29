"""Scoped administrative checks; no semantic acceptance is inferred."""
import collections
import hashlib
import json
from pathlib import Path
import re
import urllib.parse

BASE = Path(__file__).parent
REPORT = BASE.parent.parent / '12' / 'README.md'
baseline = (BASE / 'SUP_BASELINE_README_20261012.md').read_text()
report = REPORT.read_text()
window = next(line for line in baseline.splitlines() if line.startswith('**窗口：**'))
assert window in report, 'Original window changed'
frozen = baseline.split('## 4. 证据与知识整合\n\n', 1)[1].split('\n## 5.', 1)[0]
assert report.split('## 4. 证据与知识整合\n\n', 1)[1].startswith(frozen), 'Original continuous section 4 changed'
assert baseline.split('## 3. 候选与判断', 1)[1].split('## 4.', 1)[0].count('| [') == 0

statuses = collections.Counter()
requests = sorted(BASE.glob('SUP_*_20261012.request.json'))
for path in requests:
    record = json.loads(path.read_text())
    raw = path.with_name(path.name.replace('.request.json', '.raw'))
    assert raw.is_file(), path
    body = raw.read_bytes()
    assert len(body) == record['bytes'], path
    assert hashlib.sha256(body).hexdigest() == record['sha256'], path
    statuses[record['status']] += 1

files = [REPORT, *sorted(BASE.glob('SUP_*.md'))]
refs = 0
anchors = 0
for path in files:
    for match in re.finditer(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        target = match.group(1).strip('<>')
        if urllib.parse.urlsplit(target).scheme:
            continue
        name, _, anchor = target.partition('#')
        origin = REPORT.parent if path.name == 'SUP_BASELINE_README_20261012.md' else path.parent
        destination = (origin / urllib.parse.unquote(name)).resolve() if name else path
        assert destination.exists(), (path, target)
        refs += 1
        if anchor:
            assert destination.is_file(), (path, target)
            slugs = []
            for line in destination.read_text().splitlines():
                if line.startswith('#'):
                    title = re.sub(r'^#+\s+', '', line).lower()
                    title = re.sub(r'[^\w\s-]', '', title)
                    slugs.append(title.replace(' ', '-'))
            assert urllib.parse.unquote(anchor) in slugs, (path, target)
            anchors += 1

print('Freeze: original window, original empty candidate table and continuous section 4 PASS')
print('Raw/request:', len(requests), 'SHA/bytes PASS;', dict(sorted(statuses.items())))
print('Markdown/local refs:', len(files), refs, 'anchors:', anchors, 'PASS')
