# May07 作者整改 — 2026-09-14

状态：作者侧工作完成，等待 root Books 写回和新的非作者验收。`/root/may06_independent_review` 已转为作者，先前独立审计仅是封存的问题清单；本轮不构成新的非作者验收。

## 作者侧收尾

此前 34 项 pending 已全部取得 exact-v1 并完成定点 Source Review。经全文 scope recheck，28 项保留，6 项改判为 family-specific pre-denominator closure：2605.04911（通用 tabular synthesis）、2605.04932（传统 frozen predictor drift bound）、2605.04946（BatchNorm/CPA geometry）、2605.05084（图像 UDA data ordering）、2605.05123（通用 offline-to-online RL）、2605.05151（time-series Transformer superposition）。这些改判保留已读证据和具体范围理由，不以降分、blocked 或静默删除清零。

当前作者侧账本为 **548 = 137 retained + 410 closure + 1 withdrawn**；Evidence 为 **133 complete + 4 disputed + 0 pending**。Books comparison 已逐项完成，产生 8 项新增/修订与 1 项错误来源删除的 root 写回队列。作者未改共享 Books，也未自任非作者 final reviewer；日报仍保持进行中。

## 范围与冻结

依据原 548 identity 收据，复用未变化的日期/身份资料；对独立审计的 17 项重开和 11 项准入重审逐项读题摘，28 项均发现具体机制/受限反证。按同一错误关闭理由扩查 44 个完整题摘，40 项保留、4 项具体关闭。另原候选 04264、04698、05092 撤销准入。此次冻结的工作分母为 **548 = 143 候选 + 404 关闭 + 1 withdrawn**。这是作者题摘判断，不是 143 项证据完成；若后续发现真实误收按证据改判，不按篇数或保留率修池。

选择的 44 项来自审计发现的错误理由高风险簇，不是随机抽样，40/44 不能外推到其余 closures。未被重新阅读的关闭记录保留原理由并标明 legacy pending independent sampling；不能声称本轮重读全部 548 摘要。原审计曾扫描全部 469 关闭标题并完整抽查 36 项，本轮复用其中明确结果；本轮扩查不要求非候选全文。

## 重开及扩查准入

每项先连通旧约束→实际机制/反证→具体选择，再独立评分；下面是题摘准入，不冒充 Method/Evaluation/Limitation 原文审阅。所有新项在完成定点 exact-v1 之前保持待审阅。

