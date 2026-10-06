# 12/31 贡献先行的精确题摘判断

检查2026-10-02T19:18:23+08:00。86项新增相关身份的官方`https://arxiv.org/abs/2512.<ID>v1`完整题摘实际读取；官方v1页标题有时与检索当前标题不同，以下以实际v1为准。不是精确正文/受控评价审阅完成，不把摘要中的收益、理论、安全保证直接采用。重复命中先归同身份，已在26–30实际处理的同ID只定点复用题摘/必要日期请求，不新增计数或继承日报结论。现70 potential、16关闭；root指出共同摘要关闭错误后，9项含糊准入已读必要差额重开，旧61/25撤销。另HY-MT与Qwen具体判断见[机构原文](OFFICIAL_CORE.md)。

## 语言、训练与系统

| v1身份 | 具体贡献判断 |
| --- | --- |
| [24618 Youtu-LLM](https://arxiv.org/abs/2512.24618v1) | potential：从零小模型的Commonsense→STEM→Agent curriculum与轨迹mid-training，而非蒸馏；需分开词表/MLA和数据课程归因 |
| [24609 collaborative RL](https://arxiv.org/abs/2512.24609v1) | 重开potential：[v1 PDF §II-C/D](https://arxiv.org/pdf/2512.24609v1)（HTML404后有限替代）读leave-one-out team credit而非固定平均，coordination penalty与batch normalization消融主张；需要核反事实实现/归因，不把CTDE或GRPO名称本身准入 |
| [24603 CLoRA](https://arxiv.org/abs/2512.24603v1) | potential：跨LRM共享投影空间并以SADE约束冗余，改变参数预算下低秩模块协作；非只替换ViT任务 |
| [24572 KCL](https://arxiv.org/abs/2512.24572v1) | potential：逐题提供precedent以分离参数知识与推理能力，rubric生成问题；需核知识隔离而非只新增法律榜单 |
| [24571 SynRAG](https://arxiv.org/abs/2512.24571v1) | 重开potential：[v1 Methodology/Results](https://arxiv.org/html/2512.24571v1)普通文档分块检索与独立组件化syntax service共同条件化生成，另核执行查询；BLEU/ROUGE、可执行性和意图正确不等价。非token级grammar enforcement，不采用其“语法保证”或通用安全结论；非作者定点原文核见INDEPENDENT_LOCAL_REVIEW |
| [24570 data optimization](https://arxiv.org/abs/2512.24570v1) | potential反证：五类数据处理及两两组合对功能正确、code smell、maintainability目标不同，组合并不总加功能收益 |
| [24565 MCPAgentBench](https://arxiv.org/abs/2512.24565v1) | potential：真实tool definitions+模拟sandbox/干扰工具减少外部服务混杂，难度与效率联合评价，需核模拟有效性 |
| [24562 HaluNet](https://arxiv.org/abs/2512.24562v1) | potential：语义内部表示与token分布不确定性多分支互补、一pass探测；不是只声明幻觉评分更高 |
| [24556 temporal safety](https://arxiv.org/abs/2512.24556v1) | potential安全反证：language×temporal framing因子实验，低资源语言不必更不安全，过去/未来语境改变拒绝；不采用泛化“语义不理解”结论 |
| [24532 spatial RL](https://arxiv.org/abs/2512.24532v1) | potential：固定原子空间变换模型再LoRA/GRPO组合规划，静态内部state与动态环境分别验证，区别端到端RL |
| [24511 checkpoint I/O](https://arxiv.org/abs/2512.24511v1) | potential：buffered/direct、alignment/coalescing与file-system aware聚合影响checkpoint吞吐；需核端到端与synthetic差别 |
| [24505 math competition](https://arxiv.org/abs/2512.24505v1) | 关闭：新增地区题集与三个模型错误分类，未给出可纠正具体评估混杂或改变机制的验证；不是因数学题材一律AI for Science |
| [24478 HOLOGRAPH](https://arxiv.org/abs/2512.24478v1) | potential：以sheaf局部belief/gluing建LLM causal prior，Locality在大图失败的反证比概念比喻重要，需核假设 |
| [24438 ViT compositionality](https://arxiv.org/abs/2512.24438v1) | potential：DWT输入primitive的组成与原图latent近似关系，具体表示组合验证而非旧术语归纳 |
| [24314 QianfanHuijin](https://arxiv.org/abs/2512.24314v1) | potential：分阶段reasoning/agentic/general RL与对应消融可能限定能力归属，需辨别是否仅成熟CPT/SFT/RL堆叠 |
| [24195 CorGi](https://arxiv.org/abs/2512.24195v1) | potential：block贡献分配cache间隔、cross-attention salient token局部更新保护对象细节，cache不是无差别复用 |
| [24176 Internal Guidance](https://arxiv.org/abs/2512.24176v1) | potential：中间层辅助训练与中/深输出外推，避免bad-model guidance额外训练/步；需核训练预算和CFG共存 |
| [24157 TeleChat3-MoE](https://arxiv.org/abs/2512.24157v1) | potential：Ascend训练数值一致性、attention-aware调度、分层expert通信、ILP并行组合；须逐拟采用增量核而非硬件品牌清单 |
| [24120 architecture generation](https://arxiv.org/abs/2512.24120v1) | 重开potential：[v1 Context Overflow/Dataset Balanced Evaluation/Limitations](https://arxiv.org/html/2512.24120v1)多example造成生成失败与按dataset平衡避免aggregate样本分布混杂；hash漏semantic equivalence。具体设计/评价反证，不采用n=3普遍最优或100x |
| [24113 CogRec](https://arxiv.org/abs/2512.24113v1) | 重开potential：[v1 Ablation Study](https://arxiv.org/html/2512.24113v1)分开bootstrapping、chunking和symbolic engine，禁chunking时transient LLM答复无法转长期rule的局部验证；需核rule质量/错误持久化，Soar成熟机制本身不算新 |
| [24103 intrinsic critique](https://arxiv.org/abs/2512.24103v1) | potential反证：无外部verifier的self-critique在特定planning/many-shot有效，不能用既有失败认识整体否定；模型限October2024 |
| [24063 SFT/RL generalization](https://arxiv.org/abs/2512.24063v1) | potential：atomic skill与低层统计联合跟踪，RL稳定与SFT表面过拟合的局部反证，非所有SFT必退化 |
| [24058 CRS](https://arxiv.org/abs/2512.24058v1) | potential：calibration/perturbation/uncertainty联合可能揭示单指标漏掉的failure，需区分加权合成与真盲区验证 |
| [24052 audio AHA](https://arxiv.org/abs/2512.24052v1) | potential：counterfactual hard negatives区分音频证据和语言 plausible内容，时间关系/数量错误诊断；需核污染与外集收益 |
| [24044 jailbreak filters](https://arxiv.org/abs/2512.24044v1) | potential安全反证：完整input/output filter改变仅model ASR解释，检测至少一filter不等同实际pipeline必拦截或安全保证 |
| [24014 iCLP](https://arxiv.org/abs/2512.24014v1) | potential：显式轨迹计划蒸馏为VQ离散latent code再语言推理；需核latent学习代价与计划错误 |
| [23995 RepetitionCurse](https://arxiv.org/abs/2512.23995v1) | potential安全：重复token触发推理MoE router集中、EP设备闲忙不均与TTFT DoS；训练balance不自动保障推理SLA |

## 多模态、生成与行动

| v1身份 | 具体贡献判断 |
| --- | --- |
| [24499 ADS](https://arxiv.org/abs/2512.24499v1) | potential安全：以pretrained denoiser代理decoder、color-aware quaternion扰动主动破坏扩散隐写payload，区分检测与净化；仅Pulsar威胁模型 |
| [24497 JEPA-WM planning](https://arxiv.org/abs/2512.24497v1) | potential：系统拆architecture/objective/planner对表示空间规划的贡献，模拟与真实数据，需核组合最优对比归因 |
| [24473 F2IDiff](https://arxiv.org/abs/2512.24473v1) | potential：高保真12MP patch超分下文本条件不足、DINO低层条件约束hallucination，改变低退化输入的生成边界 |
| [24470 Semantic Lookout](https://arxiv.org/abs/2512.24470v1) | potential行动安全：handover间隙world-anchored有限轨迹候选、人工持续override，不把语义建议升格主航线authority；40场景/实船局部结果非法规合规保证 |
| [24426 CF-VLA](https://arxiv.org/abs/2512.24426v1) | potential安全：meta-action counterfactual改正后再轨迹，rollout-filter-label挖难场景与自适应思考；需核执行前安全边界 |
| [24331 LVLDrive](https://arxiv.org/abs/2512.24331v1) | potential：Gradual Fusion Q-Former渐注LiDAR，保留已有VLM能力并补metric空间，需核灾难扰动对照 |
| [24330 SenseNova-MARS](https://arxiv.org/abs/2512.24330v1) | potential：BN-GSPO稳定interleaved visual/search/crop训练，HR-MMSearch高分辨率知识检索评价；不只三工具编排 |
| [24329 WM-SAR](https://arxiv.org/abs/2512.24329v1) | 关闭：literal/norm/intention角色+deterministic score+LogisticRegression用于sarcasm，非action-conditioned world dynamics，已有组合任务收益无新增通用边界 |
| [24227 Mirage](https://arxiv.org/abs/2512.24227v1) | potential：2D temporally-agnostic latent注入3D decoder避causality破坏，3D/2D分阶段alignment，区别只做driving数据增强 |
| [24165 DiffThinker](https://arxiv.org/abs/2512.24165v1) | potential：image-to-image生成表达长程视觉推理，和text CoT不同factorization/并行控制；比较预算与成功判定未审 |
| [24149 LEWM](https://arxiv.org/abs/2512.24149v1) | potential：visual/action状态显式加入emotion并预测transition、删除emotion反证，非仅拟人化名称；需核状态与标签泄漏 |
| [24146 D2-Align](https://arxiv.org/abs/2512.24146v1) | potential反证：preference mode collapse与reward embedding方向校正，frozen reward模型避免style偏置，需核hold-out diversity |
| [24143 activation steering](https://arxiv.org/abs/2512.24143v1) | potential：单contrastive forward取得方向并每reverse-step应用，MDLM token/submodule scope与AR不同 |
| [24138 GARDO](https://arxiv.org/abs/2512.24138v1) | potential反证：高uncertainty样本选择regularization、更新reference、奖励diversity，与固定reference防hack压力不同 |
| [24119 GeoBench](https://arxiv.org/abs/2512.24119v1) | potential：形式核验任务分层perception/planning/theorem/backtracking，CoT在部分任务退化，非新增数学榜单即排除 |
| [24111 adversarial objects](https://arxiv.org/abs/2512.24111v1) | potential安全：JVP diffusion方向约束生成自然攻击对象，MDE错误可传播控制；数字/物理实验不等于所有VLA受攻击 |
| [24035 anisotropic denoising](https://arxiv.org/abs/2512.24035v1) | 范围关闭：经典anisotropic算子行动由DQN排序，非生成基础模型diffusion/flow机制；不因标题diffusion收入 |
| [24022 FUSE/MF-RSVLM](https://arxiv.org/abs/2512.24022v1) | potential：recurrent visual注入防language深层visual forgetting，需核是否真机制而非remote sensing任务变化 |
| [24015 CVC](https://arxiv.org/abs/2512.24015v1) | potential：source-preserving/target deviation速度拆分与posterior/Tweedie correction，核误差与真实flow假设，不采用“exact”作保证 |

## Agent、记忆与执行

| v1身份 | 具体贡献判断 |
| --- | --- |
| [24615 Youtu-Agent](https://arxiv.org/abs/2512.24615v1) | potential：execution/toolkit/context解耦生成、Practice/RL接合可能改变适配成本；需辨成熟meta-agent组合与真实训练/执行接口差额 |
| [24613 group deliberation](https://arxiv.org/abs/2512.24613v1) | 重开potential：[v1 PDF §II-A/B、III-D.2](https://arxiv.org/pdf/2512.24613v1)HTML404后读Gaussian task-embedding viewpoint modulation、自博弈weight更新和组件消融；相似度不证明factual support、所谓improved PPO需核，不采纳可靠性保证 |
| [24504 map reasoning](https://arxiv.org/abs/2512.24504v1) | potential反证：partial observation下结构memory胜exploration策略、scale饱和，分别干预体验获取/存储/使用 |
| [24461 belief search](https://arxiv.org/abs/2512.24461v1) | potential：外部posterior belief更新与信息增益surrogate选action，无梯度test-time适应；需核GT对齐reward是否泄漏 |
| [24449 PackKV](https://arxiv.org/abs/2512.24449v1) | potential：动态增长KV有损压缩与解压/matvec融合co-design，memory与带宽/吞吐取舍，不照录cuBLAS数字 |
| [24415 customer attacks](https://arxiv.org/abs/2512.24415v1) | potential安全：统一rubric/uncertainty下domain×payload splitting影响越权让利，需核真实执行权限与只生成答复差别 |
| [24325 MaRCA](https://arxiv.org/abs/2512.24325v1) | 范围关闭：推荐阶段CTDE/MPC revenue-cost分配，没有foundation model训练/推理或LLM协作机制；不把Agent泛指RL当项目主线 |
| [24189 SCP](https://arxiv.org/abs/2512.24189v1) | 范围关闭：科学资源/实验生命周期与物理实验室平台，AI for Science路线暂缓；不借通用协议/授权owner重新引入整套科研平台 |
| [24145 paired seeds](https://arxiv.org/abs/2512.24145v1) | potential评价边界：相同seed匹配随机源、正相关条件variance减少；需核不相关时“weak dominance”及模型适用，不当普遍统计保证 |
| [24040 ROAD](https://arxiv.org/abs/2512.24040v1) | potential：失败logs→decision-tree protocol替代curated gold fitness的冷启动优化，需核debugging新增约束和泛化 |
| [24008 SPARK](https://arxiv.org/abs/2512.24008v1) | 关闭：persona选择+独立RAG/长短memory/共享debate/relay概念框架，只有testable predictions，不公开可改变机制判断的验证或具体新控制 |
| [23959 HGMem](https://arxiv.org/abs/2512.23959v1) | potential：hyperedge memory演化高阶facts/thought关系影响后续子查询，非passive accumulation |
| [23880 CASCADE](https://arxiv.org/abs/2512.23880v1) | 范围关闭：材料/化学SciSkillBench与自主实验/论文重现，明确科研应用路线；未借Agent memory重新引入AI for Science |
| [23862 Infini-Attention study](https://arxiv.org/abs/2512.23862v1) | potential反证：300M预训练下多次compression检索退化与balance factor，虽旧机制但新成立边界可准入 |
| [23852 Trellis](https://arxiv.org/abs/2512.23852v1) | potential：固定KV memory两pass recurrent压缩、online-gradient/forget gate更新，区别仅低比特存储 |
| [23844 CAB](https://arxiv.org/abs/2512.23844v1) | 关闭：91组用户规则/15访谈归纳行为期待与时间/工作轴，未给具体模型执行blindspot或可验证机制修正；保留人机研究价值但不借通用可靠性词凑贡献 |
| [23809 ZTA-FL](https://arxiv.org/abs/2512.23809v1) | 范围关闭（安全题摘已完整读）：IIoT generic IDS联邦/TPM/SHAP/对抗训练，无大模型资产或Agent模型execution；不采用其认证/Byzantine保证 |
| [23647 NestBrowse](https://arxiv.org/abs/2512.23647v1) | potential：nested结构分离浏览interaction control与page exploration，减ReAct verbose负担；需要实际action/completion边界 |
| [23646 OmniAgent](https://arxiv.org/abs/2512.23646v1) | potential：audio引导coarse-to-fine temporal定位与按需工具感知，而非dense frame captions；核budget与跨模态归因 |
| [23631 BOAD](https://arxiv.org/abs/2512.23631v1) | potential：bandit arm为subagent并按team helpfulness credit探索hierarchy，区别手写roles；需核有限评估budget与OOD |
| [23611 InfTool](https://arxiv.org/abs/2512.23611v1) | potential：API规格生成verified轨迹→gated GRPO→针对能力gap再生成闭环，需辨循环质量提升与自我偏差 |
| [23483 TV-RAG](https://arxiv.org/abs/2512.23483v1) | potential：temporal offset检索+entropy frame采样改善多channel时序丢失，需拆时间衰减与帧预算 |
| [23480 software supply chain](https://arxiv.org/abs/2512.23480v1) | 重开potential/安全：[v1 §VI-F](https://arxiv.org/html/2512.23480v1)移ledger不改变detection而LLM/RL分别影响recall/false-positive主张，具体区分审计与检测的局部验证可能有贡献。不能因成熟组合关闭；不接受其ledger trust guarantees或provenance不可用概括，具体威胁/授权/对照仍未审 |
| [23445 behavior coverage](https://arxiv.org/abs/2512.23445v1) | 范围关闭：传统MPC pedestrian/MAS仿真coverage，不含foundation VLA或world-model机制，不用autonomous一词倒推 |
| [23424 AKG](https://arxiv.org/abs/2512.23424v1) | potential：跨DSL/backend生成迁移与correctness/portability检查可能改变kernel交付边界，需核是否只有整体PyTorchEager对比 |
| [23366 AGRO-SQL](https://arxiv.org/abs/2512.23366v1) | 重开potential：[v1 §3.1/Limitations](https://arxiv.org/html/2512.23366v1)DAG数据库augmentation防accidental execution correctness、Gen-as-Check分歧审计及execution等价不保证NL faithfulness的边界；不是只借GRPO/verified标签 |
| [23320 MESA-MIG](https://arxiv.org/abs/2512.23320v1) | 重开potential：[v1 §4.4/Table1](https://arxiv.org/html/2512.23320v1)逐attribute agent删除对应semantic/style/diversity/emotion的不同failure signature，局部可归因验证；音乐任务本身不构成贡献，不采用人工配对的通用效果 |
| [23294 SemCom](https://arxiv.org/abs/2512.23294v1) | 重开potential：[v1 AKB-JSCC case study/Fig4](https://arxiv.org/html/2512.23294v1)LVM source prior与entropy/SNR/上一action输入RL rate controller构成codec/资源联合设计；只有w/o channel KB消融，不授source/channel双侧独立归因。AWGN、训练SNR与baseline CBR不同的限制保留；只核该差额，6G愿景不是新机制 |
| [23236 KernelEvolve](https://arxiv.org/abs/2512.23236v1) | potential：多抽象/多硬件graph search及runtime context检索prompt，真实AI kernel交付和正确性验证；DLRM不自动排除全部kernel系统，100%只限测试集 |
| [23212 LIMO](https://arxiv.org/abs/2512.23212v1) | 范围关闭：STT-MTJ annealer/TSP与普通图像分类face检测，未服务大模型计算；不将所有matmul硬件扩入本主线 |
| [24255 oblivious graphs](https://arxiv.org/abs/2512.24255v1) | 范围关闭：trusted processor一般graph analytics，无模型计算/状态/推理应用链，100x不是模型系统收益 |
| [23961 KYC recommendation](https://arxiv.org/abs/2512.23961v1) | 范围关闭：KYC推荐content vertical/nDCG比较，不含具体foundation模型或Agent协作机制 |

## 官方月身份有界补检的新命名

| v1身份 | 具体贡献判断 |
| --- | --- |
| [23941 response analytics](https://arxiv.org/abs/2512.23941v1) | 范围关闭：学生答复评分teacher priors/embedding residual线性分析，非foundation模型训练/评价机制，不借Ch66引回教育应用 |
| [23966 LoZA](https://arxiv.org/abs/2512.23966v1) | potential：limited-compute将full attention转sparse，prefill/decode兼顾与million-context midtraining；需核稀疏模式/转换代价 |
| [23971 CEC-Zero](https://arxiv.org/abs/2512.23971v1) | potential：生成错误+cluster-consensus reward无人工标签、声称unbiased/convergence需核条件，不仅CSC成绩 |
| [23988 RISE](https://arxiv.org/abs/2512.23988v1) | potential：step级SAE自动发现/干预推理行为与confidence，区别word-level人工标签；需核方向与行为因果 |
| [24000 WISE](https://arxiv.org/abs/2512.24000v1) | 范围关闭：Fakeddit20k fake/satire传统轻量分类benchmark，未检验foundation推理/可靠性新边界 |
| [24098 SageMaker demo](https://arxiv.org/abs/2512.24098v1) | 关闭：集中既有云训练操作资料的首次使用教程，无新增training runtime/接口机制；不是否定文档价值 |
| [24265 DATAMASK](https://arxiv.org/abs/2512.24265v1) | potential反证：quality-only长期收益递减、diversity-only丢质量；policy-gradient mask统一joint selection，需核selection训练总成本 |
| [24297 FIGR](https://arxiv.org/abs/2512.24297v1) | potential：RL学习何时构造可执行视觉中间状态增强global constraints，数学reasoning机制非AI for Science应用 |

## 日期与采用边界

70个potential各自上述官方链接就是必要日期请求身份；不为同身份反复请求。已穷尽可用官方日期方法：日粒度announced_date_first不受支持、catchup12/31 Cache miss、月长表身份、Submitted与原始2025假日排期均不能提供逐篇实际首次公告；不从空响应补零、不假定所有Submitted都同批公开、不把Jan/Feb datehold移回December。可接受替代为逐ID官方new公告/历史RSS或作者可验证首次公开范围，且整个范围落本窗。当前逐项安全终态隔离：不评分、不进入确定候选、不正面采用、不进Books、不支持Coverage/Evidence/零遗漏/性能/安全保证。恢复只重开具体ID与真实所属Daily，再读必要精确正文/owner/相邻。

16项贡献/范围关闭不依赖精确日，不额外造日期请求。9项共同错误影响的含糊准入已完成上述局部核，原摘要关闭全部撤销；普通准入待办0重新建立，不沿用旧ready标签。重点请root定点检查全部安全/设计反证potential和9项重开，普通关闭24008/23844/24505/24098等按理由分层抽样；作者不声称这些已独立通过。
