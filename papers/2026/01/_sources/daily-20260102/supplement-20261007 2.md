# 2026-01-02 Daily 增量来源补查

**补充窗口：** 2026-01-01 ～ 2026-01-01（北京时间前一完整自然日）

**授权边界：** 保留旧报告窗口、104 个候选家族、日期归属、评分和有效审阅；这里只补遗漏，不改 README、Books 或 Learning State。

**本轮作者：** supp_jan02

**实际检查时间：** 2026-10-07 13:21～13:35 +08:00（包括后五项补检和最终格式核对）。
**状态：** 作者14源有限检查和15个具名新线索题摘已收尾；以下原始停点保留。root补查校准与当前必要审阅见文末；不沿用旧报告“完成”作为本轮验收，尚无本輪Books写入。

## 1. 可直接插入报告的增量（当前）

旧 arXiv 原始主题列表定点补读10项，fresh四主题缓冲再补读5项，合计15个具名查漏线索的精确v1完整题摘已经读完；未把257/116/93/143条原始返回建成逐项关闭队列。API的`published`是提交字段，不是公开日期。当前没有确认新增落Jan1的候选，不给正式评分、正面Evidence或Books采用。以下保留原始题摘、具体初筛判断与必要日期恢复点，交独立复核者校准；不因为摘要具有系统词汇、章节能映射或全文已可访问而准入。

mHC（2512.24880）已在本日旧报告有效审阅并落实 `MODEL-TRANSFORMER-LAYER`；此次官方研究索引仍能确认同一家族，直接去重，不重新深审、不重评分、不挪原日期。旧 104 个家族的机制结论和争议均复用，不因自然日补充窗口重新扩大它们的审阅。

## 2. 每日 14 源实际有界入口与停点

本次逐项请求下列官方入口；HTTP 200 只表示响应取得，不自动表示日期切片完成。仅使用指定主题/邻近日期段；不扫描每周分组，不要求证明全机构历史无删除。

