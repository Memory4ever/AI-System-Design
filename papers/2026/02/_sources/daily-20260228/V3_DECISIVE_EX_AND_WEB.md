# 02/28 一次决定性准入核与辅助原源

## 2602.22261 Sustainable LLM Inference using Context-Aware Model Switching — EX

HTML exact-v1返回404，转一次原PDF `https://arxiv.org/pdf/2602.22261v1`（本轮2026-10-05约23:12+08实际读§3–4，PDF14页，方法约p3–8、对照p8–9）。cache→lexicalrule→sentenceembeddingclassifier的fastpathfirst及用户调整threshold均是成熟routing组合；明确对照仅固定Qwen3 4B最大tier。150人工curated prompts/每类50、三个tiers1B/4B/4B；BERTScore参考是最大model回复而非独立正确性，NVML只GPU energy不计CPU。这些限制不作为“可信度低因此排除”，排除依据是必要core/对应对照没有新增可选条件、失效边界或纠正既有routing认识。67.5%/93.6%/本地部署不提供准入，停止全文/日期追踪。

## OpenAI Stateful Runtime — EX

原URL为 `https://openai.com/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/`，非少了environment的旧尝试URL。RSS原pubDate `Fri, 27 Feb 2026 05:30:00 GMT` =02/27 13:30+08落窗；本轮网页工具成功原HTML，2026-10-05约23:14+08，核心“workingcontext”涵盖memory/history、tool/workflowstate、environment与identity/permission，面向AWSnativepersistentorchestration。原文明确“willbeavailablesoon”，没有恢复/幂等/一致性协议、实现或对照；是已知statefulorchestration原则的服务预告，不因知名厂商/Agent标签自动入选，不授已GA或可用生产能力。

同RSS本窗其余三项联合声明/商业合作/融资为范围EX；mentalhealthupdate原pubDate00:00GMT=02/27 08:00+08在窗前，不挪到当日09:00。

辅助搜索原值：`site:openai.com/index "February 27, 2026"`、`site:anthropic.com "Feb 27, 2026"`、`site:research.google "February 27, 2026"`。搜索只定位原源、不作无遗漏证明。Anthropic当日warstatement是policy消息，不提供模型/Agent机制增量；research历史目录未恢复不得零命中。
