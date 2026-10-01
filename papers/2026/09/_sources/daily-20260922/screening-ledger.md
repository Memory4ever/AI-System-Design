# 2026-09-22 Screening Ledger

窗口：`2026-09-21T09:00:00+08:00`（含）～`2026-09-22T09:00:00+08:00`（不含）。

## 旧检查点漏斗（待重建原始 arXiv 明细）

- 非 arXiv Daily 来源：13 个；3 个 raw family，0 个候选，3 个候选前关闭。Qwen Code v0.24.3 的改判见下文。
- arXiv：12 个目标分类；733 个去重身份，68 个候选，665 个候选前关闭。
- 合计：既有检查点记载 736 个 raw identity；本轮局部改判后为 68 个暂列候选、668 个候选前关闭。原始 733 身份及逐项排除理由没有保存在本目录，以上 arXiv 分母仍待从官方列表重建，不能当作已独立复核的闭环数字。
- arXiv 独立准入复核：68 / 733 retained；初筛 27 项 false positive 为 0，补回 false negative 41 项。

## 非 arXiv 事件

| Source Family | 时间 | 处置 | 理由 |
| --- | --- | --- | --- |
| [Qwen Code v0.24.3](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.3) | 2026-09-21T22:17:28+08:00（[GitHub API `published_at`](https://api.github.com/repos/QwenLM/qwen-code/releases/tags/v0.24.3) = `2026-09-21T14:17:28Z`） | 候选前关闭（09-23 复核改判） | 官方 release 的 JDBC binding/session persistence、trusted-workspace 频道启动恢复、host-side lease evidence、sandbox 路由及 Hosted Harness boot fence 是具体版本实现/修复。Ch84“AgentRun / Workflow state”“typed Session value”“长任务恢复依赖 Event Log”已承载状态持久化、恢复及副作用证据；Ch72 已承载 effect-time 授权与执行 fence。release 未披露新的通用机制、对照评价或足以改变适用边界的证据，不能因多个条目能映射多个章节就当作长期贡献。此判断只覆盖上述可能触发准入的条目，不宣称 release 其余每条已逐项评价。 |
| Kimi CLI 1.51.0 | 2026-09-22T00:02:35+08:00 | 候选前关闭 | 只披露归档与迁移事实，未公开新的模型、Agent 状态/控制、评价或长期机制 |
| MiniMax Code v0.5.1 | 2026-09-21T19:01:44+08:00 | 候选前关闭 | 只披露构建、checksum、安装与有限平台兼容性测试 |

动态或日期精度边界：Meta Research 目录、Hunyuan Research“全部”列表、Google Research publication index 与 MiMo 官网本轮不能稳定给出完整日级增量；这些限制不支持正面证据，也不被改写为“已证明无更新”。

## arXiv 关闭分类

其余 665 个身份按以下主因关闭：

1. 领域应用包装或当前暂缓的 AI for Science，没有新增可迁移的大模型/Infra 机制。
2. 经典 ML、控制、视觉或机器人局部方法，没有改变本项目主线的设计边界。
3. 新数据集、benchmark 或 library 只增加覆盖，没有暴露新的评价失效或 release gate。
4. 局部 gate/loss/adapter/fusion/prompt 改进只提供单任务 operating point，没有长期 Design Delta。
5. 257 个普通 replacement 没有机制、评价、纠错或安全变化信号；版本标签本身不进入候选。

`2609.12748` 是唯一明确的实质纠错 replacement：当前摘要撤回旧版 causal transmission 解释，但论文整体没有 withdrawn。其余完整 retained ID 清单见当日 README §3。

## 独立 false-negative 抽检

- 应用/AI for Science：18 项。
- 经典 ML/控制/视觉/机器人：20 项；恢复 `2609.21039`、`2609.21155`、`2609.21022`。
- Benchmark/evaluation：16 项；保留真正改变 evaluator contract 的工作。
- Infra 边缘：14 项；恢复 execution-plan、FSDP、kernel addressability 与 autoscaling/queueing 增量。
- Replacement：检查 correction/withdrawal/revision 语义；仅 `2609.12748` 进入候选。

此 ledger 只保存旧扫描的汇总与本轮定点纠偏；由于逐项原始列表和排除理由未留存，它本身不能证明发现面或准入分母完整，也不替代 Evidence Review 或 Books Gate。

## 09-23 续跑的可复核边界

本目录实际只有本 ledger、`evidence-notes.md` 与 `books-queue.md` 三份概括记录，没有 733 个 arXiv 身份的原始列表、十二分类查询/分页停止点、665 项逐项排除理由，也没有所谓 25 份 exact-v1 正文快照。既有“全量独立准入复核通过”叙述因此暂不能由留存材料重演；不能把本轮局部 Qwen 改判扩大成对剩余 68 项及所有排除项的重新验收。恢复时先从官方分类公告/列表和版本历史重建各事件身份、窗口及去重，再按研究合同 §3 对共享准入理由做双向校准与分层复核。
