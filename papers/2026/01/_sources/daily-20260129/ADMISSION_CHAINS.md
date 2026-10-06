# 2026-01-29 第二批准入校准输入

## 当前已冻结 reconciliation（覆盖下方早期暂定评分/待办标签）

2026-10-04 root实际逐项必要证据与处置通过41个确认落窗阳性家族：6整合/5文件、2已有覆盖、33仅报告。DART19278原已知遗漏项已恢复标准5与Only必要证据独立通过。Muon19400潜在新理论5分保留，但必要公式实际非作者核确认中心速率争议，最终Disputed/暂缓，不是EX或Only。冻结确认窗唯一候选42=41阳性+1争议；9必要日期终态隔离不计入。下方早期主表实际52条，不是49或最终分母，已按当前README与具名关闭归并。执行侧普通待办0，整日报告日级验收尚待。

19225/19290完整原题摘及决定性核心关闭已由root实际通过；19613/19700亦实际定点关闭，19747由原trace/patch/accept新增执行改动重判5标准Only后必要源通过。DART并行prefix-only未来边缘logits+CPU Ngram树ranking实际新增局部分支拟2+1+2=5，不保原7，逐项保资源代价与大batch反侧。此恢复只对应原已发现身份，不扩来源/会议或宽库存队列。

日期终态保留9项：19739/19686/19208/19245/19055/19156/19336、ART19673、HASTE19051。其必要first-public不能唯一确定，不计确认落窗分母，不因访问成本关闭贡献；来源表/当前README自包含身份、需求和重开点。普通工作不冒充受阻，历史正文材料全部保留。

这是题摘语义判断，不是审阅完成或最终候选池。全部以下项均已读精确 v1 完整题摘；来源映射见下。首批 Axe / ODC / SDFT 已由 root 校准，其余待第二批校准。映射 owner 仅作设计选择定位，未用作准入依据。日期上限取 TITLE_LEADS.tsv 的 DataCite `created` 原值，非 Updated；v1 Submitted 与官方公开日程仅提供首次可能公开下界。尚未独立复核或确认日期的项不写进确定候选分母。

## 原始完整题摘映射

- AB1.md：19001,19051,19055,19060,19062,19082,19089,19090。
- AB1_RECOVERY.md：19026,19048,19061,19066。
- AB2.md：19092,19106,19122,19132,19138,19139,19156,19174,19193,19199,19204,19208,19213,19221,19225,19231,19239,19245。
- AB3.md：19249,19278,19280,19285,19290,19306,19312,19320,19334,19336,19362,19400,19402,19404,19451,19484,19487,19503,19507,19510,19563,19583,19588,19605。
- remaining0_RECOVERY.md：19657,19672,19739,19747。
- remaining1_RECOVERY.md：19752,19773,19781,19786。
- remaining2_RECOVERY.md：19793,19798,19827。
- remaining3_RECOVERY.md：19834,19847,19897。
- abweb5_RECOVERY.md：19673,19675,19686,19700；最后两项页面正文预算不足，已由 remaining0 恢复。AB4.md 是并行 curl 失败的空头记录，不作为已读依据；AB4_RECOVERY.md 是 19611/19613/19620/19634 的完整 primary AB 恢复。

## 明确原始增量，拟准入（需 root 校准）

