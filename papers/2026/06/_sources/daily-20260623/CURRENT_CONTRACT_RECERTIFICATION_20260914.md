# 2026-06-23 当前合同再认证（2026-09-14）

- **窗口：** 2026-06-22T09:00:00+08:00 ～ 2026-06-23T09:00:00+08:00
- **范围：** 当前 Daily 清单的 13 个机构源 + SRC-ARXIV。
- **验收结论：** 来源定点补查完成；新增候选 0，新增 Books 队列 0；/root 非作者独立复核通过。

## arXiv 证据复用

现有 canonical raw inventory、全量题摘账本、V3 admission audit、exact-v1 evidence 与 Books queue 的 identity/version 仍一致，按研究合同 §7 复用，不机械重读。

当前 owner inventory 为 1556 个 identity，冻结候选为 50 个。withdrawal、first-public owner、题摘准入、Evidence 与 Books 定位沿用已匹配的 V3 审计；本轮没有发现版本或身份变化。

## 机构来源定点补查

| 来源 | 实际检查与窗口结论 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 Research 可见时间序列并配合窗口定点检索；本窗未发现范围内新增的大模型/Infra 原始研究。 | 已检查 | 无 |
| SRC-ANTHROPIC | 官方 Research 时间序列按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-GOOGLE-AI | 官方索引中 A24 research partnership 的 datePublished=2026-06-22T14:30:00Z 落入本窗；内容是创意合作公告，没有模型、训练、推理或平台机制，题摘/正文层面在候选前关闭。 | 已检查 | 无 |
| SRC-META-AI | 官方 Research 时间序列按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-QWEN | 官方博客时间序列按窗口检查；本窗未发现新的 Source Family 或重要 revision。 | 已检查 | 无 |
| SRC-DEEPSEEK | 官方 Research/发布索引按窗口检查；本窗未发现新的 Source Family 或重要 revision。 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Platform Blog 与 MoonshotAI 官方仓库发布时序按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 官方 Research 的 publicList 接口分页一次取全（totalNum=8），按展示首发日期检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-ZAI | 官方 Research 时间序列在 2026-06-16 与 2026-05 条目之间形成窗口边界；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 官方 Research、论文目录与发布页按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | ERNIE 官方技术博客与仓库发布时序按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | MiMo Paper/Blog 官方时间序列与仓库按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-MINIMAX | 中英文官方博客与 Agent Tech Blog 时间序列按窗口检查；相邻可见条目为 06-09/06-01，本窗未发现范围内新增。 | 已检查 | 无 |

## 分母与 Books 影响

- **SRC-GOOGLE-AI：** 官方索引中 A24 research partnership 的 datePublished=2026-06-22T14:30:00Z 落入本窗；内容是创意合作公告，没有模型、训练、推理或平台机制，题摘/正文层面在候选前关闭。

上述条目均未形成新的 Candidate Denominator 成员：排除项不用于正面证据，不评分、不进入 Books；重复项沿用真实 first-public owner 的既有处置。本轮没有需补写 Books 的 Source Family。

## 作者侧验收

- 固定北京时间窗口：通过。
- 到期每日来源：14/14 已处理。
- 候选身份、exact-v1、撤回、Evidence、Books 复用条件：通过。
- 新增可执行工作：0。
- 非作者独立复核：/root 已检查来源/日期/准入、候选与 Books 队列；结论通过。
