import datetime
import json

from bs4 import BeautifulSoup
from SUP_CAPTURE import ROOT
from SUP_RSC_PARSE import walk

soup = BeautifulSoup((ROOT / "SUP_ANTHROPIC.raw").read_text(), "html.parser")
chunks = []
for script in soup.find_all("script"):
    value = script.string or script.get_text()
    prefix = "self.__next_f.push("
    if value.startswith(prefix):
        parsed = json.loads(value[len(prefix):-1])
        if len(parsed) > 1 and isinstance(parsed[1], str):
            chunks.append(parsed[1])
objects = []
for line in "".join(chunks).splitlines():
    payload = line.partition(":")[2]
    if payload.startswith(("{", "[")):
        try:
            objects.extend(walk(json.loads(payload)))
        except json.JSONDecodeError:
            pass
pubs = [x for x in objects if "publishedOn" in x]
pubs = list({json.dumps(x, sort_keys=True):x for x in pubs}.values())
(ROOT / "SUP_ANTHROPIC_FIELDS.json").write_text(json.dumps(pubs, ensure_ascii=False, indent=2) + "\n")
print("ANTHROPIC", len(pubs), [(x.get("title"), x.get("publishedOn")) for x in pubs if "2025-09" in str(x.get("publishedOn"))])
for key in ["SUP_ZAI", "SUP_ZAI_P2"]:
    data = json.loads((ROOT / (key + ".rsc.json")).read_text())[0]
    print(key, "count", len(data["blogsItems"]), "next", data["nextPage"], "hasMore", data["hasMore"])
    for x in data["blogsItems"]:
        print(x.get("title_en"), x.get("createAt"), x.get("date"))
data = json.loads((ROOT / "SUP_HUNYUAN_API.raw").read_text())["data"]
print("HUNYUAN", data["totalNum"], len(data["list"]))
for x in data["list"]:
    print(x["id"], x["title"], {k:v for k,v in x.items() if "time" in k.lower() or "date" in k.lower()})
data = json.loads((ROOT / "SUP_SEED_BLOG_API.raw").read_text())
print("SEED", {k:v for k,v in data.items() if k != "sub_article_list"})
for x in data["sub_article_list"]:
    meta = x["ArticleMeta"]
    print(datetime.datetime.fromtimestamp(meta["PublishDate"]/1000, datetime.timezone(datetime.timedelta(hours=8))).isoformat(), meta["IsPinned"], x["ArticleSubContentEn"]["Title"])
print("SEED_PAPERS", (ROOT / "SUP_SEED_PAPERS_API.raw").read_text())
