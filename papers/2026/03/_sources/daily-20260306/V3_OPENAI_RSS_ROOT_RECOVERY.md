# OpenAI 官方 RSS 日期定点恢复

mar02_v3 于2026-10-01直接GET [官方RSS](https://openai.com/news/rss.xml)，HTTP200，当前约754928字节。此入口在官方Blog页底RSS链接可见，不是第三方聚合器；pubDate字段按其明确GMT转换，不把原网页day-only补为09:00。

按root请求只恢复有限原字段供03/01～04作者/非作者对窗；本文件放在当前03/06工作目录，不修改其他日报，不评分/审阅这些恢复项，也不把feed全量变成候选队列。pubDate是官方feed给出的发布字段，不独立认证网页从未更早公开；采用主张应结合原文/项目发布并由对应日级独立复核。

## 恢复范围

提取区间为[2026-02-28T01:00Z,2026-03-05T01:00Z)，即BJT[02/28 09:00,03/05 09:00)。其中03/01～04默认Daily的联合窗口是BJT[02/28 09:00,03/04 09:00)；剩余03/04 09～03/05 09段仅为03/04日历日期的邻接定位，不属于前四份Daily，不据此扩展它们窗口。

此有限提取共10项：

| 原始身份 | pubDate原值 | 北京时间 | 默认Daily时间归属（只按feed字段） |
| --- | --- | --- | --- |
| [VfL Wolfsburg turns ChatGPT into a club-wide capability](https://openai.com/index/vfl-wolfsburg) | Thu, 05 Mar 2026 00:00:00 GMT | 2026-03-05T08:00:00.000+08:00 | 03/05（不属于03/01～04联合窗） |
| [Introducing ChatGPT for Excel and new financial data integrations](https://openai.com/index/chatgpt-for-excel) | Thu, 05 Mar 2026 00:00:00 GMT | 2026-03-05T08:00:00.000+08:00 | 03/05（不属于03/01～04联合窗） |
| [Introducing the Adoption news channel](https://openai.com/index/introducing-the-adoption-news-channel) | Thu, 05 Mar 2026 00:00:00 GMT | 2026-03-05T08:00:00.000+08:00 | 03/05（不属于03/01～04联合窗） |
| [The five AI value models driving business reinvention](https://openai.com/index/the-five-ai-value-models-driving-business-reinvention) | Thu, 05 Mar 2026 00:00:00 GMT | 2026-03-05T08:00:00.000+08:00 | 03/05（不属于03/01～04联合窗） |
| [Extending single-minus amplitudes to gravitons](https://openai.com/index/extending-single-minus-amplitudes-to-gravitons) | Wed, 04 Mar 2026 10:00:00 GMT | 2026-03-04T18:00:00.000+08:00 | 03/05（不属于03/01～04联合窗） |
| [How Axios uses AI to help deliver high-impact local journalism ](https://openai.com/index/axios-allison-murphy) | Wed, 04 Mar 2026 00:00:00 GMT | 2026-03-04T08:00:00.000+08:00 | 03/04 |
| [Understanding AI and learning outcomes](https://openai.com/index/understanding-ai-and-learning-outcomes) | Wed, 04 Mar 2026 00:00:00 GMT | 2026-03-04T08:00:00.000+08:00 | 03/04 |
| [GPT-5.3 Instant: Smoother, more useful everyday conversations](https://openai.com/index/gpt-5-3-instant) | Tue, 03 Mar 2026 10:00:00 GMT | 2026-03-03T18:00:00.000+08:00 | 03/04 |
| [GPT-5.3 Instant System Card](https://openai.com/index/gpt-5-3-instant-system-card) | Tue, 03 Mar 2026 10:00:00 GMT | 2026-03-03T18:00:00.000+08:00 | 03/04 |
| [Our agreement with the Department of War](https://openai.com/index/our-agreement-with-the-department-of-war) | Sat, 28 Feb 2026 12:30:00 GMT | 2026-02-28T20:30:00.000+08:00 | 03/01 |

本次有限提取中03/01默认窗有Our agreement一项；03/02与03/03默认窗没有item；03/04默认窗有GPT5.3 Instant与card、Axios、AI学习结果四项。不能用这一结果声明所有未列出的OpenAI历史材料不存在。root只定点重开相应源/身份，不扩大为全部事件审阅或跨日全文队列。

## 原始提取值

```json
[
  {
    "title": "VfL Wolfsburg turns ChatGPT into a club-wide capability",
    "link": "https://openai.com/index/vfl-wolfsburg",
    "pubDate": "Thu, 05 Mar 2026 00:00:00 GMT",
    "UTC": "2026-03-05T00:00:00.000Z",
    "BJT": "2026-03-05T08:00:00.000+08:00"
  },
  {
    "title": "Introducing ChatGPT for Excel and new financial data integrations",
    "link": "https://openai.com/index/chatgpt-for-excel",
    "pubDate": "Thu, 05 Mar 2026 00:00:00 GMT",
    "UTC": "2026-03-05T00:00:00.000Z",
    "BJT": "2026-03-05T08:00:00.000+08:00"
  },
  {
    "title": "Introducing the Adoption news channel",
    "link": "https://openai.com/index/introducing-the-adoption-news-channel",
    "pubDate": "Thu, 05 Mar 2026 00:00:00 GMT",
    "UTC": "2026-03-05T00:00:00.000Z",
    "BJT": "2026-03-05T08:00:00.000+08:00"
  },
  {
    "title": "The five AI value models driving business reinvention",
    "link": "https://openai.com/index/the-five-ai-value-models-driving-business-reinvention",
    "pubDate": "Thu, 05 Mar 2026 00:00:00 GMT",
    "UTC": "2026-03-05T00:00:00.000Z",
    "BJT": "2026-03-05T08:00:00.000+08:00"
  },
  {
    "title": "Extending single-minus amplitudes to gravitons",
    "link": "https://openai.com/index/extending-single-minus-amplitudes-to-gravitons",
    "pubDate": "Wed, 04 Mar 2026 10:00:00 GMT",
    "UTC": "2026-03-04T10:00:00.000Z",
    "BJT": "2026-03-04T18:00:00.000+08:00"
  },
  {
    "title": "How Axios uses AI to help deliver high-impact local journalism ",
    "link": "https://openai.com/index/axios-allison-murphy",
    "pubDate": "Wed, 04 Mar 2026 00:00:00 GMT",
    "UTC": "2026-03-04T00:00:00.000Z",
    "BJT": "2026-03-04T08:00:00.000+08:00"
  },
  {
    "title": "Understanding AI and learning outcomes",
    "link": "https://openai.com/index/understanding-ai-and-learning-outcomes",
    "pubDate": "Wed, 04 Mar 2026 00:00:00 GMT",
    "UTC": "2026-03-04T00:00:00.000Z",
    "BJT": "2026-03-04T08:00:00.000+08:00"
  },
  {
    "title": "GPT-5.3 Instant: Smoother, more useful everyday conversations",
    "link": "https://openai.com/index/gpt-5-3-instant",
    "pubDate": "Tue, 03 Mar 2026 10:00:00 GMT",
    "UTC": "2026-03-03T10:00:00.000Z",
    "BJT": "2026-03-03T18:00:00.000+08:00"
  },
  {
    "title": "GPT-5.3 Instant System Card",
    "link": "https://openai.com/index/gpt-5-3-instant-system-card",
    "pubDate": "Tue, 03 Mar 2026 10:00:00 GMT",
    "UTC": "2026-03-03T10:00:00.000Z",
    "BJT": "2026-03-03T18:00:00.000+08:00"
  },
  {
    "title": "Our agreement with the Department of War",
    "link": "https://openai.com/index/our-agreement-with-the-department-of-war",
    "pubDate": "Sat, 28 Feb 2026 12:30:00 GMT",
    "UTC": "2026-02-28T12:30:00.000Z",
    "BJT": "2026-02-28T20:30:00.000+08:00"
  }
]
```
