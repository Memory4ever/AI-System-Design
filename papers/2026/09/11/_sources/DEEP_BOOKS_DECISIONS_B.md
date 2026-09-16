# 2026-09-11 Deep Books Decisions — Batch B

本文件只登记 Books Decision 与正文锚点，不替代 `DEEP_REVIEW_BATCH_A.md`、`DEEP_REVIEW_BATCH_B.md` 的逐篇证据审阅，也不改变 Daily Report 的 Evidence、Access、Review 或 Complete 状态。此次写入只覆盖分配给本批次的六个章节；Ch27 只给 Root-owned 建议，Ch72 只核对既有正文，未修改 README、Ch27 或 Ch72。

## 决策总表

| Source family | Score | Stable owner | Books decision | 正文锚点 / 后续动作 |
|---|---:|---|---|---|
| `SF-2026-ARXIV-2609-11020` | `3/1/3=7` | `INFER-KV-CACHE` | Integrated | Ch45 `KV intervention 必须冻结 Layer Scope、Position 与 Conditioning` |
| `SF-2026-ARXIV-2609-11058` | `2/3/2=7` | `MULTIMODAL-REPRESENTATION` | Integrated | Ch23 `Edge split 把 fused latent 变成通信接口` |
| `SF-2026-ARXIV-2609-11061` | `3/2/3=8` | `TRAIN-GRPO` | Integrated | Ch33 `Fork Placement 要追踪 Belief Shift，而不是假设中点最有信息` |
| `SF-2026-ARXIV-2609-11063` | `3/3/3=9` | `MODEL-POSITION-ENCODING` | Integrated（bounded handoff） | Ch13 `隐藏坐标的相似不能替代输出分布的几何` |
| `SF-2026-ARXIV-2609-10901` | `2/2/3=7` | `AGENT-RAG` | Integrated | Ch76 `Query Policy 与 Evidence Graph 分开拥有控制与证明` 的 post-run evidence graph |
| `SF-2026-ARXIV-2609-11065` | `3/2/3=8` | `AGENT-RAG` | Integrated | 同一 Ch76 锚点的 pre-run query policy |
| `SF-2026-ARXIV-2609-11067` | `3/2/3=8` | `PLATFORM-EVALUATION-SYSTEM` | Integrated | Ch66 `Judge 的输入扰动必须保留 Clean Twin` |
| `SF-2026-ARXIV-2609-11085` | `3/2/3=8` | `PLATFORM-EVALUATION-SYSTEM` | Integrated | Ch66 `Binary Verdict 通过不等于语义忠实` |
| `SF-2026-ARXIV-2609-11146` | `3/2/3=8` | `TRAIN-DATA` | Integrated | Ch27 `递归合成语料要先分清 Corpus Recursion 与 Parameter Recursion` |
| `SF-2026-ARXIV-2609-10992` | `2/2/3=7` | `PLATFORM-SECURITY` | Existing Coverage；No Change | Ch72 `隐私检测是 Policy-bound Sensor，不是安全判决` 与 `从独立 Span 到关系感知的本地 Sanitization` |

所有十项的 exact-v1 HTML 均可访问；first public 均为 `2026-09-11T08:00:00+08:00`，审阅时 submission history 只有 v1 且无 withdrawal notice。实现 artifact 状态按深审文件分别保留，不能由 HTML 可读推导代码可复现：2609.11020、11058、11065、11085 的公开实现不可审，2609.11063 仅 request-only，2609.11067 虽链接公开仓库但未执行 code audit。

## 已写回的长期增量与边界

### `2609.11020` → `INFER-KV-CACHE`

长期增量不是 persona 技巧，而是 KV 从精确复用状态变为行为干预状态后，实验和运行时都必须显式冻结 layer/head/position、K/V 动作、token-history conditioning 与 read/write 顺序。正文保留 exact-prefix reuse / dense recompute 作为失败回退，并明确 representation alignment 不等于 behavior preservation。单模型、单 persona pair、单 prompt、小样本以及 `n=1` cache dump 只支持合同边界，不支持普适中层因果结论。

### `2609.11058` → `MULTIMODAL-REPRESENTATION`

长期增量是把 edge-side fused latent 提升为版本化表示接口，使跨模态融合与通信边界进入同一 contract；它不是一个新的多模态模型摘要。正文同时保留 task-aware compression 的未来任务信息损失、端侧计算/能耗、带宽不再受限时收益消失，以及 raw、低压缩、per-modality feature 与 late-fusion fallback。证据只覆盖 MS-COCO 图文匹配与估算链路，不证明真实边缘部署、隐私或开放生成。

### `2609.11061` → `TRAIN-GRPO`

长期增量是把 tree rollout 的 fork placement 写成独立 sampling-control state：belief-shift probe 只选择更可能产生 sibling 分化的 checkpoint，leaf verifier 仍拥有 correctness，global/local reward 仍拥有 credit。正文登记 checkpoint drift、probe FLOP、树状态复制、siblings 同解与代码任务反例，并保留 midpoint、uniform tree 和 chain/group sampling。离线 BSV 没有被写成在线稳定 selector。

