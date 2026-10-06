# Nov18 Finite Screening

作者Carver，初筛2026-10-04T20:13:46+08:00，root反馈同步2026-10-04T20:53:35+08:00。本日fresh原响应；只实际题摘，不继承17候选/响应/关闭。首批见[FIRST_CALIBRATION_READY](FIRST_CALIBRATION_READY.md)，root已实际35完整v1AB（10876/10909多段另补全），非作者日级尚未结束。

## 入口和停止

[collect.py](collect.py)四窄主题分别model（CL/LG，language model/Transformer/MoE）、systems（DC/AR/PL/OS/PF，LLM/GPU/kernel）、agents（AI/IR/MA，tool/memory/context+LLM）、multimodal（CV/RO，foundation/world/VLM）。`submittedDate:[202511131900 TO 202511141859]`仅作惯常Sunday公告邻域的发现范围，不是公开窗口证明。每查询start0/max50：21、9、1、13，均短页停止；44返回去重41身份。原API有后来版本摘要，贡献判断改读exact-v1原页。

[cs.DC目标相关标题补检](arxiv-csDC-target-titles.html)实际skip50/show50，50标题；宽月总数338只定位查漏，不是338题摘/全文队列。相关FengHuang/HPCAgentTester已在主题命中，无新增身份；未扩大一般分布式算法。方法和路径receipt保存真实查询/执行时间。

41身份：35完整题摘实际读完（原页全部200，有对应receipt），6明确领域标题关闭。原25potential/10AB拟关闭；root纠正Conformal评价盲区的误范围关闭后为26论文potential/边界待校准、9具体增量/范围拟关闭。potential不是确定当窗候选，尚未评分/全实验审阅/owner对读；不以它们支持Books或召回保证。35原事件页轻量withdrawn/retracted/erratum/corrigendum检查无命中，不称遍历版本史或附件。

## 26篇完整题摘potential

每行原页`abs-<ID>v1.html`、官方`https://arxiv.org/abs/<ID>v1`；全部精确v1。具体日期见[DATE_REVIEW](DATE_REVIEW.md)。表述是待验证命题，不是实验已成立。

