# 02/25 末批相关主题线索：日期优先隔离

执行2026-10-05。通过本日inventory相关title命名补检后读完整题摘；沿ROADMAP主线选择训练/表示/attention、RAG/memory/Agent执行验证、多模态生成/worldmodel/VLA、推理precision/cache/kernel/hardware，未把19058～20161号段变成逐项题摘队列。下列仅潜力线索，不是确定本窗候选：原同身份DataCite Registered均晚于2026-02-25T01:00:00Z，Submitted只约束最早可能公开，Updated:v1不能替代dated公开事件。不因来源当前可访问而展开非必要正文、评分或Books；逐项可用dated公告/可信历史snapshot恢复上界时才定点重开。

以下题摘中具体潜力已清楚；仍须日期及证据确认，不能拿此表授正面Evidence或Coverage。

| ID尾号 | 原约束 → 题摘原文增量 → 潜在选择 |
| --- | --- |
| 19058 | modality融合归因不明 → causal amp/SNRF lowrank干预 → 核跨模态神经元机制 |
| 19063 | 3D benchmark缺egopose可使任务不适定 → PoseRecover/Align对照 → 核几何能力评价 |
| 19066 | discrete diffusion inverse gradient不稳 → 唯一objective/stable steps → 核inverse可行假设 |
| 19069 | RL训练问题同任务局限 → 可迁移steppingstone question → 核生成数据的credit |
| 19083 | one-step图像编辑易形变 → low-energy transport → 核低步数/保真取舍 |
| 19084 | GPU通信NUMA归因难 → UCX/MPI细粒度trace → 核allreduce执行测量 |
| 19091 | preference chorus压缩丢目标 → multiobjective嵌入/生成 → 核跨目标表示 |
| 19101 | moral valence与grammar混 → ablation分拆 → 核可观测偏好归因 |
| 19109 | addition routing抽象不明 → rotation/negative control → 核表征与因果功能 |
| 19111 | tail activation全量adapter贵 → eigenspace LoRA → 核rank预算 |
| 19116 | gossip每步通信贵 → local event阈值/收敛 → 核优化通信条件 |
| 19117 | egocentric layout易混 → allocentric symbol bipartition → 核视觉空间解耦 |
| 19127 | RAG hop成功掩链条断裂/过展 → trace自动benchmark → 核证据链盲区 |
| 19128 | kernel search plan/instantiate耦合 → 双层非单调搜索 → 核新执行计划空间 |
| 19140 | affective modal alignment多解 → one-to-many rectflow循环适配 → 核融合目标 |
| 19141 | sycophancy不只hallucination → Bayes-user spirals → 核反馈自强化条件 |
| 19142 | learned optimizer小规模OOD难 → normalized Celo2到1.3B → 核尺度转移 |
| 19143 | sparse attention head互竞争 → cooperative Markov ODE → 核学习动态假设 |
| 19149 | VLM后编辑无局部安全控制 → spatial gate → 核保留/防unsafe编辑 |
| 19157 | persona trait重叠 → contrast SAE facet router → 核表示解耦 |
| 19159 | valence可probe不等于可操控 → distributed-head干预 → 核因果边界 |
| 19160 | formal game答对不能看rule保持 → horizon/obfuscation控制 → 核长程推理评价 |
| 19161 | DiT加速后decoder成为瓶颈 → decoder prune/operator蒸馏 → 核端到端生成成本 |
| 19163 | AV diffusion时空模态冲突 → MS-MoE/RoPE/AV-DPO → 核联合生成对齐 |
| 19169 | LoRA静态子空间受限 → activation-conditioned低秩理论 → 核动态rank表示 |
| 19187 | 固定题库RLVR饱和 → adaptive symbolic problem/verifier loop → 核curriculum |
| 19188 | OCR字符串与position混 → specialist spotting+LLM → 核位置知识边界 |
| 19193 | 固定action primitive限制行为 → visual prompt flow低级primitive → 核行动表示 |
| 19198 | prompt调节离pretrain geometry → manifold约束 → 核迁移条件 |
| 19208 | 各任务同rollout预算 → variance+entropy advantage allocation → 核探索预算 |
| 19215 | unlearning被恢复 → two-layer combinatorial结构 → 核抑制/删除边界 |
| 19218 | schema tool simulation缺状态 → state+completion feedback before execute → 核工具预演权限/验证 |
| 19225 | MoE local routing无任务成功credit → success-gradient modulation → 核语义/专家分配 |
| 19239 | encoded fact但流程仍错 → oracle checkpoint区分gate/binding → 核procedural hallucination |
| 19240 | RAG graph局部cell retrieval → graph cycle结构 → 核检索单位 |
| 19241 | precision影响capacity解释不稳 → signal-dependent/independent理论 → 核有效容量 |
| 19242 | ANN降维混召回硬件 → PCA pHNSW filtering → 核RAG索引质量/成本 |
| 19260 | VLA模拟高成功混控制可靠 → Hanoi neuro-symbolic与π0负侧 → 核能耗/规则 |
| 19261 | NAS图生成局部无效 → topo diffusion双向RL → 核有效架构空间 |
| 19268 | edge低prec向量engine resource约束 → mixedprec CORVET → 核推理compute数据流 |
| 19271 | federation drift一阶处理不足 → second-order geometry preconditioner → 核异构优化 |
| 19274 | feature重要性不等于最小因果单位 → delta debugging保持prediction → 核可解释性验证 |
| 19275 | unlearning破坏retain → nullspace causal tracing → 核target/retain控制 |
| 19276 | multipage code重复组件反馈乱 → reuse+priorityfeedback → 核执行错误定位 |
| 19281 | reasoning预算fixed → MPC/entropy dualcontroller → 核有限推理状态 |
| 19309 | opponent更新成本高 → smooth fictitious play/BoN无weightupdate → 核在线对手模型 |
| 19313 | VLM生成reward数值不稳 → token logprob progress → 核action评价 |
| 19316 | CTC teacher逐步伪标签昂贵 → oneshot target+mixed sampling → 核声音训练预算 |
| 19317 | personalized retrieval static → multistepRL query/evidence → 核memory选择credit |
| 19320 | memory survey只列术语不够 → saturation/judge/backbone/cost实测 → 核评价依赖 |
| 19327 | offpolicy sequence ratio难控 → soft gate sequence importance → 核复用RL轨迹 |
| 19331 | neuron alignment outlier污染 → partial OT → 核对应关系适用条件 |
| 19345 | SAPO gate任意选 → admissible-family性质+controlledQwen → 核policy update |
| 19350 | 2D投影空间歧义 → 3D pose token/camera → 核VLA几何条件 |
| 19355 | active perception时间尺度冲突 → fast disentangled/statistical更新 → 核continual表示 |
| 19357 | context folding混planning与data → MentalBlackboard分拆诊断 → 核状态压缩 |
| 19359 | video2sim参数识别混perception/expression → paired sim-real控制 → 核worldmodel identification |
| 19362 | offline longhorizon400步RL不稳 → optimal-A baseline → 核offpolicy updates |
| 19367 | contrastive多模态可对齐不等于可生成 → geometry/caption density条件 → 核representation损失 |
| 19372 | VLM多path推理成本固定 → critic advantage+confidence exit → 核预算/验证 |
| 19393 | cosine不满足gauge invariance → gauge correction理论 → 核normalization后是否真消除gauge |
| 19396 | safety goal framing易被attack → framing disentangle控制 → 核对抗条件 |
| 19407 | issuehistory多余token → graph+history剪枝零Py → 核代码检索预算 |
| 19416 | RL reward hacking不可定位 → reverse contrast/SAE repair → 核reward恢复 |
| 19418 | shared视觉encoder迁移attack → prototype graybox → 核跨模型安全 |
| 19439 | optimization代码rationale不保证可行 → solver与rational/verified检查对照 → 核执行验证，不采用供应链领域结论 |
| 19449 | encoder更新需全下游重对齐 → fixed-codebook interface适配 → 核稳定表示接口 |
| 19455 | time-series trace RL泛化混 → domain reasoning注入控制 → 核训练数据/目标 |
| 19458 | human/AImodel互补非单准确率 → decision-theoretic reward → 核互补选择 |
| 19461 | pyramid generation重噪低效 → residual parallel MoT → 核noise/并行采样 |
| 19485 | federated expert迁移通信贵 → disjoint expert mobility async → 核状态/通信 |
| 19490 | SQL Agent测试覆盖靠手写 → grammar/logic mutation+repair → 核测试生成执行 |
| 19497 | 单图质量不保证multiimage一致 → checkpoints+attention rebalancing → 核跨图表示 |
| 19505 | prompt视觉控制不稳 → latent visual-token inference energy → 核test-time control |
| 19506 | feature cache复用预算static → magnitude/errorschedule → 核缓存错误控制 |
| 19509 | ensemble越多越好不成立 → imperfect oracle value-of-compute → 核协作预算 |
| 19510 | bilevel datamix短inner horizon混最优 → T=1反例/horizon理论 → 核配比选择 |
| 19512 | diffusion uniform scalarnoise不够 → anisotropic jointtrain/Heun → 核matrixnoise |
| 19514 | Agent仅虚拟行动安全假设 → hirehuman REST/MCP攻击实测 → 核委派物理边界 |
| 19517 | 推理step数不表明correctflow → state-error flow诊断 → 核evaluation |
| 19519 | 全sample lengthreward不稳 → filter与toolthinking selective → 核RL sampling |
| 19526 | SearchR1比较混reward/算法 → avoidance penalty+PPO/REINFORCE → 核检索策略归因 |
| 19530 | CLIP LoRA classprototype冲突 → orthonormal textprototype → 核表示几何 |
| 19533 | grokking任务差异无结构解释 → algebraic factorization控制 → 核能力形成 |
| 19538 | planning lookahead optimismbias → diffusion bias测量 → 核worldmodel规划 |
| 19542 | 3Dedit视角不一致 → view与latentflow interleave → 核执行修正 |
| 19543 | 技能reward缺stability → stable reward设计 → 核skills acquisition |
| 19547 | Agent架构安全与base混 → 同base twoAgent controlledattack → 核协作安全 |
| 19548 | extraction丢结构却看token覆盖 → union extractor/benchmark控制 → 核数据质量 |
| 19549 | docretrieval visualvector内存大 → prune-merge → 核质量/索引容量 |
| 19570 | 全视觉评估昂贵 → cheapconsistency+text discrepancy选择 → 核judge budget |
| 19571 | videoreasoning混recognition/explanation → physicalprotocol预算控制 → 核blindspot |
| 19574 | streamingTTS固定ratio延迟差 → wordinterleave CTC → 核流式质量/延迟 |
| 19575 | concept特征重叠 → target/residual exclusionloss → 核解耦表示 |
| 19578 | active learning generic influence → goal inversecurvature GLM → 核数据选择条件 |
| 19580 | optimizer-state预测不能verified leap → finite-difference criterion → 核训练跨步可行性 |
| 19585 | common/private模态分拆不足 → pairwise tri-subspace → 核representation |
| 19594 | serving优化纯hardtest漏intent → hard+soft54tasks → 核优化Agent评价 |
| 19600 | 一步scoreanchor分布偏 → fixednoise manifold support → 核训练free生成 |
| 19605 | modality shared/private token互扰 → hierarchical约束预算 → 核融合 |
| 19612 | PT/SFT事实不同可忘性 → stage/salience对照 → 核unlearning |
| 19615 | rareobject低先验 → classsynonym/visual enhance controlledhint → 核感知与先验 |
| 19619 | dLLM error混data/model/sampler → HMM oracle隔离unmask错误 → 核步数/长度条件 |
| 19622 | graphcodebook压缩OOD退化 → compressedattention VecFormer → 核表示/成本 |
| 19626 | neuralcompression precision在线修正贵 → high-CDF precision跳bias → 核模型压缩 |
| 19631 | T2I unlearning全UNet污染 → textencoder targetedmisdirection → 核删除位置 |
| 19633 | solver计划不保证feasible → plangraph+constraintdecode反馈 → 核执行验证 |
| 19634 | worldmodel固定step偏occupancy → policy-timescale consistency → 核未来状态 |
| 19643 | KG QA difficulty+abstention混 → dynamicdepth/noise controls → 核拒答评价 |
| 19651 | Bayesian filtering需unroll → composable singlestep denoise → 核score推断 |
| 19672 | endtoendRL routingcollapse → skill competence/cost模型 → 核成本校准路由 |
| 19708 | class/image LoRA分配冲突 → shared/private Dirichlet → 核adapter |
| 19710 | VLA视觉几何与action混 → decoupled3D pose/unitcamera → 核预训练迁移 |
| 19715 | deepfake标签掩judge rationale → visualrationale bootstrap → 核evaluator |
| 19733 | unrolling gradient初始发散 → truncate/warmstart定理 → 核优化条件 |
| 19756 | 数据蒸馏依赖指定架构 → unCLIP prototype → 核训练数据迁移 |
| 19762 | mobileGPU kernel受TCM限制 → MLIR mega-kernel → 核compiler/dataflow |
| 19764 | RGB/depth/force分别训练 → norm/sharedexpert jointaction-env → 核VLA模态融合 |
| 19766 | 单图consistent不保scene → explicit3D scaffold → 核生成几何 |
| 19768 | trajectory grounding模糊 → keypointspatialvision → 核VLA空间表示 |
| 19788 | expertprior错可负迁移 → causallyconditioned Bayesianprior → 核噪声知识注入 |
| 19799 | ReLU rescale函数相同误推训练相同 → kernel/path控制 → 核优化几何 |
| 19805 | densemix弱记忆 → selectiveRL keytokens MetaMamba → 核状态表示 |
| 19811 | semanticquerycache可误归并 → schema/confidence/rollup验证 → 核缓存答案边界 |
| 19816 | recurrent music KV压缩漂移 → fullcontext/resetdiagnostic → 核长程状态压缩 |
| 19818 | pickle detector容易evasion/OOD → bytecodeMLscanner控制 → 核model artifact安全 |
| 19843 | MAS fault不区分topology → prompt/response/routing15fault → 核恢复控制 |
| 19870 | visualtoken压缩改attention实现 → basis reconstruction Flash兼容 → 核token/算子边界 |
| 19895 | reasoning diversity与correctness冲突 → bounded path entropy → 核RL多样性 |
| 19910 | intra/inter表示对齐混 → SSR2 GCD控制 → 核representation |
| 19918 | privateinfer只防半honest → maliciousclient protocol → 核威胁模型 |
| 19926 | LoRA DPnoise耦合 → alternativegradient → 核privacy/utility |
| 19931 | robustclassifier合成data混 → diffusionfeature AT分拆 → 核表示鲁棒性 |
| 19938 | expert load等同importance不成立 → replicateheavy+quant memorybound → 核MoE容量/通信 |
| 19945 | DP AdamW secondmoment偏差异构 → biasremoved update → 核训练几何 |
| 19946 | T2I漂亮不等于训练data有效 → diversity regression反证 → 核syntheticdata质量 |
| 19956 | fixedattentionmask OOD难 → maskpolicy control → 核视觉泛化 |
| 19964 | RND ensemble posterior关系不明 → NTK Bayesian equivalence → 核不确定性假设 |
| 19969 | entropyattention=重要性误差 → IDF reweight → 核信息选择 |
| 19974 | imagegeneration空间judge不稳 → checker/editor GRPO → 核可执行reward |
| 19980 | AR规划逆序难泛化 → dLLM reverseplanning控制 → 核生成因子分解 |
| 19983 | VLM语境安全不保物理state → context CBF uncertainty → 核行动安全 |
| 19991 | speechtext固定rank昂贵 → Matryoshka rank/dim → 核表示资源 |
| 20017 | tablecontext依赖已知query → query-independent信息保持canonical → 核memory reuse |
| 20021 | isolatedAgent test漏持续滥权 → livecase falsecompletion/nonowner/shell → 核权限/完成证据 |
| 20031 | introspection报告是否真实未知 → conceptinjection/logitlens控制 → 核可观测性 |
| 20048 | Agent graphnavigation并非总更好 → BM25/control/toolunused → 核检索归因 |
| 20055 | environment编辑须持续保持constraint → scenegraph+2metrics → 核状态变更验证 |
| 20057 | force/action/worldmodel分离控制冲突 → imaginedonline/adaptiveswitch → 核闭环行为 |
| 20060 | MeanFlow oneshot模态不足 → continuousnoise GMM proposals → 核一步生成分布 |
| 20062 | init只看规模忽略feature reuse → diagonalnetwork4regime → 核pretrain形成 |
| 20064 | workflow语言未保信息流 → lambda noninterference/Lean harness → 核codeAgent安全 |
| 20070 | trainingfree inverse score难算 → kernel stochasticinterpolant drift → 核inverse采样 |
| 20078 | multiAgent gradientvariance随N涨 → analytical descent N→constant → 核MARL优化 |
| 20083 | RAG压缩/quant硬件失配 → CQCiM jointcontrol → 核memory算子代价 |
| 20084 | chart美观不保原则规则 → executable ASP检测/修复 → 核evaluation盲区 |
| 20089 | edge CLIP structuraltext错位 → alignment控制 → 核跨模态压缩 |
| 20091 | RAG externaljudge混 → single/multidoc internal-layer relevance → 核证据选择 |
| 20094 | CoT可被因果方向混杂 → matched oppositegraph/noise → 核causal reasoning |
| 20102 | refusaloutput不能约束latent → learned CBF barrier steering → 核安全可达性 |
| 20111 | selectiveprediction需cleanlabels → online abstention学习条件 → 核有限反馈理论 |
| 20113 | voice style/content混 → bottleneck destylizer双流DiT → 核streaming内容保留 |
| 20114 | unlearning单任务proxy不稳 → capacity/continual/memorization协议 → 核删除评价 |
| 20117 | RLVR verifier只看solution → verifier-environment generation → 核训练reward |
| 20119 | human video规划缺机器人几何 → keypoint/handreference switch → 核跨行动主体迁移 |
| 20122 | factualknowledge无法区分trainfreq与检索 → knowncorpus/context控制 → 核parametric知识 |
| 20132 | policydivergence多样性难控 → advantage f-div matching → 核RL更新 |
| 20133 | 搜索演化固定预算 → hierarchical bandit improvement → 核Agent预算分配 |
| 20137 | chart principles/rules难可执行 → ASP检测 → 核规范评价 |
| 20151 | nonmonotonicCRC不保stability → calibration条件理论 → 核风险控制 |
| 20152 | utility函数黑箱不可识别 → interpretable module learning → 核模型辨识条件 |
| 20153 | ensembleconfidence混epistemic/aleatoric → joint calibration → 核不确定性 |
| 20156 | skillfile常被当可信instruction → 202contextattack → 核工具/skill权限边界 |
| 20157 | monocularpose/geometry混flow → factoredsupervision → 核视频生成空间 |
| 20159 | video漂亮不保证规则推理 → ruleverifier/newtask scale控制 → 核评价盲区 |
| 20160 | 多view重建context线性增 → fastweight streaming → 核表示状态容量 |
| 20161 | edgefoundation压缩混对齐/trainingcost → projection+layeralign → 核端侧资源/质量 |