| suffix | owner | D+R+U | 准入理由 |
| --- | --- | --- | --- |
| 04059 | `TRAIN-SFT` | 2+1+2=5 | 连续蒸馏时旧 teacher 不再可访问；外部无标签数据保留其 logits，分离新知识迁移与旧知识遗忘，因此需要比较仅当前 teacher 蒸馏和保留旧响应的取舍。 |
| 04062 | `INFER-TENSORRT-LLM` | 2+2+2=6 | 低于 4-bit 压缩受质量/重训代价约束；混合精度结构量化、层自适应特征蒸馏和熵调 KL 联合提供新的低比特执行分支，需对齐硬件与训练预算。 |
| 04065 | `TRAIN-GRPO` | 2+1+2=5 | 无监督推理不能固定奖励/探索分配；FER 的自由能信号与 AAS 的 advantage 统计调整提供新的训练信号控制分支，须核查是否超出已有熵奖励。 |
| 04066 | `TRAIN-GRPO` | 2+1+2=5 | 固定 policy 聚合/clip 不随训练能力变化；power-mean 目标在算术/几何均值间切换并反馈调 clip，改变 RLVR 更新控制。 |
| 04078 | `TRAIN-SFT` | 2+1+2=5 | 固定模仿 teacher 路径会忽略 student 当前状态；同一 prefix 下比较两者下一步 validity 再分配蒸馏强度，改变逐步监督的选择。 |
| 04091 | `TRAIN-DISTRIBUTED-TRAINING` | 2+2+2=6 | 无可信根的异构联邦学习不能依赖固定可信聚合者；折扣 Beta reputation 联合客户端选择、RepFedAvg 与 BFT，需核查 Byzantine/Sybil 假设下的训练信任边界。 |
| 04100 | `TRAIN-RLHF` | 3+1+2=6 | 直接中心化 emphatic TD 可能破坏关键矩阵正定性；仅正则辅助变量的修复改变稳定算法构造，结论限该线性 TD 设定而非所有 RL。 |
| 04115 | `MODEL-TRANSFORMER-LAYER` | 2+1+2=5 | 相同已实现函数不意味着相同后续学习动力学；低秩 RNN 中 loss-invisible 状态承载训练历史，改变仅由当前 loss/输出判断可塑性的解释。 |
| 04180 | `PLATFORM-EVALUATION-SYSTEM` | 3+1+2=6 | 真假文本来自不同作者会把风格线索混入 factuality 评价；v1 将真答案同样改写为 LLM 风格并约束伪造局部改词，观察 detector 随风格/结构对齐退化，要求用配对风格控制检验事实检测能力。 |
| 04217 | `MODEL-POSITION-ENCODING` | 2+1+2=5 | RoPE phase 与 ALiBi 距离通道不能表示所有耦合；Jordan block 生成距离调制 phase，且稳定 shear 破坏群律，改变位置基函数与数值稳定的取舍。 |
| 04230 | `TRAIN-PRETRAINING` | 2+2+2=6 | 结构化 preconditioner 提早丢弃跨层几何；dense quadratic step 的 layerwise LQR 等价式给出参考，再学习可复用的近似逆，改变二阶优化近似评价。 |
| 04243 | `PLATFORM-EVALUATION-SYSTEM` | 3+1+2=6 | 端到端 temporal QA 失败不能直接归因推理；事件表示提取与给定图上的推理隔离，改变推理能力测量与神经/符号模块分工。 |
| 04251 | `PLATFORM-EVALUATION-SYSTEM` | 3+1+2=6 | 漏洞补丁通过 oracle 不等于修复根因；动态定位多样化、加权证据排名与 root-cause 评价改变 repair 验收目标。 |
| 04305 | `PLATFORM-SECURITY` | 2+2+2=6 | token-level watermark 在改写下易失效；AMR 语义结构嵌入及 parser 检测提供不同 provenance 机制，需核查语义保持与解析误差。 |
| 04308 | `MODEL-EMBEDDING` | 2+1+2=5 | 新知识通常靠权重更新并承担遗忘；Markov token 状态扩展与 token-to-dictionary embedding tuning 给出保留旧转移的条件，需限定模型化假设而非承诺真实 LLM 零遗忘。 |
| 04330 | `MODEL-SELF-ATTENTION` | 3+1+2=6 | 隐式推理的规模泛化不等于深度泛化；Horn-clause 受控任务分离图宽度/拓扑与深度外推，改变何时需要显式 CoT 的判断。 |
| 04344 | `MODEL-SAMPLING` | 2+1+2=5 | 精确前缀条件预测受经验支持域限制；先扰动到语义邻居的 pre/post additive-noise 模型给出外推条件，改变采样/输入扰动的适用解释。 |
| 04363 | `PLATFORM-EVALUATION-SYSTEM` | 3+1+2=6 | tabular ICL 受 context 类别先验偏移影响；test-time posterior/prior rescaling 无需重训，改变 label-shift 校准选择。 |
| 04373 | `MULTIMODAL-EMBODIED-VLA` | 2+2+2=6 | 平均任务奖励不保证最坏情形 runtime 安全；bilevel regret 搜索反例再编译 counterfactual 干预规则，改变保护层如何从失败样本构造。 |
| 04421 | `MODEL-SELF-ATTENTION` | 2+1+2=5 | 离散 attention 与连续 RNN 的组合缺少统一状态解释；attention-logit ODE 及门控极限连接 SDPA/CT-RNN，提供可核验的 sink 控制设计分支。 |
| 04426 | `AGENT-CONTEXT` | 2+1+2=5 | 固定比率 token 删除会丢关系；原子事实行与符号语义重写同时形成压缩和寻址索引，改变压缩单位而非仅换摘要 prompt。 |
| 04461 | `MULTIMODAL-GENERATIVE-PARADIGMS` | 2+2+2=6 | 整段视频 TTS 候选探索昂贵且缺 temporal guidance；chunk noise 继承、跨窗 reward pruning 与奖励驱动被逐出 KV 的更新路径，提供 streaming 特有的质量/状态成本选择。 |
| 04467 | `INFER-TENSORRT-LLM` | 2+1+2=5 | Nsight 指标多不等于可操作瓶颈解释；由 profile 数据约束 agent 解释并测下游优化效果，需核其新增证据反馈能否改变 kernel 优化循环。 |
| 04494 | `TRAIN-DPO` | 2+1+2=5 | BT 标量偏好不能表达一般扩散偏好；self-play Nash 目标替代 reward-induced preference，改变 diffusion alignment 的目标建模。 |
| 04495 | `AGENT-RAG` | 2+2+2=6 | 文档相关性不等于生成器有用性；query-only 稳定性为 control 估计 passage 边际影响，再最小 Kendall 修正排名，改变检索/生成衔接且不把稳定性当正确率。 |
| 04507 | `PLATFORM-EVALUATION-SYSTEM` | 3+1+2=6 | 可校准 belief 文本不等于因果 belief-conditioned action；Bayesian teacher 蒸馏与 posterior-prefix 干预分离报告和控制，改变 agent 可解释性验收。 |
| 04515 | `MULTIMODAL-WORLD-MODELS` | 3+1+2=6 | 视频物理错误可能混入生成 artifacts 或常识先验；物理程序生成对抗课程分离视觉事实与叙事先验，改变物理 reasoning 评价和监督。 |
| 04530 | `AGENT-WORKFLOW` | 2+1+2=5 | 自由 ReAct 混合收集证据与承诺根因；phase-gated escalation 在同 backend 对照下提高诊断，改变工具诊断 workflow 的可行性判断。 |
| 04539 | `TRAIN-DPO` | 3+1+2=6 | 偏好胜率会奖励冗长而不保证 entailment；NLI/verifier 混合信号及相反 judge 排序改变知识生成的偏好目标和评价。 |
| 04542 | `MODEL-SAMPLING` | 3+1+2=6 | 逐 token power sampling 不等于序列分布幂变换；后缀信息与 true-reward/self-reward 协方差决定收益，改变温度自奖励的理论解释。 |
| 04617 | `TRAIN-SFT` | 2+1+2=5 | 把 vision TTA 平滑直接套流式传感会错过状态转换；feature surprise 按 prototype 几何决定惯性保持/释放，提供无反传在线适配机制，适用范围限 WHAR。 |
| 04651 | `TRAIN-SFT` | 2+2+2=6 | 新例子适配通常支付反传或长 context 成本；单遍把带标签例子编译进 fast weights，提供冻结表征下不同训练/推理成本分配。 |
| 04683 | `MODEL-SELF-ATTENTION` | 2+1+2=5 | attention 计算能力不能只用通用逼近描述；average hard attention 与特定 arithmetic-circuit 家族的双向模拟界定其表示能力，须保留替代 FFN 等假设。 |
| 04712 | `MODEL-MOE` | 2+1+2=5 | 增加专家不保证持续 RL 可塑性；expert feature 的谱 proxy 与 Parseval penalty 针对 spectral plasticity loss，改变 MoE 正则选择。 |
| 04727 | `PLATFORM-EVALUATION-SYSTEM` | 3+1+2=6 | attention-enhanced 模型优势可能来自序列时间泄漏和设置差异；时间排序/固定跨折超参后差距缩小，改变 sequential learner 比较的有效性条件。 |
| 04738 | `INFER-TENSORRT-LLM` | 2+1+2=5 | 激活/权重 outlier 不必总靠在线 rotation/scaling；Hessian 稳定零空间的 additive suppression 可离线吸收，改变低比特量化的执行负担。 |
| 04747 | `TRAIN-DISTRIBUTED-TRAINING` | 2+2+2=6 | FL 客户贡献奖励通常依赖公开 test/标签；categorical reports 与 honest majority 下的 KFCA 修复 label-flipping 激励，提供不同信任假设。 |
| 04754 | `INFER-TENSORRT-LLM` | 3+1+2=6 | 近似乘法器稳健性不能从 CNN 推到 ViT 或 dense 推到 MoE；架构与重训条件下的排序反转改变硬件近似的质量验收。 |
| 04763 | `AGENT-RAG` | 3+1+2=6 | 语法函数边界并非默认最佳 code chunk；864 受控设置中 function chunking 不占 Pareto 前沿，改变 chunking 与 context budget 的联合选择。 |
| 04764 | `PLATFORM-EVALUATION-SYSTEM` | 3+1+2=6 | LLM surrogate 的 prompt/逐点或联合查询不是格式细节；不确定性对齐与 downstream regret 受协议改变，要求把 elicitation 计入 surrogate 定义。 |
| 04830 | `MULTIMODAL-GENERATIVE-PARADIGMS` | 2+1+2=5 | 局部 denoising 可用性与语义分岔常被分开分析；DiT 中两个 critical time 接近提供何时需要 conditioning/global compute 的诊断。 |
| 04911 | `TRAIN-DATA` | 2+1+2=5 | 小数据按集拟合会混淆泛化结构与记忆；跨数据预训练的 tabular ICL 改变质量/隐私经验取舍，不能外推 DP 保证或声称完全无记忆。 |
| 04920 | `TRAIN-GRPO` | 2+1+2=5 | token-level 模仿可能偏重训练组合；outcome RL 与 binary/composite reward 对照检验组合泛化，改变 SFT/RL 的目标选择边界。 |
| 04946 | `MODEL-TRANSFORMER-LAYER` | 2+1+2=5 | BN 不只是优化重参数化；训练批条件下切换超平面移到质心并改变区域划分，提供 batch-dependent realized function 的解释而非推理期同一函数保证。 |
| 04952 | `MODEL-MOE` | 2+2+2=6 | 细粒度 MoE 的全专家打分会抵消稀疏计算收益；VQ shortlist 后做受限精确 router，改变路由精度与执行成本边界。 |
| 04957 | `PLATFORM-EVALUATION-SYSTEM` | 2+1+2=5 | 图耦合会破坏普通 conformal 的 exchangeability；条件高频谱分解提供不同校准机制，需把交通图结果限定为图预测而非通用 LLM coverage。 |
| 04970 | `TRAIN-SFT` | 2+1+2=5 | 独立技能适配常需改权重或堆 context；冻结模型的 soft-vocabulary skill tokens 可单独训练再组合，改变技能更新与组合的参数界面。 |
| 04971 | `MODEL-TRANSFORMER-LAYER` | 3+1+2=6 | 跨层几何连续性不能仅归于非线性；保旋转非线性反例分离 residual 梯度相干与对称破缺，改变 activation/norm 角色解释。 |
| 04972 | `PLATFORM-EVALUATION-SYSTEM` | 2+1+2=5 | 显式专家 criteria 未必能稳定提升对齐；专家/样本身份/评价维度的受限证据挑战只增加 rubric 的策略，需区分主观异质性与模型错误。 |
| 04995 | `AGENT-PLANNING` | 2+1+2=5 | 自适应查询优势不必在实现约束后保留；ReLU realizability 下四类构造分离 adaptive querying 与表示能力，改变 agent 学习理论解释。 |
| 05009 | `TRAIN-DISTRIBUTED-TRAINING` | 2+2+2=6 | 异构分散模型不能默认互相可信；同一验证 trust gate 同时控制辅助蒸馏与部署 ensemble，改变训练和推理共享信任信号的设计。 |
| 05025 | `PLATFORM-EVALUATION-SYSTEM` | 2+1+2=5 | 采样一致性 UQ 有多次 decode 成本；attention 对均匀分布的 KL probe 提供单 pass 替代，需与低成本首 token/语义梯度 sensor 同协议比较。 |
| 05026 | `MULTIMODAL-GENERATIVE-PARADIGMS` | 2+1+2=5 | 扩散结构幻觉不仅可用 mode interpolation 解释；局部内在维数与 IQ 抑制提供另一诊断/纠正分支，需区分机制证据和下游医学类比。 |
| 05040 | `TRAIN-SFT` | 2+1+2=5 | self-distillation 不必只匹配自身原分布；reward 重加权 teacher 给出目标与最优性条件，改变何时应选择外部 teacher 或 self-teacher。 |
| 05045 | `MULTIMODAL-REPRESENTATION` | 3+1+2=6 | 视觉识别对旋转/噪声稳健不代表关系判断稳健；关系幻觉的分离对照及部分有效预处理改变 VLM robustness 评价。 |
| 05084 | `TRAIN-DATA` | 2+1+2=5 | mini-batch discrepancy 估计方差不只由 batch 大小决定；对 CORAL/MMD 优化采样顺序的无偏降方差机制，改变 domain adaptation 数据组织。 |
| 05103 | `PLATFORM-EVALUATION-SYSTEM` | 2+1+2=5 | groundedness sensor 不必二次生成或读内部状态；语料句间 embedding delta 的局部 Gaussian field 给出可追溯偏离信号，不把语料偏离等同事实错误。 |
| 05113 | `MODEL-LONG-CONTEXT` | 3+1+3=7 | 长递推不能无条件套无限宽初始化；线性复高斯状态在 t≈sqrt(n) 出现有限宽边界，改变长程稳定性解释。 |
| 05115 | `MODEL-SELF-ATTENTION` | 3+1+2=6 | 线性 activation steering 可能离开自然行为流形；双向几何干预比较显示路径形状重要，改变内部控制从方向到几何轨迹的选择。 |
| 05123 | `TRAIN-RLHF` | 2+2+2=6 | offline-to-online 先选一条 policy 再微调可能浪费交互预算；UCB 联合选择和 fine-tune 分配允许换候选，改变评估与学习预算划分。 |
| 05134 | `PLATFORM-EVALUATION-SYSTEM` | 2+1+2=5 | 黑盒幻觉检测通常需要多采样或外部 grounding；两种 regime 的 Koopman transition residual 加阈值校准提供单样本替代，必须检查训练标签和域迁移。 |
| 05138 | `MULTIMODAL-WORLD-MODELS` | 2+2+2=6 | 纯文本计划不易反证 world model；可执行 Python model 由历史观测 verifier 约束再规划，同时关闭 harness 泄漏渠道，改变模型校验与动作执行关系。 |
| 05151 | `MODEL-TRANSFORMER-LAYER` | 3+1+2=6 | 时间序列 Transformer 的竞争力不能直接套 NLP superposition 解释；SAE 扩维及因果干预未见强 superposition 必要性，改变表征机制外推边界。 |
| 05166 | `PLATFORM-EVALUATION-SYSTEM` | 3+1+2=6 | 多次生成语义一致性未必比单 decode 更有价值；首个内容 token 的 top-k entropy 在受控 QA 达到相当检测，改变 UQ 成本基线。 |
| 05176 | `MODEL-SELF-ATTENTION` | 2+1+2=5 | 线性 ICL 理论不足解释 nonlinear regression；attention 构造多项式/spline 特征并给 context/training size 误差界，补充 attention 作为 featurizer 的机制解释。 |
| 05189 | `MODEL-LONG-CONTEXT` | 3+1+3=7 | 线性记忆容量不能只数 d² 参数；top-1 retrieval 有 log n 极值代价，而 top-k/TAM 改变阈值，明确容量必须绑定读取判据。 |
| 05204 | `TRAIN-SFT` | 2+2+2=6 | 普通 SFT 会损伤少步扩散能力；同模型 teacher 额外读目标图像、student 在自身 rollout 上蒸馏，改变保留 few-step 能力的连续适配路径。 |
| 05206 | `MULTIMODAL-GENERATIVE-PARADIGMS` | 3+1+2=6 | 简单屏蔽 DiT 高 norm token 并不能修复语义损伤；encoder 与 denoiser 双 register 分治提供不同 outlier 处理机制。 |