| v1 ID | 原有约束 → 原文实际增量 → 待核后会改变的选择 | 拟 owner | 拟分数 |
| --- | --- | --- | --- |
| 19001 | 推理压缩通常只控制输出预算 → 以 attention outlier 为信号按句删除 reasoning 片段 → 需核查删除内容与回答质量的取舍，而非把省 token 当自动无损 | AGENT-CONTEXT | 2+1+3=6 |
| 19026 | 更细 microscaling block 常被认为总能降低误差 → 分离窄局部分布与有限 scale dynamic range，给出越细反而更差条件及 UE5M3 替代 → block size 与 scale format 必须联合选择 | INFER-TENSORRT-LLM | 2+2+3=7 |
| 19055 | user edit 常直接当 SFT target 或 preference → 同一 feedback 含 label/preference/edit cost，理论给出各自依赖 user/distribution/class 的不同 tradeoff → 训练目标不能按反馈载体单选 | TRAIN-SFT | 2+1+3=6 |
| 19060 | MM-RAG 外部 detector/segmenter 预先决定检索 → 模型自生 search trigger、query modality 与 pixel mask，通过交错 supervision 学何时/如何检索 → region identity 与检索决策可进入联合训练 | AGENT-RAG | 2+1+3=6 |
| 19061 | 数据投毒检查关注 query/answer label → 保持两者干净但篡改 CoT 可跨域转移特定行为 → 对 reasoning supervision 的完整性检查不能由 label 正确代替 | TRAIN-DATA | 3+1+3=7 |
| 19062 | positive user approval 可被作交互质量代理 → 1.5M 对话中 disempowerment potential 与 approval 同向关联 → acceptance contract 不能把满意度独当用户自主性/长期可靠性的保证；限定真实使用观察相关性 | PLATFORM-EVALUATION-SYSTEM | 2+1+3=6 |
| 19066 | repair 模型输出 patch 后独立做 regression test → 联合生成 bug reproduction test 与 patch，并在真实120Google bug 上检查联合生成是否改变 test/patch选择 → 修复正确性需验证原失败与修后通过链 | AGENT-WORKFLOW | 2+1+3=6 |
| 19089 | 跨层 activation sharing 固定区域可能伤训练 → 从深到浅逐渐扩张共享区域，训练后同一模型支持可变共享长度 → sharing configuration 不必只靠静态结构裁剪 | MODEL-TRANSFORMER-LAYER | 2+2+3=7 |
| 19092 | 跨设备 shard 与线程 layout 分属不同表达 → named axes 统一 tiling/sharding/replication/offset 与 collective → 编译可在同一坐标语义下联合规划两级布局 | INFER-TENSORRT-LLM | 2+2+3=7（首批已通过） |
| 19122 | function-call 数据生成固定模式不能针对当前模型弱点 → RL query generator 与 FC 模型零和交替训练 → callable robustness 数据可随被训练模型更新而非静态扩增 | AGENT-TOOL-CALLING | 2+1+3=6 |
| 19139 | 多模态 prefix reuse 只按输入封装可能重复 encode 同图 → content hashing 跨输入格式识别视觉内容并复用 vision encoding → cache key 需区分内容身份与传输形式 | INFER-VLLM | 2+1+3=6 |
| 19156 | Muon 理论常以 exact SVD 替实际 Newton-Schulz → 分析有限 q NS 同阶收敛与 q/多项式度决定的常数，并去除 sqrt-rank loss → 近似正交化步骤数可由质量界而非只经验配置 | TRAIN-PRETRAINING | 2+1+3=6 |
| 19199 | UI 更新让历史 GUI grounding/流程失效 → 把稳定功能语义与 task intent 分成两级 memory 并按访问知识演进 → memory refresh 可按语义稳定度而非整条轨迹共用 TTL | AGENT-MEMORY | 2+1+3=6 |
| 19204 | visual-agent pipeline 选择通常手写 → memory-to-next-state 的 trajectory-tree supervision 学 hyper-agent transition → 可训练的委派策略需与 rule-based 微控制分开验证 | AGENT-MULTI-AGENT | 2+1+3=6 |
| 19208 | Transformer token association 只在训练后解释 → 早期梯度 leading term 将权重写成 bigram/interchangeability/context 三种 corpus statistic 组合 → 对 association 的解释需保留训练阶段和近似假设 | WORLDVIEW-WHY-MODELS-LEARN | 2+1+3=6 |
| 19213 | MX 低 bit 的 power-of-two shared scale 导致精度缺口 → 在线可编码的 metadata 修正量化并有轻量硬件支持 → bits/metadata/计算必须一起计成本，不按 payload bit 比较 | INFER-TENSORRT-LLM | 2+2+3=7 |
| 19221 | recurrent state 常仅视为固定 history summary → conditional DiT 编辑/生成 RWKV state，再以 global context 生成 WKV parameter → fixed-state容量与上下文依赖参数是不同替代路径；仅设计可行性 | MODEL-LONG-CONTEXT | 2+1+3=6 |
| 19231 | refusal 是稳固安全层的默认假设 → 1000 benign prefix 可无 malicious text 地删除 refusal 并做因果对照 → input safety 与 refusal robustness 应分开测量 | PLATFORM-SECURITY | 3+1+3=7 |
| 19239 | snippet vulnerability accuracy 被外推项目级效用 → 项目级 source/sink tracing 上低 recall/high false warning 与高成本 → 代码审查 acceptance 要绑定完整上下文和审查负担，不沿用局部基准 | PLATFORM-EVALUATION-SYSTEM | 2+1+3=6 |
| 19245 | 多轮质量评估多看输出或静态 confidence → 以 token uncertainty trajectory 波动 SpikeScore 识别 turn/domain变化 → 多轮可靠性诊断需要时间变化而非单次阈值 | PLATFORM-EVALUATION-SYSTEM | 2+1+3=6 |
| 19249 | memory agent 用历史 observation 直接行动 → 主动 probe 新 observation 并相对当前 ground truth 校验 drift → derived memory 的 freshness 应作为操作前条件 | AGENT-MEMORY | 2+2+3=7 |
| 19278 | draft model 逐 token 生成候选带串行依赖 → 并行预测未来 logits、树形draft并Ngram剪枝 → speculation 降draft latency时必须核验 proposal 质量/verification工作量的联合变化 | INFER-SPECULATIVE-DECODING | 2+2+3=7 |
| 19280 | RL rollout 固定 query mix/预算浪费简单题并欠覆盖难题 → EMA debias/multiplicative weight 动态调题并保持 mean rollout budget → 策略与采样分布共同适配，不能把均预算当同样训练分布 | TRAIN-GRPO | 2+2+3=7 |
| 19320 | STE round surrogate 在低比特训练不稳定 → 用 Fourier rounding surrogate 保留梯度形状 → QAT 的 backward approximation 需评价训练稳定性而非只前向量化误差 | INFER-TENSORRT-LLM | 2+1+3=6 |
| 19334 | benchmark contamination 很难被 output-only评测定位 → instance embedding perturb 与较少污染 reference model 对照 → decontamination结论依赖reference质量，不可只看单模型准确率 | PLATFORM-EVALUATION-SYSTEM | 2+2+3=7 |
| 19362 | 不等 sequence 的 FSDP per-layer collective 让快worker等待 → 点对点 parameter-server + on-demand barrier 将同步降至minibatch → 保持同步优化时可以改变通信/负载均衡粒度 | TRAIN-ZERO | 2+2+3=7（首批已通过） |
| 19400 | Muon 收敛界依赖严格update assumptions → 声称在更广设置给更快非凸收敛界 → 若正文提供具体假设/速率差，才能改变 optimizer理论适用条件（准入关键事实含糊，需定点 theorem） | TRAIN-PRETRAINING | 待判，不能仅概括性摘要定分 |
| 19402 | 多模型router需离线调参猜准确率 → 把 accuracy target作为runtime输入，用learned dual conditioning一策略覆盖区间 → acceptance 从超参间接调参变为可测constraint-response，非硬SLA保证 | INFER-SCHEDULING | 2+1+3=6 |
| 19404 | RL每轮全路径rollout成本高 → experience cache 固定 prefix只生成suffix → rollout节约的成立条件取决于prefix stale/off-policy与质量，而非token数本身 | TRAIN-GRPO | 2+2+3=7 |
| 19487 | scalar answer-vector steering在jailbreak/overrefusal间取舍 → 将近orthogonal answer/benign vectors以minimum-norm weight更新对齐 → 安全判定与是否作答可用方向耦合而非只变refusal强度 | PLATFORM-SECURITY | 3+1+3=7 |
| 19605 | proof failure导致全解释重生成 → entailment tree逐节点自底向上验证，诊断局部修订，theta role bindings保faithfulness → formal verifier的返回值可支持局部repair而非全轨迹retry | AGENT-WORKFLOW | 2+1+3=6 |
| 19611 | MHA heads独立且缩KV要牺牲表达 → HLC learnable K/V组合+group norm，并用low-rank virtual heads → head mixing与cache rank可作为独立质量/内存旋钮 | MODEL-MULTI-HEAD-ATTENTION | 2+1+3=6 |
| 19613 | KIE多个独立field仍AR逐一生成 → field masks+joint单forward，配套mask training → 推理并行来自任务conditional independence；不能推广所有document reasoning | MULTIMODAL-GENERATIVE-PARADIGMS | 2+1+3=6 |
| 19620 | GRPO同组全失败时advantage collapse → 同query历史trajectory replay+failed/truncated entropy ranking → outcome零差组可引入历史/结构信号，但需核实offpolicy与reward代理偏差 | TRAIN-GRPO | 2+1+3=6 |
| 19634 | VLA固定visual/depth/temporal计算路径 → 以action context选择/reuse/prune三轴计算，再由dense policy自蒸馏 → controller quality与选择性算力需联合检验 | MULTIMODAL-EMBODIED-VLA | 2+2+3=7 |
| 19657 | DLM sink位置随step移动导致信息过混合不稳定 → self-only但global-visible extra token结构sink，position/semantic无关性对照 → attention mask可固定吸收通道，不需把sink当语义内容 | MULTIMODAL-GENERATIVE-PARADIGMS | 2+1+3=6 |
| 19672 | federated LLM response provenance只能粗到client整体 → late-layer selection+gradient weighting做token级attribution → debug/malicious-client定位可细到生成token，但不得把经验accuracy当隐私保证 | PLATFORM-TRACE | 2+1+3=6 |
| 19673 | 音频单任务高分无法判断跨任务组合reasoning → ART要求融合不同audio tasks → audio reasoning eval不能由isolated识别任务汇总代替 | PLATFORM-EVALUATION-SYSTEM | 2+1+2=5 |
| 19675 | low-rank残差量化仍受salient columns outlier支配 → 相近重要性column permuted-blockHadamard保护salient块+R1SVD → rank/rotation/量化准备成本需共评而非通用rotation无损假设 | INFER-TENSORRT-LLM | 2+1+3=6 |
| 19686 | video RL全序列reward无法定位模态/时间依赖 → counterfactual mask+frame shuffle+entropy三信号选token更新 → RL token权重可结合perceptual/temporal因果敏感度，不单看entropy | TRAIN-GRPO | 2+1+3=6 |
| 19700 | editing只保刚性param-output mapping导致跨模态cascaded under/overfit → OOD三目标+trajectoryTV稳编辑路径 → edit success需同时测试semantic/factual shift，而非只原prompt | TRAIN-SFT | 2+1+3=6 |
| 19739 | activation优化对所有样本同策略 → instance-aware token seeking/ditching削减保留activation → 激活保存的粒度可取决实例，但AB未说明signal需定点method再判准入 | INFER-GPU-MEMORY | 待判 |
| 19747 | agent handoff语义drift与patch回归无法由simulation充分约束 → explicit design contract+dependency slicing localizedpatch+temporal/formal多分支验证 → code-agent正确性链要区分simulation覆盖与formal命题 | AGENT-WORKFLOW | 2+1+3=6 |
| 19773 | 静态诊断准确率无法测主动补证据能力 → atomic evidence ground truth+coverage metric，发现strong reasoner也遗漏信息 → interactive eval需测evidence elicitation而非只末端正确性；医疗仅evaluation实例非科学应用路线 | PLATFORM-EVALUATION-SYSTEM | 2+1+3=6 |
| 19781 | acoustic token保无关speaker、phonetic token可能丢prosody → differentiable-kmeans ASR/resynthesis多目标，测prosody保留与identity丢弃 → speech token需明确目标保留信息而非只重建/ASR两端选择 | MULTIMODAL-REPRESENTATION | 2+1+3=6 |
| 19786 | 减codebook被认为会分离accent与phonetic/speaker → ABX+VC两类probe显示ASRfine-tune降低accent但缩codebook不能解耦 → bitrate与信息可分离性不是同一轴 | MULTIMODAL-REPRESENTATION | 2+1+3=6 |
| 19793 | cyclicMAS统一强模型浪费轻子任务 → semantic embedding+graph结构meta-feature router，并onpolicy失败反馈更新 → 路由成本质量评估需包括阶段/图状态，非只query语义 | AGENT-MULTI-AGENT | 2+1+3=6 |
| 19798 | VLM只以视觉condition生成text形成text-dominant bias → 把visual tokens列为统一AR监督target → vision-as-input与vision-as-target改变能力与loss权重，不等于多模态输入自然保细节 | MULTIMODAL-REPRESENTATION | 2+1+3=6 |
| 19827 | oracle evidence一次给齐常被视为RAG upperbound → 控制检索覆盖/anchor/query/composition的分步实验，iterative可超过GoldContext → perfect retrieval不等于最优context schedule；ChemQA仅机制实例，需要确认不把sciencedomain应用纳入路线 | AGENT-RAG | 2+1+3=6（范围待校准） |
| 19834 | visual CoT常泛化为比textreasoning更强 → interleaved/纯text在favor visual world model与非此类任务的受控对照 → 视觉generation收益必须绑定representation bottleneck，非所有reasoning | MULTIMODAL-GENERATIVE-PARADIGMS | 2+1+3=6 |
| 19847 | activation steering静态方向可能伤已正确样本 → polarity-aware mean-difference找neurons并adaptive intervention → testtime steering需区分correctness-dependent gating和额外判别预算 | AGENT-REFLECTION | 2+1+3=6 |
| 19897 | SFT demonstration离线target产生forgetting → demo-conditioned selfteacher给onpolicydistill signal → 无reward时可以用同模型ICL teacher替fixed目标，但旧技能保持只能取局部实验 | TRAIN-SFT | 2+1+3=6（首批已通过） |

