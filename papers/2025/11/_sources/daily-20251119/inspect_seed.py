"""Extract pagination and dated identities, not an abstract-reading queue."""
import datetime
import json
import pathlib

root = pathlib.Path(__file__).parent
result = {}
for filename in ("seed_papers_page0.json", "seed_blog_page0.json",
                 "seed_blog_page20.json", "seed_publications_page20.json"):
    data = json.loads((root / filename).read_text())
    fields = {key: value for key, value in data.items() if key != "sub_article_list"}
    rows = []
    for item in data.get("sub_article_list", []):
        meta = item["ArticleMeta"]
        rows.append({"id": meta["ID"], "article_type": meta["ArticleType"],
                     "pinned": meta["IsPinned"], "publish_date_raw": meta["PublishDate"],
                     "publish_utc": datetime.datetime.fromtimestamp(
                         meta["PublishDate"] / 1000, datetime.timezone.utc).isoformat(),
                     "title": item["ArticleSubContentEn"]["Title"]})
    result[filename] = {"pagination": fields, "identities": rows}
output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
(root / "seed_page_boundaries.json").write_text(output)
print(output)
