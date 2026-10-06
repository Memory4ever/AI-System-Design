# 2026-02-17 准入理由纠偏

95是原始日期门槛成立的潜力身份，不是最终候选分母；完整139题摘原证不变。撤去此前“有公式、接口、state、消融即有长期贡献”的共同理由。只重开受此理由影响项，不设保留率，也不因证据费时、Books已覆盖或访问状态排除。普通未完成继续。

## 2602.12709 ReFilter — 准入前关闭，root actual 校准通过

完整题摘声称 context encoder + token gate + latent residual fusion 能抵御 top-k 噪声；必要 exact-v1 §3.3–3.4/B50–74已读，原块见 V3_ADMISSION_BOUNDED_CORE.md。具体是最后 token state 与 context token 拼接线性 scorer/sigmoid、跨 query 共享 position prior、weighted sum LayerNorm 与 residual；不作 softmax 的求和约束是局部 fusion 模块选择。原题摘与定点核心没有建立新的 filtering 有效条件、噪声强度/相关性边界或足以改变检索设计判断的证据；仅“更多 top-k 会带来无关信息”是成熟压力，局部 QA 指标与组合本身不满足本项目门槛。不是否认其学术/工程价值，也不是因为 Ch76 已有主题而排除。当前 abs 只有 v1，无撤回/纠错说明；不展开 biomedical 应用或全部消融。

## 2602.12628 RL-Co — 准入前关闭，root actual 校准通过

完整题摘与 exact-v1 IV-A/B、V-C/B146–153已读。旧判断是 sim interaction 扩展行为而实域监督防忘；实际加入 mixed SFT warm-start 后 sim RL + real-SFT regularizer。π0.5/PickPlace 去 StageII real-SFT 后 real81.38→40.25而 sim 上升、去 StageI real 为12.5、两者去为6.25，验证这份配方的初始化/保留依赖；sim-SFT 缺失导致三百万步仍弱也是该初始化控制。并未建立超出已知 sim-domain forgetting/BC anchoring 的非显然机制或新有效性条件；单任务对成熟两阶段 recipe 的必要性消融不自动成为长期贡献。因此在最终分母前关闭，不按指标高低或现有 owner 覆盖缩池。当前 abs 有 v2/v3/v4，但版本号与后续正文不证明重要修订；当前事件页未标纠错/撤回，不全版本 diff。原源/完整题摘与本窗共同日期证据保留。

## 其余必要含糊范围

12528、12640、12687、12734、12996、13042、13067、13081、13086、13131、13195只读决定准入的有限核心。已读不等于准入；继续明确原约束→非显然实际差额→具体选择，成立后再评分和补相应必要证据。13081安全提示/13131算法与文字矛盾必须保留，不因拟排除删除反侧；13067理论/视觉组件不得仅凭 spectral/Transformer 词映射 owner。

### 下一批五个具体准入入口（root actual 准入校准通过；必要证据待完成）

- **12528 DiffuRank**：自由dLLM listwise解码不保证有效permutation → 由全mask位置logits作assignment，并以结构DocID mask训练/约束生成 → reranker选择应把并行解码与permutation有效性分开，不把任意并行token输出直接当rank list。新增不是assignment算法本身，而是其相对vanilla解码的有效性合同；质量/配置/费用留证据阶段核。
- **12687 CUD**：全局teacher smoothing会改写非目标dark odds → 对GT不符的top1做budget/margin控制的质量转移，其他class保持；teacher entropy按困难样本塑形 → 可区别选择teacher目标修正与单一温度。仅此有界条件性替代入口，不因一般校准原则或公式准入；unique projection/实际保证需必要原证明及控制，不能从模块名授予。
- **12734 Real2Gen**：生成mesh不带真实metric scale/canonical orientation，VLM caption属性估计不足 → 将生成/实例匹配与RGBD语义对应结合恢复尺度/pose，IV-C同输入比较caption估计 → sim asset必须从“语义像”进入可核物理grounding，而不是默认生成形状可直接仿真。89个matchable mesh切片和非同构canonicalization proxy须保留，不授通用机器人policy。
- **13042 GPTZero**：纯Human/AI AUC不能判断混合文档taxonomy → §5.5相同三种训练标签在pure集合AUC约96%却在mixed population分类不同 → detection评价必须固定mixed语义与目标人口，不能用AI probability平均当内容AI比例。本入口是可核评价盲区而非厂商accuracy/商业实现；40k内部集、architecture未披露及阈值选择留必要证据核。
- **13195 ConverSeg**：categorical/spatial referring成绩未测intent/functional grounding → 新functional/affordance pixel任务及同模型数据配比/训练顺序反侧 → 要重验功能意图与传统referring两种population，不从SAM2/LoRA组件组合授普遍空间理解。Dense EOS删除近似不变与传统任务回归不得隐藏，实际质量与合成GT来源留证据核。