## 明确关闭或准入关键事实需补读

- 19051 HASTE：hard-negative generation/retraining循环是成熟原则；AB有baseline逃逸64%及更少iterations，但未给出新的成立条件或攻击/防御边界。决定是否只是现有原则的具体验证，需定点评价 protocol；暂不评分。安全主题不免贡献门槛，纠错/约束变化未见。
- 19082：payoff/language改变cooperation只是领域博弈benchmark行为，AB未说明改变执行、委派或系统safety contract的失效条件；关闭。若原文提供可用于通用Agent contract的新因果识别则重开，而非泛化governance口号。
- 19090：data-free DP syntheticdistillation含一般深度学习机制，但AB未建立LLM/Transformer、capability production或runtime主线关系。需只读setup确认是否为一般image classification；不因DP主题映射security准入。
- 19106：AST+introspection KB作deterministic check/repair及200手造Python snippets，未提出新的检测边界或证明compiler不能发现的机制，主要成熟staticanalysis组合；关闭。
- 19132：Edge/Core INC分类+6障碍的综述不凭review类型排除；需读六障碍是否给出新成立条件。停点为定点概览段，不扩全附录。
- 19138：semanticmemory+code-navigation+tool use的应用组合，153%相对correctcomments不能独立识别改动收益，AB未给新constraint/control；关闭（若安全纠错/约束信号正文实际出现须重开）。
- 19174：SHIELD检索/pattern/LLM三阶段+KB/prompt更新是成熟自适应检测loop；AB没有证明自愈resource-exhaustion边界，不能把F1当DoS防护保证；关闭，保留上述安全反证供root复核。
- 19193：executable Python监督+三阶段pipeline的table任务组合，数字未给新可行性/可靠性条件；关闭。
- 19225：KG路径sampling/relation preference若只是检索recipe不足，需定点method明确被替代假设后定判。
- 19285：memorization score temperature/noise correlation潜在测量增量需读AB具体内容后定判，现未评分。
- 19290：runtime角色graph生成可能是新委派execution也可能只是DynamicMAS包装；定点流程定义后定判。
- 19306：AppCards+curiositythreshold的移动Agent检索recipe，AB未解释threshold新条件；关闭。
- 19312：LightSBB是diffusiontransport理论，需确认结论影响generation objective而非一般优化；不能只用扩散词映射生成范式。
- 19336：event generator+GES+generation evaluation有可能是representation/transition增量，需明确是否action-conditioned；不以WorldModel命名准入。
- 19451：借SMEAR成熟dense expertgradient原则用于4语种ASRprojector，无新的routing条件；关闭。
- 19484：navigation+experience memory+diffusion motion的领域组合和dynamicbenchmark未说明新的model/control约束；关闭。
- 19503：早期gradient layer importance+同sign merge，有明确pruning时机/merge干扰条件；可准入但原始增量尚需root校准（不因遗漏于上表关闭）。
- 19507：4Agent自动构造LVLM safetybench，成本/模型区分度没有新增measurementblindspot或安全failurepath；关闭。
- 19510：ReAct、CaP、TaP与56任务的新benchmark组合，未显示新execution或可靠性条件；关闭。
- 19563：两层placement+effectivecapacity/Lyapunov是通用microservice调度，需判断是否FM实际state/partition约束而非语言包装，仿真84%本身不足；定点setup。
- 19583：component→metric的taxonomy没有新增测量混杂、盲区或机制证据；关闭。
- 19588：teacherstudent分歧→atomicQA→CoTfilter的curriculum具有实际learning增量，但仅医法域局部实验不自动准入；需要是否提出通用teachererror控制条件（定点filter定义）。
- 19752：五子系统+12designpatterns重构术语，ReAct case study没有新执行机制/失败识别条件；关闭。

