import datetime
import json
import pathlib
import re
from recover_day import ROOT, Page


for filename in sorted(ROOT.glob("seed_type*.raw")):
    response = json.loads(filename.read_text())
    print(filename.name, {key:value for key,value in response.items() if key != "sub_article_list"})
    for article in response.get("sub_article_list", []):
        date = datetime.datetime.fromtimestamp(article["ArticleMeta"]["PublishDate"]/1000, datetime.timezone.utc)
        if datetime.datetime(2025,10,15,tzinfo=datetime.timezone.utc) <= date < datetime.datetime(2025,10,21,tzinfo=datetime.timezone.utc):
            print(article["ArticleSubContentEn"]["Title"], date.isoformat(), article)
response = json.loads((ROOT/"hunyuan_publicList.raw").read_text())
print("HUNYUAN", response["data"]["totalNum"])
for article in response["data"]["list"]:
    print(article["title"], re.findall(r"date =[^\n]+", article.get("content", ""))[:1])
raw = (ROOT/"anthropic_research.raw").read_text()
for match in re.finditer(r"2025-10-1[78]", raw):
    print("ANTHROPIC", raw[max(0,match.start()-150):match.end()+150])