### 下一批六个准入前关闭（root actual 必要核心校准通过）

- **12640 ImageRAGTurbo**：retrieved H-space blend/SLERP，再加cross-attention adapter与decoder LoRA，属于已知retrieval conditioning和one-step adaptation的局部组合；best-per-prompt weight是额外oracle选择，未提出新可实施blend条件或非显然generation路径差额。不是因为提升小或只单模型而排除。
- **12996 Know More**：按采样正确率/token entropy命名mastered/confused/missing后检索/合成/SFT，并加正确/错误符号entropy辅助RL；仅把已知knowledge-confidence混杂与定向数据/entropy calibration拼成recipe，未建立新的知识可识别性、数据收益条件或可靠性机制。“认知边界”措辞不作新增内部状态证据。
- **13067 SIEFormer**：III-C具体是低阶graph filter与learned FFT/value分支、zero-init保留pretrained输出；normalized-Laplacian谱界是成熟图理论。没有从这份GCD模块组合建立新的foundation学习机制/有效性条件，不能以spectral解释或局部分类指标替代本项目门槛；不否认视觉模型研究范围本身。
- **13081 Flexible but Fragile**：planner/executor工具与event checks/operator intervention是成熟结构；§6 qualitative例子展示prompt先验忽略指令/路径次优，未建立区别已知prompt敏感与执行授权分离的新失效路径或成立条件。保留实机器人e-stop必要反侧，Valdemar该实验是simulation而非两平台均实机；不把安全失败删掉，拟EX仍需root定点核。
- **13086 UniManip**：AOG scene/task graph+memory recovery，IV-C用morphological closing、重力向下occupancy completion、ESDF/A* clearance与SLERP。这是已知保守未知空间与hierarchical闭环组件集成，未提出新policy/几何有效边界；不得以state、图、collision-free或量化指标自动准入，不认证全robot collision guarantee。
- **13131 APPO**：retainment/textual gradient/EA/Pareto与consistency rewrite是已有prompt优化组件；adaptive mutation按历史CLIP similarity归一化也是局部controller替换，未建立非显然搜索边界。**必要矛盾保留**：§4.3.6/B98高相似度应提高mutation，Alg4/B101的(vmax−savg)/(vmax−vmin)却随savg递减；这影响采用具体controller但不把未准入的组合自动升级为长期纠错论文。拟EX需root核此信号，不能删反证。

本批原块见V3_ADMISSION_BOUNDED_CORE.md；题摘/原源均保留。root已实际核五个有界入口与六项排除理由，并核13081真实急停/模拟区分、13131符号矛盾；排除不授“无安全/纠错信号”。139题摘目前44EX、87个日期确认后仍需贡献/必要证据处理的身份、8早Submitted隔离。87不是冻结最终候选分母；五入口不默认Deep，12687仅GT错峰有界质量转移、13195仅传统referring遗漏functional/intent评价继续，不把recipe公式或混训练防忘评分。
# 追加定点

## 追加五项必要含糊定点（作者准入判断；非全文队列）

- 12662 CogRouter：固定step思考深度/将终局优势广播不能比较成功动作的不同思考成本 → exact-v1 III-D/B72–87保留同history与成功action，四level改写thinking后用action logprob作权重分配 → 训练可选择动作条件thinking level的信用接口，不把confidence当正确性；只用ALFWorld主线，ScienceWorld科学应用不另入。此非四级ACT-R命名贡献。拟2+1+2=5标准。
- 12852 WebClipper：直接删除低收益call会断原trajectory支持与ReAct衔接 → B33–60区分信息多producer/动作多predecessor、抽取依赖图做反向支持闭包并只重写跨删步thought → pruning必须保护所依赖信息而非仅缩短路径。LLM图/三次完全集合多数与PPL不授true minimality或causal sufficiency，符合有界训练数据替代。拟2+1+2=5标准。
- 12916 RTWI：对完整trace单一text confidence忽略tool cue acquisition与final reasoning两个失败来源 → B34–60按两stage top-k entropy分别做query warmup阈值，任一失配可停止再加权vote → 视觉工具使用的采样预算可按producer/consumer阶段分配，不把tool调用text可靠性认证visual evidence truth。不同于“filter+vote组合”名称，具体双stage接口成立边界待实验核。拟2+1+2=5标准。
- 13013 ASID：single-pass caption fusion以覆盖换hallucination → B77–89的attribute Error/Missing只改受影响字段，保留其他内容与ASR/timestamp原证，并有同video stage-wise下游反側入口 → multimodal data curation应区分coverage、属性修复与时间grounding而非只综合caption评分。本文新增不是标注数据量或现成模型名。拟2+1+2=5标准。
- 13055 Curriculum-DPO++：题摘所述rank/layer gradual schedule本身只是成熟model curriculum；定点exact-v1 B51–69还实际新增consistency-model preference proxy，以冻结reference PF-ODE两点consistency distance差替noise-prediction项并排除EMA target。需区别无density的consistency residual代理与原DPO log odds，而不是借DPO名字授概率保证；作为有限生成偏好目标替代可继续标准核，成熟curriculum/zero-padding rank扩展不计新分。拟2+1+2=5标准。Prompt-mask负样本不授真实human preference或必更差。

