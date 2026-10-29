"""Bounded Sep14 recovery captures and mechanical baseline; no source claims."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import re
import xml.etree.ElementTree as ET
import urllib.error
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[4]
REPORT = ROOT / "papers/2025/09/15/README.md"


def save_json(path, value):
    with path.open("x") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def baseline():
    prefix = BASE / "REPAIR_BASELINE_20261022"
    report = REPORT.read_bytes()
    with prefix.with_suffix(".md").open("xb") as handle:
        handle.write(report)
    paths = [REPORT.relative_to(ROOT).as_posix(), BASE.relative_to(ROOT).as_posix()]
    commands = {
        "head": ["git", "rev-parse", "HEAD"],
        "status": ["git", "status", "--porcelain=v1"],
        "scoped_working": ["git", "diff", "--", *paths],
        "scoped_cached": ["git", "diff", "--cached", "--", *paths],
    }
    result = {"checked_utc": datetime.now(timezone.utc).isoformat(),
              "report_bytes": len(report), "report_sha256": hashlib.sha256(report).hexdigest()}
    for key, command in commands.items():
        run = subprocess.run(command, cwd=ROOT, capture_output=True, check=True)
        target = BASE / ("REPAIR_BASELINE_20261022_" + key + ".txt")
        with target.open("xb") as handle:
            handle.write(run.stdout)
        result[key] = {"file": target.name, "sha256": hashlib.sha256(run.stdout).hexdigest()}
    save_json(prefix.with_suffix(".json"), result)
    print(json.dumps(result, ensure_ascii=False))


def capture(stem, url):
    raw = BASE / ("REPAIR_" + stem + "_20261022.raw")
    meta = BASE / ("REPAIR_" + stem + "_20261022.request.json")
    if raw.exists() or meta.exists():
        raise FileExistsError(stem)
    record = {"url": url, "method": "GET", "checked_utc": datetime.now(timezone.utc).isoformat(),
              "headers": {"User-Agent": "AI-System-Design bounded Sep14 recovery", "Accept": "application/vnd.api+json"}}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=record["headers"]), timeout=50) as response:
            body = response.read()
            record.update(status=response.status, final_url=response.url)
    except urllib.error.HTTPError as error:
        body = error.read()
        record.update(status=error.code, error=str(error))
    except Exception as error:
        body = b""
        record["error"] = str(error)
    with raw.open("xb") as handle:
        handle.write(body)
    record.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest(),
                  finished_utc=datetime.now(timezone.utc).isoformat())
    save_json(meta, record)
    print(stem, record.get("status"), record["bytes"], record.get("error", ""), flush=True)


def queries():
    cats = {
        "model": ["cs.CL", "cs.LG"],
        "systems": ["cs.DC", "cs.AR", "cs.PL", "cs.OS", "cs.PF", "cs.LG", "cs.CL"],
        "agents": ["cs.AI", "cs.CL", "cs.IR", "cs.MA"],
        "multimodal": ["cs.CV", "cs.RO", "cs.LG", "cs.CL"],
    }
    groups = {
        "model": [
            ['"language model"', '"language models"', "LLM", "LLMs", "transformer", "transformers", '"mixture of experts"', '"mixture-of-experts"', '"foundation model"', '"foundation models"'],
            ["architecture", "architectures", "attention", "optimization", "optimisation", "training", '"post-training"', "posttraining"],
        ],
        "systems": [
            ['"language model"', '"language models"', "GPU", "GPUs", "LLM", "LLMs"],
            ["inference", "communication", "communications", "kernel", "kernels", "serving", "parallel", "parallelism", "compiler", "compilers", "compilation"],
        ],
        "agents": [
            ['"language model"', '"language models"', "LLM", "LLMs"],
            ["agent", "agents", "agentic", "retrieval", "memory", "memories", "safety", "jailbreak", "jailbreaks", '"tool calling"', '"tool use"', "tool", "tools"],
        ],
        "multimodal": [
            ['"foundation model"', '"foundation models"', '"world model"', '"world models"', '"vision language"', '"vision-language"', '"vision-language-action"', '"vision language action"', '"video generation"', '"video generative"', "diffusion", '"flow matching"', "VLM", "VLMs", "VLA", "VLAs"],
        ],
    }
    specs = []
    for theme in cats:
        category = "(" + " OR ".join("cat:" + c for c in cats[theme]) + ")"
        arxiv = category + " AND " + " AND ".join("(" + " OR ".join("all:" + t for t in group) + ")" for group in groups[theme])
        arxiv += " AND submittedDate:[202509131600 TO 202509141559]"
        dc_category = "subjects.subject:(" + " OR ".join('"' + c + '"' for c in cats[theme]) + ")"
        dc_groups = []
        for group in groups[theme]:
            terms = "(" + " OR ".join(group) + ")"
            dc_groups.append("(titles.title:" + terms + " OR descriptions.description:" + terms + ")")
        dc = dc_category + " AND " + " AND ".join(dc_groups)
        dc += " AND registered:[2025-09-13T16:00:00Z TO 2025-09-14T15:59:59Z]"
        specs.append({"theme": theme, "arxiv": arxiv, "datacite": dc,
                      "category_fields": cats[theme], "lexical_groups": groups[theme]})
    save_json(BASE / "REPAIR_QUERY_SPEC_20261022.json", specs)
    for spec in specs:
        theme = spec["theme"]
        dc_url = "https://api.datacite.org/dois?" + urllib.parse.urlencode({
            "client-id": "arxiv.content", "query": spec["datacite"], "page[size]": 200, "page[number]": 1})
        capture("DCFORMS_" + theme, dc_url)
        arxiv_url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
            "search_query": spec["arxiv"], "start": 0, "max_results": 200,
            "sortBy": "submittedDate", "sortOrder": "ascending"})
        capture("AXFORMS_" + theme, arxiv_url)
        time.sleep(3)


def controls():
    specs = json.loads((BASE / "REPAIR_QUERY_SPEC_20261022.json").read_text())
    known = {r["id"].split("arxiv.")[1]: r for r in json.loads((BASE / "REPAIR_DATE77_20261022.raw").read_text())["data"]}
    selected = {"model": "2509.11155", "systems": "2509.11155", "agents": "2509.11079", "multimodal": "2509.10919"}
    for spec in specs:
        identity = selected[spec["theme"]]
        day = known[identity]["attributes"]["registered"][:10]
        query = spec["datacite"].split(" AND registered:")[0]
        query += ' AND doi:"10.48550/arxiv.' + identity + '"'
        query += " AND registered:[" + day + "T00:00:00Z TO " + day + "T23:59:59Z]"
        url = "https://api.datacite.org/dois?" + urllib.parse.urlencode({"client-id": "arxiv.content", "query": query, "page[size]": 10})
        capture("CONTROL_THEME_" + spec["theme"], url)
    lexical = [
        ("llms", "LLMs", "2509.11155"),
        ("language_models", '"language models"', "2509.11155"),
        ("foundation_models", '"foundation models"', "2509.10919"),
        ("transformers", "transformers", "2509.11208"),
        ("agents", "agents", "2509.11078"),
        ("agentic", "agentic", "2509.11079"),
        ("kernel", "kernel", "2509.14265"),
        ("kernels", "kernels", "2509.14265"),
        ("tool", "tool", "2509.11155"),
        ("tools", "tools", "2509.11065"),
    ]
    for name, term, identity in lexical:
        day = known[identity]["attributes"]["registered"][:10]
        query = "(titles.title:" + term + " OR descriptions.description:" + term + ")"
        query += ' AND doi:"10.48550/arxiv.' + identity + '"'
        query += " AND registered:[" + day + "T00:00:00Z TO " + day + "T23:59:59Z]"
        url = "https://api.datacite.org/dois?" + urllib.parse.urlencode({"client-id": "arxiv.content", "query": query, "page[size]": 10})
        capture("CONTROL_FORM_" + name, url)


def analyze():
    sys.path.insert(0, str(ROOT / "scripts"))
    from arxiv_publication_date import publication_date_envelope
    ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}

    def entries(name):
        root = ET.fromstring((BASE / name).read_bytes())
        return root, root.findall("a:entry", ns)

    def identity(entry):
        return re.search(r"\d{4}\.\d{5}", entry.findtext("a:id", namespaces=ns)).group()

    old = {identity(e) for e in entries("arxiv-api.raw")[1]}
    old66 = set()
    fresh = set()
    themes = []
    for theme in ("model", "systems", "agents", "multimodal"):
        old66.update(identity(e) for e in entries("SUP_arxiv-" + theme + "_20261012.raw")[1])
        root, found = entries("REPAIR_AXFORMS_" + theme + "_20261022.raw")
        fresh.update(identity(e) for e in found)
        dc = json.loads((BASE / ("REPAIR_DCFORMS_" + theme + "_20261022.raw")).read_text())
        themes.append({"theme": theme, "arxiv_total": int(root.findtext("o:totalResults", namespaces=ns)),
                       "arxiv_returned": len(found), "datacite_total": dc["meta"]["total"],
                       "datacite_returned": len(dc["data"]), "datacite_next": dc.get("links", {}).get("next")})
    raw = json.loads((BASE / "REPAIR_DATE77_20261022.raw").read_text())
    derived = [publication_date_envelope(r, r["id"].split("arxiv.")[1]) for r in raw["data"]]
    derived.sort(key=lambda row: row["arxiv_id"])
    save_json(BASE / "REPAIR_DATE77_ENVELOPES_20261022.json", derived)
    extra = publication_date_envelope(json.loads((BASE / "REPAIR_DATE10972_20261022.raw").read_text()), "2509.10972")
    save_json(BASE / "REPAIR_DATE10972_ENVELOPE_20261022.json", extra)
    checks = []
    for path in sorted(BASE.glob("REPAIR_*.request.json")):
        meta = json.loads(path.read_text())
        body = path.with_name(path.name.replace(".request.json", ".raw")).read_bytes()
        assert len(body) == meta["bytes"] and hashlib.sha256(body).hexdigest() == meta["sha256"], path
        checks.append({"file": path.name, "status": meta.get("status"), "bytes": len(body)})
    result = {"checked_utc": datetime.now(timezone.utc).isoformat(), "old96": len(old), "old66": len(old66),
              "old_union107": len(old | old66), "fresh69": len(fresh), "new_only": sorted(fresh - old - old66),
              "total_union108": len(old | old66 | fresh), "themes": themes, "request_checks": checks,
              "date77_bounded": sum(r["status"] == "bounded" for r in derived),
              "date77_lower_bounds_exclude_target": sum(r["earliest_announcement_utc"] > "2025-09-14T15:59:59Z" for r in derived)}
    save_json(BASE / "REPAIR_ANALYSIS_20261022.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def qa(stage):
    current = REPORT.read_text()
    baseline_text = (BASE / "REPAIR_BASELINE_20261022.md").read_text()
    def section4(text):
        return text.split("## 4. 证据与知识整合", 1)[1].split("## 5. 缺口与下一步", 1)[0]
    window = lambda text: re.search(r"^\*\*窗口：\*\* .+$", text, re.M).group()
    targets = []
    for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", current):
        value = urllib.parse.unquote(match.group(1).split("#", 1)[0])
        if not value or "://" in value:
            continue
        path = (REPORT.parent / value).resolve()
        targets.append(str(path))
        assert path.exists(), path
    assert section4(current) == section4(baseline_text), "continuous old section4 changed"
    assert window(current) == window(baseline_text), "old hour window changed"
    relative = REPORT.relative_to(ROOT).as_posix()
    paths = [relative, (BASE / "SUP_SCREEN_FINAL_20261012.md").relative_to(ROOT).as_posix(),
             (BASE / "REPAIR_TOOL_20261022.py").relative_to(ROOT).as_posix()]
    result = {"checked_utc": datetime.now(timezone.utc).isoformat(), "stage": stage,
              "report_bytes": REPORT.stat().st_size, "report_sha256": hashlib.sha256(REPORT.read_bytes()).hexdigest(),
              "old_window_unchanged": True, "continuous_old_section4_unchanged": True,
              "local_references": len(targets), "unique_local_paths": len(set(targets)), "missing_paths": []}
    commands = {"validator": ["python3", "scripts/validate_research.py", "--report", relative],
                "working_check": ["git", "diff", "--check", "--", *paths],
                "cached_check": ["git", "diff", "--cached", "--check", "--", *paths]}
    for name, command in commands.items():
        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        result[name] = {"command": command, "exit": run.returncode, "stdout": run.stdout, "stderr": run.stderr}
    save_json(BASE / ("REPAIR_QA_" + stage + "_20261022.json"), result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if sys.argv[1] == "baseline":
        baseline()
    elif sys.argv[1] == "get":
        capture(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "queries":
        queries()
    elif sys.argv[1] == "controls":
        controls()
    elif sys.argv[1] == "analyze":
        analyze()
    elif sys.argv[1] == "qa":
        qa(sys.argv[2])