| 来源 | 实际入口、原始响应与停止依据 | 当前结果与采用边界 |
| --- | --- | --- |
| SRC-OPENAI | [官方 RSS](https://openai.com/news/rss.xml) 200、761497 bytes；实际XML解析1251项，限定Dec2025/Jan2026日期段查看至邻近 Grove `Fri, 02 Jan 2026 10:00:00 GMT` 与 Atlas hardening `Mon, 22 Dec 2025 00:00:00 GMT`。中间一次无UA探针403不覆盖成功。目标仅Jan1研究发布日期切片。 | 已检查：该RSS日期切片无Jan1行。Grove窗外且只是cohort公告，不深审；不授全机构召回保证。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 本次200、280129 bytes；从SSR实际读publishedOn序列，Jan8 `critical-infrastructure-defense`与Dec19 `bloom`夹住Jan1，Dec18 `project-vend-2`在前，避免把illustration `_createdAt`误当研究日期。 | 已检查：取得的完整Publications序列目标切片无Jan1行；不把网页首屏当历史末页。 |
| SRC-GOOGLE-AI | [Research Jan2026 月档](https://research.google/blog/2026/01/) 200、173273 bytes，最早 Jan12，页面末无下一页；[DeepMind Blog](https://deepmind.google/discover/blog/) 200、197417 bytes，首页仅晚期条目、页码至19；[pubs?year=2026](https://research.google/pubs/?year=2026) 200、311521 bytes，却显示773页、无日级首公开字段。 | 月博客有限 Jan1 切片已检查，无落窗条目；pubs 年参数响应不能证明 Jan1 发布，DeepMind 尚未恢复对应历史页。缺的是这两个具体目录的 Jan1 原发布切片，不是全站无删除证明。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 200、281933 bytes，只能从可读层提取当前 Muse 标题；未得到 Jan1 日期列表。 | 受阻：必要目标日期切片不可提取。保留具体原目录问题，不以当前模型主页替代当日发布。 |
| SRC-QWEN | [旧Blog](https://qwenlm.github.io/)与[qwen.ai/research](https://qwen.ai/research)分别200、17283/92469 bytes；动态shell不作日期证据。按root给出的确切[官方API](https://qwen.ai/api/page_config?code=research.research-list)本轮fresh200、57340 bytes，返回60项数组，完整按date字段检查；非时间排序，最大date=2025-12-23，未取末项当时序停点。原响应也保留在[root本轮raw](../daily-20260104/supplement-20261007/qwen.raw)。 | 已检查：完整当前research-list的有限Jan1切片无行；不要求证明历史无删除，不因迁移shell另建全机构快照请求。 |
| SRC-DEEPSEEK | [研究与动态](https://www.deepseek.com/news/) 200、102358 bytes，研究索引 mHC Dec31 与 Engram Jan12 夹住补充窗口。 | 已检查：mHC 本日旧报告已处理，去重；Engram 窗外不扩审。没有新的落窗机制事件。 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)200、12227 bytes，本次全文可读26行dated目录，最近Nov7功能记录、Nov6 K2 Thinking、较旧至May2024；没有分页按钮，读完整有限日期序列后停止。 | 已检查：本入口无Jan1条目；不把K2旧事件重评分，不外推至全GitHub通知。 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) 200、6885 bytes shell；定点读 root 本轮恢复的 [publicList 原响应](../daily-20260104/supplement-20261007/hunyuan.raw)：`totalNum=9`、list9项，已到当前接口末项，最早 displayPublishTime=1770090898（2026-02-03），`publicAt` 单列，不混用。 | 这9项有限目录已检查，无 Jan1 行；不把晚于目标窗口的当前目录称为 Jan1 原始快照。若有具名 Jan1 公告才定点重开，不要求全机构历史补证。 |
| SRC-ZAI | [Research?page=2](https://www.zhipuai.cn/zh/research?page=2)本次200、1207016 bytes；SSR完整18个publication createAt原值读至`hasMore=false`，最邻近Dec21与Jan13；GLM-Image createAt Jan13、AutoGLM Dec8与CMS `createdAt=Jan7`区分。旧本日[page2记录](ZAI_PAGINATION.json)同样18/hasMore=false可复用身份。 | 已检查：该有限Research目录没有Jan1 createAt；不把CMS入库时间当公开。 |
| SRC-BYTEDANCE-SEED | 正确 `/api/get_article_list_v2`，article_type=1/2，publish_year=2026，order_desc=false，count20/page_token0：论文53501 bytes、total82/20条，博客16618 bytes、total23/20条；最早 PublishDate 分别1768838400000（Jan20）与1770825600000（Feb12），已跨过目标窗上界停止，不追后续晚页。2025降序博客15项最近Dec24；论文一次响应105 bytes仅total94/空sub-list，不能作零事件。2025论文具体原切片见本日 [有效原记录](SEED_API_RECOVERY.json)。 | 2026两类首日期切片与2025博客已检查；2025论文复用有效邻近字段，不拿空响应证明覆盖。未发现本窗原始发布条目。 |
| SRC-BAIDU-ERNIE | [官方Blog](https://ernie.baidu.com/blog/zh/) 200、26083 bytes，10个 dated article，Jan8 后到 Dec23/Dec9/Nov21，页面“下一页2/2”，已越过目标窗口下界停止。 | 已检查：无 Jan1 行；榜单短文不产生训练/推理机制贡献，窗外不深审。 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/) 200、58111 bytes，Paper与Blog目录可读；Blog15项仍无公开日期，More隐藏。旧Paper8项邻近Jan8/Sep19可复用。 | Paper有限切片已检查；Blog缺具名原文publication日期/历史停止字段，不由Paper无新项推出Blog无事件。 |
| SRC-MINIMAX | [Blog](https://www.minimax.io/blog) 200、134584 bytes，13个日期，最近邻 Jan27 与 Dec23；[Agent Tech](https://agent.minimax.io/docs/techblog) 200、211616 bytes，仅列May13单项。读至Dec23跨过窗下界，主Blog停止。 | 主Blog有限切片已检查无 Jan1 行；AgentTech当前唯一晚页不揭示Jan1目录。仅保留该栏目原历史入口问题，不假定栏目当时不存在。 |
| SRC-ARXIV | 本日旧[四主题原线索](ARXIV_THEME_RAW.json)/[缺段线索](ARXIV_DEFERRED_GAP_RAW.json)定点浏览Dec29～31相关标题，不将整类变队列。fresh cs.CL语义API97/97；随后四主题/12类same submittedDate缓冲Dec29 19Z～Jan1 00Z，max100：model257（100/100/57），runtime116（100/16），multimodal93（93），agent143（100/43），均最后start+实际条数=total停止；查询原值下节保存。`cs.CL/2601`与`cs.CL/20260101`400、cs.LG/2601一轮429；web cs.CL末页cache miss；[cs.LG月目录](https://arxiv.org/list/cs.LG/2025-12?show=2000)取得首2000/3465，仅核入口，未全月逐项筛。 | 有界来源检查收尾，公开日期覆盖受限：submittedDate/API published不证明公开，15题摘只查漏线索。holiday原页本轮200但日程不独自证明具体论文被接受/公告；潜在贡献须有dated官方身份列表/作者正文。缓冲混入晚月ID不按Jan1准入；不扩大身份队列、不核旧104日期。 |

## 3. 十项精确 v1 原始题摘与初筛

原始 API 请求：<https://export.arxiv.org/api/query?id_list=2512.24445v1%2C2512.24780v1%2C2512.24592v1%2C2512.24478v1%2C2512.24985v1%2C2512.25073v1%2C2512.24111v1%2C2512.24762v1%2C2512.24635v1%2C2512.24404v1&max_results=10>。实际返回10/10，逐项读完整摘要；下列 submitted 原值仅身份恢复，不作为公开归属。没有用 Weekly 补造候选。

### [Adaptive Learning Guided by Bias-Noise-Alignment Diagnostics](https://arxiv.org/abs/2512.24445v1)

API published/updated原值：`2025-12-30T19:57:52Z`（提交）。

> Learning systems deployed in nonstationary and safety-critical environments often suffer from instability, slow convergence, or brittle adaptation when learning dynamics evolve over time. While modern optimization, reinforcement learning, and meta-learning methods adapt to gradient statistics, they largely ignore the temporal structure of the error signal itself. This paper proposes a diagnostic-driven adaptive learning framework that explicitly models error evolution through a principled decomposition into bias, capturing persistent drift; noise, capturing stochastic variability; and alignment, capturing repeated directional excitation leading to overshoot. These diagnostics are computed online from lightweight statistics of loss or temporal-difference error trajectories and are independent of model architecture or task domain. We show that the proposed bias-noise-alignment decomposition provides a unifying control backbone for supervised optimization, actor-critic reinforcement learning, and learned optimizers. Building on this framework, we derive diagnostic-driven instantiations including a stabilized supervised optimizer, a diagnostic-regulated actor-critic scheme, and a diagnostic-conditioned learned optimizer. Under standard smoothness assumptions, we establish bounded effective updates and stability properties for all cases. Representative diagnostic illustrations in actor-critic learning highlight how the proposed signals modulate adaptation in response to temporal-difference error structure. Overall, this work elevates error evolution to a first-class object in adaptive learning and provides an interpretable, lightweight foundation for reliable learning in dynamic environments.

初筛：原文的实际新增是loss/TD increment的EMA与gradient-momentum alignment作为学习步调门控；可能改变“仅按瞬时gradient moments调参”的解释，但通用稳定性控制并不自动成为基础模型知识。定点看到§3 Eq1–6只给标量loss差、比例和cosine定义，不据名称当新统计识别；需要独立校准其具体新成立条件是否足以改变foundation训练选择。当前不评分、不采泛化可靠性。

### [Gradient Descent as Implicit EM in Distance-Based Neural Models](https://arxiv.org/abs/2512.24780v1)

API submitted：`2025-12-31T10:56:43Z`。

> Neural networks trained with standard objectives exhibit behaviors characteristic of probabilistic inference: soft clustering, prototype specialization, and Bayesian uncertainty tracking. These phenomena appear across architectures -- in attention mechanisms, classification heads, and energy-based models -- yet existing explanations rely on loose analogies to mixture models or post-hoc architectural interpretation. We provide a direct derivation. For any objective with log-sum-exp structure over distances or energies, the gradient with respect to each distance is exactly the negative posterior responsibility of the corresponding component: $\partial L / \partial d_j = -r_j$. This is an algebraic identity, not an approximation. The immediate consequence is that gradient descent on such objectives performs expectation-maximization implicitly -- responsibilities are not auxiliary variables to be computed but gradients to be applied. No explicit inference algorithm is required because inference is embedded in optimization. This result unifies three regimes of learning under a single mechanism: unsupervised mixture modeling, where responsibilities are fully latent; attention, where responsibilities are conditioned on queries; and cross-entropy classification, where supervision clamps responsibilities to targets. The Bayesian structure recently observed in trained transformers is not an emergent property but a necessary consequence of the objective geometry. Optimization and inference are the same process.

初筛：原文声称LSE梯度responsibility足以推出GD=EM及Transformer Bayesian结构必然性，若成立会改变attention/学习解释；不能用代数identity借成熟原则加分。已取得精确HTML，§3.2又明确“implicit EM”不指coordinate-ascent EM/收敛保证，与摘要无条件等价存在收窄；§4.3在`L=d_y+logsumexp(-d)`下给`r_j−1[j=y]`，实际求导是`1[j=y]−r_j`。这是需要独立校准的具体设计反证信号，暂不正面采用；必要日期未取得不自造Jan1归属。不据此否全部论文或所有Transformer Bayesian现象。

### [SliceLens: Fine-Grained and Grounded Error Slice Discovery for Multi-Instance Vision Tasks](https://arxiv.org/abs/2512.24592v1)

API submitted：`2025-12-31T03:28:41Z`。

> Systematic failures of computer vision models on subsets with coherent visual patterns, known as error slices, pose a critical challenge for robust model evaluation. Existing slice discovery methods are primarily developed for image classification, limiting their applicability to multi-instance tasks such as detection, segmentation, and pose estimation. In real-world scenarios, error slices often arise from corner cases involving complex visual relationships, where existing instance-level approaches lacking fine-grained reasoning struggle to yield meaningful insights. Moreover, current benchmarks are typically tailored to specific algorithms or biased toward image classification, with artificial ground truth that fails to reflect real model failures. To address these limitations, we propose SliceLens, a hypothesis-driven framework that leverages LLMs and VLMs to generate and verify diverse failure hypotheses through grounded visual reasoning, enabling reliable identification of fine-grained and interpretable error slices. We further introduce FeSD (Fine-grained Slice Discovery), the first benchmark specifically designed for evaluating fine-grained error slice discovery across instance-level vision tasks, featuring expert-annotated and carefully refined ground-truth slices with precise grounding to local error regions. Extensive experiments on both existing benchmarks and FeSD demonstrate that SliceLens achieves state-of-the-art performance, improving Precision@10 by 0.42 (0.73 vs. 0.31) on FeSD, and identifies interpretable slices that facilitate actionable model improvements, as validated through model repair experiments.

初筛：不是“用了VLM发现错误”本身，而是image-level聚合会把同图正确对象与错误对象混合，instance-grounded slice将评价unit切换；可能改变slice发现的分母及annotation合同。§3.2/§5.3.2可读，VLM yes置信排序与线性斜率仍是proxy，不证明成因；尚未判断是否有超过既有评价粒度分责的新贡献。待root题摘校准，不采用0.73/0.31宣传为普遍效果。

### [HOLOGRAPH: Active Causal Discovery via Sheaf-Theoretic Alignment of Large Language Model Priors](https://arxiv.org/abs/2512.24478v1)

API submitted：`2025-12-30T21:47:05Z`。

> Causal discovery from observational data remains fundamentally limited by identifiability constraints. Recent work has explored leveraging Large Language Models (LLMs) as sources of prior causal knowledge, but existing approaches rely on heuristic integration that lacks theoretical grounding. We introduce HOLOGRAPH, a framework that formalizes LLM-guided causal discovery through sheaf theory--representing local causal beliefs as sections of a presheaf over variable subsets. Our key insight is that coherent global causal structure corresponds to the existence of a global section, while topological obstructions manifest as non-vanishing sheaf cohomology. We propose the Algebraic Latent Projection to handle hidden confounders and Natural Gradient Descent on the belief manifold for principled optimization. Experiments on synthetic and real-world benchmarks demonstrate that HOLOGRAPH provides rigorous mathematical foundations while achieving competitive performance on causal discovery tasks with 50-100 variables. Our sheaf-theoretic analysis reveals that while Identity, Transitivity, and Gluing axioms are satisfied to numerical precision (<10^{-6}), the Locality axiom fails for larger graphs, suggesting fundamental non-local coupling in latent variable projections. Code is available at [https://github.com/hyunjun1121/holograph](https://github.com/hyunjun1121/holograph).

拟排除：原增量在用LLM先验支持tabular causal discovery的sheaf/gluing/latent投影，并未建立foundation能力形成、attention或系统执行的新解释；“局部belief合并”和自然梯度术语不是Agent state正确性机制。范围排除不是由数学/小模型标签拒绝；此论文识别性问题的应用接口没有改变项目主线设计。无评分，不为无关日期另追材料。

### [DarkEQA: Benchmarking Vision-Language Models for Embodied Question Answering in Low-Light Indoor Environments](https://arxiv.org/abs/2512.24985v1)

API submitted：`2025-12-31T17:31:29Z`。

> Vision Language Models (VLMs) are increasingly adopted as central reasoning modules for embodied agents. Existing benchmarks evaluate their capabilities under ideal, well-lit conditions, yet robust 24/7 operation demands performance under a wide range of visual degradations, including low-light conditions at night or in dark environments--a core necessity that has been largely overlooked. To address this underexplored challenge, we present DarkEQA, an open-source benchmark for evaluating EQA-relevant perceptual primitives under multi-level low-light conditions. DarkEQA isolates the perception bottleneck by evaluating question answering from egocentric observations under controlled degradations, enabling attributable robustness analysis. A key design feature of DarkEQA is its physical fidelity: visual degradations are modeled in linear RAW space, simulating physics-based illumination drop and sensor noise followed by an ISP-inspired rendering pipeline. We demonstrate the utility of DarkEQA by evaluating a wide range of state-of-the-art VLMs and Low-Light Image Enhancement (LLIE) models. Our analysis systematically reveals VLMs' limitations when operating under these challenging visual conditions. Our code and benchmark dataset will be released upon acceptance.

初筛：候选理由不能只是新增夜间场景或性能下降；更具体可能是RAW-linear曝光×noise×ISP与LLIE条件的分离，改变评价stimulus身份和前处理选择。§III/TableI可读，配对EV-only/noise/LLIE切片不等真实全天候robot任务或物理sensor普遍分布；需校准这是具体评价盲区还是已有原则的场景实例，不因embodied或VLM词汇准入。不采用“将release”作开源已验证。

### [GaMO: Geometry-aware Multi-view Diffusion Outpainting for Sparse-View 3D Reconstruction](https://arxiv.org/abs/2512.25073v1)

API submitted：`2025-12-31T18:59:55Z`。

> Recent advances in 3D reconstruction have achieved remarkable progress in high-quality scene capture from dense multi-view imagery, yet struggle when input views are limited. Various approaches, including regularization techniques, semantic priors, and geometric constraints, have been implemented to address this challenge. Latest diffusion-based methods have demonstrated substantial improvements by generating novel views from new camera poses to augment training data, surpassing earlier regularization and prior-based techniques. Despite this progress, we identify three critical limitations in these state-of-the-art approaches: inadequate coverage beyond known view peripheries, geometric inconsistencies across generated views, and computationally expensive pipelines. We introduce GaMO (Geometry-aware Multi-view Outpainter), a framework that reformulates sparse-view reconstruction through multi-view outpainting. Instead of generating new viewpoints, GaMO expands the field of view from existing camera poses, which inherently preserves geometric consistency while providing broader scene coverage. Our approach employs multi-view conditioning and geometry-aware denoising strategies in a zero-shot manner without training. Extensive experiments on Replica and ScanNet++ demonstrate state-of-the-art reconstruction quality across 3, 6, and 9 input views, outperforming prior methods in PSNR and LPIPS, while achieving a $25\times$ speedup over SOTA diffusion-based methods with processing time under 10 minutes. Project page: https://yichuanh.github.io/GaMO/

初筛：潜在具体增量是固定existing-pose扩FOV而非另造novel camera，结合multi-view denoising的支持接口；但同pose并不自动证明未知区域几何一致。需决定性方法说明是否新增了生成约束/可验边界，不能由“geometry-aware”或25×准入。本轮只取得HTML，未授标准/深入完成、硬件速度或Books采纳。日期仍未确认。

### [Guided Diffusion-based Generation of Adversarial Objects for Real-World Monocular Depth Estimation Attacks](https://arxiv.org/abs/2512.24111v1)

API submitted：`2025-12-30T09:41:41Z`。

> Monocular Depth Estimation (MDE) serves as a core perception module in autonomous driving systems, but it remains highly susceptible to adversarial attacks. Errors in depth estimation may propagate through downstream decision making and influence overall traffic safety. Existing physical attacks primarily rely on texture-based patches, which impose strict placement constraints and exhibit limited realism, thereby reducing their effectiveness in complex driving environments. To overcome these limitations, this work introduces a training-free generative adversarial attack framework that generates naturalistic, scene-consistent adversarial objects via a diffusion-based conditional generation process. The framework incorporates a Salient Region Selection module that identifies regions most influential to MDE and a Jacobian Vector Product Guidance mechanism that steers adversarial gradients toward update directions supported by the pre-trained diffusion model. This formulation enables the generation of physically plausible adversarial objects capable of inducing substantial adversarial depth shifts. Extensive digital and physical experiments demonstrate that our method significantly outperforms existing attacks in effectiveness, stealthiness, and physical deployability, underscoring its strong practical implications for autonomous driving safety assessment.

初筛：具体可能是JVP将下游梯度送回pretrained diffusion的denoised样本路径，改变guidance对象，而不是汽车攻击效果；若只是成熟classifier/denoiser guidance在MDE换任务，不足准入。需独立校准，不能把模拟物体自然性、MDE偏移当VLA闭环风险实证。未给评分/安全采用。

### [OpenOneRec Technical Report](https://arxiv.org/abs/2512.24762v1)

API submitted：`2025-12-31T10:15:53Z`。

> While the OneRec series has successfully unified the fragmented recommendation pipeline into an end-to-end generative framework, a significant gap remains between recommendation systems and general intelligence. Constrained by isolated data, they operate as domain specialists-proficient in pattern matching but lacking world knowledge, reasoning capabilities, and instruction following. This limitation is further compounded by the lack of a holistic benchmark to evaluate such integrated capabilities. To address this, our contributions are: 1) RecIF Bench & Open Data: We propose RecIF-Bench, a holistic benchmark covering 8 diverse tasks that thoroughly evaluate capabilities from fundamental prediction to complex reasoning. Concurrently, we release a massive training dataset comprising 96 million interactions from 160,000 users to facilitate reproducible research. 2) Framework & Scaling: To ensure full reproducibility, we open-source our comprehensive training pipeline, encompassing data processing, co-pretraining, and post-training. Leveraging this framework, we demonstrate that recommendation capabilities can scale predictably while mitigating catastrophic forgetting of general knowledge. 3) OneRec-Foundation: We release OneRec Foundation (1.7B and 8B), a family of models establishing new state-of-the-art (SOTA) results across all tasks in RecIF-Bench. Furthermore, when transferred to the Amazon benchmark, our models surpass the strongest baselines with an average 26.8% improvement in Recall@10 across 10 diverse datasets (Figure 1). This work marks a step towards building truly intelligent recommender systems. Nonetheless, realizing this vision presents significant technical and theoretical challenges, highlighting the need for broader research engagement in this promising direction.

初筛：数据/八任务榜单/推荐分数本身不准入。唯一可能直连foundation主线的是co-pretraining的通用能力保持与scaling成立条件，摘要未说明改变遗忘取舍的新机制；必须用最小决定性core判断，不把推荐标签自动拒绝或从“fully reproducible”声称已复现。HTML已取得但未进行Evidence审阅；不冻结候选。

### [DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information](https://arxiv.org/abs/2512.24635v1)

API submitted：`2025-12-31T05:13:34Z`。

> Automated Program Repair (APR) aims to automatically generate correct patches for buggy programs. Recent approaches leveraging large language models (LLMs) have shown promise but face limitations. Most rely solely on static analysis, ignoring runtime behaviors. Some attempt to incorporate dynamic signals, but these are often restricted to training or fine-tuning, or injected only once into the repair prompt, without iterative use. This fails to fully capture program execution. Current iterative repair frameworks typically rely on coarse-grained feedback, such as pass/fail results or exception types, and do not leverage fine-grained execution-level information effectively. As a result, models struggle to simulate human stepwise debugging, limiting their effectiveness in multi-step reasoning and complex bug repair.
> To address these challenges, we propose DynaFix, an execution-level dynamic information-driven APR method that iteratively leverages runtime information to refine the repair process. In each repair round, DynaFix captures execution-level dynamic information such as variable states, control-flow paths, and call stacks, transforming them into structured prompts to guide LLMs in generating candidate patches. If a patch fails validation, DynaFix re-executes the modified program to collect new execution information for the next attempt. This iterative loop incrementally improves patches based on updated feedback, similar to the stepwise debugging practices of human developers. We evaluate DynaFix on the Defects4J v1.2 and v2.0 benchmarks. DynaFix repairs 186 single-function bugs, a 10% improvement over state-of-the-art baselines, including 38 bugs previously unrepaired. It achieves correct patches within at most 35 attempts, reducing the patch search space by 70% compared with existing methods, thereby demonstrating both effectiveness and efficiency in repairing complex bugs.

拟排除：更新variable/control-flow/call-stack后再次prompt/validation，是已有执行观察—修复提案—验证循环的粒度实例；摘要没有新增trace真实性、状态归属、执行机制或可靠性成立条件。局部Defects4J提升/尝试次数不建立新的长效系统判断。无纠错/安全标记见摘要；不评分，不为此追日期。

### [Lifting Vision: Ground to Aerial Localization with Reasoning Guided Planning](https://arxiv.org/abs/2512.24404v1)

API submitted：`2025-12-30T18:36:39Z`。

> Multimodal intelligence development recently show strong progress in visual understanding and high level reasoning. Though, most reasoning system still reply on textual information as the main medium for inference. This limit their effectiveness in spatial tasks such as visual navigation and geo-localization. This work discuss about the potential scope of this field and eventually propose an idea visual reasoning paradigm Geo-Consistent Visual Planning, our introduced framework called Visual Reasoning for Localization, or ViReLoc, which performs planning and localization using only visual representations. The proposed framework learns spatial dependencies and geometric relations that text based reasoning often suffer to understand. By encoding step by step inference in the visual domain and optimizing with reinforcement based objectives, ViReLoc plans routes between two given ground images. The system also integrates contrastive learning and adaptive feature interaction to align cross view perspectives and reduce viewpoint differences. Experiments across diverse navigation and localization scenarios show consistent improvements in spatial reasoning accuracy and cross view retrieval performance. These results establish visual reasoning as a strong complementary approach for navigation and localization, and show that such tasks can be performed without real time global positioning system data, leading to more secure navigation solutions.

拟排除：visual route/RL、contrastive对齐与feature交互组合未描述新的transition/观测可辨识性、reasoning因果机制或控制成立条件；提升geo-localization指标与无GPS表述不改变foundation表示或VLA闭环设计。不是因视觉/导航领域直接拒绝。无评分，不为不影响处置的日期追查。

## 4. fresh 有界查询与五项补检题摘

四查询共同原值：`(cat:cs.CL OR cat:cs.LG OR cat:cs.DC OR cat:cs.AI OR cat:cs.CV OR cat:cs.RO OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.IR OR cat:cs.MA) AND submittedDate:[202512291900 TO 202601010000] AND <主题表达式>`。API `/api/query`，`sortBy=submittedDate&sortOrder=descending&max_results=100`，按前表start0/100/200停止；没有从total反推本日候选数。仅从返回标题定点挑相关/含糊条目；已有相关104家族直接去重，后月ID作日期不明源线索，不逐项关全年身份。

- model：`(all:"language model" OR all:transformer OR all:"mixture of experts" OR all:pretraining OR all:"reinforcement learning")`。
- runtime：`(all:"GPU" OR all:"distributed training" OR all:"inference" OR all:"kernel" OR all:"compiler" OR all:"checkpoint")`。
- multimodal：`(all:"multimodal" OR all:"diffusion" OR all:"world model" OR all:"vision language action" OR all:"video generation")`。
- agent：`(all:"agent" OR all:"retrieval augmented" OR all:"memory" OR all:"tool use" OR all:"planning")`。

后五项精确v1 API实际5/5返回，题摘读完，原请求：<https://export.arxiv.org/api/query?id_list=2512.23824v1%2C2512.24103v1%2C2512.24965v1%2C2512.24547v1%2C2512.25052v1&max_results=5>。这也是本轮原始查漏停止点；不继续扩充Submitted池。

### [MS-SSM: A Multi-Scale State Space Model for Efficient Sequence Modeling](https://arxiv.org/abs/2512.23824v1)

API submitted：`2025-12-29T19:36:28Z`。

> State-space models (SSMs) have recently attention as an efficient alternative to computationally expensive attention-based models for sequence modeling. They rely on linear recurrences to integrate information over time, enabling fast inference, parallelizable training, and control over recurrence stability. However, traditional SSMs often suffer from limited effective memory, requiring larger state sizes for improved recall. Moreover, existing SSMs struggle to capture multi-scale dependencies, which are essential for modeling complex structures in time series, images, and natural language. This paper introduces a multi-scale SSM framework that addresses these limitations by representing sequence dynamics across multiple resolution and processing each resolution with specialized state-space dynamics. By capturing both fine-grained, high-frequency patterns and coarse, global trends, MS-SSM enhances memory efficiency and long-range modeling. We further introduce an input-dependent scale-mixer, enabling dynamic information fusion across resolutions. The proposed approach significantly improves sequence modeling, particularly in long-range and hierarchical tasks, while maintaining computational efficiency. Extensive experiments on benchmarks, including Long Range Arena, hierarchical reasoning, time series classification, and image recognition, demonstrate that MS-SSM consistently outperforms prior SSM-based models, highlighting the benefits of multi-resolution processing in state-space architectures.

初筛：有限state难兼顾多时间尺度→不同resolution的SSM dynamics与input-dependent mixer→可能改变固定状态内存/时间粒度取舍；不是因LRA/小模型排除，也不由“SSM替attention”自动准入。摘要没有具体新resolution因果/合并机制或适用条件，需决定性core与独立准入校准；尚未确认Jan1公开，不评分不深审。

### [Enhancing LLM Planning Capabilities through Intrinsic Self-Critique](https://arxiv.org/abs/2512.24103v1)

API submitted：`2025-12-30T09:23:25Z`。

> We demonstrate an approach for LLMs to critique their \emph{own} answers with the goal of enhancing their performance that leads to significant improvements over established planning benchmarks. Despite the findings of earlier research that has cast doubt on the effectiveness of LLMs leveraging self critique methods, we show significant performance gains on planning datasets in the Blocksworld domain through intrinsic self-critique, without external source such as a verifier. We also demonstrate similar improvements on Logistics and Mini-grid datasets, exceeding strong baseline accuracies. We employ a few-shot learning technique and progressively extend it to a many-shot approach as our base method and demonstrate that it is possible to gain substantial improvement on top of this already competitive approach by employing an iterative process for correction and refinement. We illustrate how self-critique can significantly boost planning performance. Our empirical results present new state-of-the-art on the class of models considered, namely LLM model checkpoints from October 2024. Our primary focus lies on the method itself, demonstrating intrinsic self-improvement capabilities that are applicable regardless of the specific model version, and we believe that applying our method to more complex search techniques and more capable models will lead to even better performance.

初筛：作者主张没有外部verifier的局部self-critique收益，可能是对“intrinsic correction必然无益”的受限反证；不能因只是旧prompt迭代自动排除负面/反证价值，但也不能用局部榜单推翻可靠性边界。摘要未明确matched采样/示例/token预算、真实judge及失败人口；只记录待校准线索，不授self-verification成立或所有版本泛化；没有已确认Jan1公开日。

### [ShowUI-$π$: Flow-based Generative Models as GUI Dexterous Hands](https://arxiv.org/abs/2512.24965v1)

API submitted：`2025-12-31T16:51:14Z`。

> Building intelligent agents capable of dexterous manipulation is essential for achieving human-like automation in both robotics and digital environments. However, existing GUI agents rely on discrete click predictions (x,y), which prohibits free-form, closed-loop trajectories (e.g. dragging a progress bar) that require continuous, on-the-fly perception and adjustment. In this work, we develop ShowUI-$π$, the first flow-based generative model as GUI dexterous hand, featuring the following designs: (i) Unified Discrete-Continuous Actions, integrating discrete clicks and continuous drags within a shared model, enabling flexible adaptation across diverse interaction modes; (ii) Flow-based Action Generation for drag modeling, which predicts incremental cursor adjustments from continuous visual observations via a lightweight action expert, ensuring smooth and stable trajectories; (iii) Drag Training data and Benchmark, where we manually collect and synthesize 20K drag trajectories across five domains (e.g. PowerPoint, Adobe Premiere Pro), and introduce ScreenDrag, a benchmark with comprehensive online and offline evaluation protocols for assessing GUI agents' drag capabilities. Our experiments show that proprietary GUI agents still struggle on ScreenDrag (e.g. Operator scores 13.27, and the best Gemini-2.5-CUA reaches 22.18). In contrast, ShowUI-$π$ achieves 26.98 with only 450M parameters, underscoring both the difficulty of the task and the effectiveness of our approach. We hope this work advances GUI agents toward human-like dexterous control in digital world. The code is available at https://github.com/showlab/showui-pi.

初筛：one-shot离散点击不能表达有视觉反馈的连续拖曳→discrete/continuous联合动作与flow action expert→可能改变GUI tool动作合同与闭环消费接口。不能借机器人“dexterous”外推物理控制，也不由450M/榜单准入；具体反馈频率、状态同步及增量动作语义需独立校准。没有确认Jan1公开、不评分。

### [Hierarchical Vector-Quantized Latents for Perceptual Low-Resolution Video Compression](https://arxiv.org/abs/2512.24547v1)

API submitted：`2025-12-31T01:07:17Z`。

> The exponential growth of video traffic has placed increasing demands on bandwidth and storage infrastructure, particularly for content delivery networks (CDNs) and edge devices. While traditional video codecs like H.264 and HEVC achieve high compression ratios, they are designed primarily for pixel-domain reconstruction and lack native support for machine learning-centric latent representations, limiting their integration into deep learning pipelines. In this work, we present a Multi-Scale Vector Quantized Variational Autoencoder (MS-VQ-VAE) designed to generate compact, high-fidelity latent representations of low-resolution video, suitable for efficient storage, transmission, and client-side decoding. Our architecture extends the VQ-VAE-2 framework to a spatiotemporal setting, introducing a two-level hierarchical latent structure built with 3D residual convolutions. The model is lightweight (approximately 18.5M parameters) and optimized for 64x64 resolution video clips, making it appropriate for deployment on edge devices with constrained compute and memory resources. To improve perceptual reconstruction quality, we incorporate a perceptual loss derived from a pre-trained VGG16 network. Trained on the UCF101 dataset using 2-second video clips (32 frames at 16 FPS), on the test set we achieve 25.96 dB PSNR and 0.8375 SSIM. On validation, our model improves over the single-scale baseline by 1.41 dB PSNR and 0.0248 SSIM. The proposed framework is well-suited for scalable video compression in bandwidth-sensitive scenarios, including real-time streaming, mobile video analytics, and CDN-level storage optimization.

拟排除：VQ-VAE-2的两级结构扩到3D residual conv再加VGG感知loss，只给64²重建指标；未新增可学习video codec的表示/时间commit语义、foundation训练收益条件或压缩预算反证。CDN/edge/real-time仅潜在应用，不授rate/latency/decoder实测。非因小模型/低分辨率自动拒绝；无新主线机制依据，不评分，不为无关日期追加请求。

### [AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG](https://arxiv.org/abs/2512.25052v1)

API submitted：`2025-12-31T18:48:07Z`。

> Retrieval-augmented generation (RAG) is highly sensitive to the quality of selected context, yet standard top-k retrieval often returns redundant or near-duplicate chunks that waste token budget and degrade downstream generation. We present AdaGReS, a redundancy-aware context selection framework for token-budgeted RAG that optimizes a set-level objective combining query-chunk relevance and intra-set redundancy penalties. AdaGReS performs greedy selection under a token-budget constraint using marginal gains derived from the objective, and introduces a closed-form, instance-adaptive calibration of the relevance-redundancy trade-off parameter to eliminate manual tuning and adapt to candidate-pool statistics and budget limits. We further provide a theoretical analysis showing that the proposed objective exhibits epsilon-approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection. Experiments on open-domain question answering (Natural Questions) and a high-redundancy biomedical (drug) corpus demonstrate consistent improvements in redundancy control and context quality, translating to better end-to-end answer quality and robustness across settings.

初筛：token约束下context集合相关性/冗余与pool-statistics闭式校准、近似submodularity条件，可能新增greedy上下文选择的成立边界。不是因为RAG术语或biomedical场景准入；Natural Questions也不自动给贡献。需确认与成熟MMR/集合选择相比实际新条件，而非只新tradeoff配方。当前日期不明，保留线索，不评分、不把embedding冗余当真实答案support。

## 5. 精确恢复点与独立复核

15个新题摘不继承旧104的日期权限。潜在线索身份为24445/24780/24592/24985/25073/24111/24762/23824/24103/24965/25052；只有经root贡献校准仍需要本次处理的条目，才请求其官方dated announcement/list含论文ID或作者具名dated原始正文，确认首次公开/实质revision确在Jan1。具体重开点就是对应上节题摘及其原链接，不索秒级证明、不把submitted/API published作公开。若贡献校准关闭，不再为其追日期。拟明确排除24478/24635/24404/24547的具体理由已逐项保留，无日期考古请求。

作者可执行来源和题摘收尾已完成，不再扩Submitted缓冲池。普通待办仅root独立准入/覆盖校准：可复用现有完整AB和实际目录字段，不重审旧104。若拟排除获校准且其余潜在线索日期不能确认，则作为不支持Jan1候选/Books/无遗漏的外部保留项隔离；不是新候选审阅完成。当前无Books提案/写入。

本次具体来源缺口：Google pubs日级公开字段/DeepMind目标历史分页、Meta Jan1研究目录、MiMo具名Blog日期/分页、MiniMax Agent Tech Jan1目录；当前可用首页/月档/原Markdown有限入口已执行，不能因这些具体入口受限而请求所有机构全部历史快照。Qwen/Hunyuan/ZAI已取得的有限完整当前目录不再额外背负“证明无删除”任务。arXiv新增潜在线索只缺上述具名ID公开日期依据，不索旧104日期。

复核者：待root（非作者）。结论：未授通过。仅新增本文件；不stage、commit、push。最终对新增内容执行 `git diff --no-index --check /dev/null papers/2026/01/_sources/daily-20260102/supplement-20261007.md`；本地六个证据链接已逐个核存在，标题、引用块与表格结构检查通过。这只确认增量格式与本地链接，不冒充报告validator或语义Gate。

## root后续校准与必要审阅（2026-10-07）

上面的日期/准入待办是作者原停点，不是当前最终处置。root实际完整读15个具名题摘并定点读决定性core；最终5项贡献前关闭为24478、24635、24404、24547、24592。前四项理由成立；SliceLens24592在检测/分割/姿态错误切片中组合VLM假设与验证，没有建立改变foundation评价判断的具体增量；不是按领域或小模型标签拒绝。MDE24111最初被root按“下游深度攻击复用diffusion/JVP”关闭，但独立负侧复核发现其IV-C确实将外部方向再经score Jacobian调制，原关闭理由遗漏设计差额，现明确撤销。仅重开此项，按Jan01补充候选2+1+2=5必要审阅；符号/JVP接口与语义保证争议隔离，不入Books，实际证据见[new-evidence末节](new-evidence-20261007.md)。未删除原题摘、反证或改判原因，其余有效证据不推倒。

### 独立日级日期校准

audit_jan02_dates实际逐项重开24445/24780/24592/24985/25073/24762/24965/25052的abs v1、[官方ID规则](https://info.arxiv.org/help/availability.html)及[官方假期公告](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/)。8项v1提交均晚于Dec30 ET14、早于Dec31 ET14；Dec30没有公告，2512身份是在首次公告分配且不可回溯月份，排除延迟到Jan才首次公告。因此官方规则联合限定为Dec31 ET公告日，即BJT Jan01。不是Submitted等于公开，也不授逐篇精确时刻或全网家族最早正文证明。原8项不再请求“具名公告缺身份”；其中24592已贡献前关闭，其余7项新增准入。23824/MS-SSM与24103/Intrinsic Self-Critique的提交下界及月份仍不能唯一决定Jan01日级公开，保留这两个具名日期请求，不因可读摘要/全文先评分采用。

### 24445v1：诊断门控优化器

准入与评分：梯度统计不足以描述误差时间结构→loss/TD增量EMA及alignment门控→可核步幅调节的替代分支；2+2+2=6。root读[exact-v1](https://arxiv.org/html/2512.24445v1) §3 Eq1–7、§4 Eq10–19/Algorithm1、§5–7及AppendixA/B的直接相关假设。

采用边界：bias/noise门控有界，加到Adam式归一方向上；alignment修正与步幅门控是不同对象。Appendix只给有界更新草图，Eq19下降式需要额外方向/预条件条件，不能从门控小于一得出必然下降；负alignment也使“投影从不放大范数”的无条件解释不成立。§7明示仅代表性诊断曲线，未给模型/数据/硬件/精度/预算/seed完整评价，相关字段Not Disclosed，SLO非此训练目标。可检查机制不等于大模型预训练效果证实。拟标准审阅完成、仅报告；不授通用稳定/收敛或改写TRAIN-PRETRAINING已有梯度诊断与optimizer边界。共享Books不写。

### 24780v1：GD与EM解释的中心争议

准入与评分：作者把soft assignment解释推广为训练机制等价→可能改变学习解释；2+1+3=6，因中心理论关系须深入核直接推导。root读[exact-v1](https://arxiv.org/html/2512.24780v1) §2–4，核Eq4–6、§3.2及§4.3。

Eq4的LSE导数为负responsibility正确，但Eq6负LSE的导数应为正responsibility，正文却继续写负；§4.3给L=d_y+LSE(-d)，其导数应为1[j=y]−r_j，打印成相反符号。§3.2末段主动把“implicit EM”限为responsibility-weighted更新，不保证coordinate-ascent EM或其收敛，必须保留该自限；争议在于§4.1仍进一步主张相同fixed points/path及上述导数符号。责任权重恒等式本身不证明GD一步最大化Q或一般Transformer训练等价EM。此为可定位理论争议，不否正确恒等式和作者已有自限；无实验配置可以修复该推论。争议/暂缓，不进入WORLDVIEW-WHY-MODELS-LEARN或MODEL-SELF-ATTENTION。恢复需精确版本勘误或含目标、梯度与M-step条件的有效推导，不索无关附件。

### 25052v1：预算RAG选择与保证的边界

准入与评分：固定MMR权重→按候选相关/冗余及预期容纳量调beta→预算条件下选择分支；2+1+2=5，拟理论保证触发深入核相关部分。root读[exact-v1](https://arxiv.org/html/2512.25052v1) §3 Eq1–7/Algorithm1、§4.1–4.3、§5–6。

F为相关性之和减成对非负相似惩罚，该假设下边际差本身非负，已是次模；不意味着单调。§4.2.4明确承认cardinality的1−1/e不直接移植到token knapsack，须保留作者自限；争议在§4.3.4后续仍给标准greedy保证而未满足相应条件。Eq23～24给边际差的上界，并不能证明Eq21所需下界；允许负cosine时该推导不足，若坚持非负假设则已经精确次模。Eq7的分母较Eq5–6多一半因子，且epsilon说明未进入式；Algorithm1不放入过长最高分项后若不移出/重选，literal continue可能重复。实验只匹配所选chunk数，NQ/私有drug、Conan embedding、GLM-4.5-air与IOU/定性回答不等完整token或成本/SLO匹配；hardware/precision/batch/concurrency/SLO Not Disclosed。启发式可能有用，但“近最优保证”尚不可采用。争议/暂缓，保持AGENT-RAG既有重排/去重/packing，不改Books；恢复需明确成本约束、可终止算法及适用保证/校准式的精确修订或一致实现。

其余24985/25073/24762/24965由jan02_new_evidence读取对应必要机制/eval/限制并提出具体owner处置；root只写共享Books。以上3项由root审阅，其结论须非作者复核，不能用本段自授日级通过。当前7新增家族的证据与Books全部收尾前本日保持进行中；旧104家族及原证明仍有效，不因补查重写。

## 本轮最终分区补正

15个具名完整题摘的最终分区为8个新增确定家族、5个贡献前关闭、2个日级公开日期保留。新增MDE24111的具体准入改判、Jan01日级联合证明和必要原源争议见[new-evidence末节](new-evidence-20261007.md)与[root独立审计](root-evidence-audit-20261007.md)；原“7新增/6关闭”的中间停点被此处覆盖，但证据保留。8项已审为4实际Books整合/1仅报告/3争议暂缓；112总行中原104字节、顺序、日期、评分及有效证据均保留，仅移除旧表内截断GFM的空白行，并连续附8新行，不冒称原排版从未动。普通剩余仅最后日级非作者结论写回，外部保留不授正面证据。
