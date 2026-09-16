# Daily Research — 2026-05-23

**规范：** V3
**窗口：** 2026-05-22T09:00:00+08:00 ～ 2026-05-23T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-16T09:29:45+08:00

## 1. 结论

本次按当前 V3 合同重建，而不是继承旧 V2.1 的 `raw=0 / candidate=0 / Complete`。arXiv 官方发布节奏证明本窗没有公告批次：2026-05-21 20:00 EDT 的批次换算为北京时间 2026-05-22 08:00，早于窗口一小时；下一批按周末规则在 2026-05-24 20:00 EDT，晚于窗口。因此 arXiv raw 为 0，DataCite 字段不承担 first-public 时间语义。

日级机构源经 event-type prune 后冻结 6 个可证明本窗公开的唯一事件家族：`6 = 3 retained + 3 family-specific closures + 0 withdrawn`。三个候选为 VeOmni `#779/#781` 与 Hy-MT2 `#1`：前两项分别建立 host-side multimodal metadata producer/consumer contract 与 HSDP shard/replica collective 时序；第三项把多语言 evaluator 的 response join 从内容 `md5` 修正为 `(md5, instruction_lang)`，保留显式 legacy fallback，并按 test-item identity 重算 coverage。三项 exact commit/PR Evidence 与 Books 对读均完成，评分为 `6/7/6`，且评价纠错触发 Hy-MT2 的深入审阅。Books 为 `2 Integrate + 1 No Change`：root 已在 Ch40/Ch39 写入两项 paired binding，Hy-MT2 的完整 identity 命题由 Ch66 现有正文直接承载。新的 fresh non-author 已独立复算集合、复核三项 Evidence/Books、Anthropic 时间隔离与两项 root 正文，全部 Gate 通过。