| ID / 原题名 | 旧约束 → 原文具体增量 → 需要重考虑的选择；未授边界 |
| --- | --- |
| 2511.11553 Multistability of Self-Attention Dynamics in Transformers | 单一principal-eigenvector收敛直觉 → 连续时间attention/Oja多种稳定状态 → 动力学解释须带假设。root实际§1/2/Assumption1：固定QKV、unit sphere、time=layer/infinite-depth，V symmetric positive且simple largest eigenvalue；仅此ODE，非训练或一般Transformer等价。 |
| 2511.11518 W2S-AlignTree | 训练对齐成本/推理控制不足 → weak step-level proxy+entropy-aware MCTS指导strong生成 → inference-time控制取舍；不采用摘要分数或普适weak-to-strong结论。 |
| 2511.11505 FarSkip-Collective | MoE依赖阻塞通信 → skip连接改变依赖并self-distill恢复能力，再实际compute/comm overlap → 模型结构与调度共同优化；非只NCCL替换/无损保证。 |
| 2511.11500 Honesty over Accuracy | prompt警告不能带来abstention → ternary RLVR惩罚形成risk frontier，abstention作cascading协调信号 → 训练风险目标与推理选择；不授医疗安全或普遍校准。 |
| 2511.11315 LAET | 全层适配成本 → hidden-state分析选择有效层、冻结其余 → layerwise fine-tuning资源选择；实验为金融任务，不以金融指标自动收，具体选择机制值得有限核验。 |
| 2511.11018 Automata-Based Steering | 结构合法不等多样 → traversal history引导新结构 → constrained decoding diversity选择；奖项不作证据，非通用测试充分性。 |
| 2511.11007 VisMem | 长生成丢视觉grounding → short perceptual/long semantic latent memory动态调用 → VLM表示保留方式；认知类比和摘要11.8%不直接采用。 |
| 2511.10881 Negative Bias | 将no偏置仅归因attention heads → format-level/knowledge-shortcut，CoT可能放大、context/IDK减少 → 提示/评估控制变量；局部反侧不授所有模型。 |
| 2511.10899 From Proof to Program | 工具执行正确被当推理改善 → TIM过程退化与结果accuracy分离 → tool evidence需看过程；数学是学习/推理反侧，不是science应用。 |
| 2511.10819 LLM-as-a-Grader | correlation被当评分一致 → GPT4o局部约0.98相关仍仅55%exact agreement且开放技术响应可变 → evaluator验证协议；教育场景是局部测量，不自动外推或因场景关闭。 |
| 2511.10811 Transformers know more than they can tell | arithmetic失败被统称hallucination → Collatz表示进制、modulo类学习与loop长度错误分离 → 能力形成/控制结构解释；不是证明Collatz或通用LLM算法。 |
| 2511.11526 Bridging Hidden States | early/pooled late fusion/decoder绑定 → encoder上层cross-only双向attention+gated residual，理解/生成解耦 → 融合位置取舍；未核效率/对照条件。 |
| 2511.11520 Scalable Policy Evaluation with Video World Models | 真实机器人policy评估昂贵 → pretrained视频action conditioning作learned evaluator，比较policy rank/value及常见失败 → world-model验收选择；simulated evaluator非真实安全认证。 |
| 2511.11502 PAS | VLM依输出历史而丢图像依赖 → conditional information分析与prelim attention score无需额外forward → 在线hallucination测量选择；不授attention因果或通用过滤保证。 |
| 2511.11313 DocSLM | 长文档memory受限 → hierarchical multimodal compressor+streaming abstention/entropy calibration → sequential memory/回答取舍；非无限长度无损、实际edge部署已验证。 |
| 2511.11298 VLA Benchmarking Experiences | 单一success排行不足 → ID/OOD/language、success/time/cost与具体失败对照 → VLA适用边界；仅四模型/四任务不授全机器人结论。 |
| 2511.11011 LS-NWM | pixel预测成本高 → latent action-conditioned transition与multi-frame AR planning → world model状态表示选择；447x等须控制实际预算。 |
| 2511.10946 Abstract 3D Perception | 2D输入不足3D retrieval → abstract boxes/multiview proxy/voting/3D-aware reasoning → 几何表示选择；非物理正确/无需任何3D先验。 |
| 2511.11332 UFO3 | 单设备workflow脆弱 → mutable distributed DAG、显式控制/数据依赖、async更新和fault injection → 跨设备执行恢复约束；不授所有失败/安全/性能保证。 |
| 2511.11248 T-MAN | NPU非GEMM/dequant瓶颈 → fused两级lookup、unified layout/tiling、prefill pipeline/vector decode → low-bit execution选择；配置收益需core，非全NPU。 |
| 2601.08833 Revisiting Disaggregated LLM Serving | PD被认为performance/energy总更好 → load/transfer medium与DVFS Pareto反侧 → stage分离应带成本条件；January arxiv first-announcement排除November，别处first public仍未知。 |
| 2511.10909 MMA-Sim | floating-point MMA规格未披露 → targeted/random test推导bit-accurate行为，未文档化误差 → 数值复现/硬件契约；实际v1标题MMA-Sim，不用后来题名/验证扩张。 |
| 2511.10753 FengHuang | 本地HBM需求 → local/remote共享内存、active paging/near-memoryops → memory/compute放置；vision+initial simulations非实机。 |
| 2511.13751 Inside VOLT | late inversion/predicate reload/divergent select破坏split/join → IR planning加last MIR safety net → SIMT控制流降级的具体正确性机制。root实际§4.3支持potential；§5.2 psort instruction增多、ZiCond请求密度变慢条件保留，不授普遍性能或production保证。 |
| 2511.10860 HPCAgentTester | 易错parallel-pattern难转执行test → HPCBugKG到AST pattern、recipe再execution critique → 并行约束驱动测试反馈的具体机制，root实际§4.1.1支持potential。§3.2 Listing3 ASSERT_FALSE/is_consistent与caption矛盾；§5.2多模型+5迭代预算，Table3不是同模型公平提升保证，不授oracle可靠/复现。 |
| 2511.11472 Quantifying and Improving Adaptivity in Conformal Prediction through Input Transformations | 不均衡difficulty bins使coverage violation/平均set size估计失真 → input transformations排序后uniform-mass分箱、两项adaptivity指标及group-conditional阈值 → 不确定性评价及预测集合构建需控制分箱质量。root实际§3及Limitation，TSS受base accuracy/ground-truth rank饱和影响；旧范围关闭撤销，不采医学效果或无条件coverage保证。 |

## 九篇完整题摘拟关闭（日期未核，无需扩日期/全文）

