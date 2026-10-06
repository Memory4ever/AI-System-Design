"""Fetch finite original history slices, not an article review queue."""
from pathlib import Path
import subprocess
import sys

directory = Path(sys.argv[1])
fetch = Path(__file__).parents[0].parent / "daily-20251002" / "fetch.py"
entries = {
    "google-october": "https://www.research.google/blog/2025/10/",
    "google-october-page2": "https://www.research.google/blog/2025/10/?page=2",
    "deepmind-pubs-history": "https://deepmind.google/research/publications/page/2/",
    "ernie-page2": "https://ernie.baidu.com/blog/zh/page/2/",
    "seed-blogs0": "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&order_desc=false&mode=1&page_token=0",
    "seed-blogs20": "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&order_desc=false&mode=1&page_token=20",
    "seed-blogs40": "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&order_desc=false&mode=1&page_token=40",
    "seed-papers0": "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&order_desc=false&mode=1&page_token=0",
    "seed-papers20": "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&order_desc=false&mode=1&page_token=20",
    "arxiv-announced": "https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=language+model&terms-0-field=all&classification-include_cross_list=include&date-filter_by=date_range&date-from_date=2025-10-02&date-to_date=2025-10-03&date-date_type=announced_date&abstracts=show&size=50&order=-announced_date_first",
    "arxiv-cl-titles": "https://arxiv.org/list/cs.CL/2025-10?skip=0&show=25",
    "arxiv-cv-titles": "https://arxiv.org/list/cs.CV/2025-10?skip=0&show=25",
    "arxiv-dc-titles": "https://arxiv.org/list/cs.DC/2025-10?skip=0&show=25",
    "arxiv-pl-titles": "https://arxiv.org/list/cs.PL/2025-10?skip=0&show=25",
    "arxiv-ir-titles": "https://arxiv.org/list/cs.IR/2025-10?skip=0&show=25",
}
for name, url in entries.items():
    subprocess.run([sys.executable, str(fetch), str(directory), name, url], check=True)
subprocess.run([sys.executable, str(fetch), str(directory), "hunyuan-page1", "https://api.hunyuan.tencent.com/api/blog/publicList", "--json-body", '{"pageNum":1,"pageSize":20,"renderType":0}'], check=True)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")), *map(str, directory.glob("*.raw"))], check=True)
