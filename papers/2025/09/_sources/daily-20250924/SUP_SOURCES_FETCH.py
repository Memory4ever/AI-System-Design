import argparse
import json

from SUP_CAPTURE import capture


ENTRIES = [
    ("SUP_OPENAI", "https://openai.com/research/", None),
    ("SUP_OPENAI_RSS", "https://openai.com/news/rss.xml", None),
    ("SUP_ANTHROPIC", "https://www.anthropic.com/research", None),
    ("SUP_GOOGLE", "https://research.google/pubs/", None),
    ("SUP_GOOGLE_SEPT", "https://research.google/blog/2025/09/", None),
    ("SUP_DEEPMIND", "https://deepmind.google/research/", None),
    ("SUP_META", "https://ai.meta.com/research/", None),
    ("SUP_META_P5", "https://ai.meta.com/global_search/?page=5", None),
    ("SUP_QWEN", "https://qwen.ai/api/page_config?code=research.research-list", None),
    ("SUP_DEEPSEEK", "https://www.deepseek.com/", None),
    ("SUP_DEEPSEEK_LOG", "https://api-docs.deepseek.com/updates", None),
    ("SUP_KIMI", "https://platform.kimi.com/blog", None),
    ("SUP_HUNYUAN", "https://hunyuan.tencent.com/research", None),
    ("SUP_ZAI", "https://www.zhipuai.cn/zh/research", None),
    ("SUP_ZAI_NOTES", "https://docs.z.ai/release-notes/new-released", None),
    ("SUP_SEED", "https://seed.bytedance.com/en/research", None),
    ("SUP_SEED_PAPERS", "https://seed.bytedance.com/en/public_papers", None),
    ("SUP_ERNIE", "https://ernie.baidu.com/blog/zh/", None),
    ("SUP_ERNIE_P2", "https://ernie.baidu.com/blog/zh/page/2/", None),
    ("SUP_MIMO", "https://mimo.xiaomi.com/", None),
    ("SUP_MINIMAX", "https://www.minimax.io/blog", None),
    ("SUP_MINIMAX_CN", "https://www.minimaxi.com/blog", None),
    ("SUP_MINIMAX_AGENT", "https://agent.minimax.io/docs/techblog", None),
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int)
    parser.add_argument("stop", type=int)
    options = parser.parse_args()
    for name, url, data in ENTRIES[options.start:options.stop]:
        capture(name, url, json.dumps(data) if data is not None else None)
