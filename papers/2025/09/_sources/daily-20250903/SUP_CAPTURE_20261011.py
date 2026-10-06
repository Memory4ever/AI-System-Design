"""Retrieve bounded official inputs without replacing the original day's captures."""
import datetime
import hashlib
import importlib.util
import json
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = pathlib.Path(__file__).parent
OUT = BASE / "supplement-20261011"
spec = importlib.util.spec_from_file_location("original_capture", BASE / "capture.py")
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)
URLS = {name: original.URLS[name] for name in (
    "openai-rss", "anthropic", "google-pubs", "deepmind-research", "google-month",
    "meta-publication", "meta-results6", "meta-blog3", "meta-darling", "qwen-config",
    "deepseek-home", "deepseek", "moonshot", "hunyuan", "hunyuan-api", "zai",
    "zai-releases", "seed", "seed-blog2025", "seed-paper", "ernie", "ernie-page2",
    "mimo", "minimax-en", "minimax-cn", "minimax-agent",
)}
URLS["qwen-canonical"] = "https://qwenlm.github.io/"
URLS["arxiv-availability"] = "https://info.arxiv.org/help/availability.html"
URLS["arxiv-cl-day-attempt"] = "https://arxiv.org/list/cs.CL/2025-09-02?show=2000"
URLS["arxiv-cv-month-first"] = "https://arxiv.org/list/cs.CV/2025-09?skip=0&show=100"
URLS["arxiv-cl-month-first"] = "https://arxiv.org/list/cs.CL/2025-09?skip=0&show=100"
URLS["anthropic-claude4-corrected-card"] = "https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285/Claude%204%20System%20Card.pdf"
URLS["anthropic-opus41-addendum"] = "https://assets.anthropic.com/m/4c024b86c698d3d4/original/Claude-4-1-System-Card.pdf"
URLS["anthropic-opus41-announcement"] = "https://www.anthropic.com/news/claude-opus-4-1"
URLS["arxiv-advanced-form"] = "https://arxiv.org/search/advanced"
URLS["seed-main-js"] = "https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/deploy/flow/ai_official_website/88329/static/js/main.c981da25.js"
URLS["seed-paper-us0"] = original.URLS["seed-paper"]
URLS["seed-paper-us20"] = original.URLS["seed-paper20"]
URLS["seed-blog-us0"] = original.URLS["seed-blog2025"]
URLS["seed-paper-realUS0"] = original.URLS["seed-paper"]
URLS["seed-paper-realUS20"] = original.URLS["seed-paper20"]
URLS["seed-blog-realUS0"] = original.URLS["seed-blog2025"]
URLS["google-month-2"] = original.URLS["google-month-2"]
URLS["google-aug"] = original.URLS["google-aug"]
URLS["meta-results5"] = original.URLS["meta-results5"]
URLS["meta-blog2"] = original.URLS["meta-blog2"]
URLS["meta-blog"] = original.URLS["meta-blog"]
URLS["zai-page2"] = original.URLS["zai-page2"]
URLS["minimax-en2"] = original.URLS["minimax-en2"]
URLS["seed-pxdesign"] = "https://seed.bytedance.com/zh/public_papers/pxdesign-fast-modular-and-accurate-de-novo-design-of-protein-binders"
THEMES = dict(original.THEMES)
THEMES["hardware"] = '(cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"large language model" OR all:LLM OR all:transformer)'
for name, theme in THEMES.items():
    params = {
        "search_query": theme + " AND submittedDate:[202508291800 TO 202509011800]",
        "start": 0, "max_results": 200, "sortBy": "submittedDate", "sortOrder": "ascending",
    }
    URLS["arxiv-" + name] = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)


def fields(*terms):
    return "(" + " OR ".join(field + ":\"" + term + "\"" for term in terms for field in ("ti", "abs")) + ")"


