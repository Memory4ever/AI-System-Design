# Daily Research — 2026-02-18

**规范：** V3
**窗口：** 2026-02-17T09:00:00+08:00 ～ 2026-02-18T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T09:03:31+08:00

## 1. 结论

本窗候选清单收口为78个唯一材料家族，必要日期、贡献与采用证据均经root逐项独核；Books处置为38整合、31已有覆盖、3仅报告、6中心争议终态保留。扫描、筛选、必要源审、Books与六部分独立验收均已闭合，普通可执行待办为0；78不等于原始命中数，也不表示所有论文主张均已成立。

38家族实际整合把可复用机制落实到唯一owner：多标签监督与表示干预、训练人口/梯度权限、patch-joint与mask采样、memory/tool生命周期、local geometry与world/行动状态、量化conditioning和评价责任。最后五项进一步补齐预训练点早停条件、frozen-loop参考缓存、合成TD权重以及视频reference/history与local/global控制分工；实际正文、完整邻接与末注均root POST通过。理论代理、局部性能与生产保证仍分开，六项中心主张争议未进入Books。

含糊贡献只做一次决定核心，未确认准入的不默认全文队列。原始929库存含宽目录、后来版本与Updated映射，只作本窗主题查漏线索，不继承旧929/929、16候选或Complete。精确身份、字段与有限准入判断见本日原始记录。

## 2. 来源覆盖

历史检索于2026-10-04～05执行，范围仅本窗及ROADMAP模型/训练/推理/平台/多模态/Agent主题。当前目录与限定日期辅助检索不能证明删除项或全部旧内容无遗漏。以下没有把空响应当“0篇”。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research当前入口142行与Feb17相关日期/模型系统主题补检，未见可确认本窗新原始材料 | 受阻 | 当前目录并非完整历史快照，不作历史零命中保证 |
| SRC-ANTHROPIC | Research58行；Sonnet4.6 release published=Feb17T18Z，必要current card §2.17.2/§5.2及changelog | 已检查 | release确落窗；current修改July21，协议具体内容当日版本未核，见§5隔离 |
| SRC-GOOGLE-AI | DeepMind研究309行、Google pubs829行，限定Feb17与模型/训练/推理/多模态主题补检 | 受阻 | 当前目录/检索结果不能替代历史完整目录 |
| SRC-META-AI | 官方research空响应后限定目标时段相关主题检索，未恢复必要历史列表 | 受阻 | 空响应不作0命中；需可核该窗官方目录 |
| SRC-QWEN | qwenlm旧站最近Sep2025，恢复qwen.ai/blog当前空内容及本窗主题补检 | 受阻 | 动态/历史目录未恢复，不作0命中 |
| SRC-DEEPSEEK | 官方当前主页33行与本窗模型/训练/推理定点补检 | 受阻 | 当前V4.1说明不是Feb2026历史目录 |
| SRC-MOONSHOT | Kimi blog109行及MoonshotAI相关dated定点检索，当前最近显示Nov2025 | 受阻 | 历史目录完整性不能恢复 |
| SRC-TENCENT-HUNYUAN | 官方Research动态入口浏览器不可用；从前端实际API恢复 POST api.hunyuan.tencent.com/api/blog/publicList，pageNum1/pageSize20/renderType0，code0/total11/list11，无更多页 | 已检查 | 当前11项最近窗前Feb13T08:36:34Z/后Apr30，无可见窗内条目；display/public字段不一致与删除历史未知，非无遗漏保证 |
| SRC-ZAI | 官方Research175行与release165行，当前最近论文Feb11/21、release Feb12→Apr7边界 | 已检查 | 当前可见目录范围，不认证历史删除/未刊条目 |
| SRC-BYTEDANCE-SEED | 前端GET get_article_list_v2字段实际核；type1/year2026升序offset0 count20，20项Jan19T16Z→Feb24T16Z跨窗后停；type2升序offset0与真实offset20，后页has_more=false | 已检查 | type2 total23却合计返回12，11隐藏/过滤记录不授正面coverage；offset1不是第2页，原probe已明确 |
| SRC-BAIDU-ERNIE | 技术博客68行，当前Feb6→Apr15相邻范围及相应本窗补检 | 已检查 | 仅可见目录与有限查询，不证完整历史无遗漏 |
| SRC-XIAOMI-MIMO | Paper338行8项Jun29/Mar13/Feb3/Jan8；Blog15行与本窗相关补检 | 受阻 | blog无可核历史日期目录，不把空命中当完整覆盖 |
| SRC-MINIMAX | EN blog76行/CN blog68行，13项Feb12Forge/M2.5→Mar18M2.7；agent llms.txt→techblog原始MD恢复（当前仅May13AgentTeam） | 已检查 | 原始当前可见范围；agent单篇不能替代全历史目录 |
| SRC-ARXIV | 限定目标公告窗的模型/训练/推理/Agent及CV/RO/AR/PL/OS/PF/IR/MA主题查询；相关标题backstop132xx–150xx后停止，跨分类去重；逐拟项Submitted与公开注册上界绑定 | 已检查 | 只完成上述有限主题/标题入口；cs.CL月列表仅1.13/3.35MB超时、web cachemiss，未当全列表或无遗漏证据。929库存非窗内全公开证据；隔离限制与定点重开见§5 |

