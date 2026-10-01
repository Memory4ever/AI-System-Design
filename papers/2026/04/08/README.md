# Daily Research — 2026-04-08

**规范：** V3
**窗口：** 2026-04-07T09:00:00+08:00 ～ 2026-04-08T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T15:16:25+08:00

## 1. 结论

按当前合同独立重建，不继承旧V2.1的44项候选、评分与Complete。567个去重arXiv发现身份只作宽召回线索，已浏览标题并对主线可能项读取摘要；它们不是当天有效贡献数，也不是全文队列。旧材料完整保留于[存档](../_sources/daily-20260408/V2_1_REPORT_ARCHIVE.md)。

34项工作集合经逐家族日期核对，5项缺少早于09:00的可用上界，移入精确日期隔离；非作者定点否定侧复核恢复04943/05074与05217后，最终确定候选32项（含Anthropic一项及arXiv31项），20项深入、12项标准审阅，15项已实际整合、16项已有覆盖、1项理论争议暂缓。主要增量涉及有损speculative acceptance的条件/最终分布界、多drafter选择状态、部分KV读取的联合归一化、流式训练buffer生命周期、共享base/adapter执行分离、检索向量信任与聚合梯度、tokenizer及attention转换、有限样本评价、代码编辑oracle与flow目标边界。首发归属使用永久ID分配规则、相邻公告批次/OAI及各家族版本可用时间构成有界推断，08:00～09:00不是单字段给出的精确公告时刻。In-Place TTT及5项跨截点线索的必要证据保留，不评分、不据它们写Books；不能从Submitted或DOI created反推归属。15项正文落点与限制已逐项对账，见[续跑点](../_sources/daily-20260408/V3_REVIEW_CHECKPOINT.md)。非作者日级验收通过；完成包含实际Books整合与具名外部保留项的安全隔离，不等于所有来源无缺口或作者主张均被证实。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方[News RSS](https://openai.com/news/rss.xml)1230项至2015年；04-06T10:00Z→04-08T05:00Z跨窗，无落窗News项；Research/Index只取得最新列表 | 受阻 | RSS不等于全部Research论文；历史索引分页受限，作者arXiv另查 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)嵌入publishedOn历史条目；Mythos04-07T09:35Z落窗，正文已读 | 已检查 | 未披露漏洞不能独立验证，不据宣传补机制 |
| SRC-GOOGLE-AI | [Research April目录](https://research.google/blog/2026/04/)9项；DeepMind实际/blog/page/3/共24项、覆盖May→Jan，April邻域Robotics04-14T16Z→Gemma04-02，DiLoCo04-23T16Z明确窗外；Research Publications历史首发目录仍未形成停点 | 受阻 | Google04-08文章因同家族重复说明关闭；Publications历史日期未恢复，不能以Blog/selected pubs替代完整Research覆盖 |
| SRC-META-AI | [Blog](https://ai.meta.com/blog/)与?page=2已读，04-08两项发布→04-06/03-27；两篇exact博客正文已读；[Publications](https://ai.meta.com/research/publications/)恢复仍HTTP500 | 受阻 | 两篇04-08博客仅原始日历日，直连HTML未恢复更精确时间；Research/Publications历史目录仍缺，见§5精确隔离，不作全源零命中 |
| SRC-QWEN | 官方research.research-list静态60项+article/retrieval动态40项，04-02T04:00+08→04-15T10:00+08跨窗；组织最新100新仓无落窗；Qwen3/Qwen3.6无release条目 | 已检查 | 官网列表不替代作者论文；无release不证明无所有artifact变化 |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/)Research02-25→06-24、动态12-01→04-24跨窗；组织最新100新仓无落窗；V3.2 release列表为空 | 已检查 | 仅公开目录与重要仓库，不全扫任意commit |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)所列研究到2025年11月；组织最新100新仓无落窗；kimi-cli release100项至2025-10-24无本窗 | 已检查 | 官网未列原始论文仍由arXiv查漏 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)官方publicList pageNum1/pageSize100/renderType0：9/9项，04-30/04-23→02-13跨窗；T1无release，新仓补检无落窗 | 已检查 | 仅官网可见目录，不宣称所有未列论文不存在 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)id157 GLM-5.1 createAt=04-07T16:00Z落窗，已读训练目标/长任务案例；GLM-5 release空、新仓无落窗 | 已检查 | 机制/完整评价未披露，不能由8小时演示外推自主性 |
| SRC-BYTEDANCE-SEED | Publications page_token20/40跨04-09/04-08→04-07→03-31；Blog page0/20跨04-08T16Z→03-31T16Z→2025年12月；Seed-Coder release空 | 已检查 | 07026 CMS日期早于v1提交，见缺口；科学任务排除 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)04-15/04-30→02-06跨窗；ERNIE唯一release2025-06-30；组织新仓无落窗 | 已检查 | 仅公开目录/重要artifact检查 |
| SRC-XIAOMI-MIMO | [官网](https://mimo.xiaomi.com/)Paper8项06-29→03-13→02-03跨窗；Blog14项无日戳；官方JS路由恢复后定点查3篇，UltraSpeed06-08明确窗外、其余未得原始时间；MiMo release空、新仓无落窗 | 受阻 | 无日戳Blog的当窗归属未恢复；原始发布日期/可验证早发正文到达后只重开对应项 |
| SRC-MINIMAX | [Blog](https://www.minimax.io/blog)12项读完，05-26→03-18→02-14跨窗；[Agent Tech Blog原始目录](https://agent.minimax.io/docs/techblog.md)唯一项05-13；M2.7 release空、新仓无落窗 | 已检查 | 不以页面组件当前日期/lastmod替代文章发布时间 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html)Tuesday20:00EDT→本窗08:00；04934/04935和06170/06171 DOI批次边界与官方OAI交叉；raw567仅发现库存；31个arXiv保留家族精确版本已审，逐项v1可用上界与组合批次证据核对 | 已检查 | 5项跨截点及06169更早首发线索精确隔离；待非作者分母/排除侧复核，不把Updated孤证叫首发 |

## 3. 候选与判断

下表为经独立复核冻结的32项确定候选。31项arXiv的08:00～09:00是永久ID公告分配、相邻批次/OAI与本家族v1可用上界共同支持的有界推断，不是Submitted、Updated或DOI created本身的公告时刻。5项缺少截点前可用上界移到§5，不评分；明确窗外或贡献排除项不列候选。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Claude Mythos Preview's cybersecurity capabilities](https://www.anthropic.com/research/mythos-preview) | 2026-04-07T17:35:00+08:00 | 漏洞proposal、重现、严重性与披露分账；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)、PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Cactus: Accelerating Auto-Regressive Decoding with Constrained Acceptance Speculative Sampling](https://arxiv.org/html/2604.04987v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 显式divergence预算与exact verifier sampling不同；条件预算不等于最终算法预算；2+2+2=6 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)有损分支的条件h与最终h_alg、隐式Γ及exact fallback |
| [Measuring the Permission Gate: A Stress-Test Evaluation of Claude Code’s Auto Mode](https://arxiv.org/html/2604.04978v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | Edit/Write操作状态绕过shell gate，区分未覆盖与分类误差；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)受保护config/self-state mutation与跨protocol同effect的执行时授权 |
| [Top-K Retrieval with Fixed-Size Linear-Attention Completion: Backbone- and KV-Format-Preserving Attention for KV-Cache Read Reduction](https://arxiv.org/html/2604.05438v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | summary补全未读numerator/denominator，扣除已读支持防双计；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)exact/residual减除及联合归一化、selector成本与退化边界 |
| [MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU](https://arxiv.org/html/2604.05091v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | CPU权威状态与无持久weight pointers模板、stream事件生命周期；2+2+2=6 | 深入完成 | 整合：TRAIN-ZERO [Ch39](../../../../books/part-04-training-system/39-zero.md)CPU-authoritative流式buffer与layer-template绑定生命周期 |
| [Edit, But Verify: An Empirical Audit of Instructed Code-Editing Benchmarks](https://arxiv.org/html/2604.05100v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 编码oracle须同时验目标改动与未要求区域不变量；失败可来自artifact而非能力；1+2+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)代码oracle的change/preserve双面合同与diff/AST/coverage不充分边界 |
| [Not All Turns Are Equally Hard: Adaptive Thinking Budgets For Efficient Multi-Turn Reasoning](https://arxiv.org/html/2604.05164v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 回合budget会消耗后续资源，global soft penalty不同于硬cap；1+2+2=5 | 标准完成 | 已有覆盖：AGENT-PLANNING [Ch79](../../../../books/part-07-agent/79-planning.md)belief/remaining-budget控制与hard cap、verification reserve |
| [Nidus: Externalized Reasoning for AI-Assisted Engineering](https://arxiv.org/html/2604.05080v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | finite spec/PO外置、mutation前验证；完整性只限建模路径；1+2+2=5 | 标准完成 | 已有覆盖：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)protocol-owned mutation与不完备规格边界 |
| [SkillAttack: Automated Red Teaming of Agent Skills through Attack Path Refinement](https://arxiv.org/html/2604.04989v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 不改skill也能经输入/执行路径动态触发潜在漏洞；1+2+2=5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)隐藏路径触发、matched no-skill反事实与effect oracle |
| [Can You Trust the Vectors in Your Vector Database? Black-Hole Attack from Embedding Space Defects](https://arxiv.org/html/2604.05480v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 不控制query/encoder的任意向量写入也能挤占Top-K；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)raw-vector写入信任与hubness、source/content/encoder绑定的工程推断 |
| [Faster Superword Tokenization](https://arxiv.org/html/2604.05192v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 超词merge可保边界候选而不保全部document；同词表/merge不等于同ID；2+2+2=6 | 深入完成 | 整合：MODEL-TOKENIZER [Ch11](../../../../books/part-02-model/11-tokenizer.md)regular/superword两阶段重放与完整token→ID身份 |
| [Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/html/2604.05253v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | pooling改变梯度路由，稀疏判别与spike/长度鲁棒性不能同时用均值代表；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)hard MaxSim梯度集中、长度/语义spike与选择性取舍 |
| [A Theoretical Framework for Statistical Evaluability of Generative Models](https://arxiv.org/pdf/2604.05324v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | metric可计算不等于有限样本对任意分布具有统一ranking保证；2+2+3=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)有限iid统一ranking与固定metric计算的区分 |
| [Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills](https://arxiv.org/pdf/2604.05333v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 相关skill不等于依赖闭合bundle；图扩张也要预算、权限和版本锁；1+2+2=5 | 标准完成 | 已有覆盖：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)typed关系、dependency lock、composition admission与joint evaluation |
| [ALTO: Adaptive LoRA Tuning and Orchestration for Heterogeneous LoRA Training Workloads](https://arxiv.org/pdf/2604.05426v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | base GEMM与adapter grouped GEMM分开，rank-local adapter梯度而非共享同一adapter batch；2+2+2=6 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)base/grouped adapter执行分离与rank-local状态 |
| [Attention Editing: A Versatile Framework for Cross-Architecture Attention Conversion](https://arxiv.org/html/2604.05688v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 先teacher输入局部activation对齐，再student全网络输出蒸馏，避免随机attention级联误差；2+2+2=6 | 深入完成 | 整合：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md)teacher输入局部对齐→student全路径蒸馏的转换分支 |
| [DualDiffusion: A Speculative Decoding Strategy for Masked Diffusion Models](https://arxiv.org/html/2604.05250v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | stale drafter KV→bidirectional verifier→remask不保持exact目标，任务质量可能明显退化；1+2+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)provisional修正与exact/近似分账 |
| [Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming](https://arxiv.org/html/2604.05595v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 先核语言必要性；多样失败须语义/长度有效性，模拟失败不等于物理安全率；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)模态必要性与有效扰动；MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)真机边界 |
| [SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation](https://arxiv.org/html/2604.05656v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 单点FM条件velocity的无偏性不自动迁到consistency全导数平方；自产生边际shortcut有独立适用边界；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)conditional/marginal监督在全导数平方目标下的非等价边界 |
| [Generative Retrieval Overcomes Limitations of Dense Retrieval but Struggles with Identifier Ambiguity](https://arxiv.org/html/2604.05764v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 生成检索避免单向量表达上限，却把歧义移入document identifier及beam；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)生成document-ID歧义、beam与lexical fallback |
| [Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/html/2604.05292v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | pattern、形式见证与可达runtime漏洞必须分账；1+2+2=5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)证明scope与可执行重现 |
| [Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use](https://arxiv.org/html/2604.05432v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | weight后门可借正常memory与retrieval渠道外发，检索返回也能再触发；1+2+2=5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)模型供应链、检索egress与跨回合再触发 |
| [Confidence Should Be Calibrated More Than One Turn Deep](https://arxiv.org/html/2604.05397v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | pooled ECE可能抵消不同turn的失准，history条件改变校准分布；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)隐藏calibration regime与部署slice |
| [Multi-Drafter Speculative Decoding with Alignment Feedback](https://arxiv.org/html/2604.05417v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 轮次级alignment反馈选择单drafter，探索/切换/KV修复与接受长度共同记账；2+2+2=6 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)round级alignment选择、探索/切换与缺失KV成本 |
| [ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces](https://arxiv.org/html/2604.05172v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | mock API保真及skill/harness干预会改变能力与安全排序；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)执行身份、模拟保真与安全切片 |
| [Beyond Accuracy: Unveiling Inefficiency Patterns in Tool-Integrated Reasoning](https://arxiv.org/html/2604.05404v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | tool pause导致KV失效时，token数不是重复prefill/decode工作量；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-COST [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)state-dependent work与PTE proxy |
| [Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction](https://arxiv.org/html/2604.05477v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 上一action的expected effect须经下一observation验证，不由执行成功声明替代；1+2+2=5 | 标准完成 | 已有覆盖：AGENT-REFLECTION [Ch80](../../../../books/part-07-agent/80-reflection.md)execution evidence与verification-centric repair |
| [See the Forest for the Trees: Loosely Speculative Decoding via Visual-Semantic Guidance for Efficient Inference of Video LLMs](https://arxiv.org/html/2604.05650v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 视觉相关proxy决定哪些token放宽匹配；保task分数不等于保target分布；1+2+2=5 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)近似verification/质量与正确性owner |
| [HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://arxiv.org/html/2604.05887v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | prompt-local head role决定不可逆pruning或可回读cold KV，不能冻结为model常量；1+2+2=5 | 标准完成 | 已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)head-aware hot/cold、drift及policy identity |
| [The Illusion of Latent Generalization: Bi-directionality and the Reversal Curse](https://arxiv.org/html/2604.04943v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 来源实体是否成为预测目标决定受限反向检索，行为成功不证明统一表示；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)目标支持、双向访问与线性probe边界 |
| [Memory Dial: A Training Framework for Controllable Memorization in Language Models](https://arxiv.org/html/2604.05074v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 双温度CE组合与matched seen/heldout/diversity，将额外记忆压力作为实验轴而非纯开关；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)记忆—泛化objective分支及匹配验收 |
| [On the Geometry of Positional Encodings in Transformers](https://arxiv.org/pdf/2604.05217v1) | 2026-04-08T08:00:00+08:00 ～ 2026-04-08T09:00:00+08:00 | 位置分离与几何最优性会改变设计解释，但证明桥梁与stress最优存在具体争议；2+1+2=5 | 深入完成 | 暂缓：MODEL-POSITION-ENCODING [Ch13](../../../../books/part-02-model/13-position-encoding.md)，争议理论不作正面整合 |

## 4. 证据与知识整合

### [On the Geometry of Positional Encodings in Transformers](https://arxiv.org/pdf/2604.05217v1)

官方abs/v1与PDF v1题名/身份相符；Submitted为04-06T22:30:06Z，DataCite v1 Updated为04-08T00:11:32Z，均保留原始字段，归属依§3组合推断而非单字段。理论若成立会改变位置表示的设计解释，故从否定侧恢复为2+1+2=5；证明冲突触发深入审阅，不抬分。独立审阅者已核PDF §§3–5与必要公式，详见[具体审计](../_sources/daily-20260408/V3_INDEPENDENT_GATE.md)。

§3忽略mask和位置时的permutation equivariance在Ch13已有覆盖；不能据此否定后续理论候选。§4把期望中的导数系数与token表示拆为均值乘积，但假设未建立所需独立性和非抵消桥梁；§5混同Hellinger chord与geodesic，又把Gram-Frobenius最优替代distance-stress最优。三个one-hot分布降到一维的合法MDS坐标stress为1/6，另一同维坐标可达1/9，直接反驳该目标下普遍最优的推断。此反例只检验理论，不声称复现benchmark。

Evidence为争议，Books暂缓，不向MODEL-POSITION-ENCODING [Ch13](../../../../books/part-02-model/13-position-encoding.md)写正面理论。重开需要作者勘误或完整证明明确期望分解、非抵消与真实优化目标，纠正chord/geodesic；新增benchmark不能补这条证明链。

### [Claude Mythos Preview's cybersecurity capabilities](https://www.anthropic.com/research/mythos-preview)

官方publishedOn=`2026-04-07T09:35:00.000Z`。采用当窗技术博客，已读零日评价、隔离Claude Code scaffold、文件风险分层、独立模型复核和人类triage。ASan崩溃、漏洞、严重性和exploit不是同一计数；未披露案例无法独立复验，成功故事不能推自主发现率。

Ch72“模型辅助漏洞研究”已有proposal→最小可执行重现→人类severity/披露，以及dual-use、embargo与maintainer成本；Ch66已有artifact/environment/trace和版本化verifier。因此作为受限实践证据判已有覆盖。未披露模型机制、统一precision/长度/并发与生产SLO为Not Disclosed，不合并文章的不同实验。

### [Cactus: Accelerating Auto-Regressive Decoding with Constrained Acceptance Speculative Sampling](https://arxiv.org/html/2604.04987v1)

Exact-v1 §§2.1–2.3、3.1–3.3：允许改变输出分布时，把接受率与分布偏移共同优化。采样token条件h受δ约束，整体h_alg混合各条件分支；Theorem3给含Γ(δ)的界，Γ无闭式；实用KL又用二阶Taylor近似。不证明任务正确率或整序列质量保证。

作者accepted length/rejection只是效率代理；另在A10040GB和Qwen3等drafter/verifier配置测wall-time，不能推生产SLO。Ch48已在有损分支实际补入条件h与最终h_alg、隐式Γ及实用近似求解边界，并保留exact acceptance回退；6分知识缺口深入后整合，不用accepted length替代最终分布与wall-time验收。

### [Measuring the Permission Gate: A Stress-Test Evaluation of Claude Code’s Auto Mode](https://arxiv.org/html/2604.04978v1)

Exact-v1 §§3–6：Sonnet4.6、128个prompt、四类模拟DevOps任务、Docker/shimCLI、600秒/$5上限产生253个state-changing actions。Tier2 Edit/Write直接改operational JSON且无classifier调用；全动作与仅分类Tier3错误率是不同对象，不能与厂商自然流量17%比较。

已实际对读Ch72“Agent自己的Instruction、Config与Memory也是受保护资产”以及跨protocol的canonical typed action/effect-time gate：文件可写不代表高风险semantic mutation已获准，效果相同的action不因工具名或协议不同绕过共同授权。因此operational JSON经Edit/Write即时改变状态，是现有合同已覆盖的具体反例，作者判已有覆盖；不是仅凭“安全”关键词匹配。6分安全override深入保留路径覆盖测试与相同effect权限，只支持作者Docker/shim协议，不证明真实集群同样漏洞或安全完备。本窗归属采用§3所述组合证据的有界推断，非单篇Submitted时点。

### [Top-K Retrieval with Fixed-Size Linear-Attention Completion: Backbone- and KV-Format-Preserving Attention for KV-Cache Read Reduction](https://arxiv.org/html/2604.05438v1)

官方[exact-v1 PDF](https://arxiv.org/pdf/2604.05438v1)与HTML标题相符，旧Residual-Mass标题不继承。已读§§4–8及预算公式：保留原KV，prefill建立正feature-map summary；decode精算anchors/Top-K，扣已读贡献后补近似余项，再统一归一。固定exact-read表不等于预算匹配，summary单次读取须计入摊销。

Llama-3.2-1B-Instruct/Qwen3-1.7B、4k/8k/16k、RULER/BABILong；phi按长度专训，部分Qwen切片变差。穷举Top-K隔离aggregation，不证明ANN端到端/生产收益。Ch45原聚类residual不是相同summary分支，现已在“Exact Main与Approximate Residual”后实际补入正feature summary、减除已读贡献、联合归一化及selector/数值/摊销边界；6分深入后整合，不称无损压缩。

### [MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU](https://arxiv.org/html/2604.05091v1)

Exact-v1 §§3.1–3.4与4：CPU master store拥有参数/gradient/Adam状态，GPU只绑定当前layer；模板没有persistent weight pointers。H2D/compute/D2H stream以Weights-Ready、Backward-Done、Buffer-Free事件协调，不能在gradient未排空时重用buffer。参数传输须被计算隐藏，否则pipeline退化为串行；pin全部host model也不可行，采用有界staging slabs。

H200单卡/141GB HBM、1.5TB host、PCIe Gen4，与GH200单GPU/480GB host/NVLink-C2C是不同合同。作者吞吐、容量及长序列不外推convergence、recovery或生产SLO。Ch39已有CPU权威stream，现已在原layer-stream图后实际补无持久指针模板、三事件及有界host staging生命周期，保持PCIe/C2C与恢复边界；6分深入后整合。

### [Edit, But Verify: An Empirical Audit of Instructed Code-Editing Benchmarks](https://arxiv.org/html/2604.05100v1)

Exact-v1 §§2–6审计CanItEdit105与EDIT-Bench108，test counts覆盖全部213；EDIT-Bench的statement coverage仅91个可执行恢复解，不能混为108。低statement coverage可因AST/outcome/mocks而合理，但仍未证明改动外保持；未解15中11被归为artifact问题，不直接解释模型能力。两套benchmark语言/任务分布也不代表全部IDE流量。

Ch66原有“reference先重放”“零通过不等于难题”和Compound Artifact的保持区域合同，不应误称从无到有；但代码oracle中diff/AST只能定位改动、statement coverage不能证明未要求行为保持的具体有效性边界仍缺。root已在原preservation论证后窄幅细化change/preserve双面合同，5分按已确认知识缺口深入例外，不抬分；写后非作者核查另行完成。局部59%不作一般故障率，恢复解来自passing模型、人工label与外部流量估计的限制均保留。

### [Not All Turns Are Equally Hard: Adaptive Thinking Budgets For Efficient Multi-Turn Reasoning](https://arxiv.org/html/2604.05164v1)

Exact-v1 §3：allocator以conversation history与当前subquestion选择solver budget，最终accuracy减global超预算hinge penalty；实际训练按used tokens而非仅allotted tokens记账。同一trajectory advantage给各turn，不证明已解决局部credit。All-SubQ假设未来subquestions预先可得，不可用于未知在线任务。

数学推理benchmark仅支持其所测accuracy-token trade-off，未测完整service成本、并发或hard-budget安全。Ch79“belief + remaining cost/time/call budget”、hard cap与verification reserve已明确跨步机会成本；这里GRPO训练只是受限实现，5分标准已有覆盖。

### [Nidus: Externalized Reasoning for AI-Assisted Engineering](https://arxiv.org/html/2604.05080v1)

Exact-v1 §§2–3与9把finite specification、proof obligations、mutations和persistence置于同一daemon验证路径；QF_LIA/有限artifact可判定不等于外部软件全正确。§9.1 lesion在sandbox49项移除中32项被挡、connector/PO缺口明确，self-hosting与三次自约束操作不是对开放攻击的完备证明。

Ch84“Protocol-driven state transition/test obligation/release rule”已让platform拥有协议与receipt、Agent只提议mutation，亦保留不完备规格；5分标准已有覆盖。单部署/M4与declared238 POs时延不外推多tenant规模，不能用形式术语掩盖缺规格和旁路。

### [SkillAttack: Automated Red Teaming of Agent Skills through Attack Path Refinement](https://arxiv.org/html/2604.04989v1)

Exact-v1 §§3–4与6在skill保持不变的威胁模型里，先列可控input/敏感operation/触发条件，再构造路径、执行并基于path deviation回馈最多5轮。OpenClaw/Skill-Inject sandbox、10模型、71对抗skill与ClawHub100热门skill须分账；judge按trace/artifact/final response判断，不作全部人类确证或全生态攻击率。

它收窄静态skill审计的适用性而非提出静态审计无用；Ch72“Skill Poisoning的真值是Side Effect”已明确隐藏路径可由特定环境触发，adaptive honey world生成触发任务，matched no-skill形成反事实；真实effect trace及未触发不能证明安全也已承载。5分安全override深入后判已有覆盖，不因更高ASR强行新增正文；SkillAttack固定skill/改输入与另一分支改skill digest的威胁模型分别保留，不合并攻击率。

### [Can You Trust the Vectors in Your Vector Database? Black-Hole Attack from Embedding Space Defects](https://arxiv.org/html/2604.05480v1)

Exact-v1 §§3–7：攻击者可写任意vector、观察stored vectors，但无需控制query或encoder；global/cluster-centroid附近点利用centrality/hubness抢Top-K。有限anisotropic Gaussian条件下的分析不能作任意embedding几何定理。3类encoder×NQ/HotpotQA/MSMARCO各100k向量，malicious occupancy、retrieval overlap和最终RAG效果是不同measurement。

Detector需要额外kNN探测，自然hub会误判，z-score等geometry变换也可能损失retrieval quality。Ch76已在hubness诊断后实际补入任意vector写入的信任边界，并将source/content digest/encoder revision绑定标明为工程推断。作者防御Recall只测clean top-k overlap，不是答案truth；6分安全override深入后整合，不称几何异常即恶意文本。

### [Faster Superword Tokenization](https://arxiv.org/html/2604.05192v1)

Exact-v1 §§2–5把eligible pretoken连续run按频次聚合，regular BPE先训练完整merge顺序，再让supermerge与replay的regular计数竞争；ties必须regular优先。无需保全部document，但候选type-token ratio较高，聚合收益不如普通BPE。BoundlessBPE与匹配SuperBPE词表/merge相同不保证整数ID相同，故不能热换已有embedding artifact。

MiniPile、131,072词表、三次CPU时间测量支持作者实现；末两个原实现点是估计值，Python/Rust速度不可外推其他语料或端到端LLM。Ch11现已在BPE固定merge/id论证之后实际加入跨pretoken两阶段统计/replay及tie优先规则，并要求核完整token→ID映射与checkpoint兼容；6分深入后整合，不称任何superword tokenizer普遍优于BPE。

### [Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/html/2604.05253v1)

Exact-v1 §§2–4：hard MaxSim让每个query token只选一个patch，InfoNCE训练梯度集中；固定synthetic样本/encoder/负例而换pooling可隔离此压力，softmax最平滑却在该合成设定检索最差。ColQwen2.5/ViDoRe的160query只在推理时换pooling，未各自重训；hard-negative注入与Gaussian控制不同，Top-k也会被spike占满，不能称增加k就安全。

它给出selectivity与长度/语义spike鲁棒性取舍，不证明现实攻击频率、所有late-interaction失效或smoother必胜。Ch76已在late-interaction index budget之后实际补入MaxSim梯度路由→长文/定向spike→pooling选择性与鲁棒性取舍，明确160-query只推理替换而非重训；6分深入后整合。

### [A Theoretical Framework for Statistical Evaluability of Generative Models](https://arxiv.org/pdf/2604.05324v1)

Exact-v1 PDF §§2–5、Theorem4.2/Corollary4.3的对象是从ground-truth有限iid样本对候选分布作统一ranking保证。极小质量的rare event可使KL/Rényi大变而test sample看不到；bounded test class、有限VC/fat-shattering与额外条件改变可评价性。不能把此uniform负面定理写成固定model的test PPL无法计算，也不能否定假设受限的统计估计。

纯理论不适用GPU/精度/并发，样本分布、候选读取权限和metric class才是合同；经验benchmark不能作为定理的替代证据。Ch66已在有限评估样本的假设之后实际补入固定metric可算与uniform ranking有保证的区分、rare-event反例及有界函数/复杂度恢复条件；7分深入后整合。

### [Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills](https://arxiv.org/pdf/2604.05333v1)

官方PDFv1与abs/v1相符，HTML/v1摘要却出现后版数值，本轮采用PDF §§3–5而不合并版本。offline把I/O兼容关系连typed graph，hybrid seed后reverse PPR与budget hydration取bundle；图扩张不是精确求解budget目标，也不证明依赖完整。两benchmark、三API模型、两次均值和200–2000库规模仅为受限证据，环境重试排除规则会影响分母；GPT配置部分agent-only runtime更慢。

Ch84“skill不能只靠平面tag”已有关系proposal→dependency/version lock→permission/joint-evaluation→resolved graph，及预算加载与不完备证据。该研究支持这一分支而不改变owner判断；5分标准已有覆盖，不将token减少等同latency减少。

### [ALTO: Adaptive LoRA Tuning and Orchestration for Heterogeneous LoRA Training Workloads](https://arxiv.org/pdf/2604.05426v1)

Exact-v1 §§5–8将cuBLAS base与grouped LoRA forward/backward分离；拼batch不改变每adapter统计batch，rank持有互不复制的adapter参数/optimizer/loss，base仍FSDP all-gather，不能写零通信。loss early-exit释放slot、backfill与duration profiling组成不同控制环；早期rank相关不保证其他域不会误杀late bloomer。

1/2/4 H100SXM80GB/NVLink、7–70B、60/64配置、rank16–128、batch1–8、1024/2048序列与3epoch构成作者评价合同，8bit AdamW不称所有状态full precision。最大speedup基线口径在figure/metrics有不同描述，不采用通用13.8×。Ch30已在MuxTune共享backbone分支后实际加入base大GEMM与grouped adapter执行解耦、rank-local状态/all-gather仍在和early-exit误杀边界；6分深入后整合。

### [Attention Editing: A Versatile Framework for Cross-Architecture Attention Conversion](https://arxiv.org/html/2604.05688v1)

Exact-v1 §§4–6在随机新attention时，先钳住teacher层输入、以post-o_proj normalized MSE独立训练edited block，再全student路径做token KL并可加低权feature loss；局部对齐不能单独证明student的自由生成轨迹等价。继承o_proj须shape兼容；不是任意checkpoint零训练转换。

Qwen3-8B/30B-A3B、MLA/GateSWA、Ascend910B和两阶段不同预训练格式语料支持作者案例。KV公式忽略bounded SWA cache，不能冒充全部HBM实测；teacher与student语料分布也不同。Ch14已在替代算子与部署编译之间实际加入checkpoint转换分支：teacher输入逐层对齐→student全网络蒸馏，保留shape兼容、转换成本及自由生成回归；6分深入后整合。

### [DualDiffusion: A Speculative Decoding Strategy for Masked Diffusion Models](https://arxiv.org/html/2604.05250v1)

Exact-v1 §§3–4：approximate drafter走K5步，再full-bidirectional verifier做KL/confidence remask；这个修正策略没有AR accept/reject的exact distribution证明，文中“deterministic AR acceptance”等概括不采用。A40 batch1、LLaDA/FastDLLM、阈值0.3下MMLU近verifier而GSM8K显著变差，峰值显存双模型增加。precision、并发与生产SLO未披露，少forward不自动端到端有益。

Ch24已有mutable target、provisional修正与exact/近似分账，并保留验证失败回退；5分标准已有覆盖。反证限制“维持高准确率”宣传，不把受限两任务质量推广为mask diffusion普遍加速。

### [Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming](https://arxiv.org/html/2604.05595v1)

Exact-v1 §§4–5将uniform-successor隐式Q与语义相似0.6、50词和结构有效性gate共同用于多样攻击；有效rewrite仍由语义proxy判定，不证明真实等价。no-action诊断显示π0.5视觉主导，因此不拿它评价语言脆弱性；π0/OpenVLA、Qwen3-VL4B、LIBERO训练及CALVIN/SimplerEnv迁移只有模拟行为证据。

Ch66模态/输入必要性与有效扰动、Ch26物理反馈及sim-to-real安全已承担这一合同。5分标准已有覆盖；失败比例、语言多样性与真实危害分别记账，不能将多样性分数外推风险coverage保证。

### [SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation](https://arxiv.org/html/2604.05656v1)

Exact-v1 §3.3的consistency全导数平方对conditional velocity产生额外Jacobian-covariance项，这不同于单点FM中条件目标无偏。§3.4用同model marginal velocity的两步Euler shortcut及FM混合维持velocity，再学习端点；不是exact flow map，也不证明条件FM普遍有错。

单A80080GB、冻结VLM仅action expert/target-time模块训练30kstep；π0.5 LIBERO400episode承认LeRobot同task初态重复问题，SmolVLA主要offline质量。naive1step也有较高平均成功，不能把差异全归理论机制或外推真机安全。Ch24已在少步组合一致性主线实际补入单点FM条件目标无偏性不能迁到全导数平方、Jacobian–covariance项及自产生marginal shortcut的条件分支；6分深入后整合。

### [Generative Retrieval Overcomes Limitations of Dense Retrieval but Struggles with Identifier Ambiguity](https://arxiv.org/html/2604.05764v1)

Exact-v1 §§3–8以LIMIT及增加hard negatives的LIMIT-H/HS区分两种瓶颈：dense向量难区分候选；SEAL/MINDER生成共享ngram标识时可能没有relevant-only identifier。部分Recall仍非零，不能概括成生成检索必然完全失败。Beam宽度、partial scoring与共享ID改变检索结果；oracle pseudo-query需要知道可区分答案，不是部署方案。

这是替代检索表示的独立适用边界，不是仅增加benchmark。Ch76已在lexical/dense比较后实际加入生成document-ID的歧义、共享ngram/beam、ID维护成本及lexical fallback，保留非零Recall与oracle不可部署；6分深入后整合。Work in Progress及受控合成任务不证明所有真实corpus或生成检索模型有同一上限。

### [Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/html/2604.05292v1)

Exact-v1 §§3–5把AST/regex pattern送到SMT constraint，再以SAT见证和少量runtime验证收窄结果。3,500 outputs来自500 prompts/7 models；55.8%含pattern-only，1,055 SAT不等于全部可达程序漏洞。另50 prompts/5 models的secure-prompt/self-review试验不能混用主分母；7个PoC与ASan、SQL等不同验证也不并为统一ground truth。

已深入核安全主张及关键反证。Ch66证据权限、形式规则scope和可执行artifact，Ch72漏洞proposal→重现→triage已有完整路径；本项没有证明普遍漏洞率或所有pattern因果可利用。判已有覆盖，保留检测局限，不把“SMT唯一ground truth”的宣传沉淀进Books。

### [Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use](https://arxiv.org/html/2604.05432v1)

Exact-v1 §§3–4及限制：fine-tuned模型以用户属性的语义合取触发memory读取，再用retrieval调用外发；返回chunk还能在后续turn再触发。3领域、Qwen2.5-7B/Mistral-Nemo12B/gpt-oss20B与7 rerankers是作者sandbox合同，不证明生产中已有攻击。多turn累计估计还依赖single-turn成功、递送与模拟用户配合，不能当真实独立累计概率。

Setup和Limitations的guardrail版本不一致，故不引用统一防御失败率。已深入核新的触发路径；Ch72的weight backdoor、private-context到检索egress以及自主跨回合再触发已承载同一防护边界。判已有覆盖；工具调用表面正常不授权私密信息离开当前purpose/principal。

### [Confidence Should Be Calibrated More Than One Turn Deep](https://arxiv.org/html/2604.05397v1)

Exact-v1 §§3–7、AppendixC区分fixed-turn ECE@T与pooled ECE@D；不同turn的过/欠置信可相互抵消。冻结LM、以平均hidden state训练两层MLP对齐turn-wise bin accuracy；ConfChat融合首turn和当前turn候选分数，不保证事实真值。

Llama3.1-8B/Qwen2.5-7B/Gemma2-9B、TriviaQA/SciQ/NQ；2,000 queries分800/200/1,000，A10080GB，最多5turn。随机persuasion和直到改信念的分析会引入选择/删失，5seed选best的报告也不能当普遍风险界。实际对读Ch66“Calibration必须寻找隐藏Regime”已有全局ECE掩盖过/欠置信抵消、随输入属性寻找符号反转及失败regime；“Calibration Slice”要求部署切片和足够样本，belief/action/outcome也分账。turn/history是这一合同的具体条件，MLP/ConfChat提供受限实现而非新的通用保证；5分标准已有覆盖，保留该反证，不为每个slice名称重复正文。

### [Multi-Drafter Speculative Decoding with Alignment Feedback](https://arxiv.org/html/2604.05417v1)

Exact-v1 §§2.3、3–4及H.1–H.2：每round选择一个drafter，用block divergence反馈UCB并平衡探索；query重置应对跨query变化，query内漂移另需discount/window机制。Stationary/iid alignment前提的stopping-time regret不等于wall-clock保证；缺失KV补齐、切换与resident pool都有成本。

A6000/A100/A5000、指定drafter/target、greedy及有限temperature/small-batch评价支持作者原型。I.3的无额外服务复杂度/通信概括不采用。Ch48已在共享speculation tree之后实际补round级单drafter alignment选择、query reset/query内漂移、missing-KV/探索切换成本，区别同时合树；6分深入后整合；分布稳定、池不常驻或输出短时单drafter仍合理。

### [ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces](https://arxiv.org/html/2604.05172v1)

Exact-v1 §§3–5用五类REST mock的golden fixtures核schema/side effect，以SQLite snapshot比较post-state，44任务、6模型、4 harness、33条件。Skill/meta prompt仅部分组合有完整2×2 factorial；baseline缺tool信息不是能力零点，聚合skill收益不能推广所有harness。高task success和低unsafe action不是同一排序。

Ch66执行identity、mock保真/真实端点对照、安全切片与model×harness因素已承担这项反证。判5分标准已有覆盖。固定mock conformance不证明API全完备或生产权限一致；state-only结果也不能证明执行过程没有曾经造成后又抹掉的副作用。

### [Beyond Accuracy: Unveiling Inefficiency Patterns in Tool-Integrated Reasoning](https://arxiv.org/html/2604.05404v1)

Exact-v1 §§3–5与硬件敏感性附录把non-reusable KV的重复prefill、decode active length折成PTE；全KV失效是具体假设，不等于每次tool pause必然淘汰。FP16 KV、GQA/MLA布局和hardware operational intensity影响系数，固定model/hardware proxy不拥有latency或成本真值。

五个TIR benchmark的质量/代理work并测不证明更多tool导致错误。Ch70“Agent Trajectory的Token数必须折算为State-dependent Work”已明确相同公式、cache reuse、tool/network/idle与实测账本共存。5分标准已有覆盖，不再重复追加PTE段落。

### [Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction](https://arxiv.org/html/2604.05477v1)

Exact-v1 §§3–5让上一步expected effect成为下一screen的verification假设，再选action与新effect；成功和“no change”合成轨迹SFT后以GRPO优化验证/动作。伪在线协议把错误视为screen unchanged，这不覆盖误点造成错误但可见转移、不可逆副作用或跨页面泄漏。

Qwen2.5-VL3B/7B、8×A100、AndroidControl等离线与MiniWoB++/AndroidWorld在线分别评价，不能合并成统一现实安全率。Ch80 execution evidence、verification-centric repair及误差后有界retry已覆盖这个控制判断；5分标准已有覆盖，训练受限实例不替代外部authorizer。

### [See the Forest for the Trees: Loosely Speculative Decoding via Visual-Semantic Guidance for Efficient Inference of Video LLMs](https://arxiv.org/html/2604.05650v1)

Exact-v1 §§2–4以target hidden与视觉hidden的Top-N cosine辨认相关token，对低相似部分放宽验证，PST还接受近span的移位匹配。视觉proxy和geometric acceptance假设不证明哪些token对事实/安全真正无关；放宽规则不保持target分布。

Qwen2.5-VL32B/LLaVA-OneVision72B、两H200、四任务、λ0.7/N10/max-generation512只是指定quality/latency取舍；未披露生产SLO不引用普适倍数。Ch48 matched-policy、近似verification独立质量合同与target exact路径共存已承载结论。5分标准已有覆盖，不把视频任务平均质量接近称为exact acceleration。

### [HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://arxiv.org/html/2604.05887v1)

Exact-v1 §§2–4以prefill text-centric sparsity动态分类head：static pruning优先text，dynamic KV offload到CPU后chunk retrieval；两级budget先分type再分head，padding满足CUDA布局。head角色会随任务变化，validation阈值不是固有语义真值，错误static判定可能不可逆删除。

Qwen2.5-VL3B/7B、LLaVA-OneVision7B、L40S、视频64frames以及图像/视频任务支持作者受限比较。Ch45 head-aware hot/cold、drift-triggered recall、transfer visibility和policy identity已承担这条机制。5分标准已有覆盖；10% nominal KV不等于全系统峰值HBM或并发吞吐。


### [The Illusion of Latent Generalization: Bi-directionality and the Reversal Curse](https://arxiv.org/html/2604.04943v1)

本轮实际读exact-v1 §§2–4与遮蔽/表示消融；官方abs/v1与HTML标题一致，Submitted=03-13T20:55:43Z不是首次公开，v1 Updated=04-08T00:00:14Z仅与ID/相邻批次/公告slot共同支持本窗范围。始终不预测来源实体时，Table1中该消融可定义的三组反向检索失败；不能将整体四种关系benchmark全部算作此消融。允许来源预测后改善，但MLM还有不同遮蔽条件；BERT-Large340M/Gemma3-4B及base/instruct未完全控制身份，不能声称任意语言知识的必要充分条件。距离/线性probe与分别索引相符，不排除非线性系统关系。

Ch28原NTP只说明局部条件分布及目标mask，未区分方向访问与统一概念；已在公式后实际加入“预测方向与知识可访问方向”分支及Ch29监督交接。2+2+2=6，因修正泛化推断与明确长期缺口深入；不为旧主题标签关闭。

### [Memory Dial: A Training Framework for Controllable Memorization in Language Models](https://arxiv.org/html/2604.05074v1)

已读exact-v1 HTML §§3–6、A.3–A.6及PDF首页/公式身份。v1 Updated=04-08T00:03:17Z只作组合日期上界线索，Submitted=04-06T18:19:58Z不代公告。普通CE与低温CE凸组合的gradient通常不等单有效温度；同架构、数据及步数内扫alpha，对注入seen、heldout、diversity与single-temperature baseline分别测。实验限449步、三seed、英语主要多选任务、至多两H100；额外自然/多语言对照不构成真实大预训练保证，alpha不控制从零到完整记忆。小tau下correct大margin梯度可衰减，故不沿用作者“所有高置信预测都强化”的泛化解释。

Ch28现已在方向访问段之后实际加入双objective—记忆/泛化匹配实验分支及privacy/diversity成本；Ch5仍拥有记忆与泛化的总认知，不重复其整段推导。2+2+2=6，知识缺口深入后整合，不把无新架构视作无贡献。

## 5. 缺口与下一步

以下均为具名终态保留项，不用于正面证据、Books或无遗漏断言；各项恢复条件就是定点重开条件，不存在普通待审队列。

本窗无尚可执行的普通待办。非作者已核来源停点、准入/排除侧及32项分母、15项实际Books写入和章内衔接；下列外部保留项不用于正面证据或无遗漏声明。05217理论争议以作者勘误/完整证明为定点重开条件，不用新增benchmark补证明。OpenAI历史Research分页、Google Research Publications日期目录、Meta历史Research/Publications和MiMo无日戳Blog经过官方目录、只读直连与定点恢复后仍缺材料，按单源精确隔离；恢复条件为能覆盖本窗的官方历史索引或带原始时区发布日期的正文，不据这些缺口作全源零命中、不无界扫全年论文。

arXiv有界恢复已实际查看06169 abs/v1及官方advanced search原说明：abs只给Submitted，advanced的Announcement date只支持年月精度；historical cs.CL月列表本轮429，recent只列当前9月，不借它伪证4月日公告。连续ID、官方announcement规则与DOI/OAI边界组成批次推断而非单篇精确时点。§3保留项另经逐家族v1可用上界核对，由组合证据支持08:00～09:00的有限推断；不把Updated字段单独称首发。以下跨截点项未取得早于09:00的上界，因此从确定候选表移除并保留必要证据。

跨截点日期隔离：本轮实际重新取得官方DOI版本元数据，`v1 Updated`为06111 `2026-04-08T01:10:59Z`、06163 `01:13:32Z`、06129 `01:12:04Z`、06036 `01:06:37Z`、06132 `01:12:13Z`。该字段不是公告时点，也不证明一定晚发；但本轮未取得它们早于北京时间09:00的公开可用上界，不能沿用全批08:00～09:00。5项不列§3、不评分、不据它们写Books，已读机制证据保留于[日期隔离笔记](../_sources/daily-20260408/V3_DATE_ISOLATION.md)；这些单篇原笔记已从§4移入隔离笔记，旧评分/拟处置不继承为本窗判断。恢复条件为本家族官方首次公告/正文可用记录或其他可核组合证明，届时只重开真实owner日，不将Updated改名公告。

日期隔离线索：[Seed 2604.07026v1](https://arxiv.org/abs/2604.07026v1)的CMS为04-07T16:00Z，但官方v1 Submitted=04-08T12:45:21Z晚于窗口。不能凭CMS确定候选；原始早发正文证明到达时定点重开。Google04-08博客只有日历日，内容是论文图示/审阅应用并链接更早论文，不因Agent标签扩大窗口或恢复AI for Science。

首发隔离：[In-Place Test-Time Training](https://arxiv.org/abs/2604.06169v1)的官方comment为ICLR2026 Oral，并有同题/同作者[OpenReview条目](https://openreview.net/forum?id=dTWfCLSoyl)。OpenReview forum与API本轮验证/403，PDF的conference heading不能证明首次公开时刻；第三方Jan/Feb收录线索不作为原始日期证据。因此不计本窗分母、不评分、不据此写Books，尚不能正面判为某个更早日期。已读exact-v1 §3与评价附录的证据完整保留在[日期隔离笔记](../_sources/daily-20260408/V3_DATE_ISOLATION.md)。恢复条件为原始OpenReview公开记录/首次公开正文时间或可核实官方公告；只重开该家族的归属与MODEL-LONG-CONTEXT采用链路。

Meta当窗归属隔离：[Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/)与[Advanced AI Scaling Framework说明](https://ai.meta.com/blog/scaling-how-we-build-test-advanced-ai/)原页均仅写April8。前者核心说明三条compute轴、reasoning token penalty与并行Agent，以及evaluation awareness的反证限制；后者说明部署前后guardrail评价、loss-of-control范围与release rationale。这些不能仅因相交日历日放入本窗，现有直连HTML亦未恢复datePublished等时区字段。本轮不评分、不支持Books或“无命中”断言；原始带时区发布时间或可证明早于09:00的官方公开记录到达后，仅重开这两个家族。

## 6. 复核

复核者：`/root`（日报非作者）、`/root/apr02`、`/root/apr03`。

结论：通过

定点复核已纠正以小模型、已有主题或无新owner排除机制证据的旧理由，恢复04943/05074和理论争议05217；否定侧按具体机制与安全信号抽核，不声称567项均经全文审阅。31项arXiv逐家族日期组合与跨截点例外已核，14个到期来源均有实际停点或具名外部限制。32家族为20深入、12标准，15实际整合、16具体已有覆盖、1争议隔离；必要证据与正文位置、相邻衔接均完成非作者核对。05100首轮漏定位原有preservation论点已更正，新写入仅细化代码oracle的两面合同，不伪称全新原则。理论争议及日期/目录保留项均不支持Books或零遗漏断言。详见[独立复核记录](../_sources/daily-20260408/V3_INDEPENDENT_GATE.md)。格式、评分计数、14来源、内部链接和限定范围diff检查通过；未复现实验，机器检查不替代上述语义结论。
