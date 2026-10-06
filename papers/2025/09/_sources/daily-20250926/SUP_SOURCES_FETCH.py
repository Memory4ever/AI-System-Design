import json

from SUP_CAPTURE import capture

entries = [
    ("SUP_OPENAI", "https://openai.com/research/", None),
    ("SUP_OPENAI_RSS", "https://openai.com/news/rss.xml", None),
    ("SUP_ANTHROPIC", "https://www.anthropic.com/research", None),
    ("SUP_GOOGLE", "https://research.google/pubs/", None),
    ("SUP_GOOGLE_SEPT", "https://research.google/blog/2025/09/", None),
    ("SUP_DEEPMIND", "https://deepmind.google/research/", None),
    ("SUP_DEEPMIND_P5", "https://deepmind.google/blog/page/5/", None),
    ("SUP_META", "https://ai.meta.com/research/", None),
    ("SUP_META_P5", "https://ai.meta.com/results/?content_types%5B0%5D=publication&page=5", None),
    ("SUP_QWEN", "https://qwen.ai/api/page_config?code=research.research-list", None),
    ("SUP_DEEPSEEK", "https://www.deepseek.com/", None),
    ("SUP_DEEPSEEK_LOG", "https://api-docs.deepseek.com/updates", None),
    ("SUP_KIMI", "https://platform.kimi.com/blog", None),
    ("SUP_HUNYUAN", "https://hunyuan.tencent.com/research", None),
    ("SUP_HUNYUAN_API", "https://api.hunyuan.tencent.com/api/blog/publicList", {"pageNum": 1, "pageSize": 100, "renderType": 0}),
    ("SUP_ZAI", "https://www.zhipuai.cn/zh/research", None),
    ("SUP_ZAI_P2", "https://www.zhipuai.cn/zh/research?page=2", None),
    ("SUP_ZAI_NOTES", "https://docs.z.ai/release-notes/new-released", None),
    ("SUP_SEED", "https://seed.bytedance.com/en/research", None),
    ("SUP_SEED_PAPERS", "https://seed.bytedance.com/en/public_papers", None),
    ("SUP_SEED_BLOG_API", "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true", None),
    ("SUP_SEED_PAPERS_API", "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true", None),
    ("SUP_ERNIE", "https://ernie.baidu.com/blog/zh/", None),
    ("SUP_ERNIE_P2", "https://ernie.baidu.com/blog/zh/page/2/", None),
    ("SUP_MIMO", "https://mimo.xiaomi.com/", None),
    ("SUP_MINIMAX", "https://www.minimax.io/blog", None),
    ("SUP_MINIMAX_CN", "https://www.minimaxi.com/blog", None),
    ("SUP_MINIMAX_AGENT", "https://agent.minimax.io/docs/techblog", None),
]

for name, url, data in entries:
    capture(name, url, json.dumps(data) if data is not None else None, timeout=25)
