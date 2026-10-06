# 03-19 补03-18：有限后批准入判断

只处理已由四个模型/训练/推理/多模态/可靠性窄主题恢复的完整题摘，不把256标题或已下载37项自动列候选。题摘原件为同目录SUP_AB_<ID>；精确身份与当前header已读取，普通后续版本号不触发全史diff。以下为作者判断，除具名root项外仍须必要证据/独核；不是完成收据。日期使用与首批同标准的availability日下界＋SUP_LATER_METADATA（32）/MISSING5（5）findable/registered同BJT03/18公开上界限定推断，非Submitted=public或精确公告时刻；具体先稿信号另核。

## 明确潜在增量：准入后继续必要原证

| 精确v1 | 原约束 → 完整题摘实际增量 → 影响的判断 | 作者评分/范围 |
| --- | --- | --- |
| [16164 Power-Aware](https://arxiv.org/abs/2603.16164v1) | 单一power-cap经验不能跨工作负载 → H100/H200/MI300X在视觉与LM续训/推理的非一致能效曲线，尤其两种HBM配置同厂GPU也不同 → power cap需绑定算子/带宽与设备，而不是全fleet一个数；并非仅新增bench目录 | 2+2+2=6；核负载/时长/质量与功率测量代价，未证通用最优 |
| [16428 SlideFormer](https://arxiv.org/abs/2603.16428v1) | 单GPU微调状态超过HBM且naive offload阻塞 → sliding GPU层窗口、CPU更新及多级I/O异步重叠/内存生命周期 → 需核状态驻留、依赖和吞吐是否来自机制而非不同精度/适配范围 | 2+2+3=7；数字暂不采用 |
| [16104 Helium](https://arxiv.org/abs/2603.16104v1) | 单call engine不知跨call依赖 → Agent query-plan operator、proactive prompt/KV reuse与cache-aware workflow调度 → 可以改变关键路径与缓存生命周期选择，不只把workflow改称query | 2+2+2=6；核缓存有效性/全部费用与端到端对照 |
| [16514 FleetOpt](https://arxiv.org/abs/2603.16514v1) | 最坏context统一容量浪费 → 两pool边界的边际成本条件及压缩跨越硬路由cliff → 重新考虑长度分池的容量/质量共同边界 | 2+2+2=6；work-in-progress不直接排除；同作者FleetSim是相关但非自动同事件/非已审重复，推导与压缩质量尚未核 |
| [16435 VQKV](https://arxiv.org/abs/2603.16435v1) | scalar/低秩KV在压缩/重建之间受限 → training-free vector codebook/index表示KV → 核codebook构建、查表/解码与在线预算，区分HBM占用与端到端收益 | 2+2+2=6；不能把82.8%或4.3倍照录普遍收益 |
| [16440 CGC](https://arxiv.org/abs/2603.16440v1) | PPL/importance代理未显式描述能力 → SAE breadth/entropy/consistency密度用于预算与phase-transition论证，并有PPL负面结果 → 核密度代理与功能能力/冗余是否真的联系；rho≈0非独立证明 | 2+1+2=5；小模型和负面结果不排除，理论桥必须核 |
| [16105 ZipCal](https://arxiv.org/abs/2603.16105v1) | 校准选择依赖昂贵model-specific信号 → Zipf词汇多样性model-agnostic选择 → 核词频代理在哪些压缩任务保留质量以及是否只是省选择费，不等压缩执行加速 | 2+1+2=5 |
| [16127 WSO](https://arxiv.org/abs/2603.16127v1) | 只按pretrain loss批准LR decay → 1B/8B不同训练长度中pretrain较差而SFT较好的反排序 → 需将pretrain checkpoint与后续适配目标分验，sharpness解释不能预支因果 | 2+2+3=7；acceptedICLR2026标签不自证早发，不凭conference名称隔离 |
| [15803 Priority Mask](https://arxiv.org/abs/2603.15803v1) | uniform corruption不区分信息密度 → complementary reasoning/syntax样本与priority mask → 重新考虑DLLM masking目标与context-collapse；核数据标注/预算及非机制替代解释 | 2+1+2=5 |
| [15923 Recall Theory](https://arxiv.org/abs/2603.15923v1) | 无限数据/正交embedding的存储解释 → 有限N、随机非正交d、L在单层GD early phase的乘性约束与统计lower bound → 需区分learned recall与理想attention容量 | 2+1+3=6；ICLR2026标签不自证早发，不泛化到完整LLM |
| [16535 SympFormer](https://arxiv.org/abs/2603.16535v1) | feature-only attention flow → token携带velocity的惯性/Hamiltonian离散块，linear/bilinear Stein flow与elliptical preservation → 核多状态演化假设/离散稳定性与oracle count非GPU时延 | 2+1+3=6 |
| [16140 Noisy RLVR](https://arxiv.org/abs/2603.16140v1) | 已声称100%错标签也可学 → 原错误集合残留clean、重新verification后math/Text2SQL反退 → 改变噪声训练的证据前提，不能泛化一切噪声或借名称关闭 | 3+2+3=8；设计反证，必要深入 |
| [16157 DyJR](https://arxiv.org/abs/2603.16157v1) | replay直更旧样本会过拟合 → recent FIFO/adaptive buffer作为JS动态分布约束而非准确样本直接梯度 → 需核off-policy分布/参考刷新全费和diversity/质量 | 2+1+2=5 |
| [16158 EGCA](https://arxiv.org/abs/2603.16158v1) | outcome advantage均匀扩散 → candidate/reference同instrumentation earliest divergence映射token span并mask后续 → 核可比较执行语义、reference权限、非对齐改写与18%全费 | 2+1+2=5；workshop2026不得自动当早发或低质 |
| [16223 DCRL](https://arxiv.org/abs/2603.16223v1) | majority伪标签陷spurious mode → 临时unlearning产生explorer与anchor双共识harmonic目标 → 改变自举reward的独立性/费用判断，核为何不是两个同偏差分布 | 2+1+2=5 |
| [15957 GASP](https://arxiv.org/abs/2603.15957v1) | self-play困难不等有信息 → 真实hard goalpost引导easy→hard variant curriculum → 改变开放数据生成的grounding选择，核teacher预算/goalpost泄露与pass20协议 | 2+1+2=5；两个2026workshop仅日期线索 |
| [15990 W2T](https://arxiv.org/abs/2603.15990v1) | LoRA factors的gauge不唯一 → QR/SVD canonical representation后weight-space预测 → 改变adapter检索/评估的representation选择，核退化奇异值/符号与预测不等模型能力认证 | 2+2+2=6 |
| [16856 OEL](https://arxiv.org/abs/2603.16856v1) | 直接回放user trajectory及离线训练不可用user env → 提取经验再on-policy context distill入参数的循环 → 核知识来源/模型版本一致性、隐私与额外采集费用 | 2+2+2=6 |
| [16843 LEAFE](https://arxiv.org/abs/2603.16843v1) | 只outcome训练使成功模式变窄 → feedback summary/回退branch搜索的修正轨迹SFT → 核固定交互费下的recovery/passk与GRPO分布差异，非一般reflection流程 | 2+2+2=6 |
| [16673 RARRL](https://arxiv.org/abs/2603.16673v1) | 固定reason/act时延和成功冲突 → 学高层whether/role/budget resource policy → 核经验latency profile与真实closed-loop是否一致，不把ALFRED映射批准低层控制 | 2+2+2=6 |
| [15759 SimDist](https://arxiv.org/abs/2603.15759v1) | real RL低数据下长credit困难 → sim dynamics/reward/value结构蒸馏让real只short-horizon ID → 核哪些value/reward能跨域保留及sim-to-real偏差，而非仅换sim数据 | 2+2+3=7 |
| [16195 S-VAM](https://arxiv.org/abs/2603.16195v1) | 多步生成昂贵/一步feature noisy → 自身多步video的VFM目标蒸馏至一步decoupler → 核几何/语义代理质量及teacher费用，不把一步特征等真实future | 2+2+2=6；v2仅次日普通版本未见具体变更，不自动全diff |
| [16218 Velocity VLA](https://arxiv.org/abs/2603.16218v1) | 低频pose chunk对低层feedforward缺速度 → finite difference桥与C2 B-spline空间接口 → 改变compliance/动态tracking的交接，核数据/控制器共同变化与单任务范围 | 2+2+3=7 |
| [16139 IOMM](https://arxiv.org/abs/2603.16139v1) | UMM generation costlyphase依赖paired text-image → image-only masked视觉pretrain再少量paired alignment → 核语义/视觉能力分期与总数据/费，不能以SOTA单数准入 | 2+2+2=6 |
| [16373 SemTok](https://arxiv.org/abs/2603.16373v1) | grid pixel codec难紧凑global semantics → 2D→1D discrete、semantic alignment与two-stage generation → 核可变token/位置恢复与reconstruction/semantic目标交接 | 2+1+2=5 |
| [16256 FrameRepeat](https://arxiv.org/abs/2603.16256v1) | 更长CoT可能丢视觉anchor → AOI marginal repeat-gain监督frame scorer/推理强化帧 → 核加token费与受控视觉漂移反证，不将重复上下文自动归机制 | 2+2+2=6 |
| [16870 VideoReasoning](https://arxiv.org/abs/2603.16870v1) | reasoning被解释为frame时间序列 → denoise-step探针、层分工与多seed latent trajectory ensemble → 核实际干预/匹配算力是否支持CoS而非只可视化归因 | 2+2+3=7；具体设计反证必要深入 |
| [16669 Kinema4D](https://arxiv.org/abs/2603.16669v1) | 2D/staticcontrol难保机器人精确几何 → URDF运动学4D控制与generative环境RGB/pointmap反应分责 → 核kinematic精确不等环境物理真值/泛化 | 2+2+3=7 |
| [16860 DreamPlan](https://arxiv.org/abs/2603.16860v1) | real planner RL昂贵且危险 → 初始次优探索训练action video model后想象ORPO → 核modelerror/reward/planner训练与最终real验证边界，非只用现成想象术语 | 2+2+2=6 |
| [16086 HEAR](https://arxiv.org/abs/2603.16086v1) | chunk openloop盲区会丢短促声音 → 因果stream Historizer/未来audio codes/flow action及strict timing协议 → 改变音频状态保留与决策clock选择，核泄漏与真实delay预算 | 2+2+3=7 |
| [16152 HIPO](https://arxiv.org/abs/2603.16152v1) | 多目标偏好不明确priority不对称 → systemcompliance CMDP/primaldual训练约束 → 核constraint估计/可行性与userutility，不将训练统计约束当执行鉴权或hard保证 | 2+2+2=6 |
| [15800 EchoSafe](https://arxiv.org/abs/2603.15800v1) | 只unsafe拒绝混淆安全意图 → minimal safe/unsafe pairs受控上下文评价＋retrieved self-memory → 核paired evaluator/reflection记忆污染和false-refusal，非只扩大榜单 | 2+2+2=6 |
| [15809 StubbornNeighbors](https://arxiv.org/abs/2603.15809v1) | consensus可被一个persuasive agent控制 → FJ动理模型与trust-adaptive communication干预 → 核opinion抽象/LLM对照与抗攻击—协作退路，不当通用安全保证 | 2+2+2=6 |
| [16475 CausalFaithfulness](https://arxiv.org/abs/2603.16475v1) | 自洽intermediate结构未必决定答案 → deterministic structure→decision任务的controlled edit唯一正确输出，toolderivation优于提示 → 修正schema≠causalcommit证据，核干预是否与原input冲突及适用范围 | 3+2+3=8；设计反证必要深入 |

## 两项歧义的定点core：不扩大附件

[16093 Joint AV](https://arxiv.org/html/2603.16093v1)：完整AB后只核§III-C/Eq15–16、IV-C/D/E/Table1与结论。方法是原有CogVideoX输出与prompt再送MMAudio；重训MM-Diffusion和两新data collection是场景/数据实例。所谓joint latent失败只描述异构decoder不稳定，未给定位的必要条件或受控局部反证。Table1跨concert与AIST++且unconditional/text条件不同，不支持替代设计归因；这不是因为负面或小数据排除，而是未识别会改变本项目判断的机制/边界。作者拟贡献EX，待代表排除独校，不另追不影响关闭的精确日期或复制Books。

[16586 Policies on Paths](https://arxiv.org/html/2603.16586v1)：完整AB后定点§3.2–3.5与§4.1–4.5。root已独立实际AB/§3.1–3.5判定具体“step风险→terminal fleet riskbudget”聚合桥足以潜在改变设计解释，正式准入，**1+2+2=5**只给此新增命题，不借成熟guardrail增分。作者已读支持和关键反侧：`1−product(1−π)`在未给joint条件下称union概率；两项完全同相关的同事件π=.5，实际union=.5而product=.75。示例最大敏感等级归一化为score，无校准概率；外发时才非零的评分在后续terminal step可归零，不自动保留先前已发生harm。中心争议拟安全隔离，未提供实验系统不是排除理由；保候选/5分，不EX不NC、不写Books、不支持正面Evidence或安全保证。一次请求只需给出joint条件或有效风险组合、保留历史harm的task-risk定义及score校准材料；可检修正式/受限对照即可定点重开。已送reader必要原证隔离核，不追无关EU法条/厂商全史。

FleetSim16054由root独立接管，见SUP_ROOT_FLEETSIM_20261011.md；6分具体准入/中心争议原证已准备但待reader，不重复原证、不先计安全处置。FleetOpt16514只作者AB，必要Source/owner由root新接管，未开始作者审阅。当前后批34明确AB贡献＋root FleetSim/Paths两项准入；16093拟EX待代表独校，15871同稿先发去重/15958必要日期未定、16077撤回版本单独处理。结合首10（含Google）是拟46家族，尚未完成版本/同源最终归并，不冻结或预支任何后批Source/Books。