NARROW = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND ' + fields("language model", "LLM", "transformer", "mixture of experts") + ' AND ' + fields("architecture", "attention", "optimizer", "training", "evaluation"),
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.CL) AND ' + fields("language model", "GPU", "LLM") + ' AND ' + fields("inference", "communication", "kernel", "serving", "parallel"),
    "multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL) AND ' + fields("foundation model", "world model", "vision language", "vision-language", "VLA", "multimodal model"),
    "agents": '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND ' + fields("language model", "LLM") + ' AND ' + fields("agent", "retrieval", "memory", "safety", "jailbreak"),
    "hardware": '(cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND ' + fields("large language model", "LLM", "transformer"),
}
for name, theme in NARROW.items():
    params = {"search_query": theme + " AND submittedDate:[202508291800 TO 202509011800]", "start": 0, "max_results": 200, "sortBy": "submittedDate", "sortOrder": "ascending"}
    URLS["arxiv-narrow-" + name] = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)


def retrieve(name, url):
    OUT.mkdir(exist_ok=True)
    headers = {"User-Agent": "Mozilla/5.0"}
    data = None
    receipt = {
        "url": url, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "purpose": "2025-09-02 BJT supplement; current directory and submittedDate are not public-date proof",
        "method": "GET",
    }
    if name == "hunyuan-api":
        payload = {"pageNum": 1, "pageSize": 100, "renderType": 0}
        data = json.dumps(payload).encode()
        headers["Content-Type"] = "application/json"
        receipt.update(method="POST", body=payload)
    if name.startswith("seed-"):
        headers["Accept-Language"] = "en-US,en;q=0.9"
        headers["Referer"] = "https://seed.bytedance.com/en/public_papers"
        if "-us" in name:
            headers["x-tt-locale"] = "en-US"
        if "-realUS" in name:
            headers["x-tt-locale"] = "US"
    receipt["headers"] = headers
    request = urllib.request.Request(url, headers=headers, data=data)
    body = None
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            body = response.read()
            receipt.update(status=response.status, final_url=response.url, response_headers=dict(response.headers))
    except urllib.error.HTTPError as error:
        body = error.read()
        receipt.update(status=error.code, error=str(error), final_url=error.url)
    except Exception as error:
        receipt["error"] = str(error)
    if body is not None:
        receipt.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
        (OUT / (name + ".raw")).write_bytes(body)
    (OUT / (name + ".request.json")).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(name, receipt.get("status"), receipt.get("bytes"), receipt.get("error"), flush=True)
    return receipt


def extract_exact():
    from lxml import html
    rows = []
    for path in sorted(OUT.glob("abs-2509.*v1.raw")):
        receipt = json.loads(path.with_suffix(".request.json").read_text())
        if receipt.get("status") != 200:
            continue
        root = html.fromstring(path.read_bytes())
        def text_at(xpath):
            return " ".join(" ".join(root.xpath(xpath)).split())
        rows.append({
            "id": path.stem.removeprefix("abs-"), "url": receipt["url"], "abshtml": path.name,
            "title": text_at('//meta[@name="citation_title"]/@content'),
            "abstract": text_at('//blockquote[contains(@class,"abstract")]//text()'),
            "comments": text_at('//td[contains(@class,"comments")]//text()'),
            "history": text_at('//div[contains(@class,"submission-history")]//text()'),
            "citation_arxiv_id": text_at('//meta[@name="citation_arxiv_id"]/@content'),
        })
    (OUT / "SUP_EXACT_20261011.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
    print("exact parsed", len(rows), "empty abstracts", [row["id"] for row in rows if not row["abstract"]])


if __name__ == "__main__":
    names = sys.argv[1:] or list(URLS)
    for name in names:
        if name == "--extract":
            extract_exact()
            continue
        if name.startswith(("abs-2509.", "abs-2510.")) and name.endswith("v1"):
            retrieve(name, "https://arxiv.org/abs/" + name.removeprefix("abs-"))
        elif name.startswith("core-2509.") and name.endswith("v1"):
            retrieve(name, "https://arxiv.org/html/" + name.removeprefix("core-"))
        else:
            retrieve(name, URLS[name])
