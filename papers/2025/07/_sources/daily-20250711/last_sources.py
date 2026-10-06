import concurrent.futures
from capture import fetch
TASKS=[
('ernie-page2','https://ernie.baidu.com/blog/zh/page/2/'),
('dm-flashlite','https://developers.googleblog.com/en/gemini-25-flash-lite-is-now-stable-and-generally-available'),
('dm-backstory','https://deepmind.google/blog/exploring-the-context-of-online-images-with-backstory/'),
('dm-imo','https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/'),
('dm-t5gemma','https://developers.googleblog.com/en/t5gemma/'),
('dm-medgemma','https://research.google/blog/medgemma-our-most-capable-open-models-for-health-ai-development/'),
]
with concurrent.futures.ThreadPoolExecutor(6) as pool:
    for t,r in zip(TASKS,pool.map(lambda t:fetch(*t),TASKS)): print(t[0],len(r))
