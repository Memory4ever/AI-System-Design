# Daily Research — 2026-02-27

**规范：** V3
**窗口：** 2026-02-26T09:00:00+08:00 ～ 2026-02-27T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T12:30:00+08:00

## 1. 结论

本日固定窗口内冻结108个唯一候选家族（107论文＋Nano原release）：62实际Books整合、38具体已有覆盖、1仅报告、7中心争议安全隔离；必要证据、Books落实与独立复核均达到本窗安全终态，普通待办0。主题发现共有218个具名论文身份：107候选、91贡献排除、20日期保留项，宽目录不当作本日新论文或额外审阅队列。最终复核纠正21941未证落窗、21297误隔离，以及21760中心争议仍残留Books的三处问题；必要原证保留，错误采用链已撤。来源历史段和日期保留项不授正面覆盖、无遗漏或性能/安全保证。

## 2. 来源覆盖

十四每日来源已按本窗达到有限停止或具体外部隔离，经独立复核；未扫描每周组。arXiv按模型形成、训练/推理、平台、Agent及多模态主题查询，具名查漏只核具体增量，不把分类/月库存扩成逐项队列。同ID Registered上界结合有依据的availability下界确认落窗；Submitted、Created、Updated不直接替代公开时间。

实际入口与响应见[本日来源目录](../_sources/daily-20260227/)。以下仅证明记录中的有限检查，不宣称全站历史召回。每周组未扫描，按需组没有另起会议/版本批次扫描。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | `news/rss.xml`窗内Figma、PNNL、mental-health三事件；前两项按RSS核心说明有限排除；独立复核定点重开[mental-health原文](https://openai.com/index/update-on-mental-health-related-work/)并读核心说明，仍仅已有parental controls和未来trusted contact/extended-conversation评价公告；Feb27 05:30Z Amazon窗外停止 | 已检查 | 前两项不授不可取得正文机制；mental-health原文未披露新增可核机制，不将未来评价记为完成 |
| SRC-ANTHROPIC | Research原HTML内174 publishedOn字段，实际Feb25 20:02Z deprecation→Mar5边界，无窗内字段；可见页面仅10近期项不单独作依据。`V3_ANTHROPIC.raw`、sitemap仅定位 | 已检查 | 有限官方嵌入目录，不保证历史删除项或全机构发布；窗前deprecation不重审 |
| SRC-GOOGLE-AI | Research `blog/2026/02/`7条（Feb3～17）实际读完；DeepMind publications页1 Feb15→Mar10实际停止；Nano官方原release 16Z与changelog有限事实 | 已检查 | DeepMind原gzip损坏响应不作为证据，`*_RESTORE`恢复可读；Nano Mar19更新前具体spec未恢复，原release事实外不采用 |
| SRC-META-AI | Research原响应为空／动态stub；官方publication page3辅助恢复Feb26 PAHF/Feb27 VSONAR两身份。PAHF OAI header Feb19上界证已窗前；VSONAR arXiv Mar1/Registered晚，OR旧稿有公开迹象但API403/challenge | 受阻 | 必要原目录历史段及VSONAR首次公开／重要修订精确版本日期不可确认；目录收录日不当首次公开，保留项不支持当窗候选或零命中 |
| SRC-QWEN | 官方`api/v2/article/retrieval?type=qwen_ai&language=en-US`40条extra.date实际Feb3/10/16邻界，无窗内；不继承旧Daily覆盖 | 已检查 | 仅该原始目录有界结果，不是整个机构无遗漏 |
| SRC-DEEPSEEK | 当前研究导航只定位；官方API updates实际Dec1 2025→Apr24 2026，无窗内API事件，有限搜索原源无新增身份 | 受阻 | 研究导航历史论文／技术发布目录未恢复；API changelog不能替研究覆盖，隔离本窗历史研究段请求，不声称机构零命中 |
| SRC-MOONSHOT | Kimi平台Blog实际止于2025Nov7，共所列24旧事件；本窗有界官方检索无新增身份，不用GitHub Created/Updated证公开 | 受阻 | 2026Feb26～27历史研究／发布目录缺段，旧首页不能证明覆盖；需带公开时间的官方历史列表或定点公告 |
| SRC-TENCENT-HUNYUAN | 首查Research→官方POST publicList，pageSize1000/total9实际Feb3 CLBench、Feb13 HunyuanClip到Apr邻界 | 已检查 | 仅目录9条有限结果；无窗内条目，不全文科学应用 |
| SRC-ZAI | 首查官方Research时间排序15条实际Feb21 GLM5 report→Mar15；release-notes Feb12→Apr7对应核目录；较早与窗外止 | 已检查 | 只采用目录/发布日期；不把后来报告、API更新当本日初公开 |
| SRC-BYTEDANCE-SEED | 论文API type1/year2026 offset60的19条Feb27→Jan27、80尾2 Jan20/22，再空tail；type2 blog12条Feb14→更早实际止 | 已检查 | CUDAAgent目录PubDate Feb27 00BJT vsApr23回填、project仅Feb27日期无TZ、arXiv晚提交，精确首次公告未恢复；安全日期保留，不入候选或Books |
| SRC-BAIDU-ERNIE | 官方Blog页1十条实际Feb6→Apr15邻界，尾Nov2025已越过窗；仅读所需目录及日期 | 已检查 | 有限该博客目录；无需把页2更早条目变逐项队列，未授全机构召回 |
| SRC-XIAOMI-MIMO | Paper8条实际Feb3 HySparse→Mar13；Blog定点页只Dec16 2025 MiMoV2Flash，主页15项Blog导航多为后续／无日期，官方窗内检索无新身份 | 受阻 | 本窗完整dated Blog历史段未恢复；当前Paper可有限止，undated导航不认证零发布，需官方历史dated目录或具体公告 |
| SRC-MINIMAX | EN12条／CN13条Research实际Feb12/14→Mar18邻界，Jan27/28尾止；Agent TechBlog仅May13一条，未把当前模板当历史 | 已检查 | 仅所列研究/技术入口有限结果，EN/CN日期不同但均窗前，不改本日候选；不授全站无遗漏 |
| SRC-ARXIV | 3主题查询306/138/134命中关联191身份＋具体主题4；完整v1题摘195，再具名查漏23新身份（22091重复只日期修正），不是宽479逐项队列；`V3_ADMISSION.tsv`92IN/84EX/19DATE及named13IN/7EX/2准入/1DATE | 已检查 | 官方availability下界＋同ID Registered上界使107候选落窗；20早Submitted潜力项仅缺sameID精确公告，有限日期隔离、不全文/评分/Books；覆盖是约定主题有限停止，不是全分类召回 |

## 3. 候选与判断

最终日期纠偏：21941仅有Registered上界，已移至日期保留项并撤销对应Books采用；21297的Submitted晚于前一公告截止，按同一availability规则完整落窗，定点恢复其必要审阅与Books判断，不扩大窗口或重扫其他日期。

下表维护108个唯一家族：62整合、38已有覆盖、1仅报告、7中心争议。全部准入、必要原证、具体owner与实际Books写后已独立复核；日期字段原值与上下界依据见[日期材料](../_sources/daily-20260227/V3_DATE_PACKET.md)。中心争议仅安全隔离，不记为正面Evidence通过。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Robust AI Evaluation through Maximal Lotteries](https://arxiv.org/abs/2602.21297v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:53:50+08:00 | 从固定聚合偏好改为固定切片矩阵上的人口权重不确定集，显式交换最弱组与聚合偏好胜率；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66偏好聚合段](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；固定TV半径、彩票目标与不覆盖未知组/组内漂移的边界。 |
| [SymTorch: A Framework for Symbolic Distillation of Deep Neural Networks](https://arxiv.org/abs/2602.21307v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:54:04+08:00 | 投影坐标上的函数代理：分别验投影误差与代理误差，full-forward吞吐不外推decode；2+1+3=6；[证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md) | 深入完成 | 整合：MODEL-FFN [具体正文](../../../../books/part-02-model/16-feed-forward-mlp.md) |
| [Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data](https://arxiv.org/abs/2602.21320v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:54:23+08:00 | Generator/Solver互补self-play reward从能力前沿生成tool任务改变RL数据课程；2+2+3=7；[证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md) | 深入完成 | 整合：TRAIN-GRPO [具体正文](../../../../books/part-04-training-system/33-grpo.md) |
| [Dynamic Symmetric Point Tracking: Tackling Non-ideal Reference in Analog In-memory Training](https://arxiv.org/abs/2602.21321v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:54:25+08:00 | 器件对称参考点与loss驻点分开；混合gradient坐标/EMA动态校准与额外模拟state；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXT4_EVIDENCE.md) | 深入完成 | 整合：TRAIN-PRETRAINING [具体正文](../../../../books/part-04-training-system/28-pretraining.md) |
| [HiPPO Zoo: Explicit Memory Mechanisms for Interpretable State Space Models](https://arxiv.org/abs/2602.21340v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:54:52+08:00 | HiPPO显式polynomialmemory自适应allocation/associative结构可解释SSM状态形成；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md) | 深入完成 | 整合：MODEL-LONG-CONTEXT [具体正文](../../../../books/part-02-model/22-long-context.md) |
| [Scaling View Synthesis Transformers](https://arxiv.org/abs/2602.21341v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:54:54+08:00 | compute-matched encoder-decoder NVS scaling反驳decoder-only最优归因，需核architecture/预算；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXT4_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Alignment-Weighted DPO: A principled reasoning approach to improve safety alignment](https://arxiv.org/abs/2602.21346v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:55:01+08:00 | reasoning/finalanswer分段weightedDPO改变jailbreak浅refusal与utility取舍；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md) | 深入完成 | 整合：`TRAIN-DPO` [具体正文](../../../../books/part-04-training-system/34-dpo.md)；语义两段独立loss/proxy与不完备guard接口；root已核实际正文162及邻接/末注473。 |
| [Black-Box Reliability Certification for AI Agents via Self-Consistency Sampling and Conformal Calibration](https://arxiv.org/abs/2602.21368v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:55:34+08:00 | 有限样本认证、同校准集反选α与候选集合真值量词的中心冲突；3+2+3=8；[证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md) | 争议 | 暂缓：[中心冲突与重开条件](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md) |
| [Interleaved Head Attention](https://arxiv.org/abs/2602.21371v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:55:39+08:00 | 跨headqkv线性混合pseudoheads组合token关系而非独立H矩阵；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md) | 深入完成 | 整合：`MODEL-MULTI-HEAD-ATTENTION` [具体正文](../../../../books/part-02-model/15-multi-head-attention.md)；softmax前head混合/虚拟位置与P²预算；root已核正文94及邻接/末注330。 |
| [MMLoP: Multi-Modal Low-Rank Prompting for Efficient Vision-Language Adaptation](https://arxiv.org/abs/2602.21397v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:56:17+08:00 | lowrank跨层prompt与共享up-projection/zero-shot anchors实现parameter-accuracy取舍；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md) | 深入完成 | 整合：TRAIN-LORA [具体正文](../../../../books/part-04-training-system/30-lora.md) |
| [FlowFixer: Towards Detail-Preserving Subject-Driven Generation](https://arxiv.org/abs/2602.21402v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:56:24+08:00 | 语义CLIP/DINO分数高仍可丢关键细节；matching keypoints作为不同fidelity观测，并以单步去噪造高频损失训练对。拟仅detail/semantic评估对象差额。；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md) | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；目标粒度、scorer/proxy和人工锚点已覆盖；保AKI被copy-paste放大反侧与局部人评人口。 |
| [Overconfident Errors Need Stronger Correction: Asymmetric Confidence Penalties for Reinforcement Learning](https://arxiv.org/abs/2602.21420v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:56:50+08:00 | policy/reference confidence shift只加强过度reinforced负advantage，修正Pass1/Passk探索取舍；2+1+3=6；[证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md) | 深入完成 | 整合：TRAIN-GRPO [具体正文](../../../../books/part-04-training-system/33-grpo.md) |
| [On the Structural Non-Preservation of Epistemic Behaviour under Policy Transformation](https://arxiv.org/abs/2602.21424v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:56:56+08:00 | 信息条件policyseparation不被convexmix/biasedpriorgradient保留，probe条件理论反侧；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md) | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` [具体正文](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；固定probe条件行为与平均reward分开；保留Stage1 +5→Stage2 +1混杂，不采用无条件policy-mix保持定理。 |
| [PSF-Med: Measuring and Explaining Paraphrase Sensitivity in Medical Vision Language Models](https://arxiv.org/abs/2602.21428v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:57:02+08:00 | 只采用paraphrase consistency不等visual grounding及SAE causal patch控制命题，不采用医疗决策结论；2+2+3=7；[证据](../_sources/daily-20260227/V3_NEXT4_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Provably Safe Generative Sampling with Constricting Barrier Functions](https://arxiv.org/abs/2602.21429v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:57:03+08:00 | 噪声到终态constricting safety tube离散CBF/QP过滤改变flow采样约束保证；2+2+3=7；[证据](../_sources/daily-20260227/V3_NEXT4_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [具体正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [MINAR: Mechanistic Interpretability for Neural Algorithmic Reasoning](https://arxiv.org/abs/2602.21442v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:57:22+08:00 | GNNalgorithmiccircuits patching识别multi-taskreuse/formation，模型能力机理非领域应用；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md) | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [具体正文](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [VLA Knows Its Limits](https://arxiv.org/abs/2602.21445v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:57:27+08:00 | chunk预测长度与实际执行前缀分开，attention代理adaptive horizon；2+2+3=7；[证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Adversarial Intent is a Latent Variable: Stateful Trust Inference for Securing Multimodal Agentic RAG](https://arxiv.org/abs/2602.21447v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:57:30+08:00 | 跨检查点风险summary与多阶段相关失败；持久state不等校准posterior；3+2+3=8；[证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md) | 深入完成 | 已有覆盖：PLATFORM-SECURITY [具体正文](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [When Learning Hurts: Fixed-Pole RNN for Real-Time Online Training](https://arxiv.org/abs/2602.21454v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:57:40+08:00 | small-data实时RNN固定pole的条件与optimizer landscape负面证据；2+1+3=6；[证据](../_sources/daily-20260227/V3_NEXT5_EVIDENCE.md) | 深入完成 | 整合：MODEL-LONG-CONTEXT [具体正文](../../../../books/part-02-model/22-long-context.md) |
| [VecGlypher: Unified Vector Glyph Generation with Language Models](https://arxiv.org/abs/2602.21461v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:57:50+08:00 | 直接AR SVG serialization替代raster后处理，coordinate/两阶段训练消融刻画表示质量边界；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXT5_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [具体正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Geometric Priors for Generalizable World Models via Vector Symbolic Architecture](https://arxiv.org/abs/2602.21467v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:57:59+08:00 | latent group结构以complex multiplication承载动作composition，gridworld局部world-model边界；2+1+3=6；[证据](../_sources/daily-20260227/V3_NEXT5_EVIDENCE.md) | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [具体正文](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [The Design Space of Tri-Modal Masked Diffusion Models](https://arxiv.org/abs/2602.21472v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:58:06+08:00 | trimodal masked-diffusion modality/noise/batch研究，物理与逻辑batch解耦的SDE重参数；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXT5_EVIDENCE.md) | 深入完成 | 整合：TRAIN-PRETRAINING [具体正文](../../../../books/part-04-training-system/28-pretraining.md) |
| [Pancake: Hierarchical Memory System for Multi-Agent LLM Serving](https://arxiv.org/abs/2602.21477v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:58:13+08:00 | agent ANN index层级缓存、跨agent协调与GPUCPU协作，真实owner RAG索引而非KV/HBM；2+2+3=7；[证据](../_sources/daily-20260227/V3_NEXT5_EVIDENCE.md) | 深入完成 | 整合：AGENT-RAG [具体正文](../../../../books/part-07-agent/76-rag.md) |
| [Both Ends Count! Just How Good are LLM Agents at "Text-to-Big SQL"?](https://arxiv.org/abs/2602.21480v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:58:18+08:00 | TexttoBigSQL任务规模下accuracy不等execution cost的评价盲区；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md) | 标准完成 | 已有覆盖：PLATFORM-COST [具体正文](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [GradAlign: Gradient-Aligned Data Selection for LLM Reinforcement Learning](https://arxiv.org/abs/2602.21492v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:58:35+08:00 | trusted validation gradient对齐选RL problems而非accuracy过滤，适用reward噪声/非平稳数据；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md) | 深入完成 | 整合：TRAIN-DATA [具体正文](../../../../books/part-04-training-system/27-data.md) |
| [Beyond Refusal: Probing the Limits of Agentic Self-Correction for Semantic Sensitive Information](https://arxiv.org/abs/2602.21496v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:58:41+08:00 | SemSI editing构造rewrite与truncate的capacity界及reasoning privacy-utility反侧；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md) | 深入完成 | 整合：PLATFORM-SECURITY [具体正文](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [See It, Say It, Sorted: An Iterative Training-Free Framework for Visually-Grounded Multimodal Reasoning in LVLMs](https://arxiv.org/abs/2602.21497v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:58:43+08:00 | 候选受限decider、同图派生sentence evidence与真实acquisition分责；raw margin非校准；2+2+2=6；[证据](../_sources/daily-20260227/V3_CLARIFY4_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Easy3E: Feed-Forward 3D Asset Editing via Rectified Voxel Flow](https://arxiv.org/abs/2602.21499v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:58:45+08:00 | 2D edit通过sparsevoxel flow改变3D结构，normal-guided外部appearance恢复压缩表示丢高频；geometry与appearance prior分责。；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md) | 标准完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [具体正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；geometry/control与appearance prior分责已覆盖；保25-step与75秒全链、silhouette/生成多视角非真值。 |
| [WaterVIB: Learning Minimal Sufficient Watermark Representations via Variational Information Bottleneck](https://arxiv.org/abs/2602.21508v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:58:59+08:00 | watermarkmessage信息bottleneck过滤covertexture减少regenerationattack脆弱性，需核necessary保证；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md) | 深入完成 | 整合：PLATFORM-SECURITY [具体正文](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [I/O Optimizations for Graph-Based Disk-Resident Approximate Nearest Neighbor Search: A Design Space Exploration](https://arxiv.org/abs/2602.21514v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:59:08+08:00 | ANN page复杂度把路径长度和页locality共同计价；sameimplementation/factorial揭page shuffle/search单独弱联合有用，需严格I/O模型与召回预算。；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md) | 深入完成 | 整合：`AGENT-RAG` [具体正文](../../../../books/part-07-agent/76-rag.md)；page locality×consumer expansion与饱和SSD多读反侧；root已核正文227及邻接/末注1260。 |
| [Training Generalizable Collaborative Agents via Strategic Risk Aversion](https://arxiv.org/abs/2602.21515v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:59:10+08:00 | strategic risk aversion抑制协作free-riding/未知partner失败，实际LLM协作受限机制；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md) | 深入完成 | 整合：AGENT-MULTI-AGENT [具体正文](../../../../books/part-07-agent/82-multi-agent.md) |
| [LiLo-VLA: Compositional Long-Horizon Manipulation via Linked Object-Centric Policies](https://arxiv.org/abs/2602.21531v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:59:34+08:00 | transport/global reach与object-centric interaction拆分改变长任务错误恢复/skill组合；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md) | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；verified skills、fresh observation与局部恢复实际已覆盖；GT checker、人验、重复尝试和36/27统计冲突保留，不授物理undo。 |
| [ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning](https://arxiv.org/abs/2602.21534v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:59:38+08:00 | 四维policy-gradient controlled instability拆解与SAMPO改变agent RL稳定训练；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md) | 深入完成 | 整合：TRAIN-GRPO [具体正文](../../../../books/part-04-training-system/33-grpo.md) |
| [Enhancing Multilingual Embeddings via Multi-Way Parallel Text Alignment](https://arxiv.org/abs/2602.21543v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:59:51+08:00 | multiwayparalleltextvsEnXcontrastive控制crosslingualalignment，既有embedding升级边界；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md) | 深入完成 | 整合：`AGENT-RAG` [具体正文](../../../../books/part-07-agent/76-rag.md)；translation group/all-language anchor与预算人口分责；root已核正文272及邻接/末注1261。 |
| [Muon+: Towards Better Muon via One Additional Normalization Step](https://arxiv.org/abs/2602.21545v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:59:54+08:00 | Muon polar不消除row/column imbalance，postpolar单归一化改变optimizer下降条件；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md) | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING` [具体正文](../../../../books/part-04-training-system/28-pretraining.md)；post-polar归一与variance state/order分责已覆盖；Table15仅有限matched LR对照，保搜索费与非交换归一。 |
| [RAC: Relation-Aware Cache Replacement for Large Language Models](https://arxiv.org/abs/2602.21547v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:59:57+08:00 | topic prevalence/structural reuse信号替代短recency-frequency的语义cache驱逐；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md) | 深入完成 | 整合：INFER-KV-CACHE [具体正文](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM Inference](https://arxiv.org/abs/2602.21548v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T10:59:58+08:00 | storage到decode再RDMA到prefill双路径使用idle NIC打破PD存储瓶颈；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md) | 深入完成 | 整合：`INFER-PD-DISAGGREGATION` [具体正文](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；DE代读仍回PE计算miss、完整prompt后才DE H2D；root已核正文438–456及完整邻接/末注589。 |
| [Training-free Composition of Pre-trained GFlowNets for Multi-Objective Generation](https://arxiv.org/abs/2602.21565v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:00:25+08:00 | pretrainedGFlowNets linearreward exact/nonlinear distortion composition理论，非采用molecule科学应用；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md) | 深入完成 | 整合：MODEL-SAMPLING [具体正文](../../../../books/part-02-model/20-sampling.md) |
| [Duel-Evolve: Reward-Free Test-Time Scaling via LLM Self-Preferences](https://arxiv.org/abs/2602.21585v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:00:56+08:00 | pairwise selfpreferences+Bayesian BradleyTerry/Thompson分配search预算替代scalar evaluator；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md) | 标准完成 | 已有覆盖：`MODEL-SAMPLING` [具体正文](../../../../books/part-02-model/20-sampling.md)；有限candidate comparison graph/query-local状态和独立oracle已覆盖；保MAP/Laplace近似、discarded ties与全生成/judge预算。 |
| [CADC: Content Adaptive Diffusion-Based Generative Image Compression](https://arxiv.org/abs/2602.21591v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:01:06+08:00 | diffusion codec quantization-distortion/noise prior与auxdecoder信息压缩改变rate-perception取舍；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Breaking Semantic-Aware Watermarks via LLM-Guided Coherence-Preserving Semantic Injection](https://arxiv.org/abs/2602.21593v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:01:09+08:00 | embedding约束coherent语义改变击穿semantic watermark的安全反侧；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md) | 争议 | 暂缓：中心ASR人口/阈值争议：ASR=编辑后仍阳性，但最低72>阈值12与Table81%无法合并；仅报告原事实、不正面采用。重开需same-image编辑成功标签、检测统计/阈值、表/图有效分母。 |
| [SPOC: Safety-Aware Planning Under Partial Observability And Physical Constraints](https://arxiv.org/abs/2602.21595v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:01:12+08:00 | partialobservability/physicalconstraint onlineplanning评价隐含hazard失效边界；2+1+2=5；[证据](../_sources/daily-20260227/V3_REMAIN4_EVIDENCE.md) | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Hidden Semantic Bottleneck in Conditional Embeddings of Diffusion Transformers](https://arxiv.org/abs/2602.21596v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:01:14+08:00 | conditional embedding高angular冗余与pruning少维度不损质量，改变conditioning预算；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [具体正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [AQR-HNSW: Accelerating Approximate Nearest Neighbor Search via Density-aware Quantization and Multi-stage Re-ranking](https://arxiv.org/abs/2602.21600v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:01:20+08:00 | densityadaptiveANNquant与multistagererank改变RAGindex recall/cost，需核graphbuild/真实配置；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md) | 标准完成 | 已有覆盖：`AGENT-RAG` [具体正文](../../../../books/part-07-agent/76-rag.md)；coarse navigation→低成本精化→原向量重排已覆盖；原PDF仅uniform8bit与density percentile，保5000sample、earlystop非exact、total memory与billion实测不支持。 |
| [Structurally Aligned Subtask-Level Memory for Software Engineering Agents](https://arxiv.org/abs/2602.21611v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:01:38+08:00 | episode级memory与subtask functional decomposition错配，改变SWE存取更新granularity；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md) | 深入完成 | 整合：AGENT-MEMORY [具体正文](../../../../books/part-07-agent/77-memory.md) |
| [When More Is Less: A Systematic Analysis of Spatial and Commonsense Information for Visual Spatial Reasoning](https://arxiv.org/abs/2602.21619v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:01:51+08:00 | singleprecisecue胜multi-context/excesscommonsense、CoT须先ground的受控负面VSR边界；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md) | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；派生cue的可消费性与可靠性分责已覆盖；保按效果排序/amount+relevance混杂，未采用cognitive-overload因果定律。 |
| [ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation](https://arxiv.org/abs/2602.21622v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:01:56+08:00 | tactile纠正grasp/共享TCP图coordination与独立policy边界，需核adaptive modality实际贡献；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md) | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；真实contact、任务gate和physical controller责任已覆盖；全TCP共享、仿真/真机futurework、70/30数据未隔离均保留。 |
| [Multi-Layer Scheduling for MoE-Based LLM Reasoning](https://arxiv.org/abs/2602.21626v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:02:02+08:00 | request/engine/expert三层load与expertdependency placement调度边界，避免把SJF成熟算法当新增；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md) | 深入完成 | 整合：MODEL-MOE [具体正文](../../../../books/part-02-model/21-moe.md) |
| [Tokenizing Semantic Segmentation with RLE](https://arxiv.org/abs/2602.21627v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:02:04+08:00 | mask由densepixel改为RLE token序列，视频长度/instanceidentity编码取舍；需有限core核编码具体差额，非RLE本身新。；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning](https://arxiv.org/abs/2602.21628v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:02:06+08:00 | competence-based reward rubric分层权重改变RL curriculum而非仅采样题；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md) | 深入完成 | 整合：TRAIN-GRPO [具体正文](../../../../books/part-04-training-system/33-grpo.md) |
| [Self-Correcting VLA: Online Action Refinement via Sparse World Imagination](https://arxiv.org/abs/2602.21633v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:02:14+08:00 | sparse future progress/trajectory heads作为内部future feedback在线action refinement；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md) | 争议 | 暂缓：中心state-guide坐标争议：Eq8 local位移与Eq13/14 world位移直接相加/点积；不静默补R_t。重开需同版实际reward坐标/旋转与Fig4对应；SPI独立经验保留但不冒充OAR真机。 |
| [Scalable Multilingual Multimodal Machine Translation with Speech-Text Fusion](https://arxiv.org/abs/2602.21646v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:02:35+08:00 | 同text的synthetic/authentic语音对照；派生模态引入TTS prior但非新环境观测；2+1+2=5；[证据](../_sources/daily-20260227/V3_CLARIFY4_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Sparsity Induction for Accurate Post-Training Pruning of Large Language Models](https://arxiv.org/abs/2602.21652v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:02:45+08:00 | 中心等价与fast-refresh原定义冲突；有限表格不恢复中心主张；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md) | 争议 | 暂缓：[中心冲突与重开条件](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md) |
| [CCCaption: Dual-Reward Reinforcement Learning for Complete and Correct Image Captioning](https://arxiv.org/abs/2602.21655v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:02:50+08:00 | caption completeness与correctness分reward抛开不全人类gold监督，需核judge/质量代价；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md) | 深入完成 | 整合：TRAIN-GRPO [具体正文](../../../../books/part-04-training-system/33-grpo.md) |
| [DWA-KD: Dual-Space Weighting and Time-Warped Alignment for Cross-Tokenizer Knowledge Distillation](https://arxiv.org/abs/2602.21669v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:03:13+08:00 | cross-tokenizer双空间entropy加权与SoftDTW lexical/context alignment明确词表/序列边界；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTB5_EVIDENCE.md) | 深入完成 | 整合：TRAIN-SFT [具体正文](../../../../books/part-04-training-system/29-sft.md) |
| [Primary-Fine Decoupling for Action Generation in Robotic Imitation](https://arxiv.org/abs/2602.21684v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:03:38+08:00 | 离散mode选择→条件连续residual；one-NFE不等去除码本/分类训练费用；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md) | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；粗mode→连续细动作与错误路由/码本/监督切换已覆盖；one-NFE不免前置训练，total variance不授预测mode保证。 |
| [EditFlow: Benchmarking and Optimizing Code Edit Recommendation Systems via Reconstruction of Developer Flows](https://arxiv.org/abs/2602.21697v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:03:58+08:00 | last-edit-only合法动作错拒的条件性推断，与有限人注/多模型recall分账；2+2+2=6；[证据](../_sources/daily-20260227/V3_REMAIN4_EVIDENCE.md) | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2602.21704v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:04:08+08:00 | truthfulness/perception不同head+semantic-dependent vectors驱动动态activation steering；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTB5_EVIDENCE.md) | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [TranX-Adapter: Bridging Artifacts and Semantics within MLLMs for Robust AI-generated Image Detection](https://arxiv.org/abs/2602.21716v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:04:26+08:00 | uniform artifact attention dilution与OT/crossattention互融的受限fusion机制；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTB5_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations](https://arxiv.org/abs/2602.21723v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:04:37+08:00 | reference-free DF条件surface/gradient/velocity，由privilegedDF latent蒸馏到egodepth部署；真实观测/几何prior与条件迁移成本。；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md) | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；privileged teacher与runtime observation分责已覆盖；保不可见背部contact、视觉/teacher真机人口差异及DAgger费用。 |
| [Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild](https://arxiv.org/abs/2602.21736v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:04:56+08:00 | inverse dynamics+realaction jointly aligned latent action替代fullvisualreconstruct用于wildvideo VLA预训练；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTB5_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Enhancing Multi-Modal LLMs Reasoning via Difficulty-Aware Group Normalization](https://arxiv.org/abs/2602.21743v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:05:07+08:00 | perception entropy/uncertainty regroup共享std的GRPO multimodal归一化；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTB5_EVIDENCE.md) | 深入完成 | 整合：TRAIN-GRPO [具体正文](../../../../books/part-04-training-system/33-grpo.md) |
| [Accelerating Diffusion via Hybrid Data-Pipeline Parallelism Based on Conditional Guidance Scheduling](https://arxiv.org/abs/2602.21760v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:05:32+08:00 | 降序schedule令parallel elseif分支不可达；性能表不修复中心算法；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md) | 争议 | 暂缓：[中心冲突与重开条件](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md) |
| [Easy to Learn, Yet Hard to Forget: Towards Robust Unlearning Under Bias](https://arxiv.org/abs/2602.21773v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:05:51+08:00 | bias-aligned forget可能反而提高目标classaccuracy，指出shortcutunlearning与causal/bias梯度路径分账。安全项必要深入。；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md) | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [具体正文](../../../../books/part-06-ai-infrastructure/72-security.md)；合法retain泛化、删除影响和行为/probe分责已覆盖；保forget-class accuracy增反例及loss方向冲突，不采sharpness因果。 |
| [From Statics to Dynamics: Physics-Aware Image Editing with Latent Transition Priors](https://arxiv.org/abs/2602.21778v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:05:58+08:00 | pairedimageboundary不足physicaltransition监督，learnedtimequeries用视频trajectory补causaledit；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md) | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [具体正文](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Beyond Static Artifacts: A Forensic Benchmark for Video Deepfake Reasoning in Vision Language Models](https://arxiv.org/abs/2602.21779v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:06:00+08:00 | staticartifact与temporalgrounding/forensicreasoning三层benchmark揭video评价盲区；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md) | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [XStreamVGGT: Extremely Memory-Efficient Streaming Vision Geometry Grounded Transformer with KV Cache Compression](https://arxiv.org/abs/2602.21780v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:06:01+08:00 | stream3D causalKV固定预算prune+dimadaptivequant的kernelfriendly质量/记忆取舍；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md) | 标准完成 | 已有覆盖：INFER-KV-CACHE [具体正文](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DHP: Efficient Scaling of MLLM Training with Dynamic Hybrid Parallelism](https://arxiv.org/abs/2602.21788v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:06:13+08:00 | 精确v1DHP：异构MLLM动态nonpowerdegree混合并行/通信组与毫秒规划，不沿用后版FCP通用LLM宣传；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md) | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [具体正文](../../../../books/part-04-training-system/36-distributed-training.md) |
| [DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and Spatial Hand-Object Representations](https://arxiv.org/abs/2602.21811v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:06:47+08:00 | handobjectgeometry/representation旧dexterous任务性能，最小core看是否新可泛化condition/真实输入假设，不凭单camera泛化宣传。；2+1+2=5；[证据](../_sources/daily-20260227/V3_REMAIN4_EVIDENCE.md) | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:06:57+08:00 | dualstreamMMDiT audiovisualjoint+concat统一inpainting+低分辨率sequence/highreskeyframe取舍；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [具体正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [DocDjinn: Controllable Synthetic Document Generation with VLMs and Handwriting Diffusion](https://arxiv.org/abs/2602.21824v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:07:06+08:00 | seedcluster参数化sampling与语义visual解耦合成doc训练data控制real样本预算；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTD5_EVIDENCE.md) | 深入完成 | 整合：TRAIN-DATA [具体正文](../../../../books/part-04-training-system/27-data.md) |
| [FewMMBench: A Benchmark for Multimodal Few-Shot Learning](https://arxiv.org/abs/2602.21854v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:07:50+08:00 | instruction-tuned多模态fewshot/CoT可regress且retrieval/context未救回的评价反侧；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTD5_EVIDENCE.md) | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [DynamicGTR: Leveraging Graph Topology Representation Preferences to Boost VLM Capabilities on Graph QAs](https://arxiv.org/abs/2602.21864v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:08:05+08:00 | 同graph固定visual/text格式对不同task/model不合适，query-level representationrouting需冻结utility/brevity与格式等价；是否新路由/blindspot须有限核。；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection](https://arxiv.org/abs/2602.21887v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:08:38+08:00 | thinkinglanguage作为onpolicy RL action扩探索，同budget nonEnglish增量；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTD5_EVIDENCE.md) | 深入完成 | 整合：TRAIN-GRPO [具体正文](../../../../books/part-04-training-system/33-grpo.md) |
| [A task-based data-flow methodology for programming heterogeneous systems with multiple accelerator APIs](https://arxiv.org/abs/2602.21897v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:08:53+08:00 | CUDA/SYCL/Triton跨native执行dependence与threadpool统一管理避免oversubscription，训练runtime互操作；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md) | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [具体正文](../../../../books/part-04-training-system/36-distributed-training.md) |
| [EmoOmni: Bridging Emotional Understanding and Expression in Omni-Modal LLMs](https://arxiv.org/abs/2602.21900v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:08:57+08:00 | ThinkerTalker hidden接口丢情绪信息，用ECoT显式高层指令handoff改变omnimodal表示；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTD5_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Learning in the Null Space: Small Singular Values for Continual Learning](https://arxiv.org/abs/2602.21919v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:09:25+08:00 | fixedsmall-singularbasis weightLoRAupdates保旧inputnullspace，比gradientprojection不同continuallearning机制；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md) | 标准完成 | 已有覆盖：`TRAIN-LORA` [具体正文](../../../../books/part-04-training-system/30-lora.md)；低干扰subspace proposal与retention gate已覆盖；保past/current输入身份冲突，weight decay不授hard spectral bound，有限经验不推出zero forgetting。 |
| [Large Language Models are Algorithmically Blind](https://arxiv.org/abs/2602.21947v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:10:06+08:00 | LLM预测algorithm性能区间与真实executions校准失败，修正declarativeknowledge推算性能；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTE5_EVIDENCE.md) | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MEDSYN: Benchmarking Multi-EviDence SYNthesis in Complex Clinical Cases for Multimodal Large Language Models](https://arxiv.org/abs/2602.21950v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:10:11+08:00 | 文本/图像移除对照揭示证据合成盲区；不收医学部署结论；2+2+2=6；[证据](../_sources/daily-20260227/V3_REMAIN4_EVIDENCE.md) | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [MindDriver: Introducing Progressive Multimodal Reasoning for Autonomous Driving](https://arxiv.org/abs/2602.21952v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:10:14+08:00 | semantic→futurephysicalimage→trajectory对齐progressive奖励明确VLA推理表示接口；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTE5_EVIDENCE.md) | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [When LoRA Betrays: Backdooring Text-to-Image Models by Masquerading as Benign Adapters](https://arxiv.org/abs/2602.21977v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:10:51+08:00 | 独立分享LoRA作为texttrigger→targetvisual backdoor载体，冻结base而adapter拥有供应链写权；核benignutility/触发scope/真实防御反侧，安全必要深入。；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md) | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [具体正文](../../../../books/part-06-ai-infrastructure/72-security.md)；生成链可变组件与实际adapter bytes/条件行为已覆盖；保双组件、容量不匹配与benign/多adapter退步，probe不授防御。 |
| [CxMP: A Linguistic Minimal-Pair Benchmark for Evaluating Constructional Understanding in Language Models](https://arxiv.org/abs/2602.21978v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:10:52+08:00 | minimalpairs分离grammaticalacceptability和constructionmeaning的learnedability边界；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTE5_EVIDENCE.md) | 深入完成 | 整合：WORLDVIEW-LLM-INTELLIGENCE [具体正文](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md) |
| [Enhancing LLM-Based Test Generation by Eliminating Covered Code](https://arxiv.org/abs/2602.21997v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:11:20+08:00 | coveragefeedback删已覆盖codeslice改变剩余context/iteration目标而非无界generate；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTE5_EVIDENCE.md) | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [World Guidance: World Modeling in Condition Space for Action Generation](https://arxiv.org/abs/2602.22010v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:11:39+08:00 | futureobservation压到actionconditionspace，预测condition+action而非整帧world，控制取舍；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTE5_EVIDENCE.md) | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations](https://arxiv.org/abs/2602.22013v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:11:44+08:00 | visualdegradation与semanticdualpath/unidirectional隔离改变VisRAG retrievalgeneration共同错误；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [A Diversity Diet for a Healthier Model: A Case Study of French ModernBERT](https://arxiv.org/abs/2602.22014v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:11:45+08:00 | commensuratesize随机/多样性数据对照，小Frenchencoder也可改变pretrainingdata判断；不把不同训练时间/尺寸headline当matchedcompute。；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md) | 深入完成 | 整合：TRAIN-DATA [具体正文](../../../../books/part-04-training-system/27-data.md) |
| [FlowCorrect: Efficient Interactive Correction of Generative Flow Policies for Robotic Manipulation](https://arxiv.org/abs/2602.22056v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:12:47+08:00 | deploymentrelativehumanpose corrections局部flowpolicy adaptation无backboneretrain的记忆边界；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Semantic Partial Grounding via LLMs](https://arxiv.org/abs/2602.22067v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:13:04+08:00 | LLM语义partialgrounding裁剪PDDL对象/操作算子改变grounding成本与plancompleteness风险；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md) | 标准完成 | 已有覆盖：AGENT-PLANNING [具体正文](../../../../books/part-07-agent/79-planning.md) |
| [Language Models Exhibit Inconsistent Biases Towards Algorithmic Agents and Human Experts](https://arxiv.org/abs/2602.22070v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:13:08+08:00 | statedtrust和performance-conditioned bets偏差相反，评价格式不能代真实决策倾向；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md) | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Understanding Artificial Theory of Mind: Perturbed Tasks and Reasoning in Large Language Models](https://arxiv.org/abs/2602.22072v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:13:12+08:00 | perturbedfalsebelief reasoningchains/finalfaithfulness分离ToM与CoT反侧；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md) | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation](https://arxiv.org/abs/2602.22088v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:13:35+08:00 | 视觉global在free-space导航，接触后force-local估interactionframe、hybridforce/positioncontrol；条件切换/坐标估计与真实contactfeedback分责。；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Learning to Drive is a Free Gift: Large-Scale Label-Free Autonomy Pretraining from Unposed In-The-Wild Videos](https://arxiv.org/abs/2602.22091v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:13:39+08:00 | unposedwildvideo sequence-levelmultiteacher pseudo4Drepresentation可video-centric autonomypretrain；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md) | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [具体正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [PASTA: A Modular Program Analysis Tool Framework for Accelerators](https://arxiv.org/abs/2602.22103v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:13:56+08:00 | GPU驻留collect-and-analyze改变trace处理位置；device summary有损及total-profile成本分账；2+2+2=6；[证据](../_sources/daily-20260227/V3_CLARIFY4_EVIDENCE.md) | 深入完成 | 整合：PLATFORM-TRACE [具体正文](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Don't stop me now: Rethinking Validation Criteria for Model Parameter Selection](https://arxiv.org/abs/2602.22107v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:14:02+08:00 | validationacc早停/同lossobjective checkpointselection反侧；test-best是事后oracle不作为可部署规则，小classifier不直接外推LLM。；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md) | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [具体正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；selector与独立test目标分责已覆盖；同trajectory有限反证不授普遍lossES失败，未拒绝不等统计等价。 |
| [Probing the Geometry of Diffusion Models with the String Method](https://arxiv.org/abs/2602.22122v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:14:25+08:00 | stringmethod沿learnedscore探索MEPvsprincipalcurve，likelihoodmax不等perceptualrealism，不用protein科学应用；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [具体正文](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [SWE-Protégé: Learning to Selectively Collaborate With an Expert Unlocks Small Language Models as Software Engineering Agents](https://arxiv.org/abs/2602.22124v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:14:28+08:00 | SLM soledecisionmaker learns遇stalledstate求expert及anti-loopreward，选择性delegation取舍；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md) | 深入完成 | 整合：AGENT-MULTI-AGENT [具体正文](../../../../books/part-07-agent/82-multi-agent.md) |
| [WeaveTime: Stream from Earlier Frames into Emergent Memory in VideoLLMs](https://arxiv.org/abs/2602.22142v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:14:54+08:00 | temporalreconstructobjective教order+uncertaintytriggeredhistoryretrieval恢复strictstreamcausality；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [NoLan: Mitigating Object Hallucinations in Large Vision-Language Models via Dynamic Suppression of Language Priors](https://arxiv.org/abs/2602.22144v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:14:57+08:00 | multimodalvslanguageonly分布差动态suppressdecoderprior，因果inputcontrols定位hallucination；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [When AI Writes, Whose Voice Remains? Quantifying Cultural Marker Erasure Across World English Varieties in Large Language Models](https://arxiv.org/abs/2602.22145v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:14:59+08:00 | semanticsimilarity高仍抹culturalmarkers，IER/SPS双指标纠正preservation评价；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md) | 争议 | 暂缓：中心marker成员/IER分母争议：每条至少1marker却1490texts仅624instances，IER排baseline但表n1490/7450；不采用身份损失量化。重开需冻结成员、有效IER人口与一致权重/表格。 |
| [Provable Last-Iterate Convergence for Multi-Objective Safe LLM Alignment via Optimistic Primal-Dual](https://arxiv.org/abs/2602.22146v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:15:00+08:00 | optimisticprimaldual lastiterateparametrizederrorneighborhood保证改变safeRLHF收敛解释；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md) | 争议 | 暂缓：中心参数化last-iterate保证争议：原假设容许θ=0 score/Jacobian/Fisher全零、精确NPG不动而类内更优policy存在；不采用Cor3.10保证。重开需排除退化的额外expressivity/update条件或收窄定理。 |
| [CoLoGen: Progressive Learning of Concept`-`Localization Duality for Unified Image Generation](https://arxiv.org/abs/2602.22150v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:15:06+08:00 | 同空间联合训练与staged专家反侧；representation分责而非新MoE原理；2+1+2=5；[证据](../_sources/daily-20260227/V3_CLARIFY4_EVIDENCE.md) | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [具体正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [LLMTailor: A Layer-wise Tailoring Tool for Efficient Checkpointing of Large Language Models](https://arxiv.org/abs/2602.22158v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:15:21+08:00 | 跨checkpointlayerweight+optimizerstate按update选择合并复合snapshot，恢复identity不等普通save；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md) | 标准完成 | 已有覆盖：`TRAIN-CHECKPOINT` [具体正文](../../../../books/part-04-training-system/35-checkpoint.md)；有界近似恢复正文已覆盖layer weight/moments配对与跨step非coherent恢复；保预regroup条件、Table4解释反向和restore成本。 |
| [DySCO: Dynamic Attention-Scaling Decoding for Long-Context LMs](https://arxiv.org/abs/2602.22175v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:15:46+08:00 | retrievalheads动态选择/缩放contextattention提升longcontextdecoding，额外compute条件；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md) | 深入完成 | 整合：MODEL-LONG-CONTEXT [具体正文](../../../../books/part-02-model/22-long-context.md) |
| [GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL](https://arxiv.org/abs/2602.22190v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:16:07+08:00 | GUIpartialverifiability负gradient可靠性/ KLtrustregion/offlineonlinegap与actionawareSFT；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md) | 深入完成 | 整合：TRAIN-GRPO [具体正文](../../../../books/part-04-training-system/33-grpo.md) |
| [Improving Parametric Knowledge Access in Reasoning Language Models](https://arxiv.org/abs/2602.22193v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:16:12+08:00 | math-trainedreasoning未优化worldknowledgeaccess，cue/RLTriviaQA的taskconditional边界；2+1+2=5；[证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md) | 标准完成 | 已有覆盖：`WORLDVIEW-LLM-INTELLIGENCE` [具体正文](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md)；接口elicitation与内部知识/因果分责实际已覆盖；保MATH cue反退、训练集evaluation与RL/SFT预算不等。 |
| [Off-The-Shelf Image-to-Image Models Are All You Need To Defeat Image Protection Schemes](https://arxiv.org/abs/2602.22197v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:16:18+08:00 | off-the-shelfimg2img可移除多种保护扰动，而非只需专门adaptiveattacker；防御评价威胁模型必须包含一般生成修复路径，安全必要深入。；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md) | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [具体正文](../../../../books/part-06-ai-infrastructure/72-security.md)；一般变换/quality/原decoder/threat-model分责已覆盖；保8prompt搜索、PRC/VINE不同协议与selected失败人口，不授全保护失败。 |
| [Solaris: Building a Multiplayer Video World Model in Minecraft](https://arxiv.org/abs/2602.22208v1) | 2026-02-26T09:00:00+08:00 ～ 2026-02-26T11:16:34+08:00 | 同步multiagentactions/viewsworldmodel+self-forcingcheckpointing改变multiplayerconsistency状态；2+2+2=6；[证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md) | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [具体正文](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Nano Banana 2 原始release](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/) | 2026-02-27T00:00:00+08:00 | 高量生成/速度目标release事实；1+1+2=4，旧版spec未恢复不采用 | 已关闭 | 仅报告：只保原始事件与目标，非未恢复机制 |

## 4. 证据与知识整合

### [Robust AI Evaluation through Maximal Lotteries](https://arxiv.org/abs/2602.21297v1)

实际读取精确[v1正文](https://arxiv.org/html/2602.21297v1)完整题摘、§3 Def1–2、§4 Def4–5/§4.2 Def16与Eq2/LP、§5 Fig3–4与Discussion。固定各组margin `M_k`，在TV权重集合 `W` 内对最坏人口及对手优化模型彩票，新增的是可定义的评价选择分支，不是将成熟minimax名称当新机制。半径增大交换低组与强组表现；原20% held-out、200 bootstrap只支持受测偏好人口，没有证明回答正确、组内漂移/未知群体鲁棒性或发布策略。Theorem19固定组矩阵、iid组标签的条件不推广成全部margin估计误差界；未采用附录公理、稀疏定理或通用收敛承诺。统计比较不运行LLM推理，hardware/precision/length/batch/concurrency/SLO未披露；论文输入token价格不是总服务费/延迟。矩阵采集、半径/群组选择与LP计算均计成本，支持不足时保留切片、描述性portfolio及校准聚合结果。Ch66原有population/portfolio论点之后实际补入目标、权重身份、取舍与回退；独立复核者 `feb27_final_gate` 已核必要原源和owner差额，实际写后仍待最终定点验收。没有核代码或复现实验。

日期：Submitted=`2026-02-24T19:01:11Z`严格晚于前一announcement截止，Registered=`2026-02-26T02:53:49Z`作上界；按本日记录中同一availability规则得 `[2026-02-26T09:00:00+08:00,2026-02-26T10:53:50+08:00)`，完全落窗。此前DATE隔离纠正为IN；21941反向纠正为DATE。二者净替换，仍为108候选家族。

有效的既有原证/owner审阅定点复用；非原packet作者 `feb27_close_oct06` 独核22项必要原证与直接反侧，root逐owner核本轮原29处实写，最终独立复核者 `feb27_final_gate` 核新增21297及全部拟入选日期/判断和风险排除项。撤除日期未证的21941旧采用后，累计62整合、38已有覆盖、1仅报告、7中心争议，共108家族。这里的深入/标准完成指拟采用命题已读足必要证据，不声称已核代码、复现实验或证明论文全部主张。

### [SymTorch: A Framework for Symbolic Distillation of Deep Neural Networks](https://arxiv.org/abs/2602.21307v1)

投影坐标上的函数代理：分别验投影误差与代理误差，full-forward吞吐不外推decode。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data](https://arxiv.org/abs/2602.21320v1)

Generator/Solver互补self-play reward从能力前沿生成tool任务改变RL数据课程。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Dynamic Symmetric Point Tracking: Tackling Non-ideal Reference in Analog In-memory Training](https://arxiv.org/abs/2602.21321v1)

器件对称参考点与loss驻点分开；混合gradient坐标/EMA动态校准与额外模拟state。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXT4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [HiPPO Zoo: Explicit Memory Mechanisms for Interpretable State Space Models](https://arxiv.org/abs/2602.21340v1)

HiPPO显式polynomialmemory自适应allocation/associative结构可解释SSM状态形成。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Scaling View Synthesis Transformers](https://arxiv.org/abs/2602.21341v1)

compute-matched encoder-decoder NVS scaling反驳decoder-only最优归因，需核architecture/预算。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXT4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Alignment-Weighted DPO: A principled reasoning approach to improve safety alignment](https://arxiv.org/abs/2602.21346v1)

reasoning/finalanswer分段weightedDPO改变jailbreak浅refusal与utility取舍。非原packet作者 feb27_close_oct06 独立必要源/actual owner PRE通过并按窄段写入；root实际正文/完整邻接与自身末注POST通过，写入ownership已释放。语义两段独立loss/proxy与不完备guard接口；root已核实际正文162及邻接/末注473。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Black-Box Reliability Certification for AI Agents via Self-Consistency Sampling and Conformal Calibration](https://arxiv.org/abs/2602.21368v1)

有限样本认证、同校准集反选α与候选集合真值量词的中心冲突。root必要原文已核；中心冲突安全隔离，不采用外围成熟原则替代本项准入命题，不写Books。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Interleaved Head Attention](https://arxiv.org/abs/2602.21371v1)

跨headqkv线性混合pseudoheads组合token关系而非独立H矩阵。非原packet作者 feb27_close_oct06 独立必要源/actual owner PRE通过并按窄段写入；root实际正文/完整邻接与自身末注POST通过，写入ownership已释放。softmax前head混合/虚拟位置与P²预算；root已核正文94及邻接/末注330。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [MMLoP: Multi-Modal Low-Rank Prompting for Efficient Vision-Language Adaptation](https://arxiv.org/abs/2602.21397v1)

lowrank跨层prompt与共享up-projection/zero-shot anchors实现parameter-accuracy取舍。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [FlowFixer: Towards Detail-Preserving Subject-Driven Generation](https://arxiv.org/abs/2602.21402v1)

语义CLIP/DINO分数高仍可丢关键细节；matching keypoints作为不同fidelity观测，并以单步去噪造高频损失训练对。拟仅detail/semantic评估对象差额。。非原packet作者 feb27_close_oct06 已核必要精确v1、关键反侧与实际owner正文/邻接；已有覆盖通过，无Books修改。目标粒度、scorer/proxy和人工锚点已覆盖；保AKI被copy-paste放大反侧与局部人评人口。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Overconfident Errors Need Stronger Correction: Asymmetric Confidence Penalties for Reinforcement Learning](https://arxiv.org/abs/2602.21420v1)

policy/reference confidence shift只加强过度reinforced负advantage，修正Pass1/Passk探索取舍。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [On the Structural Non-Preservation of Epistemic Behaviour under Policy Transformation](https://arxiv.org/abs/2602.21424v1)

信息条件policyseparation不被convexmix/biasedpriorgradient保留，probe条件理论反侧。非原packet作者 feb27_close_oct06 已定点核精确v1必要机制、直接反侧及实际owner相邻正文；已有覆盖通过，不改Books。固定probe条件行为与平均reward分开；保留Stage1 +5→Stage2 +1混杂，不采用无条件policy-mix保持定理。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [PSF-Med: Measuring and Explaining Paraphrase Sensitivity in Medical Vision Language Models](https://arxiv.org/abs/2602.21428v1)

只采用paraphrase consistency不等visual grounding及SAE causal patch控制命题，不采用医疗决策结论。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXT4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Provably Safe Generative Sampling with Constricting Barrier Functions](https://arxiv.org/abs/2602.21429v1)

噪声到终态constricting safety tube离散CBF/QP过滤改变flow采样约束保证。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXT4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [MINAR: Mechanistic Interpretability for Neural Algorithmic Reasoning](https://arxiv.org/abs/2602.21442v1)

GNNalgorithmiccircuits patching识别multi-taskreuse/formation，模型能力机理非领域应用。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [VLA Knows Its Limits](https://arxiv.org/abs/2602.21445v1)

chunk预测长度与实际执行前缀分开，attention代理adaptive horizon。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Adversarial Intent is a Latent Variable: Stateful Trust Inference for Securing Multimodal Agentic RAG](https://arxiv.org/abs/2602.21447v1)

跨检查点风险summary与多阶段相关失败；持久state不等校准posterior。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [When Learning Hurts: Fixed-Pole RNN for Real-Time Online Training](https://arxiv.org/abs/2602.21454v1)

small-data实时RNN固定pole的条件与optimizer landscape负面证据。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXT5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [VecGlypher: Unified Vector Glyph Generation with Language Models](https://arxiv.org/abs/2602.21461v1)

直接AR SVG serialization替代raster后处理，coordinate/两阶段训练消融刻画表示质量边界。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXT5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Geometric Priors for Generalizable World Models via Vector Symbolic Architecture](https://arxiv.org/abs/2602.21467v1)

latent group结构以complex multiplication承载动作composition，gridworld局部world-model边界。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXT5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [The Design Space of Tri-Modal Masked Diffusion Models](https://arxiv.org/abs/2602.21472v1)

trimodal masked-diffusion modality/noise/batch研究，物理与逻辑batch解耦的SDE重参数。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXT5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Pancake: Hierarchical Memory System for Multi-Agent LLM Serving](https://arxiv.org/abs/2602.21477v1)

agent ANN index层级缓存、跨agent协调与GPUCPU协作，真实owner RAG索引而非KV/HBM。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXT5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Both Ends Count! Just How Good are LLM Agents at "Text-to-Big SQL"?](https://arxiv.org/abs/2602.21480v1)

TexttoBigSQL任务规模下accuracy不等execution cost的评价盲区。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [GradAlign: Gradient-Aligned Data Selection for LLM Reinforcement Learning](https://arxiv.org/abs/2602.21492v1)

trusted validation gradient对齐选RL problems而非accuracy过滤，适用reward噪声/非平稳数据。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Beyond Refusal: Probing the Limits of Agentic Self-Correction for Semantic Sensitive Information](https://arxiv.org/abs/2602.21496v1)

SemSI editing构造rewrite与truncate的capacity界及reasoning privacy-utility反侧。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [See It, Say It, Sorted: An Iterative Training-Free Framework for Visually-Grounded Multimodal Reasoning in LVLMs](https://arxiv.org/abs/2602.21497v1)

候选受限decider、同图派生sentence evidence与真实acquisition分责；raw margin非校准。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_CLARIFY4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Easy3E: Feed-Forward 3D Asset Editing via Rectified Voxel Flow](https://arxiv.org/abs/2602.21499v1)

2D edit通过sparsevoxel flow改变3D结构，normal-guided外部appearance恢复压缩表示丢高频；geometry与appearance prior分责。。非原packet作者 feb27_close_oct06 已核必要精确v1、关键反侧与实际owner正文/邻接；已有覆盖通过，无Books修改。geometry/control与appearance prior分责已覆盖；保25-step与75秒全链、silhouette/生成多视角非真值。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [WaterVIB: Learning Minimal Sufficient Watermark Representations via Variational Information Bottleneck](https://arxiv.org/abs/2602.21508v1)

watermarkmessage信息bottleneck过滤covertexture减少regenerationattack脆弱性，需核necessary保证。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [I/O Optimizations for Graph-Based Disk-Resident Approximate Nearest Neighbor Search: A Design Space Exploration](https://arxiv.org/abs/2602.21514v1)

ANN page复杂度把路径长度和页locality共同计价；sameimplementation/factorial揭page shuffle/search单独弱联合有用，需严格I/O模型与召回预算。。非原packet作者 feb27_close_oct06 独立必要源/actual owner PRE通过并按窄段写入；root实际正文/完整邻接与自身末注POST通过，写入ownership已释放。page locality×consumer expansion与饱和SSD多读反侧；root已核正文227及邻接/末注1260。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Training Generalizable Collaborative Agents via Strategic Risk Aversion](https://arxiv.org/abs/2602.21515v1)

strategic risk aversion抑制协作free-riding/未知partner失败，实际LLM协作受限机制。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [LiLo-VLA: Compositional Long-Horizon Manipulation via Linked Object-Centric Policies](https://arxiv.org/abs/2602.21531v1)

transport/global reach与object-centric interaction拆分改变长任务错误恢复/skill组合。非原packet作者 feb27_close_oct06 已定点核精确v1必要机制、直接反侧及实际owner相邻正文；已有覆盖通过，不改Books。verified skills、fresh observation与局部恢复实际已覆盖；GT checker、人验、重复尝试和36/27统计冲突保留，不授物理undo。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning](https://arxiv.org/abs/2602.21534v1)

四维policy-gradient controlled instability拆解与SAMPO改变agent RL稳定训练。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Enhancing Multilingual Embeddings via Multi-Way Parallel Text Alignment](https://arxiv.org/abs/2602.21543v1)

multiwayparalleltextvsEnXcontrastive控制crosslingualalignment，既有embedding升级边界。非原packet作者 feb27_close_oct06 独立必要源/actual owner PRE通过并按窄段写入；root实际正文/完整邻接与自身末注POST通过，写入ownership已释放。translation group/all-language anchor与预算人口分责；root已核正文272及邻接/末注1261。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Muon+: Towards Better Muon via One Additional Normalization Step](https://arxiv.org/abs/2602.21545v1)

Muon polar不消除row/column imbalance，postpolar单归一化改变optimizer下降条件。非原packet作者 feb27_close_oct06 已定点核精确v1必要机制、直接反侧及实际owner相邻正文；已有覆盖通过，不改Books。post-polar归一与variance state/order分责已覆盖；Table15仅有限matched LR对照，保搜索费与非交换归一。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [RAC: Relation-Aware Cache Replacement for Large Language Models](https://arxiv.org/abs/2602.21547v1)

topic prevalence/structural reuse信号替代短recency-frequency的语义cache驱逐。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM Inference](https://arxiv.org/abs/2602.21548v1)

storage到decode再RDMA到prefill双路径使用idle NIC打破PD存储瓶颈。非原packet作者 feb27_close_oct06 独立必要源/actual owner PRE通过并按窄段写入；root实际正文/完整邻接与自身末注POST通过，写入ownership已释放。DE代读仍回PE计算miss、完整prompt后才DE H2D；root已核正文438–456及完整邻接/末注589。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Training-free Composition of Pre-trained GFlowNets for Multi-Objective Generation](https://arxiv.org/abs/2602.21565v1)

pretrainedGFlowNets linearreward exact/nonlinear distortion composition理论，非采用molecule科学应用。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTI8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Duel-Evolve: Reward-Free Test-Time Scaling via LLM Self-Preferences](https://arxiv.org/abs/2602.21585v1)

pairwise selfpreferences+Bayesian BradleyTerry/Thompson分配search预算替代scalar evaluator。非原packet作者 feb27_close_oct06 已定点核精确v1必要机制、直接反侧及实际owner相邻正文；已有覆盖通过，不改Books。有限candidate comparison graph/query-local状态和独立oracle已覆盖；保MAP/Laplace近似、discarded ties与全生成/judge预算。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTH8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [CADC: Content Adaptive Diffusion-Based Generative Image Compression](https://arxiv.org/abs/2602.21591v1)

diffusion codec quantization-distortion/noise prior与auxdecoder信息压缩改变rate-perception取舍。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Breaking Semantic-Aware Watermarks via LLM-Guided Coherence-Preserving Semantic Injection](https://arxiv.org/abs/2602.21593v1)

embedding约束coherent语义改变击穿semantic watermark的安全反侧。非原packet作者 feb27_close_oct06 已定点核必要精确v1与决定性反侧；中心争议安全隔离，不支持正面证据/Books/保证。中心ASR人口/阈值争议：ASR=编辑后仍阳性，但最低72>阈值12与Table81%无法合并；仅报告原事实、不正面采用。重开需same-image编辑成功标签、检测统计/阈值、表/图有效分母。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [SPOC: Safety-Aware Planning Under Partial Observability And Physical Constraints](https://arxiv.org/abs/2602.21595v1)

partialobservability/physicalconstraint onlineplanning评价隐含hazard失效边界。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_REMAIN4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [A Hidden Semantic Bottleneck in Conditional Embeddings of Diffusion Transformers](https://arxiv.org/abs/2602.21596v1)

conditional embedding高angular冗余与pruning少维度不损质量，改变conditioning预算。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [AQR-HNSW: Accelerating Approximate Nearest Neighbor Search via Density-aware Quantization and Multi-stage Re-ranking](https://arxiv.org/abs/2602.21600v1)

densityadaptiveANNquant与multistagererank改变RAGindex recall/cost，需核graphbuild/真实配置。非原packet作者 feb27_close_oct06 已定点核必要精确v1与决定性反侧；具体已有覆盖通过，无Books修改。coarse navigation→低成本精化→原向量重排已覆盖；原PDF仅uniform8bit与density percentile，保5000sample、earlystop非exact、total memory与billion实测不支持。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Structurally Aligned Subtask-Level Memory for Software Engineering Agents](https://arxiv.org/abs/2602.21611v1)

episode级memory与subtask functional decomposition错配，改变SWE存取更新granularity。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [When More Is Less: A Systematic Analysis of Spatial and Commonsense Information for Visual Spatial Reasoning](https://arxiv.org/abs/2602.21619v1)

singleprecisecue胜multi-context/excesscommonsense、CoT须先ground的受控负面VSR边界。非原packet作者 feb27_close_oct06 已定点核必要精确v1与决定性反侧；具体已有覆盖通过，无Books修改。派生cue的可消费性与可靠性分责已覆盖；保按效果排序/amount+relevance混杂，未采用cognitive-overload因果定律。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation](https://arxiv.org/abs/2602.21622v1)

tactile纠正grasp/共享TCP图coordination与独立policy边界，需核adaptive modality实际贡献。非原packet作者 feb27_close_oct06 已定点核必要精确v1与决定性反侧；具体已有覆盖通过，无Books修改。真实contact、任务gate和physical controller责任已覆盖；全TCP共享、仿真/真机futurework、70/30数据未隔离均保留。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Multi-Layer Scheduling for MoE-Based LLM Reasoning](https://arxiv.org/abs/2602.21626v1)

request/engine/expert三层load与expertdependency placement调度边界，避免把SJF成熟算法当新增。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTJ8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Tokenizing Semantic Segmentation with RLE](https://arxiv.org/abs/2602.21627v1)

mask由densepixel改为RLE token序列，视频长度/instanceidentity编码取舍；需有限core核编码具体差额，非RLE本身新。。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning](https://arxiv.org/abs/2602.21628v1)

competence-based reward rubric分层权重改变RL curriculum而非仅采样题。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Self-Correcting VLA: Online Action Refinement via Sparse World Imagination](https://arxiv.org/abs/2602.21633v1)

sparse future progress/trajectory heads作为内部future feedback在线action refinement。非原packet作者 feb27_close_oct06 已定点核必要精确v1与决定性反侧；中心争议安全隔离，不支持正面证据/Books/保证。中心state-guide坐标争议：Eq8 local位移与Eq13/14 world位移直接相加/点积；不静默补R_t。重开需同版实际reward坐标/旋转与Fig4对应；SPI独立经验保留但不冒充OAR真机。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Scalable Multilingual Multimodal Machine Translation with Speech-Text Fusion](https://arxiv.org/abs/2602.21646v1)

同text的synthetic/authentic语音对照；派生模态引入TTS prior但非新环境观测。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_CLARIFY4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Sparsity Induction for Accurate Post-Training Pruning of Large Language Models](https://arxiv.org/abs/2602.21652v1)

中心等价与fast-refresh原定义冲突；有限表格不恢复中心主张。root必要原文已核；中心冲突安全隔离，不采用外围成熟原则替代本项准入命题，不写Books。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [CCCaption: Dual-Reward Reinforcement Learning for Complete and Correct Image Captioning](https://arxiv.org/abs/2602.21655v1)

caption completeness与correctness分reward抛开不全人类gold监督，需核judge/质量代价。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [DWA-KD: Dual-Space Weighting and Time-Warped Alignment for Cross-Tokenizer Knowledge Distillation](https://arxiv.org/abs/2602.21669v1)

cross-tokenizer双空间entropy加权与SoftDTW lexical/context alignment明确词表/序列边界。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTB5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Primary-Fine Decoupling for Action Generation in Robotic Imitation](https://arxiv.org/abs/2602.21684v1)

离散mode选择→条件连续residual；one-NFE不等去除码本/分类训练费用。非原packet作者 feb27_close_oct06 已核必要精确v1、关键反侧与实际owner正文/邻接；已有覆盖通过，无Books修改。粗mode→连续细动作与错误路由/码本/监督切换已覆盖；one-NFE不免前置训练，total variance不授预测mode保证。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [EditFlow: Benchmarking and Optimizing Code Edit Recommendation Systems via Reconstruction of Developer Flows](https://arxiv.org/abs/2602.21697v1)

last-edit-only合法动作错拒的条件性推断，与有限人注/多模型recall分账。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_REMAIN4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2602.21704v1)

truthfulness/perception不同head+semantic-dependent vectors驱动动态activation steering。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTB5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [TranX-Adapter: Bridging Artifacts and Semantics within MLLMs for Robust AI-generated Image Detection](https://arxiv.org/abs/2602.21716v1)

uniform artifact attention dilution与OT/crossattention互融的受限fusion机制。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTB5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations](https://arxiv.org/abs/2602.21723v1)

reference-free DF条件surface/gradient/velocity，由privilegedDF latent蒸馏到egodepth部署；真实观测/几何prior与条件迁移成本。。非原packet作者 feb27_close_oct06 已核必要精确v1、关键反侧与实际owner正文/邻接；已有覆盖通过，无Books修改。privileged teacher与runtime observation分责已覆盖；保不可见背部contact、视觉/teacher真机人口差异及DAgger费用。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild](https://arxiv.org/abs/2602.21736v1)

inverse dynamics+realaction jointly aligned latent action替代fullvisualreconstruct用于wildvideo VLA预训练。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTB5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Enhancing Multi-Modal LLMs Reasoning via Difficulty-Aware Group Normalization](https://arxiv.org/abs/2602.21743v1)

perception entropy/uncertainty regroup共享std的GRPO multimodal归一化。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTB5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Accelerating Diffusion via Hybrid Data-Pipeline Parallelism Based on Conditional Guidance Scheduling](https://arxiv.org/abs/2602.21760v1)

降序schedule令parallel elseif分支不可达；性能表不修复中心算法。必要原文已核；最终独立复核发现旧Books仍有正面调度残留，本轮撤除Ch24仅属于21760的段落和自身末注，保留原证及重开条件，不以外围成熟原则替代中心采用。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Easy to Learn, Yet Hard to Forget: Towards Robust Unlearning Under Bias](https://arxiv.org/abs/2602.21773v1)

bias-aligned forget可能反而提高目标classaccuracy，指出shortcutunlearning与causal/bias梯度路径分账。安全项必要深入。。非原packet作者 feb27_close_oct06 已核必要精确v1、关键反侧与实际owner正文/邻接；已有覆盖通过，无Books修改。合法retain泛化、删除影响和行为/probe分责已覆盖；保forget-class accuracy增反例及loss方向冲突，不采sharpness因果。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [From Statics to Dynamics: Physics-Aware Image Editing with Latent Transition Priors](https://arxiv.org/abs/2602.21778v1)

pairedimageboundary不足physicaltransition监督，learnedtimequeries用视频trajectory补causaledit。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Beyond Static Artifacts: A Forensic Benchmark for Video Deepfake Reasoning in Vision Language Models](https://arxiv.org/abs/2602.21779v1)

staticartifact与temporalgrounding/forensicreasoning三层benchmark揭video评价盲区。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [XStreamVGGT: Extremely Memory-Efficient Streaming Vision Geometry Grounded Transformer with KV Cache Compression](https://arxiv.org/abs/2602.21780v1)

stream3D causalKV固定预算prune+dimadaptivequant的kernelfriendly质量/记忆取舍。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [DHP: Efficient Scaling of MLLM Training with Dynamic Hybrid Parallelism](https://arxiv.org/abs/2602.21788v1)

精确v1DHP：异构MLLM动态nonpowerdegree混合并行/通信组与毫秒规划，不沿用后版FCP通用LLM宣传。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and Spatial Hand-Object Representations](https://arxiv.org/abs/2602.21811v1)

handobjectgeometry/representation旧dexterous任务性能，最小core看是否新可泛化condition/真实输入假设，不凭单camera泛化宣传。。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_REMAIN4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v1)

dualstreamMMDiT audiovisualjoint+concat统一inpainting+低分辨率sequence/highreskeyframe取舍。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [DocDjinn: Controllable Synthetic Document Generation with VLMs and Handwriting Diffusion](https://arxiv.org/abs/2602.21824v1)

seedcluster参数化sampling与语义visual解耦合成doc训练data控制real样本预算。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTD5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [FewMMBench: A Benchmark for Multimodal Few-Shot Learning](https://arxiv.org/abs/2602.21854v1)

instruction-tuned多模态fewshot/CoT可regress且retrieval/context未救回的评价反侧。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTD5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [DynamicGTR: Leveraging Graph Topology Representation Preferences to Boost VLM Capabilities on Graph QAs](https://arxiv.org/abs/2602.21864v1)

同graph固定visual/text格式对不同task/model不合适，query-level representationrouting需冻结utility/brevity与格式等价；是否新路由/blindspot须有限核。。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTL7_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection](https://arxiv.org/abs/2602.21887v1)

thinkinglanguage作为onpolicy RL action扩探索，同budget nonEnglish增量。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTD5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [A task-based data-flow methodology for programming heterogeneous systems with multiple accelerator APIs](https://arxiv.org/abs/2602.21897v1)

CUDA/SYCL/Triton跨native执行dependence与threadpool统一管理避免oversubscription，训练runtime互操作。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [EmoOmni: Bridging Emotional Understanding and Expression in Omni-Modal LLMs](https://arxiv.org/abs/2602.21900v1)

ThinkerTalker hidden接口丢情绪信息，用ECoT显式高层指令handoff改变omnimodal表示。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTD5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Learning in the Null Space: Small Singular Values for Continual Learning](https://arxiv.org/abs/2602.21919v1)

fixedsmall-singularbasis weightLoRAupdates保旧inputnullspace，比gradientprojection不同continuallearning机制。非原packet作者 feb27_close_oct06 已定点核必要精确v1与决定性反侧；具体已有覆盖通过，无Books修改。低干扰subspace proposal与retention gate已覆盖；保past/current输入身份冲突，weight decay不授hard spectral bound，有限经验不推出zero forgetting。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。


### [Large Language Models are Algorithmically Blind](https://arxiv.org/abs/2602.21947v1)

LLM预测algorithm性能区间与真实executions校准失败，修正declarativeknowledge推算性能。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTE5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [MEDSYN: Benchmarking Multi-EviDence SYNthesis in Complex Clinical Cases for Multimodal Large Language Models](https://arxiv.org/abs/2602.21950v1)

文本/图像移除对照揭示证据合成盲区；不收医学部署结论。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_REMAIN4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [MindDriver: Introducing Progressive Multimodal Reasoning for Autonomous Driving](https://arxiv.org/abs/2602.21952v1)

semantic→futurephysicalimage→trajectory对齐progressive奖励明确VLA推理表示接口。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTE5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [When LoRA Betrays: Backdooring Text-to-Image Models by Masquerading as Benign Adapters](https://arxiv.org/abs/2602.21977v1)

独立分享LoRA作为texttrigger→targetvisual backdoor载体，冻结base而adapter拥有供应链写权；核benignutility/触发scope/真实防御反侧，安全必要深入。。非原packet作者 feb27_close_oct06 已核必要精确v1、关键反侧与实际owner正文/邻接；已有覆盖通过，无Books修改。生成链可变组件与实际adapter bytes/条件行为已覆盖；保双组件、容量不匹配与benign/多adapter退步，probe不授防御。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [CxMP: A Linguistic Minimal-Pair Benchmark for Evaluating Constructional Understanding in Language Models](https://arxiv.org/abs/2602.21978v1)

minimalpairs分离grammaticalacceptability和constructionmeaning的learnedability边界。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTE5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Enhancing LLM-Based Test Generation by Eliminating Covered Code](https://arxiv.org/abs/2602.21997v1)

coveragefeedback删已覆盖codeslice改变剩余context/iteration目标而非无界generate。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTE5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [World Guidance: World Modeling in Condition Space for Action Generation](https://arxiv.org/abs/2602.22010v1)

futureobservation压到actionconditionspace，预测condition+action而非整帧world，控制取舍。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTE5_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations](https://arxiv.org/abs/2602.22013v1)

visualdegradation与semanticdualpath/unidirectional隔离改变VisRAG retrievalgeneration共同错误。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTK6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [A Diversity Diet for a Healthier Model: A Case Study of French ModernBERT](https://arxiv.org/abs/2602.22014v1)

commensuratesize随机/多样性数据对照，小Frenchencoder也可改变pretrainingdata判断；不把不同训练时间/尺寸headline当matchedcompute。。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [FlowCorrect: Efficient Interactive Correction of Generative Flow Policies for Robotic Manipulation](https://arxiv.org/abs/2602.22056v1)

deploymentrelativehumanpose corrections局部flowpolicy adaptation无backboneretrain的记忆边界。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Semantic Partial Grounding via LLMs](https://arxiv.org/abs/2602.22067v1)

LLM语义partialgrounding裁剪PDDL对象/操作算子改变grounding成本与plancompleteness风险。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Language Models Exhibit Inconsistent Biases Towards Algorithmic Agents and Human Experts](https://arxiv.org/abs/2602.22070v1)

statedtrust和performance-conditioned bets偏差相反，评价格式不能代真实决策倾向。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Understanding Artificial Theory of Mind: Perturbed Tasks and Reasoning in Large Language Models](https://arxiv.org/abs/2602.22072v1)

perturbedfalsebelief reasoningchains/finalfaithfulness分离ToM与CoT反侧。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation](https://arxiv.org/abs/2602.22088v1)

视觉global在free-space导航，接触后force-local估interactionframe、hybridforce/positioncontrol；条件切换/坐标估计与真实contactfeedback分责。。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Learning to Drive is a Free Gift: Large-Scale Label-Free Autonomy Pretraining from Unposed In-The-Wild Videos](https://arxiv.org/abs/2602.22091v1)

unposedwildvideo sequence-levelmultiteacher pseudo4Drepresentation可video-centric autonomypretrain。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [PASTA: A Modular Program Analysis Tool Framework for Accelerators](https://arxiv.org/abs/2602.22103v1)

GPU驻留collect-and-analyze改变trace处理位置；device summary有损及total-profile成本分账。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_CLARIFY4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Don't stop me now: Rethinking Validation Criteria for Model Parameter Selection](https://arxiv.org/abs/2602.22107v1)

validationacc早停/同lossobjective checkpointselection反侧；test-best是事后oracle不作为可部署规则，小classifier不直接外推LLM。。非原packet作者 feb27_close_oct06 已核必要精确v1、关键反侧与实际owner正文/邻接；已有覆盖通过，无Books修改。selector与独立test目标分责已覆盖；同trajectory有限反证不授普遍lossES失败，未拒绝不等统计等价。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Probing the Geometry of Diffusion Models with the String Method](https://arxiv.org/abs/2602.22122v1)

stringmethod沿learnedscore探索MEPvsprincipalcurve，likelihoodmax不等perceptualrealism，不用protein科学应用。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [SWE-Protégé: Learning to Selectively Collaborate With an Expert Unlocks Small Language Models as Software Engineering Agents](https://arxiv.org/abs/2602.22124v1)

SLM soledecisionmaker learns遇stalledstate求expert及anti-loopreward，选择性delegation取舍。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [WeaveTime: Stream from Earlier Frames into Emergent Memory in VideoLLMs](https://arxiv.org/abs/2602.22142v1)

temporalreconstructobjective教order+uncertaintytriggeredhistoryretrieval恢复strictstreamcausality。root必要源/actual owner PRE，以及实际正文/完整邻接/自身末注POST均通过；自身末注已同步，窄lease释放。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTF8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [NoLan: Mitigating Object Hallucinations in Large Vision-Language Models via Dynamic Suppression of Language Priors](https://arxiv.org/abs/2602.22144v1)

multimodalvslanguageonly分布差动态suppressdecoderprior，因果inputcontrols定位hallucination。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [When AI Writes, Whose Voice Remains? Quantifying Cultural Marker Erasure Across World English Varieties in Large Language Models](https://arxiv.org/abs/2602.22145v1)

semanticsimilarity高仍抹culturalmarkers，IER/SPS双指标纠正preservation评价。非原packet作者 feb27_close_oct06 已定点核必要精确v1与决定性反侧；中心争议安全隔离，不支持正面证据/Books/保证。中心marker成员/IER分母争议：每条至少1marker却1490texts仅624instances，IER排baseline但表n1490/7450；不采用身份损失量化。重开需冻结成员、有效IER人口与一致权重/表格。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Provable Last-Iterate Convergence for Multi-Objective Safe LLM Alignment via Optimistic Primal-Dual](https://arxiv.org/abs/2602.22146v1)

optimisticprimaldual lastiterateparametrizederrorneighborhood保证改变safeRLHF收敛解释。非原packet作者 feb27_close_oct06 已定点核必要精确v1与决定性反侧；中心争议安全隔离，不支持正面证据/Books/保证。中心参数化last-iterate保证争议：原假设容许θ=0 score/Jacobian/Fisher全零、精确NPG不动而类内更优policy存在；不采用Cor3.10保证。重开需排除退化的额外expressivity/update条件或收窄定理。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [CoLoGen: Progressive Learning of Concept`-`Localization Duality for Unified Image Generation](https://arxiv.org/abs/2602.22150v1)

同空间联合训练与staged专家反侧；representation分责而非新MoE原理。root必要原源与真正承载命题的既有正文已独核通过；已有覆盖，无新写书。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_CLARIFY4_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [LLMTailor: A Layer-wise Tailoring Tool for Efficient Checkpointing of Large Language Models](https://arxiv.org/abs/2602.22158v1)

跨checkpointlayerweight+optimizerstate按update选择合并复合snapshot，恢复identity不等普通save。非原packet作者 feb27_close_oct06 已定点核精确v1必要机制、直接反侧及实际owner相邻正文；已有覆盖通过，不改Books。有界近似恢复正文已覆盖layer weight/moments配对与跨step非coherent恢复；保预regroup条件、Table4解释反向和restore成本。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [DySCO: Dynamic Attention-Scaling Decoding for Long-Context LMs](https://arxiv.org/abs/2602.22175v1)

retrievalheads动态选择/缩放contextattention提升longcontextdecoding，额外compute条件。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL](https://arxiv.org/abs/2602.22190v1)

GUIpartialverifiability负gradient可靠性/ KLtrustregion/offlineonlinegap与actionawareSFT。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Improving Parametric Knowledge Access in Reasoning Language Models](https://arxiv.org/abs/2602.22193v1)

math-trainedreasoning未优化worldknowledgeaccess，cue/RLTriviaQA的taskconditional边界。非原packet作者 feb27_close_oct06 已定点核精确v1必要机制、直接反侧及实际owner相邻正文；已有覆盖通过，不改Books。接口elicitation与内部知识/因果分责实际已覆盖；保MATH cue反退、训练集evaluation与RL/SFT预算不等。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Off-The-Shelf Image-to-Image Models Are All You Need To Defeat Image Protection Schemes](https://arxiv.org/abs/2602.22197v1)

off-the-shelfimg2img可移除多种保护扰动，而非只需专门adaptiveattacker；防御评价威胁模型必须包含一般生成修复路径，安全必要深入。。非原packet作者 feb27_close_oct06 已核必要精确v1、关键反侧与实际owner正文/邻接；已有覆盖通过，无Books修改。一般变换/quality/原decoder/threat-model分责已覆盖；保8prompt搜索、PRC/VINE不同协议与selected失败人口，不授全保护失败。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTM6_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Solaris: Building a Multiplayer Video World Model in Minecraft](https://arxiv.org/abs/2602.22208v1)

同步multiagentactions/viewsworldmodel+self-forcingcheckpointing改变multiplayerconsistency状态。非原packet作者必要原证/actual owner PRE与窄写完成；root已实际顺读正文、完整邻接与自身末注，POST通过。采用范围、关键原文坐标、直接反侧、评价人口与费用/回退，以及具体owner差额或Existing位置见[本项完整必要证据](../_sources/daily-20260227/V3_NEXTG8_EVIDENCE.md)；这里只采用该精确v1，不继承latest摘要或未读后版。

### [Nano Banana 2 原始release](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/)

官方JSON-LD原始published=2026-02-26T16:00:00Z，modified为Mar19；原release身份与高量/速度目标、changelog有限事实已由root独核，仅报告。当前更新正文不能冒充发布时机制规格；512/Thinking等旧版spec未恢复，不写Books、不采用性能/功能保证。请求与重开仅限原发布版本，见§5；[官方响应与时间依据](../_sources/daily-20260227/V3_FETCH_NANO.json)、`V3_NANO_DEV.raw`及`V3_NANO_CHANGELOG.txt`。

## 5. 缺口与下一步

普通可执行工作为0；候选必要审阅、62处实际Books整合、38具体已有覆盖、1仅报告及7中心争议隔离均已独立验收。本窗仅有下列外部/争议终态保留项，不用于正面证据、Books、无遗漏或保证；材料恢复时只按各项明确条件定点重开。


下列为已有限隔离的具体材料缺口，不是普通执行队列，也不构成额外候选分母：20项日期身份及未证落窗的具名历史事件不入108；Nano已入分母的原release仅报告，缺失spec只是受影响事实隔离。它们不用于新增正面证据、Books、无遗漏或性能/安全保证。

### 同ID首次公开日期缺口（20项）

以下保留项的Submitted不足以建立本窗公开下界；Registered只给官方公开上界，不能排除更早已公开。因此每项只请求**同ID精确v1首次announcement/公开列表记录，或可证明同版正文当时实际可得的官方公告**，不是更多全文或完整版本diff。当前same-ID官方历史公告不可得；Created/Updated和邻居ID不能作替代。取得上述材料后只重开该ID日期，完全落窗才重开准入/必要证据，不扫描整月。原字段见[日期材料](../_sources/daily-20260227/V3_DATE_PACKET.md)及对应raw。

| 保留身份 | 原Submitted v1（UTC） | 官方Registered（UTC，上界） | 当前不能采用/定点重开 |
| --- | --- | --- | --- |
| [Inference-time Alignment via Sparse Junction Steering](https://arxiv.org/abs/2602.21215v1) | 2026-01-30T08:40:47Z | 2026-02-26T02:51:46Z | 首公开未证完全落窗；仅恢复2602.21215v1同ID公告 |
| [Field-Theoretic Memory for AI Agents: Continuous Dynamics for Context Preservation](https://arxiv.org/abs/2602.21220v1) | 2026-01-31T04:33:28Z | 2026-02-26T02:51:53Z | 首公开未证完全落窗；仅恢复2602.21220v1同ID公告 |
| [Latent Context Compilation: Distilling Long Context into Compact Portable Memory](https://arxiv.org/abs/2602.21221v1) | 2026-01-31T08:38:07Z | 2026-02-26T02:51:55Z | 首公开未证完全落窗；仅恢复2602.21221v1同ID公告 |
| [Measuring Pragmatic Influence in Large Language Model Instructions](https://arxiv.org/abs/2602.21223v1) | 2026-02-02T06:52:37Z | 2026-02-26T02:51:57Z | 首公开未证完全落窗；仅恢复2602.21223v1同ID公告 |
| [Architecture-Agnostic Curriculum Learning for Document Understanding: Empirical Evidence from Text-Only and Multimodal](https://arxiv.org/abs/2602.21225v1) | 2026-02-02T10:09:26Z | 2026-02-26T02:52:01Z | 首公开未证完全落窗；仅恢复2602.21225v1同ID公告 |
| [Budget-Aware Agentic Routing via Boundary-Guided Training](https://arxiv.org/abs/2602.21227v1) | 2026-02-04T07:39:27Z | 2026-02-26T02:52:04Z | 首公开未证完全落窗；仅恢复2602.21227v1同ID公告 |
| [TRACE: Trajectory-Aware Comprehensive Evaluation for Deep Research Agents](https://arxiv.org/abs/2602.21230v1) | 2026-02-05T13:28:57Z | 2026-02-26T02:52:08Z | 首公开未证完全落窗；仅恢复2602.21230v1同ID公告 |
| [A General Equilibrium Theory of Orchestrated AI Agent Systems](https://arxiv.org/abs/2602.21255v1) | 2026-02-23T13:21:32Z | 2026-02-26T02:52:46Z | 首公开未证完全落窗；仅恢复2602.21255v1同ID公告 |
| [Structured Prompt Language: Declarative Context Management for LLMs](https://arxiv.org/abs/2602.21257v1) | 2026-02-23T17:03:31Z | 2026-02-26T02:52:49Z | 首公开未证完全落窗；仅恢复2602.21257v1同ID公告 |
| [Under the Influence: Quantifying Persuasion and Vigilance in Large Language Models](https://arxiv.org/abs/2602.21262v1) | 2026-02-24T04:09:21Z | 2026-02-26T02:52:57Z | 首公开未证完全落窗；仅恢复2602.21262v1同ID公告 |
| [Make Every Draft Count: Hidden State based Speculative Decoding](https://arxiv.org/abs/2602.21224v1) | 2026-02-02T08:25:21Z | 2026-02-26T02:51:59Z | 首公开未证完全落窗；仅恢复2602.21224v1同ID公告 |
| [ImpRIF: Stronger Implicit Reasoning Leads to Better Complex Instruction Following](https://arxiv.org/abs/2602.21228v1) | 2026-02-04T07:50:11Z | 2026-02-26T02:52:06Z | 首公开未证完全落窗；仅恢复2602.21228v1同ID公告 |
| [ACAR: Adaptive Complexity Routing for Multi-Model Ensembles with Auditable Decision Traces](https://arxiv.org/abs/2602.21231v1) | 2026-02-06T23:27:17Z | 2026-02-26T02:52:10Z | 首公开未证完全落窗；仅恢复2602.21231v1同ID公告 |
| [AngelSlim: A more accessible, comprehensive, and efficient toolkit for large model compression](https://arxiv.org/abs/2602.21233v1) | 2026-02-07T07:02:56Z | 2026-02-26T02:52:13Z | 首公开未证完全落窗；仅恢复2602.21233v1同ID公告 |
| [ToolMATH: A Math Tool Benchmark for Realistic Long-Horizon Multi-Tool Reasoning](https://arxiv.org/abs/2602.21265v1) | 2026-02-24T09:23:12Z | 2026-02-26T02:53:01Z | 首公开未证完全落窗；仅恢复2602.21265v1同ID公告 |
| [Group Orthogonalized Policy Optimization:Group Policy Optimization as Orthogonal Projection in Hilbert Space](https://arxiv.org/abs/2602.21269v1) | 2026-02-24T12:59:32Z | 2026-02-26T02:53:07Z | 首公开未证完全落窗；仅恢复2602.21269v1同ID公告 |
| [Neural network optimization strategies and the topography of the loss landscape](https://arxiv.org/abs/2602.21276v1) | 2026-02-24T17:49:13Z | 2026-02-26T02:53:17Z | 首公开未证完全落窗；仅恢复2602.21276v1同ID公告 |
| [Heterogeneous Memory Design Exploration for AI Accelerators with a Gain Cell Memory Compiler](https://arxiv.org/abs/2602.21278v1) | 2026-02-24T18:10:24Z | 2026-02-26T02:53:21Z | 首公开未证完全落窗；仅恢复2602.21278v1同ID公告 |
| [MERRY: Semantically Decoupled Evaluation of Multimodal Emotional and Role Consistencies of Role-Playing Agents](https://arxiv.org/abs/2602.21941v1) | 2026-02-24T02:53:58Z | 2026-02-26T03:09:56Z | Submitted早于前一公告截止；Registered只给上界，缺同ID首次公开下界，隔离且撤销本日Books采用；只需同版本公告/实际可得时间证明。原必要审阅保留，不将日期受阻作论文无效。 |
| [Task-Aware LoRA Adapter Composition via Similarity Retrieval in Vector Databases](https://arxiv.org/abs/2602.21222v1) | 2026-02-01T22:20:04Z | 2026-02-26T02:51:56.000Z | 首公开未证完全落窗；仅恢复2602.21222v1同ID公告 |

### 具体发布/历史目录材料

- [CUDA Agent，2602.24286](https://arxiv.org/abs/2602.24286v1)：arXiv Submitted=2026-02-27T18:58:05Z、Registered=Mar2；Seed目录PublishDate=Feb27 00BJT但Updated Apr23回填，项目页仅Feb27无时区。缺同事件原始首公开时刻及当时版本；目前只能相交不能证落窗，不评分、不全文、不Books。需官方原Feb26/27公告含TZ或旧版公开记录；只重开该release日期。[原字段](../_sources/daily-20260227/V3_DATE_2602.24286.raw)，不把后回填当时刻。
- [V-SONAR / Unified Vision-Language Modeling via Concept Space Alignment，2603.01096](https://arxiv.org/abs/2603.01096v1)：Meta目录Feb27与arXiv Mar1 Submitted/Mar3 Registered不能证明首次正文落窗；OpenReview旧2025稿存在公开线索但必要API403/challenge，当前version无法确定是首公开还是重要修订。缺官方旧稿公开时间/版本及Feb27精确事件说明；需samepaper带时间的OR旧版记录或官方版本公告，只重开该身份，必要时恢复真实归属日，不扩本窗。[有限日期记录](../_sources/daily-20260227/V3_META_VSONAR_DATE.txt)。PAHF 2602.16173已官方OAI Feb19上界证窗前，不重复全文或制造待审。
- [Nano Banana 2](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/)：原release只采用身份及高量/速度目标；Mar19 modified payload的512/Thinking等具体spec不可冒作Feb26原版。缺原published版本的spec正文，archive定点版本一次未恢复即止；只接受官方原发布快照/changelog具体旧spec引用，恢复后仅重开受影响spec，不推倒已核release事实。[有限版本请求](../_sources/daily-20260227/V3_FETCH_NANO_VERSION.json)。
- [Meta Research](https://ai.meta.com/research/)：原入口空/stub，publication page3只恢复上述具名线索；缺本窗原Research列表段，不能由辅助目录授整个覆盖。需本窗dated官方列表/原公告；仅恢复Feb26～27同主题发布段。
- [DeepSeek Research](https://www.deepseek.com/)：API updates已有限止Dec2025→Apr2026，但研究历史论文/技术发布目录缺段；API changelog不代替研究。需本窗官方dated研究目录或具体公告，只补该历史段。
- [Moonshot/Kimi Blog](https://platform.kimi.com/blog)：可取得目录24旧事件止Nov2025，本窗有界检索无新身份不证明零发布。缺Feb26～27 dated历史研究/技术发布段；需官方历史目录或同事件公告，只定点补该段。
- [MiMo Paper/Blog](https://mimo.xiaomi.com/)：Paper8条已有限止Feb3→Mar13，Blog仅旧Dec16和undated导航不能完整恢复本窗。需官方dated Blog历史段或明确本窗公告，恢复时只重开该时段；不将当前Paper零项授全部Blog覆盖。

### 中心争议终态（分母内7项）

- [21368](https://arxiv.org/html/2602.21368v1)：fixed-alpha条件被无条件搬到reliability、same-calibration α*反选、S∞只含已采候选却声称true覆盖。需修正中心量词/集合定义及相应协议的官方同版本澄清；不采用可靠性保证，不把外围conformal拆成新Books。[中心证据](../_sources/daily-20260227/V3_FIRST_EVIDENCE.md)。
- [21652](https://arxiv.org/html/2602.21652v1)：equivalent/fast-refresh中心与原操作定义冲突；需明确实际等价对象、refresh更新规则与匹配核心证据。不以有限Table1/2或Only标签抹掉中心争议，不写Books。[精确争议](../_sources/daily-20260227/V3_NEXTOTHER5_EVIDENCE.md)。
- [21760](https://arxiv.org/html/2602.21760v1)：降序t条件下τ2>τ1使parallel elseif不可达；需修正版algorithm/阈值顺序或同版实际实现解释，并说明表格对应何算法。质量表不修复中心调度，暂不采用该recipe。[决定依据](../_sources/daily-20260227/V3_NEXTC5_EVIDENCE.md)。

- [21593](https://arxiv.org/html/2602.21593v1)：中心ASR人口/阈值争议：ASR=编辑后仍阳性，但最低72>阈值12与Table81%无法合并；仅报告原事实、不正面采用。重开需same-image编辑成功标签、检测统计/阈值、表/图有效分母。 精确必要原证见对应§4链接。
- [21633](https://arxiv.org/html/2602.21633v1)：中心state-guide坐标争议：Eq8 local位移与Eq13/14 world位移直接相加/点积；不静默补R_t。重开需同版实际reward坐标/旋转与Fig4对应；SPI独立经验保留但不冒充OAR真机。 精确必要原证见对应§4链接。
- [22145](https://arxiv.org/html/2602.22145v1)：中心marker成员/IER分母争议：每条至少1marker却1490texts仅624instances，IER排baseline但表n1490/7450；不采用身份损失量化。重开需冻结成员、有效IER人口与一致权重/表格。 精确必要原证见对应§4链接。
- [22146](https://arxiv.org/html/2602.22146v1)：中心参数化last-iterate保证争议：原假设容许θ=0 score/Jacobian/Fisher全零、精确NPG不动而类内更优policy存在；不采用Cor3.10保证。重开需排除退化的额外expressivity/update条件或收窄定理。 精确必要原证见对应§4链接。

## 6. 复核

复核者：`feb27_final_gate`（未参与报告或Books写入的独立智能体）；root另承担原作者之外的分批原证/写后核验。

结论：通过

三处最终问题已定点修复并由独立复核者再核，不复跑其他有效材料。

实际范围：六部分及14每日来源、三主题API返回/总数/next停止、Seed/Qwen/Hunyuan有限目录边界及历史缺段隔离；107候选同ID日期原字段全核，另Nano原release/后修改字段分开。有效分批原证与owner审阅复用，62处实写逐项实际正文/邻接/末注写后完成；新21297与21941/21760撤除由最终独立复核者定点再核。

91排除项全查身份/题名和当前版本事件标记，完整题摘或必要core实际复查32/91：风险/反侧20项（21251、21351、21374、21394、21441、21485、21529、21550、21648、21677、21720、21873、21948、22120、21806、21833、21835、22125、22136、21800），普通分层12项（21216、21478、21597、21680、21772、21816、21862、22090、22157、21645、21698、21797）。未发现共同筛选错误；其余59题摘/全文本轮未重读，不将抽检称为全量原证审查。中心争议7项均无本日报正面Books残留；日期/历史入口保留项依合同隔离。

作者恢复执行已重新完整读取当前AGENTS、Research/Report/Prompt、daily/arxiv入口及ROADMAP与相关停点；固定窗口未移动，未扩Weekly/窗外/整类全文队列。局部原文纠偏已保在必要笔记：21600是uniform8bit＋density threshold而非region bitwidth；21548现有Books的miss-prefill路径已按原源具体纠正并获root实际POST；21633坐标冲突只隔离中心reward接口，不抹去独立SPI经验。没有重开已经稳定通过的候选。

机械检查：108唯一候选与108同URL证据标题、六部分、14来源、本地引用及V3格式/一致性校验通过；报告与本轮改动文件的限定diff检查通过。机械结果不证明研究语义，由上述独立复核承担判断。保护原有staged/unstaged改动，未stage、commit、push。
