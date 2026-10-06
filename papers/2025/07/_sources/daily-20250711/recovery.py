import concurrent.futures
from capture import fetch
TASKS=[
('seed-2025-p0','https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true'),
('seed-blog-2025-p0','https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true'),
('zai-page2','https://www.zhipuai.cn/zh/research?page=2'),
('qwen-page2','https://qwenlm.github.io/page/2/'),
('qwen-research','https://qwen.ai/api/page_config?code=research.research-list'),
('hunyuan-api','https://api.hunyuan.tencent.com/api/blog/publicList',{'pageNum':1,'pageSize':100,'renderType':0}),
('seed-cot','https://seed.bytedance.com/en/public_papers/understanding-chain-of-thought-in-llms-through-information-theory'),
('seed-cot-history','https://arxiv.org/abs/2411.11984'),
('google-gfm','https://research.google/blog/graph-foundation-models-for-relational-data/'),
('kimi-k2','https://platform.kimi.com/blog/posts/k2-report'),
]
with concurrent.futures.ThreadPoolExecutor(5) as pool:
 for t,result in zip(TASKS,pool.map(lambda t:fetch(*t),TASKS)): print(t[0],len(result))
