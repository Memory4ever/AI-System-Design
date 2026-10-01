# Daily 2026-09-20 screening ledger

## 口径与窗口

- 窗口：`[2026-09-19T09:00:00+08:00, 2026-09-20T09:00:00+08:00)`。
- 检查时间：`2026-09-21T10:18:00+08:00`。
- Daily 检查 `docs/RESEARCH_SOURCES.md` 列明的 14 个每日来源；Tencent-Hunyuan GitHub 是 `SRC-TENCENT-HUNYUAN` 的官方补充入口，不存在 UniRL 仅归 Weekly 的合同边界。
- 仓库不按普通 commit 数量扩 raw denominator；但明确改变 correctness、security、interface contract 或 runtime architecture 的官方事件须逐项完成贡献判断。
- 本窗没有 arXiv new/cross identity；无摘要的工程事件读取完整 commit message、核心 diff 与变更理由。

## 漏斗闭包

| 层级 | 数量 | 说明 |
| --- | ---: | --- |
| raw identity | 5 | MiMo-Code 3 个、UniRL 2 个官方主干 commit |
| 唯一 Source Family | 5 | 五项逻辑变更不共享同一问题/修订链 |
| 通过贡献筛选 | 2 | UniRL SGLang 配置契约与 vLLM TP 权重发布 |
| 已关闭 | 3 | 三个 MiMo family 均完成身份、日期、核心说明与关闭判断 |
| 已撤回/删除 | 0 | 精确官方 commit 页面可用，所查 main 历史未见对应 revert/withdrawal |
| Evidence 完成 | 2 | 两个 UniRL family 均完成深入审阅 |
| Books 写回 queue | 2 | `INFER-SGLANG`、`TRAIN-DISTRIBUTED-TRAINING` |

撤回数只表示所查官方 commit/main 历史未见信号，不证明未来不会撤回；后续 revert 应作为新事件重开受影响 family。

## Raw identities 与 family 归并

| Identity | 官方时间字段 | 北京时间 | Family | 处置 |
| --- | --- | --- | --- | --- |
| `Tencent-Hunyuan/UniRL@07ac948a5d70a1a08777920fd191390fc0556ac2` | commit `Date: Sun, 20 Sep 2026 01:27:56 +0800` | 2026-09-20T01:27:56+08:00 | SGLang dropped ServerArgs contract | 候选，深入完成 |
| `Tencent-Hunyuan/UniRL@a77575acaaf3ed54386b866747dda2a22d5b6b0c` | commit `Date: Sun, 20 Sep 2026 02:03:00 +0800` | 2026-09-20T02:03:00+08:00 | direct vLLM TP rollout / native IPC sync | 候选，深入完成 |
| `XiaomiMiMo/MiMo-Code@b6dbd25818c168ed152bd4d11e7f1ff0fe40d180` | Atom `2026-09-19T18:57:29Z` | 2026-09-20T02:57:29+08:00 | MCP connection lifetime | 关闭 |
| `XiaomiMiMo/MiMo-Code@895ae523309d0454e022f01c894c844094bc7cf1` | Atom `2026-09-19T21:05:24Z` | 2026-09-20T05:05:24+08:00 | session orphan reclaim | 关闭 |
| `XiaomiMiMo/MiMo-Code@4768aab0d0b5056e51b82801935cfce018be148a` | Atom `2026-09-20T00:35:18Z`；commit `committedDate=2026-09-20T08:35:18+08:00` | 2026-09-20T08:35:18+08:00 | failure persistence | 关闭 |

`b6dbd25` 与 `895ae52` 分属 MCP host connection 和 session/actor orphan state，只有宽泛 lifecycle 原则相似，没有共同问题、修订链或同一设计事件，故不能为了压缩数量归并。`7b14718946f540c24c754d17d3e4b337714d87fa` 的 lost-wake 修复作为 `895ae52` 的同一 session/actor lifecycle 支持活动记录，不另建候选；`c17d021`、`6e920fa` 是品牌/默认 prompt residual，未显示长期机制增量，不进入 raw denominator。

## 来源覆盖与停止点

