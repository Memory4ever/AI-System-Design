import collections
import hashlib
import json
import pathlib
import re
import sys
import urllib.parse


root = pathlib.Path(__file__).resolve().parent
report = pathlib.Path(sys.argv[1]).resolve()
baseline = root / "SUP_BASELINE_README_20261012.md"
old = baseline.read_text()
new = report.read_text()


def section(text, number):
    return text.split("## " + str(number) + ". ", 1)[1].split(
        "## " + str(number + 1) + ". ", 1
    )[0]


assert old.split("**窗口：**", 1)[1].splitlines()[0] == new.split(
    "**窗口：**", 1
)[1].splitlines()[0]
for number in (3, 4):
    assert section(old, number) == section(new, number), number
statuses = collections.Counter()
total = 0
requests = sorted(root.glob("SUP_*.request.json"))
for path in requests:
    metadata = json.loads(path.read_text())
    raw = (root / metadata["file"]).read_bytes()
    assert len(raw) == metadata["bytes"], path
    assert hashlib.sha256(raw).hexdigest() == metadata["sha256"], path
    total += len(raw)
    statuses[metadata["status"]] += 1
files = [report] + sorted(root.glob("SUP_*.md"))
refs = 0
report_refs = 0
for path in files:
    text = path.read_text()
    assert len(re.findall(r"^```", text, flags=re.M)) % 2 == 0, path
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        target = urllib.parse.unquote(target.split("#", 1)[0])
        base = report.parent if path == baseline else path.parent
        assert (base / target).resolve().exists(), (path, target)
        refs += 1
        report_refs += path == report
print(json.dumps(dict(requests=len(requests), statuses=dict(statuses), bytes=total,
                      sha_matches=len(requests), markdown_files=len(files),
                      local_refs=refs, report_local_refs=report_refs,
                      frozen_window=True, frozen_sections=[3, 4]), indent=2))
