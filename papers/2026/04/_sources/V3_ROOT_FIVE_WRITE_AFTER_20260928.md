# 2026-09-28 五项 Books 实写后非作者复核

本记录仅确认已实写的五处机制正文及其相邻交接，不代表相应 04/20、04/24 两份 Daily 完成。复核者 root 并非这五处正文作者；逐项重新打开官方 v1 原文与实际章节，检查没有把受限论文效果外推为通用工程结论。原始 source→owner 独立采用意见另见两日审阅笔记。

| Source Family | 实际章节与机制位置 | 写后核验结论 |
| --- | --- | --- |
| `SF-2026-ARXIV-2604-21700` | Ch72 Backdoor Evaluation：trigger 邻域与 coalition 之间 | [v1](https://arxiv.org/html/2604.21700v1) III-C–E／IV：目标片段双条件损失与自然风格触发有据；正文保留 LoRA/隐藏配置写权限、benign FPR、反演 probe 局限及旧 smoke-test 的窄边界。PASS。 |
| `SF-2026-ARXIV-2604-20985` | Ch72 DP：post-processing 与 production contract 之间 | [v1](https://arxiv.org/html/2604.20985v1) §5–6：随机只发布一个候选、LC 保守 composition、更紧独立噪声分开；没有平均 epsilon 或把同 run checkpoint 视作独立，数据集与 utility 边界清楚。PASS。 |
| `SF-2026-ARXIV-2604-21590` | Ch27 synthetic data：generator/judge 同源盲点之后 | [v1](https://arxiv.org/html/2604.21590v1) §3.2–3.3：行为树支路反推环境、用户、SOP 三类输入与真实授权分责；同 Qwen 多次回答未冒充独立投票，mock 与现实、组件与综合飞轮分开。PASS。 |
| `SF-2026-ARXIV-2604-21275` | Ch27 manifest/cursor 与 batch 原子发布之间 | [v1](https://arxiv.org/html/2604.21275v1) §III-B／IV-B／V：独立队列、round-robin 和转换后缓存归于正常读取顺序，不扩大到故障重放、全训练 bitwise 或 LLM 吞吐；有序提交代价及旧共享/串行条件保留。PASS。 |
| `SF-2026-ARXIV-2604-15804` | Ch24 交错 text/speech 与 Self-revision 之间 | [v1](https://arxiv.org/html/2604.15804v1) §2.4–2.5／Table2：ARIA prefix-rate、单流状态与未知全局比率受限；theoretical first packet 不是 tail SLO，也没有 ARIA 单独消融。固定 chunk/双轨旧方案与 Thinker→Talker handoff 均保留。PASS。 |

共同限定：PASS 为来源、owner、实际正文与相邻衔接的非作者复核；未复现实验，也未替代日期窗口、候选分母、普通待办或最终日级 Gate。路径级 `git diff --check` 在本记录写后执行。
