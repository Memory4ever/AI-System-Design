"""Check author Markdown only, leaving upstream raw material unchanged."""

import json
import re
import sys
from pathlib import Path

month = Path(__file__).parents[2]
errors = []
for day in sys.argv[1:] or ["16"]:
    source = month / ("_sources/daily-202511" + day)
    files = [month / day / "README.md"] + [
        path for path in source.glob("*.md") if not path.name.startswith("raw-")
    ]
    references = 0
    for path in files:
        content = path.read_text()
        if any(line.rstrip() != line for line in content.splitlines()):
            errors.append(str(path) + ": trailing whitespace")
        if len(re.findall(r"^```", content, re.M)) % 2:
            errors.append(str(path) + ": unpaired fence")
        for target in re.findall(r"\]\(([^)]+)\)", content):
            target = target.split("#")[0].split(" ")[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            references += 1
            if not (path.parent / target).exists():
                errors.append(str(path) + ": missing " + target)
    json_files = list(source.glob("*.json"))
    for path in json_files:
        try:
            json.loads(path.read_text())
        except Exception as error:
            errors.append(str(path) + ": " + str(error))
    print(day, "author Markdown", len(files), "local refs", references,
          "JSON", len(json_files))
print("errors", errors)
raise SystemExit(bool(errors))
