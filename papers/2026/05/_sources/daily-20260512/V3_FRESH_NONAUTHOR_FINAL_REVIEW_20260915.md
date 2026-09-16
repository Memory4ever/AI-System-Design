# 2026-05-12 V3 全新非作者终审

**复核者关系：** 未参与本日报当前 V3 作者重建、11 项 root 写回或此前 24 项 Books 写入  
**复核范围：** 仅限 2026-05-12 当前 V3 报告、账本与现有 Books 绑定；未扩展日期、来源或候选池  
**结论：** 未通过；日报保持 `进行中`

## 已确认成立的部分

- 窗口一致为 `[2026-05-11T09:00:00+08:00, 2026-05-12T09:00:00+08:00)`；1146 个 arXiv 身份均归属 2026-05-12 08:00 官方公告批次。
- 算术闭合：`1146 raw = 110 retained + 1036 pre-denominator closures + 0 withdrawn`；110 个候选在 evidence、Books comparison 与 README 中身份集合一致。
- 110 项 V3 分数均为三个 0～3 整数且 Total 正确；13 项 6 分走 standard，97 项 7～9 分走 deep。
- 110 项均有 exact-v1、withdrawal、证据与 owner 字段；所有 Stable Node 与 owner path 均可在当前 ROADMAP / Books 中解析。
- 35 项 Integrate 的正文均可在声明 owner 中定位，并位于最后一个 `## Review notes` 之前。最近 11 项 root 写回各有一个 canonical semantic marker，正文均形成“旧路径为何合理 → 新约束 → 机制/状态所有权 → 代价与 failure → fallback → exact-v1 boundary”的完整链条。

以上只确认结构与已核内容，不足以覆盖下面的语义缺口。

## 必须返修的有界问题

### 1. 八个 Daily source ID 的窗口覆盖没有覆盖注册入口

当前账本只记录每个 Source ID 的首个 endpoint；下列同一 Source ID 下的注册入口没有本窗检查依据，不能据此断言该 source 已闭合：

- `SRC-GOOGLE-AI`：缺 `https://research.google/pubs/`
- `SRC-MOONSHOT`：缺 `https://github.com/MoonshotAI`
- `SRC-TENCENT-HUNYUAN`：缺 `https://github.com/Tencent-Hunyuan` 与 `https://github.com/Tencent/llm.hunyuan.T1`
- `SRC-ZAI`：缺 `https://github.com/zai-org` 与 `https://docs.z.ai/release-notes/new-released`
- `SRC-BYTEDANCE-SEED`：缺 `https://seed.bytedance.com/en/public_papers` 与 `https://github.com/ByteDance-Seed`
- `SRC-BAIDU-ERNIE`：缺 `https://github.com/PaddlePaddle/ERNIE`
- `SRC-XIAOMI-MIMO`：缺 `https://github.com/XiaomiMiMo`
- `SRC-MINIMAX`：缺中文技术博客、GitHub 与 Agent Tech Blog 三个注册入口

返修只需定点核对这些入口在本窗的事件；不得扩为机构历史扫描。若首查入口能证明它是其他入口的完整事件索引，应把该证明写入来源行。

### 2. 十四项高风险 closure 不能由现有理由安全排除

下列题摘明确提出了可能改变当前主线机制或适用边界的内容；现有“局部方法/单一 benchmark、没有改变 owner”理由不符合“owner 不变仍可有长期增量”的准入合同。必须重开 title+完整 abstract 准入；只有准入后才按分数决定证据深度，不能直接预判 Integrate：

| arXiv | 需重开的具体增量 |
| --- | --- |
| `2605.08538` | Agent memory 的 consolidation、forgetting、reconsolidation 与 accuracy/store-size operating curve |
| `2605.08568` | prompt-aware SVD rank routing、pattern cache 与 fused execution 改变压缩模型的在线执行分支 |
| `2605.08615` | ReRAM-on-logic、低位表示与 adaptive speculative execution 的联合 accelerator 设计 |
| `2605.08703` | reward modeling 从 weight optimization 转为可演化 tool/skill context 的替代分支 |
| `2605.08813` | graph-structured multi-agent workflow 的 agent removal/replacement 与 baseline-anchored acceptance gate |
| `2605.08878` | refusal-escape direction 的 operator decomposition 及 safety–utility 机制边界 |
| `2605.08933` | Muon full-matrix 与 head-group whitening 的可解释优化 trade-off |
| `2605.09121` | retry、voting、critic refinement 与 adaptive routing 的统一 reliability/cost allocation 层 |
| `2605.09281` | MoE expert 的二维分块低秩量化与 fused single-pass execution |
| `2605.09516` | layer-level sparse routing 与 shared-softmax / routed-linear hybrid attention 架构分支 |
| `2605.09536` | diffusion LM 的 temporal-aware trajectory distillation 与 accuracy/parallelism operating modes |
| `2605.09603` | parallel masked diffusion 的 sequence-level edit correction 分支 |
| `2605.09630` | byte patch lag、entropy-triggered scratchpad 与 KV/compute/quality trade-off |
| `2605.09867` | continuous latent context 作为 online-learning persistent state 的模型机制 |

