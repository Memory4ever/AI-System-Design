# 本日有限公开字段

实际HTTP请求时间2026-10-02T16:51:18Z起；当前原入口字段仅支持以下切片，不是全机构历史证明。

- OpenAI RSS https://openai.com/news/rss.xml HTTP200，1244 metadata；实际本窗邻接字段：Cerebras Wed,14Jan2026 14:00GMT；Zenken Tue,13Jan2026 16:00GMT；SB Energy Fri,09Jan2026 11:00GMT；Datadog Fri,09Jan2026 00:00GMT；Healthcare Thu,08Jan2026 12:00GMT；Netomi Thu,08Jan2026 00:00GMT。其间未见Jan12事件。一次feed，无后续feed分页；不保证已删除历史。
- Anthropic Research HTTP200，publishedOn174处，不是174候选。actual邻接fields：property-based-testing=2026-01-14T00:00:00.000Z，next-generation-constitutional-classifiers=2026-01-09T17:17:00.000Z，critical-infrastructure-defense=2026-01-08T00:00:00.000Z。Jan15两economic项晚于本窗。当前原嵌入切片无Jan12事件。
- Kimi releases https://api.github.com/repos/MoonshotAI/kimi-cli/releases?per_page=100&page=1 HTTP200，100条跨本窗；0.76 published_at=2026-01-12T13:11:16Z位于本窗，0.75=Jan9T14:47:53Z，0.74=Jan9T13:23:56Z在窗前。0.76 body：PR603 conditional description for read file；PR604 slash commands/help display；PR602 prevent TypeScript files misidentified as video；PR605 version bump。需读具体core决定准入，不能把release或fix标签当贡献。
- Zai Research HTTP200，actual title_zh/createAt：GLM-Image=2026-01-13T16:00:00.000Z（窗后），GLM4.7Flash=Jan19T16Z（窗后）。nav复用别名条目不另计。createAt不冒充论文首公开；单当前目录仍有历史限制。
- DeepSeek updates HTTP200，实际日期headings从Sep10/Aug21/Aug13/Jul31/Apr24_2026跳至Dec1_2025，之后Sep29/22、Aug21、May28等，不见Jan12条目；单页在跨窗邻接停止，不遍历所列旧模型正文。

arXiv API首次max25带summary的工具传输超预算截断，不声称全部读完，也不把latest summary当exact-v1。已改为四主题原批次max100只返回title/identity/日期；宽标题记录只作召回，相关潜在条目再读精确版本完整题摘。
