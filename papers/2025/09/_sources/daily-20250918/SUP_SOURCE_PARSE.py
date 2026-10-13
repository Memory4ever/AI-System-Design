import datetime
import json
import pathlib

from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent
DECODER = json.JSONDecoder()


def next_objects(name):
    soup = BeautifulSoup((ROOT / name).read_bytes(), "html.parser")
    chunks = []
    for tag in soup.find_all("script"):
        source = tag.get_text()
        cursor = source.find("self.__next_f.push(")
        if cursor < 0:
            continue
        value, _ = DECODER.raw_decode(source[cursor + 19:])
        if len(value) > 1 and isinstance(value[1], str):
            chunks.append(value[1])
    for line in (line for chunk in chunks for line in chunk.splitlines()):
        _, separator, value = line.partition(":")
        if not separator:
            continue
        try:
            yield json.loads(value)
        except json.JSONDecodeError:
            continue


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


result = {}
for name in ("SUP_ANTHROPIC.raw", "SUP_ZAI.raw"):
    objects = [item for value in next_objects(name) for item in walk(value)]
    if "ANTHROPIC" in name:
        rows = [{key: item.get(key) for key in ("title", "publishedOn", "slug")}
                for item in objects if "publishedOn" in item and "title" in item]
        unique = list({json.dumps(row, sort_keys=True): row for row in rows}.values())
        result[name] = dict(object_count=len(rows), unique_records=len(unique),
                            september=[row for row in unique
                                       if str(row["publishedOn"]).startswith("2025-09")])
    else:
        lists = [item for item in objects if "blogsItems" in item]
        result[name] = [dict(hasMore=item.get("hasMore"), nextPage=item.get("nextPage"),
                            blogsItems=[{key: row.get(key) for key in
                                         ("id", "title_zh", "title_en", "createAt")}
                                        for row in item["blogsItems"]])
                        for item in lists]

result["SUP_SEED_BLOG.raw"] = []
seed = json.loads((ROOT / "SUP_SEED_BLOG.raw").read_text())
for item in seed["sub_article_list"]:
    meta = item["ArticleMeta"]
    date = datetime.datetime.fromtimestamp(meta["PublishDate"] / 1000,
                                           datetime.timezone(datetime.timedelta(hours=8)))
    result["SUP_SEED_BLOG.raw"].append(dict(
        title=item["ArticleSubContentEn"]["Title"], date=date.isoformat(),
        pinned=meta["IsPinned"]))
result["SUP_HUNYUAN_PUBLIC.raw"] = [
    {key: item.get(key) for key in ("id", "title", "displayPublishTime", "publishedAt")}
    for item in json.loads((ROOT / "SUP_HUNYUAN_PUBLIC.raw").read_text())["data"]["list"]]
path = ROOT / "SUP_SOURCE_PARSE_V3.json"
if path.exists():
    raise RuntimeError("refusing to overwrite parsed evidence")
path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(result, ensure_ascii=False, indent=2))
