# 2026-09-22 Evidence Notes

## 当前进度

- 既有检查点候选：69；09-23 经原始 release 与 Books 论点复核，Qwen Code v0.24.3 候选前关闭，暂列 68 个 arXiv 事件。arXiv 原始分母仍待重建，不能称为最终冻结。
- exact-v1 HTML 已取得并定点阅读：25。
- arXiv HTML 本轮不可得：`2609.20831`、`2609.22048`；需转 exact-version PDF/abs。
- 尚需完成 Evidence Review 或 fallback recovery：43 个暂列 arXiv 事件；原数 44 含现已候选前关闭的 Qwen Code v0.24.3。
- 已完成并写回 Books：`2609.20830`、`2609.21058`、`2609.21079`。

本目录未保存上述 25 篇的 exact-v1 正文快照或逐篇 locator；“已取得并定点阅读”是旧检查点陈述，不代表本轮可直接验收。三项 Books 写入在现有章节可见，仍待 fresh non-author 复核。

已取得 exact-v1 的 25 项为：

```text
2609.20824 2609.20830 2609.20844 2609.20845 2609.21058
2609.21079 2609.21081 2609.21172 2609.21187 2609.21257
2609.21264 2609.21284 2609.21432 2609.21450 2609.21483
2609.21561 2609.21573 2609.21594 2609.21712 2609.21827
2609.21858 2609.21908 2609.22000 2609.22005 2609.22056
```

## 已闭合的三项证据

### arXiv:2609.20830v1 — Reviser

证据支持 cursor edit actions（插入、移动、停止）把 AR 的输出状态从 append-only sequence 改为 mutable canvas，并提供作者的小规模 continuation 实验。它不证明大模型质量、长文档 editing、真实 serving latency 或普遍优于 diffusion。采用命题已写入 Ch24。

### arXiv:2609.21058v1 — Kernel addressability

证据支持先以真实 model graph 的 wall-clock share 约束 kernel 搜索价值，并指出 KernelBench 绝对容差可接受近零/未完整写出的结果。采用范围绑定 A100-80GB、披露的软件栈、BF16、KernelBench L1 与作者七个 workload；不外推到其他 GPU、shape 或生产并发。采用命题已写入 Ch49。

### arXiv:2609.21079v1 — DLB

证据支持两层 router、P2P probing、online learned latency model 及流式/离散 routing 分支。22 个月部署与迁移数字只属于作者内部基础设施；不构成通用 SLO 保证。采用命题已写入 Ch56。

## 已读但 disposition 未最终闭合的重点

- `2609.21081`：approval 必须绑定 canonical operation 与 use-time state；Ch78/Ch72 可能已有精确覆盖，需给正文锚点。
- `2609.21172`：TierKV 的 predecode 分配与 low-rank/flash tier；需与 Ch45/Ch54 既有 tiering、prefetch 与 recoverable hierarchy 对读。
- `2609.21187`：next-turn metrics 与 workflow success 分离；Ch66 已有 gold-history/next-turn 路线，需核验是否仍有新边界。
- `2609.21284`：root-scoped authorization quiescence；Ch72 已有 effect-time authorization、revocation completion 与 delegation chain，需避免重复。
- `2609.21573`：多个局部合理文档的弱信号在 distributed RAG context 中累积；需判断 Ch72 现有单文档 poisoning 是否覆盖该 failure mode。
- `2609.21858`：exact multi-draft sampling 与无偏 watermark/provenance；需对读 Ch48 的 stochastic/exact speculation 主线。
- `2609.21908`：physical condition monitor 约束 stage commit；需对读 Ch26 的闭环、safety envelope 与 correction。
- `2609.22000`：与 09-21 RecreationWorld 属同一 family 的 paper evidence event，不得重复计分。
- `2609.22005`：attention abstention/noise filtering；需对读 Ch14 的 attention failure 边界。
- `2609.22056`：retrieval confidence/abstention；需对读 Ch76 与 Ch66 的 evidence/evaluation contract。

以上“已读”只表示已获取足以继续判断的正文证据；未列最终 disposition 的项目不能在日报中冒充完成。

## 09-23 定点恢复：重要修订与准入改判

### arXiv:2609.12748v2 — 纠错范围已读，窗口事件仍待核

已读[精确 v2 正文](https://arxiv.org/html/2609.12748v2) §3 的新增 wiki operator request log、§5.7 的 exposure 分析、§6 的撤回清单、§7 限制和 §8 评测设计。v2 加入约 515 万条 request log，能观察 page request，但没有 response body、harness messages 与真实 task outcome。§5.7 指出先前 70.5% 对 46.4% 的 marker adoption 关联把 own-page edit-form request 混入 exposure；排除此项后差异为 4.3 个百分点（95% 区间跨零），按时间分层后为 -1.6 个百分点；page selection、共享行为与 nameability 仍阻止因果识别。不能将“请求”升级为“成功读到并传播”，也不能把有限 progress trace 的零关联升级为总体无收益。旧 Ch84“长任务恢复依赖 Event Log”下已经写明缺少 read log 时不能推断传播、缺少 outcome 时不能推断协作效用，未见需撤销的正面因果断言。此处是正文内容与既有论点的局部对读，尚未核实 v2 replacement 的官方公告日是否完全落本窗，也未做独立证据/Books 复核，故暂不写最终 disposition。

### Qwen Code v0.24.3 — 候选前关闭

[官方 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.3) 显示 21 Sep 14:17 UTC（北京时间 22:17），Runtime and sessions 段披露 JDBC binding/session persistence 与 trusted-workspace channel restore；Review workflow 段披露 host-side lease evidence；Other Changes 列出 runtime bwrap 隔离和 Hosted Harness capability/boot fence。对照 Ch84 的 AgentRun/Workflow state、typed Session value 与“长任务恢复依赖 Event Log”，以及 Ch72 的 effect-time authorization / execution fence，这些是已有长期合同的版本实现和局部修复。release 没有说明新的可迁移机制、受控对照或会改变适用边界的结果。因此不评分、不继续 Books Gate；只保留版本事实，不声称代码/生产可靠性已验证。原文其余发布项未在本次定点审阅中逐条评价。