返修后重新冻结 denominator，并同步 raw/retained/closure 计数；不得顺带重审其他 closure。

### 3. 五项 exact-v1 证据定位仍是模板位置

`2605.08368`、`2605.08399`、`2605.08432`、`2605.08467`、`2605.08505` 的 Method、Evaluation 与 Limitations locator 使用了统一的 `§2 Problem/Setup; §3 Method or Architecture`、`§4–§5 Evaluation`、`§6 / Appendix` 模板，而不是当前 exact-v1 的真实标题/位置。必须只重开这五份 exact-v1，替换为实际段落、表/图或附录定位，并核对采用命题与反证边界；不能用摘要句补齐。

### 4. 三十二项 No Change 尚未完成命题级 Books 对读

下列 comparison 只记录“基础契约已覆盖”或正文关键词命中，没有指出 Books 中实际承载同一结论的命题以及 exact-v1 增量为何没有改变其边界。这不满足 `No Change — Existing Coverage`：

```text
2605.09269 2605.09278 2605.09285 2605.09303 2605.09317 2605.09330
2605.09375 2605.09387 2605.09397 2605.09442 2605.09490 2605.09497
2605.09544 2605.09608 2605.09649 2605.09650 2605.09681 2605.09701
2605.09702 2605.09721 2605.09820 2605.09886 2605.09934 2605.10012
2605.10223 2605.10351 2605.10380 2605.10405 2605.10763 2605.10805
2605.10870 2605.10901
```

每项只需重读其声明 owner 的 `Review notes` 之前正文与必要相邻 handoff，给出具体命题级对照；若实际有知识缺口，则改为 Integrate 并交 root 串行写入。不得用标题、章节名、词频或 Review notes 作为已有覆盖证明。

### 5. 两项既有 Integrate 缺 canonical Source Family marker

- `2605.09315` 在 `AGENT-PLATFORM` 正文有 `arXiv:2605.09315v1` 证据，但没有 `SF-2026-ARXIV-2605-09315` marker。
- `2605.09684` 在 `PLATFORM-MONITORING` 正文有 `arXiv:2605.09684v1` 证据，但没有 `SF-2026-ARXIV-2605-09684` marker。

两段语义链本身可读，返修仅需 root 补 canonical marker 后复核唯一性与 `Review notes` 边界；作者/本 reviewer 不编辑 Books。成对的 `:start` / `:end` marker 视为一个绑定区间，不是重复写入。

### 6. 当前 V3 状态投影互相矛盾

- `V3_AUTHOR_REBUILD_LEDGER.json` 仍写 `ongoing_pending_independent_review_and_root_writeback`，但 11 项 root 写回已经完成。
- README 的 11 个候选行仍写“待 root 写回”，而同页汇总写“已由 root 写入”。
- 11 个 `owner_sha256_after_writeback` 已因共享章节后续修改而全部失配；marker 和语义仍在，因此旧 hash 不能继续充当当前写入证明。

返修后应从实际正文重新生成一致状态；hash 可以删除或刷新，但不能用旧值覆盖现状。

## Gate 判定

- Coverage：**未通过**，限定为上列 8 个 Source ID 的缺失入口。
- Candidate denominator：**未通过**，限定为上列 14 个 closure 的重开准入。
- Evidence：**未通过**，限定为上列 5 个 exact-v1 locator。
- Books：**未通过**，限定为 32 个命题级对读与 2 个 canonical marker；最近 11 个 root 语义写回本身通过。
- Report：**未通过**，状态投影需在返修后统一。

只有以上有界返修完成、必要 root 写回落实，并由另一位未参与返修的 reviewer 做新的终审后，才能将日报改为 `完成`。
