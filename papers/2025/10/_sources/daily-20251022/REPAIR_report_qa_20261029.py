"""Read-only checks for this report's preserved baseline and local references."""
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[5]
SOURCES = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2025/10/22/README.md"
text = REPORT.read_text()
baseline = (SOURCES / "REPAIR_BASELINE_20261029.md").read_text()


def section(body, number):
    return body.split(f"## {number}. ", 1)[1].split(f"## {number + 1}. ", 1)[0]


old_rows = [line for line in section(baseline, 3).splitlines() if line.startswith("| [")]
rows = [line for line in section(text, 3).splitlines() if line.startswith("| [")]
old_block = "## 4. " + section(baseline, 4)
links = re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text)
local_links = sorted(set(link.split("#", 1)[0] for link in links if not re.match(r"[a-z]+:", link)))
missing = [link for link in local_links if link and not (REPORT.parent / unquote(link)).exists()]
candidate_urls = [re.search(r"\]\(([^)]+)\)", row).group(1) for row in rows]
evidence_urls = re.findall(r"^### \[[^\n]+\]\(([^)]+)\)", section(text, 4), re.M)
daily_sources = re.findall(r"^\| (SRC-[A-Z-]+) \|", section(text, 2), re.M)
decisions = Counter(row.split(" | ")[-1].split(":", 1)[0].split("：", 1)[0] for row in rows)
paths = ["papers/2025/10/22/README.md", str(SOURCES.relative_to(ROOT))]
diff = subprocess.run(["git", "diff", "--check", "--", *paths], cwd=ROOT, text=True, capture_output=True)
cached = subprocess.run(["git", "diff", "--cached", "--check", "--", *paths], cwd=ROOT, text=True, capture_output=True)
cached_lines = cached.stdout.splitlines()
cached_files = sorted({line.split(":", 1)[0] for line in cached_lines if line.startswith("papers/")})
result = {
    "sha256": hashlib.sha256(REPORT.read_bytes()).hexdigest(),
    "six_sections": len(re.findall(r"^## [1-6]\. ", text, re.M)) == 6,
    "old_rows_exact": len(old_rows) == 2 and all(row in rows for row in old_rows),
    "old_window_exact": next(line for line in baseline.splitlines() if line.startswith("**窗口：**")) in text,
    "old_section4_contiguous": old_block in text,
    "candidate_count": len(rows),
    "unique_candidate_urls": len(set(candidate_urls)),
    "evidence_count": len(evidence_urls),
    "candidate_evidence_match": sorted(candidate_urls) == sorted(evidence_urls),
    "source_count_including_triggered": len(daily_sources),
    "decisions": dict(decisions),
    "local_reference_count": len(local_links),
    "missing_local_references": missing,
    "working_diff_check": {"exit": diff.returncode, "output": diff.stdout + diff.stderr},
    "cached_diff_check": {"exit": cached.returncode, "diagnostic_lines": len(cached_lines), "files": cached_files},
}
print(json.dumps(result, ensure_ascii=False, indent=2))
assert result["six_sections"] and result["old_rows_exact"] and result["old_window_exact"]
assert result["old_section4_contiguous"] and result["candidate_evidence_match"]
assert len(rows) == len(set(candidate_urls)) == len(evidence_urls) == 108
assert not missing and diff.returncode == 0
