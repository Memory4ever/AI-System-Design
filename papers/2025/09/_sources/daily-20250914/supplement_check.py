"""Check scoped preservation and references; this does not validate research semantics."""
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

BASE = Path(__file__).resolve().parent
REPORT = BASE.parent.parent / "14" / "README.md"
baseline = (BASE / "SUP_BASELINE_README_20261012.md").read_text()
current = REPORT.read_text()

def section(text, number):
    start = text.index("## " + str(number) + ". ")
    end = text.find("\n## ", start + 1)
    return text[start:end if end >= 0 else len(text)]

def window(text):
    return next(line for line in text.splitlines() if line.startswith("**窗口：**"))

assert window(current) == window(baseline), "Original window changed"
assert section(current, 4) == section(baseline, 4), "Original continuous section 4 changed"
assert [line for line in section(current, 3).splitlines() if line.startswith("|")] == [
    line for line in section(baseline, 3).splitlines() if line.startswith("|")
], "Original candidate rows changed"
documents = [REPORT, *sorted(BASE.glob("SUP_*.md"))]
references = 0
anchors = 0
for document in documents:
    origin = REPORT.parent if document.name == "SUP_BASELINE_README_20261012.md" else document.parent
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", document.read_text()):
        if "://" in target or target.startswith("mailto:"):
            continue
        path, _, anchor = unquote(target).partition("#")
        resolved = (origin / path).resolve() if path else document
        assert resolved.exists(), f"Missing reference: {document.name}: {target}"
        references += 1
        anchors += bool(anchor)
requests = list(BASE.glob("SUP_*_20261012.request.json"))
for request in requests:
    record = json.loads(request.read_text())
    raw = request.with_name(request.name.replace(".request.json", ".raw")).read_bytes()
    assert len(raw) == record["bytes"], request.name
    assert hashlib.sha256(raw).hexdigest() == record["sha256"], request.name
print(json.dumps({"freeze": "passed", "markdown": len(documents),
                  "local_references": references, "anchors": anchors,
                  "requests_verified": len(requests)}))