| ID | 完整题摘后的具体理由 |
| --- | --- |
| 2511.10788 Adaptive Reasoning Survey | control-augmented目标形式化及training/inference taxonomy，没有摘要可见新机制条件或直接修正证据；不因综述标签自动关。 |
| 2511.16688 Prompt-Based Value Steering | Wizard-Vicuna对value-conditioned与baseline prompt评分/价值增益方法，结论是prompt可steer；未揭示具体失效边界或新控制机制。不采用safe/trust因果。 |
| 2511.11334 LaoBench | Lao17K样本/三类任务、人审+agent验证及模型普遍困难；未见评价盲区/混杂机制足以修正设计，数据规模/新语言不能单独准入。 |
| 2511.10876 Software monitors | Railway case将LLM instrumentation+既有conformance checking组合，领域知识提高日志覆盖/F1；未见LLM执行或生成机制新边界，不以软件/monitor名称映射owner自动收。 |
| 2511.11510 OpenUS | ultrasound clinical foundation/masking与标签效率目标，领域数据/任务指标；暂缓medical/science应用，不绕通用pretraining节点引入。 |
| 2511.11212 MAFM3 | CT prognosis/segmentation/PET模块扩展并提高临床Dice；领域应用适配，没有独立模型系统机制改变，medical暂缓。 |
| 2511.11445 Action research education | 数学教育learner/teacher对话与digital augmentation理念，非模型学习/系统执行新机制。 |
| 2511.11111 SMART | GNN+LLM预测Dragonfly runtime以替代昂贵PDES，输出为HPC网络仿真预测；未提出foundation-model训练/通信本身机制，不因systems/LLM词收。 |
| 2511.10774 FVMGN | remote-sensing land-cover classification的wavelet/augmentation/特有text与alignment模块及领域generalization指标；未建立主线机制/边界，非通用VLM表征突破。 |

## 六个标题范围关闭

2511.11462 MoCap2Radar（motion capture合成radar signatures）、2511.11402 spacecraft trajectory optimization、2512.00042 standardized exam question数据fine-tuning、2511.10912 HouseMD rare disease diagnosis、2511.10806 image deblurring FFT-ReLU、2511.11311 brainMRI lesion segmentation。标题明确领域应用且当前API事件没有撤回/安全纠错提示；不称完整摘要贡献审阅，也不核与最终处置无关的精确公开时刻。若具体原始反侧/机制证据改变范围判断，仅定点重开。

## 官方公告

[OpenAI Gartner](FIRST_CALIBRATION_READY.md)原RSS落窗、核心已读，拟commercial recognition关闭。其免责声明不支持性能/安全/benchmark事实。

[Antigravity官方](https://antigravity.google/blog/introducing-google-antigravity)的[本日核心](web-date-recovery-last.json)实际读完：task-level artifacts/verification、async Manager与Editor分离、跨surface反馈进入执行、derived knowledge与capacity-correlated limits。现第27个potential（26论文+1公告），只准入线索；未授权效果、算法新颖性或production保障。Nov18日期时区/时刻未知，与截止可能相交，不能用Gemini3同日16Z时刻移植给另一公告。只请求必要日期及具体机制准入校准，不重读现行docs/实现。

## Root独立反馈与局部停点

2026-10-04T20:53:35+08:00同步root独立复核反馈：实际35完整v1AB已读（10876/10909多段单独补全）；11553/10899/10753 potential可保留，13751/10860由root继续窄core判具体增量，作者不重复其工作。11472旧理由过窄已撤销，恢复potential并完成该ID最小原日期恢复，仍public hold，见[DATE](DATE_REVIEW.md)。没有将35AB独立读完称全文Evidence或日级通过；无其他改判时26论文+Antigravity=27potential。

2026-10-04T20:59:22+08:00进一步同步root实际必要core反馈：[11553](root-core-2511.11553v1.html)§1/2/Assumption1、[VOLT](root-core-2511.13751v1.html)§4.3/5.2、[HPCAgent](root-core-2511.10860v1.html)§4.1.1/3.2 Listing3/5.2 Table3、[Conformal](root-core-2511.11472v1.html)§3/Limitation，上表最小条件和直接反侧已同步。13751/10860具体机制潜力可留，普通准入core停点撤去；27potential全部日期仍hold，不授全文Evidence、训练理论等价、oracle可靠或复现/公平性能提升。非作者其余必要反侧、有限来源/日期处置及日级继续。