剩余定点初筛是普通可执行工作，不作受阻或终态。没有因深审成本、Books已覆盖或访问状态改判。


## 2026-10-04 恢复后校准修正（覆盖上方暂定判断，不删除已读证据）

root 第一、二批原完整题摘与必要定点核：19122、19199、19204(MATA)、19090、19174、19507、19752 贡献关闭；19066 实际增量只是局部 test/patch 生成与选择，1+1+2=4低分关闭。不借既有失败→修复、分层memory、访问刷新原则给Dur3。

19026/19061/19156/19221/19245、19402/19605、19773/19781/19786/19798/19827/19834 已通过窄准入。19847v1§3.3 为早期prompt neuron特征+已训练正确性分类器gate，非oracle测试标签；AUROC .8347仅AIME局部。准入2+1+2=5，离线标签/训练和运行判别预算必须保留。

局部可复用机制通常Dur2，跨接口不自动SR2；重评对象只含原文新增命题而非联想到的成熟原则，未因阅读成本改判。ODC深入完成，root PRE与Ch39实际POST均通过；现有collective生命周期未承载owner布局与同步粒度分离，已整合Communication之后三段，正文保minibatch barrier、跨node primitive低于NCCL、hybrid内存及未来弹性边界。

### 决定性定点初筛（不是全篇审阅）

