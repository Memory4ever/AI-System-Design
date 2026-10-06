"""Nov28 finite native metadata and first exact-v1 calibration batch."""
import ast
import datetime as dt
import json
import pathlib
import urllib.parse

ROOT = pathlib.Path(__file__).parent
# Reuse only parser definitions, never the other day's queries or results.
tree = ast.parse((ROOT.parent / "daily-20251127/recover_boundaries.py").read_text())
nodes = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef))]
exec(compile(ast.Module(body=nodes, type_ignores=[]), "catalog_parser", "exec"))

for name in ("anthropic.html", "deepseek-updates.html", "moonshot.html", "mimo.html", "qwen-old.html", "ernie.html"):
    page = Page()
    page.feed((ROOT / name).read_text())
    if name == "anthropic.html":
        objects, chunks, frames = flight_objects(page)
        rows = {}
        for obj in objects:
            for value in walk(obj):
                if value.get("_type") == "post" and value.get("publishedOn"):
                    slug = value.get("slug", {})
                    slug = slug.get("current") if isinstance(slug, dict) else slug
                    rows[slug] = {"slug": slug, "publishedOn": value["publishedOn"], "title": value.get("title")}
        result = {"transport_chunks": chunks, "text_frames": frames, "unique_dated": len(rows),
                  "target_neighbors": sorted([v for v in rows.values() if "2025-11" in v["publishedOn"] or
                  v["publishedOn"].startswith("2025-12-01")], key=lambda v: v["publishedOn"]),
                  "role": "current catalog, not deletion completeness"}
    else:
        result = {"text": page.text, "pagination_links": [u for u in page.links if "page" in u or "index" in u]}
    (ROOT / (name + ".metadata.json")).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(name, json.dumps(result, ensure_ascii=False)[:7500], flush=True)

for kind in (1, 2):
    first = json.loads((ROOT / f"seed-type{kind}-page0.json").read_text())
    params = urllib.parse.urlencode({"article_type": kind, "publish_year": 2025, "count": 20,
                                   "page_token": first["next_page_token"], "order_desc": "true"})
    fetch(f"seed-type{kind}-page20.json", "https://seed.bytedance.com/api/get_article_list_v2?" + params,
          ("-H", "x-tt-locale: US"))
    for token in (0, 20):
        obj = json.loads((ROOT / f"seed-type{kind}-page{token}.json").read_text())
        rows = [{"title": x["ArticleSubContentEn"]["Title"], "date_ms": x["ArticleMeta"]["PublishDate"],
                 "utc": dt.datetime.fromtimestamp(x["ArticleMeta"]["PublishDate"] / 1000, dt.timezone.utc).isoformat(),
                 "pinned": x["ArticleMeta"]["IsPinned"]} for x in obj["sub_article_list"]]
        result = {"type": kind, "token": token, "returned": len(rows), "total": obj["total"],
                  "has_more": obj["has_more"], "next_page_token": obj["next_page_token"], "metadata": rows}
        (ROOT / f"seed-type{kind}-page{token}.metadata.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
        print("SEED", json.dumps(result, ensure_ascii=False), flush=True)

for name, url in (
    ("zai-page2.html", "https://www.zhipuai.cn/zh/research?page=2"),
    ("deepmind-page4.html", "https://deepmind.google/blog/page/4/"),
    ("deepmind-page5.html", "https://deepmind.google/blog/page/5/"),
    ("arxiv-csDC-titles.html", "https://arxiv.org/list/cs.DC/2025-11?skip=200&show=50"),
):
    fetch(name, url)

for pid in ("2511.21089", "2511.21635", "2511.21408", "2511.20982", "2511.21690", "2511.20795", "2511.20836", "2511.20799"):
    fetch("abs-" + pid + "v1.html", "https://arxiv.org/abs/" + pid + "v1")
    path = fetch("date-" + pid + ".json", "https://api.datacite.org/dois/10.48550/arXiv." + pid)
    if path:
        value = json.loads(path.read_text())["data"]["attributes"]
        print("DATE", pid, json.dumps({k: value.get(k) for k in ("created", "registered", "dates")}), flush=True)

