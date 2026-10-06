import json
import pathlib
import sys
import urllib.parse
from html.parser import HTMLParser
from fetch_day import fetch, ROOT


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "a" or (tag == "script" and attrs.get("src")):
            self.links.append(attrs.get("href", attrs.get("src", "")))
    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())


if __name__ == "__main__":
    for name in ["seed_papers", "hunyuan_research", "zai_research", "mimo_home"]:
        page = Page()
        page.feed((ROOT / (name + ".raw")).read_text())
        bundle = next((link for link in page.links if
                       (name == "seed_papers" and "/main." in link) or
                       (name == "hunyuan_research" and "/index-" in link) or
                       (name == "zai_research" and "/research/page-" in link) or
                       (name == "mimo_home" and "/index." in link)), None)
        if bundle:
            origin = {"seed_papers":"https://seed.bytedance.com", "hunyuan_research":"https://hunyuan.tencent.com",
                      "zai_research":"https://www.zhipuai.cn", "mimo_home":"https://mimo.xiaomi.com"}[name]
            fetch(name + "_bundle", urllib.parse.urljoin(origin, bundle))
    fetch("zai_page2", "https://www.zhipuai.cn/zh/research?page=2")
    fetch("ernie_page2", "https://ernie.baidu.com/blog/zh/page/2/")
    fetch("minimax_agent_md", "https://agent.minimax.io/docs/techblog.md")
    fetch("hunyuan_publicList", "https://api.hunyuan.tencent.com/api/blog/publicList",
          data=dict(pageNum=1, pageSize=100, renderType=0))
    for kind in [1, 2]:
        for offset in [0, 20, 40, 60, 80]:
            params = dict(article_type=kind, publish_year=2025, count=20,
                          order_desc="false", page_token=offset)
            result = fetch(f"seed_type{kind}_{offset}", "https://seed.bytedance.com/api/get_article_list_v2?" +
                           urllib.parse.urlencode(params), headers={"x-tt-locale":"US"})
            if result["http_status"] != "200":
                break
            response = json.loads((ROOT / result["raw_file"]).read_text())
            if not response.get("has_more"):
                break