## 明确关闭与反转

| suffix | 当前判断 |
| --- | --- |
| 04565 | 卫星遥感卸载把现成 MARL 与在线二分应用于 LEO 路由；摘要未分离新的模型/Infra 主线机制或对既有策略的重要反证，服务延迟降幅本身不足准入。 |
| 04899 | embedding 几何曲率与棋盘表示关联提供局部解释观察，但摘要未给出可改变模型设计/评价的可识别机制边界；不把几何类比直接写入主线。 |
| 04965 | 一般 OT ground metric 由位移二阶矩改形，尚未建立与本书大模型主线需改变的具体判断的直接关系；并非论文没有方法。 |
| 05193 | 数学不等式发现由 Grok 协助，但贡献对象为数学结果，不是模型或基础设施机制；按当前 AI for Science 暂缓关闭。 |
| 04264 | 观点/设计议程在单一协作生态描述 governance/provenance，未提供超出既有记忆治理原则的机制或决定性反证；不把 state owner 措辞当新贡献。 |
| 04698 | LightGBM 恶意软件 IAT/section 特征 poisoning 的局部摄取案例未支持 LLM delayed-lineage/revocation 机制，原采用命题由作者添加；撤销整合并关闭，不否定该安全研究的领域价值。 |
| 05092 | AIDE 驾驶舱状态任务组合双流 temporal gate，题摘未给出可迁移的 world-model 机制边界或重要反证；通用 world-state 治理为越界外推，撤销整合。 |