另外发现的 ZAI Synapse 62 个 direct commit、MiniMax CLI 2 个测试/维护 commit、VeOmni 4 个早期已公开 PR 的窗内 merge，以及 Hunyuan 的普通 metadata renewal/重复底层 commit，均先按事件类型关闭，没有被扩大为逐 commit 全文审阅或当日 raw denominator。Moonshot `kimi-code` 的仓库创建、外部 contributor PR 和合并共同证明本窗公开，但其 README 只把既有 tool/TUI/MCP/subagent/hooks 组合为产品能力，没有新增长期机制或 evaluation/release contract，故在分母内关闭。旧 submitted-window ledger 的 508 项不是本日 public-owner inventory，迁移对账见 [`legacy-v21-migration-v3.json`](../_sources/daily-20260523/legacy-v21-migration-v3.json)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | 官方 Research RSS；05-22 两项条目均为 `2026-05-22T00:00:00Z`（北京时间 08:00，早于窗起），下一项为 05-25。 | 已检查 | 无 |
| `SRC-ANTHROPIC` | 官方 Research 两个 05-22 页面与 Red Team snapshot；snapshot 的 `2026-05-22 10:27 PT` 正确换算为北京时间 05-23 01:27，落在本窗内，但它不证明两篇 Research 文章的发布时间。 | 受阻 | 两篇文章只显示 `May 22, 2026`，缺官方时刻/时区、RSS 或 archive；不用于正面 no-hit，材料到达后只重开该 family。 |
| `SRC-GOOGLE-AI` | DeepMind Research/Blog 相邻日期与 Google Research Publications；可确认条目由 05-19 跳至 05-28。 | 受阻 | Publications 目录部分记录只给年/venue，不能据其证明日级零遗漏；恢复日级官方时间后只重开本源本窗。 |
| `SRC-META-AI` | 官方 Research/Publications 入口。 | 受阻 | 本次空响应/内部错误，不能把空响应当作无更新；需官方可读日期目录或等价官方 archive。 |
| `SRC-QWEN` | 官方 article API 英/中列表各 37 项；相邻记录为 05-20 10:00 与 05-29 17:00。 | 已检查 | 无 |
| `SRC-DEEPSEEK` | 官方 News/Research 入口；相邻研究/模型记录为 04-24 与 06-24。 | 已检查 | 无 |
| `SRC-MOONSHOT` | Kimi Platform Blog 与 MoonshotAI GitHub；Blog 无本窗条目；`kimi-code` repo/PR 建立一项可证明本窗 first-public family。 | 已检查 | 无 |
| `SRC-TENCENT-HUNYUAN` | 官方 Research API `publicList`（5 项，日期在 02/04/07/08 月）与 Tencent-Hunyuan GitHub；Hy-MT2 PR #1 为 1 项本窗 family，普通 metadata commit source-close。 | 已检查 | `Precise` 只有当前 repo `created_at` 与 backfillable commit time，缺同期公告、release、外部 PR/fork，不能证明本窗已公开，已隔离。 |
| `SRC-ZAI` | 官方 Research 相邻日期为 05-20 与 06-16；GitHub 精确窗的 62 个 Synapse direct commit 先做 event-type prune。 | 已检查 | 无 release/tag/RFC/首次公开证据；README 明示 early design/backward compatibility 未稳定，普通内部实现不进入 raw denominator。 |
| `SRC-BYTEDANCE-SEED` | 官方 Research/Public Papers 相邻记录为 05-16 与 05-29；VeOmni GitHub 精确窗 8 commits，按 PR 首次公开时间去重后 4 个本窗 family。 | 已检查 | 无 |
| `SRC-BAIDU-ERNIE` | 官方技术博客相邻条目止于 05-09；`PaddlePaddle/ERNIE` 精确 UTC 窗 commit=0。 | 已检查 | 无 |
| `SRC-XIAOMI-MIMO` | 官方 Paper/Blog 与 XiaomiMiMo GitHub；有日期论文由 03-13 跳至 06-29，GitHub 精确窗 commit=0。 | 受阻 | Blog cards 未给可复核日级时刻；不据此证明不存在未标日条目。 |
| `SRC-MINIMAX` | 官方英/中 Blog 与 Agent Tech Blog；相邻技术条目为 03-18 与 05-26/27；GitHub 2 commits 均为 CLI 测试/错误清理维护。 | 已检查 | 无 |
| `SRC-ARXIV` | [官方 availability schedule](https://info.arxiv.org/help/availability.html)：周五/周六不公告；前批北京时间 05-22 08:00，后批北京时间 05-25 08:00。 | 已检查 | 无；DataCite 只作 legacy identity 对账，不证明 cutoff。 |

结构化来源记录见 [`source-coverage-v3.json`](../_sources/daily-20260523/source-coverage-v3.json)，严格日期与事件去重见 [`official-owner-window-evidence-v3.json`](../_sources/daily-20260523/official-owner-window-evidence-v3.json)。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [VeOmni PR #779 — host-side multimodal metadata precompute](https://github.com/ByteDance-Seed/VeOmni/pull/779) | 2026-05-22T09:04:11+08:00 | 把 qwen2-family ViT 的 varlen/window metadata 从 GPU forward 中的 D2H 同步移至可复算的 host collator producer/consumer contract；`2 + 2 + 2 = 6` | 深入完成 | 整合：`TRAIN-MEGATRON`，[第40章](../../../../books/part-04-training-system/40-megatron.md)，root 写回已通过 fresh 写后语义复核 |
| [VeOmni PR #781 — HSDP accumulation sync elision](https://github.com/ByteDance-Seed/VeOmni/pull/781) | 2026-05-22T10:37:48+08:00 | HSDP 的 sharded `reduce_scatter` 每个 micro-step 保留，而 replicated `all_reduce` 仅最后一步需要；`2 + 2 + 3 = 7` | 深入完成 | 整合：`TRAIN-ZERO`，[第39章](../../../../books/part-04-training-system/39-zero.md)，root 写回已通过 fresh 写后语义复核 |
| [Hy-MT2 PR #1 — multilingual evaluator identity correction](https://github.com/Tencent-Hunyuan/Hy-MT2/pull/1) | 2026-05-22T18:20:42+08:00 | 同一 `md5` 可对应多个 `instruction_lang` 时，response join 必须使用复合 item identity，legacy fallback 要显式隔离且 coverage 按 test item 计算；评价纠错触发深入审阅；`2 + 2 + 2 = 6` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[第66章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

逐项 raw ledger 见 [`screening-ledger-v3.json`](../_sources/daily-20260523/screening-ledger-v3.json)。三项关闭分别为：Kimi Code 首次公开只组合既有 Agent 能力；VeOmni #780 是 #771 的内部返回值封装维护；VeOmni #784 仅新增 Qwen-Image LoRA 配置。closure false-negative challenge 恢复了 Hy-MT2 #1：标题虽像普通 benchmark maintenance，exact patch 实际改变了可影响语言切片与 coverage 的 evaluator identity contract。

## 4. 证据与知识整合

### [VeOmni PR #779 — host-side multimodal metadata precompute](https://github.com/ByteDance-Seed/VeOmni/pull/779)

采用 exact event `PR #779` 与 merge commit `d13637a1c8266c4a6b6a14a07923392e91ccbf9a`。PR 的 “What does this PR do?”/“Design & Code Changes” 明示：collator 从 packed `grid_thw` 在 host 侧导出 `cu_seqlens`、`window_index` 与 max-seqlen；ViT forward 消费 versioned `vit_metadata`，未提供 metadata 时保留 runtime fallback。评价证据是单台 A100 上 sync gate `18/18`、同模型 metadata/fallback logits `rtol=0, atol=0`、Qwen lineage logits `26/26`；它没有报告端到端 step time、CPU collator cost、多节点 scale 或生产 tail。配置依赖的 host port 可能漂移，剩余 HF rotary/mRoPE sync 仍被 allowlist；fallback 是恢复 device-side metadata 计算。第40章已说明 multimodal encoder 会改变真实 layout，却未说明“把 layout metadata 作为 host producer/device consumer 的显式合同，并用等价 gate 防止 silent divergence”，故形成精确 Integrate；root 的 paired binding 已通过 fresh 写后语义复核。

### [VeOmni PR #781 — HSDP accumulation sync elision](https://github.com/ByteDance-Seed/VeOmni/pull/781)

采用 exact event `PR #781` 与 merge commit `4c42062b6bf68a68c8b009764eec0de929c7a3d3`。PR 核心说明 HSDP 梯度需要 sharded 维的 `reduce_scatter` 与 replicated 维的 `all_reduce`；gradient accumulation 时后者只在最后 micro-step 才是必要同步。披露日志绑定 Qwen3.5-35B-A3B、FSDP2、offload、EP=8、MBS=1、GBS=128，三个 iteration 的总时间由 24:25 到 24:03；节点/GPU 数、重复次数和统计不确定性未披露，因此不采用通用加速数字，只采用通信时序机制。若 accumulation boundary、replica membership 或 gradient reduction convention 不一致，延后同步会造成 silent divergence；fallback 是每个 micro-step 完整同步。第39章只说 accumulation boundary 会影响 reduce-scatter timing，尚未分离 HSDP 的 shard/replica 两个 collective 维度，故形成精确 Integrate；root 的 paired binding 已通过 fresh 写后语义复核。

### [Hy-MT2 PR #1 — multilingual evaluator identity correction](https://github.com/Tencent-Hunyuan/Hy-MT2/pull/1)

采用 exact event `PR #1` 与 merge commit `fd271bebbe493144a1f4c258cc9be07c80db5e03`。补丁给 scorer entry 增加 `instruction_lang`，把 response map 从 `{md5: response}` 改为 `{(md5, instruction_lang): response}`，仅为旧输入保留显式 md5-only fallback，并把 coverage 从 unique-md5 intersection 改为 matched test-items / test-data。采用命题不是某个 benchmark 分数，而是 evaluator join 必须保存完整 item variant identity：否则同一内容 hash 的不同语言版本会覆盖或误接 response，在所有行仍合法时静默污染语言切片与 coverage。

该机制只由 IFMTBench 的 exact patch 支持；PR 未披露受影响行数、修正前后分数、重复语言数量或受控 regression，因此不采用影响幅度或 benchmark-wide 提升。复合 key 增加 schema/ingestion 要求；md5-only fallback 会掩盖缺失语言并重新折叠 variant。安全 fallback 是仅在证明 hash 唯一或显式 legacy schema 时启用 md5-only，否则把条目标为 missing/unscorable 并保留 raw response。唯一 owner 是 `PLATFORM-EVALUATION-SYSTEM`：第66章已要求贯穿 cohort 到 analysis artifact 的完整 run identity、保存 per-example 与 language/region slice，并在跨语言派生 benchmark 中保留 label/choice identity、language-specific invalid cases 与 source-to-target lineage；这些具体命题已直接排除 content-only join，因此判定 `No Change — Existing Coverage`，不生成 root Books queue。

完整 Evidence 与 non-proof locator 见 [`exact-v1-evidence-v3.json`](../_sources/daily-20260523/exact-v1-evidence-v3.json)，现有正文对读见 [`books-current-content-comparison-v3.json`](../_sources/daily-20260523/books-current-content-comparison-v3.json)。两项写回及 root-applied 状态见 [`BOOKS_WRITEBACK_QUEUE_V3.json`](../_sources/daily-20260523/BOOKS_WRITEBACK_QUEUE_V3.json)；本次 repair author 没有写共享 Books。

## 5. 缺口与下一步

- Root Books queue 的 2 项真实 Integrate 已写入并通过 fresh non-author 终审：VeOmni #779 → `TRAIN-MEGATRON` Ch40；VeOmni #781 → `TRAIN-ZERO` Ch39。两项 paired marker 全局唯一成对、位于主 Review notes 前，正文 binding、证据边界和相邻语义均通过。
- Hy-MT2 #1 已从 closure 恢复，但 Ch66 的完整 run identity、per-example/language slice 与跨语言 lineage 命题已经承载其长期结论，故为 `No Change — Existing Coverage`，没有新增 root Books queue。
- `SRC-ANTHROPIC`：相关 snapshot 的 `2026-05-22 10:27 PT` 是北京时间 05-23 01:27，落在本窗内；但两个 Research 页面只有日期，snapshot 时刻不能代替文章 first-public 时刻。当前 family 隔离且不支持正面 no-hit，所需官方 timestamp/RSS/archive 已列入 Materials Request。
- `SRC-TENCENT-HUNYUAN / Precise`：缺少能证明仓库在本窗已经公开的官方 announcement/release/event，或同期外部 public PR/fork。当前 GitHub repo `created_at=2026-05-22T02:07:30Z` 与 initial commit `2026-05-22T08:06:55Z` 都可能被 private→public 或 backfill 打破，故不进入 raw、候选、正面证据或 Books。材料到达后只重开该 family。
- `SRC-META-AI`：官方 Publications 目录本次空响应/内部错误；可接受官方可读日期列表、官方 archive 或逐项官方事件页。恢复后只扫描本窗，不扩为整月。
- Google Publications 的日级精度与 MiMo undated Blog cards 作为检索限制隔离，不用于“无遗漏”断言；若官方日期元数据到达，只定点重开命中的条目。精确材料清单见 [`materials-request-v3.json`](../_sources/daily-20260523/materials-request-v3.json)。
- 旧 V2.1 508-item submitted-window ledger 已保留原文件，当前 owner crosswalk 为 `334+125+4+10+6+29=508`：前 479 项分别落到 05-25/26/27/28/29 owner 批次，29 项仍需其真实 owner 日定点恢复；它们不反向改变本日分母。

以上外部缺口均为终态保留项，不支持正面证据、Books 或无遗漏断言；定点重开条件是取得对应 family/item 的官方 timestamp、日期目录、archive/feed 或同等 first-public 证明，只重开命中的本源本窗，不扩窗、不扩源。

本轮 date-local repair 与独立终审均已完成；外部缺失保持精确隔离，不用于正面 no-hit 或长期采用命题。新的 fresh non-author 已复核全部 `6=3+3` 集合、三项 Evidence/Books 决定、Anthropic 时间边界及两项 root 正文，当前无剩余执行队列。

## 6. 复核

复核者：fresh non-author（未参与本日 repair 或两项 root Books 写回）

结论：通过

最终 state 为 `6=3 retained+3 closure+0 withdrawn`、`3=3 deep+0 standard`、`3=2 Integrate+1 No Change`、pending root queue=0。终审独立复核 Kimi first-public/closure、VeOmni #780/#784 closure、三项 retained exact evidence 与 Books owner；Anthropic snapshot 的 05-23 01:27 BJT 在本窗内，但只证明 snapshot 自身，两个 date-only Research 页面继续隔离。Ch39/Ch40 两项 root binding 的 marker、位置、机制、ownership、证据边界、trade-off、failure/fallback 与相邻衔接均通过。完整收据见 [`V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260916.md`](../_sources/daily-20260523/V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260916.md)。
