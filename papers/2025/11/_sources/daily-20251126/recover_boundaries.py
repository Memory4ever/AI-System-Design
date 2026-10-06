"""Finite native recovery, not a recursive site or annual-content scan."""
import datetime as dt
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).parent
jobs = [
    ("seed-type1-page20.json", "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&page_token=20&order_desc=true", ["-H", "x-tt-locale: US"]),
    ("seed-type2-page20.json", "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&page_token=20&order_desc=true", ["-H", "x-tt-locale: US"]),
    ("zai-page2.rsc", "https://www.zhipuai.cn/zh/research?page=2", ["-H", "RSC: 1"]),
    ("deepmind-page4.html", "https://deepmind.google/blog/page/4/", []),
    ("google-pubs2025.html", "https://research.google/pubs/?year=2025", []),
    ("meta-research.html", "https://ai.meta.com/research/", []),
]
for name, url, headers in jobs:
    target = ROOT / name
    run = subprocess.run(["curl", "--max-time", "20", "-L", "-sS", "-A", "Mozilla/5.0", *headers,
                          url, "-o", str(target), "-w", "%{http_code}"], capture_output=True, text=True)
    receipt = {"url": url, "headers": headers, "executed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
               "http_status": run.stdout, "exit_code": run.returncode, "error": run.stderr,
               "bytes": target.stat().st_size if target.exists() else 0,
               "stop": "specified single recovery page; no automatic next-page traversal"}
    (ROOT / (name + ".receipt.json")).write_text(json.dumps(receipt, ensure_ascii=False, indent=2))
    print(json.dumps({"file": name, **receipt}, ensure_ascii=False), flush=True)