原 04098 与 04842 维持关闭，但理由分别限定临床域外部验证与未连通 AI workload 的通用 DPU 通信，不再写无反证/无机制。04100 的 None 与 04373 正向理由配 closure 已修正。

## 证据整改原则与剩余工作

旧自动抽取的第一条 Method/Evaluation/Conclusion snippet 已被独立审计证实不能证明读懂。旧证据保留为历史提取，不覆盖真实已读段落；纠错只在核查正文后写入，不用同一模板补齐。04209 采用命题改为 Sparse-PCA 硬度下相对 Gaussian-dithered clean 参考的计算不可区分；05097 改为每条 edge 的 fast/slow 耦合，13-document 动力学例子不支持 retrieval 效果或 competitive 优势。

机构 Daily 来源需要重新核查可验证的当窗资料；旧 checked 字段不构成本轮新检查。当前机构覆盖不据零候选自动关闭。

## Books 协调

不直接修改共享 Books。Root 已删除 Ch54/04450、Ch72/04698、Ch25/05092 的不当专属段；Ch29/04468 已改为 current+frozen SFT reference 构造 dynamic anchor、inner distillation，与 reference 替换/全局 retention 保证分开。旧 35/35 queue 和当前 51 Integrate 不是本轮产出数字；逐项真实锚点/边界见后续统一映射，缺项保持未决。

## exact-v1 版本污染纠正

2605.04180 的 raw title/abstract 实为 2026-08-27 v2。原始收据与 abstract 不改；活动账本保留 revision-only provenance，按 [v1 history](https://arxiv.org/abs/2605.04180v1) 更正题名及采用命题为“配对作者风格控制”，并重新读 §3.1–3.2 / §4.1–4.3。删除本窗采用的 gold/wrong/no evidence 结果与 retrieval-confidence gate；这些是后续版本，不得倒灌。已下载候选 HTML 的 document-title 比对除署名脚注外未再发现题名差异；题名一致不证明摘要/正文未改，仍须逐项 exact-v1 审阅。
