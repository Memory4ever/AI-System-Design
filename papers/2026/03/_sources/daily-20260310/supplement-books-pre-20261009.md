# 本日 48 候选的实际 Books PRE（作者比较，非 DAY）

补窗为 2026-03-09 北京时间自然日；只用冻结 72 题摘集合。逐项原证与反侧见 [evidence-notes](supplement-evidence-notes-20261009.md)。下面的行号是本次实际读取的局部定位，不是永久身份；节点与路径以 ROADMAP 为准。已读原证不等于独立 Evidence 通过，作者 PRE 不等于独立 Books Gate。root前26项及review_mar10_remaining后22项必要原证/实际PRE已独核，候选侧普通待办0；日级DAY仍待root验收。

“已有覆盖”只针对右栏明确拟采用的稳定论点，未宣称正文已逐个介绍新 recipe；论文的有限新设计及局部反侧仍作为候选留在报告。中心争议不由通用已有原则补齐。无实际长期差额不追加案例名单，写入仍由 root 决定并执行。已完成 BoN、NOBLE、DC-DiT、R4T 的非写入者 POST 另见 evidence-notes。

| 精确 v1 | 当前处置 / owner | 实际正文与具体采用范围（四项窄写另标） |
| --- | --- | --- |
| 2603.06199 FlashPrefill | 已有覆盖 / INFER-PREFILL | Ch43 95–150、182–209、458–470：approximate discovery、row-max/pooled block 下界与选择费用。不是一般保序或无损。root 必要 Source/PRE 已通过；§3.5/T4 作者最后补读已完成。 |
| 2603.05739 BoN | 整合 / MODEL-SAMPLING | root 写 Ch20 Parallel Sampling 后两段与末注：win-rate 目标、pairwise error/coverage 与 M/N 分责；作者实际独立 POST 通过。 |
| 2603.06492 NOBLE | 整合 / MODEL-TRANSFORMER-LAYER | root 写 Ch17 184–186 与末注：不可 merge 的永久低秩非线性支路/训练与部署代价；作者独立 POST 通过。 |
| 2603.06503 BRTR | 已有覆盖 / AGENT-CONTEXT | Ch75 38–72、244–282：capacity、程序化回读/子调用与 compressor+target 总时延；Ch81 292–310 调度费用。少 token 不等少 latency 已承载。50subset 的两组件联合对照仅报告，不称 planner 单因果。 root实际必要Source/PRE已通过。 |
| 2603.06397 R4T | 整合 / AGENT-RAG | root 写 Ch76 setwise段后567/569两段与1342末注：固定 retriever/库/reward→RL fan-out→joint target tensor→diffusion→NN对象部署接口。supplement_20260310实际顺读549–577完整邻接与1337–1347末注、回对§2.3–2.5/3.1/3.4/AppA全部必要原证，非写入者POST通过。迭代采样/预付/漂移再验和事实support边界保留，不授完整RAG加速。 |
| 2603.05618 Safer Traces | 已有覆盖 / PLATFORM-SECURITY | Ch72 238–280、394–429：detector 是分布/policy sensor，final/tool/获授权 process trace 分测及 U/V 预算。root 已核必要 Source/PRE；计数与曲线争议不采用。 |
| 2603.05805 Crosscoders | 已有覆盖 / PLATFORM-EVALUATION-SYSTEM | Ch66 256–284：跨模型重建偏置、字典分区/假阳性与独立 steering，exclusive 不等概念唯一。root 已核 Source/PRE。 |
| 2603.05651 Moral | 已有覆盖 / PLATFORM-EVALUATION-SYSTEM | Ch66 285–313、338–356：adapter/serialization/retry/environment/scorer 与固定答案 judge prompt 漂移/人工 anchor，协议不等模型内在道德。root 已核 Source/PRE。 |
| 2603.05727 Tensor | 仅报告 / MODEL-TRANSFORMER-LAYER | Ch17 74–112 Norm 跨 hidden dimensions/位置与变换责任；14 108–135 完整 attention 读取。DCT feature slices、窄分支/深度共同变化是此结构分支的有限预算对照；没有证明全 Norm 层谱可分或普遍 Transformer 等价，不将具体模块写为新稳定默认。 |
| 2603.05773 Knowing | 已有覆盖 / MODEL-TRANSFORMER-LAYER | Ch17 395–406 readout、minimal pair、patching、weight revision/utility 外验；Ch72 588–603 refusal 管理访问不等消除能力。受限方向干预不签独立/唯一 harm-refusal 内因。 root实际必要Source/PRE已通过。 |
| 2603.05818 RouteGoT | 已有覆盖 / AGENT-PLANNING | Ch79 191–230 搜索预算/训练 teacher 与 runtime controller、297–310 不确定性与实际费用、368–388 完整 verifier。ordinal 成功路径路由 recipe 和 QA full 更慢仅报告，不将 all-fail 删除后的 proxy 当部署质量保证。 |
| 2603.05829 ManyShot | 已有覆盖 / AGENT-PROMPT | Ch74 67–94 示例质量/覆盖/顺序，Ch75 38–72、244–282 容量与前置成本；固定 N 选择/顺序边界。root Source/PRE 通过；GPQA test 生成/过滤不采用。 |
| 2603.05878 ROSE | 已有覆盖 / INFER-TENSORRT-LLM | Ch49 505–517 稀疏 artifact、局部重构/真实 kernel admission，2183–2199 更新顺序与误差度量分责。两级大误差优先剪枝是局部新 recipe，仅报告；不迁移量化 fixed-order 等价证明。root Source/PRE 通过。 |
| 2603.05881 CoCA | 已有覆盖 / TRAIN-GRPO | Ch33 369–387 prefix confidence/scorer 与 outcome/update 目标分责，802–855 segment credit 边界，870–904 reward 测量身份。Brier segment 配方局部评价保留，不由自采 target 授独立正确率/因果 credit。 root实际必要Source/PRE已通过。 |
| 2603.05931 FPGA GDN | 已有覆盖 / INFER-GPU-MEMORY | Ch22 460–560 GDN 状态数学；Ch54 16–35、120–142、488–550 片上减少物化/HBM往返、真实生命周期与 hardware verification。root Source/PRE 通过，特定 FPGA layout/P&R 与估算数字仅报告。 |
| 2603.05960 OMGD | 已有覆盖 / TRAIN-PRETRAINING | Ch28 298–336、512–545 活跃更新/optimizer state，800–915 layer LR 非活跃集合；Ch30 149–175 轮换原参数层/历史 optimizer 驻留。只采更新顺序/coverage 的条件分支；root Source/PRE 通过，不授逐步无偏/AdamW LM 理论率。 |
| 2603.06003 EvoESAP | 已有覆盖 / MODEL-MOE | Ch21 600–640 layer budget、离线 contribution/teacher 特定校准；Ch49 780–817 执行状态费用。层内排序与跨层预算分责已承载。固定 teacher-forced overlap/搜索仅报告，非 online acceptance，反退和不同 GPU 费用保留。 root实际必要Source/PRE已通过。 |
| 2603.06123 SmartCrop | 已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS | Ch24 1778–1807 长度 admission、画布坐标、EOS/VOID 与 commit/质量分责；首 full pass 代理/τ recipe 仅报告。root Source/PRE 通过，FLOPs 非 wall-clock。 |
| 2603.06138 PPG | 暂缓强理论 / TRAIN-GRPO | Ch33 369–387/802–855 前缀估计与分段监督不能自授终局等价。prefix max 改终值、未校正离线 ρ/actual variance 强 claim 争议隔离；窄 shaping recipe 仅报告。需原作者明确目标/采样校正才能重开，不跑代码绕公式冲突。 |
| 2603.06222 SPOT | 暂缓强归因 / MULTIMODAL-GENERATIVE-PARADIGMS | Ch24 1278–1300 冻结表示与迁移上限、Ch23 653–669 对齐不等几何真值。理想 fixed ε/marginal 下 OT 退为 mean φ(h) 的推导由我们给出，不授额外 token 结构；pause+mapping 窄分支仅报告。root 必要公式独核通过，需作者解释 pooling/归一/ε/数值差额。 |
| 2603.06317 EntropyRL | 已有覆盖 / PLATFORM-EVALUATION-SYSTEM | Ch66 723–738 evolving uncertainty sensor 与独立 correctness、Ch33 369–387 prefix BCE/relative margin 目标不同；VN entropy→Platt→confidence LoRA recipe 仅报告，低 ECE 不认证 Brier/AUROC/OOD 每实例。 root实际必要Source/PRE已通过。 |
| 2603.06248 Polarization | 暂缓 / MODEL-SELF-ATTENTION | Eq6/7 与 Appendix15/16 符号冲突、pair 求和口径不一致；Ch14 108–135 attention 路由/Value 方向不等语义贡献可复用，但不能补其中心证明。需作者更正公式与适用条件。 |
| 2603.06274 Stem | 已有覆盖 / INFER-PREFILL | Ch14 123–135 mass、Value 尺度/方向/抵消与执行选择费用，Ch43 95–150/182–209 approximate selector/error budget。TPD/OAM proxy 与 anti-diagonal/minimum/sink recipe 仅报告，不授全模型最优或语义因果。 root实际必要Source/PRE已通过。 |
| 2603.06350 MoEless | 已有覆盖 / INFER-TENSORRT-LLM | Ch21 780–857 router 语义与 replicas/placement epoch，Ch49 696–780 前层预测 expert cohort→暖复制与 async 费用、正常 router 仍权威。采用的早预测分责有具体 coverage；CDF×latency 不签 SLO/账单。 root实际必要Source/PRE已通过。 |
| 2603.06351 DC-DiT | 整合 / MULTIMODAL-GENERATIVE-PARADIGMS | root 已写 Ch24 1274–1276 全局 patch 段之后两段与1859末注；supplement_20260310非写入者实际顺读1258–1285完整邻接、1853–1864末注，回对§3.1–3.5/4.1–4.4必要原证，POST通过。非均匀2D grid→Gaussian/nearest plugback→fullgrid decoder/residual，软预算/全部费用/teacher条件与旧路径边界近文，不授DAY。 |
| 2603.06403 Bandit | 暂缓 / MODEL-SAMPLING | cost/latency 单位、causal CLS 读取未来和 reward 区间口径冲突；Ch20 230–282 校准排序/预算不等 correctness 可复用，不补齐中心目标。需实际 mask/cost objective 原件。 |
| 2603.06505 SpeakInContext | 已有覆盖 / MULTIMODAL-REPRESENTATION | Ch23 518–546 input/训练/部署信息责任、653–669 对齐与原模态 evidence 分责、727–743 encoder/时间/provenance。speech-context contrastive connector 与 gold→CTC retrieval 迁移仅本配方，不授语音内容/对齐真值。 |
| 2603.05754 SafeNight | 已有覆盖 / MULTIMODAL-EMBODIED-VLA | Ch26 725–815 全感知/transfer/controller 链费用，882–965 safety envelope，1170–1226 sensor/projection/真实控制 guard。pseudo thermal/QP 局部机制保留，不授全局安全或 recover。 |
| 2603.05757 Embo | 已有覆盖 / MULTIMODAL-EMBODIED-VLA | Ch26 882–965 imagined proposal/constraint/controller 分权、1170–1226 约束投影与独立动作验收。两次 VLM+retarget/SLSQP recipe 和 6×10 有限联合对照仅报告，非 soft target=hard physical safety。 |
| 2603.05811 LIPAR | 已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS | Ch24 1302–1345 mutable denoising state 与 clean 条件、1350–1440 per-phase anchor/cache budget 与 refresh。clean zero-noise KV/近期 RoPE identity 采用范围具体覆盖，不授 exact/无限时长。 |
| 2603.05815 HiLAM | 已有覆盖 / MULTIMODAL-EMBODIED-VLA | Ch26 135–153 high-level latent target→embodiment decoder/controller、1170–1226 latent 监督非可执行动作。freeze high/finetune low 条件分支及更深未更优仅报告，不授 observation-only 部署。 |
| 2603.05868 AnyCam | 已有覆盖 / MULTIMODAL-EMBODIED-VLA | Ch26 725–815 camera/coordinate/calibration、adapter费用与全 loop 验收。视图重绘 adapter→frozen policy 具体 recipe 留报告，sim 还要 LVSM FT、real policy 先 LoRA，不称任意 camera 免训练/安全。 |
| 2603.06001 IGAR | 已有覆盖 / MULTIMODAL-EMBODIED-VLA | Ch26 1170–1226 sensor敏感与controller guard、1350–1378 task/sensor attack 与 clean recovery；Ch66 285–313 评价对象身份。normal/contradictory instruction 分测已承载，LGS 敏感不是识别矛盾或安全 abstain。 |
| 2603.06048 GenHOI | 暂缓 / MULTIMODAL-GENERATIVE-PARADIGMS | Ch14 132 binary multiply mask 不等−∞可见性、Ch24 79–81 区域编辑/decoder验收；中心 hard isolation 与 Eq8/9 冲突隔离，RoPE 非一般单调。需作者真实 mask/公式原件，窄 gating recipe 仅报告。 |
| 2603.06136 RMD | 已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS | Ch24 939–1028 跨 resolution draft/semantic lock、1125–1345 noise/parameterization/solver/codec身份。logSNR state 切换分责已承载；fake score recipe、threshold 冲突与 teacher 费用仅报告，不授 full distribution match。 |
| 2603.06331 WorldCache | 已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS | Ch24 1350–1440 FULL anchor/每chunk phase/累计displacement/proxy触发refresh、identity与全部费用。分组近似 proxy 非观测误差/物理曲率，scale条件与缺hard cap仅报告。 |
| 2603.06408 PSIVG | 已有覆盖 / MULTIMODAL-WORLD-MODELS | Ch25 1185–1223 Reason/Execute/Render 不同状态、1266–1272 veracity/influence/克制三证据；Ch26 882–965真实控制。simulator 合法/偏好非世界真值，hybridflow/TTCO recipe 留报告。 |
| 2603.06445 WanderDream | 已有覆盖 / MULTIMODAL-WORLD-MODELS | Ch25 1185–1223 visual proxy非世界真值、1266–1272 状态真实性与下游决策效果分测。合成路径/GPT QA/real observation 相位只有限评价人口，不能将可视化认作真实可执行状态。 |
| 2603.06480 VLN prune | 已有覆盖 / MULTIMODAL-EMBODIED-VLA | Ch23 518–546 selector/proxy/原token/预算分责；Ch26 725–815全loop费用和action identity。salience×novelty/history MMR recipe 与 joint 反侧仅报告；OS≠STOP success、生成4-action latency非控制Hz。 |
| 2603.06577 Omni | 已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS | Ch24 1020–1125 typed unified路径不删codec、1778–1792 PAD/EOS/length与commit分责。tail mask/logit熵软位置/initial length是局部recipe，不授同codec或硬顺序/无损加速。 |
| 2603.05744 CodeScout | 已有覆盖 / AGENT-CONTEXT | Ch75 70–109 dependency事实/AST-symbol派生view/assembly 与独立生成提示，244–282 prep+target费用；Ch81 1091–1098 exact code verifier。issueaugmentation只派生提案，scope/filter/newrunner identity不能当实际reproduction；局部独立prep优于trajectory内增强不普遍化。 |
| 2603.05909 InfoGatherer | 已有覆盖 / AGENT-PLANNING | Ch79 297–310 calibrated prior/expected info gain→ask/explore/cost/fallback。BBA ignorance/discord recipe未成事实概率，representation+fallback联合改变不授DS唯一收益；root实际必要Source/PRE独核通过。 |
| 2603.05910 ProEvolve | 已有覆盖 / AGENT-WORKFLOW | Ch81 177–209 template/runtime graph/trace，931–967 synthetic环境先验结构/语义/可行性与test版本；1091–1098 verifier identity。coverage≠pass、环境/任务共变与memory反退仅报告；root实际必要Source/PRE独核通过。 |
| 2603.05912 DeepFact | 已有覆盖 / PLATFORM-EVALUATION-SYSTEM | Ch66 1534–1538 trace反例→owner裁定→固定version及修前后重跑，865–892 typed verifier/聚合可重算；采用纠错权限/同版本重评分已有覆盖。hiddenmicrogold/5%再校准具体recipe仅报告，posthoc一致非accuracy；root实际必要Source/PRE独核通过。 |
| 2603.06064 Interactive PDDL | 已有覆盖 / AGENT-PLANNING | Ch79 191–230 symbolic executor合法不等终局计划、368–388 milestone与完整checker；Ch81 931–955 deterministic state测试与model success分测。真实sim observation不等goal-distance，有限65→68/5.7×token负面留报告，不授所有Agent失效。 |
| 2603.06444 Streaming TTS | 已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS | Ch24 712–727 有限lookahead chunk renderer/码层vs时间帧、首包费用、RTF≠SLO与播放不可rollback；marker/reset具体训练配方仅报告，ahead等待另计，不授全部状态O(k+f)。 |
| 2603.06453 Canvas | 已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS | Ch24 79–81 local改写不能保未mask区、171 nonlinearcodec mask leakage、1163–1176独立decoder/输出验收。原图/生成region/最终像素分别验收，双回贴/VAEharmonization与qualityfilter工业recipe仅报告，segmentation非全identity保证。 |
| 2603.05828 HART | 已有覆盖 / AGENT-RAG | Ch76 496–500 crossencoder ranking、581–613 relevance/sufficiency/claim-support三层及人工anchor；span/context/MQ/rerank有限诊断保留。equivalence cosine hit非entailment/真实内因；root实际必要Source/PRE独核通过。 |

## 状态

作者已完成上述48项实际 PRE 读取，全部必要Source/PRE采用界限经root及review_mar10_remaining独核确认；四项实际整合及非写入者 POST 已通过。候选侧普通可执行0，仅本六部分root非作者DAY未验收，报告保持进行中，不改名成外部 hold。实际来源/证据与48项最终Books处置已逐项同步六部分日报。未 stage、commit、push，未写共享 Books/索引/学习状态。
