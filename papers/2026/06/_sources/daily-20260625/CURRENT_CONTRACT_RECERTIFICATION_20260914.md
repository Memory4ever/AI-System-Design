# 2026-06-25 当前合同再认证（2026-09-14）

- **窗口：** 2026-06-24T09:00:00+08:00 ～ 2026-06-25T09:00:00+08:00
- **范围：** 当前 Daily 清单的 13 个机构源 + SRC-ARXIV。
- **验收结论：** 来源定点补查完成；新增候选 1，新增 Books 写入 0；/root 非作者独立复核提出的日期与候选准入修正已落实。

## arXiv 证据复用

现有 canonical raw inventory、全量题摘账本、V3 admission audit、exact-v1 evidence 与 Books queue 的 identity/version 仍一致，按研究合同 §7 复用，不机械重读。

当前 arXiv owner inventory 为 526 个 identity；机构源新增 1 个独立 Source Family，冻结候选由 27 调整为 28。withdrawal、first-public owner、题摘准入、Evidence 与 Books 定位沿用已匹配的 V3 审计；本轮没有发现 arXiv 版本或身份变化。

## 机构来源定点补查

| 来源 | 实际检查与窗口结论 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 Research 可见时间序列并配合窗口定点检索；本窗未发现范围内新增的大模型/Infra 原始研究。 | 已检查 | 无 |
| SRC-ANTHROPIC | 官方 Research 时间序列按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-GOOGLE-AI | Introducing computer use in Gemini 3.5 Flash 的 datePublished=2026-06-24T16:00:00Z 落入本窗；正文披露 targeted adversarial training、敏感/不可逆动作显式确认和间接 prompt injection 自动停止，改变 Agent action/security release contract，重开为候选。 | 已检查 | 无 |
| SRC-META-AI | 官方 Research 时间序列按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-QWEN | 官方博客时间序列按窗口检查；本窗未发现新的 Source Family 或重要 revision。 | 已检查 | 无 |
| SRC-DEEPSEEK | 官方 V4 / V4 Preview 页面与 API changelog 的首次发布为 2026-04-24；不属于本窗，本窗无新增。 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Platform Blog 与 MoonshotAI 官方仓库发布时序按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 官方 Research 的 publicList 接口分页一次取全（totalNum=8），按展示首发日期检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-ZAI | 官方 Research 时间序列在 2026-06-16 与 2026-05 条目之间形成窗口边界；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 官方 Research、论文目录与发布页按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | ERNIE 官方技术博客与仓库发布时序按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | MiMo Paper/Blog 官方时间序列与仓库按窗口检查；本窗未发现范围内新增。 | 已检查 | 无 |
| SRC-MINIMAX | 中英文官方博客与 Agent Tech Blog 时间序列按窗口检查；相邻可见条目为 06-09/06-01，本窗未发现范围内新增。 | 已检查 | 无 |

## 分母与 Books 影响

- **SRC-GOOGLE-AI：** Introducing computer use in Gemini 3.5 Flash 的 datePublished=2026-06-24T16:00:00Z 落入本窗；独立复核指出其三项公开安全控制改变 Agent action/security release contract，故作为独立 Source Family 纳入分母并完成深审。按当前命题重评为 `2 + 2 + 2 = 6`：公开控制跨越模型传感与 action authority，但未披露算法、阈值或独立安全保证，不能按跨生命周期基础认知计分。
- **SRC-DEEPSEEK：** 作者侧曾把页面线索误读为 2026-06-24；独立复核以官方 V4 / V4 Preview 页面与 API changelog 纠正为 2026-04-24。该事件不属于本窗，不参与本窗分母。

Gemini 条目形成 1 个新的 Candidate Denominator 成员；DeepSeek 页面不属于本窗。Google 官方正文只证明发布方公开的 capability/safeguard：没有披露 adversarial-training 算法或数据、检测阈值、误报/漏报、攻击覆盖及独立评测，不能外推为开放环境安全保证。对照 `PLATFORM-SECURITY` 与 `AGENT-TOOL-CALLING` 后，现有正文已覆盖“model sensor 不拥有 authority、敏感/不可逆动作显式 approval、间接注入触发 fail-closed/sandbox”的长期命题，Books 为 `No Change — Existing Coverage`。

## 作者侧验收

- 固定北京时间窗口：通过。
- 到期每日来源：14/14 已处理。
- 候选身份、exact-v1、撤回、Evidence、Books 复用条件：通过。
- 新增候选：1；新增 Books 写入：0。
- 非作者独立复核：/root 已检查来源/日期/准入、候选与 Books 队列；其修正意见已全部落实。
