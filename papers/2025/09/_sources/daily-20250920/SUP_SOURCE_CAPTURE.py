from SUP_CAPTURE import capture

ENTRIES = [
    ("OPENAI", "https://openai.com/research/"),
    ("OPENAI_RSS", "https://openai.com/news/rss.xml"),
    ("ANTHROPIC", "https://www.anthropic.com/research"),
    ("GOOGLE_PUBS", "https://research.google/pubs/"),
    ("GOOGLE_BLOG", "https://research.google/blog/2025/09/"),
    ("DEEPMIND", "https://deepmind.google/research/"),
    ("META", "https://ai.meta.com/research/"),
    ("QWEN", "https://qwenlm.github.io/"),
    ("QWEN_CODE_ONLY", "https://qwen.ai/api/page_config?code=research.research-list"),
    ("DEEPSEEK", "https://www.deepseek.com/"),
    ("DEEPSEEK_UPDATES", "https://api-docs.deepseek.com/updates/"),
    ("KIMI", "https://platform.kimi.com/blog"),
    ("HUNYUAN", "https://hunyuan.tencent.com/research"),
    ("ZAI", "https://www.zhipuai.cn/zh/research?page=2"),
    ("SEED", "https://seed.bytedance.com/en/research"),
    ("SEED_BLOG", "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true"),
    ("SEED_PAPER", "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true"),
    ("ERNIE", "https://ernie.baidu.com/blog/zh/"),
    ("ERNIE_PAGE2", "https://ernie.baidu.com/blog/zh/page/2/"),
    ("MIMO", "https://mimo.xiaomi.com/"),
    ("MINIMAX", "https://www.minimax.io/blog"),
    ("MINIMAX_CN", "https://www.minimaxi.com/blog"),
    ("MINIMAX_AGENT", "https://agent.minimax.io/docs/techblog"),
]
for name, url in ENTRIES:
    capture("SUP_" + name, url)
capture("SUP_HUNYUAN_API", "https://api.hunyuan.tencent.com/api/blog/publicList",
        '{"pageNum":1,"pageSize":100,"renderType":0}')