日期优先使以下潜力事实含糊项不继续核心，保留原题摘和重开位置而非贡献排除：19348 tactile-conditioned diffusion具体增量；19518 LLM/RDDL新控制条件；19555 supplychain SoK/viral Agent是新失效机制还是成熟传播原则；19569 KG多视角是否新增独立表示机制；19655 minimal semantic-state是否提供非经典学习更新；19802 linear ESN diagonalization是否新增condition；19914 narrativegame协议是否揭露新混杂；20042 edgealignment pilot是否改变机制。20126 已恢复并实际读官方 exact-v1 abs 完整摘要（`V3_NATIVE_abs20126.txt`，编号12–29）：randomized unmasking size 在 K<L 下给 TC/DTC 随 K 的 KL bound，属于可改变 DLM 并行采样条件的理论潜力，不以无实验排除；仍是日期 hold，不展开必要正文、不授候选或 Books。20084/20137可能同研究家族，但日期hold不将其计入分母，也不凭相似题摘先合并。

完整题摘明确不准入且日期未核实：19088一般Maude distributedfault framework无模型学习/执行增量；19184 TSM-VLM/TD3四动作领域recipe未建新机制；19358 ReferringRGBA新任务/data+baseline无独立长期增量；19414工业causal/federation领域pipeline未建立模型能力形成机制；19441 GitHub Agent PR merge组织关联非新执行机制；19442城市偏好VLM concept judge/ridge领域metric；19450 TEE领域advisor benchmark无新增通用失效路径；19467合成post/jurylabel平台成本无新评价盲区；19583 Docker codeevaluation工具集成无新隔离/验证条件；19614 industry section-decomposition对monolithic成熟流程包装；19828文本篡改task recipe/OCR+GRPO无独立机制；19837 metaRL survey无新增反证；19844 monitoring立场原则无具体新控制证据；19850 tactile U-Net领域single/multipoint测量；19930 imitationlearning agenda无新机制；19961 visualdocretrieval survey无新证据边界；20052 LLM entropy stationary假设corpus指标无新增能力/推理机制；20065多语言localaccuracy无控制机制；20130 clinical selective-CoT领域应用，不借训练/评价节点重引暂缓科学应用。

终止规则：精确dated公开公告或可信当日snapshot此前有限入口无法恢复时，以上必要日期隔离不授当窗候选/Books/无遗漏；当前可执行32确定日期潜力的证据和Books仍继续，日期隔离不冒充整日完成。
