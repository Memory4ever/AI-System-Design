"""Capture named, bounded original-source repairs without overwriting discovery."""

import datetime
import hashlib
import json
from pathlib import Path
import sys
import urllib.request

ROOT = Path(__file__).parent
URLS = {
    "exact-v1-five-recapture": "https://export.arxiv.org/api/query?id_list=2509.01322v1%2C2509.05316v1%2C2509.00192v1%2C2509.00221v1%2C2509.02615v1&max_results=10",
    "meta-publication-page6": "https://ai.meta.com/results/?page=6&content_types%5B0%5D=publication",
    "meta-blog-page3": "https://ai.meta.com/results/?page=3&content_types%5B0%5D=blog",
    "meta-publication-page5": "https://ai.meta.com/results/?page=5&content_types%5B0%5D=publication",
    "meta-blog-page2": "https://ai.meta.com/results/?page=2&content_types%5B0%5D=blog",
    "meta-diversity-original": "https://ai.meta.com/research/publications/jointly-reinforcing-diversity-and-quality-in-language-model-generations/",
    "minimax-en-page2": "https://www.minimax.io/blog?page=2",
    "seed-paper-tail-repair": "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=20&count=20&order_desc=true",
    "seed-paper-entry-repair": "https://seed.bytedance.com/en/public_papers",
    "mimo-index-repair": "https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/index.c5195ace.js",
    "mimo-route-repair": "https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js",
    "mimo-home-repair": "https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/8557.2d420be2.js",
    "mimo-more-component-repair": "https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js",
    "deepmind-robotics-date": "https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/",
    "deepmind-frontier-date": "https://deepmind.google/blog/strengthening-our-frontier-safety-framework/",
    "deepmind-icpc-date": "https://deepmind.google/blog/gemini-achieves-gold-medal-level-at-the-international-collegiate-programming-contest-world-finals/",
    "tconst-v1-core": "https://arxiv.org/html/2509.00202v1",
    "unlearning-v1-core": "https://arxiv.org/html/2509.05316v1",
    "safellava-v1-core": "https://arxiv.org/html/2509.00192v1",
    "hallucination-v1-core": "https://arxiv.org/html/2509.00371v1",
    "bai-v1-core": "https://arxiv.org/html/2509.00309v1",
}

for name in sys.argv[1:]:
    url = URLS[name]
    meta = {"url": url, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "purpose": "new capture, not reconstruction of earlier unsaved tool response"}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ResearchReview/1.0"})
        with urllib.request.urlopen(req, timeout=40) as response:
            raw = response.read()
            meta.update(status=response.status, bytes=len(raw), final_url=response.url,
                        sha256=hashlib.sha256(raw).hexdigest(), headers=dict(response.headers))
            (ROOT / (name + ".raw")).write_bytes(raw)
    except Exception as error:
        meta["error"] = str(error)
    (ROOT / (name + ".request.json")).write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(name, meta.get("status"), meta.get("bytes"), meta.get("error"), flush=True)