- 19132 INC v1 “Low Precision Data Types” L110–115：Core-INC须在switch间传高精度accumulator，若宽度≥payload2倍则抵消宣称2倍网络节约；Edge-INC可在NI本地持宽accumulator。树上首次累加位置决定upcast边界。原成熟低精度原则→具体跨switch宽accumulator打破traffic优势→不能仅按payloadbit与AllReduce次数选offload位置。拟2+1+2=5；不是综述标签关闭。另L129–150表明固定树/reproducibility代价及Amdahl模型而非实测10倍。
- 19225 RPO-RAG v1§3.3 L157–175：next relation preference+cluster centroid relevance weights是具体局部训练recipe（confidence不等于事实正确），新组件组合尚无新可靠性成立条件。1+1+2=4，可关闭；未借全部中间监督成熟原则给DD2。请root校准此评分。
- 19290 MetaGen v1§3.3 L168–182/Alg1：rewrite低utility role，DAG保持exitpath后deactivate/swap边，跨task reward-weighted线性更新。所述validity/feedback/graph约束是成熟组合，未提出新的execute/commit边界或相较成熟机制的新失效条件，贡献关闭；不因为state/topology术语准入。
- 19563 v1§II-A/B L65–81及TableI L234–239：model仅一般core/light微服务resourcevector、bits服务率、DAG；假设core确定、light随机且分布可准确profile，仿真随机resource参数。静态重服务/动态轻服务+effectivecapacity/Lyapunov组合未新增具体foundationmodel状态或计算边界。领域包装关闭，不因edge或foundation标签准入。
- 19588 v1§F.2 L427–432：teacher自生atomicQA，以IFD/.85similarity/teacher质量阈值筛，随后同teacher用其答案当groundtruth检查原CoT。未形成独立teacher error纠错条件，只是成熟self-consistency/分解curriculum局部recipe；贡献关闭，不把“verified”当事实正确保证。
- 19503 GradPruner v1§3.1/3.2 L107–118：初期累积gradimportance、top-p稀疏、只同signmerge局部recipe，原文30%→多一层sharpdrop且merge可多去3层是特定两模型取舍，不改变通用架构结论。拟1+1+2=4关闭，保留原潜在判断与原证据，不以已覆盖或工作量关闭。
- 19336 EAWM v1§3.2 L163–169：AGMM统计pixel偏差造event，GES分段后事件预测塑造action-conditioned worldmodel latent（§A.3定义）；这不是只把observation称event，新增监督target可核。拟2+1+2=5，标准证据待做。
- 19312 LightSBB-M v1§2.2及§3：dual objective解析drift/volatility+β在SB/Bass之间插值，为generative stochastictransport而非领域应用。拟2+1+2=5，必须核actual assumptions，不把32%syntheticW2当高维image普遍质量保证。

