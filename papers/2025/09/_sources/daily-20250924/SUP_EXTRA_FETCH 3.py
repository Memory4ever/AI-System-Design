import json

from SUP_CAPTURE import capture

entries = [
    ("SUP_QWEN_EDIT", "https://docs.qwenlm.ai/research/qwen-image-edit-2509/index.json", None),
    ("SUP_QWEN_GUARD", "https://docs.qwenlm.ai/research/qwen3guard/index.json", None),
    ("SUP_QWEN_TRAVEL", "https://docs.qwenlm.ai/research/agent/index.json", None),
    ("SUP_QWEN_LIVE", "https://docs.qwenlm.ai/research/qwen3-livetranslate/index.json", None),
    ("SUP_QWEN_VL", "https://docs.qwenlm.ai/research/qwen3-vl/index.json", None),
    ("SUP_META_RESULTS_P5", "https://ai.meta.com/results/?content_types%5B0%5D=publication&page=5", None),
    ("SUP_DEEPMIND_REAL_P5", "https://deepmind.google/blog/page/5/", None),
    ("SUP_GOOGLE_RETRY", "https://research.google/pubs/", None),
    ("SUP_GOOGLE_SEPT_RETRY", "https://research.google/blog/2025/09/", None),
    ("SUP_HUNYUAN_API", "https://api.hunyuan.tencent.com/api/blog/publicList", {"pageNum": 1, "pageSize": 100, "renderType": 0}),
    ("SUP_ZAI_P2", "https://www.zhipuai.cn/zh/research?page=2", None),
    ("SUP_SEED_BLOG_API", "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true", None),
    ("SUP_SEED_PAPERS_API", "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true", None),
    ("SUP_ARXIV_ADVANCED", "https://arxiv.org/search/advanced", None),
]
for name, url, data in entries:
    capture(name, url, json.dumps(data) if data is not None else None, timeout=60)