五项raw为V3_ADMISSION_<ID>_CORE.txt。只为准入事实定点读完即停；后续才按评分必要控制/反側，不读全部appendix。12892题摘前一行误述为soft reward已纠正：实际是Soft Discrimination Score的无SFT pretraining checkpoint评价，而非保留能力训练。

## 追加六项含糊事实与13165定点裁决（root实际核心准入校准通过）

- 12609 QuEPT：多bit共同校准不能让最低precision支配其他组 → B34–65实际按H/M/L采样，共用prefix-rank slices且低bit追加capacity，先稳健high-bit token再融合其他features → 需要考虑multi-bit artifact的联合容量/校准输入而非独立PTQ集合。拟5分标准准入，只此实际共享/误差耦合，不给LoRA或ToMe名称评分。原源V3_ADMISSION_12609_CORE.txt。
- 12674 X-KD：MiniLLM逆向reward蒸馏仍需policy-gradient稳定化且不支持seq黑盒 → §3/B49–77以student logprob对应Q、reward posterior KL与TD-consistency正则加在seq/SFT objective → 可选择额外reward-encoder的监督式目标而非必用policy-gradient；不声称唯一真实teacher reward被恢复。拟5分标准准入。原源V3_ADMISSION_12674_CORE.txt。
- 12962 TriGen：MX共有exponent轴不能按普通tensor直接transpose → IV/V B104–118把INT4投影、per-channel scale位置与TMATMUL次序联合改写，compile-time transpose W，延后SW到attention结果 → 混合精度compiler需保存scale轴/算子消费方式，而不只静态MX+LUT+scheduling组合。拟5分标准准入仅此表示/执行合同，电路面积/latency条件留证据审阅。原源V3_ADMISSION_12962_CORE.txt；不用成熟tile/LUT本身准入。
- 13059 TraceBack：row/column attribution与final-answer overlap可漏start/end等隐式计算输入 → §4/B78–97把答案span、中间subquery与cell coordinates对齐，CITEBench评价这些隐式cell → 测量引用是否覆盖真实计算输入的评价粒度需区别最终答案命中。拟5分标准入口是可核benchmark blindspot，不是multi-agent/prune组合；FAIRScore B169–176的atomic facts+LLM alignment不自动认证minimal sufficiency或隐式输入，必要反侧后核。原源V3_ADMISSION_13059_CORE.txt。
- 13185 FlexAM：first-frame appearance不能表达后来出现region，原3D轨迹signal不编码当前depth且临近point身份混淆 → B14–16/38–53分别用arbitrary masked frames、initial-coordinate identity/frequency与time-varying depth及edit mask → appearance与motion条件要支持新出现对象和相近轨迹，不只加3D词/位置编码名称。拟5分标准准入这一条件表达变化，精度/解耦与点密度反侧留必要核。原源V3_ADMISSION_13185_CORE.txt。
- 13194 Semantic Chunking：完整题摘和B14–26研究的是用LLM生成semantic tree、随机K-ary树ensemble解释文本entropy；把LLM当测量工具，crossentropy上界是已有信息论，comprehension相关性留future hypothesis。未建立模型学习/表示/训练或RAG chunking选择的新有效性条件，只把语言文本结构描述及拟合映射到Books不足本项目准入。建议准入前EX；不否定随机树数学价值，也不凭未做downstream指标关闭。原源V3_ADMISSION_13194_CORE.txt。
- 13165 Krites：§3 B65–79实际是近阈值cache miss后的background judge/upsert，LWW/timestamp可选保护、相同LRU/TTL与常规限流重试；触发请求先走原决策故不变是该成熟异步流程本身。没有不同于background validation/fill的新版本一致性、权限绑定或queue/resource隔离条件。§4 B81用已有等价class oracle、不实际跑judge；curated-origin hit替换不是已测安全/质量保证。建议准入前EX而不是借async/criticalpath词增分，保留Figure1“strictly improving safety/quality”未经独立测量的原信号。原源V3_ADMISSION_13165_CORE.txt；HTML exact-v1页metadata仍v1/13Feb，正文格式date August24不得用于更改首公开，排除不为日期扩恢复。

只对上述决定事实一次定点，停止准入澄清；root已实际核七项核心，12609/12674/12962/13059/13185有界5分标准入口通过，13194/13165准入前EX通过。仅准入层通过，前五必要证据仍待办，最终分母未冻结；相同ID原始AB/原日期保留。139题摘现46EX、85日期确认且仍需贡献/必要证据定稿、8早Submitted保留；不把85日期身份当85候选。