### `2609.11063` → Ch13 bounded handoff

当前 `ROADMAP.md` 将 Ch13 映射为 `MODEL-POSITION-ENCODING` 和 `13-position-encoding.md`，而不是 Ch12 Embedding。本次按用户指定的章节号写入 Ch13，并只吸收与位置条件化 hidden state 可辨识性直接相连的测量边界：隐藏坐标的 Euclidean/cosine 几何依赖 chart，行为层等价需回到 next-token law 的 Hellinger/Fisher–Rao geometry。正文没有把通用 information geometry 的 owner 移入位置编码，也没有修改 Ch12；自然梯度控制只作为局部、需阻尼和重线性化的受限 handoff。

### `2609.10901` + `2609.11065` → `AGENT-RAG`

两项合并成一条控制—证据演进链：

```text
static top-k / fixed traversal
-> allowlisted, clamped query-policy vector
-> bounded retrieval run
-> evidence-propagation DAG over the realized trace
-> claim-level answer gate and original locator
```

MOSAIC 只拥有 pre-run 的 seed、traversal、depth、beam、stop 与 evidence-budget proposal；SearchAtlas 只拥有 post-run 的 constraint use、support flow 与 unsupported-prior trace。前者不能造事实，后者不是因果或 truth oracle，两者不能互相自证。正文保留固定检索、逐 claim citation/entailment、矛盾/约束检查、可执行 verifier 与人工升级；analyzer latency、域外退化、graph construction/parser error 都是明确 failure。

### `2609.11067` + `2609.11085` → `PLATFORM-EVALUATION-SYSTEM`

两项分别补齐 measurement instrument 的两个盲区。对 model judge，clean/noisy twin、扰动 seed/family/强度、实际 edit rate、judge revision 与 A/B/None 转移成为 receipt；稳定不代表正确，翻转方向也不自动证明真实社会偏见。对 executable verifier，同一 binary verdict 内仍需 reference-equivalent positive 与 verdict-preserving unfaithful negative；部署时不读 reference 的 learned verifier 只能作为 sensor，不能替代 solver、测试、正式证明或人工语义 authority。正文保留 abstain/quarantine/escalation，并将 `Best-of-N` 采样收益与 gate、selection、feedback 增量分开。

## Root 写回：`2609.11146` → `TRAIN-DATA`

Ch27 已写入以下长期增量：递归合成数据实验必须区分 corpus recursion 与 parameter recursion。每一代都从 clean base weights 重新训练，能隔离“共享训练语料被上一代模型输出污染”的路径；supplier-share concentration、pool composition、人类文本占比与随机 seed 应作为不同控制轴，不得把模型权重/优化器跨代累积混入同一结论。现有 mixture、provenance 与 human-anchor gate 作为失败回退。

事实边界一并保留：自然生态只测 1–4B、`K<=13`、五代、三 paired seeds，最高自然集中度为 28%；90% 只属于注入式三模型 probe；travel-propensity 是 19 arms 的 post-hoc fit；7–8B probe 未充分收敛；代码与逐 arm 测量仍待发布。结果只能说明所测配置中 composition/human-text fraction 比有限的 supplier concentration 更能解释方向与速度，不能写成“集中度无害”、普适 model-collapse law 或生产平台因果结论。正文 marker 为 `source-family:SF-2026-ARXIV-2609-11146`。

## Existing Coverage：`2609.10992` → `PLATFORM-SECURITY`

Ch72 已有两处正文共同覆盖本 family 的长期增量：

1. `隐私检测是 Policy-bound Sensor，不是安全判决` 已把 detector、candidate spans、local policy、mask/remove/pseudonymize/review 分责，并明确 learned policy 只形成 privacy–utility Pareto，不提供 differential privacy，事实改写仍需 deterministic rule 与审计回退。
2. `从独立 Span 到关系感知的本地 Sanitization` 已覆盖本地 contextual leakage graph、utility/leakage edge、选择性 sanitization、opaque placeholder、consistency-gated restoration，以及 client 对 original、graph 与 mapping 的 ownership；同时保留 fail-closed、regex/NER、rewrite 与 DP 的分层/替代边界。

因此 2609.10992 判定为 Existing Coverage / No Change。该判定不采纳论文的具体 utility/leakage 数字为长期常数，也不把 learned sanitization 当成隐私证明；Ch72 未修改。

## Gate 结论

本批次 9 个需写回的 source family 已在对应正文形成可独立阅读的旧约束→新机制→trade-off/failure→fallback/证据边界链，并在每个目标章节首个 `Review notes` 之前绑定 source marker；其中 `2609.11146` 已由 Root 写入 Ch27。`2609.10992` 为核验后的 Existing Coverage。Daily Report 的整体 Complete 仍须由 Root 汇总其它批次、README 状态、共享写入和独立语义复核后判定。
