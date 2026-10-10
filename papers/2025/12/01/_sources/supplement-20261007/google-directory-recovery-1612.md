# Google目录定点恢复原站观察

执行日期：2026-10-07，Asia/Shanghai；本次回源及有界补检在16:12:09+08:00前实际结束，精确请求秒未另采集。不伪造逐请求开始时刻。作者Avicenna，只核12-01补充窗2025-11-30，不使用root其他日期分页观察授本窗覆盖。

## DeepMind

web.open实际URL：https://deepmind.google/research/publications/
返回text/html，149行，Crawled today。本次原站观察摘录：

```text
L117: 265 publications
L145: 3 December 2025 Capturing Human Preferences with Reward Features
L146: 21 November 2025 Imitation Learning is Probably Existentially Safe
L147日期: 4 November 2025
```

实际只核目标日两侧日期/身份与分页边界，不读30篇正文，不给265项授召回，不打开与Nov30无关的page2/3/9。该原站结果与原`deepmind-page3.html`实际首页一致；旧26个月标签题名没有变成真正第3页或当天命中。

## Google Research pubs

web.open默认URL：https://research.google/pubs/
返回text/html，710行，Crawled today。实际默认页观察摘录：

```text
L113: Year
L125: 2025 678
L374-L377: Title / Title, descending / Year / Year, descending
L380: 1 - 15 of 11597 publications
```

默认可见条目署2027/2026出版年，年份选项678不是本次已读678项，也不是已生效的目标日过滤。上述目录展示不含Nov30公开日切片，停止默认首页，不把全年条目送入贡献队列；没有读这些条目的完整题摘/正文。

web.open实际年参数URL：https://research.google/pubs/?year=2025
真实返回：`Internal Error ()`，1行。不能写HTTP状态、成功2025过滤或零结果。没有把root另一次实际年筛选观察冒称本作者结果。

本机尝试：`curl -L --max-time 25 -o papers/2025/12/01/_sources/supplement-20261007/google-pubs-default-recovery.html -w 'HTTP=%{http_code} bytes=%{size_download} effective=%{url_effective}\n' https://research.google/pubs/`。实际exit28：`Connection timed out after 25006 milliseconds`，HTTP000、bytes0；没有成功响应原件，不把curl失败覆写web默认成功。

CUA实际创建隐藏iab页失败：`Browser is not available: iab`；随后listBrowsers返回`[]`。没有UI筛选/checkbox操作，没有读UI，不借其他任务kernel reset/timeout当本次执行。

必要替代补检两查询各首轮即停，无分页：

- `site:research.google/pubs/ "November 30, 2025" ("language model" OR training OR transformer OR inference)`
- `site:research.google/pubs/ "2025-11-30" (multimodal OR agent OR diffusion OR evaluation)`

实际返回Empty search results。只表明这两索引查询未恢复线索，不证明官方本窗无论文。不能由678年数量、年排序、出版年、提交日或搜索参数推公开日。

当前恢复边界：撤销“默认pubs不可达”描述；目标日相关的历史切片/具名原件公开日期未恢复。可接受官方有日公开目录、正确筛选所得具名候选再核作者首次正文，或完全落窗的可证日期区间。只重开本日相关身份/主题，不扩678篇或其他日期。不授Coverage/Evidence/Books采用。
