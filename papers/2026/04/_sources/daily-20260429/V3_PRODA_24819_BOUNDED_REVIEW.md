# 2604.24819v1 ProDa：单篇有界证据与作者侧处置

本记录只属于 2026-04-29 V3 日报的作者侧必要审阅，不是独立 Gate 或 Books 写后验收。官方身份与原文：[arXiv exact-v1 HTML](https://arxiv.org/html/2604.24819v1)、[版本页](https://arxiv.org/abs/2604.24819v1)。本窗归属借本日检查点中的官方公告规则、24765–25918 相邻 ID 与 DOI 时间**联合**批次链；不以 v1 的 submitted 或 DOI created 单字段代替首公开，也未排除该家族独立更早首发的例外。

## 贡献准入与机制

《Programming with Data: Test-Driven Data Engineering for Self-Improving LLMs from Raw Corpora》不是因覆盖 16 个学科或套用 test-driven 名称而准入。§2.1–2.2、§4.1–4.3 给出的具体控制边界是：从源语料抽 L3 推理链，再分解为 L2 关系和 L1 概念；训练样本由 L1/L2、评测题由 L3 生成，二者携带共同知识节点身份。对失败题，LLM judge 提议“概念缺口”或“推理链断裂”，分别生成对比知识或 CoT patch，按失误学科分配并混入不与 patch 共用 L2 ID 的 replay，随后从同一 base checkpoint 重训。这把评价失败接到数据修补的可追溯提案，而不让 benchmark 直接拥有真实因果归因。该设计对训练 Data owner 与 Evaluation 的交界有具体增量，值得进入候选；自然/生物医学子任务并不因此自动取得 AI-for-Science 结论。

作者侧拟 `Design Delta 3 + System Reach 2 + Durability 2 = 7`，深入审阅，唯一长期 owner 提议 Ch27 Data 的数据/训练—评测 lineage；Ch66 Evaluation 只掌最终独立 verdict。**Books 暂缓**，先交非作者核“共同知识图谱带来的故障定位”是否为 Ch27 当前 failure-driven curriculum 与 typed lineage 之外的真正窄缺口。旧 V2.1 日报给 9 分、Existing、`Complete` 不继承。

## 必要评价与直接反证

- §3.2 的 ProDa-16 与 11 个外部 benchmark 的模型排序平均 Spearman `ρ=.847`，支持受限构念相关性，不证明题目独立、无污染或诊断是因果 root cause。§3.4、Figure 5 在 Qwen-2.5-7B、每学科 1K/2K/5K/10K 生成量下与 Alpaca/EasyDataset/DataFlow 对比；1K repair 68.72 vs Alpaca 2K 峰值 68.12，5K 72.11 vs DataFlow Filter 56.18，是此生成器/模型/benchmark 的受限结果，不能据此宣告总生成成本匹配或通用优越。
- §4.2 Eq.5 仅说明 `B=f_bench(K3)`、`S=f_syn(K1,K2)` 的**输入层**分流。§4.2 又明说训练合成接收沿同一推理链的 L2 triples 及定义。因此从结构分流本身推不出作者的强句“没有任何评测题能由训练样本逐字回忆回答”；生成器完全可能把相邻 triples 组合成与 L3 题相同的表述。这里是逻辑上的必要保证缺口，**不是**声称已在公开数据中发现实际重复题。更不可能仅凭共同源图和 rank correlation 证明训练/评测独立。需 item-level overlap/近义测试、source-chunk split 与独立 holdout，反复用同一 ProDa-16 诊断/重训后的分数只能是开发反馈。
- §3.4、Table 2 的“general capabilities remain fully preserved”只能缩到受测子集、模型及指标，且表内明确有反例：Llama3.1-8B 的 C-Eval 6 子集 Base `60.64`、V1 `49.54`、V2 `50.23`，V2 相对 Base 仍约 `-10.41` 点；Qwen2.5-3B 的 MMLU 12 子集 Base `70.16`、V2 `69.11`。正文只称 MMLU 九模型有七个 V2 达到/超 Base，不能把这一统计替代每模型/每能力全保留。重训 patch、replay 与 general-capability 变化不能全归因于知识图谱本身。
- §4.3 的 LLM judge 用答错题、正确答案和图谱 metadata 决定“缺概念/缺推理”。同一错误可来自题目歧义、解析/格式、模型采样或抽取图谱错误；zero orphan 和 >99% connectivity 只证明**内部图结构**连通，非知识正确性。patch 和 replay 提高成本，图谱/评测同源偏差会闭环强化。若缺可信 source、隔离 holdout 或判题答案，回退冻结数据版本、人工 error taxonomy 与独立评测，不以自动诊断即真因。

## 现有 owner 对照与状态

已实际顺读 `books/part-04-training-system/27-data.md` 的“静态 Mixture 到版本化 Data Control Plane”、约 446 行的 Failure-driven Curriculum，以及约 754 行的 Typed Lineage Graph：它们已有 failure attribution→curriculum→independent verifier 和派生样本到评测 overlap 的原则，却未明确同一知识层级让训练样本与评测题可追踪对齐、同时制造适应性评测/共源污染的双刃边界。`books/part-06-ai-infrastructure/66-evaluation-system.md` 已有公开开发集不能冒充 release holdout 的实际命题。拟供 peer 判断的最窄 Ch27 增量是“shared specification 可用于 repair proposal；Evaluation 必须独立验证原图事实、item/semantic overlap、held-out general capability，不能由 shared graph 自动赋予测试独立性”。现在只存提案，未写共享 Books、未计 Integrate、未冻结本日候选或日级 Gate。
