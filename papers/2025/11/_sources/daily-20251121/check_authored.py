"""Check only explicit author Markdown, never upstream raw or other reviewers."""
import pathlib
import re
import subprocess
import urllib.parse

root = pathlib.Path(__file__).resolve().parents[5]
day = pathlib.Path(__file__).parent
files = [root / "papers/2025/11/21/README.md"]
files += [day / name for name in (
    "AUTHOR_STOP.md", "FIRST_BATCH_CALIBRATION.md", "ARXIV_FIRST_CALIBRATION.md",
    "NARROW_TAIL_CALIBRATION.md", "SOURCE_PROGRESS.md", "NANO_OWNER_AND_LIMITS.md")]
files += [root / "papers/2025/11/19/README.md",
          root / "papers/2025/11/_sources/daily-20251119/CODEX_DATE_REOPEN.md"]
errors = []
references = 0
for path in files:
    source = path.read_text()
    if len(re.findall(r"^```", source, re.M)) % 2:
        errors.append(f"{path}: unclosed fence")
    for number, line in enumerate(source.splitlines(), 1):
        if line.rstrip() != line:
            errors.append(f"{path}:{number}: trailing space")
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", source):
        link = match.group(1).strip("<>")
        parts = urllib.parse.urlsplit(link)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        references += 1
        target = pathlib.Path(urllib.parse.unquote(parts.path))
        target = target if target.is_absolute() else path.parent / target
        if not target.exists():
            errors.append(f"{path}: missing {link}")
    result = subprocess.run(["git", "diff", "--no-index", "--check", "/dev/null", str(path)],
                            capture_output=True, text=True)
    if result.stdout or result.stderr or result.returncode not in (0, 1):
        errors.append(f"{path}: diff check {result.stdout}{result.stderr}")
print(f"{len(files)} explicit authored Markdown; {references} local refs; {len(errors)} errors")
print("\n".join(errors))
raise SystemExit(bool(errors))
