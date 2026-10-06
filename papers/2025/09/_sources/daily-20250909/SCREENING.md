# 09日有界题摘筛选与日期保留

作者Mendel，2026-10-06。`ARXIV_CL_MONTH_RECOVERY.html`实际官方2025-09月列表1–2000/2214，仅浏览05500～06999邻段81个标题（含cross-list），未把月库存作逐项正文队列。相关/含糊72个身份均取得并实际读精确v1完整题摘；`ABSTRACT_REQUESTS.json`67次与`AMBIGUOUS_TITLE_REQUESTS.json`5次保存原请求，`ABS_2509.<ID>v1.html`保留title/abstract/comments/version原字段。下表不算本窗候选，不评分，不授Evidence完成，不用submitted、编号或当前公告政策伪公开。

## 64个具体潜力，公开日待核

只表示下述主张若成立可能改变具体选择；原局部指标未采用。必要原公开证据缺失时不转为贡献排除。

| 2509 ID / 身份 | 原约束 → 题摘实际增量 → 待核选择 |
| --- | --- |
| 05553 CFT | 正向微调可能伤逆向 → 正/负/混淆训练 → 双向知识可用性 |
| 05602 CoPeD | rationale质量混杂 → 正确性加权及错误修订蒸馏 → 监督信号选择 |
| 05605 Icon2 | 指令与偏好干扰 → latent方向筛选与双向偏好对 → instruction tuning控制 |
| 05607 CCGSEO | citation不等于语义影响 → 多Agent测语义内容影响 → 评价对象区分 |
| 05608 BinaryShield | PII与embedding泄漏 → 遮盖/二值随机响应指纹 → 可用性与隐私边界 |
| 05609 unbalanced OT | 帧token并非一对一 → 非平衡OT容许多/一与噪声 → ASR对齐选择 |
| 05634 SER | lexical/acoustic混杂 → 分层去噪对照 → 音频情绪证据来源 |
| 05635 SAID | 固定query关系 → 关系token自适应intent attention → 检索表示 |
| 05657 NASNCode | numeric语义编码不足 → 通用数值encoder/样本排序剪枝 → 代码数据选择 |
| 05660 method learning | question/solution混合 → 分离通用与专有方法 → 迁移监督 |
| 05668 LlamaGENBA | 语言配比/词表与预算 → 三语curriculum及tokenizer/扩容 → 局部训练资源取舍 |
| 05691 numeracy | embedding语义好不等于数值好 → 13模型合成财务数值负侧 → retrieval数值可靠性 |
| 05719 Farsi subjectivity | 数据数目不等于跨人口稳定 → 人口标注与不稳定负侧 → benchmark代表性 |
| 05729 QCSE | 普通上下文表示 → 五种量子语义矩阵方案 → 表示替代潜力，主线关系需校准 |
| 05741 VeriFact-CoT | 单次生成证据不足 → verify/reflect/cite多阶段 → 事实控制潜力，不先授可靠 |
| 05863 LatinX | ASR客观指标与人类判断可能不同 → DPOWER/speaker评价 → 音频测量身份 |
| 05882 friction agents | 轨迹协作缺反事实 → 角色模拟/反事实轨迹 → 群体对齐选择 |
| 05908 PSCJoint | 长hotword列表成本 → 粗细相关交集与竞争筛选 → bias phrase注入 |
| 05915 early exit | 逐样本exit与batch吞吐冲突 → 共享参数/递归深度router → 端到端吞吐取舍；dissertation需事件去重 |
| 05983 TSPC | code switching对齐 → phoneme中间表示 → 跨语种声学接口；v1页面提示较新版本撤回，v2在版本史标withdrawn，不能自动认定v1撤回，也不能忽略该信号；v1结果/采用保持隔离，需精确撤回说明或有效原版本证据 |
| 06065 FilipinoTruthfulQA | 普通翻译评价 → binary choice跨语种事实差距 → 语言切片可靠性 |
| 06074 MFCIG | word-level语义与prosody → 双图建模 → speech生成条件接口 |
| 06100 OLieRA | LoRA更新几何 → Lie乘法/正交子空间 → 参数高效更新 |
| 06160 REER | 正向探索昂贵 → 已知正确解反推reasoning → RL蒸馏样本产生 |
| 06164 EuroParl | 政治/性别偏差测量混杂 → 控制数据评价 → 局部评测边界，不是政策应用指标即排除 |
| 06174 EDIT | 长度/答案分布影响选择 → 长度约束紧凑正确训练 → inference成本质量 |
| 06184 synthetic embeddings | 合成数据并非普遍提高 → 类别局部收益/退化 → data recipe适用范围 |
| 06195 LaKDA | 同query跨语种排序偏差 → language-aware loss → multilingual检索偏差 |
| 06277 NoEncore | 已有unlearning可能留音乐记忆 → 初步失败证据 → 删除保证边界 |
| 06283 SFR DeepResearch | 能力保留与持续RL冲突 → 合成数据/动态工具持续RL → reasoning-agent后训练 |
| 06350 MaskGCG | prompt冗余影响gradient攻击 → learnable mask → 攻击空间与防护评价 |
| 06356 PL-CA | 直接RAG占长context → knowledge augmentation转parametric向量/FFN LoRA → retrieval与权重知识取舍，不能因legal应用名关闭 |
| 06401 MULTICOM | judge跨语言稳定性 → 多语言context及human比较 → 评价协议偏差 |
| 06415 document pruning | token删后文档乱序 → index-preserving分类/max pool → context剪枝可读性 |
| 06501 WebExplorer | 搜索深度与数据质量 → long-to-short探索/演化query → web-agent训练数据 |
| 06518 Crown/Frame/Reverse | 架构形状混杂 → FFN/head非均匀配置提案 → 小规模结构选择；原v1 comments已承认int32数据被uint16 loader误读、每隔一token为0、reported results skewed，故原180M/5B可比性能结论不采用，恢复须正确数据读取的精确修订与重跑 |
| 06524 LAMDAS | 通用领域数据成本 → one-class隐式domain选择 → 数据筛选效率 |
| 06531 SLiNT | 结构与语义gradient干扰 → pseudo-neighbor/hard contrastive/decoupled gradient → embedding结构注入 |
| 06596 HAVE | head贡献不确定 → value magnitude/gating融合 → head-level uncertainty |
| 06631 Guided Decoding | format合法不等于质量 → 3 engine/0–2轮反侧 → 受约束解码评价 |
| 06650 MoLER | retriever训练与多路推理成本 → MoL/CPT/GRPO/MSLF → 训练-推理融合成本 |
| 06652 IntrEx | 单turn/大模型并非engagement代理 → 序列成对学习者标注及7/8B对照 → 主观评价聚合与训练切片 |
| 06675 ParCzech4Speech | 更多音频不等于更可靠对齐 → WhisperX/Wav2Vec处理与3个对齐粒度 → speech数据产物边界 |
| 06704 disagreement | 聚合掩盖主观差异 → BCE/contrastive处理分歧 → label分布选择 |
| 06736 VehicleWorld | stateless FC缺环境预测 → explicit state transition/coordinated APIs → stateful tool-plan界限 |
| 06795 ProCon | 拒答方向drift → projection loss/early warmup分布 → 安全微调能力取舍 |
| 06806 synthetic tabular pretraining | 表格模式学习数据不足 → SCM/随机森林teacher/序列化预训练 → 参数形成；v1题名与月最新不同 |
| 06807 MoGUv2 | 安全router位置 → 可分类层选择与双向adapter → backbone安全能力耦合 |
| 06809 logical reasoning | 神经logical能力弱 → saturation TPTP有效符号证明数据/负侧 → 学习形成，不以形式题目自动AIforScience排除 |
| 06822 RAFFLES | end-success不定位失败 → judge/evaluator迭代step attribution → Agent测量误归因 |
| 06836 COMPACT | 架构变化与压缩混杂 → common-token weighted词表/FFN剪枝保持标准结构 → 部署压缩 |
| 06838 EPT | 英语trust不代表Persian → 六维切片差距 → 语言安全评价边界 |
| 06861 Test-Time Scaling | 更长reasoning不保证知识正确 → 12模型accuracy/hallucination/abstain/recall → 计算与事实风险取舍 |
| 06870 AggLM | 多数票丢minority正确 → RL aggregator/easy balance → 聚合收益/成本 |
| 06888 mmBERT | 低资源受语言采样影响 → annealed低资源/逆mask schedule → multilingual预训练 |
| 06902 PCN | 输出numeric并非受检claim → renderer/verifier/fail-closed → 声明policy的soundness，不授通用安全 |
| 06932 LLaDA-VLA | action autoregression → local special token/分类与层级dVLM → 动作解码路径 |
| 06941 outcome exploration | 重复答案浪费rollout → UCB历史+batch final-answer diversity → 结果级探索 |
| 06945 IRG | 图像生成与reasoning分离 → thinking/image interleave及6学习模式/2阶段 → 视觉反思训练 |
| 06948 cooperative SFT-RL | SFT/RL目标耦合 → bilevel meta-guide → 监督与探索协同 |
| 06949 TraceRL | 固定block/轨迹采样 → diffusion trajectory preference/value/block适配KV → 质量runtime成本 |
| 06952 Wavelength | 理解不等于交流产出 → RSA改善production而非必须理解 → communicative能力边界 |
| 06982 CARE | 生成token即commit → buffer/rollback/reflection guard → 流式安全边界；v1submitted09/01，不按ID顺序归09 |
| 06994 ViLD | OCR组乱序与Judge混杂 → BlockWeaver组匹配/complete-faithful评价 → 文档处理测量；v1submitted09/03，非09日期证据 |

