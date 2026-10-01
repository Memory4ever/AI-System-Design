# GPT-6 prompt caching：定点证据笔记

状态：官方时间与工程说明已核；非作者独立复核判定为 `Version Fact / Existing Mechanism`，候选前关闭，不评分、不改 Books。若日后出现影响正确性或兼容性边界的新的原始证据，只重开该受影响项。

- 原始事件：[OpenAI, *Better prompt caching for GPT-6*](https://openai.com/index/better-prompt-caching-for-gpt-6/)；官方 RSS `https://openai.com/news/rss.xml` 的 `pubDate` 为 2026-09-22T21:00:00Z，即北京时间 09-23 05:00，落在本窗。需保留 RSS 原字段和文章页面的日级日期，不以 crawler 时间代替发布。
- 原始技术边界：[OpenAI Prompt caching guide](https://developers.openai.com/api/docs/guides/prompt-caching) 明示 GPT-5.6 起已有 explicit breakpoint、implicit/explicit mode、cache write 费用与可复用边界；[diagnostics guide](https://developers.openai.com/api/docs/guides/prompt-caching/diagnostics) 列出 `tools_changed` 等 miss reason。故不能把 explicit breakpoint 本身当作 GPT-6 首创机制。
- 本次发布披露的新组合：对 GPT-6 共享前缀使用默认缓存、提供命中率/输入构成 Dashboard、在 miss 时比较 model/tools/settings/input、并允许追加 `configuration_update` 改变 reasoning effort 而保留 request-level effort 和 prefix identity。产品页还建议稳定 tool definition/schema/order、通过 allowed tools 控制可调用集合而不改 cacheable prefix，以及可预热已知上下文。
- 系统意义：cache correctness identity 与 cache economics 必须分开；可复用的前缀未改变时，动态 suffix 不应无谓写入高成本 cache；引入诊断后，miss 可以归因到 token/工具配置变化而不是笼统归咎于模型服务。这里是作者公开的 API 行为和客户案例，不是独立证实的跨提供商通用收益。
- 与已有 Books 的复核：`AGENT-CONTEXT` Ch75 已有 prefix identity、tool-schema 抖动与 token reduction/reuse trade-off；`INFER-KV-CACHE` Ch45 已有 exact-prefix/stateful KV。本事件的 Dashboard/diagnostics 和 `configuration_update` 是厂商接口组合，未给出改变上述长期机制或设计判断的证据，因此候选前关闭，不为制造 diff 重述。
- 数字边界：产品页客户案例的命中率、成本下降和“up to”折扣只在其各自工作负载/计费/部署配置成立；未披露模型、输入输出长度、batch、并发、SLO、精度、硬件或独立 evaluator 的字段不得补造，本文不采用这些倍率作为性能结论。
