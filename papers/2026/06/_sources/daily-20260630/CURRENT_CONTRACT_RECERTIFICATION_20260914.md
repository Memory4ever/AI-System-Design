# 2026-06-30 当前合同再认证（2026-09-14）

- **窗口：** 2026-06-29T09:00:00+08:00 ～ 2026-06-30T09:00:00+08:00
- **范围：** 当前 Daily 清单的 13 个机构源 + SRC-ARXIV。
- **验收结论：** 来源定点补查完成；MOPD 从错误的候选前关闭中重开，新增候选 1，新增 Books 写入 0；/root 非作者独立复核意见已落实。

## arXiv 证据复用

现有 canonical raw inventory、全量题摘账本、V3 admission audit、exact-v1 evidence 与 Books queue 的 identity/version 仍一致，按研究合同 §7 复用，不机械重读。

当前 owner inventory 为 1132 个 identity，冻结候选由 54 调整为 55。withdrawal、first-public owner、其他题摘准入、Evidence 与 Books 定位沿用已匹配的 V3 审计；MOPD 的旧 closure 被本文件和更新后的全量语义账本显式取代。

## 机构来源定点补查

| 来源 | 实际检查与窗口结论 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 Research 可见时间序列并配合窗口定点检索；本窗未发现范围内新增的大模型/Infra 原始研究。 | 已检查 | 无 |
| SRC-ANTHROPIC | 官方 Research 时间序列按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-GOOGLE-AI | Google DeepMind 与 Google Research 官方发布索引按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-META-AI | 官方页列出 2026-06-29 的非侵入式脑信号句子解码研究；这是 BCI/神经科学垂直任务，没有可迁移的大模型系统机制，题摘语义关闭。仅有日期不影响该排除处置。 | 已检查 | 无 |
| SRC-QWEN | 官方博客时间序列按窗口检查；本窗未发现新的 Source Family 或重要 revision。 | 已检查 | 无 |
| SRC-DEEPSEEK | 官方 Research/发布索引按窗口检查；本窗未发现新的 Source Family 或重要 revision。 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Platform Blog 与 MoonshotAI 官方仓库发布时序按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 官方 Research 的 publicList 接口分页一次取全（totalNum=8），按展示首发日期检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-ZAI | 官方 Research 时间序列在 2026-06-16 与 2026-05 条目之间形成窗口边界；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 官方 Research、论文目录与发布页按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | ERNIE 官方技术博客与仓库发布时序按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 官网列出 MOPD；对应 arXiv:2606.30406v1 于 2026-06-29T14:51:28Z 首发。两者按同一 Source Family 去重，以 arXiv exact-v1 为 owner evidence；该机制改变 post-training 的 rollout/data/control ownership，已纳入候选。 | 已检查 | 无 |
| SRC-MINIMAX | 中英文官方博客与 Agent Tech Blog 时间序列按窗口检查；相邻可见条目为 06-09/06-01，本窗未发现范围内新增。 | 已检查 | 无 |

## 分母与 Books 影响

- **SRC-META-AI：** 官方页列出 2026-06-29 的非侵入式脑信号句子解码研究；这是 BCI/神经科学垂直任务，没有可迁移的大模型系统机制，题摘语义关闭。仅有日期不影响该排除处置。
- **SRC-XIAOMI-MIMO：** MOPD 以 arXiv:2606.30406v1 的 2026-06-29T14:51:28Z 为 first-public owner；MiMo 官网是同 family provenance。其 student-owned on-policy rollouts、domain-teacher services 与 capability-integration control flow 构成长周期训练系统贡献，旧 closure 无效。V2 评分为 `3 + 3 + 3 = 9`。

Meta BCI 条目仍在候选前关闭；MOPD 形成 1 个新的 Candidate Denominator 成员，并完成 exact-v1 Method、Evaluation、limitations/counterevidence 与 benchmark contract 审阅。对照 `TRAIN-GRPO` 后，正文已覆盖 student-owned on-policy rollout、teacher signal、outcome-verifier authority、teacher/student lineage 与 domain/support mismatch 的长期机制；多 teacher/domain routing 是该主线的受限实例，Books 为 `No Change — Existing Coverage`。

## 作者侧验收

- 固定北京时间窗口：通过。
- 到期每日来源：14/14 已处理。
- 候选身份、exact-v1、撤回、Evidence、Books 复用条件：通过。
- 新增候选：1；新增 Books 写入：0。
- 非作者独立复核：/root 已检查来源/日期/准入、候选与 Books 队列；其 MOPD 重开意见已落实。