## 8个完整题摘关闭

- 05566 Ad-hoc Conventions：302名人类在tangram命名的心理语言学实验；Agent只有类比，未建立模型形成/执行机制。无正文无贡献的断言。
- 05617 pop lyrics emotion：MOS六情感强度数据、zero-shot与BERT微调应用；题摘没有具体测量盲区、控制反证或学习机制差额，不因小模型本身关闭。
- 05716 ConvQA survey：按history/question/answer组件、数据及技术归纳，题摘没有具体修正现有判断的证据或新执行机制；只此题摘层结论。
- 06221 beamforming assistant：Whisper/embedding RAG/GPT4o-mini用于声阵工程对话，没有新增foundation/Agent失效控制机制。
- 06637 n-gram intertext：文学intertext平均embedding计量，领域应用，不以其数值当模型表示机制。
- 06733 DeepResearch RL survey：三轴综述和方向指导，题摘层未提出具体新机制或评价反证；非所有综述机械排除。
- 06917 Paper2Agent：AlphaGenome/ScanPy/TISSUE科学assistant，当前AIforScience暂缓；不经MCP/Agent owner重新引入。
- 06920 insider threat：Claude合成syslog、GPT检测的应用指标；题摘无新的模型训练/安全执行边界。

另外主题搜索实际读EnergyGPT 2509.07177完整题摘，能源领域LLaMA3.1-8B curated SFT应用，无形成机制差额；不纳入72身份分母。明确领域标题05505/05867/05878/05978/06079/06196/06200/06813/06883分别为医学RAG、TCM GraphRAG、临床摘要、医学图像、SeePhys、招聘流程/ensemble、风机日志和claim extraction应用，简记标题范围关闭；未深读、不声明正文无贡献。若有具体安全/纠错或新机制线索仅重开受影响身份。

## 日期恢复停止

官方日路由2025-09-09为400、250909为404；月路由2025-09恢复200但无public字段。`ARXIV_ADVANCED.html`按announced_date_first/date-from09/08/to09/09与large language model实际200返回no results，不能授零事件。原政策20:00 Eastern给常规09/09 08BJT批次线索，不证明这些身份实际归批次或没有defer/提前公开。具名06184/06861/06949日期查询只得辅助podcast索引，非原公开凭据。不用DataCite注册/接受、submitted或月编号作下界。

上述64身份取得官方公告、作者可核发布记录或完全落窗公开区间后，只重开对应事件的准入/精确v1必要审阅；不重扫2214月库存、不扩其他Daily。非作者DAY直接复读原72份题摘及comments后发现06518的数据读取更正和05983的较新版本撤回信号，现已具名保留并收窄；前者原性能/可比结论失效，后者v2撤回不自动扩大到v1。两项不能仅恢复日期就授采用；当前不是安全或性能认证。
