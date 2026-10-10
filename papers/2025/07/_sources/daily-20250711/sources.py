import concurrent.futures
from capture import fetch
SOURCES={
'openai':'https://openai.com/news/rss.xml',
'anthropic':'https://www.anthropic.com/research',
'deepmind':'https://deepmind.google/blog/page/6/',
'google-month':'https://research.google/blog/2025/07/',
'google-pubs':'https://research.google/pubs/',
'meta':'https://ai.meta.com/research/',
'qwen':'https://qwenlm.github.io/',
'deepseek':'https://www.deepseek.com/',
'moonshot':'https://platform.kimi.com/blog',
'hunyuan':'https://hunyuan.tencent.com/research',
'zai':'https://www.zhipuai.cn/zh/research',
'seed':'https://seed.bytedance.com/en/public_papers',
'ernie':'https://ernie.baidu.com/blog/zh/',
'mimo':'https://mimo.xiaomi.com/',
'minimax':'https://www.minimax.io/blog',
'minimax-cn':'https://www.minimaxi.com/blog',
}
with concurrent.futures.ThreadPoolExecutor(6) as pool:
 for name,data in pool.map(lambda t:(t[0],fetch(*t)),SOURCES.items()): print(name,len(data))