TokenSeek19739/Video-KTR19686 有明确same稿ICLR信号，唯一note ID已恢复但OpenReview公开时间接口403/浏览器验证；无精确公开日期则终态隔离日期，不当确定本窗候选。DART19278目前officialrepo明确EMNLP26，先前“ICLR”推测撤销；不由conference名字赋予2025时间。完整有限身份恢复在OPENREVIEW_IDENTITY_RAW.md。

恢复后root核19484/19510/19583任务recipe/taxonomy关闭；19503/19563/19588定点新命题4分关闭通过。19139像素hash/encoding reuse/continuous batching只有成熟cache实现，未见新的统一内存正确性或条件差额，贡献关闭。19249仅保留同methods受控20轮drift中memory有利初始表现却伤hidden变更、probe纠正未普遍成功反侧；2+1+2=5获root校准，撤销旧7与全freshness扩展。

19001实际§4替attention Softmax为Softmax1并LoRA SFT，不是posthoc句删除；校正上方早期准入链为attention outlier信号/actuator与质量长度取舍，证据仍待必要控制/理论核。19400 v1 Cor3.1的η^-1隐藏常数与η~1/T时O(1/T)中心主张冲突，定点原公式已核；争议隔离，不用降分/关闭掩盖。19208 author publication信号恢复唯一note A4Us8jxVGq，但API403/forum429；19245 author publication精确title+author信号恢复note Y16qXOaylp/API403；二者同稿first-public日期必要未定，终态日期隔离不进入确定当窗分母、不扩整个ICLR列表。对应原始材料 OPENREVIEW_POINT2_RAW.md。
