# 2026-06-01～10 每日厂商源再认证

本文件只修复旧报告把历史期已存在的每日源误写成“不适用”的口径。检查范围为
`2026-05-31T09:00:00+08:00`～`2026-06-10T09:00:00+08:00`；每个事件仍按各日报的
09:00 截点归属。arXiv 的逐项身份、语义筛选、撤回和 exact-v1 证据继续使用各日报已有记录，
没有因本次来源修复而从零重跑。

## 来源结论

| 来源 | 实际检查入口 | 窗内事件及处置 |
| --- | --- | --- |
| `SRC-OPENAI` | [Research](https://openai.com/research/) 与官方发布页 | 06-02 Codex 产品说明缺少可改变长期机制的公开细节，关闭；06-03 GPT-Rosalind 属暂缓的 AI for Science，关闭；[Dreaming](https://openai.com/index/chatgpt-memory-dreaming/) 只披露 `2026-06-04` 日期，无法在 09:00 截点下唯一分配给 06-04 或 06-05，隔离为日期缺口，但其机制已由 `AGENT-MEMORY` 正文承载；06-08 经济研究项目不改变当前 AI System 设计，关闭。 |
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research) | 06-05 “Making Claude a chemist” 属暂缓的 AI for Science；没有发现其他需要进入本段候选分母的事件。 |
| `SRC-GOOGLE-AI` | [DeepMind publications](https://deepmind.google/research/publications/) 与 Google Research | 06-04 的合作/超智能讨论没有披露可落到训练、推理、平台或 Agent 运行时的机制，关闭；没有发现其他需保留事件。 |
| `SRC-META-AI` | [Research publications](https://ai.meta.com/research/publications/) | 06-05 发布的 [SIRA 页面](https://ai.meta.com/research/publications/superintelligent-retrieval-agent-the-next-frontier-of-agentic-retrieval/) 指向 `arXiv:2605.06647`；该家族 v1 已于 05-07 首次公开，v2 没有解决本批日报的已知未决问题，按非重要修订去重，不重复评分。 |
| `SRC-QWEN` | [Qwen](https://qwenlm.github.io/) 与官方仓库 | 没有发现本段窗口内需要进入候选分母的模型、机制或系统事件。 |
| `SRC-DEEPSEEK` | [DeepSeek](https://www.deepseek.com/) 与官方仓库 | 没有发现本段窗口内需要进入候选分母的模型、机制或系统事件。 |
| `SRC-MOONSHOT` | [Kimi Platform Blog](https://platform.kimi.com/blog) 与 [kimi-code releases](https://github.com/MoonshotAI/kimi-code/releases) | GitHub `published_at` 给出精确时刻：0.7.0/0.8.0 归 06-03；0.9.0 归 06-04；0.10.0/0.10.1 归 06-05；0.11.0 归 06-06；0.12.0/0.12.1 归 06-10。逐日只保留改变 Agent state/control contract 的 release family，其余补丁在相同版本事件内关闭。 |
| `SRC-TENCENT-HUNYUAN` | [Research “全部”列表](https://hunyuan.tencent.com/research) 与官方仓库 | 列表在 05-21 后直接到 07-06；没有 06-01～10 的研究条目。 |
| `SRC-ZAI` | [官方 Research](https://www.zhipuai.cn/zh/research) 与官方仓库 | 列表在 05-20 后直接到 06-16；没有本段窗口研究条目。 |
| `SRC-BYTEDANCE-SEED` | [Research](https://seed.bytedance.com/en/research)、[论文目录](https://seed.bytedance.com/en/public_papers) 与官方仓库 | 没有发现本段窗口内需要进入候选分母的事件。 |
| `SRC-BAIDU-ERNIE` | [ERNIE 技术博客](https://ernie.baidu.com/blog/zh/) 与官方仓库 | 可见列表在 05-09 后进入更早条目；没有 06-01～10 的研究条目。 |
| `SRC-XIAOMI-MIMO` | [MiMo](https://mimo.xiaomi.com/) 与官方仓库 | 没有发现本段窗口内需要进入候选分母的官方研究或 release 事件；用户 issue 不属于官方研究发布。 |
| `SRC-MINIMAX` | [Research / Blog](https://www.minimax.io/blog) | [MiniMax M3](https://www.minimax.io/blog/minimax-m3) 的 JSON-LD `datePublished=2026-05-31T17:31:18Z`，即 06-01 01:31:18+08，归 06-01；[MaxProof](https://www.minimax.io/blog/minimax-maxproof-math-proof-evolution) 的 JSON-LD `datePublished=2026-06-09T13:43:00Z`，即 06-09 21:43:00+08，归 06-10。 |

## Kimi Code 版本事件

| owner Daily | tag 与 `published_at` | 候选判断 |
| --- | --- | --- |
| 06-03 | `0.7.0` — `2026-06-02T02:23:53Z`; `0.8.0` — `2026-06-02T14:56:13Z` | goal mode、background question、approval lifecycle 与 compaction todo 改变长期 Agent run 的状态/控制接口，标准审阅；Books 已有覆盖。 |
| 06-04 | `0.9.0` — `2026-06-03T14:01:42Z` | ACP adapter 与不改变主 turn 的 side-channel 属 Agent protocol/runtime 边界，标准审阅；Books 已有覆盖。 |
| 06-05 | `0.10.0` — `2026-06-04T13:46:30Z`; `0.10.1` — `2026-06-04T17:35:34Z` | goal queue 与 config reload 改变 durable workflow/config state；crash patch 不单独计分；Books 已有覆盖。 |
| 06-06 | `0.11.0` — `2026-06-05T10:26:45Z` | 层级 sub-skill discovery 与固定 30 分钟 subagent timeout 改变 capability discovery 与 delegation budget；Books 已有覆盖。 |
| 06-10 | `0.12.0` — `2026-06-09T03:56:11Z`; `0.12.1` — `2026-06-09T09:04:14Z` | micro-compaction、goal/background/sub-skill 默认启用与 `/swarm` 改变 context、workflow 与 multi-agent control；补丁并入同一事件；Books 已有覆盖。 |

## 证据边界

- GitHub release 证明公开版本、时刻和 release note 中声明的接口变化，不证明生产可靠性、跨模型收益或内部未公开实现。
- 厂商 Blog 可证明公开架构说明和作者实验，benchmark 只在其披露的模型、脚手架、硬件与 evaluator 条件下成立。
- 目录未命中只支持“本次实际入口没有发现相关事件”，不支持开放世界绝无遗漏。
- Dreaming 缺精确发布时刻，不用于任一日报的确定候选数量、评分或完成性断言；未来取得原始时刻时只重开 06-04/05 的该家族。
