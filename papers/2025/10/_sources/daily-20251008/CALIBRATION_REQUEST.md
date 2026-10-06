# 2025-10-08 首批准入校准请求

作者：本日独占作者。本文件保留原请求，Peirce已提供[FIRST结果](FIRST_INDEPENDENT_REVIEW.md)；最新采用边界见[作者停点](AUTHOR_CLOSEOUT.md)，以下拟定理由不是最终Evidence或Books验收。

窗口：2025-10-07T09:00:00+08:00 ～ 2025-10-08T09:00:00+08:00。

1. [Gemini 2.5 Computer Use](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)：原件 `gemini_release.html` 的 JSON-LD `datePublished=2025-10-07T19:00:00+00:00`，北京时间 10-08 03:00，落窗。官方 core 的 screenshot/action loop 本身非新增原则；值得继续的是每一步模型外 safety service 对建议动作执行前判定及其确认/拒绝契约。原有工具安全依赖模型输出与执行器权限 → 本次公开模型外逐动作检查接口及剩余注入风险 → 需区分动作提议、检查与执行，核其可靠性边界。拟 2+2+2=6，安全约束深入受影响 core；owner `PLATFORM-SECURITY`，邻接 `AGENT-TOOL-CALLING`。性能宣传不能替代可比评价。
2. [Disrupting malicious uses of AI: October 2025](https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/)：官方 RSS `Tue, 07 Oct 2025 03:00:00 GMT`，北京时间 10-07 11:00，落窗。发布 core 给出 AI 叠加既有攻击流程、未观察到新攻击能力的季度案例。拟先核原报告是否有可修正工具安全/滥用能力评价的具体证据；不能以“又一批案例”直接准入，也不能以安全题目直接高分。拟定点读相关 cyber 案例后裁决，尚不冻结为贡献候选。
3. 代表性日期排除：[VecInfer 2510.06175](https://arxiv.org/abs/2510.06175) 的搜索摘要支持潜在 KV 量化增量，但 `Tue Oct 7 17:35:28 2025` 是 submitted 线索，不是 first-public；当前官方公开列表恢复失败，不能先放候选表。
4. 代表性窗外排除：ERNIE 官方博客页2中 PLAS 是 2025-09-12，PaddleOCR-VL 是 2025-10-16；没有本窗事件，不读正文、不评分、不继承其它 Daily 处置。

来源边界：14 daily 源；Google pubs 独立检查、不以 Blog 替代；arXiv 查询发生日期筛选失效，未将返回的宽库存变为题摘队列；尚有 source recovery 普通待办。

原请求已获Peirce FIRST反馈，按其具体边界修订日报，不把此请求旧文当最新结论。来源普通恢复已处理，最终DAY仍待非作者。
