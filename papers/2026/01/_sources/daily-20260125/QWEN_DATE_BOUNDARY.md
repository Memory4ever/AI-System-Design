# Qwen necessary date recovery — 2026-01-25

检查：2026-10-04T08:54:00+08:00。原源：[Pushing Qwen3-Max-Thinking Beyond its Limits](https://qwen.ai/blog?id=qwen3-max-thinking)。搜索缓存显示 `2026/01/25`，没有时区，不能作为本窗时间。

官网 HTML 是 SPA；实际读其 `https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_blog-index.js` 与 `p_blog-useblog.hook.js`，恢复页面自己使用的 GET 路径、code、language/path/type 参数。没有把私人 git_url 当作可用证据。

实际原源 [article API](https://qwen.ai/api/v2/article/?language=en-US&path=qwen3-max-thinking&type=qwen_ai) 返回：

```text
id: 1ff49275-d588-4f5a-8458-ee3886552fc3
title: Pushing Qwen3-Max-Thinking Beyond its Limits
path: qwen3-max-thinking
language: en-US
extra.date: 2026-01-26T04:00:00+08:00
extra.author: QwenTeam
extra.wordCount: 603
content JSON-LD datePublished: 2026-01-23T04:00:00+08:00
content JSON-LD dateModified: 2026-01-23T04:00:00+08:00
content JSON-LD wordCount: 807
```

实际 [retrieval API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 返回 `data.articles` 40 项，未含分页字段。只对 date metadata 排序，窗口邻接记录是：

```text
2026-01-22T00:00:04+08:00 qwen3tts-0115
2026-01-26T04:00:00+08:00 qwen3-max-thinking
2026-01-29T00:00:04+08:00 qwen3asr
```

停止：原源列表时间已跨过本窗；没有把 40 项变成题摘或全文队列。page_config 恢复的旧 research-list 只到 2025 年，不授历史覆盖；遗漏 code 的请求 500、猜测路径 `/api/v2/article/qwen3-max-thinking` 与旧 docs index 404 均只算失败尝试。

完整核心说明已读：工具使用与经验累计 test-time scaling 是有意义的待验证信号。对 heavy 模式，不单纯增大并行轨迹数，而限制并行数、将预算转向多轮反思，并以 take-experience 摘取历史认识减少重复推导；原文声称在相近 token 消耗下有收益。这可能改变 `AGENT-REFLECTION` / `AGENT-CONTEXT` 的预算与历史表示取舍，不能以“已有主题”拒绝。

但列表/正文的时间及字数元数据不一致。两条带时区原值都在本窗外，搜索缓存的相交日期又不具精确时间权限；当前不能确定首公开正文是否在本窗，更不能把任一字段授为精确首次公开。作为本窗终态日期保留项，不评分、不采用性能数字、不进 Books、不支撑覆盖完整性。重开只需该材料官方原始公告时间、明确版本/修订说明或可信公开存档，核其是否完全落在本窗；若窗外，只路由其真实归属日，不重扫本日或全月。
