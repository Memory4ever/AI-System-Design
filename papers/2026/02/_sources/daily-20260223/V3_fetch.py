"""Original source recovery for the single 2026-02-23 Daily window."""
import concurrent.futures
import json
import pathlib
import urllib.request

BASE = pathlib.Path(__file__).parent
TASKS = [
    ('openai_rss', 'https://openai.com/news/rss.xml', None),
    ('anthropic_research', 'https://www.anthropic.com/research', None),
    ('deepmind_rss', 'https://deepmind.google/blog/rss.xml', None),
    ('google_blog_feb', 'https://research.google/blog/?year=2026&month=2', None),
    ('google_pubs', 'https://research.google/pubs/?year=2026', None),
    ('meta', 'https://ai.meta.com/research/', None),
    ('qwen', 'https://qwen.ai/blog', None),
    ('deepseek', 'https://www.deepseek.com/', None),
    ('moonshot', 'https://platform.kimi.com/blog', None),
    ('hunyuan', 'https://hunyuan.tencent.com/research', None),
    ('hunyuan_list', 'https://hunyuan.tencent.com/api/blog/publicList', {'page':1,'pageSize':100,'tag':''}),
    ('zai', 'https://www.zhipuai.cn/zh/research', None),
    ('zai_releases', 'https://docs.z.ai/release-notes/new-released', None),
    ('seed_papers', 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&order_desc=false&page_token=0&count=100&locale=en-US', None),
    ('seed_blogs', 'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2026&order_desc=false&page_token=0&count=100&locale=en-US', None),
    ('ernie', 'https://ernie.baidu.com/blog/zh/', None),
    ('mimo', 'https://mimo.xiaomi.com/blog', None),
    ('minimax', 'https://www.minimax.io/blog', None),
    ('minimax_cn', 'https://www.minimaxi.com/blog', None),
    ('minimax_agent', 'https://agent.minimax.io/docs/techblog', None),
    ('availability', 'https://info.arxiv.org/help/availability.html', None),
]
RECOVERY = [
    ('hunyuan_real', 'https://api.hunyuan.tencent.com/api/blog/publicList', {'pageNum':1,'pageSize':100,'renderType':0}),
    ('google_blog_archive', 'https://research.google/blog/?year=2026&page=6', None),
    ('qwen_git', 'https://api.github.com/repos/QwenLM/Qwen3.5/commits?since=2026-02-22T01%3A00%3A00Z&until=2026-02-23T01%3A00%3A00Z&per_page=100', None),
    ('moonshot_git', 'https://api.github.com/repos/MoonshotAI/Kimi-K2.5/commits?since=2026-02-22T01%3A00%3A00Z&until=2026-02-23T01%3A00%3A00Z&per_page=100', None),
    ('deepseek_git', 'https://api.github.com/repos/deepseek-ai/DeepSeek-V3.2/commits?since=2026-02-22T01%3A00%3A00Z&until=2026-02-23T01%3A00%3A00Z&per_page=100', None),
    ('glm_git', 'https://api.github.com/repos/zai-org/GLM-5/commits?since=2026-02-22T01%3A00%3A00Z&until=2026-02-23T01%3A00%3A00Z&per_page=100', None),
    ('ernie_git', 'https://api.github.com/repos/PaddlePaddle/ERNIE/commits?since=2026-02-22T01%3A00%3A00Z&until=2026-02-23T01%3A00%3A00Z&per_page=100', None),
    ('mimo_git', 'https://api.github.com/repos/XiaomiMiMo/MiMo-V2-Flash/commits?since=2026-02-22T01%3A00%3A00Z&until=2026-02-23T01%3A00%3A00Z&per_page=100', None),
    ('minimax_git', 'https://api.github.com/repos/MiniMax-AI/MiniMax-M2.5/commits?since=2026-02-22T01%3A00%3A00Z&until=2026-02-23T01%3A00%3A00Z&per_page=100', None),
]
FINAL_RECOVERY = [
    ('google_2026', 'https://research.google/blog/2026/?page=6', None),
    ('deepmind_feed', 'https://deepmind.google/api/v1/blog/feeds/rss/', None),
    ('arxiv_datacite', 'https://api.datacite.org/dois?prefix=10.48550&query=created%3A%5B2026-02-22T01%3A00%3A00Z%20TO%202026-02-23T00%3A59%3A59Z%5D&page%5Bsize%5D=100', None),
    ('qwen_news', 'https://qwen.ai/blog?id=qwen3.5', None),
]
EXTRA = [
    ('hunyuan_zh', 'https://api.hunyuan.tencent.com/api/blog/publicList', {'pageNum':1,'pageSize':100,'renderType':0}, {'Accept-Language':'zh-CN,zh;q=0.9'}),
    ('meta_blog2', 'https://ai.meta.com/blog/?page=2', None),
]

def fetch(task):
    name, url, payload = task[:3]
    headers={'User-Agent':'Mozilla/5.0','Content-Type':'application/json','Accept-Language':'en-US,en;q=0.9'}
    if len(task)>3:
        headers.update(task[3])
    req=urllib.request.Request(url, data=json.dumps(payload).encode() if payload else None,
        headers=headers)
    try:
        with urllib.request.urlopen(req,timeout=25) as response:
            raw=response.read()
            (BASE/('V3_NATIVE_'+name+'.txt')).write_bytes(raw)
            return {'name':name,'url':url,'payload':payload,'status':response.status,'bytes':len(raw)}
    except Exception as error:
        return {'name':name,'url':url,'payload':payload,'error':str(error)}

if __name__=='__main__':
    import sys
    tasks=EXTRA if '--extra' in sys.argv else FINAL_RECOVERY if '--final' in sys.argv else RECOVERY if '--recover' in sys.argv else TASKS
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results=list(pool.map(fetch,tasks))
    (BASE/('V3_NATIVE_EXTRA.json' if '--extra' in sys.argv else 'V3_NATIVE_FINAL_RECOVERY.json' if '--final' in sys.argv else 'V3_NATIVE_RECOVERY.json' if '--recover' in sys.argv else 'V3_NATIVE_FETCH.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(results,ensure_ascii=False,indent=2))