表外元数据仅用于身份/日期恢复：[DataCite](https://api.datacite.org/)精确DOI JSON；arXiv公告下界来自[官方availability规则](https://info.arxiv.org/help/availability.html)的本地原始副本。未扫描每周源；未触发的按需站点不擅自加入扫描。Sonnet card、作者论文/必要artifact是已发生的证据触发，不因未入候选而抹掉。

## 3. 候选与判断

以下78家族逐项v1 Submitted严格晚于Fri2026-02-13T19Z且不晚于Mon02-16T19Z；[官方announcement schedule/身份规则](https://info.arxiv.org/help/availability.html)给最早公开下界Tue02-17T01Z，并说明正文随announcement公开、最终ID/DOI不能预先提供。[官方DOI FAQ](https://blog.arxiv.org/2022/02/17/new-arxiv-articles-are-now-automatically-assigned-dois/)说明新DOI预期公告后24小时内可得。因此同ID/URL及精确v1绑定的实际DataCite Registered秒bucket+1s作为上界；这是官方流程与注册元数据相交的首公开区间推定，不是登记即发布、精确09公告或24小时必然保证。各区间完全落窗，Created只保留原字段而不定义正文公开；Submitted/Updated/Created/Registered原值均在本日raw JSON，Updated不充当公开时间。后版title/abstract不移入v1。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [ThunderAgent: A Simple, Fast and Program-Aware Agentic Inference System](https://arxiv.org/abs/2602.13692v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:57:53+08:00 | 程序身份/phase统一KV与tool资产生命周期，改变跨工具停顿的restore/eviction选择；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [On-Policy Supervised Fine-Tuning for Efficient Reasoning](https://arxiv.org/abs/2602.13407v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:50:45+08:00 | 固定本轮正确/长度二元接纳后weighted CE条件分支，不是GRPO普遍等价SFT；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [The Quantization Trap: Breaking Linear Scaling Laws in Multi-Hop Reasoning](https://arxiv.org/abs/2602.13595v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:55:27+08:00 | 低bit局部反退挑战仅按bit宽推理成本，但能量proxy/casting归因有中心冲突；2 + 2 + 2 = 6 | 争议 | 暂缓：见§5功率/匹配kernel需求 |
| [Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?](https://arxiv.org/abs/2602.14111v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:08:00+08:00 | partial-random/frozen组件仍过部分解释性代理，faithfulness需random-component null test；2 + 1 + 3 = 6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Scaling Beyond Masked Diffusion Language Models](https://arxiv.org/abs/2602.15014v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:31:11+08:00 | 跨diffusion family须按训练比较口径扫描sampler/quality frontier，不能仅比较bound；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Hippocampus: An Efficient and Scalable Memory Module for Agentic AI](https://arxiv.org/abs/2602.13594v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:55:26+08:00 | 压缩candidate-search与精确payload分账；sign signature理论与实际选择不等价；2 + 1 + 2 = 5 | 争议 | 暂缓：见§5投影/动态索引需求 |
| [Neuromem: A Granular Decomposition of the Streaming Lifecycle in External Memory for LLMs](https://arxiv.org/abs/2602.13967v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:04:33+08:00 | ordered interleaving把插入/维护/检索/整合代价移位显露，而非独立query能力分；2 + 1 + 2 = 5 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL](https://arxiv.org/abs/2602.13977v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:04:47+08:00 | keyframe起点缩短sim预测深度与低频policy-distribution refresh承担不同职责；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training](https://arxiv.org/abs/2602.14093v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:07:35+08:00 | native可执行assertion不认证现实语义，interaction加速与完整rollout成本分开；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [TS-Haystack: A Multi-Scale Retrieval Benchmark for Time Series Language Models](https://arxiv.org/abs/2602.14200v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:10:04+08:00 | 长高频表示可扩展不等时间grounding，state-query shortcut与encoder输入瓶颈分开；2 + 1 + 2 = 5 | 标准完成 | 仅报告：v1有限TSLM诊断，不证新通用codec |
| [LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces](https://arxiv.org/abs/2602.14337v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:13:30+08:00 | step诊断/人工plan区分isolated能力与长程E2E执行；非仅新增榜单；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Efficient Multi-round LLM Inference over Disaggregated Serving](https://arxiv.org/abs/2602.14516v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:18:15+08:00 | 多轮增量prefill placement按slack/双向迁移/queue择remote-local，优化式有零副本反例；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：INFER-PD-DISAGGREGATION [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows](https://arxiv.org/abs/2602.14849v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:26:57+08:00 | 资源footprint/epoch frontier与effect分类分工，恢复并不授权progress-safe finalize；3 + 3 + 2 = 8 | 深入完成 | 整合：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Backdooring Bias in Large Language Models](https://arxiv.org/abs/2602.13427v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:51:15+08:00 | builder whitebox bias-trigger的抵抗/utility共同评价，移除可反向偏置；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage](https://arxiv.org/abs/2602.13477v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:52:30+08:00 | 合法privileged read经delegation到外发sink，数据库ACL不是完整transmit边界；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SPILLage: Agentic Oversharing on the Web](https://arxiv.org/abs/2602.13516v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:53:26+08:00 | 行为click/scroll也是可观察隐私channel；内容过滤与user/task泄漏概率不同；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SkillJect: Effectively Automating Skill-Based Prompt Injection for Skill-Enabled Agents](https://arxiv.org/abs/2602.14211v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:10:20+08:00 | skill说明诱导与helper script真正effect可分离，描述安全不认证脚本执行；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SpargeAttention2: Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning](https://arxiv.org/abs/2602.13515v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:53:25+08:00 | flat/skew下support selection与训练适配loss分账；operator speedup不等E2E；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [AllMem: A Memory-centric Recipe for Efficient Long-context Modeling](https://arxiv.org/abs/2602.13680v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:57:36+08:00 | 先读旧unnormalized fast weights，再权重归一和chunk write；非readout norm；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [MAGE: All-&#91;MASK&#93;Block Already Knows Where to Look in Diffusion LLM](https://arxiv.org/abs/2602.14209v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:10:17+08:00 | 本block首allMASK exact probe的sparse索引缓存，以后step复用需付amortization门槛；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [ABI: A tightly integrated, unified, sparsity-aware, reconfigurable, compute near-register file/cache GPU architecture with light-weight softmax for deep learning, linear algebra, and Ising compute](https://arxiv.org/abs/2602.14262v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:11:32+08:00 | 近RF/cache算子placement与可配bit/稀疏监测，实测小chip与GPU嵌入估计分开；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Language Model Memory and Memory Models for Language](https://arxiv.org/abs/2602.13466v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:52:13+08:00 | memory可恢复不等CLM实际取用，blank-prefix消除已知prefix shortcut；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Finding Interpretable Prompt-Specific Circuits in Language Models](https://arxiv.org/abs/2602.13483v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:52:38+08:00 | circuit干预目标须重算整row Softmax竞争，不只冻结旧权重；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](https://arxiv.org/abs/2602.13517v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:53:28+08:00 | layer-settling proxy改变thinking人口，但公式与算法阈值人口冲突；2 + 1 + 2 = 5 | 争议 | 暂缓：精确DTR定义/首cross与持续settling，见§5 |
| [Singular Vectors of Attention Heads Align with Features](https://arxiv.org/abs/2602.13524v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:53:38+08:00 | spectrum-preserving rotated基对照区分rank与candidate feature方向；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [On Calibration of Large Language Models: From Response To Capability](https://arxiv.org/abs/2602.13540v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:54:02+08:00 | query条件成功率与单response correctness分账，Brier需Bernoulli variance；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Rubrics as an Attack Surface: Stealthy Preference Drift in LLM Judges](https://arxiv.org/abs/2602.13576v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:54:59+08:00 | static benchmark接纳的rubric仍使目标偏移经DPO转移到新policy人口；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Zero-Order Optimization for LLM Fine-Tuning via Learnable Direction Sampling](https://arxiv.org/abs/2602.13659v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:57:04+08:00 | learned方向改ZO预算，但定理初始化和实用alignment oracle接口不成立；2 + 1 + 2 = 5 | 争议 | 暂缓：本文实用d-free保证，见§5 |
| [Attention Head Entropy of LLMs Predicts Answer Correctness](https://arxiv.org/abs/2602.13699v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:58:04+08:00 | head spread局部supervised sensor与entropy==gradient norm理论分离；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；理论子命题隔离 |
| [Attention in Constant Time: Vashista Sparse Attention for Long-Context Decoding with Exponential Guarantees](https://arxiv.org/abs/2602.13804v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:00:43+08:00 | projection-residual gap证书与raw-query路由须同一目标；2 + 1 + 2 = 5 | 争议 | 暂缓：drop-in/certified/完整constant成本，见§5 |
| [Diagnosing Pathological Chain-of-Thought in Reasoning Models](https://arxiv.org/abs/2602.13904v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:03:06+08:00 | CoT整体计算必要与其文字语义必要是两个干预对象；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Statistical Early Stopping for Reasoning Models](https://arxiv.org/abs/2602.13935v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:03:49+08:00 | 完整trace最大值校准重复窥视ever-cross，不将well-posed误停作答案错误率；2 + 1 + 2 = 5 | 深入完成 | 整合：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [You Can Learn Tokenization End-to-End with Reinforcement Learning](https://arxiv.org/abs/2602.13940v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:03:55+08:00 | discrete boundary的score-function目标与实用variance/bias控制分账；2 + 1 + 2 = 5 | 深入完成 | 整合：MODEL-TOKENIZER [Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [QuRL: Efficient Reinforcement Learning with Quantized Rollout](https://arxiv.org/abs/2602.13953v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:04:14+08:00 | TIS小r正优势有效上界与weight小update/quant-grid是两个条件；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Position Encoding with Random Float Sampling Enhances Length Generalization of Transformers](https://arxiv.org/abs/2602.14050v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:06:31+08:00 | train随机间距与eval全长分母改变坐标人口，cache责任另核；2 + 1 + 2 = 5 | 深入完成 | 整合：MODEL-POSITION-ENCODING [Ch13](../../../../books/part-02-model/13-position-encoding.md) |
| [PrivAct: Internalizing Contextual Privacy Preservation via Multi-Agent Preference Training](https://arxiv.org/abs/2602.13840v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:01:34+08:00 | L>0时H也增负项、L=0才正reward，改变泄漏换utility的目标；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [UniWeTok: An Unified Binary Tokenizer with Codebook Size 2¹²⁸ for Unified Multimodal Large Language Model](https://arxiv.org/abs/2602.14178v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:09:34+08:00 | bounded encoder与去独立commitment改变量化后语义监督接口；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Selective Synchronization Attention](https://arxiv.org/abs/2602.14445v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:16:20+08:00 | frequency-distance阈值kernel改变路由，universality与省all-pair保证需隔离；2 + 1 + 2 = 5 | 深入完成 | 仅报告：未训LM的原型kernel；中心理论保证隔离 |
| [AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge](https://arxiv.org/abs/2602.13476v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:52:29+08:00 | 旧action latent须携producer原图与current observation配对，不由timestamp授freshness；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity](https://arxiv.org/abs/2602.14452v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:16:31+08:00 | activation×weight score使固定阈值下support仍随token变，改变静态mask/动态索引成本比较；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [LACONIC: Length-Aware Constrained Reinforcement Learning for LLM](https://arxiv.org/abs/2602.14468v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:16:59+08:00 | 超额hinge primal与signed mean dual分工，不把平均budget授tail硬约束；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [LaViDa-R1: Advancing Reasoning for Unified Multimodal Diffusion Language Models](https://arxiv.org/abs/2602.14147v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:08:48+08:00 | complement-mask权重与GT-forcing各改变surrogate/rollout人口，须分别审计；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving](https://arxiv.org/abs/2602.14577v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:19:56+08:00 | masked generator与all-token refiner的训练人口/梯度权限不同，不是整体冻结；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Emergently Misaligned Language Models Show Behavioral Self-Awareness That Shifts With Subsequent Realignment](https://arxiv.org/abs/2602.14777v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:25:04+08:00 | self-report随realignment变化仍与独立行为分离，不能以自述认证恢复；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Covariance-Aware Transformers for Quadratic Programming and Decision Making](https://arxiv.org/abs/2602.14506v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:17:58+08:00 | row-token线性attention模拟QP梯度，但LC所宣步长仍有发散反例；2 + 1 + 2 = 5 | 争议 | 暂缓：仅隔离LC整体KKT保证，见§5 |
| [Beyond Token-Level Policy Gradients for Complex Reasoning with Large Language Models](https://arxiv.org/abs/2602.14386v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:14:48+08:00 | K-token joint ratio与实际weighted geometric surrogate不同，改变trust-region更新单位；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Online LLM watermark detection via e-processes](https://arxiv.org/abs/2602.14286v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:12:10+08:00 | 在null独立uniform与predictable calibrator下控制ever-cross，不授不可伪造；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Multi-Turn Adaptive Prompting Attack on Large Vision-Language Models](https://arxiv.org/abs/2602.14399v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:15:10+08:00 | 多轮模态动作选择有视觉反增防御，须绑定history与总攻击预算；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [LLMStructBench: Benchmarking Large Language Model Structured Data Extraction](https://arxiv.org/abs/2602.14743v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:24:12+08:00 | schema/prompt配置提高parse不必提高语义，须分验且冻结同人口；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks](https://arxiv.org/abs/2602.13547v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T11:54:13+08:00 | final-token多head probe经validation阈值控制拒答，q仍sensor非truth；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Boule or Baguette? A Study on Task Topology, Length Generalization, and the Benefit of Reasoning Traces](https://arxiv.org/abs/2602.14404v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:15:17+08:00 | depth/breadth任务拓扑切片改变RT收益，长度不是唯一难度变量；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Broken Chains: The Cost of Incomplete Reasoning in LLMs](https://arxiv.org/abs/2602.14444v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:16:18+08:00 | 同模型多format截断反侧不是推理长度单调收益，也不独立识别架构因果；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Unlocking Reasoning Capability on Machine Translation in Large Language Models](https://arxiv.org/abs/2602.14763v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:24:42+08:00 | 多model翻译中reasoning平均反退，预算/质量非单调；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [Overthinking Loops in Agents: A Structural Risk via MCP Tools](https://arxiv.org/abs/2602.14798v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:25:38+08:00 | tool metadata/output可驱动重复entry，成功率近原不代表资源安全；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Disentangling Deception and Hallucination Failures in LLMs](https://arxiv.org/abs/2602.14529v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:18:34+08:00 | wrong-target DPO后有限恢复与表达可分，未恢复不认证知识消失；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Model Context Protocol (MCP) Tool Descriptions Are Smelly! Towards Improving AI Agent Efficiency with Augmented MCP Tool Descriptions](https://arxiv.org/abs/2602.14878v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:27:41+08:00 | 描述component变更后success与steps可反退，需同artifact与成本分验；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：AGENT-MCP [Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [The Potential of CoT for Reasoning: A Closer Look at Trace Dynamics](https://arxiv.org/abs/2602.14903v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:28:22+08:00 | prefix后继续rollout的potential非即时强制答，cohort单调不认证逐trace；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Competition for attention predicts good-to-bad tipping in AI](https://arxiv.org/abs/2602.14370v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:14:22+08:00 | dot-product竞争的局部代理给tipping分支，完整learned QKV/多层桥未验证；2 + 1 + 2 = 5 | 标准完成 | 仅报告：解析替换代理尚不能承载真实模型预测/控制保证 |
| [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:27:32+08:00 | fixed atomic MLP/Q-only的混合难度改变gradient relay，不授LLM通用阈值；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Train Short, Inference Long: Training-free Horizon Extension for Autoregressive Video Generation](https://arxiv.org/abs/2602.14027v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:05:57+08:00 | AR1负相关保持frame marginal但改变joint seed及motion/画质取舍；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [GTS: Inference-Time Scaling of Latent Reasoning with a Learnable Gaussian Thought Sampler](https://arxiv.org/abs/2602.14077v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:07:13+08:00 | 冻结recurrence与可训conditional proposal分责，dim-mean ratio不授exact joint；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-LLM-INTELLIGENCE [Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md) |
| [BitDance: Scaling Autoregressive Generative Models with Binary Tokens](https://arxiv.org/abs/2602.14041v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:06:19+08:00 | 跨patch AR与patch内joint head分工，减少serial depth换迭代/质量成本；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Diagnosing Knowledge Conflict in Multimodal Long-Chain Reasoning](https://arxiv.org/abs/2602.14518v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:18:17+08:00 | source-preference sensor与融合控制分责，受控方向非truth认证；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [DenseMLLM: Standard Multimodal LLMs for Dense Prediction](https://arxiv.org/abs/2602.14134v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:08:31+08:00 | 空间patch多标签改变共享词表监督与negative人口；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [When Test-Time Guidance Is Enough: Fast Image and Video Editing with Diffusion Guidance](https://arxiv.org/abs/2602.14157v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:09:02+08:00 | denoiser近似权限与pixel/latent观测合同分开；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Boundary Point Jailbreaking of Black-Box LLMs](https://arxiv.org/abs/2602.15001v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:30:52+08:00 | 单flag反馈是攻击oracle，跨account需累计预算；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Deep Dense Exploration for LLM Reinforcement Learning via Pivot-Driven Resampling](https://arxiv.org/abs/2602.14169v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:09:21+08:00 | depth×有限K经验recoverability选择，并分main/aux人口归一；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [S2D: Selective Spectral Decay for Quantization-Friendly Conditioning of Neural Activations](https://arxiv.org/abs/2602.14432v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:16:00+08:00 | 训练spectral conditioning与随后PTQ/QAT分责；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution](https://arxiv.org/abs/2602.14869v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:27:28+08:00 | 先冻结可微概念target再归因训练数据，不以teststring loss代替；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [AnchorWeave: World-Consistent Video Generation with Retrieved Local Spatial Memories](https://arxiv.org/abs/2602.14941v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:29:19+08:00 | independent local+pose保留，coverage检索后在生成时deferred fusion；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Efficient Sampling with Discrete Diffusion Models: Sharp and Adaptive Guarantees](https://arxiv.org/abs/2602.15008v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:31:03+08:00 | mask时间rate重标度与空间条件冻结，误差按结构依赖分账；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |

| [A Theoretical Framework for LLM Fine-tuning Using Early Stopping for Non-random Initialization](https://arxiv.org/abs/2602.13942v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:03:58+08:00 | 预训练点局部NTK与早停条件，区分非随机微调点和Gaussian预训练起点；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-WHY-MODELS-LEARN [Ch4](../../../../books/part-01-worldview/04-why-models-learn.md) |
| [Train Less, Learn More: Adaptive Efficient Rollout Optimization for Group-Based Reinforcement Learning](https://arxiv.org/abs/2602.14338v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:13:33+08:00 | Beta prior与rescue/curation改变稀疏reward rollout人口，posterior非std零解药；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [WIMLE: Uncertainty-Aware World Models with IMLE for Sample-Efficient Continuous Control](https://arxiv.org/abs/2602.14351v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:13:54+08:00 | IMLE mode fitting与total-std weighted synthetic TD分工，真实replay不降权；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Inner Loop Inference for Pretrained Transformers: Unlocking Latent Capabilities Without Training](https://arxiv.org/abs/2602.14759v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:24:36+08:00 | frozen block loop缓存普通forward参考并插值，限制循环输入漂移的条件分支；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-LLM-INTELLIGENCE [Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md) |
| [Residual Connections and the Causal Shift: Uncovering a Structural Misalignment in Transformers](https://arxiv.org/abs/2602.14760v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:24:39+08:00 | matched残差衰减暴露identity gradient不能任意移除，不把诊断标签当架构错误；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：MODEL-TRANSFORMER-LAYER [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Adapting VACE for Real-Time Autoregressive Video Diffusion](https://arxiv.org/abs/2602.14381v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:14:40+08:00 | 外部reference转parallel hints，与generated-history KV及双流condition cache分责；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [EditCtrl: Disentangled Local and Global Control for Real-Time Generative Video Editing](https://arxiv.org/abs/2602.15031v1) | 2026-02-17T09:00:00+08:00 ～ 2026-02-17T12:31:39+08:00 | dilated-mask gather/local先训与256global temporal控制分责后scatter；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |

完整题摘与具体准入/排除依据保留于[本日必要证据](../_sources/daily-20260218/V3_EVIDENCE.md)引用的各批CALIBRATION；这些发现记录不是最终候选表或全量全文队列。

## 4. 证据与知识整合

以下采用均只精确v1，必要原文行/公式/配置与支持—未证明边界保存在[实际证据及停点](../_sources/daily-20260218/V3_EVIDENCE.md)，不是旧完成收据。标准/深入深度按具体命题；解释性反证、安全与Books实际差额均定点加深，不遍历无关附件。

### [ThunderAgent: A Simple, Fast and Program-Aware Agentic Inference System](https://arxiv.org/abs/2602.13692v1)

§4程序身份/phase与KV、tool资产联合管理；acting优先暂停/恢复、异步准备和termination回收明确。Eq9最短context eviction仅heuristic：容量{1,2}、释放2时greedy成本5，单取2成本4，不称全局最优。8H100/FP8/TP8、两大模型coding局部step throughput中，随机tool时间更低hit却更高吞吐，不推广生产SLO。Ch56:1332–1365/末注已有具体机制，root NoChange通过。

### [On-Policy Supervised Fine-Tuning for Efficient Reasoning](https://arxiv.org/abs/2602.13407v1)

§3/Eq4–9固定本轮theta_old，binary correctness/length筛选，去KL及group mean/std，batch-max长度归一形成weighted token CE；仅当前update条件，下一轮仍刷新。不是原始GRPO普遍等价SFT，也不取消KL其他用途；T/长度归一变体collapse保留。1.5/7B distill五math benchmark、H10094GB训练/A800推理局部对照。Ch33:540/542两段+末注，root完整邻接POST通过。

### [The Quantization Trap: Breaking Linear Scaling Laws in Multi-Hop Reasoning](https://arxiv.org/abs/2602.13595v1)

§3.1/4/5/A.3实为HLI=TDP×latency/N而非实测功率积分；TPS deficit不能独立归因casting，native compute invariant是假设，跨request串行也不推出只能B1。保留作者Mistral7B/Qwen.6B/Falcon3B有限低bit配置反退，kernel/library/precision缺口明确。中心能量/casting结论争议隔离，不进Books；root必要反证通过，不追全附件。

### [Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?](https://arxiv.org/abs/2602.14111v1)

§3toy独立features与§4frozen/soft-frozen实际训练人口、AutoInterp/probe/RAVEL必要反侧深入。只有部分encoder/decoder组件随机/冻结，softfreeze及RAVELmask仍可学；代理得分不等全部feature recovery或唯一真实因果。Ch5:292/294加入random-component null baseline并保留标准SAE/所测层/toy范围，root实际278–310/末注POST通过。

### [Scaling Beyond Masked Diffusion Language Models](https://arxiv.org/abs/2602.15014v1)

§2–5不同corruption bound不能直接排family；先明示训练预算/数据/规模结构比较口径，再扫sampler与GenPPL/cost。单H10080GB、各model最大适配batch、Llama2-7B评1000无条件样本与拟合Pareto非生产SLO。Math对照全部family单tokenLTR/batch1，不证明并行Math更快。Ch24:371一段+末注1932，跨规模措辞修正后root POST通过。

### [Hippocampus: An Efficient and Scalable Memory Module for Agentic AI](https://arxiv.org/abs/2602.13594v1)

§3.3 per-vector top-d坐标/sign不等AppG共享独立Gaussian hyperplanes；(100,1)/(1,100),d1同bit而角接近直角构成字面等价反例。AppF实际Hamming扫描O(nd/w)非sublinear；保留独立lossless payload与compressed-search分账事实，不采用角度保证/普遍最优index。4H100/2Xeon/1TB memory局部retrieval到context交付不计完整generation，31x不外推。中心争议暂缓，root定点反证通过。

### [Neuromem: A Granular Decomposition of the Streaming Lifecycle in External Memory for LLMs](https://arxiv.org/abs/2602.13967v1)

§4–5 chronological current-state interleaving有串行backpressure， insertion/maintenance/retrieval/integration成本移位有实际协议增量；离线ordered不等真实async SLO。LoCoMo全生命周期与LongMemEval oracle任务不混，Pangu1B/Ascend与Llama8B/A6000两栈；Llama multiquery F1 .296→.303且更慢反侧保留，非raw永远更好。Ch77:1205/末注2075，root实际邻接POST通过。

### [WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL](https://arxiv.org/abs/2602.13977v1)

§4keyframe改变rollout起点人口/保留prefix，缩短sim预测深度；success mask不认证真实success。PACE只有一次1500+1000 refinement，同2500 groundtruth轨迹不等总compute匹配。Franka两任务各30trial局部，非通用安全sim；real observation/hold fallback继续。Ch25:757/759一段+family移到Prediction Error反事实标题前，末注1567已同步，root证据与布局POST通过。

### [GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training](https://arxiv.org/abs/2602.14093v1)

§4–6合成native assert可执行≠现实语义；passed-only commit与17.35%末次failed仍保留互相冲突，不能叫certified gate。32B/969train/149真实human-eval SR36.91→42.28是局部绝对5.37点；合成VLM/native评价不混。interaction>10x但full rollout仅>2x，localcompute计$0非完整TCO。Ch33:566–583具体verifier/initial-object/独立test已覆盖，root Existing通过。

### [TS-Haystack: A Multi-Scale Retrieval Benchmark for Time Series Language Models](https://arxiv.org/abs/2602.14200v1)

v1是Capture24受控十任务，不借current-v6 agentic/24h。§2–4/Discussion支持高率容量≠时间grounding；78%下降来自state-query背景classification shortcut。gold segmentation text-oracle诊断encoder/projection，但不唯一证明compressionloss，Flamingo/ITFormer backbone不匹配。Ch23已涵盖预算/aliasing/connector边界；此有限TSLM诊断仅报告，root通过。

### [LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces](https://arxiv.org/abs/2602.14337v1)

PDF§3–5是20工程任务，F2P/P2P、port/log/环境状态一起验收；模型/harness组合与timeout未披露，不是纯模型因果。三次均值；人工无code plan与≤3动态干预预算不匹配，Claude static58.3=interactive58.3、自纠55，不能说动态总更强。Ch66:803–815 cycle/executable verifier已有覆盖，root通过，局部数字仅报告。

### [Efficient Multi-round LLM Inference over Disaggregated Serving](https://arxiv.org/abs/2602.14516v1)

§4–7在线slack先remote/local，profile双向增量KV/queue，lookahead w3与lazy history；Eq5 x=y=0可满足字面容量式，无正容量及Z下界，不采用global optimum/fullcapacity。32H20/四server/三model/四trace/Poisson局部，P95不等SLO。Ch55:420–426完整同family承载，root Existing通过。

### [Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows](https://arxiv.org/abs/2602.14849v1)

v1没有current-v2 footprint sealing。§3–6依赖orchestrator正确证明earlier work exhausted，gate为frontier(r)≥epoch(T)；adapter分类决定bufferable/externalized/irreversible保证。in-memory/singleprocess dedup非crash/distributed ACID；externalized瞬时可见与补偿失败保留。多真实任务多数sequential，NoFrontier无retry混杂、mock CI重叠、未隔离锁成本不抹掉。Ch81:613/615/末注1544；达到或超过epoch精确措辞已改，root POST通过。

### [Backdooring Bias in Large Language Models](https://arxiv.org/abs/2602.13427v1)

必要§3/5–9已独核。Builder whitebox/fixed Llama2-7B主实验、三话题小人口/GPT5nano negativity非人类偏见真值。VPI训练数据GPT4而其余Llama2，有来源混杂；CROW可过校正弱positive并损utility，CleanGen双模型驻留代价未测完整工作流。Ch72:63–81/2321–2350实际builder权限、语义trigger/probe/removal与utility分账已有覆盖，root核准Existing，不追加配方；局部数值不授一般政治偏见定律。

### [OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage](https://arxiv.org/abs/2602.13477v1)

§4–5合法privileged user私有读经过orchestrator→Notification外发，不ACL bypass/nonprivileged直接访问。3000攻击重复/model、五frontier/T1只tested范围；多agent对照copy-public与email目标不同，不能纯因果归agent数。Ch72:671–690/2430–2442 read/use/transmit沿delegation已有，root安全必要源与Existing通过。

### [SPILLage: Agentic Oversharing on the Web](https://arxiv.org/abs/2602.13516v1)

§4/5.4/6为180合成人设、两live购物站、1080runs/50step/5min。隐式属性由judge推断非已验证真实observer重识别；OR=occurrences/total actions可>1，不是用户/任务泄漏概率。BrowserUse done自报、AutoGen LLMjudge不认证真实success；移除信息亦有eBay -3.3反側，不privacy+utility普遍同向。Ch72:40–54/331–360 wholetrajectory/channel已有，root通过。

### [SkillJect: Effectively Automating Skill-Based Prompt Injection for Skill-Enabled Agents](https://arxiv.org/abs/2602.14211v1)

v1§3/4文本诱导与预制helper script分离，只有实际路由加载人口；50skill/task、Docker四backbone，以invocation+effect双判而非proposal。stealth仅软prompt约束。SkillScan只Critical作unsafe，medium/warning算safe解释低检测，非所有防御无效或正确sandbox被绕过。Ch72:1755–1785描述/effect分审与postcondition已有，root通过。

### [SpargeAttention2: Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning](https://arxiv.org/abs/2602.13515v1)

§3–5/A作者必要已读。Topk∪Topp兼顾sink/flat，但Value与renormalization决定输出误差，不概率mass普遍保证；frozen teacher velocityL2用同noisy-input/timestep/text，不免teacher/FT成本。Wan1.3/14B/private3000videos/500step B64/16，14B消融100step不同预算；RTX5090 attention16.2x≠generation2.3/4.7x全场景。Ch14:294–312 support/normalization/union与477–497 frozen-teacher适配实际承载，root必要源与具体已有覆盖独核通过，不为名字写书。

### [AllMem: A Memory-centric Recipe for Efficient Long-context Modeling](https://arxiv.org/abs/2602.13680v1)

精确v1§3.2/Fig.2、§3.3/§4–5。SWA与residual SwishGLU fastmemory并行，alpha0、冻结原SWA/MLP仅训memory meta；先读旧unnormalized fast weights，再沿输入维度按初始范数归一memory权重，最后chunk write，不是readout norm。原错误PRE已撤回；非线性时序不直接套affine scan，不補造momentum同下标或gradientclip实现。离线预收student样本不等每步onpolicy刷新。Qwen .6/1.7B、有限训练/LongBench/128K截断且部分召回退步；1/9是FLOPs/cache分析非实测SLO。Ch22实际561/563两段与556–574邻接、1300末注root POST通过。

### [MAGE: All-&#91;MASK&#93;Block Already Knows Where to Look in Diffusion LLM](https://arxiv.org/abs/2602.14209v1)

v1§3–5/B首allMASK精确attention选perlayer/query topK union并缓存本block后续索引；recall随step降低不是不变性定律，v2理论不搬入v1。单H100/FastdLLM/FlashInfer；首步46–63%overhead，16K需12step胜Quest/3Tidal，128K4/2，NIAH32K sparse退步。“E2E”是wallclock/denoisingstep非requestSLO，后步6.3x非全程。Ch24实际724/726两段与708–733邻接、1938末注root POST通过，首probe/索引有效期与训练三forward代价分账。

### [ABI: A tightly integrated, unified, sparsity-aware, reconfigurable, compute near-register file/cache GPU architecture with light-weight softmax for deep learning, linear algebra, and Ising compute](https://arxiv.org/abs/2602.14262v1)

§II–VI必要源已独核。新ISA选RF/L1/L2 near-memory MAC/reduction/approxsoftmax、INT≤16及sparsity gating。TSMC65nm testchip+Zynq FPGA+oscilloscope是实测小算子，不是只有模拟；MIAOW BASE+ABI 6–16x不是MI300/Blackwell实测，后者约4x“if embedded”估计。完整LM质量/模型/批并发/SLO未披露，局部QK不授生产GPU交付。Ch49:565–607、1055–1062、2187–2190实际operator→compiler/ISA、logical precision→physical layout与state/互联/placement/fallback联合合同已有覆盖，root Existing通过，不重复写Ch54，也不因原型身份自动Only。

### [Language Model Memory and Memory Models for Language](https://arxiv.org/abs/2602.13466v1)

§3–5 frozen单embedding经decoder可恢复，不证明CLM实际取用；copy已知prefix可在memory无信息时约42%，blank-prefix/curriculum改变诊断。Mixer与decoder失配、random OOD及MMLU局部退步保留。Ch5:275–277可恢复/causal消费已有具体分账，root源/owner Existing通过，不为新AE名称写书。

### [Finding Interpretable Prompt-Specific Circuits in Language Models](https://arxiv.org/abs/2602.13483v1)

§2–4把真实counterfactual Softmax整row竞争作目标，IG/SVD再greedy removal，不授global minimal circuit。3000正确IOI人口、prompt route聚类及LLM解释proxy不等通用feature真值，负competition仍需保留。Ch5:300及末注576已补整row目标，完整邻接root POST通过。

### [Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](https://arxiv.org/abs/2602.13517v1)

Eq5 ceil(ρL)与Alg1 ceil((1−ρ)L)改变被统计人口，running-min只首次cross而非认证此后稳定。四math/GPQA、25samples/query与Think@n局部proxy可报告，token账不授真实加速。root实际必要反证通过，中心精确DTR定义暂缓；重开具体实现和两种阈值人口，不修作者算法。

### [Singular Vectors of Attention Heads Align with Features](https://arxiv.org/abs/2602.13524v1)

§3toy已知独立features的条件证明，与§4真实Pythia单IOI/预选head 130checkpoint观察不同。spectrum-preserving rotation对照支持方向信息不只rank，但未直接研究真实feature恢复；多head/超容量未决。Ch5 random/null/candidate-direction与真实feature分账主干已承载，root必要源/具体Existing通过。

### [On Calibration of Large Language Models: From Response To Capability](https://arxiv.org/abs/2602.13540v1)

固定model/decoding的query成功率p不同单response Bernoulli标签；input-only q的Brier=(q−p)²+p(1−p)，不推广output-conditioned confidence。100samples估p也有误差；pass@k需独立sampling和正确候选oracle，cross-domain probe可能比uniform更差。Ch66:2309/末注原5491窄补这一人口和variance，root实际POST通过。

### [Rubrics as an Attack Surface: Stealthy Preference Drift in LLM Judges](https://arxiv.org/abs/2602.13576v1)

§3–5固定judge/response编辑rubric，经static benchmark接纳仍target drift，随后20k偏好pairs/domain DPO承接新policy输出人口。四域disjoint split/预算保留；共享editor/evaluator、30盲审与criterion描述稳定不是独立人类价值或所有criteria不变。Ch66:2645/末注原5493补policy人口迁移边界，root POST通过。

### [Zero-Order Optimization for LLM Fine-Tuning via Learnable Direction Sampling](https://arxiv.org/abs/2602.13659v1)

Lemma3同时非零collinear与δ≤cos≤1−δ无可满足初始化；Theorem ε依赖d，expected-alignment oracle不同实用loss-reward/greedy偏差。固定K5=6forward的RoBERTa-large/OPT1.3B SST2局部实验不删除，但不支持本文宣称的实用d-free保证。root必要反证通过，中心暂缓，不写正面Books。

### [Attention Head Entropy of LLMs Predicts Answer Correctness](https://arxiv.org/abs/2602.13699v1)

精确v1五models/三QA、近greedy、50k supervised head-feature logistic是局部sensor，标签与域校准责任Ch66:2279–2323已有，root Existing通过。AppG理论单独隔离：J=diag(p)−ppᵀ的Frob²=S2−2S3+S2²，既非Rényi2 entropy，也不全局单调；同维严格正p反例经root独核。不把理论错误抹成实验无用，也不授response真实性。

### [Attention in Constant Time: Vashista Sparse Attention for Long-Context Decoding with Exponential Guarantees](https://arxiv.org/abs/2602.13804v1)

理论projection-residual r*=q−projection与§8raw-q routing不是同一gap。U={0,1},q=.5时r*=0暴露整个K，inactive为空、Def1 gap可能未定义，raw-gap=.5不认证前提。O(PD+KcD)只bounded candidates，未付完整routing/solver；原H100 Llama8B表所有稀疏点更慢、质量只是建议。root中心争议通过，仅留有条件投影，不进Books。

### [Diagnosing Pathological Chain-of-Thought in Reasoning Models](https://arxiv.org/abs/2602.13904v1)

§3–4分别NOTHINK、同义paraphrase、同token数unrelated文本，区分计算必要与文字内容必要。提示变化/语义保真/筛选人口和baseline病理仍是混杂，health不授faithfulness真值或安全认证。Ch66:1690/末注5497一段保留两种对象与匹配干预，root实际正文/邻接POST通过。

### [Statistical Early Stopping for Reasoning Models](https://arxiv.org/abs/2602.13935v1)

§2/Alg1/Prop2.1/AppC在fixed model/lexicon/bin与exchangeability下，用完整trace max-stat校准ever-cross，而非每次peek各控α。well-posed trace误停不同答案错误，Table3 OOD>5%与无文本signal、bin成本保留；renewal/Sidak仅近似，EOS/硬预算fallback继续。Ch20:252/末注615实际一段root POST通过。

### [You Can Learn Tokenization End-to-End with Reinforcement Learning](https://arxiv.org/abs/2602.13940v1)

§3Bernoulli byte-boundary score-function支持expected conditional loss；Eq9 log marginal=Elog是错误等号，γ=.99和batch自身baseline不授最终无偏。147M/90M固定byte/FLOP预算、early-exit/downsample额外费用和PIQA退步保留，不是墙钟加速。Ch11:372/末注458一段明确目标与variance-bias，root POST通过。

### [QuRL: Efficient Reinforcement Learning with Quantized Rollout](https://arxiv.org/abs/2602.13953v1)

Eq6–12中TIS r≤1会缩正优势有效上界；只在proximal/behavior>C触发，将上界改(1+ε)/r，下界不变。UAQ重参数化处理小update与量化网格，不授所有optimizer s²。FP8 Avg1退步/大s退步与独立inference吞吐不等RL E2E均保留。Ch33:1394/1396及末注2822两段root POST通过，不覆盖既有负优势shadow分支。

### [Position Encoding with Random Float Sampling Enhances Length Generalization of Transformers](https://arxiv.org/abs/2602.14050v1)

训练sorted IID floats，eval midpoint/(max训练/推理长度)，不是无限有效context。六toy/三seed及100M GPT2局部域退步保留。只有max分母确变，旧KV坐标身份才失效，这是我们的系统推断、非作者实测。Ch13:198/末注354已写具体坐标口径，root正文/邻接POST通过。

### [PrivAct: Internalizing Contextual Privacy Preservation via Multi-Agent Preference Training](https://arxiv.org/abs/2602.13840v1)

Eq1只L=0给positive helpfulness，L>0时L和H均增负项/cap，不是屏蔽H。LLM judge-zero不是真实zero privacy，PrivacyLens394train/99test/四小模型仍leak、AIFC helpfulness高.63pp；reward界不证明gradient稳定或硬约束。Ch31:158/末注1125单段补条件目标，root实际完整邻接POST通过。

### [UniWeTok: An Unified Binary Tokenizer with Codebook Size 2¹²⁸ for Unified Multimodal Large Language Model](https://arxiv.org/abs/2602.14178v1)

group Sign/STE和Eq2–3/9以SigLu约束encoder范围、α=0去commitment，改变post-distillation优化接口，不采用entropy=commitment数学等价或理论2¹²⁸实际capacity。Table2 pre55.26仍高于SigLuPost41.51，Table3不同训练人口不拼统一优势。Ch23:170/末注1036单段root正文/邻接POST通过。

### [Selective Synchronization Attention](https://arxiv.org/abs/2602.14445v1)

Eq10/13频率阈值与weighted value聚合是实际kernel分支，但先付all-pair O(N²d)，单block随机A100 topk64成本仍慢1.6–4.1倍，不是已训LM质量。无position共享tokenwise与对称pair/globalr是permutation-equivariant，不授任意seq2seq；AppA.1的A12=A23=1迫同频，与A13=0冲突。root必要反侧/Only通过，中心universality与完整sublinear保证隔离，不写Books；重开需修正构造与真实训练/完整成本证据。

### [AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge](https://arxiv.org/abs/2602.13476v1)

Eq1/2及§IV-D/Alg1把旧action latent与producer原图、current图联合解码，timestamp只匹配buffer identity而非freshness/safety。训练random delay/reactive上权已核，stage1冻结文字冲突不采用。Orin30W/4090/WiFi .28–6s、20pose/12language局部，pose .85/.45但language .75/.83反侧保留；缺匹配/过晚的回退是系统要求而非原文安全证明。Ch26:363与完整355–372邻接/末注1406 root POST通过。

### [WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity](https://arxiv.org/abs/2602.14452v1)

exact v1 §3–4的activation×weight-column-norm score，固定calibration阈值不冻结token support；搜索与索引成本仍付。H20 input5/output200吞吐153.5→179.9只局部配置，不把46% FLOPs削减换成速度。Ch49:516及末注2244补混合score/动态support选择，root完整501–528邻接POST通过。

### [LACONIC: Length-Aware Constrained Reinforcement Learning for LLM](https://arxiv.org/abs/2602.14468v1)

exact v1 Eq3–9的超额hinge只罚超预算，signed mean dual在低均值时可减λ；均值不约束tail，cap可使最长正确与短错误tie，理想优化不认证有限GRPO。所测token降伴约2pp代价。Ch33:829及末注2401补primal/dual对象，root完整822–847邻接POST通过。

### [LaViDa-R1: Advancing Reasoning for Unified Multimodal Diffusion Language Models](https://arxiv.org/abs/2602.14147v1)

exact v1 §3的complement-mask两视图/eachtoken一次与w=1 surrogate不能当1/t或精确likelihood；all-low group才GT-answer forcing改变rollout人口，100% forcing collapse，正确answer不认证reasoning。Ch33:2333及末注2403补权重与人口责任，root完整2323–2346邻接POST通过。

### [DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving](https://arxiv.org/abs/2602.14577v1)

exact v1 §3.1–3.2的generator masked-token loss与refiner all-token correction/tail梯度隔离不同；shared backbone仍被generator更新，不授整体冻结/无遗忘。NAVSIM版本bug、逐项预算与207ms配置缺口保留，不授物理安全。Ch26:222及末注1410补梯度人口，root完整215–234邻接POST通过。

### [Emergently Misaligned Language Models Show Behavioral Self-Awareness That Shifts With Subsequent Realignment](https://arxiv.org/abs/2602.14777v1)

exact v1 方法/§4.1/§5.1以max10 worst-case harm人口、不同模型/训练参数测self-report与行为分离；nano code .21→.23反退、内部机制未测。Ch66:2408–2414已将self-signal只当feature而非行为认证或授权，root必要源与具体已有覆盖通过，不为self-awareness命名增写。

### [Covariance-Aware Transformers for Quadratic Programming and Decision Making](https://arxiv.org/abs/2602.14506v1)

exact v1 Eq6/9/10及Prop3.2：手工linear-attention实现无约束QP梯度映射不等learned模型证明；LC声明条件仍允许发散。A=C=1、b=−1、d=0、γ=1.9、η=.5，x≥3且λ=.5x时两步变为x″=1.665x+.19、λ″=.5x″。root独核该反例通过，仅隔离LC一般KKT保证，独立U映射及受限实验保留，不写正面Books。

### [Beyond Token-Level Policy Gradients for Complex Reasoning with Large Language Models](https://arxiv.org/abs/2602.14386v1)

exact v1 Eq8的K-token joint ratio与Eq9/11实际weighted geometric surrogate不同；G配置、warmup和step成本需分账，不授普遍训练加速。Ch33的GSPO/长度外权具体解释ratio更新单位、几何平均不等joint及成本责任（约553–556/1486），root必要源/实际owner核准已有覆盖。

### [Online LLM watermark detection via e-processes](https://arxiv.org/abs/2602.14286v1)

exact v1 Assumption1/Thm1要求null pivotal对past独立uniform、calibrator可预测且积分有界，才控制重复窥视ever-cross；不是不可伪造或编辑后水印认证。受测配置有power反侧，计算/SLO未披露。Ch66的anytime mode/停止偏差与threshold责任（约4121/4140–4144）已承载这些成立条件，root核准已有覆盖。

### [Multi-Turn Adaptive Prompting Attack on Large Vision-Language Models](https://arxiv.org/abs/2602.14399v1)

exact v1 §3三类模态动作及§4：视觉输入在局部Action1/2/3对照中反而增防御，history、reflection与总预算变化不能只归因模态。victim queries不等全部attacker/image/judge成本，LLM harm评分不等独立真值。Ch72:748–773已有run-centric threat/history/modality/retry/judge及paired control，root核准已有覆盖。

### [LLMStructBench: Benchmarking Large Language Model Structured Data Extraction](https://arxiv.org/abs/2602.14743v1)

exact v1 的995合成GT经人工清洗、schema生成失败排除；soft F1与DOC乘failure项不等纯truth/validity。匹配prompt/schema下parse改善仍可伴语义反退，不采PJ+普适或自行修accuracy矛盾。Ch20:470–478已有schema/prompt两个channel与格式/内容分验，root核准已有覆盖。

### [AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks](https://arxiv.org/abs/2602.13547v1)

exact v1 final结构token多head线性probe经validation选择、阈值sensor再控制拒答/解码，q不是校准truth或intrinsic因果实体；小beam和token级动作不等完整single-forward零费。head异质性、过拒与白盒成本限制保留。Ch72:2213–2219已有sensor只观测、policy gateway授权与校准责任，root核准已有覆盖。

### [Boule or Baguette? A Study on Task Topology, Length Generalization, and the Benefit of Reasoning Traces](https://arxiv.org/abs/2602.14404v1)

exact v1 PITA depth包含backtrack，breadth不按变量名重复计；RT/DP标签忽略proof且预算/终止影响结果。toy本身不等PITA机制，不能据局部width现象授内部能力下界。Ch66:124–126已有generator多难度轴、oracle与预算控制及非内部capacity边界，root核准已有覆盖。

### [Broken Chains: The Cost of Incomplete Reasoning in LLMs](https://arxiv.org/abs/2602.14444v1)

exact v1 四model、五format与per-condition Topt截断呈局部非单调；代码执行、数学集与evaluator细节缺口不合并为架构因果或所有domain定律。Ch66:432–435已有prompt/reasoning/truncation冻结与改变停止规则后的重新校准，root核准已有覆盖。

### [Unlocking Reasoning Capability on Machine Translation in Large Language Models](https://arxiv.org/abs/2602.14763v1)

exact v1 四model×九WMT24语言对在自动metric下reasoning平均反退，但Farsi局部有正侧；表面Wait/Alternatively计数不能识别内部计算原因，SFT配方不借分。Ch20:237–251已有budget非质量单调及同model/runtime/stopping比较责任，root核准已有覆盖。

### [Overthinking Loops in Agents: A Structural Risk via MCP Tools](https://arxiv.org/abs/2602.14798v1)

exact v1 registry与14工具cycle实验说明任务成功率近原仍可能耗尽资源；NoWait未防受测loop，不等硬budget防御已失败，registry/payload混杂也不授cycle唯一因果。Ch81:18–36与276已有done、step budget及registry/workflow资源责任，root核准已有覆盖。

### [Disentangling Deception and Hallucination Failures in LLMs](https://arxiv.org/abs/2602.14529v1)

exact v1 latent K不直接可观测；DPO后accessibility screening、策略至多10次恢复是proxy，未恢复不认证知识被删除，有限恢复也不授意图deception。Ch5的probe/score/choice与形成—访问—使用干预（约271–279）已承载此具体分离，root核准已有覆盖。

### [Model Context Protocol (MCP) Tool Descriptions Are Smelly! Towards Improving AI Agent Efficiency with Augmented MCP Tool Descriptions](https://arxiv.org/abs/2602.14878v1)

exact v1 router仅改client描述组件；231任务/202工具不是完整856库。三model旧aggregate baseline非paired，Next80B仅部分组件、搜索API也替换；steps非token/E2E成本，p>.2不证明等价。Ch83:260–283已有description/schema同artifact身份、更新重验及更完整描述的费用，root必要源/owner核准已有覆盖，不为smell分类增写。

### [The Potential of CoT for Reasoning: A Closer Look at Trace Dynamics](https://arxiv.org/abs/2602.14903v1)

exact v1 Eq3.1的potential来自prefix后继续rollout的128次终点正确率，不是强制即时回答；正确cohort平均单调不约束每条链，flat不认证可删，gold optimal-chunk搜索付MN成本且非部署selector。Ch66:1693–1702已有操作性诊断与faithfulness分账，3804–3810已有重复continuation测量，root核准已有覆盖，不混同两个干预。

### [Competition for attention predicts good-to-bad tipping in AI](https://arxiv.org/abs/2602.14370v1)

exact v1 BODY218–245以penultimate mean-pool与六phrase centroid构造analytic attention替final layer，提供局部方向/几何现象。代理尚未验证与完整learned QKV、多层动力学的对应桥，故不采用可预测tipping或控制保证，也不将安全场景叙述当部署证据。root具体Only理由通过，不是因小模型或缺普遍证明否认其研究价值，不写Books。

### [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872v1)

exact v1 PDF §3/5/7–8的fixed atomic MLP、position-only Q/zero init、nonabelian simply-transitive群作用与精确期望长度归一更新下，过大难度比仍长plateau，moderate ratio提供有限gradient relay条件。Z96/EMA/entropy toy不是同理论前提，终点正确不认证全trajectory，真实LLM语义/原子技能变化未验证。精确PDF页1February17/题名与HTML生成August24、旧DataCite题名分开。Ch33:350及末注2845补此条件分支；root实际338–373邻接、正文与末注POST通过，锁释放，不采普遍课程最优。

### [Train Short, Inference Long: Training-free Horizon Extension for Autoregressive Video Generation](https://arxiv.org/abs/2602.14027v1)

exact v1 Eq10–11以AR1负相关noise调整joint/temporal spectrum，每frame Gaussian marginal不变不证明joint无分布失配，ρ=−1退化为alternating。NTK/RoPE旧部件不借分，training-free只adaptation；Table3 without-ANS motion33.84→40.63同时image70.08→69.77，有限长片不授无限稳定。Ch24:284–295尤其289/291已拥有marginal/joint noise identity、coupling权限、denoiser/sampler分工与未校准退independent，root必要原源/owner核准已有覆盖，不为temporal轴名称补书。

### [GTS: Inference-Time Scaling of Latent Reasoning with a Learnable Gaussian Thought Sampler](https://arxiv.org/abs/2602.14077v1)

exact-v1 §3–5及必要附录为冻结backbone的条件diagonal proposal，dim-mean密度比不是joint求和，无偏保证不采用。单A100/two backbone/GSM8K，N2反侧、pass@N需selector、head/rollout费用及正文20k与附录10k训练口径分开。Ch8:308/末注345、完整291–320 root POST通过，不授推理普胜或latent posterior。

### [BitDance: Scaling Autoregressive Generative Models with Binary Tokens](https://arxiv.org/abs/2602.14041v1)

exact-v1 PDF §3.2–3.3/Eq3/5–7为patch内joint binary diffusion/flow head及跨patch block-causal AR；组合数不认证有效容量，head不认证exact sampling。ImageNet256/A100/B64/BF16及匹配消融支持局部tradeoff，patch增大FID也退步，head迭代/训练与外family配置分账。Ch24:46/末注1970、完整38–59 root POST通过。

### [Diagnosing Knowledge Conflict in Multimodal Long-Chain Reasoning](https://arxiv.org/abs/2602.14518v1)

exact-v1 §3–5及必要appendix D以受控source指示形成token-level conflict读出；forward/reverse非对称只三7/11B模型局部结果，probe调参/指标循环、约10%span人工核验人口与topK每candidate forward成本保留。α=.6与声明搜索.1–.5冲突不修，VCD VT冲突率.03→.15反侧不删除。Ch23现冲突检测→融合控制权、视觉anchor非真值及漂移回退具体已有覆盖，root通过；不虚称完整该实验已写书。

### [DenseMLLM: Standard Multimodal LLMs for Dense Prediction](https://arxiv.org/abs/2602.14134v1)

exact-v1 §3/Eq2–5用multi-hot Bernoulli监督，valid域内topk负例非所有unlabeled真负；rawlogit/多子词均值/readout与监督费用分开。分辨率/专用head反侧保留。Ch23:81/末注1235和完整75–87 root POST通过。

### [When Test-Time Guidance Is Enough: Fast Image and Video Editing with Diffusion Guidance](https://arxiv.org/abs/2602.14157v1)

exact-v1 §2–4的既有VJP-free不作独创，denoiser Jacobian≈(1/α)I忽略noise predictor导数非精确；latent linearGaussian mask不等pixel合同，thinmask/dilation/FLUX反侧及solver/codec/cost保留。Ch24:141/完整134–147/末注root POST通过。

### [Boundary Point Jailbreaking of Black-Box LLMs](https://arxiv.org/abs/2602.15001v1)

exact-v1 §3及必要附录为singlebit classifier反馈攻击；mainmodel绕过另需human-found消息，不把未ban账户/Max50/nonempty分母当自然发生率。batchmonitor仅建议，local fixedpopulation理论非adaptive保证。Ch72 Deny Disclosure及Extraction Budget具体已有feedback oracle/跨principal global预算，root Existing通过，不虚称BP算法或防御实测。

### [Deep Dense Exploration for LLM Reinforcement Learning via Pivot-Driven Resampling](https://arxiv.org/abs/2602.14169v1)

exact-v1 §4.1–4.4/Eq1–4及必要评价/Implementation/Limitations：logistic depth拟合至少一suffix成功proxy，不是逐prefix真概率；prefix gradientmask不免forward、suffix local非root无偏，λ/串行采样与未恢复失败限定。Eqtrajectorymean和Appbatchtokenmean冲突不修。Ch33:243/末注2409和239–250 root POST通过。

### [S2D: Selective Spectral Decay for Quantization-Friendly Conditioning of Neural Activations](https://arxiv.org/abs/2602.14432v1)

exact-v1 §4/5 PCDR top≤3/.95/100步缓存及higher-power spectral penalty，是checkpoint conditioning不是fakeQAT；norm上界不唯一归因outlier。8×A100 18sSVD/6sgradient，提前3iter重叠非零费用；PTQ4ViT512W4A4 4.2→3.8反侧保留。Ch49:938/末注2250和934–944 root POST通过。

### [Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution](https://arxiv.org/abs/2602.14869v1)

exact-v1 §3/Eq1–15把概念activation梯度用于data attribution；EKFAC/H≈I/projection近似分账，Eq2 ∇f与Eq7 ∇loss冲突不合并。有限筛选重训/VectorFilter OOD失败、曲率准备与生成成本保留，非真实因果证书。Ch27:1177/末注1268和1172–1183 root POST通过。

### [AnchorWeave: World-Consistent Video Generation with Retrieved Local Spatial Memories](https://arxiv.org/abs/2602.14941v1)

exact-v1 §3.2–3.4/有限eval及必要设置：local world coordinates不提前融合surface，FoV/coverage greedy K、joint anchors/pose融合；global1对local多anchor非pure-fusion控制，10k/8H100/500partial revisit有限。90%与80%denoise口径冲突不修，不授物理。Ch25:1035/末注1262和1029–1041 root POST通过。

### [Efficient Sampling with Discrete Diffusion Models: Sharp and Adaptive Guarantees](https://arxiv.org/abs/2602.15008v1)

exact-v1 Th1–3/Algorithm1/Eq18–19及PDF绑定，mask解析hazard与末步unmask不授正确性；score/init/dependence分账，合法非零rate需核。uniform下界限定τ-leaping path-KL及熵分离，不授所有outputKL。少steps非去dS费用/实测LM加速。Ch24:1061/末注1666及1053–1068 root POST通过。

### [A Theoretical Framework for LLM Fine-tuning Using Early Stopping for Non-random Initialization](https://arxiv.org/abs/2602.13942v1)

exact-v1 §3.5–4.2/§7，empirical NTK谱与局部linearization解释早停bias–variance；Gaussian预训练起点、可控参数邻域、充分宽度、稳定核满秩/RKHS条件不外推普通LLM。未知目标差额范数/噪声使理论停点不可直接算，GPT-Neo1.3B有限任务用hold-out、100sample谱/3run，不授谱即通用兼容性。Ch4:59/末注432及51–64实际邻接，root必要源/actual owner与实际正文/完整邻接及末注POST通过。

### [Train Less, Learn More: Adaptive Efficient Rollout Optimization for Group-Based Reinforcement Learning](https://arxiv.org/abs/2602.14338v1)

exact-v1 §4/Beta(1,1) posterior mean、8初始/总16 rescue与curated4人口；只替mean仍未解决原式group std=0，不采用稳定性或Eq8全局最优。1.5B/7B、2A10/4A100有限math/code验证best-checkpoint/Avg8–Pass8，generation预算非train-token预算。Ch33:428–464已承载shrinkage prior/最终归一边界及adaptive population/support；root实际必要源与owner已有覆盖通过，不为Beta名称改书。

### [WIMLE: Uncertainty-Aware World Models with IMLE for Sample-Efficient Continuous Control](https://arxiv.org/abs/2602.14351v1)

exact-v1 §3.1–3.3/§4.1/4.3/§6，nearest-latent assignment与ensemble+latent总方差用于synthetic TD w=1/(std+1)，real w1。variance不是真值且含aleatoric、std启发式非严格inversevariance，函数逼近重加权不普适Bellman无偏。1Mstep/10seed IQM、Humanoid-run5seed/warmup失准与H8有限，proprioception只合成训练非planning，单L40S3seed墙钟非全部matched E2E。Ch25:339/末注1264及332–345，root必要源/actual owner与实际正文/完整邻接及末注POST通过。

### [Inner Loop Inference for Pretrained Transformers: Unlocking Latent Capabilities Without Training](https://arxiv.org/abs/2602.14759v1)

exact-v1 §II–IV，baseline h0与cached loop states的uniform/η插值/相对h0权重，不认证valid activation domain。Gemma2-2B/WinoGrande naive区间全部退，区间选好再固定其他benches，ARC-E退/Llama3-8B不一致；norm跨family未控，MCQ likelihood非自由生成。额外block/参考forward/cache/层扫成本保留。Ch8:308/末注320及298–316，root必要源/actual owner与实际正文/完整邻接及末注POST通过。

### [Residual Connections and the Causal Shift: Uncovering a Structural Misalignment in Transformers](https://arxiv.org/abs/2602.14760v1)

exact-v1 §4 matched150M/10B比较，α0去identity gradient优化反退，fixed first与learned last是不同干预/人口；current/next相似度不认证结构错误。TableII Wikitext28.46→28.62及metric方向不清，不采全任务改善/唯一对齐因果，成本配置缺口保留。Ch17:251–269已解释I+JF、residual scaling/gate及局部稳定边界，root必要源/实际owner已有覆盖通过，不按新算法名追加。

### [Adapting VACE for Real-Time Autoregressive Video Diffusion](https://arxiv.org/abs/2602.14381v1)

exact-v1 §3–4/dual-stream必要方法/有限评价，refs不再充当历史KV；inactive/reactive cache分开、inpaint跳reactive防ghosting。LongLive1.3B/5090 BF16 SageAttention539→698ms、Krea14B/H100 FA2 inpaint741→958ms，15chunk+3warm-up inference-only；R2V fidelity严重退/长序列需reanchor，不授training-free=实时。Ch24:101/末注1675及93–107，root必要源/actual owner与实际正文/完整邻接及末注POST通过。

### [EditCtrl: Disentangled Local and Global Control for Real-Time Generative Video Editing](https://arxiv.org/abs/2602.15031v1)

exact-v1 §3–4/Table3/§5，local mask人口与全局背景分责，local先训/global后加，LoRA128/8A100约1day。A6000Ada25DDPM、45edit+150inpaint6sec：global FPS4.90→4.67，LPIPS5.54比VACE5.44退/CLIP9.58比9.76退；FPS排除VAE，4K/fast-motion瓶颈与padding未来近似保留。不采全部成本只随mask/零质量损失。Ch24:71/末注1677及65–78，root必要源/actual owner与实际正文/完整邻接及末注POST通过。

## 5. 缺口与下一步

普通可执行工作：无。78家族日期/贡献/必要证据/Books处置、所有写后检查及六部分整日独立验收均通过。公开区间按§3的官方流程与同身份Registered元数据推定，不把登记时间当实际发布时刻；未知首公开材料不借用这一上界补造下界。

本窗外部/中心终态保留项已隔离，不用于正面证据、Books、完整coverage或无遗漏/性能/安全保证；以下各项保留精确定点重开条件：

- [DPBench 2602.13255](https://arxiv.org/abs/2602.13255v1)：v1早Feb2 Submitted，不足本窗公开下界；具体同模型协议deadlock贡献线索仍留，需要可核首次public artifact/公告而非邻ID或Updated，再开日期。
- [Sonnet4.6](https://www.anthropic.com/news/claude-sonnet-4-6)：本窗release事实已核；current release July21修改/card later changelog，使MMMU/ART具体协议当日存在未证明。需当日可核card/release原刊artifact；不扩完整revision史。
- [Quantization Trap](https://arxiv.org/abs/2602.13595v1)：中心能源/casting归因争议。重开只需功率积分、同运行路径matched kernel profiling及跨request batching实证，不循环追附件。
- [Hippocampus](https://arxiv.org/abs/2602.13594v1)：signature/theory与dynamic index保证争议。重开实际共同投影/索引实现、动态更新边界及匹配E2E；独立lossless payload事实不删除。
- [Deep-Thinking Tokens 2602.13517](https://arxiv.org/abs/2602.13517v1)：Eq5/Alg1互补阈值改变统计人口，running-min不能认证cross后稳定，隔离精确可复现DTR中心定义。重开需要作者更正或明确版本实现的阈值人口、稳定性判据与对应实验，不能自行择一修正；有限proxy结果仍可报告。
- [Covariance-Aware Transformers 2602.14506](https://arxiv.org/abs/2602.14506v1)：只隔离LC一般KKT/收敛保证，不删除U映射和局部学习实验。重开需要更正步长/约束条件并解释上述满足原声明条件的发散反例，及与实际learned模型的明确桥；不自行替作者修证明。
- [RynnBrain 2602.14979](https://arxiv.org/abs/2602.14979v1)：v1Submitted=Feb13T18:59:56Z早于Fri19Z，不能套Tue01Z下界；原官方News代码/checkpoint Feb9、report Feb17但未有完全落窗时分/原始报告日期区间。早family artifact不替代paper公开；需本窗精确原刊证据才能纳入，真实归属未定，不重跑别日。
- 机构历史目录与Seed11未返回项：具体范围见§2；有限可用原入口恢复后留名限制，不能说0命中/完整历史已审。待出现可核原目录/原刊材料只定点重开受影响源/候选。

第五批13804的drop-in/certified/fullcost constant bridge已发现中心争议；有条件Euclidean投影不等softmax保证，raw-q gap不是projection-residual gap，query位于conv时inactive为空/Def1不可认证，即使raw-gap>0，不能写成true gap=0。稀疏路径原表全点更慢，质量仅建议补测。13659的Lemma3字面初始化前提无可满足非零点，理论alignment oracle与实用loss-reward/greedy接口不同；只暂缓本文这一宣称的d-free实用ZO保证，不替作者修定理或宣其他全部理论错误。两项root必要反证均已通过，本次保留中心争议，不写正面Books；重开分别需要可核projection-gap证书与完整routing/quality评价，以及更正初始化假设/实用oracle对应证明。

## 6. 复核

复核者：root（非本日报告作者feb18_v3）。
结论：通过

root已实际独核78家族的日期、准入与必要证据；38家族正文、完整邻接及末注POST通过，31项具体已有覆盖、3仅报告和6中心争议安全处置通过。13699经验结果已有覆盖，理论子命题独立隔离。原14351按小模型/foundation桥排除的范围误判已纠正；13942/14338/14351/14759/14760/14381/15031七事件均采用精确v1和独立日期区间，后两个HTML生成日期不作首公开。版本、布局、评价分母与反例精度问题已限定纠正，各实际位置见§4及本日必要证据。

排除复核复用早期实际准入校准；本次纠错/安全/设计信号负侧定点实际核13529、13574、13591、13611、14606、15028、14299共7项，保留成熟组合/评价代理与未核当日版本的具体理由，不授隐私或共享memory因果结论。普通负侧按主题/理由实际抽检13851、13962、14296、14697、14721五项（形式验证负结果、代码knowledge、FSM/模拟规模、context-weight组合），并复用13626/13738两项已核校准；其他明确排除仅按原筛选理由处理，未称全量负侧独核。查询/标题backstop及宽inventory未转成929篇逐项待办，未扫描每周源。

最终复核实际重核新增7事件、最后5处正文/完整邻接/末注、上述负侧样本；原78必要证据与owner结果按未变化身份/版本/采用命题复用。来源方面核Seed实际日期投影与停页、Hunyuan11范围及Registered官方流程桥，确认六部分自包含限制、普通待办0和本日完整窗口；历史/日期/中心争议隔离项不获得正面Coverage、Evidence、Books或无遗漏保证。

V3 validator通过，78行候选与78项证据标题一一对应；14份本日报告/原始Markdown及24个owner Markdown解析通过，71个本地引用均存在。MiniMax原始MD的1个站点相对链接按原站身份保留，不误当仓库文件也不改原始源。上述本日Markdown与owner文件限定cached/unstaged diff-check均通过；这些检查只验证接口与可判定一致性，不替代root日级语义验收。既有及无关修改保留，未stage、commit、push。