| 来源 | 实际检查入口/停止点 | raw | 结果 |
| --- | --- | ---: | --- |
| SRC-OPENAI | Research 官方目录最新项 | 0 | 最近相关项早于窗口 |
| SRC-ANTHROPIC | Research 官方目录，最新可见 09-17 | 0 | 早于窗口 |
| SRC-GOOGLE-AI | DeepMind Research 与 Google Research publications 最新项 | 0 | 无当窗研究/系统发布 |
| SRC-META-AI | Meta AI/FAIR Research 最新项 | 0 | 无当窗研究发布 |
| SRC-QWEN | Qwen 官方站与合同列明的官方研究/发布入口 | 0 | 无当窗贡献事件 |
| SRC-DEEPSEEK | 官方 Research/News 最新项 | 0 | 最近相关变更早于窗口 |
| SRC-MOONSHOT | Kimi Blog 与合同列明的官方研究/发布入口 | 0 | 无当窗贡献事件 |
| SRC-TENCENT-HUNYUAN | Hunyuan Research 与 Tencent-Hunyuan GitHub；UniRL main 的当窗 contract-level 事件 | 2 | 两项通过贡献筛选并深入完成 |
| SRC-ZAI | Research、release notes 与官方研究/发布入口 | 0 | 无当窗事件 |
| SRC-BYTEDANCE-SEED | Research、public papers 与官方发布入口 | 0 | 无当窗事件 |
| SRC-BAIDU-ERNIE | 技术博客与官方研究/发布入口 | 0 | 无当窗事件 |
| SRC-XIAOMI-MIMO | Paper/Blog；MiMo-Code main Atom feed 到窗口起点前 | 3 | 三个独立 family，语义筛选后关闭 |
| SRC-MINIMAX | 中英文 Blog、Agent Tech Blog 与官方发布入口 | 0 | 最新技术文章早于窗口 |
| SRC-ARXIV | 十二目标分类 official new/cross announcement cadence | 0 | Friday batch 09-19 08:00+08 早于窗口；周五、周六无新 batch |

## 语义筛选结论

### UniRL SGLang dropped-argument contract

`07ac948` 的完整 message 和核心 diff 显示：adapter 从目标版本 live `ServerArgs` 计算允许集合，把 UniRL 自有 metadata 与真正 unknown keys 分开；unknown keys 默认 warning，严格环境变量开启时抛错。它改变 framework→engine 配置契约的保护行为，能阻止 typo/version skew 被静默过滤后继续运行，属于明确 correctness/interface-contract 纠错，进入候选并深入审阅。

### UniRL direct vLLM TP rollout / native IPC sync

`a77575a` 的完整 message、PR #480 与核心 diff显示：加入 direct vLLM 0.27 rollout process、FSDP canonical full-tensor export、receiver-native TP slicing/fusion、CUDA IPC device mapping、publication manifest/receipt/rank consensus，以及 partial in-place load 后 poison/fail-stop。它新增跨训练/推理布局的权重发布机制与失败边界，进入候选并深入审阅。

### MiMo MCP connection lifetime

`b6dbd25` 为 MCP host connection 加入 config snapshot binding、请求/turn settle 后释放 retired connection、失败 fallback 可重试及 OAuth probe/子进程清理。它实现 owner revision、reference drain 与 stale-attempt isolation，但没有新 protocol、替代设计或会改变选型的证据，故关闭。

### MiMo session orphan reclaim

`895ae52` 对 orphan question part 做 age gate、busy/retry/live actor guard、directory-scoped transactional re-check 后再 settle。它实现 lease/age boundary、live-owner re-check、作用域与原子写入；`7b147189` 提供同一路径的 lost-wake 支持修复。两者没有新增长期协议或评价边界，故关闭。

### MiMo failure persistence

`4768aab` 将 SDK execution exception 在写入 session history 前经统一 `errorMessage` 提取并截断，并增加长异常持久化回归测试。它避免异常无限放大 durable state/context，但没有提出新边界计算、资源模型、攻击证据或跨实现评价；外部错误进入 durable state 前必须 bounded 已是通用不变量，故关闭。
