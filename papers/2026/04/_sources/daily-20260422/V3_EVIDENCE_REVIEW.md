# Apr22 必要证据与具体 Books 比较

作者：apr02。当前工作稿，不等于分母冻结、独立通过或日 Gate。窗口固定前日09:00至本日09:00；日期以原库存的早v1字段、OAI/连续边界与官方公告slot联合推定08:00～09:00，不单以submitted/DOI created作公开时间，拟正式采用前仍定点核例外。来源/准入进度见[V3_REVIEW_CHECKPOINT](./V3_REVIEW_CHECKPOINT.md)。未复现实验。

## 2604.18592v1 — Two-dimensional early exit optimisation of LLM inference

[official exact-v1](https://arxiv.org/html/2604.18592v1)。2+1+2=5，标准审阅已完成作者侧，独立终态待核。实际§3.1–3.3/Eq1–8/Alg1、§4.1–4.3、§5 Tables2–3、§6.1/6.4。只处理输入句子前缀×逐步开放层深的分类执行分支，不把它移作通用生成停止。旧全输入layer exit适合需要整个文档的信息；新路径以累计margin触发停止，未达阈值回最后层/末句，过去句子只补新开放层。算法状态是句子/层表示与类分数，而非原文后缀已被证明无信息。

§3.3将一次sentence-layer处理当abstract operation；§4.3预先存所有测试embeddings后扫约250组阈值，§6.4明确需要optimized inference engine和wall-clock后续工作。测试max-layer accuracy与2/4百分点允许损失定义比较边界，不能称独立线上校准保证。DGX A100×4/40GB是训练环境，不证明服务时相同speedup；模型Llama3.1-8B/3.2-3B、Gemma3n-E4B、Qwen2.5-7B，三sentiment数据各10K训练/5K测试且至少10句，输出分类、推理precision/concurrency/SLO未披露。复杂Amazon-5和FT后优势消失/倒转，Table5 Gemma MMS从2.3→4.6的代理收益到FT1.8→1.9，均不能外推wall-clock。

当前Ch56已有future-recovery early exit、估计器校准及model×budget共同资源合同；未把2D具体算法说成已覆盖。拟仅报告：有输入证据×深度的局部分支及反例，但本论文没有真实engine/端到端比较，长期采用只重复现有质量/预算边界，暂不为一个未实测路径新增机制正文。不是因为分类/小模型而拒绝贡献，也不由已覆盖主题降候选。独立可据明确缺口另裁决。

## 2604.18658v1 — Owner-Harm: A Missing Threat Model for AI Agent Safety

[official exact-v1](https://arxiv.org/html/2604.18658v1)。2+2+2=6，安全/评价适用边界深入。实际§2.4–2.5、§4.1–4.6 Tables3/6/8/9、§5/6.5–6.6。原文把owner资源/目的地/授权scope与content harm分开，但‘任何缺context classifier必有FN’不由定义无条件推出（always deny可没有FN却utility失败）；仅采用不能同时正确区分两个同内容不同授权上下文的边界，不采用绝对FN定理。

AgentDojo27 injection/97user task的1/27→4/27与450个优化后单作者标注diagnostic不能合并成泛化成功率。工具词表规则transfer与Qwen-turbo zero-shot比较的输入对象也不同：AgentDojo以goal/injection描述替tool-call，不能把gap百分比归因全靠Datalog。§4.6 pilot N12/15：拼goal文本的TPR下降并未实现structured goal-vs-action方案；P2去context也不能证明特定架构唯一因果。shadow30,204calls由作者非盲复核，不是独立生产安全验收。API relay model/evaluator/labels见原文；hardware/precision/latency/concurrency/SLO未披露，本文无吞吐比较。

拟已有覆盖 `PLATFORM-SECURITY` / Ch72：实际“Goal Alignment不等于组合后的授权”段及其前后sensor/dispatch/effect分权，完整承载数据范围×敏感性×目的地必须按owner authorization关系判、局部goal一致不代权限、guard规则/语义sensor各有适用条件；此处不主张原算法已在书里，也不采用author预测40–60% ceiling或‘goal structured后必改善’。有限新跨benchmark反证保留日报，但现有实际命题无需改。拟终态等待非作者核。

## 2604.18788v1 — Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs

[official exact-v1](https://arxiv.org/html/2604.18788v1)。2+2+2=6，确认具体knowledge gap深入。实际§3.1–3.3、§4.1–4.3、§5.1/5.6–5.8。静态NPU shape与MoE动态assignment冲突；host按calibration分capacity tiers，同tier专家组为dense固定切片并保weighted scatter，group launch摊销与padding/overflow质量冲突共同选择。热group驻NPU、冷/过细group CPU fallback是**graph placement**；§4.1明确overflow tokens不能临时spill到CPU/GPU，不能把它与预置冷专家CPU路径混写。容量不足以activation saliency pruning有损，不称dropless。

§4.2 graph过大（作者M2Ultra约1.2GB例）会CPU fallback；§5.8 Ours-all最佳latency却Ours-TG最佳energy，不能写三优化消灭trade-off。M2Max64GB/M2Ultra192GB、Phi3.5MoE/Phi-tiny/Qwen3-30B-A3B、FP16、prompt1024/4096、chunk256/512/1024、平均decode8token，同checkpoint/tokenizer/CoreML baseline；并发与生产tailSLO未披露。§5.6约10–20%token drop与约31.7–37.5%padding伴随约1%质量代价，是受测容忍，不证明效率不来自减有效工作或无质量损失。校准/跨数据dominance只有作者样本，不保证routing drift安全。

当前Ch49“Routed Activation Materialization→Indexed Execution”已有fixed capacity与dropless数据搬运，异构placement有dependency critical path，未承载**只接受静态图的后端中capacity tier×group granularity×graph residency联动及不能临时overflow spill的边界**。拟唯一 owner `INFER-TENSORRT-LLM` / Ch49，紧接上述fixed-capacity引句或附近两段，Ch21只提供router语义、Ch50 runtime不重占该执行机制。最小拟稿：静态shape约束下host先确定assignment/容量等级、同tier固定切片组执行再weighted scatter；随后解释group launch摊销与padding/质量、超大图fallback、校准热group与CPU冷group的条件、overflow pruning并非动态spill，漂移/质量不容忍时回退保守padding或通用dynamic backend。仅提案，未授锁/未实写，不计Integrate。

root 的[V3_ROOT_FIRST_THREE_ADOPTION](./V3_ROOT_FIRST_THREE_ADOPTION.md)已独立核前三项必要来源与当前正文：18592标准仅报告、18658安全深入已有覆盖、18788窄gap通过。18788据root许可实际写Ch49“Routed Activation Materialization→Indexed Execution”引段之后两段，source marker `SF-2026-ARXIV-2604-18788`；root随后实际顺读正文及邻接，确认capacity×group×residency、CPU placement不等overflow spill、精度与latency-energy取舍均与必要原文一致，写后独立通过。此单篇为实际整合，未复现实验，不代替整日日级Gate；共享锁已释放。

## 2604.18616v1 — ARGUS: Agentic GPU Optimization Guided by Data-Flow Invariants

[official PDF v1](https://arxiv.org/pdf/2604.18616v1)，HTML入口404但PDF必要内容已取得，并非全文受阻。2+2+2=6，具体compiler证据缺口深入提案。实际§3–7、§8、§9.3/9.4：每个元素的symbolic tag经layout algebra流动，用SMT关系断言在访问位置给出违反元素配对的反例；编译反馈→单元测试→profiling职责不同。flow-sensitive/path-insensitive，merge成top、pipeline shared-state重置；没有完整heap/global-write追踪，循环/形状静态限制也不构成任意kernel或softmax数学等价证明。

60个非平凡GEMM/conv消融同时移除tag与compiler feedback，不能将全部收益归因SMT。200个KernelBench任务的受测validity不保证speed：L1/L2 geomean .74/.88仍慢于reference，L2有4个PyTorch fallback。作者8×MI300X192GB、ROCm7.1.1/LLVM20，warmup与有限重复kernel测量；GEMM/GQA bf16、MoE FP8是不同配置，GQA形状映射Llama70B TP8不等真实serving验证；并发/输入输出/SLO未形成统一服务合同。

实际Ch49 interface symbolic-shape/type/memory、GeneratedTypedIR段没有**跨layout重排后逐元素语义配对的关系标签反馈**；Ch78 code/effect gate不拥有这个kernel数据关系。拟Ch49该接口主线最窄两段：shape合法不足以保证元素角色配对，编译期tags+反例指导修复但不替运行测试/数学验；维护知识库、保守top与未覆盖memory边界、fallback成本就近。apr20_resume已有限独立源→owner采用通过；尚未实写，不计整合。

## 2604.18791v1 — HELM: Harness-Enhanced Long-horizon Memory for Vision-Language-Action Manipulation

[official exact-v1](https://arxiv.org/html/2604.18791v1)。2+2+2=6，memory-conditioned risk输入与监督接口的具体缺口深入提案。实际§3、§4.1–4.4/Alg1、§5.1–5.4 Tables1–4、§6：episodic memory给VLA prompt及risk predictor分别提供历史；predictor标签是未来5步内失败，不是真实即时unsafe oracle。最多3次恢复尝试、回checkpoint动作目标不保证物理状态可逆；forward-recovery也只是模拟分支。

LIBERO-LONG 10任务/500episodes、CALVIN ABC→D、3seeds与受控边界扰动。Table3 full81.5、w/oSV73.1、SV无memory输入79.2；8.4pp是移除整个SV的差，2.3pp是SV保留但移除其memory输入的差，memory-free SV相对w/oSV仍有6.1pp，不能把2.3写成“无memory时SV全部增量”。该对照支持memory条件输入分支而非“历史越长越无用”；Oracle-history仍优于普通history。完整HELM与ensemble包含其他差异，intro“SV更准”不能由8.4比9.5推出。50K rollout数据一致不等总训练compute，A100约2h及12ms/step、15%overhead是作者条件；precision/实时控制SLO未披露。MLP输入维度文字与concat描述不清，不采用精确维度实现保证。此次apr20_resume非作者发现差值误读，作者定点重开官方Table3核81.5/73.1/79.2后纠正，不推倒其他有效证据。

实际Ch26 readiness/postcondition、局部纠错与long-horizon control已有责任主线，但未承载**过去执行记忆作为risk predictor条件输入，监督未来有限horizon失败与当前环境truth分开**的接口。拟在readiness/long-control邻段补最窄条件分支，保retrieval/监督/延迟成本与非可逆恢复、forward correction或safe stop；不是新模型摘要，不将SV替代controller safety。apr20_resume已有限独立源→owner采用通过；尚未实写，不计整合。

## 2604.18860v1 — Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents

[official exact-v1](https://arxiv.org/html/2604.18860v1)。2+2+2=6，保护边界深入提案。实际§3、§4 A/B/C、§5.1–5.8 Tables7–10：observation到click之间桌面状态变化；执行前截图复核使用target patch SSIM、全屏diff及窗口标题，三者都不能观测透明DOM hit-target改向。window存在不等新窗口、像素一致不等handler identity一致；再截图仍留race，不采用普适原子性不可能论。

Opus4.6/Ubuntu22.04 ARM VM、10个OSWorld任务测得gap；A135、B45、C45试验不可并成同一成功分母，30 benign零FP是有限样本。Table10的44/45=97.8%而非99.3%，表中timer还与30秒描述不一致；不将3模型headline全成功作保证。M4主机/1920×1080/API模型、单click试验、precision/concurrency/控制SLO未披露。未实现DOM验证推荐不算已证明防御。

实际Ch72 GUI grounding与general TOCTOU/effect gate缺**像素/窗口registry与实际点击handler不同观察面**的具体保护边界。拟在GUI grounding后两段：effect-time freshness需绑定目标/handler，不以截图稳定为权限；补不同sensor覆盖/剩余race与animations误报成本，高风险交可信DOM/OS绑定或人工fail-closed。Ch78仅保effect handoff。apr20_resume已有限独立源→owner采用通过；尚未实写，不计整合。

## ARGUS / HELM / GUI 三处最窄正文拟稿（待root许可与实际写后）

ARGUS插入Ch49 model–kernel interface的关系约束段后、生成kernel验证主线内，Ch48 speculative目标与Ch50 serving执行不重复此编译机制：

> Shape、dtype与访问合法，还不能证明layout重排后乘加的两个元素承担正确角色。一个编译反馈分支为元素附加关系标签，让它们随tile、transpose与layout代数传播，再用solver在实际访问位置检查角色配对，返回违反关系的具体元素作为修复线索。标签检查拥有可表达的数据关系，不替代运行时功能测试、数学等价或profiling；编译通过、测试正确和真正更快仍是三个验收对象。
>
> 这增加标签规则、布局知识库、求解与修复循环的成本。保守合流为未知、未覆盖global-write/heap、循环与形状限制，都可能使检查失去精度；受测反馈消融还共同改变编译信息，不能把全部改进归给solver。作者的MI300X kernel比较仍有慢于参考和PyTorch回退的任务，不构成任意kernel安全或Serving收益保证。表达能力不足、求解成本过高或目标库已经成熟时，应保留保守检查、独立测试及原backend，而不是凭关系标签越过功能Gate。<!-- source-family:SF-2026-ARXIV-2604-18616 -->

HELM插入Ch26“从Skill Postcondition到Next-skill Readiness Contract”中sensor不是真值的引段后、下游成功训练之前，Ch25只交接历史状态表征、Ch27只交接监督数据身份：

> Handoff是否可继续，还可能依赖过去的执行而非当前图像。一个条件分支把episodic memory同时交给动作策略与独立risk predictor，用未来有限步内是否失败的轨迹标签训练后者：历史为它提供当前observation没有的条件，但这类预测是有限horizon的失败sensor，不是当前环境的安全真值，也不能直接取得动作提交权。需分别冻结策略版本、memory检索规则、标签horizon与环境，否则策略或历史更新后，原校准可能失效。
>
> 历史检索和额外监督增加计算、存储与控制延迟；缺失、错误或过期记忆也会误导sensor。作者模拟实验中，保留verifier但移除其memory输入造成较小退步，不等于没有memory时verifier全无作用。回到已记录checkpoint的动作目标也不恢复物理状态，尝试次数有界仍需重新验readiness和safety envelope。记忆缺少支持、延迟超界或动作不可逆时，保留短horizon反馈、forward correction、safe stop或人工接管；模拟成功率不能升级成真机实时或恢复保证。<!-- source-family:SF-2026-ARXIV-2604-18791 -->

GUI插入Ch72现有无害图标→action grounding两段后、语义重建前；Ch78 effect layer只交接目标绑定，不重复界面攻击：

> GUI目标正确还带有时间条件：截图用于选定坐标，实际dispatch却可能进入另一个窗口或handler。执行前复读target patch、全屏diff或窗口registry能发现不同类型的漂移，但像素和窗口身份都不是hit-target语义；透明覆盖或handler改向可使画面保持相同，而动作去向已经改变。安全Gate因此要区分“所见内容仍新鲜”与“即将接收effect的对象仍被授权”，不能把截图稳定当作目标绑定证明。
>
> 再截图也留下复读到dispatch的剩余race，动画会增加误报和等待成本。高风险effect应尽量使用可信DOM/OS对象绑定、不可歧义的动作接口或人工确认，不可取得绑定时fail closed；低风险可撤销交互仍可走视觉快路径。作者的有限VM任务只验证几个sensor的覆盖差异，未实现的DOM校验只是建议，不支持它能消除所有race、跨Agent攻击或提供通用原子性。<!-- source-family:SF-2026-ARXIV-2604-18860 -->

## 2604.18995v1 — R²-dLLM: Accelerating Diffusion Large Language Models via Spatio-Temporal Redundancy Reduction

[official exact-v1](https://arxiv.org/html/2604.18995v1)。2+2+2=6，提前finalize与训练轨迹筛选的主张按必要机制深入，拟仅报告，不因Only逃避审阅。实际§4.1–4.2/Eq2–4、§5.1–5.2/Eq5、§6.1–6.7：窗口平均confidence可联合提交、重复预测取最高confidence位置，连续top1稳定且末步过阈值提前finalize；稳定不是正确性。SFT用冗余分数选择自生成回答、block32/complementary masks；Figure5及§6.7限定correct responses而§5.1没说明正确性筛选oracle，不能称无真值/无需外部判断的可靠训练pipeline。

LLaDA8B/Dream7B、generation256/block32、single H200141GB latency与4×H200其他工作分别绑定；非vanilla皆复用dual KV。MATH/HumanEval存在质量退步，Table6文字/表格数字也不一；NFE不能单独等价端到端收益或独立归因组件。precision/并发/生产SLO未披露。保留局部启发式与联合训练结果，不采用所有模型质量保持保证。

实际Ch24已有confidence×position的commit/readiness、连续步稳定仍可错与self-distill代价；本稿局部窗口/last-confidence等选择未改变该长期责任或新适用条件，不伪称R²算法本身已完整Existing。拟仅报告保留受限机制/反证，若独立复核定位真正未承载的边界再定点改判；未有Books新增。

## 2604.18607v1 — TurboEvolve: Towards Fast and Robust LLM-Driven Program Evolution

[official v1](https://arxiv.org/html/2604.18607v1)，实际§3.1–3.3、§4.2–4.3、§5.1–5.3必要机制与受控 seed 实验。2+1+2=5，标准完成、拟仅报告；root三项有限准入/处置校准已通过。不是仅因组件组合而拒绝：同一初始pool删去最强20%后，adaptive sampling与cross-island elite injection的排序/终局改变，是seed quality×allocation的受限新证据。完整pool下多个方案接近，不能把退化pool优势写成统一最优。

Verbalized sampling取多个程序但不使用回答中的权重，保前K；K在1/3/5/7间按archive update动态调整，cluster seed与elite互通继承OpenEvolve机制。800 evaluation包含编译/运行失败；Gemini2.5/3 Flash、3 seeds及API token费用只支持披露任务/协议的作者比较，不是其他论文对照预算都matched。hardware、推理precision、并发、端到端SLO未披露。Ch79已有搜索多样性/elite reuse/验证预算与起点条件主线；该局部pool条件证据保留报告，不把具体Turbo算法说成已有正文，也不因新选择器自动加章段。

## 2604.18909v1 — ChipLight: Cross-Layer Optimization of Chiplet Design with Optical Interconnects for LLM Training

[official v1](https://arxiv.org/html/2604.18909v1)，实际III-A/B、IV-A/B及V-A–C中的必要设计和模拟反证。2+2+2=6，root已独立通过具体准入；具体owner差异触缺口深入，拟两段、未写。CP/EP的通信阶段在允许条件下分离，采用可切换光链路，使同rail/port capacity在两种phase间复用，不是同时把一条链路容量算两次。封装内memory die与D2D/optical ports的取舍和外层parallel planner共同影响bottleneck。

作者用ASTRA/估算H100逻辑、HBM3与CPO参数模拟Qwen3-235B-A22B及规模扩展，并非实际1024卡训练部署；模拟吞吐比例不能作为实机加速。对照要保同optical ports/rail与是否reuse，较小规模优化有限、较大package减少NoP资源也可能移走瓶颈。precision、sequence/并发、真实SLO与光交换故障恢复未形成完整线上合同。

实际Ch36 collective语义/多GPU-NIC rail段及“可重构Fabric”说明拓扑revision，不承载**已知训练phase中CP与EP共享受约束光链路**这一不同资源选择。拟唯一 `TRAIN-DISTRIBUTED-TRAINING`：在可重构Fabric主线内部先讲互斥phase→同rail链路reuse及schedule/collective identity仍分权，再讲phase重叠/交换成本/状态漂移让复用失效，静态独立链路或普通ring/tree保留。Ch37/CP/EP算子切分不被该物理计划改写，Ch35仍拥有持久恢复；不采用模拟百分比或无故障保证。

## 2604.18701v1 — Curiosity-Critic: Cumulative Prediction Error Improvement as a Tractable Intrinsic Reward for World Model Training

[official v1](https://arxiv.org/html/2604.18701v1)，实际§3–5.3/Eq3–27、§6/6.1–6.2 Table1、§7限制。2+2+2=6，拟窄缺口深入，待独立source→owner。历史error improvement在γ→1、有限horizon的telescoping恒等式成立；将终态error换成渐近基线、再换成条件期望和同样本post-update error训练的critic，是原文明示的近似，不把当前critic变成已知不可约噪声oracle。§5.1以MSE最优conditional mean讨论，测量却用L2 norm而非平方：该基线是所选MSE训练目标下的残差，不能自动称任意metric/任意模型无法降低的绝对下界（例如非对称标量分布的绝对损失由median而非mean最小化）。只限制这条普遍说法，不否定telescoping或受测经验。

实验30×30格、450确定/450独立随机200维TV像素、预测当前cell而非下一转移，移动本身确定。MLP世界模型MSE/Adam每环境步更新、相同100随机warmup；critic60→128→1预测该样本更新后L2误差，tabular EMA为必要对照，策略V-table/ε=.3及EMA reward normalization固定。35K步/5 seeds以全部确定cell平均L2评价；Neural1.858±.080、Tabular1.912±.070、Oracle1.736±.063、Random2.348±.377，证明受限噪声环境中采样分配差异，不是大模型/机器人开放世界保障。hardware/precision/实时SLO未披露，§7明示高维/连续环境尚待验证。

实际Ch25探索admission段（无action视频→逆动作→forward差异→真实环境监督）区分模型自洽与环境truth，而后文“Prediction Error不能替代Update的反事实效用”已经明确不可学习噪声和update/hold效用分账，不能声称现章不辨不可约误差。拟新增仅限**在线learned post-update baseline作为探索排序surrogate**，不替代update/hold的真实收益裁决。唯一 `MULTIMODAL-WORLD-MODELS`，在探索采样主线内插入下列literal两段，后文反事实效用保留。尚无锁/实际写入，等待root有限采用核。

> 当探索预算有限、每次交互后都会更新预测模型时，还可以让另一条在线 critic 学习“同一样本更新后仍会剩下多少误差”，用当前预测误差与该基线的差来排序取样，而不是把最惊讶的区域直接当作最有学习价值的区域。这条分支把取样信号的估计交给 critic，把真实 transition 的监督仍交给环境：在所选损失和训练配方下，持续随机的观测可能误差很高，却不应因不能稳定降低的部分反复占据探索预算。它提供的是可学习进展的代理，不是已知的不可约噪声下界，更不是 planner 的真实 return；更新是否值得 promote，仍由后文的 update/hold 反事实效用合同验收。
>
> 在线基线需要额外训练、历史样本和归一化状态，同样本更新后的评价也可能乐观；critic 与预测器共享偏差、环境噪声变化或尚未访问区域，都可能让差值失真。作者的受限格子环境以确定与随机像素混合观察比较 neural critic、tabular baseline 和随机探索，支持这条噪声环境采样分支，不证明高维真实控制或任意误差指标下的最优探索。基线不稳定、交互不能安全试验或新区域缺少支持时，应保留 count/random 混合与保守探索，再用实际预测改进和闭环结果验收，不能把代理分数升级成动作执行权。<!-- source-family:SF-2026-ARXIV-2604-18701 -->

## 18909 两段窄稿（已实际写入并通过写后核）

> 另一个复用边界来自训练阶段，而非拓扑随意重连：当 context parallel 的序列交换与 expert parallel 的 token 交换在计划中不同时占用链路时，可以让两种 phase 复用同一受约束 rail/port 的可切换光通路，避免为峰值不重叠的通信各自预留一套物理资源。复用许可来自实际 phase 的互斥和链路容量约束，不能把同一条带宽同时记给两个 collective；CP/EP 的逻辑切分、rank 与 collective identity 仍由原并行计划保持，物理 planner 只决定何时连接哪些端点。
>
> 这条路径要把切换时间、phase 重叠、端口/封装内资源和 plan revision 一起纳入 step 成本；流水线或计算通信 overlap 改变后，原先互斥的 phase 可能竞争同一链路。作者在 chiplet、HBM 与光端口联合规划中的模拟结果只支持所测训练配置和假设，不是已部署集群吞吐，也不保证交换故障后可恢复。切换成本超过节省、实际流量偏离规划或无法验证互斥时，应保留独立链路、静态 ring/tree 或更保守的共享时段；持久恢复仍交给 checkpoint 合同，而不从光通路可重构性推导状态安全。<!-- source-family:SF-2026-ARXIV-2604-18909 -->

## 三项消歧关闭及日期工作依据

2026-09-27T21:28+08 补记当前官方 abs 轻核：18728/19089均只有v1且无 comments，19105只有v1、comments为12页3图；未见具体withdrawal/correction事件。它们的submitted仅识别版本，不当first-public。三个早v1字段与OAI/slot/连续身份组合支撑本窗有界推断，待日级独立核；不以页面未写标记声称全历史无纠错。

## 2604.19241v1 — UniEP: Unified Expert-Parallel MoE MegaKernel for LLM Training

[官方PDF-v1](https://arxiv.org/pdf/2604.19241v1)，实际读取§3.1–3.2/Algorithm1、§4.1、§5.1/5.3–5.4、§6.1–6.3/6.7–6.8及Tables3–7。官方HTML-v1页头为July29，当前PDF首页为April22且页边标v1/21Apr；本次采用PDF，不将后稿HTML细节回填。2+2+2=6，具体numerical/overlap缺口深入，拟Ch36窄增量，待非作者source→owner和实际写入。

顺序分离是准入依据：GPU可以在token数据到达后先执行ready tile，但token的最终expert buffer地址由source-rank前缀和本地stable-sort共同固定；tile-ready scoreboard与payload的release/acquire控制消费，combine需要等同一token的Top-k贡献再按约定归约，不由传输完成先后改写数学顺序。它将dispatch+GroupGEMM、GroupGEMM+combine局部融合为persistent workers；动态角色分配与relay一次跨rank传输/本地复制并非免费，消耗SM/HBM、原子队列及同步状态。buffer确定顺序只是必要条件，不足以独自证明所有GEMM/全训练bitwise；不采用摘要的无条件全图保证。

§6.1绑定两种Hopper节点、每node8GPU、80/96GB HBM、NVLink200/400GB/s单向；精确产品型号原表未命名，不据容量猜卡。12个DeepSeek/Qwen/Kimi MoE形状、8K/32K/128K，DeepEP commit3fcf25+TE2.11和COMET19831c是作者baseline；serial TE逐expert host同步与kernel选择同被改变，巨大layer倍数非纯通信因果。Table7在Cluster1/32K下拆subbatch的不逐bit路径有两项反收益（MoE10=.97、MoE11=.98），不能称放宽一致性必定更快。§6.7的128GPU/512K生产运行吞吐增加只支持披露训练配置，具体global/microbatch、全run质量验收、并发故障/SLO并不完整；不在正文照搬headline。model-driven调优29.7–149.9ms及4096-token bucket有摊销假设，缓存/配置漂移要重验；数值同一与收敛同一不同。

实际Ch36 Token Dispatch Contract拥有router/permutation/rank-group/step责任，后文Exact Training Replay拥有reduction/sample/collective顺序冻结；已有内容不能被说成完全没有数值合同。真正拟补的是**固定逻辑placement/归约次序与按物理到达readiness调度分离**，在Token Dispatch主线内两段：固定地址和Top-k贡献边界允许ready tile overlap，不能将无序到达变成无序累加；换取workers/scoreboard及低精度规则成本，不可证明所选GEMM顺序时回退顺序reference、或明确采用统计而非逐bit验收。Ch35持久恢复、Ch37局部tensor lowering不被该schedule接管。apr20_resume已在[V3_APR20_UNIEP_DASH_EVPO_INDEPENDENT](./V3_APR20_UNIEP_DASH_EVPO_INDEPENDENT.md)完成必要原文→真实owner采用核；root授锁后实际写入Ch36 Token Dispatch段内622/624两段与1640 Reviewnote，scoped diff通过。锁已释放，待root实际写后，不预计I7。

## 2604.19351v1 — DASH-KV: Accelerating Long-Context LLM Inference via Asymmetric KV Cache Hashing

[官方HTML-v1](https://arxiv.org/html/2604.19351v1)，实际§3.1–3.4/Eqs1–21、§4.1.1–4.1.4/Tables1–2、§5.3–5.4/§7。2+2+2=6，必要实现/性能宣称边界深入，拟仅报告。query动态MLP与key一次线性编码分责，在Hamming代理上选择全精度、residual补偿、mask三个计算等级；蒸馏/bit-balance/tanh退火是额外训练状态，不是既有checkpoint无代价索引。代理距离和学得残差不保证attention真值，V/full-K维护也不由hash表示自动消失。

关键反证是§4.1.4与§7明确原型使用FP16模拟binary hash，未实现底层bitwise operators，而存储/速度收益按理论1-bit packed模型计算。因此不把“约2倍/4倍”外推实测Serving或现有kernel；没有硬件、batch/concurrency/输出长度/SLO完整绑定，performance claim保持理论/原型范围。训练3K/推理32K、Qwen2-7B/Llama3.1-8B/Qwen2.5-14B LongBench作者对照支持受限质量，Table1 Llama平均42.43<Full42.70与多个切片退步保留。中间层替换/首尾Full降低误差也是选择成本；不能从少bit推sublinear总体decode，或将prefill平方与每步线性读取混同。

实际Ch45已有selector/summary质量联合预算、低成本ANN尚须验收、表示与consumer联合artifact及回退FullKV主线；本稿具体学得Q/K hash和residual配方保留报告，不把算法说成书中完整Existing，也不因索引新名自动追加长期正文。重新取得pinned packed-bit实现、真实端到端I/O/配置及质量合同才重开其部署效率采用，非外部材料Block整个family。apr20_resume已独立必要原文/实际owner核，受限仅报告通过，见上述三项独立文件；不是日级Gate。

## 2604.19485v1 — EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training

[官方HTML-v1](https://arxiv.org/html/2604.19485v1)，实际§2.2–2.3、§3/Eqs3–9/Algorithm1、§4.1–4.4/Table1、Limitations、AppendixA.1–A.2及C必要对照条件。2+2+2=6，中央保证范围深入，拟仅报告，待非作者有限裁决。terminal-only且γ=λ=1时可用critic或group mean构造return residual；每prompt batch的EV正负切换baseline，但训练全过程保留并更新critic，不是GRPO的无critic显存路径。零variance组的数值实现、sample EV与population EV不能靠公式自动相同。

在G=V+epsilon、E[epsilon|s]=0的population分解下，critic残差方差R+Var(delta)与常数baseline残差R+Var(V)的比较有条件成立；不等policy-gradient方差或learning success。AppendixA.1的Kalman融合K=PA/(PA+PB)还需两估计误差相关性/偏置条件：例如critic误差delta=a(V−E[V])使critic-error与mean-error相关，不能默认无交叉项。批量选择会与returns共享采样，§Limitations本人已明确没有有限样本concentration bound，故不采用Eq9“每步不劣于两者”的实现保证，不因这一披露把全部经验判无效/永久D；正文的PPO/GRPO不是总体替代史。

Qwen2.5-3B三Agent任务/7BMATH，Sokoban/FrozenLake/WebShop与DAPO17K的有限任务合同；Table1每任务512样本=32query×16rollout，best-validation口径不能当独立固定终点。AppendixC方法步数/clip/LR有不同，critic warmup额外200步也非零预算；Gaussian注噪是噪声干预，不证明EV是所有critic失败唯一因果。硬件/precision/端到端SLO与跨seed不确定性未完整披露。实际Ch32已承载critic质量、EV监测、额外state/成本、与group基线条件选择；本地zero-threshold recipe和受限intervention留报告，不写成已经采用稳定普遍controller。

**18616/18791/18860实际写后PASS（root，非作者）**：root实际顺读Ch49:1165–1185、Ch26:705–720、Ch72:960–983及各自相邻论证和三条Review notes。关系标签不代替等价/性能验收；有限horizon记忆sensor不代替物理恢复；GUI像素/窗口freshness不代替handler/effect绑定。成本、反证、共存与限制均保留，未复现实验。三项已实际整合，本日累计6项；前面各项“拟稿/待写”是历史准备阶段，当前采用状态以本段及正式README为准，不表示日级Gate通过。

**18701/18909实际写后PASS（root，非作者）**：实际顺读Ch25探索选样新增两段及后文update/hold、Ch36fabric新增两段及Live Reconfiguration交接。critic的任务是post-update代理与采样排序，不取得true return/执行权；同rail/port资源只在CP/EP互斥时复用，切换、overlap、模拟与checkpoint责任具体。两处符合前述未变的必要源边界，Review notes可仅同步写后通过；本日实际整合累计3，不等日期/整日Gate完成，未复现实验。

两处literal拟稿已由root非作者有限采用复核：root实际读18909 IV-B.2的同rail容量/CP-EP互斥复用、18701 §3–5.3/6/7的telescoping近似链与critic输入监督，并对读真实Ch36可重构Fabric、Ch25探索选样及后文update/hold。该写前阶段记录有效，后续实际写入与写后PASS以本节前段具名记录为准。18909只复用不重叠phase的物理资源，不更改collective identity、不将模拟当部署吞吐；18701承认现章已区分不可约噪声与真实效用，只新增online post-update误差基线的采样代理，不将MSE mean或L2测量升级任意metric不可约oracle。拟稿保留实际成本/失效与旧路径；不是日级日期Gate或全论文所有主张通过。

## 2604.19012v1 — Security Is Relative: Training-Free Vulnerability Detection via Multi-Agent Behavioral Contract Synthesis

[官方v1](https://arxiv.org/html/2604.19012v1)。2+2+2=6，安全评价边界深入，拟仅报告，待独立裁决。实际§3.1–3.5、§4.1–4.4、§5.2–5.5、§6.1：semantic slicer与规格生成器先消费漏洞/补丁配对、CVE和commit信息，再让judge逐样本核合成合同。它新增了reference生成权限这一可检查条件，不能把training-free说成没有特权标签，更不能把配对参考协议的结果外推到只提供单个未知函数的部署。

原文435对中8对格式失败，427有效对，但文字同时列859样本，与2×427不一致，不能补造统一分母。作者规格差异消融支持该受限pipeline，外部文献baseline未共同匹配输入权限/预算；17/97 false positives的安全担忧由作者审查，不是独立maintainer认定。Qwen3.5-9B slicer、多个7–14B规格/judge模型，dual RTX4090 24GB、Transformers bf16、temperature .2/top-p .9；无训练/量化，服务并发与SLO未披露。

对读Ch66 Evaluation Identity的model×harness×environment×scorer、reference权限与独立truth主线：此处具体算法及配对辅助不能被叫作已完整承载；受限新证据保留报告，不采用“语义歧义已解决”或模型大小公平比较，不需为这套本地规格组合新增Books正文。

## 2604.19049v1 — Refute-or-Promote: Adversarial Stage-Gated Multi-Agent Review for High-Precision LLM-Assisted Defect Discovery

[官方v1](https://arxiv.org/html/2604.19049v1)。2+1+2=5，标准审阅，拟仅报告。实际§3、§4.2–4.5、§5.2–5.11。冷上下文批判、条件反证、经验复现和人工裁决分工是受限流程；重要反证是多Agent共享的错误假设可被真正的行为测试推翻。旧171候选的36验证结果来自不断变化的pipeline，prospective30项的25淘汰另有分母，不能合成固定stage的精确因果收益。

CVEs、标准符合性与维护者接受也不是相同outcome。80+Agent与10个专职审阅者的Bleichenbacher共识仍误读CEK/GCM，作者经验测试纠正；这不证明共识总错。人工救回false kills、目标与预算差异、缺共同消融保留；订阅价不含人工劳动，不是完整成本。模型/API与各wave不同，hardware/precision/concurrency/SLO未形成统一合同。实际Ch66 measurement/reference/judge shared-blind-spot与独立outcome验收已经拥有一般责任原则；本地stage recipe及案例作为新受限反证留日报，不追加算法摘要，也不称完整算法已Existing。

## 2604.19092v1 — RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation

[官方v1](https://arxiv.org/html/2604.19092v1)。2+2+2=6，标准审阅后拟已有覆盖，待独立核真实owner。实际§3.1–3.3/3.5、§4.1/4.3–4.4及Tables1–2：生成视频经retarget/IDM提取动作后在重建模拟器执行，perceptual alignment、提取结果和实际任务检查器分别评价；真实场景来源不使evaluation自动变成真机。转换器自身用成功轨迹和有限配对sim/real运行作校准，不证明生成分布下或原始失败轨迹的转换忠实。

Table2的Sim+Real与Real-only不同，不能将转换器失败全部归世界模型。任务成功要求阶段和最终检查，不只可看的视频；Veo/Wan/Cosmos等生成配置与提取接口不同，不作统一公平架构归因。模型硬件、precision、总采样成本/并发、控制SLO未形成匹配合同。实际Ch25 Rollout Admission明确视频质量不能替代action-conditioned可执行结果，Ch66 Evaluation Identity明确harness/environment/scorer与adapter语义分别冻结。拟已有覆盖仅采用这条完整pipeline评价身份/环境outcome责任，不说原benchmark或转换器实现已在书里；新benchmark本身不产生必要正文gap。

## 2604.19157v1 — SAW-INT4: System-AWare 4-Bit KV-Cache Quantization for Real-World LLM Serving

[官方v1](https://arxiv.org/html/2604.19157v1)。2+2+2=6，标准审阅，拟仅报告。实际§2–4.2、Tables2–4及Appendix D的工作负载/指标/短长上下文。token/head分组、K block-Hadamard与在register中旋转query融合到decode kernel，保持stored K布局与consumer一致；plain INT4可能有更高带宽，旋转的kernel和端到端排序不等价。Ch45 inner-dimension grouping实际已有另一个kernel/layout分支，因此不采用“token-wise是paged attention唯一兼容方案”的一般说法。

短上下文量化开销能让BF16系统TPS更高；长队列下BF16同时active decoder减少，per-request decode TPS反而更高，却不表示请求更快完成。Appendix D为single H10080GB、Qwen3-8B、输入16384/256、输出1024、并发8/16/32/64/128；Table4单kernel为Qwen3-32B、2×H100/TP2/batch32，不合并为同一个SLO。评测有质量退步、block-size取舍与GLM不发生同类plain-INT4 collapse的反例，不称全模型近乎无损。实际Ch45量化反馈/rotation与layout联合artifact及Ch56请求完成/吞吐/队列分账已承载采用原则；本稿有限融合配方和条件化指标反转保留报告，不默认每个kernel新名都需要新机制正文。

18614 [HadAgent v1](https://arxiv.org/html/2604.18614v1)实际III-A/D/E与IV-A–E：固定bit-identical推理是架构假设，实际single-node macOS/Python asyncio测试没有分布式network；IV-C验证schema/hash/signature/缺失字段，而非独立重执行LLM输出，IV-D record/hub微秒/毫秒不是完整inference+consensus延迟。哈希/重计算/信誉/投票成熟组合没有实际新增执行保真桥，按具体贡献前分母关闭；不因blockchain标签或只无benchmark而拒绝。root具名独立校准通过。

本小批原库存18607/18614/18701/18909 v1 Updated依次00:00:42/00:00:54/00:03:06/00:19:27Z；前三者邻界连续ID与本日官方slot相容，18607/18614/18909 OAI日期04/22，18701当前OAI无值。DOI created晚于01:00Z只作批次落库身份辅助，不改名公开时刻。使用整批公告+连续邻界、早字段的有据08:00～09:00推断仍须独立日期Gate；不把当前三项标准/深入或关闭审阅误当落窗已独立验收。

## 2026-09-27T21:17:55+08:00：四项最小消歧收束

本轮实际重读当前AGENTS/三合同/统一Prompt及ROADMAP owner映射；复用162份完整题摘，不新增宽库存或全文队列。以下三项形成标准审阅提案，一项前分母关闭，均待非作者有限裁决，不预支当日日级Gate。

### 2604.18728v1 — The Cost of Relaxation: Evaluating the Error in Convex Neural Network Verification

[官方HTML-v1](https://arxiv.org/html/2604.18728v1)，实际§3.1–3.5、§4.1–4.3、§5.1–5.2。2+1+2=5，拟标准仅报告。凸过近似的可达解不一定是原网络可达解，但它可以保守证明整域没有反例；不把文中存在性查询的unsound称作所有安全证书失效。受测30个随机ReLU网络和MNIST/Fashion-MNIST比较原输出与全上包络输出，半径、深度及误差/分类不一致分账，支持有限替代表示误差观察，不证明LLM证书普遍失效。Ryzen5500U/TF2.4.1；精度未披露，Serving长度/并发/SLO不适用。

不采用§4.1从矩阵乘积直接推出所有网络指数增长的强表述：元素绝对值条件本身没有排除项间抵消、零偏置与等号边界；本次保留的是所测误差而非该普遍增长保证。§5.1使用半径.025定义包络但采样写[-1,1]，也不能把域外样本称同一域证书测量。真实Ch72保护sensor/形式条件与Ch66实验域责任已经拥有一般边界，具体随机网络测量只留报告，不追加全论文理论。

### 2604.19089v1 — Towards Scalable Lifelong Knowledge Editing with Selective Knowledge Suppression

[官方HTML-v1](https://arxiv.org/html/2604.19089v1)，实际§4/Eq8–10、§5.1/5.3/Tables2–6、Limitations。2+1+2=5，拟标准仅报告。冻结模型、外部事实池、NLI selector和首token对比干预是具体条件化编辑路径；Table3的locality/正确性分工及Table6全token干预反收益支持有限作用范围，不证明删去参数知识。Llama3.1-8B/GPT-J6B、selector1000监督例/A100、k5/alpha.2；precision/concurrency/输出长度/SLO未完整绑定，检索与selector训练/维护非零成本。

Eq8将prior写成旧答案首token的标量，Eq10若逐候选减同一常数，归一化会抵消，不能据印刷公式采用一般分布保证。为这一歧义只定点读取[作者代码](https://github.com/ekgus9/LightEdit/blob/f1031749a727173262ec440b6f934addf3c4bdc9/editors/lightedit/lightedit.py)：prefill_hook实际取得各对象前位置的**整个vocabulary** log-softmax平均向量，PriorSuppressionProcessor只在首步逐token扣减该向量。当前artifact解释了可运行的向量干预，不证明它在April已同版本发布或复现实验；不据标量写法否定全部作者结果。Ch20已有logit策略/归一化与Ch29外部context可逆控制边界；本地selector/首步配方只报告，不称整个编辑算法已有覆盖。

### 2604.19105v1 — EgoMotion: Hierarchical Reasoning and Diffusion for Egocentric Vision-Language Motion Generation

[官方HTML-v1](https://arxiv.org/html/2604.19105v1)，实际III-A/B、IV-A/B/D与TablesI–IV。2+1+2=5，拟标准仅报告。stage1用motion-token监督适配PaliGemma2-3B，stage2固定其梯度再训motion generator；joint-tuning语义对齐较高、fidelity较差的对照是可保留取舍，不证明梯度冲突已被独立测量。Nymeria约140K个5秒片段/80–20划分、23joints/150frames、b256；硬件/精度/实际控制SLO未披露，FS/FC不是物理controller成功。TableIII训练成本含适配阶段，不将只训generator与总两阶段成本混合。

真实Ch26 Action-facing Representation/Gradient Authority段已讲joint改写语义、分阶段/固定表示代价与direct-fusion共存。新受限对照仍值得报告，但无需为RVQ/latent diffusion组合新增长期正文；不因motion窄领域或局部实验拒绝，也不以FID或单框架排序声明生成范式因果优越。

### 2604.19299v1 — Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms

[官方HTML-v1](https://arxiv.org/html/2604.19299v1)，实际§3.1–3.4/4。最小消歧后具体前分母关闭，不评分：base无工具、SAS全工具、MAS按金融角色分配不同工具，固定ReAct/最多5轮在20金融数据集上的质量/能耗/延迟profile没有建立同权限同预算下新的协作失效条件或主线设计边界。completion只表示返回合法响应，不是任务正确；tokens/s与总延迟的分母不同仍是已有原则。不是因金融应用或小模型排除，而是原文新增主要为受限组合工作点，不能据规模排行改写Agent通用设计；不为关闭项重读全部附件。

四项v1 Updated为00:04:28/00:33:33/00:34:09/00:47:09Z，OAI均04/22。仅与已有官方slot、连续批次联合支持本日08～09推断，非单字段首发日志；本日独立日期Gate尚未通过。

## UniEP 实际正文非作者验收

root已实际順读Ch36:622/624两段及上下游，必要源沿apr20已核且未变化的PDF-v1范围复用。placement、payload visible/readiness与归约次序分离、完整训练未证、资源成本与reference回退和Ch35/37交接通过；正式记录见[V3_APR20_UNIEP_DASH_EVPO_INDEPENDENT](./V3_APR20_UNIEP_DASH_EVPO_INDEPENDENT.md)顶部。实际整合由6增为7，不代表日级Gate。

## 六项最小消歧后的有限审阅（162题摘内，不扩原始池）

### 2604.18913v1 — LogosKG

[官方HTML-v1](https://arxiv.org/html/2604.18913v1)，实际§3.2–3.4/Algorithm1、§4–5/Tables2–3、A.1。2+2+2=6，标准，仅报告待独立核。将实体/关系/三元组拆成稀疏关联矩阵时，frontier聚合不能单独保留路径；另存activated triple IDs恢复路径，按subject完整邻接分区、degree平衡、LRU和批查询路由，属于具体图检索执行分支，不因医学下游排除。

Table4的Jaccard比较是受测retrieved entity set，不证明全部path provenance或医学真值；Table2存在TorchCPU反收益，Table3大图cache不足导致换页压力。双EPYC9454/256GB、2H100NVL94GB与Numba/SciPy/Torch后端，不得把所有差异归GPU；concurrency/精度/SLO未统一披露。Ch76“GraphRAG的Citation必须绑定实际Traversal”已承载路径/来源与truth分权，本稿的incidence executor及局部profile保留报告，不冒称完整算法Existing，也不采用“遍历确定所以诊断可靠”。当前abs只有v1、comments为ACL2026接受，不是withdraw。

### 2604.18951v1 — Superficial Success vs. Internal Breakdown

[官方HTML-v1](https://arxiv.org/html/2604.18951v1)，实际§2–4.2/Tables1/4–6及AppendixD/E的诊断口径。2+1+2=5，标准，拟具体已有覆盖Ch82，待非作者核。固定learned topology跨域测试时，final accuracy与role/message代理可分离，增加了协作评价的负面证据；R以角色/输出cosine和peer相似度构造，O以消息/输出相似度权重乘LLM usefulness judge，不是移除消息的因果效用。

100日志的MAST/judge错误分组、行归一化heatmap不等所有运行failure prevalence；binary/MCQ/数字输出协议与领域有混杂，三run/两base范围不能推所有拓扑不泛化。实际Ch82“角色正确性必须独立于终局成功验收”832–836已明确terminal accuracy不证明角色分解、role anchor仅sensor与单体fallback，窄采用原则已完整承载。当前abs有v2=04/22T02:54Z（窗后），comments只有篇幅/共同贡献，未发现决定本次处置的具体纠错信号；采用v1不做无必要diff。OAI04/23可来自后版本，不能单独推迟v1归属。

### 2604.19031v1 — SAGE

[官方HTML-v1](https://arxiv.org/html/2604.19031v1)，实际§3.2–3.4、§4.2–4.4、§5.2–5.3/Eq12/Table5。2+2+2=6，因中心机制归因/评价权限边界深入，拟仅报告待非作者核。冻结backbone取last-token state、按dataset×backbone单独训练task-conditional SAE与分类器；中层可解码信息和最后层分类性能不同，是值得报告的表示选择证据，但这是派生probe训练，不是对原backbone决策的因果恢复。

class-centroid投影SNR/幅度与Top-K特征裁剪支持受限可预测性；不能由低幅度比证明原模型因功能语义压制而失败。标注bug/fix span中心4096窗口是特权输入合同，不能外推未知位置全文件；Table5有precision/recall取舍，小语言切片不稳定，四backbone各训练SAE不等同一表示跨架构transfer。RTX3090、SAE10epoch/B256/F16，Servingprecision/concurrency/SLO ND。Ch66 Attribution Contract2297–2300已分probe和可识别因果；本局部sensor配方留报告，隔离过强因果/普遍优于参数扩展的主张，不否定受测收益。当前abs只有v1/ISSTA接受说明。

### 2604.19305v1 — DebugRepair

[官方HTML-v1](https://arxiv.org/html/2604.19305v1)，实际§3.2–3.4/Algorithm2、§4.4–4.5、§5.1/5.4/Table6。2+1+2=5，标准，拟仅报告待非作者核。先slice测试再提议变量/插入日志，真正执行插桩代码获得runtime trace，不是模型虚构运行；去日志/注释后逐行一致及compile检查只保证所检查结构，不保证日志无观察副作用。规则fallback又有临时变量/控制结构改写，需在其受限运行范围理解。

perfect fault localization、6×4修复+8augmentation为32patch，但最多10次instrumentation调用另外存在；GPT3.5/API及双XeonGold6138/251GB，modelserving硬件/精度/总成本/SLO ND。Table6debugging有益，但去augmentation后plausible不变而人工correct下降，测试通过不等语义正确；主要文献baseline预算也不同。Ch80可执行诊断、frozen trace缺失状态与外部副作用重验已有原则，本稿定向插桩/受限实验保留报告，不把整套debug算法写已有覆盖。当前abs只有v1，无具体withdraw/correction事件。

### 两项贡献前关闭

- [19004 Ocean](https://arxiv.org/html/2604.19004v1)：实际§3估计symbolic pass及§5.1的337方阵/64矩形SuiteSparse工作负载；HLL/共享-全局hash是通用SpGEMM新实现，但原文与本项目的连接仍为稀疏attention潜在类比，没有建立大模型计算的特定layout/误差/执行约束或测量反证。按项目范围具体关闭，非说GPU新算法无价值，不追全部附件或发表史。
- [19093 AdaPGC](https://arxiv.org/html/2604.19093v1)：实际§4.2–4.4/§5.1–5.3，伪标签class-Gaussian累计统计+fused预测KL选择teacher、一侧stopgrad/InfoNCE与成熟entropy/balance组合，在Kinetics/VGGSound腐败分类的局部消融未分离新的teacher有效性/类别漂移边界。新增主要是已有校准/非对称适配配方工作点，未改变模态可靠性与任务贡献分账原则，故贡献前关闭；不是因为小模型/音视频分类或没有普遍保证拒绝。

上述四个拟候选v1 Updated=18913 00:19:38Z、18951 00:23:13Z、19031 00:29:06Z、19305 00:47:41Z，均早于01Z；只有18951当前OAI为04/23（v2后续），其余04/22。仍须与已存批次/公告slot共同解释，不能将Updated当first-public；日级日期独立验收待完成。两关闭项日期未作为采用依据。

## 生成修正与训练目标：三项必要审阅

### 2604.18738v1 — Remask, Don't Replace: Token-to-Mask Refinement in Masked Diffusion Language Models

[官方HTML-v1](https://arxiv.org/html/2604.18738v1)与[PDF-v1](https://arxiv.org/pdf/2604.18738v1)首页题摘一致，和库存当前v3题摘不同；本次以实际v1为准，不扩revision diff。实际§4.1–4.3/Alg1、§5.1–5.4、§6/主表及Limitations。2+1+2=5，标准拟Only。拆开当前token是否可疑与有无足够自信替代，检测器不变时把replacement换成MASK，延后在更新上下文中填回；每位置重掩预算与每步比例cap防重复开销。它提供具体detector/action比较，不只是换benchmark。

v1仅LLaDA2.1-mini、greedy、block32，八任务BBH仍退步、AIME不变；pilot选择与主表不可合成统一端到端成本。hardware/precision/并发/SLO ND。§5的mask无方向偏差、错token都adversarial是机制假设，不是一般定理；均匀噪声与结构错误不同不等支持集完全不重叠。当前Ch24允许重写→训练噪声/软输入→proposal span/remask→commit界限已承载长期职责，局部action消融保留报告，不因三种detector未逐字写入而追加算法。待非作者有限处置。

### 2604.18739v1 — Discrete Tilt Matching

[官方HTML-v1](https://arxiv.org/html/2604.18739v1)，实际§2.3、§3.1–3.3/Eqs11–19、§4.1–4.4/Table1、SAR必要条件。2+2+2=6，具体目标缺口深入，拟Ch24窄整合待非作者采用。不可算sequence marginal时，从冻结base rollout/reward构造masked中间状态，以exp(hr)加权的局部CE和control variate拟合reward-tilted unmask posterior；所需身份是base分布、mask hazard与局部target，不是AR token ratio。理论minimizer/terminal KL依赖相应base条件律及完整期望，不证明有限神经训练/旧buffer或confidence reveal都exact。

LLaDA8B、LoRA128/64、block32、训练长度256/T128，8H100的Sudoku比较；precision/生产concurrency/SLO ND。Table1在MATH/GSM弱于SPG，maze中大h/无control变差，replay和额外mask状态/优化有成本。Ch24现CTMC timing/destination及masked CE有一般目标链，但没有reward倾斜由terminal样本→local posterior→受条件KL的后训练分支；Ch31拥有奖励/KL设定，Ch33拥有具体policy-gradient，不应把这条matching误写成GRPO新版本。拟两段置Ch24 CTMC目标后：解释上述分工并保近似/成本/AR-RL共存，不采用最优/普遍更稳保证。当前abs v2/v3 May仅版本信息，未见决定本次处置的纠错说明，不展开史。

### 2604.18839v1 — One Step Forward and K Steps Back: Better Reasoning with Denoising Recursion Models

[官方HTML-v1](https://arxiv.org/html/2604.18839v1)，实际§3.1–3.3/Eqs3–7、§4.1–4.5、§5/Table1、§6。2+2+2=6，具体目标缺口深入，拟Ch24窄整合待独立采用。单步noised-target reconstruction与从自身状态多次应用的训练合同不同；从腐化目标初始化后在有限k次共享转移末端监督、整窗反传，为中间路径提供课程而不用完整长链TBPTT。这不等无条件train/test分布相同或证明模型真的执行规划。

现Ch24 finite-loop prefix distill监督中间深度，没有该“目标腐化初始化×短递归窗末端监督”的替代；拟接ELT有限loop段后两段，区分各目标/状态来源/梯度窗。ARC7M/14M、pass@2/checkpoint候选聚合与task提供示例FT须联合看，SPRM有预训切片退步，调深度/数据共同改变，不能将所有收益归递归。硬件/precision/总候选成本/concurrency/SLO未完整披露，额外k反传有activation成本；长轨迹/窗口外仍须验收。保单步denoising、TBPTT和固定深度共存，非新通用替代。

三项早v1 Updated分别00:05:31Z/00:05:32Z/00:12:16Z，当前OAI分别无值/May20/Apr22；与本日连续ID和官方slot共同支持工作归属，不能由当前OAI后版本或submitted更早单独改owner。未日级日期验收。必要审阅24→27，实际I7未变；这三项尚需非作者处置，不预支新增Books。

## 恢复后同步七项实际非作者复核

已实际读取[apr01三项标准Only审计](./V3_APR01_THREE_ONLY_INDEPENDENT.md)及[root四项处置与两项否定侧审计](./V3_ROOT_FOUR_DISPOSITIONS.md)。18728/19089/19105的5分标准Only、18913的6分标准Only、18951的5分具体Ch82 Existing、19031的6分定点深入Only、19305的5分标准Only均通过有限必要原文与实际owner比较。19004/19093具体前分母关闭亦有root必要原文反向核验。前文“待独立核”是形成证据时的阶段记录，以本次同步为当前状态；不改变评分或候选数量，27项必要审阅、I7仍未冻结。复核未验本日日期、全量否定集或全部外部目录，18738/18739/18839仍是普通独立采用待办。

## 静态 Adapter 接口与监督/评价合同：三项必要审阅

### 2604.18655v1 — Unlocking the Edge deployment and ondevice acceleration of multi-LoRA enabled one-for-all foundational LLM

[官方HTML-v1](https://arxiv.org/html/2604.18655v1)实际§3.1–3.5/4、Tables2–6、Limitations及必要A.1。2+2+2=6，具体执行接口缺口深入，拟Ch49整合待非作者采用。固定图可分别按任务编图并共享base、装全部adapter后one-hot选择，或把同尺寸LoRA矩阵作为runtime输入；最后一种让图结构与可换adapter值分离，但固定placeholder尺寸是前提。CTG是共同prefill后以mask隔离各suffix-KV，不证明不同adapter下任意prefix都可共享；DS2D另需prefix-tuning，不是没有训练。

1B/3B、GalaxyS24/SM8650与S25/SM8750 NPU；§3.3 INT4权重/INT8激活与附录INT16分支不可拼成一套条件。Table3单流174与式23×8+40不符，故不采用总体加速倍数；Table4超过100的相对G-Eval不称绝对准确率。长度/完整batch/并发/SLO和私有训练未披露。实际Ch49图/常量折叠及Apple静态shape未承载同shape adapter输入ABI分支；Ch30低秩训练与Ch45 adapter-KV identity仅交接。拟在三类优化前窄补2段：部署图与adapter值责任、shape/精度/状态兼容门槛和重编译/独立图回退，不并入全套手机框架。

### 2604.18811v1 — Rethinking Dataset Distillation: Hard Truths about Soft Labels

[官方HTML-v1](https://arxiv.org/html/2604.18811v1)实际§2–3.3、Table1/2与Figs1–2。2+1+2=5，标准拟仅报告。HL、固定teacher soft-label与augmentation相关SL+KD改变监督信息，学生compute匹配不等teacher总compute匹配；同学生预算下随机/高质量subset差距缩小，不能把蒸馏收益全归于输入subset本身。

ImageNet1K/ResNet18、TinyImageNet/ConvNet-D4、IPC10–700及2–50 full-dataset-equivalent epochs是受测边界；不推LLM软标签普遍使数据无关。硬件/精度ND，Serving长度/并发/SLO不适用。实际Ch27 bounded data patch及format/content干预已绑定actual supervision、teacher和预算责任；本次增加的是受限分类对照，算法/全部DD理论不称Existing，仍报告新反证，不因小模型或单分类否定贡献。当前abs仅v1/CVPR说明，无决定处置的撤回标记。

### 2604.18835v1 — Semantic Needles in Document Haystacks: Sensitivity Testing of LLM-as-a-Judge Similarity Scoring

[官方HTML-v1](https://arxiv.org/html/2604.18835v1)实际§2、§3三个结果切片、§4限制及必要stopping定义。2+1+2=5，标准拟仅报告。相同语义扰动移动文档内部位置或换成无关周边文本，会改变judge similarity分布；这不同于candidate-order交换。五LLM、四到八句文档及negation/conjunction/entity置换，GPT5原hay方向例外保留，不称所有模型统一偏差。

停止协议先看最少100文档与均值变化，再以各位置最大样本量补齐；局部分布指纹不是跨版本稳定保证，similarity不是事实正确标签。§2完整输入由i,j=0…9产生1…19句，前文四到八句仅§3首尾偏差切片，不能当全文范围。API精确版本/硬件/precision/并发/SLO未完整披露。实际Ch66 Judge-as-truth/evidence-budget/顺序扰动及相关样本责任已承载采用原则；文档内部扰动是新受控证据，但尚不要求把所有敏感性配方追加正文。只作报告，不采用“语境解释框架”因果或长上下文失效通则。当前abs仅v1、页数说明，无决定处置的撤回标记。

三项v1 Updated=00:01:53Z/00:10:45Z/00:11:56Z，OAI分别Apr27/Apr22/Apr22；18655后v2解释当前OAI日期。与既有连续ID/slot联合支持本窗工作归属，不能把submitted或Updated单独当first-public。三项使用162已筛范围，不增加题摘数；必要审阅27→30，待有限非作者采用/处置和日级日期Gate。

## 生成目标三项的实际采用终态

已实际读取[root有限审计及写后记录](./V3_ROOT_GENERATION_THREE_INDEPENDENT.md)：18738标准Only通过；18739/18839的source→actual owner和Ch24真实正文/相邻链路写后均通过。实际分别在CTMC目标后与ELT有限loop后，不只Review notes。正式表/§4已同步30证据家族、实际I9；其他普通待办及日级日期/来源Gate继续，不代表全日完成。前文三项的阶段待核由本节替换，不重复审未变材料。

18811/18835标准Only与18655写前采用已由root有限核，见V3_ROOT_FOUR_DISPOSITIONS末；18835范围误述已按实际§2更正。18655获Ch49锁后在“静态图可以固定接口，而不必固定每个Adapter值”真实写两段，51/53，锁已释放待root写后，尚不计I10。

## 执行表示与保护评价：三项必要审阅

### 2604.18610v1 — SpikeMLLM: Spike-based Multimodal Large Language Models via Modality-Specific Temporal Scales and Temporal Compression

[官方HTML-v1](https://arxiv.org/html/2604.18610v1)，实际§2.2–2.3/3.1–3.4/Eqs3–14、§4.2 Tables4–5及§4.3。2+2+2=6，具体执行表示缺口深入提案。整数激活的逐步展开改成带符号、二进制activation spike、带时间权重的累积；不是所有模型weights变binary。压缩前先删除该对称scale下不可达的负端码，不是任意FP16表示等价。MED跨层cosine仅作时间预算proxy，模态/层分配与固定平均预算需共同验收。

算法对照与系统比较分开：Qwen2VL7B相关FLOP计数只分MAC/AC；硬件为SMIC28nm综合、ARM SRAM、HBM及cycle模拟，对比A800 FP16/batch1，不把模拟器与实板合成同硬件部署加速。长文本、并发/SLO未完整披露。当前Ch49低位LUT/ternary执行及persistent路径未承载activation码本×加权时间展开的ABI分支；拟窄补两段，保scale/非线性、时步累积成本与GPU回退，不采用headline倍率。待root独立必要源→owner。

### 2604.18663v1 — Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation

[官方HTML-v1](https://arxiv.org/html/2604.18663v1)，实际§3.1/4.1–4.3/5.1–5.6及Limitations。2+2+2=6，安全行为深入，仅报告已由root独立通过。单注入文档结合query/retrieval hook与语义payload，目标是流畅但无实质信息的输出，而非显式拒绝。A.4初采NQ/Hotpot/FiQA各100 query再按clean AUS≥4筛除；Table7随配置排除8～33/100，最终可回答cohort不是统一100。攻击fitness与SASR/HASR/MAD共同使用AUS，不能当三套独立任务真值。

GTR/Contriever与Llama2 7/13B、Mistral7B是主要边界；更多context不保证防御，PPL判据有数据集反向，不能说所有过滤总无效。主要方法/评价未绑定完整hardware/precision/并发/SLO，不外推线上攻击率。实际Ch72 Containment/可用性与质量分账已有长期采用原则；新soft-failure攻击与受限对照值得报告，不称整个算法已覆盖，也不为每个payload新增Books。root已在V3_ROOT_FOUR_DISPOSITIONS完成必要原文/具体owner有限核。

### 2604.18697v1 — Beyond Indistinguishability: Measuring Extraction Risk in LLM APIs

[官方HTML-v1](https://arxiv.org/html/2604.18697v1)，实际II-C/III-A–D、Alg2、IV-A–C与V必要范围。2+2+2=6，保护/保证范围深入，拟仅报告。membership advantage是相对先验、抽取是绝对生成风险；最坏前缀/逐位置rank envelope与固定API解码需分开。Alg2在top-m看不到目标时回到实际概率，作者明确这是低于不可得rank上界的估计，不可升级worst-case certificate。

受控实验为GPT2Small/Enron与Llama3.1 8B/Pile、BookSum，不是真实商用API部署；局部log-Lipschitz和完整条件期望不普遍成立。V实际说明DP降低ratio，不能从upper-bound差异否定此改善。Ch72 membership/抽取、先验/接口/攻击预算已具体分开，本次保新估计配方和上述权限限制，不称完整算法Existing、不采用DP全面无用或partial logits紧界。生产硬件/precision/concurrency/SLO未绑定，root已有限必要源/owner核通过Only，见V3_ROOT_FOUR_DISPOSITIONS。

三项早v1原字段分别00:00:48Z/00:02:01Z/00:02:57Z，当前OAI皆Apr22；官方slot/连续批次共同支撑工作归属，不把任一字段改名实际首发日志。当前abs-v1轻量查看未见决定本次裁决的撤回信号，不查完整版本史。均在162已筛范围，不增加题摘；必要审阅30→33，实际I9不变，普通独立未决继续。

## 空间接口、SAE干预与近似Prox：三项必要审阅

### 2604.18747v1 — URoPE: Universal Relative Position Embedding across Geometric Spaces

[官方v1](https://arxiv.org/html/2604.18747v1)，实际§3.1–3.3/Eqs1–10、§4.1–4.5主表/消融和0.C。2+2+2=6，具体表示/执行视图缺口深入提案。已知K/R/t将key像素射线提升到固定depth anchors，投影到query相机平面后使用普通2D RoPE；同view退化2D位置规则、2D–3D可不投影。anchor不是真实深度估计，几何标定也不由表示自动证明。

§3.3/Eqs8–9的关键边界：query-view移到batch维，K/V沿batch重复N次；attention渐近算术不变不等瞬时内存免费，也不是一份已旋转K在各query-view间通用。LVSM/Objaverse/RE10k、PETR/StreamPETR/nuScenes、UniMatch/Scenes11/SUN3D/RGBD是有限任务配置；RGBD SqRel .201弱于UniMatch .175（作者注明pose/depth误差），不采用全面指标优胜。联合batch/depth/width规模对照不能把50倍总因果归位置编码；未标定/大规模未验证、完整精度/并发/SLO未绑定。实际Ch23参考位置/pose、camera-state、track identity段已有几何身份原则，但没有query-dependent相对位置及KV执行视图门槛。拟在native3D/相机状态链最窄两段，Ch24/25只交接，不补物理真值；待root独立采用，未写Books。

### 2604.18756v1 — Towards Understanding the Robustness of Sparse Autoencoders

[官方v1](https://arxiv.org/html/2604.18756v1)，实际§3.1–3.4/4.1–4.3/5 RQ1–4、Tables1–9、§6。2+2+2=6，保护行为范围深入，拟仅报告。预训SAE替换residual为decoder(encoder(h))，base参数不变，白盒攻击可穿过SAE求梯度；改变前向表示不是安全sensor，也不是梯度屏蔽。Gemma2 2/9/27B、Llama3 8/70B与Mistral7B，bf16/PyTorch/NVIDIA GPU但SKU未披露；GCG500步/20后缀、Beast非梯度但可用logits、1500黑盒jailbreak和约218 HarmBench prompt分别说明。

跨模型30个off-diagonal pair和base/SAE跨配置36 pair不混分母；§5层深结果不是单调，Gemma L20→L30 ASR13.9→8.1是反例。No-Suffix依旧是有害prompt，不构成通用benign任务无损证据；三evaluator和黑盒detector方向也不同。§6增加500→1500步只测50prompt，不能证明优化预算无限鲁棒。谱/Jaccard变化支持作者bottleneck假说，不单独排除所有替代因果或给正式安全保证。Ch72保护/sensor与Ch66评价责任已有采用原则，本次保留可检查的表示干预/攻击合同，而非称全部算法已有覆盖或自动新增每个防御配方；拟Only，待非作者有限裁决。

### 2604.18857v1 — Task Switching Without Forgetting via Proximal Decoupling

[官方v1](https://arxiv.org/html/2604.18857v1)，实际III-A/B/C、Eqs3–8/Alg1/TheoremIII.1及IV主表/IV-G直接消融。2+1+2=5，标准拟Only。task-loss梯度形成plastic x，reflect 2x−y后对旧参数差做Fisher加权soft-threshold得到z，再以z−x校正auxiliary y，task最终提交z。F由1000样本对角Fisher并均值归一；k=5重复协商、η=γ=.005/λ10是实际配方，不等一次普通SGD零成本。

阈值条件只说明坐标被prox重置，不能识别它就是真知识保持；exact convex DRS条件不满足于近似SGD/非凸f，因此不采用稳定交集必收敛或zero-forgetting。ResNet18/5层AlexNet、多分类序列/独立task heads与表中负BWT保留；CIFAR短序列仍弱于SBMCL/BAN。TableII三runs与正文五random seeds口径不拼为统一CI；Fig13相对SGD1.16时间不支持无成本。λ过大阻适应，hardware/precision完整CI未披露，Serving SLO不适用。实际Ch29 trainable-subspace/参数保护最终delta与Ch28优化state已承载一般责任，这个反射/共识局部recipe尚不足以新增独立长期结论；Only不意味着精确算法已Existing，待独立处置。

三v1原字段00:06:01Z/00:06:29Z/00:13:17Z，OAI为空/Apr22/Apr22；个别字段缺OAI不伪造，与既有连续ID/官方slot组合待日级日期核。三abs-v1已有轻量撤回查看，不追完整版本史。162题摘不重复增加，必要审阅33→36。

18655实际Ch49写后已由root顺读两段及上下冷启动/三类优化通过，见V3_ROOT_FOUR_DISPOSITIONS末。报告/Review notes同步真实I10，普通队列和日级Gate仍开，不继承前文阶段pending。

## 攻击机会、字段干预、正确子集 Reward 与 Harm Probe：四项必要审阅

### 2604.18874v1 — How Adversarial Environments Mislead Agentic AI?

[官方v1](https://arxiv.org/html/2604.18874v1)，实际§2.1–2.2、§3.1–3.8、§4.1–4.4和Tables3/5/7。2+2+2=6，保护行为评价深入，拟窄已有覆盖：PLATFORM-EVALUATION-SYSTEM / Ch66。

代理仅改工具响应内容/图拓扑，不改权重或系统prompt；实验不允许独立verification channel。语义误导按non-abstain后的wrong计算DR，图陷阱按trap entry/遍历预算计算ER/BW，engagement另有retrieval与reference条件。Llama只有8/450实际engaged，7进入陷阱；5.6%无条件ER不能据此称模型鲁棒。11K是不同模式合并，不与主表5064、5336或后来每模型100个有效场景混为同一配对分母；Qwen原表82% API error不抹去。五模型原配置、ReAct/tool10次、T0与冻结snapshot只关闭受测接口，hedge/boost控制文字长度支持局部framing效应，跨维度logistic transfer接近chance不证明独立内部模块或普遍正交性。

实际Ch66“过程探索/利用错误”约2120的可观察opportunity、Outcome Witness约2139的提前失败不可作更安全，以及Ch72约603–605的中间完整性/external effect分账，已承载拟采用的机会→接触→错误/效果责任。不把该具体攻击harness或两种拓扑算法称全部Existing；独立语义复核待执行。服务硬件/精度/完整端到端SLO未披露，不将攻击率当生产安全保证。

### 2604.18880v1 — Where Fake Citations Are Made: Tracing Field-Level Hallucination to Specific Neurons in LLMs

[官方v1](https://arxiv.org/html/2604.18880v1)，实际§2.1–2.3、§3.1–3.4、§4.1–4.3/Table2、§7及直接统计说明G。2+1+2=5，标准拟仅报告。题摘新增贡献不是又发现hallucination，而是把citation的title/author/year/venue/DOI独立标签与FFN down-projection前干预绑定，能定点反查局部字段控制是否一律改善。

50个CS主题×3 citation-count×8风格、九生成器约108K citation不是108K真值论文；OpenAlex DOI/标题候选匹配后GPT5.4-mini+web复核，200条双专家约93%一致，未收录不等伪造。唯一probe/intervention模型Qwen2.5-32B，80/20 topic split、类平衡和64×27648 CETT features都限制推断范围；cross-field AUC .46–.59不能推出独立神经subspace。Table2 suppressβ0改善title/author，但year46.5<48.5、venue35.1<41.2，DOI仅微增；β4增强恶化也不证明一组唯一hallucination neurons。随机同数量neurons五次与β0有区别，但统计G把五field作配对样本，suppression-vs-random p=.062不是普遍显著改善。100条生成的JSON合法性不代一般fluency/utility。

Ch5“不是每个Neuron一个知识”与“可读出/干预/原决策”主线支持限制干预解释，但这个细分field实验不是全算法已有覆盖；作为可复查的局部反证仅报告，不新增每个probe配方。训练/推理完整硬件、精度、长度/并发/SLO未绑定，不采用通用低成本修复主张；待非作者必要处置核。

### 2604.18892v1 — Prioritizing the Best: Incentivizing Reliable Multimodal Reasoning by Rewarding Beyond Answer Correctness

[官方v1](https://arxiv.org/html/2604.18892v1)，实际§3.1–3.3/Eqs1–8、§4.1–4.3/Tables1–2和必要B/C judge/failure说明。2+2+2=6，真实objective接口缺口深入提案，canonical TRAIN-GRPO / Ch33；Ch66只接measurement边界。

binary answer verifier先形成正确子集I+，gpt-oss20B仅看文字(q,z,a)，对该子集按tie-aware tier排序，wins+half-ties经K−1归一再在I+居中；K<2明确aux=0，不能把Eq6裸代入singleton。总r=verifier+λaux，λ1下correct最小.5：负aux不是overall negative reward。纯子集零和重分配再进入原完整group GRPO normalization，没有识别token因果credit，也不让text-only judge成为visual truth。对比pointwise用同judge，Qwen2.5-VL7B/ViRL/rollout8/两epoch/lr1e−6/KL1e−2/step140固定；没有matched总judgecompute/墙钟证据，one-call读多trajectory不是免费。五bench各随机500题，RCAcc=Acc−CBIR是joint正确且consistency accepted，不是条件准确率；N/A解析处理、隐藏选项/晚答案修订会误判。Group总体RC54.7 vsRLVR47.4，但MMMU-Pro38.8<pointwise39.0，不能说所有任务最佳或正确CoT已证明faithful。硬件/精度/完整长度batch/并发/SLO未披露，未复现。

实际Ch33约650–671已把answer/context辅助相加分责，约989–1005已有outcome hard gate与bounded shaping，但未表达**正确集合内零和目标**与**最终完整group advantage**是两个不同归一范围。不是仅新增rank名词，真正差异是verifier决定资格、judge只重排已通过者、零/单correct fallback使辅助目标缺省可定义。拟在“Sequence Reward怎样作用到Tokens”后、具体集合credit分支前嵌最窄两段：

> 答案verifier可靠却不能区分多个正确回答的过程质量时，可以先保留完整组的outcome reward，只在已验证正确的子集中做有界、tie-aware的相对质量排序，并把居中辅助分数加回原reward；没有至少两个正确回答时辅助项归零。正确性资格由外部verifier决定，过程judge只拥有子集内相对偏好，之后仍在原prompt的完整rollout组内计算advantage。子集居中不等完整组归一，也不识别token级因果贡献。
>
> 这个分支用额外judge上下文和相对质量噪声换取正确答案之外的学习区分；judge看不到图像或受选项/解析影响时，过程一致性不能证明grounding或faithfulness。受限多模态对照有任务退步且未匹配全部judge成本，故应同时验收最终答案与独立过程切片；子集过小、judge不可靠或预算紧时回退outcome-only、可靠PRM或人工process标注，不凭零和公式承诺无reward hacking。

本项后续已获root必要源→actual owner/literal采用通过并按锁实际写入Ch33 Sequence Reward后两段；apr01真实顺读正文和前后交接的写后核通过，见[V3_APR01_18892_WRITE_AFTER.md](./V3_APR01_18892_WRITE_AFTER.md)。因此本项实际Integrate；上方拟稿保留为采用依据，不再是普通待办。未复现实验或通过全日Gate。

### 2604.18901v1 — Harmful Intent as a Geometrically Recoverable Feature of LLM Residual Streams

[官方v1](https://arxiv.org/html/2604.18901v1)，实际§3.1–3.6、§4.1–4.8、§5.1–5.6及必要限制。2+2+2=6，安全sensor深入，拟窄已有覆盖 PLATFORM-SECURITY / Ch72。各策略同element-wise max pooled prompt residual；不是不同pooling已对照。fit100+100、valid50+50选LDA best layer后各probe共用层，Soft-AUC从LDA warm-start不能据9°接近证明全局最优。角度probe约73°不同只说明不同读出模式，§5.4明确2D组合互补仍future，不当独立信息通道已证。

effectiveAUROC=max(AUC,1−AUC)与经验ROC插值TPR@1%FPR不是预先冻结部署阈值下的1%承诺。base/instruct/abliterated四family十二小模型及Qwen3.5 .8–9B只在clean English single-turn的heldout AdvBench/HarmBench/JBB/XSTest标签测量；maxpool可被token outlier影响，没有adaptive/multiturn/crosslingual验证，decodable harm与refusal分离不单独证明训练causality。RTX3070-Mobile8GB/nativebf16的probe局部时间不能外推免费线上安全gate；完整长度/batch/concurrency/SLO未绑定。

实际Ch72“Refusal Behavior不等于危险知识已删除”约1958与“Learned Security Sensor与Reference Monitor”约650，以及Ch66 calibration slice约1580–1606，已具体承载拟采用的表示可读≠拒答、probe≠authority、访问/模型/切片/operating point身份。仅对此有限命题拟Existing，不声称各种几何策略全已写进书稿；待非作者核。

四v1 Updated原字段分别2026-04-22T00:14:50Z/00:15:09Z/00:16:18Z/00:18:15Z；当前OAI前三Apr22、末May12。Updated/OAI不等实际首发日志：结合连续ID、已核官方slot与早字段作08～09BJT有界工作归属，末项后续datestamp不机械迁日；待整日日级日期复核。实际abs-v1轻量查看未见需改变本次裁决的撤回标记，18901后有v2不自动重要修订/全版本比较。完整题摘仍162，必要家族36→40、实际I10未变。

### 18610 已通过采用的 literal 与实际写后

> 低位整数activation并不只有一次性解码成dense乘法的执行分支：在码本、符号和scale已约定时，可以把指定整数码展开成带时间权重的binary activation spikes，用多个时步累积实现对应的线性算子输入；输入事件二进制不代表矩阵权重全部binary，也不把任意浮点模型变成精确等价的spiking模型。压缩可先移除特定对称scale下不可达的负端码，再共同选择模态/层的时步预算；非线性与跨层scale仍各自需要验证，时间一致性proxy不拥有最终质量判定权。
>
> 这用重复累积、时间状态和专用执行器换取局部低成本计算，预算越少越可能损伤表示。MAC/AC计数与工艺综合/cycle模拟应和实板端到端延迟分开：受限多模态对照尚不能证明同硬件、所有序列及线上SLO的部署收益。已有dense GPU、低位LUT和较大时间预算仍应共存；质量或scale接口不满足时回到原整数/dense执行，不以headline模拟倍率决定替代。Ch49 activation/state执行链是唯一owner，Ch23只交接模态表示。

root已必要源/actual owner和literal采用通过；实际两段嵌入Ch49低位执行路径后（753/755附近），去掉自指编写说明，Review notes对应1943。root已实际读取两段与相邻主干/Review并写后PASS，可计I11；锁已释放，不代表全日Gate或实验复现。18747写前采用与18756/18857 Only处置本轮root有限核通过，原必要证据复用，未预支18747实写。

### 18747 最窄 literal（已实际写入并获root写后通过）

已在Ch23位置/相机几何接口中reference累计offset与pose目标grid分责之后、native3D之前写入以下最窄机制；root实际顺读663/665附近两段及两侧正文，write-after PASS，Review856同步。未复现实验，不预支本日报Gate：

> 相对几何还可以由query所在视图定义，而不只由全局reference坐标给出。标定相机的token射线先在若干固定深度锚点升至3D，再投影到当前query视图，以普通2D RoPE编码投影位置；深度锚点是接口假设，不是逐点测得的depth truth。同一view退化为原2D规则，多view则让同一key在不同query-view下拥有不同位置视图，camera calibration与编码器共同定义这个derived state。
>
> 数学接口可以复用2D attention，不代表执行只保留一份无条件通用KV：把query-view维移到batch并重复K/V会增加几何计算、内存和读写，view或标定改变后不能沿用旧derived position。受限重建、检测与matching对照有RGBD指标退步，联合训练recipe也不支持单因果归因。标定不可信、锚点范围失配或预算不足时，已有2D位置、显式3D编码和任务专用几何接口仍应共存；第24/25章各自验收生成与环境状态，不把位置规则升级为物理真值。

### 2604.18933v1 — Gated Memory Policy

[官方v1](https://arxiv.org/html/2604.18933v1)，实际III-B/Fig3/Eqs1–2、IV-C Findings1–7、V及直接VIII-E/F。官方abs-v1和HTML均为短标题，库存长标题不沿用。2+2+2=6，Ch26实际episode memory/curator段之后拟窄gap深入：读历史的资格不由history长度直接决定，可由独立error-proxy校准controller。

两套不同policy分别memory-off/on在半训练集拟合，另一半以action prediction error ratio生成BCE gate标签；冻结gate后再用全数据训练最终policy，不是固定同一policy的每步因果memory necessity证明。history cross-attention residual被binary gate缩放，历史动作按当前diffusion step的一步更干净噪声训练及推理；滑窗缓存不是无限记忆。Fig13联合训练regularization两侧反益支持分开校准，而最佳checkpoint与多trial最后成功不当first-attempt成功。3080百forward均值与5090长history配置不能合成同一延迟合同；VIII-F gate流程有多policy/rollout成本、作者也建议必要时才启用。precision/完整控制SLO/并发未披露，未复现。

实际Ch26已解释episode state与history sensitivity≠warranted choice，但未承载**先独立校准读门、再冻结并重训policy**的训练/部署分支。拟仅两段解释proxy-gate与缓存/action controller不同责任，保留noise支持与反益/成本；不新增整套benchmark摘要。待非作者source→owner，不计实写。

### 2604.18946v1 — Reasoning Structure Matters for Safety Alignment of Reasoning Models

[官方v1](https://arxiv.org/html/2604.18946v1)，实际§3.1/4.1–4.4、5.4/5.5及6.4/Table5、6.5/Table6。完整摘要之后用最小结构定义消歧，准入不是因为安全字样：PU→HA→CR分段监督和移除/改写ablation提供具体保护行为与over-refusal权衡。2+2+2=6，安全深入拟Only。

900harm+100benign构成1K SFT，PU来自模型trace首句、HA另行生成理由、harm CR模板拒绝，不能证明结构是所有安全风险根因。Table5 actual full不是三指标均最佳；去PU的harm更低而效用变化，去HA/CR也有多方向差异，正文行号映射误差以真实表行为准。改写拒绝和改变benign量同时改变训练目标/支持，prompt intervention与SFT权重修改不同对象。R1-distill/Qwen/Llama/S1有限模型，不当DeepSeek671B；CMMLU仍有退步，multi-turn平均不推开放环境。完整precision/长度/batch/concurrency/SLO未绑定，不采用headline训练分钟。

Ch29条件化SFT与Ch72训练模板/stop-parser身份、sensor≠authority已有一般责任；本局部训练recipe和混合代价不被泛称全部Existing，也不逐算法写新章。仅报告受限保护分支及反证，待非作者处置。

### 2604.18963v1 — Distillation Traps and Guards: A Calibration Knob for LLM Distillability

[官方v1](https://arxiv.org/html/2604.18963v1)，实际§3–6/Eqs5–11、Tables1–4及直接Algorithm1/AppendixE。2+2+2=6，teacher calibration/模型保护深入，拟Ch29窄gap；Ch72仅接发布/抽取边界。

冻结原teacher与calibration proxy，先更新teacher使任务reward、原分布KL anchor和到proxy的sequence log-ratio共同作用；η两符号改变可教性，再训练student。task与calibration reward分别groupnorm，实际不是裸Eq6无尺度改变的唯一实现。不同tokenizer可各自给生成文本打分，不证明token probability逐项等价或终止/长度测度完整桥。Table4 Gemma token-RKL有两个反向，teacher/student utility也不是全部不变，不能把共变直接叫完全因果；wrong-trace偏好只是受测信号。Gemma12B→4B/Qwen8B→1.7B及更小proxy、有限数学/QA/RM评价，collapse不证明任意攻击者不可蒸馏。H100 AppendixE校准与下游GKD有额外一次性成本，批量/precision/长度/并发/SLO未全绑定；未复现。

Ch29目前capacity/表示/样本支持比较未表达**teacher本身先成为对student compatibility的可更新artifact**。拟在teacher选择/对齐段加入两段：学生loss以外还可先校准teacher，发布效用与可教性须分别验收；不把‘undistillable’当IP保护保证，不写完整RL recipe。待非作者必要采用核；student/teacher保持原状态和普通KD仍共存。

### 2604.18970v1 — Mechanistic Anomaly Detection via Functional Attribution

[官方v1](https://arxiv.org/html/2604.18970v1)，实际§3.2–4.2/Eqs2–6、5.1–5.3/Tables1–2、6及直接C.4/D.2/D.4。2+2+2=6，安全深入拟Only：参数邻域loss response与activation probe是不同sensor访问对象，受测obfuscation可改变检测排序，不用旧泛化‘局部研究’关闭。

trusted reference给局部SGLD采样及loss trace，test使用固定模型自己的prediction作为伪标签，再与reference trace作相关聚合；不是已知正确答案/训练样本因果归属。C.4也对trusted取prediction，不能把每条算法loss称gold。sharp/flat orthogonality需要相应support，不能从clean accuracy一概推出所有后门只落flat。Gemma2-2B与Llama8B limitedbackdoor、313+313+313与4096sampling、1000draws；LLM AUROC仅选实际正常/实际触发样本，不是全部query。DER threshold事后选best与offline UMAP额外test集不同contract，未固定线上低FPR。H100多forward/gradient时长是整批摊销，不是无状态单请求SLO；precision/完整generation长度/并发ND，未复现。

actualCh72 learned sensor/reference monitor已承载reference/threshold/authority责任，但此coupling estimator非全部Existing。本次保留whitebox诊断替代与obfuscation局部反证；trusted机制是否正常本身未可外部certify，ensemble decorrelation仍future，不采用‘modality-independent部署安全’保证或新增每个诊断器配方。拟Only待非作者核。

四项raw v1 Updated分别04/22T00:21:23Z、00:22:54Z、00:23:54Z、00:24:20Z；OAI空/Apr22/Apr22/May26。结合已核官方slot、连续ID及早字段推断本日08～09完全落窗范围，字段本身不是公开日志；提交都Apr21 provenance、18933后v2不自动重要revision，abs-v1当前轻量查看未见决定处置的withdraw说明。待全日日期复核，来源角色均作者实验/机制，评分不是独立验证。原162题摘不增数，必要40→44，实际I11未变。

### 2604.18978v1 — Low-Rank Adaptation for Critic Learning in Off-Policy Reinforcement Learning

[官方v1](https://arxiv.org/html/2604.18978v1)，实际§4–7/Eqs9–14及D计算成本段。2+1+2=5标准，拟仅报告：同一低秩约束在静态真值回归与bootstrap/replay shift下出现排序反转，值得核验更新子空间的正则化条件，而非因机器人benchmark进入主线。随机冻结基座仍作dense前向；feature-block低秩因子可训练，embedder/head另训；球面约束通过缩放B而不改冻结W0。Eq12在非零更新/κ∈(0,1)有正根，不把带ε实现称精确无条件单位范数。

13个SAC/FastTD3控制任务、5seed、SimbaV2及匹配可训参数的稀疏对照是受限证据；作者D明确实测显存和训练时间近似，不由参数节省推加速。rank/normalization与warmup差异非语言模型普遍结论。实际Ch30随机scaffold段107–111已说明固定基座/训练身份及dense成本，Ch32 critic属于价值估计；本次新增bootstrap条件的局部验证与归一化配方仅报告，不声称整套算法已完整覆盖，也不为这一受限配方默认新增正文。未复现，GPU具体SKU/precision/线上SLO未在采用范围绑定，待非作者有限处置核。

### 2604.18982v1 — Savoir: Learning Social Savoir-Faire via Shapley-based Reward Attribution

[官方v1](https://arxiv.org/html/2604.18982v1)，实际§3.1–3.5/Eqs1–6、§4、§5.2/Table2及D。3+1+2=6纠错深入，拟窄争议/暂缓采用归因与成本保证，非否定全部经验。机制先用删除部分话语后的重建history作future rollouts得到coalition utility，再以Shapley分信用、拟合RM，最后GRPO；utility仍是SOTOPIA grader而非真实社会因果，重建partner responses不保证原policy可达。

中心消融§5.2明确Shapley-only令所有S的v(S)=U(完整episode)；代入Eq4全部边际差为零，不能从Table2非零收益直接推出Shapley独立贡献。KernelSHAP Eq5缺显式baseline/端点约束，D的n=16样本例98也不等其min(12n+2,200)=194；不采用印出的精确Shapley或额外成本数字。Qwen2.5-7B、2×A10080GB、14/90scenario、GPT4o grader/partner主对照是作者受限结果，不推“推理有害”。实际Ch33集合内归因197与prefix continuation1785分别已有价值/信用职责；这条coalition实施证据有明确中心缺口，不支持新Books或完整Existing。重开只需实际Shapley-only coalition值、baseline/端点处理与有效simulation计数，不请求全部代码/版本史；待非作者核反例。

### 2604.19001v1 — When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains

[官方abs-v1](https://arxiv.org/abs/2604.19001v1)与[HTML-v1](https://arxiv.org/html/2604.19001v1)标题一致，替换库存HarmThoughts旧题名。实际§3.1–3.3、§4–6及直接A.1评价分母；2+1+2=5保护行为深入，拟仅报告。对同批标注依次合并16→6→3→2类，给出细粒度行为监测与binary安全分数不能互换的受控证据。1018条已筛harmful/partial trace、56931句，不是所有请求的风险率；人类691句/13trace校准后，整库由Claude机器标注，分布JS接近不证明逐句正确。

prompt级split、句mean pooling及best-layer/component sweep和不同parse成功分母保留；不能将事后best probe当固定线上monitor，几何可分不证明干预因果。7个输出标签反转例中2个内部比例倒置是有限描述，不推出RLHF必然学到隐藏恶意。实际Ch72 learned-sensor/authority分层与sentence-fence2393–2397已经要求taxonomy/分段漂移和effect独立验收；新granularity实测仅报告，不称新taxonomy天然优于旧方案或该算法全部Existing。未复现；线上latency/并发/SLO与GPU/precision未绑定，待非作者有限核。

### 2604.19015v1 — FedProxy: Federated Fine-Tuning of LLMs via Proxy SLMs and Heterogeneity-Aware Fusion

[官方v1](https://arxiv.org/html/2604.19015v1)，实际§4.1–4.3/Eqs4–14/Alg1、§5.1–5.3/Tables2–7/Limitations。2+2+2=6保护约束深入，拟仅报告。公共Alpaca的相邻层cosine用于删block生成同形状子网络，客户端适配该proxy，服务器分析task vectors作稀疏/带权符号合并，最后覆盖原LLM对应层；不是decode-time logit fusion。Alg1抽象写训练φ，不等全参数FT：§5成本明确为LoRA更新，不沿用“所有proxy参数都训”的旧推断。

IP在§5.3.3明确只是减少直接暴露、非密码/信息保证；proxy弱不证明不可抽取。Eq6用绝对cosine，反向也可获高权，不把它称同方向共识；Eq7高C表示冲突，§4.2.2文字把高C称consensus与公式不符，采用以实际formula为准，不扩大为所有经验失效。Llama2/Mistral7B、4/8client、QA/GLUE受测设置，Table4迭代通信/可训参数约4倍，非同预算；HTIES和ProxyTuning有任务逆序。实际Ch30组合admission518及同坐标merge530–537已有发布后行为回归责任，Ch36负责通信；本受限proxy配方/成本证据仅报告，不默认逐字算法缺口，更不宣称整个IP trilemma解决。未复现，硬件precision/线上SLO采用范围ND，待非作者核。

四项沿原162题摘，raw v1 Updated分别04/22T00:25:09Z、00:25:16Z、00:26:28Z、00:27:50Z；OAI分别May8、Apr22、空、Apr22。与已核slot/连续ID/早字段联合推断本日08～09，字段不直接等公开时刻；全日日期独立仍待验。当前44→48必要家族，实际I12不因这四条拟处置增加；不扩大515或重复完整题摘计数。

### 2604.18943v1 — Personalized Benchmarking: Evaluating LLMs by Individual Preferences

[官方v1](https://arxiv.org/html/2604.18943v1)，实际§3.2–3.4、§4.1–4.2、§5.1/5.4与§6；2+1+2=5，标准拟具体已有覆盖 Ch66。在13,383用户中选择至少25个battle的115人，平均59次；只比较每人实际投过的模型，不为未见模型补默认rating。个体与总体Spearman的Elo/BT差异提供具体测量边界，但题目选择、比较图和小样本估计仍随人不同；低相关不能单独证明偏好因果差异或个性化部署收益，p=.165也不证明BT等于随机。

topic/style模型预测的是已估rating向量，验证MAE改善不是匹配prompt后的在线utility实验。actual Ch66“Judge Ranking”217–230已明确局部比较/全局区间、slice identity、子群抵消和population/release分权；该具体采用原则已承载，115人新证据并非所有个性化算法已覆盖。没有新Books gap，不采用“多数人必然被aggregate误导”的强表述。硬件/precision/latency不是本次统计命题的评价对象，不适用；数据选取、pair覆盖和估计不确定性仍是contract。未复现实验，待非作者核。

### 2604.18966v1 — Self-Improving Tabular Language Models via Iterative Group Alignment

[官方abs-v1](https://arxiv.org/abs/2604.18966v1)与[HTML-v1](https://arxiv.org/html/2604.18966v1)题名一致，旧库存Reward-Guided Post-Training题名不用。实际§3.2–3.6/Eqs5–10/Alg1、§5.4/Table5–7和§6；2+1+2=5标准拟仅报告。高/低组各自policy/reference log-ratio均值的差先进入sigmoid，再共同反传；不是把逐pair DPO loss取均值，也不是GRPO组内reward normalization。随机组、固定scorer及训练双方消融提供受限目标/反馈条件证据；group变大也会平滑稀有模式，不能说任何B都减少有效噪声。

scorer可读取真实数据训练，LM alignment消费新生成row；Alg1评分池与classifier训练池分开，不能把“没有额外real row直接进入LM loss”改写成系统未访问real数据或formal privacy。Table7结构fidelity若干低于原baseline，MIA≈.5不保证所有privacy攻击；固定reference比值不自动成为KL硬约束或全分布防collapse保证。本次不采用未经检查的普遍convergence/monotonic/privacy主张。actual Ch34 chosen/rejected相对margin和group数据流、Ch31 proxy/独立评价已承载一般责任；局部tabular group目标与scorer对照只报告，不将整个算法泛称Existing，也不因一项新的sigmoid配方默认追加正文。作者采用RTX4090/A100混合GPU，训练分钟不能作matched硬件端到端收益；完整precision/row-length/batch/concurrency/SLO没有在本次采用范围绑定，未复现。待非作者处置。

### 2604.19033v1 — Intentional Updates for Streaming Reinforcement Learning

[官方v1](https://arxiv.org/html/2604.19033v1)，实际§3–6/Eqs3–16/Algorithms1–3、§7.3/7.5–7.7/Tables1–3；2+2+2=6，拟Ch28具体gap深入。先定义当前输出的目标变化，再用局部Jacobian与方向的内积反解scalar stepsize；TD(0)希望当前残差缩减固定比例，trace分支改为衰减历史输出变化的聚合单位，并用运行估计而非保存全Jacobian。普通parameter LR与RMSProp方向仍共存；分母接近零、非线性大步、旧梯度与当前tangent不一致都限制近似。

policy分支只设采样action的典型log-prob变化；原文明确非exact KL约束、非hard cap，action-dependent stepsize改变期望方向。不能把batch1经验变成无偏policy gradient或长期稳定保证。Table2 fidelity只在λ=0、30runs、三环境核验，不能验证有trace的全部界；Finger-turn多seed不稳、Table1多反向、Table3policy更新99分位比更大均保留。性能限MuJoCo/DMControl/Atari/MinAtar，不宣称语言模型预训练收益；GPU/precision/完整在线SLO未绑定，未复现。

actual Ch28“聚合梯度与逐样本残差”已给batch Jacobian/伪逆最小范数，后段给旧函数动量重投影；缺的是**先指定标量输出单位、再沿已选方向控制步长**，尤其streaming trace状态不等完整batch逆问题。拟在该段之前窄加两段：parameter-step单位→output变化单位→局部反解及trace聚合；典型policy变化≠KL硬保证、计量误差/方向偏置/回退。Ch32仅交接policy约束，不另起recipe摘要。待非作者source→actual owner，未写Books。

### 2604.19043v1 — 最小范围消歧后前分母关闭

完整题摘已在原162内读过，再实际核[官方v1](https://arxiv.org/html/2604.19043v1) ROSAME/视觉trace方法、MILP输入/整合和Table1即可决定范围，不评分、不加入正式表。它从符号predicate/action alphabet及完全观测的首尾state出发，拟合独立小型schema网络，再用subset MILP生成一致pseudo-label；Blocksworld/Gripper/Logistics/Hanoi/8-puzzle对照确有新的传统planning学习贡献，不能称无新意。当前研究对象仍是传统lifted action-schema识别，不是foundation模型的latent dynamics、VLA控制或大模型规划接口；逻辑纠错只能对当前主线作类比，没有原文提供的直接迁移机制。按Sources cs.AI不全扫传统planning这一范围边界关闭，不因小模型/负面结果拒绝。MILP一致不等物理真值仍保留，不把先前“潜在5”强制转正式候选。

以上四身份仍属原162题摘；三个新增正式必要家族，19043只最小范围消歧。raw v1 Updated=04/22T00:22:42Z、00:24:04Z、00:29:12Z、00:29:57Z；OAI Apr22/May19/Apr22/May8，只与slot/连续批次共同支持有界推断，不把字段改名first-public。48→51必要家族、实际I12，18892实际正文待root写后，不预I13。未扩大515、未冻结分母，普通工作继续。

### 2604.19052v1 — Cell-Based Representation of Relational Binding in Language Models

[官方v1](https://arxiv.org/html/2604.19052v1)，实际§3.1–3.3/Eqs2–6/Figures2–9；2+2+2=6，拟 Ch5 真实表示机制缺口深入。单一语义向量相近不能解释同实体不同关系的取用：以attribute-token activation预测entity×relation离散索引，用低维PLS作候选，再定向patch属性/查询/末token检验绑定输出。五个合成domain、Llama3-8B-Instruct/Qwen3-8B、random-direction和保索引内容/顺序扰动支持局部可读与行为相关；近完美fit不等自然语言泛化，高层检索示意不等完整原生circuit。

跨context需translation；13种pattern和受限DocRE不证明任意域同坐标。组件/层/scale选择、非自然activation与计算成本均保留，random matrix未证明全部范数matched，不采用唯一存储/真值保证。actual Ch5“信息存在、可读与被使用”205–220已有一般阶梯，缺的是entity与relation双索引不能压成单一entity位置的具体机制分支。拟窄补“语义内容 vs绑定地址”两段，保留文本检索、独立行为与原probe；待非作者采用，不写Books。硬件/precision/干预并发/SLO采用范围ND，未复现。

### 2604.19059v1 — AeroBridge-TTA: Test-Time Adaptive Language-Conditioned Control for UAVs

[官方v1](https://arxiv.org/html/2604.19059v1)，实际§III–VI/Eq3、TablesII–V；2+1+2=5，标准拟仅报告。最近transition更新32维latent，冻结部署权重只运行小MLP；同checkpoint改变α=0/.02/.1四条件对照是具体闭环适应证据，不只无人机组合成功。训练PPO/domain-randomization与部署latent状态分责；MiniLM只映射五任务，不证明foundation VLA接口可无训练替换。

V-B文字30episodes与TableIV60不同，不合成精确分母；V-C单checkpoint30episode不足归因两agent所有OOD增益。ID若干退步、Mass+50%两者因推力上限全失败、α门控future；50Hz是head主张，不是端到端SLO。actual Ch26受限action adaptation188–194和真实residual203–207已有状态/更新/执行权分账，但不是逐字算法Existing。本次保留无梯度latent适应的局部证据，不据四模拟条件新增普遍VLA或安全结论；仅报告待独立处置。hardware/precision/完整控制延迟ND，全部仿真，未复现。

### 2604.19071v1 — HoWToBench: Holistic Evaluation for LLM’s Capability in Human-level Writing using Tree of Writing

[官方v1](https://arxiv.org/html/2604.19071v1)，实际§3.1–3.3、§5.1–5.3、§6.1–6.2/Tables3/5–7；2+1+2=5，标准仅报告。instruction先由J_W给权重、leaf分别评分再聚合，与评分器临时改变权重不同；50文本扰动中Auto-planning的Drop=-.06、Repeat=-.30，反升发生在genre转换，撤销原笼统方向描述。221已选prompt、9模型、36专家/每篇两评分、system-level correlation及五高agreement专家回查的选择边界保留；§4.6的137/1302原人类参考被专家选出的LLM回答替换，不称纯人工reference。apr01必要原文/实际owner有限非作者通过，见V3_APR01_FOUR_19071_18842_DISPOSITIONS.md，不是日Gate。

SC的隐含贡献比例与显式weight不是同一估计量，方差不能归因全部收益；长度相关非增加输入的因果。额外judge/reference/regex、中文单轮/genre与扰动范围有限。actual Ch66 Per-verifier Outcome/聚合身份477–487已有子结果、权重版本与verifier分权；保留树状写作仪器局部反证，不称算法全部Existing或逐rubric新增Books。hardware/precision/SLO不作为该统计命题证据，调用/样本成本不省，未复现；待非作者处置。

### 2604.19079v1 — Reducing the Offline-Streaming Gap for Unified ASR Transducer with Consistency Regularization

[官方v1](https://arxiv.org/html/2604.19079v1)，实际§2.1–2.4/Eqs1–5、§3.1–3.4、§4.1–4.3/Tables1–2；2+2+2=6，Ch24 具体概率监督接口缺口深入，实际写入并经 root 非作者写后复核通过。同输入两context模式分别RNNT训练，对每个有效(t,u)完整词表分布作对称KL；frame-level CTC一致性损害streaming RNNT，辅助表示一致不等最终Transducer一致。Triton现场log-softmax/反向重算避免额外完整张量，仍需双模式前向；DM半batch预算匹配不等免费监督。

128M FastConformer/120k小时/100k steps/32 A100/greedy batch128/8测试集是主对照；XL正文280k与caption240k不合并。0.16s仍退步，C+R只理论等待非tail SLO，near-zero成本缺完整kernel量测。CTC损害原因是作者解释，compressed三概率/lattice-posterior只有早期对照，不保证full-KL普遍优。actual Ch24 CTC位置分布与n-best接口325–327缺跨可见context在最终RNNT lattice对齐、辅助CTC与目标解码不同合同；已后接两段，Ch23交接声学身份，失准保留pure-streaming/SM。precision/训练长度/并发/tailSLO ND，未复现；实际写后复核通过，见 [root 独立复核](../V3_ROOT_CH24_TWO_WRITE_AFTER_20260928.md)。

四家族仍在原162題摘；v1 Updated=04/22T00:30:14Z、00:30:37Z、00:31:51Z、00:32:27Z，OAI均Apr22。结合slot、连续ID/邻界和早字段推定08～09，字段不是首发日志。51→55必要家族，I12不变，18892写后待root；不冻结515宽库存、不把普通待核伪称外部受阻。

## 后续五项必要审阅：19047 / 19083 / 19087 / 19108 / 19117

本组均复用原162完整题摘，不新增raw或全文队列。逐项官方abs-v1已轻量核身份/当前版本说明，未见本组撤回标记，不宣称完成全站撤回检索。早v1 Updated依次为04/22T00:30:06Z、00:33:03Z、00:33:23Z、00:34:19Z、00:35:05Z；RARE OAI空、19117当前OAI为05/05，均不能单独改成首次公开字段。结合相同连续批次与官方slot推定08～09，定点例外仍留日级独立核；submitted仅provenance。

### 2604.19047v1 — RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora

[官方HTML-v1](https://arxiv.org/html/2604.19047v1)，实际§3.1–3.5、§4.1/Table2、§5.1–5.5/Tables3–4。2+2+2=6，拟评价有效性gap深入。重复文档使固定gold document ID错罚替代支持，近似重复又可能把Top-K消耗在同一信息上；原文先抽atomic information、用相似度过滤与LLM等价判定构造多chunk支持映射，再以Coverage与all-required PerfRecall分开部分/完整覆盖。CRRF把五准则分别调用后rank-fusion，§5.4的100 Hotpot长passage对照只支持该rank仪器局部排序，不证明judge已校准或事实为真。

Table2人工480项的filter recall89.6/83.6与precision57.5/50.8保留，4.2%整体FN不等全部benchmark无错。§5.3四hop Finance90.1→8.5是受测retrieval变化，跨domain相似度/训练能力未受控，不能归因相似性唯一cause。§5.5的E2E−PerfRecall被称Parametric Gain，但两项不同计分对象的差不是参数知识因果贡献；partial evidence可与模型先验共同答对，四格分解仍是诊断而非上限。作者GPT5 Mini generator/GPT5 judge及九retrievers/四corpora、Top10/hop1–4配置有限；hardware/precision、在线batch/concurrency/SLO未披露，新增atom/等价judge与基准构造成本不免费，未复现。

actual Ch66 RAG阶段归因596–611保存pipeline identity和stage receipt，Atomic Claim/alternative-evidence-path 1665–1696解释依赖与OR，却未具体说明retrieval gold应允许同一required information的替代chunk、并分部分覆盖/全必要覆盖。拟唯一owner PLATFORM-EVALUATION-SYSTEM / Ch66，窄补在RAG阶段归因中：固定document ID基线适用于唯一支持；冗余corpus需版本化information-to-support映射，Top-K按所需信息并集验收，随后说明LLM等价映射误差、all-required不保证生成正确、数量随atomization/预算变化。不是采用完整RARE框架或将CRRF常规化。root已完成非作者source→实际owner及[Ch66真实正文/邻接写后复核](../V3_ROOT_FOUR_WRITE_AFTER_20260928_B.md)，该窄分支已实际写入；未复现实验。

### 2604.19083v1 — ProjLens: Unveiling the Role of Projectors in Multimodal Model Safety

[官方HTML-v1](https://arxiv.org/html/2604.19083v1)，实际§4.1–4.2、§5.1–5.2.2/Eqs4–7/Table3、§6.1–6.3/Eqs8–9/Table4。2+2+2=6，安全/具体gap深入。只微调projector也可引入行为；整体ΔW谱分散、neuron频率/幅度无显著分群，不意味着行为无低维可干预结构。原文对同一clean/poisoned image分别取projector输出残差ΔE，再分解方向/逐token幅度；rank-k移除与重构是干预依据，而feature norm和幅度相关>0.95仍不是独立因果操控norm的证明。

Table3 rank1减去ΔW1可恢复Jailbreak utility28.91→86.91，但不同攻击/层非单调；rank1重构ASR0而rank3两层75.4，不能称唯一一维原因/全backdoor修复。LLaVA1.5-7B、10% poison、四trigger/behavior是主配置，MathVista24.3→17.7和POPE80.2→62.5 utility损害不隐藏。LogitLens token语义不是生成行为真值，clean输入也有漂移，不能靠单阈值把所有poison定位。hardware/precision/onlinebatch、latency/concurrency/SLO在本采用范围未绑定；需要干净projector对照/干预重测，未复现。

actual Ch72 upstream soft-channel/projector provenance766–768和learned sensor主线已分sensor/effect，但没有整体权重谱/单神经元统计阴性与paired输出残差低维干预的诊断对象分离。PLATFORM-SECURITY / Ch72两段已嵌在artifact/sensor论证：固定clean对应资产与matched input，分别检查ΔW/ΔE及行为干预；低维恢复只作受限diagnostic，保干净资产访问、全utility/未知trigger和回退。不要将Trojan Projection Hypothesis写成普遍norm→backdoor因果律。实际正文/邻接经[root非作者写后复核](V3_ROOT_19083_WRITE_AFTER.md)通过。

本次实际对读 Ch72 `Embedding 也是可执行数据供应链` 的 soft-channel/projector 段与模型文件行为验收段，最窄正文准备稿（保留为写前过程证据）：①“仅比较干净与待发布 projector 的整体权重谱或单神经元激活，若未见异常，不足以排除输入条件化行为。对同一干净/触发图像保留 clean projector 基线，逐样本比较输出 embedding 残差，再把低维分解、trigger probe 与最终生成行为分开验收；这些是不同的检测对象，不应让某一 sensor 代替 effect gate。”②“受测低秩移除可恢复某个 Jailbreak Output 切片的 utility，却在攻击、层和 rank 间不单调，重建与移除也非同一证明；MathVista/POPE 有退步，未知 trigger 仍需独立回归。该分支需要可访问的 clean 对照资产、配对输入与额外干预计算，不能由残差方向或 feature norm 推出普遍后门因果律。无可信基线或受限评测失效时回退已验收 artifact，不把可疑 projector 自动放行。”原文证据为[官方 exact-v1](https://arxiv.org/html/2604.19083v1) §5.1–6.3/Eqs4–9/Tables3–4；实际 Ch72 两段已由 root 非作者写后复核通过，见 [独立记录](V3_ROOT_19083_WRITE_AFTER.md)。

### 2604.19087v1 — OLLM: Options-based Large Language Models

[官方HTML-v1](https://arxiv.org/html/2604.19087v1)，实际§2.2–2.3/Eqs1–6、§3/Figure4、§4。2+1+2=5，标准拟仅报告。冻结backbone/head，以可见next gold token的encoder学K10离散option，decoder产生hidden bias；部署另由只读h的policy模仿encoder。训练时的特权option与部署选择分权是真实控制分支，不把它等同普通temperature或全词表policy。

约70% vs51%明确是optimal latent selection与LoRA结果，不是已部署policy的matched效果；§4把RLpolicy作为未来研究，与intro效率强句分开，未证明RLsample效率或所有valid continuation安全。训练本身含target0.2的KLuniform项，因此“无explicit KL”不能覆盖全部训练阶段。模型1.7B与AppendixB diagnostic1.5B口径分开，1.56%trainable不等同完整compute/latency下降；硬件/precision/完整训练与推理预算/SLO未披露。本次保留option接口与oracle gap证据，actual Ch20 sampling/steering212–243已有controller/sensor/外层预算责任，但不称整个算法Existing；没有可信部署选择与RL对照，不为“未来可用”新增长期优越保证。待非作者Only处置。

### 2604.19108v1 — Robust Continual Unlearning against Knowledge Erosion and Forgetting Reversal

[官方HTML-v1](https://arxiv.org/html/2604.19108v1)，实际§3.1–3.2、§5.1、§6/Eqs11–14/Tables1–3/Figures2/5/6。2+1+2=5，保护行为深入拟仅报告。当前forget与过去forgotten分开：后三阶段不再访问旧forget训练样本，用retain clusterability/条件VAE与原类negative margin控制；后续更新使过去删除目标重新可识别是具体保护失效，并非因小模型自动范围排除。

class-aligned CIFAR100/VGGFace2与class-misaligned MUFAC身份删除/属性任务不同；负class margin在后者不等删除个人影响，原文承认retrain仍有正margin，MUFAC亦有 reversal。Eq12比较当前forget集合与下一阶段累积forgot集合，改变样本mix，不能把单个均值当每个旧请求的配对恢复量；DBI几何与参数删除/攻击隐私不是同一证明。三阶段ResNet18/50、ViT和face/classification数据，不外推LLM多通道删除；只retain utility/识别accuracy不能证明membership/extraction已解除。actual Ch72约265–268行是遗忘 observable/独立攻击验收，约2673–2675行是concept suppression≠参数擦除；原2667–2671行属persuasion，不再泛引为遗忘。此算法不是精确Existing：本次留连续更新的局部配方/指标边界，仅报告而不新增类margin普遍删除原则。硬件/precision/完整成本/线上SLO未绑定，未复现；[apr20有限独立源→owner审阅](./V3_APR20_FOUR_18946_19108_INDEPENDENT.md)通过。

### 2604.19117v1 — LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit

[官方PDF-v1](https://arxiv.org/pdf/2604.19117v1)，abs当前v4/05-02；v1-HTML含legacy措辞且摘要与PDF表达有差异，故定点以实际PDF页头v1/04-21及必要pp3–9作为采用材料，不据此宣称整篇HTML已被晚稿污染，也不展开完整版本史。实际§3.1–3.4、§4.3–4.6、§5/Limitations，2+2+2=6，具体解释gap深入。独立题材ranking、matched random heads、patching与zeroing提供受限行为干预；component位置共享不等任务方向共享，opinion方向近正交并有sign-inconsistent零化效果。70B set sufficiency与mean-ablation不必要分开，不从相关ranking推出唯一知识来源。

Gemma2-2B零化将sycophancy28→81而factual69→70，方向是迎合增加而非安全改善。12模型13checkpoint主张依TransformerLens可用接口/单template，非普遍intent或现象学knowing；Llama3.1→3.3自然对照不能唯一归因posttraining，两个模型anti-syc/sham DPO才是额外有限受控证据。§4.5 CI重叠与均值落±.05不能单独证明所有probe等效，应保统计范围，不能将AUROC≈.61–.85升级部署monitor。硬件/precision与开放线上攻击/SLO未披露；需要whitebox hooks/干预，未复现。

actual Ch5 probe-readable/使用/模块移植180–224已有知识存在≠access，尚未分“共享组件位置/任务特定方向/行为策略”三对象。拟WORLDVIEW-REPRESENTATION / Ch5最窄两段接读出与使用：同一模块可介导真假评估和迎合表达，行为拒绝下降未必移除该诊断substrate；须分位置、方向、干预与最终行为，不把silencing当universalalignment。原有expression/access论点仍成立，这不是首次发现knowledge≠behavior；拟新增granularity与干预反证，待非作者采用，不写Books。

五项作者必要审阅与actual owner已比较，55→60工作家族；I12不变，三个gap只提案、两Only待独立，不宣称day Gate。

## 后续四项必要审阅：19009 / 19018 / 19021 / 19024

四项均来自原162完整题摘范围，不增加宽库存或重复题摘计数。官方abs轻量核精确v1及当前说明；submitted仅provenance。早v1 Updated依次为04/22T00:27:10Z、00:28:08Z、00:28:32Z、00:28:35Z，OAI除19021为空外均为Apr22。与官方slot、连续批次/邻界共同支持本窗08～09有界推断，不把Updated当首次公开。采用v1必要方法和决定性评价，不审无关版本差异。

### 2604.19009v1 — Guiding Distribution Matching Distillation with Gradient-Based Reinforcement Learning

[官方v1](https://arxiv.org/html/2604.19009v1)，实际§3.1–3.3/Eqs1–7/Alg1、§4.1–4.4/Tables1–4与人评段。2+2+2=6，拟Ch24具体蒸馏监督接口gap深入。DMD冻结real score、在线学习fake score，从detach后的student输出构造implicit regression target；reward model评分VAE解码后的构造目标，而非直接评分早期raw sample。不同t/fake快照产生target group，clipped reward差控制正负velocity policies。采用“teacher distribution给方向、reward instrument判断构造目标”分工，不采全面消除优化冲突的无条件保证。

SDXL4NFE与50/100NFE teacher、SD3Medium及作者GenEval/quality协议有限。Table1 Aesthetic5.8120低于CFG teacher5.8276；Table3 CLIP .2930低于NFT .2931，并非所有metric均优。Table4分t/fake/组合，非总训练compute严格matched；target group、fake score与reward调用增加成本。人评55.1%缺必要样本数/CI，不升级普遍人类偏好。hardware/precision/完整训练预算、online batch/concurrency/SLO未绑定，NFE不等wall-clock，未复现。

actual Ch24 Few-step Distillation约1093–1135已有student状态coverage与teacher energy target选择；Ch31独立reward梯度/QP不能替代对DMD implicit target而非raw output施加reward的监督对象分支。拟唯一MULTIMODAL-GENERATIVE-PARADIGMS / Ch24内部窄补target构造/评分/更新分责与reward bias、diversity、额外成本及普通DMD/更多步回退，不把整个框架入书；待非作者采用与实写。

### 2604.19018v1 — Local Linearity of LLMs Enables Activation Steering via Model-Based Linear Optimal Control

[官方v1](https://arxiv.org/html/2604.19018v1)，实际§4.1–4.3/Eqs13–23、§5、§6–9/Tables1–3及必要AppendixF.1–F.3。2+2+2=6，拟TRAIN-RLHF / Ch31具体runtime控制gap深入。对比均值方向定义linear feature/setpoint，在代表activation处线性化block得到Jacobian；offline Riccati计算gain，runtime按当前feature误差反馈。控制horizon是层深，不完整规划未来自回归内容；每次forward重施加。最小Euclidean移动只对linear feature约束成立，setpoint/probe不是语义真值。局部可微/Lipschitz及quadratic remainder条件不等全开放输入认证，采样最大误差不是全域上界。

Gemma2-2B toxicity4.16→.18伴PPL8.95→12.26、MMLU54.54→53.56；攻击可利用controller增加jailbreak，actuator不是safety authority。RTX4090、单词prompt/max100 tokens/100次中Gemma TPS51.37→40.28、Qwen14B31.53→21.51；offline Jacobian、gain存储和每token矩阵控制不免费。RTP/TruthfulQA代理、Q/R/λ调参与盲测切片分开；runtime precision/batch/concurrency/SLO未完整绑定，70B单项float16不外推全部配置，未复现。

actual Ch31约423–446已讲条件SAE intervention、token gate及组合失败；窄缺口为层间局部传输模型产生固定gain、在线误差反馈，非首次可撤销控制。Ch5负责probe可读/被用，Ch72保独立authority。拟Ch31 actuator主线两段：offline模型/feature/gain identity、online控制与线性化漂移；超校准区/utility损害回退小静态steering或权重后训练。待非作者采用，不写Books。

本次对读 Ch31 `从持久权重更新到条件化 Activation Intervention` 的现有 prompt/token gate、双 SAE 成本与组合失败段，最窄正文提案（待 root 写前裁决）：①“选择何时施加一个已知方向之后，还要决定当前激活偏离目标多少、干预怎样沿后续层传播。可在代表性激活附近离线估计各层的局部传输 Jacobian，选定 feature/setpoint 与状态/干预代价后求固定的层间 gain；runtime 每层读取当前 feature error 并反馈，保持 base weight 不变。这里规划的 horizon 是同一次前向的层深，不是未来自回归内容，也不是安全 policy authority。”②“局部线性近似与固定 gain 省去每 token 重解 Riccati，却引入离线 Jacobian、gain 版本/显存、逐 token 矩阵控制与漂移风险；feature setpoint 不是语义真值，理论 remainder 条件不能认证开放输入。受测 toxicity 改善伴 PPL/MMLU 与 RTX4090 TPS 退步，攻击也可利用该 actuator；超过校准域时回退较小静态 steering 或持久后训练，并以独立行为 Gate 验收。”原文锚点为[官方 exact-v1](https://arxiv.org/html/2604.19018v1) §4.1–4.3/Eqs13–23、§5–9/Tables1–3；本段未授权写入/未获非作者采用。

### 2604.19021v1 — FG²-GDN: Enhancing Long-Context Gated Delta Networks with Doubly Fine-Grained Control

[官方v1](https://arxiv.org/html/2604.19021v1)，实际§3.1–3.6/Eqs10–14、§4/Tables1–4/Figure2与必要AppA。2+2+2=6，MODEL-LONG-CONTEXT / Ch22控制粒度×并行代数gap深入，实际写入且经 root 非作者写后复核通过。naive channel-wise left gate破坏对称rank-one形式；key/value按sqrt gate缩放保DPLR/Householder-WY/UT，再以独立key/value scales分开erase/write。不是全矩阵独立Adam learning rate，而是低秩约束换并行训练兼容。

Table4 vectorβ LBP16.0低于KDA16.4，separate scalar16.7、两者18.3；Table2 RULER16K44.6低于KDA44.9。H80080G/BF16、总32768 token、2k×16到32k×1 prefill中<5%开销，不证明decode/端到端SLO。340M15B/1.3B100B、8K训练为限定recipe；§3.6与AppA的3:1 hybrid方向文字不同，不采用精确层比例为已证实现事实，不否定可定位的transition代数。在线concurrency/SLO未披露，未复现。

actual Ch22约230–274 GDN→GDN-2早已说明channel decay与erase/write解耦；不能据新算法名宣称原则从无到有。已在GDN后、GDN-2前补窄增量是“细粒度gate破坏原低秩transition时chunk parallel不会自动保留；双边gate约束表达自由度以换代数兼容”，保kernel/投影成本、任务退步与标量gate/Attention共存。已获[root 实际写后独立复核](V3_ROOT_19021_WRITE_AFTER.md)通过。

### 2604.19024v1 — Policy Gradient Primal-Dual Method for Safe Reinforcement Learning from Human Feedback

[官方v1](https://arxiv.org/html/2604.19024v1)，实际§2.1–2.2、§3.1–3.2、§4.1–4.2及§5；未遍历全部证明附件，不声称形式证明复核完成。2+1+2=5，安全理论必要深入，拟仅报告。有限CMDP/完整tabular参数化、Slater feasible policy、已知可逆/Lipschitz preference link下，以成对差加absolute harmlessness one-bit anchor恢复目标；相对偏好不给绝对constraint阈值。NPG或zeroth-order perturbation、clip后inverse link与primal-dual更新避免拟合RM，但仍依赖反馈/链接/锚点合同。

界含优化T、反馈M与γ^H truncation，目标为分布期望discounted utility及平均constraint，不是逐response/trajectory的hard安全。实验只有10states4actions、γ.9/H80、M16/64/256及模拟BT反馈，非真人LLM服务；LLM硬件/precision/上下文/SLO不适用，未复现。Ch31已有relative score、proxy/硬约束分权，但不把该算法称精确Existing。本次保“绝对锚点+continuing horizon”的受限理论比较，尚无LLM稳定部署配方，5深入Only待独立终态。

四项作者必要证据/actual owner比较已完成，60→64工作家族；三gap仅提案、一Only待独立，本日I12，18892实际写后仍待root。普通队列和日级Gate继续，不冻结分母。

## 后续四项必要审阅：19141 / 19147 / 19149 / 19162

四项复用原162完整题摘，实际读取official HTML-v1必要方法、决定性实验/局部附录及abs身份说明，不遍历全部附件/版本史。早v1 Updated依次04/22T00:37:03Z、00:37:30Z、00:37:37Z、00:38:33Z/OAI均Apr22，与官方slot、连续ID及邻界支持08～09有界推断；submitted只作provenance，Updated不是first-public日志。未见本组官方撤回标记，不宣称全站查撤回。

### 2604.19141v1 — Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation

[官方v1](https://arxiv.org/html/2604.19141v1)，实际§3.1–3.3/Eqs3–4、§4.1–4.4/Figures3–4/7–8/Tables1–2、AppA.1、B.1–B.2/AlgS2。2+2+2=6，拟Ch24具体训练状态support gap深入。独立patch时刻使最大时刻接近clean，即使均值平衡也可能始终给较干净上下文，不能据此保证纯noise部署起点受训。LTG先采最大时刻再限制其他patch时刻；difficulty head以ground-truth velocity误差NLL/stopgrad训练，DualLoop按难易推进再对齐。difficulty是误差代理而非校准uncertainty；shared full-model forward的固定NFE不证明逐patch kernel成本消失。

Fig8相关.11→.52不是开放校准；PF+REPA+Lookahead FID2.00差于SiT+REPA1.96。随机ordering主实验退步与AppA某threshold轻微改善并存。ImageNet256、130/458/675M400k步/50kFID样本，以及T2I1.2B120M recap COYO、不同encoder/AE/分辨率recipe有限，非全comparator配方matched。hardware/precision、完整wall-clock/online batch/concurrency/SLO未绑定；新增head/异步管理/训练成本保留，未复现。actual Ch24约679、760–810已有corruption/cache与difficulty原则，窄差异是训练控制信息最大值不能以均值替代及异构状态support必须覆盖部署起点。拟唯一MULTIMODAL-GENERATIVE-PARADIGMS / Ch24，保代理失准/同步uniform fallback；待非作者采用，不写Books。

### 2604.19147v1 — Nexusformer: Nonlinear Attention Expansion for Stable and Inheritable Transformer Scaling

[官方v1](https://arxiv.org/html/2604.19147v1)，实际§3.2–3.3/Eqs3–14、§4.1–4.3/Tables1–2、§5.1–5.3/Tables3–4及直接AppC/D初始化说明。3+1+2=6，中心增长桥纠错深入，拟窄争议暂缓。QKV为GeLU(GeLU(XW_M)W_A)W_D，Eqs12–14/§5.2新增M/A通道与cross-block均零。GeLU(0)=0：新增D行梯度乘零的新A activation；A old→new列经零D反传、A new→old行乘零M；新增M经零A新行反传。因此按打印普通fresh梯度所有新增块为零，fresh零moment AdamW不因decay而激活。initial function preservation并不推出AppC新增梯度非零/可学习扩容。此有限代数反证待独立核，不宣称实际代码没有bias/扰动/非零耦合/继承optimizer-state或实验造假。

经验保留：8×A800、context4096/global batch1M tokens、100B预训+30B增长、170～640M；41.5%是300M目标PPL预算比较非全compute。Nexus170M平均41.71低于TokenFormer42.04、240M43.73低于43.91；增长440M45.88低于380M46.35非单调。R²=.658/NOC rank-overlap不是普遍增长/orthogonal知识保证，precision/服务SLO ND，未复现。actual Ch14 QKV与Ch17梯度可作后续owner，但不采用“全零新增块可学”。只隔离中心桥，保nonlinear QKV局部比较与初始function equality。重开需精确初始化/optimizer-state补充及新块非零梯度/受控学习依据，不无限追发表史；待root非作者窄争议裁决。

### 2604.19149v1 — How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns in Thinking LLMs for Quantitative Reasoning

[官方v1](https://arxiv.org/html/2604.19149v1)，实际§3.1–3.2/Table1、§4.2–4.4/Eqs1–8、§5.1–5.9/Tables3–8与必要设置。2+1+2=5，标准拟仅报告。answer→trace attention构造centroid/diagonal/anchor；GPT5/Gemini3标注trace质量/关键span，以正确池/错误池按SRQ各取极端80%形成CAA，再分别干预answer/reason阶段。SamePool控制池大小、几何/语义消融支持受限selection，但正确性/trace质量/reading共同被选，不是holding content固定的纯reading因果操控。

Table1正确差trace12与错误好trace3表明非必要充分；AIME6.6pp是四题小cohort，Eq9 max-prob非频率校准真值。white-box attention/API标注/steering成本、hardware/precision/完整预算/concurrency/SLO ND保留，未复现。actual Ch5约180–240可读/使用、Ch66 trace/信心authority已分一般对象，不称整个算法Existing；保局部selection证据，没有稳定通用reading controller，不写Books，待非作者Only处置。

### 2604.19162v1 — Mind the Unseen Mass: Unmasking LLM Hallucinations via Soft-Hybrid Alphabet Estimation

[官方v1](https://arxiv.org/html/2604.19162v1)，实际§4/Eqs1–6、§5.1–5.3/Tables1–3/AppB。2+1+2=5，标准拟仅报告。n5～50采样经DeBERTa NLI成semantic class，用Good–Turing missing-mass与normalized Laplacian heat trace估支持，再按coverage融合。N100 pseudo-oracle是操作reference非真实alphabet，shared dev β/α/τ与pair-NLI/spectral成本保留。Eq5文本subtract/打印加项不同，pi*=k_obs·p_hat/estimated_support一般和≠1，故不称真实完整alphabet Shannon entropy；不据局部口径否定经验或自动全家族争议。

MAE改善不推出AUROC全面更好，Table3 n8/10有plugin/NumSets更高mean AUC。OPT6.7B/Qwen3/Mistral7B/Phi3.5与五QA受限，CoQA未列对应AUROC；硬件/precision/length/batch/concurrency/SLO ND，额外n生成/N100 reference不免费，未复现/代码未验。actual Ch66约340–365有限样本/rare failure及1822–1842低熵相关错已有一般边界，但非精确算法Existing；保小n估计/排序证据，缺开放风险保证，仅报告待独立核。

64→68必要工作家族，一gap提案、两Only、一中心桥争议，实际I12不变；18892实际写后仍待root。原162/515范围未扩，不冻结分母。

## 后续四项必要审阅：19201 / 19234 / 19254 / 19295

四项来自原162完整题摘范围；19201旧库存摘要尾部截断，已以官方HTML的完整摘要补足，不将截断摘要算完整初筛。实际使用exact-v1必要方法、主要表和直接相关限制。早v1 Updated依次为04/22T00:41:25Z、00:42:49Z、00:44:31Z、00:47:04Z，OAI当前日期并非都Apr22（19234为Apr28）；与已核公告slot/连续ID/邻界共同支持08～09有界归属推断，不改名为首次公开日志。当前abs版本说明定点核，19234/19254后发版本不回填本窗；未遍历版本史，未见本组官方撤回说明。

### 2604.19201v1 — Cascaded Code Editing: Large-Small Model Collaboration for Effective and Efficient Code Editing

[官方v1](https://arxiv.org/html/2604.19201v1)，实际§3.1–3.3、§4.3–4.4与§5.1–5.3/Tables4–7。2+1+2=5，标准拟仅报告。强模型给编辑草稿、弱模型把草稿应用到原代码；apply阶段承担长上下文、多文件、未改区域保持和格式对齐，不能因模型较小而视为简单无损操作。CLC从短到长/多文件训练，GCLC加入通用代码任务；118280训练与1981合成benchmark以repository分离，DeepSeek过滤及两位作者的人类检查不等独立复现或所有泄漏均排除。Aider Pass@2包含反馈后第二次尝试，非两次独立采样；CodeBLEU/ExactMatch不能替代功能测试。

质量和成本不是单向优胜：DSV3 direct Pass@2=56.0高于14B cascade54.2；DSR1 67.6→75.1改善，作者wall-time27.31h→23.80h/计价6.54→5.32。强阶段token减少时，DSV3总token仍357.1K→522.7K增加。强模型16×H20/SGLang、弱模型1×H20/vLLM，训练8×H20/BF16、batch32、8192/16384长度3epochs；不同模型/执行池与DeepInfra单价不构成统一硬件下的通用成本定律，online concurrency/SLO及完整训练成本ND。CLC→GCLC的合成EM79.0→77.6退步而DSR1下游Pass@2=73.3→75.1，Pass@1=39.6→39.1，说明局部文本保持与带反馈任务成功是不同目标。

actual Ch56 cascade/quality与Ch78内容保持/effect gate已经承载阶段验收和总成本不能只看强调用的一般责任。本次保两阶段训练目标及作者受限排序反转，不称整套算法Existing，也无须再给成熟cascade原则新增一个产品分支；仅报告待非作者处置，未复现。

### 2604.19234v1 — Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation

[官方v1](https://arxiv.org/html/2604.19234v1)，实际§3.1–3.4/Eqs1–15、§4.1–4.4/Tables1–4。2+2+2=6，因process信用与多目标保证边界作必要深入，拟仅报告。时间权重由相邻latent与最终latent余弦相似度差截断加epsilon、再沿时间归一；目标系数c_k^i没有t下标，实际advantage为w_t^i乘样本级多目标融合，因此是可分离的时间代理×样本目标权重，不是各目标独立拥有一条时间信用分配。固定样本中各目标梯度共享policy方向，Eq11标量min-norm形式可成立；不能把这个局部形式升级为跨样本/全部参数/clip后更新的真实Pareto或因果信用保证。exploration混合也改变原min-norm目标。最终latent相似度和reward instruments不拥有独立视觉真值。

FLUX.1-dev/Wan2.2-T2V14B、图像8×H100/视频32×H100；50k Dance prompts、1k图像test，图像train512/20steps与infer512/50steps、视频train336×592×53/12steps与infer480×832×53/50steps不同。Table1 Aesthetic6.6028低于Dance6.8917，Table4完整方法ImageReward1.1998低于TCD-only1.2618；MOCA-only Aesthetic6.2120低于base6.2508，并非各目标全部提高。precision/完整训练compute、服务length/batch/concurrency/SLO ND；相似度、多个reward及搜索成本保留，未复现。

actual Ch33生成器内部状态/Typed Credit Boundary已经分开step proxy、真实过程反馈与无偏或因果归因；Ch31多目标融合也不承诺目标一致。本次保可分离代理设计及具体反向结果，不把这个受限权重配方自动写成长期新分支，亦不以Eq11的局部合法性否定经验或将全家族争议化。6深入Only待非作者裁决。

### 2604.19254v1 — ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning

[官方v1](https://arxiv.org/html/2604.19254v1)，实际§3.1–3.4/Eqs1–9、§4.1–4.7/Tables1–2和必要AppA/B/D。2+2+2=6，拟TRAIN-LORA / Ch30状态化适配资产gap深入。shadow backbone跨base深度复用，但每层injection/projection与gate/update权重并非全部共享；s_l将既有shadow state与当前base hidden信息组合，再用二者差经random-down/zero-up瓶颈注入base。初始函数保持与可学习通路分别验收，auxiliary shadow CE也有独立监督责任。它不是能直接merge进固定线性weight delta的普通LoRA。部署需绑定base revision、shadow权重、layer coupling/schema、初始状态及attached执行模式。

detach得到的是shadow s0/独立head的另一个预测器，不是把依赖base hidden的深度更新凭空在无base下运行，也不保证与attached模型功能等价。Table1 random-shadow detached36.09 vsattached76.92、预训.5B shadow detached62.11 vsattached77.11；预训额外FineWeb/Wudao各100k、454M可训练参数等不是同训练预算。2×A800、Qwen.6/4/8B、五次均值但无对应CI；SQuAD .6B80.54低于LoRA80.75/DoRA80.91，20News8B76.99低于LoRA77.03，更新消融在GSM明显但Amazon几乎不变。§4.6十次平均延迟3.7～5.9%不是完整tail/SLO，precision/完整长度与在线batch/concurrency合同ND，未复现。

actual Ch30 Recurrent Launch State约365–385有权重/prompt之外的固定S0适配面，Merge与动态Adapter段区分资产；尚未承载随层深根据base hidden演进的shadow state及attached/detached两个非等价artifact。拟在这一主线补最窄责任分支：固定launch state不能替代depth-conditioned动态state，不能按可训练参数少推导可merge或等价脱离base；保额外backbone/coupling执行成本、状态reset/层schema变更失效及显式LoRA/S0共存。仅source→owner提案，未独立采用/未写Books，不预支整合。

### 2604.19295v1 — TEMPO: Scaling Test-time Training for Large Reasoning Models

[官方v1](https://arxiv.org/html/2604.19295v1)，实际§3.1–3.4/Eqs1–12/Alg1、§4.1–4.5/Tables1–2、§5–6。2+2+2=6，因测试时更新与critic反馈来源边界作必要深入，拟仅报告。unlabeled问题用于policy更新，但critic周期性在labeled D_L上用当前rollout的outcome监督刷新；terminal V作reward、prefix V作baseline，不能写成没有标签/外部反馈的自我改进。variational identity在真实P(correct|x,y)条件下成立，不证明learned V在更新后的policy分布中等于真条件概率或ELBO已tight。Eq11 baseline读取包含当前action的prefix，不采用无偏token因果信用保证；§6本就未给形式收敛证明，不能据缺失保证否定全部经验。

D_L含DAPO17k数学/12.8k DOLCI一般任务；PPO初始化actor/critic。AIME24/25/Beyond用于test adaptation，AIME26/OlymMath是heldout；BBH/AGI/Zebra与heldout GPQA分开，不能把所有列都称独立未知任务泛化。Qwen14B AIME26 Pass50.0→46.3、Olym51.6→50.2退步；Qwen8B GPQA平均37.2低于TTRL41.1。frozen-critic对照支持该recipe局部刷新收益，不严格匹配更多critic训练compute。≤8B batch256/mini64、14B128/32、max length16k/dual-clip GSPO；硬件/precision、完整训练计算/在线concurrency/SLO ND，未复现。

actual Ch31 Candidate distribution随policy变化的RM数据闭环与Ch33 value scorer版本/OOD已经承载刷新一般机制，Ch80明确反思不等参数适应。这里保测试时policy/有标签critic两条数据流和局部反向结果，不称此整套算法Existing，也不只因它换成test-time而默认新增章节机制；6深入Only待非作者有限处置。若后续证明真实新状态/恢复合同，再定点重开Books判断，而非全篇或全版本扩审。

68→72必要工作家族：三受限Only、一Ch30窄gap提案，实际I12不变；18892实际写后仍待root。原162题摘/515宽库存范围未扩，不冻结分母。

## 后续四项必要审阅：19300 / 19321 / 19330 / 19398

复用原162题摘；19321原最小消歧通过同层数selection与allocation反向对照确有值得保留的局部证据，非因新selector名字准入。official abs/v1身份与当前说明定点核，19330晚v2不回填v1；早Updated00:47:12Z、00:48:28Z、00:49:39Z、00:53:59Z及既有slot/连续ID/OAI邻界支持本窗08～09有界归属，OAI current不是first-public。未见本组官方撤回说明，未完整版本史扫描。

### 2604.19300v1 — HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models

[官方v1](https://arxiv.org/html/2604.19300v1)，实际§3.1–3.3、§4.1–4.3/Eqs1–5/Tables4–6与直接AppendixA/C/E。2+1+2=5，标准拟具体已有覆盖。准入是最小audio/prompt扰动配对、缺证据肯定与有效问题误拒分母不同，而非5720任务规模本身。两annotator+senior三轮核audio/question/reference，少数分歧discard；2662contrast、621invalid/adversarial，三次运行均值非所有切片CI。原文任务定义区分capability error与hallucination，评价中accuracy仍混一般任务错；不能把所有错误都当无grounding生成。Eq4打印整体binary accuracy而文字又称按预测类conditional，Eq3的布尔条件形式及实际解析器需分别辨认，不能拿未清分母组合唯一幻觉率。

AppendixE lowercase/去标点/keyword Yes-No、数值抽取、拒答词表是measurement layer，不能假设所有解释或多次数字均正确解析；FRR Eq5 valid-prompt refusal不等有害肯定/内容捏造。Table4–6模型在不同domain名单不同，overall不支持同一完整cross-domain排序。AppendixC1000条paraphrase的均值0.7pp不足证明全部wording invariant或模板无bias，保未报告CI/分层差异。不同LALM/API版本、音频时长/采样、hardware/precision/batch/concurrency/SLO未统一披露，未复现。

actual Ch66约466–468已分blanket refusal/应拒控制/内容级伤害与risk tier，约335–345 EvalSpec绑定backend/parser/参考，后续paired intervention也保存任务与response分母。采用“grounded回答正确性、有效query误拒、无证据肯定及parser误差不能相互代替”的一般命题已有真实承载；不是整套HalluAudio已实现。拟PLATFORM-EVALUATION-SYSTEM / Ch66具体Existing，待非作者必要处置核，不新增Books。

### 2604.19321v1 — RDP LoRA: Geometry-Driven Identification for Parameter-Efficient Adaptation in Large Language Models

[官方v1](https://arxiv.org/html/2604.19321v1)，实际§3.2/Alg1、§3.6–3.7/Eqs3–4、§4.1–4.3/Table2与§5。2+1+2=5，标准拟仅报告。从input样本hidden trajectory到多resolution RDP pivots、1/sqrt(t)投票及velocity混合，离线冻结layer priority；参数free/training-free只指selector不需训练，不等没有forward/calibration/epsilon search或K/beta选择。几何转折是proxy，不识别causal bottleneck或语义真值。

rank32/alpha64、相同训练协议的Qwen3-8B MMLU-Math中13层selected81.67高于random13层75.56及FullLoRA79.32，而geometry-weighted78.20/reduced79.23不优于uniform selected；因此选择身份与容量分配要拆分，不能说加大importance权重必然更好。单run、单benchmark、跨模型附录概括无主表逐配置/CI；K是chosen sparsification而非被证明无超参数，matchedlayercount不等所有执行预算严格matched。hardware/precision/length/batch、总训练时间和SLO ND，未复现。

actual Ch30 target modules/rank段已明确最优位置依赖任务、base和budget，动态层probing分支拥有selector代理与额外成本；但不称RDP算法Existing。保受限选择×allocation反向对照，不为几何importance实现另加成熟原则正文，5Only待独立核；未因单模型或负面结果关闭。

### 2604.19330v1 — Text-To-Speech with Chain-of-Details: modeling temporal dynamics in speech generation

[官方v1](https://arxiv.org/html/2604.19330v1)，实际III-A/B Eq1、IV-A–G/TablesI–V。2+2+2=6，MULTIMODAL-GENERATIVE-PARADIGMS / Ch24时间粒度生成接口 gap 深入，实际写入并经 root 非作者写后复核通过。不是只沿RVQ residual-codebook refinement，而是DAC首codebook的token时间轴先4×decimation、再2×、最后完整86.13Hz；同decoder在各level读取前一级及text/speaker条件，逐level masked refinement。训练抽level并腐化上一层10%，分别应对coarse-condition误差；decoder参数共享不等跨level计算免费或粗状态与细状态可互换。

摘要免explicit phoneme duration不能照写为无时长预测：III-B/Fig2仍先用G2P+duration估计utterance length，IV-A明列六层256hidden duration predictor。可说局部phonetic planning由粗token序列承担，但其因果和总时长模块替代未做充分控制。TableIV1→2→3levels WER7.67→5.19→4.88支持该recipe的时间层级选择；TableV共享/独立新增codebook8.48/7.03较decimated4.88差，说明更复杂tokenizer不是自然更优。主表4～10秒LibriSpeech、LibriTTS/3297h英MLS与SeedTTS有限，SeedTTS large2.73差于MaskGCT2.62；参数少与不同训练数据/架构不能证明同compute或全部音质最佳。20steps/level、batch256/400k训练、CFG/noise schedule、44.1kHz绑定；hardware/precision/RTF/streaming延迟/SLO ND，MOS方法被提及但未以完整可核MOS结果证明“更自然”，未复现。

actual Ch23约220音频语义/声学side-channel是representation分工，Ch24现speech interleaving以及多尺度生成原则未具体承载“temporal downsample首codebook”和“residual codebook层级”是两种不同条件链。已在Ch24语音生成邻段最窄补此factorization及total-length predictor仍需保留；保coarse错误传播、逐level forward/CFG成本、过短层token少于phoneme限制与单level/独立semantic-acoustic方案共存。实际写后复核通过，见 [root 独立复核](../V3_ROOT_CH24_TWO_WRITE_AFTER_20260928.md)。

### 2604.19398v1 — GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models

[官方v1](https://arxiv.org/html/2604.19398v1)，实际§3.1–3.2/Eqs1–6、§4.1–4.4/Tables1–5、直接AppendixD/I相关控制。3+1+2=6，中心每步预算保证纠错深入，拟窄争议隔离。FFNchannel/KVgroup以parameter-footprint proxy统一成本，gate probability排全局prefix、hard forward/soft STE backward、冻结base；固定mask后scale calibration并slice/fold成dense checkpoint。STE surrogate不是mask最优梯度或全局knapsack optimum，parameter预算不等latency/实时KV总cap。

中心打印规则有具体guard反例：§3.2先prefix至B，再将全空FFN/KV group最高p置1，未描述再平衡扣款。两组A={a1,a2},B={b1}、cost各1、budget2、score .9/.8/.1时prefix保a1/a2成本2，保护B再加b1成本3；可行a1+b1成本2确存在，因此不是故意给不可行minimum预算。这个有限反例只否定“此打印组合始终budget feasible”，不推实际code无补偿/全部实验失真。重开需明确protected组预算预留/再投影规则或实际mask-cost检查，当前不采用hard cap保证。

经验保留：A10080GB/BF16，512×512 Wiki calibration、batch1/4epochs/noAdamWdecay；主LLaMA2-7B及其他LLM表。Table1 .8retain PTB48.18差于FLAP36.94，PIQA.7405<.7465；score p vs p/c在同budget/固定learnedutility的allocation控制支持受限不同排序，而不证明p全局最优。scaling可降PPL却微降平均taskaccuracy；Table9 GSM8K高稀疏近0能力退步保留。weights/KV/peak B4/T256/2048是有限测量，sorting0.11%不是所有mask/训练成本，decode/concurrency/tailSLO ND，未复现。actual Ch49稀疏artifact/kernel admission一般责任不能拿来洗掉中央预算未证；不写Books，6窄D暂缓待root独立核，不否定其他有限机制和经验。

72→76必要家族：一具体Existing、一Only、一Ch24窄gap、一预算桥窄D。I12不变，18892actual仍待root；原162/515范围不扩，不冻结分母。

### 2604.19405v1 — Lost in Translation: Do LVLM Judges Generalize Across Languages?

[官方v1](https://arxiv.org/html/2604.19405v1)，实际§3.1–3.3、§4.7/Fig4、Limitations/A.6。2+1+2=5，标准拟具体Existing，待独立核。视觉内容固定但query/answer翻译不等语义严格等价；LaBSE/Comet阈值、回译/重译影响接受集合。A.6约200例英语回译审查不是25语言全部native审核，另有Bengali300例局部native核验。OpenCQA的GPT-5 reference有同源偏差，跨judge相关不证明真值。

§4.7更换三种translator时Qwen3-VL32B平均68.8→64.4→58.1，跨语言方差也变；有限排名稳定不证明绝对分数来自纯judge能力。22模型/各任务的pairwise accuracy、位置/长度/JSON解析分别测，hardware/precision/length/batch/concurrency/SLO未统一披露，未复现。actual Ch66约925–931已要求跨语言task/label/parser identity、transformation lineage、native review，且不能互换分数；采用这条长期命题已具体承载，不称完整benchmark实现。拟PLATFORM-EVALUATION-SYSTEM / Ch66已有覆盖。

### 2604.19440v1 — What Makes an LLM a Good Optimizer? A Trajectory Analysis of LLM-Guided Evolutionary Search

[官方v1](https://arxiv.org/html/2604.19440v1)，实际§3.1–3.3、§4.2.1–4.2.3、§5/Limitations。2+1+2=5，标准拟仅报告。固定初始population/Top20%父选择，15模型/8任务/30generations×10offspring/每组合两次/temperature .7。prompt优化、TSP/binpacking支持search-operator测量，不因symbolic子任务恢复AIforScience。

NN novelty由edge-set/embedding/function-grid分别定义；breakthrough依赖fitness improvement，与最终fitness相关不能识别唯一原因。换model还改变其他latent特性，作者明确难隔离local refinement；保zero-shot相近但轨迹不同、novelty非稳定结果代理，不采“增加多样性必无效”或最佳local策略。相同calls非相同tokens/价格/wallclock，API成本为估算，硬件/精度/长度/并发/SLO未统一披露。actual Ch79约169–188已有heuristic/budget/verifier主线；未给可直接采用的新controller，不称trajectory算法Existing，保局部证据Only待独立核。

### 2604.19444v1 — Unsupervised Confidence Calibration for Reasoning LLMs from a Single Generation

[官方v1](https://arxiv.org/html/2604.19444v1)，实际§3/Eqs1–4、§4/Tables1–2、§6、A.1代码/A.2评价。2+1+2=5，标准拟Only。离线100次采样（temperature .7/TopP .95/TopK20）估answer频率，modal response作proxy监督；StandardScaler/Ridge和另一数据划分的isotonic，部署读取单response embedding，也测外部Gemma3 embedding。不用gold训练非零离线成本/非真实正确率保证。

九模型/五任务/36组合，exact-match、ECE/Brier/AUROC及语言/数学/QA shift；Table2 QA ECE2 .134/Brier .232是平均而非任意新域保证。§6承认需重新离线采样，一致错误可继承，未测开放互动/多轮。vLLM生成/辅助embedding与regressor仍耗算力；hardware/precision/length/batch/concurrency/SLO Not Disclosed，未复现。actual Ch66 learned-confidence与1822相关错误段已有proxy≠truth原则，不称ridge/isotonic算法Existing；保离线摊销实现Only，不另造通用release置信保证，待独立。

### 2604.19459v1 — Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning

[官方v1](https://arxiv.org/html/2604.19459v1)，实际§2–3、§4.1–4.3/Tables3–8、AppendixA直接限制。2+2+2=6，formal-verification保证边界深入，拟具体Existing。Lean检查给定axiom下proof，不能验NL规格真值；two-stage的locked仍允许stage2改axiom、事后diff flag，不是硬不可变锁。

303题/两模型/temperature1/三run，unified最多三编译修订、two-stage每stage三次，非同总调用预算；定向双方向/不同fewshot另分账。stage-diff能抓新增axiom，却漏stage1已错但自洽翻译（Case177）。Table6 107fabrication按609+300 pooled记录，过滤后105分析/88unique，不能混为独立任务率。LLM judge有FP/FN、正确样本抽检非完整faithfulness；未见systematicgaming非证明不存在。actual Ch66约3279–3283要求spec-validity先于proof，1244–1246分sensor/semantic authority，具体已承载采用命题，不称整evaluationExisting；hardware/precision/length/并发/SLO未统一披露，未复现，待独立核。

四官方abs当前均v1、题名一致，轻量页未见撤回/勘误提示不证明全标记不存在。缓存v1 Updated=04/22T00:54:16Z、00:56:51Z、00:57:25Z、00:58:14Z/OAI Apr22，仅联合slot/连续批次支持08～09推断，不等first-public日志。76→80必要家族，I12不变；两E/两Only仍待独立，原162/515不扩，未冻结。

### 2604.19125v1 — Do Emotions Influence Moral Judgment in Large Language Models?（历史拟候选，现前分母关闭）

[官方v1](https://arxiv.org/html/2604.19125v1)，实际§3.1–3.4、§4.1–4.3/Table3。2+1+2=5，标准拟仅报告，待非作者处置核。并非因道德任务标签准入：相同被评动作的正负情绪包装出现系统方向偏移，remorse/relief又有逆valence例外，四位人类的方向不一致，提供语言框架与评价对象不能混为一谈的受限反证。GPT5.1选择情绪/模板，包含“Out of…”的动机暗示，保持文字动作不证明所有道德相关语义严格不变；不能把它当纯情绪因果干预或所有偏移都是不应发生。

2026-09-28 重判：上述评分与仅报告处置是历史草案，不再计入本日候选。root 非作者重读完整题摘、Social-Chem/ETHICS 设置与情绪措辞对照后确认：这是一项可成立的局部道德接受度行为评价，但未提供本项目大模型/Infra 长期机制、可复算平台 release contract 或具体设计选择的新边界。family-specific pre-denominator closure；保留身份、原审阅与反证，不把其作为零分、Books 或正式日报候选。若后续实质修订给出可迁移的评价/发布边界，才定点重开。

Social-Chem contested4678、ETHICS hard1008、七模型，独立1–7 ratings；人类仅100情境×三版本×四人，1200评分不是1200独立情境，也不证明人类普遍免疫或规模唯一解释。remorse可作为悔意信息，数据关联/模型家族差异不能识别训练因果；contrast flip是四变体排序变更，不是所有生产二元决策翻转率。完整hardware/precision/length/batch/concurrency/SLO Not Disclosed，未复现。Ch66现paraphrase/source变换有效性与Ch31alignment代理已有一般框架，原文没有足够依据改变通用道德决策或部署规则，保具体受限测量Only，不把新benchmark等同新长期owner。

### 2604.19167v1 — LBLLM: Lightweight Binarization of Large Language Models via Three-Stage Distillation

[官方v1](https://arxiv.org/html/2604.19167v1)，实际§3/4.1–4.3、§5/Tables1–6、Limitations及必要B/C存储与速度口径。2+2+2=6，标准拟Only，待非作者核。准入是同W(1+1)A4下joint layer distillation发散而先weight/bitmap、后activation参数refinement可行的具体约束，不是低bit新名字。PTQ提供初始binary W与group bitmap；WAT保持activation FP16训练W/G与quant参数，AAR固定W/G再训练quant/clipping/knee参数。部署一bit权重加一bit bitmap是约二bit编码，不是全artifact纯一bit；scale及embedding/norm仍有高精度状态。

LLaMA1/2/3及局部Qwen、8192×2048训练样本、单H10080GB/CUDA12.8，Table3 DT=NAN与WAT/AAR窄对照支持阶段选择，不证明sequential是所有量化的理论必要条件。平均common-sense54.91仍低于FP16 63.71，ARC-e/BoolQ也未全面优于BWA；Table12 GSM23.43与D.2正文37.42冲突，不采用该具体优越性。B/C内存公式只算linear weights并含bitmap/参数，不是全服务resident/KV峰值；Table9矩阵计时未绑定完整batch/length/concurrency/SLO，不采端到端倍率，统计独立seeds不足。Ch49已有artifact格式/辅助参数、质量与实际kernel分责；本篇是受限准备配方与joint-error失败证据，尚不足改变一般执行选择，不称全部算法Existing，不新增Books。未复现。

### 两项最小消歧后的前分母关闭

- [2604.19400v1 CASCADE](https://arxiv.org/html/2604.19400v1)：完整题摘后实际§4两阶段与§6.1 Table2决定准入。由同一documentation生成tests及替代implementation，原实现fail/新实现pass是已有生成式cross-check，p2f/f2f停用减少误报，但未提供独立spec-truth桥；71错误/814一致Java和PFP是局部工具证据。没有足以改变当前大模型评价/执行责任的新失效条件或设计选择，不把实际发现bug的应用收益扩大成长期贡献。贡献前关闭，不评分，不冒称已核所有发表史。
- [2604.19431v1 CTLF](https://arxiv.org/html/2604.19431v1)：完整题摘后实际§2–3定义与§5。已知事件空间/固定reference分布的有限world枚举与删输出计数，将偏差表示成新逻辑算子；实际generator分布估计、加权transition和在线识别仍future。没有新的可验收大模型机制/有效性边界桥，不因逻辑名称或toy生成语境扩大准入；仅此贡献关闭，不断言逻辑本身无学术价值。

19125/19167官方abs当前v1同题、页面无可见撤回/纠错提示；原v1 Updated分别00:36:01Z/00:39:03Z，OAI Apr22，与已核公告slot/连续身份簇联合有据推断08～09，不作为独立first-public时刻。80→82正式必要家族，另两具体前关闭；I12不变，原162/515不扩，分母未冻结。

## 后续四项必要审阅：19090 / 19145 / 19238 / 19245

均复用原162完整题摘。早v1 Updated分别00:33:34Z/00:37:27Z/00:43:09Z/00:43:21Z，与已核公告slot、连续批次与邻项OAI合用推断本窗08～09；19238缺OAI、19245当前OAI为次日，不能把这些字段改名为精确首次公开，也不能因当前OAI晚一天自动迁日。版本污染按本组必要命题定点处理，不展开完整版本史。四项尚待非作者有限处置核。

### 2604.19090v1 — Dual-Guard: Dual-Channel Latent Watermarking for Provenance and Tamper Localization in Diffusion Images

[官方v1](https://arxiv.org/html/2604.19090v1)，实际§3.1–3.3、§4.1–4.4/4.7，Tables2–3/6/10–11。2+2+2=6，保护行为深入，拟仅报告。准入不是“新增watermark”本身：reprompt保留初始noise的模型来源signal，却改变具体发行内容；双通道把model-of-origin与record-specific integrity分开。Full每图保存round-trip VAE latent约64KB及24bytes key/fingerprint，Lite无reference只是未同等实证的回退。被查image-record的闭集认证不等开放世界来源查询；key/reference未知的black-box威胁模型也不覆盖white-box联合自适应攻击。

SD2.1/512²/50 DDIM/guidance7.5，1000prompt冻结快照；220auth+220tampered校准后冻结threshold。4000 provenance样本按四种生成条件分组，2400攻击与1000+1000定位集不能混同分母。Table3局部攻击GS pass .995、dual pass .975不等最终localization拒绝；Table6 text-overlay recall .471是细stroke被VAE平滑的反例。Table10直接生成latent reference clean pass0，而round-trip reference .997，说明reference构建必须与verifier校准一致，不证明所有generated reference天生不兼容。三证据融合favor高recall，IoU .255/precision .273不能写成精确恢复全部编辑区域；完整hardware/precision/online batch/concurrency/SLO Not Disclosed，未复现。

actual Ch72约820–839已分metadata/watermark/detector职责，2682–2695明确key、transform、detector、攻击轨迹与不可变origin record；不是Dual-Guard算法完整已覆盖。保来源与内容完整性双anchor的局部实现和reference失效反证，仅报告，不因双模块产品组合自动追加长期正文。若独立核认为record-specific content anchor相对上述主线仍有真实缺口，按实际差异定点重开，不预支Books。

### 2604.19145v1 — ST-Prune: Training-Free Spatio-Temporal Token Pruning for Vision-Language Models in Autonomous Driving

[官方PDF-v1](https://arxiv.org/pdf/2604.19145v1)，18页首页/页眉April22，实际§3–4.4、§5.1–5.3/Tables3–7。HTML-v1当前正文页头August24不能作本窗版本；仅定点以PDF恢复，不沿晚稿。2+1+2=5，标准拟Only。MTP用patch时间方差/recency作soft proxy进入多样性选择，RSP按ring相邻view双向cosine估重复且独立保留各view单位；motion proxy非物理运动真值，feature相似非同一对象。temporal-first省后续bilateral预计算，spatial-first本身仍合法，不能写后者不可行。

同DriveMM/SigLIP/Llama3.1-8B，四驾驶benchmark，single RTX PRO6000、batch1、λ=.6/.8；Table3同时计pruning/prefill/decode，先encoder/projector剪可能打破原downsample形状，局部更快prefill不等端到端最好。10%token下DriveLM accuracy81.23→77.60、Lingo70.8→65.2，而部分Omni均值略高，不采全部任务near-lossless或物理控制安全。Table5两级预算乘法25%=50%×50%、10%≈32%×32%，不是普遍最优50/50；模块增量近似相加不证明因果独立。推理precision、完整生成长度/concurrency/tail SLO Not Disclosed，未复现。actual Ch23层位置/selector成本、batch/view身份、任务质量共同验收已是主线；这里保具体时空proxy/排序反例Only，不称完整算法Existing，也不因新局部selector默认gap。

### 2604.19238v1 — Allo{SR}²: Rectifying One-Step Super-Resolution to Stay Real via Allomorphic Generative Flows

[官方PDF-v1](https://arxiv.org/pdf/2604.19238v1)，本轮curl成功20页，首页arXiv:2604.19238v1/21Apr2026，必要pp7–10 §3.2/Eqs6–12、pp11–14 §4/Tables1–2已实际读取，Table2页14已视觉复核。原始临时文件`/tmp/apr22-pdf.fPpIb2/2604.19238v1.pdf`仅便于本轮peer复用，长期依据为官方URL；当前HTML/库存摘要和官方abs不同，不沿库存字句替代PDF。2+1+2=5，标准拟Only。

LR latent不是Gaussian source；Eq6按配对LR/HR的信号与residual二阶量选一个全局t*，是statistical proxy，不等全状态分布/预训velocity field support已匹配。Eq7单步Euler、Eq9–10配对插值velocity监督与Eq11–12共享参数的两条flow score alignment分别承担source、局部路径及distributional约束，不能从条件路径直线推实际marginal ODE精确或有限训练确保自然流形/无prior collapse。FLUX.1-dev，VAE/DiT LoRA rank64，AdamW、batch16、8×A100/10ksteps；95k训练图、×4恢复/128²→512²等有限配置。

Table2去ATM的RealSR PSNR26.17/FID100.54优于Full24.97/112.88，DRealSR FID121.75优于Full132.48，而若干NR指标相反；不照录所有metric协同最优。Table1也含重建/感知取舍。50–200×NFE下降不是wall-clock或real-time SLO合同，推理precision/batch/concurrency/完整时延未披露，未复现。Ch24约150–158已有trained source compatibility、276–280区分path straight与sampler；保受限SR目标/来源统计代理和反向质量选择Only，不将全部算法称Existing，不新写通用保证。

### 2604.19245v1 — Talking to a Know-It-All GPT or a Second-Guesser Claude? How Repair reveals unreliable Multi-Turn Behavior in LLMs

[官方v1](https://arxiv.org/html/2604.19245v1)，实际§4.1–4.4、§5.1–5.4及§7。2+1+2=5，标准拟Only。UMWP各2600 answerable/unanswerable，人工去89 ambiguous后answerable2511；五model先回答后受三种challenge，两轮2511/2600同题反复产生25555/76665responses，不能当同等数量独立任务。第三种alternative固定36，来自overall median而非逐题难度/尺度匹配；correct numeric gold与explicit nonnumeric/noncommittal两个不同评分合同必须分开。

challenge可修wrong亦可腐蚀correct，GPT在36诱导log-ratio近0而其他model正，不采所有模型均同方向；Claude unanswerable 1127次36不是独立无条件失败率。100人工 trouble-marker标签κ=.786、classifier75%只是受限sensor，语言风格分类.59→.85不识别内部repair机制；RLHF解释未干预验证。GPT4o、ClaudeSonnet4.5、DeepSeekR1-distill70B、Phi4、Mistral7B/API版本及表中配对分母保留；完整hardware/precision/token总预算/batch/concurrency/SLO Not Disclosed，未复现。actual Ch80开篇独立反馈/停止与65–83逐约束保留validprogress已有一般原则，本篇提供局部repair-profile而非稳定通用controller，Only，不称完整行为测试已经覆盖。

82→86工作家族，四项Necessary Review完成仍待独立，不冻结分母；18892已apr01实际write-after PASS，当前真实I13，不因其余仅报告自动逃避非作者审阅。
## 最后一组原有限信号：十项必要审阅与一项前分母关闭

仍属于原162完整题摘范围，没有新增raw或从515宽库存派生全文队列。以下10项拟纳入工作表，86→96；19395具体前分母关闭，不评分。该集合尚待来源、日期、否定侧及非作者终态复核，**不是冻结分母**。本次逐项实际打开当前官方abs并核必要exact-v1正文，未见决定处置的撤回说明；这不是另行证明不存在撤回/纠错。早v1 Updated原值如下，与官方slot、连续ID及已有邻界/OAI联合有界推断，不改名首发日志：19264=00:45:20Z、19267=00:45:34Z、19292=00:46:56Z、19301=00:47:14Z、19334=00:50:02Z、19342=00:50:31Z、19395=00:53:56Z、19438=00:56:35Z、19457=00:58:13Z、19461=00:58:21Z、19473=00:59:14Z（均2026-04-22）；19461没有当前OAI，需以邻界联合审而非孤字段定时。

### 2604.19264v1 — DR-MMSearchAgent: Deepening Reasoning in Multimodal Search Agents

[官方v1](https://arxiv.org/html/2604.19264v1)，实际§3.1–3.3/Eqs2–11、§4.1–4.3/Tables1–5。2+2+2=6标准，拟仅报告。新增的是跨batch rollout结构位置对优势的乘性重加权，以及按正确/错误的工具次数Gaussian reward，不是因出现Agent就准入。G×T列归一化后到正/负理想点距离产生Fi、A'=A(1+Wi)；A=0不能由这种乘权变非零，跨prompt及长度分布会改权重，未识别因果step credit。BGAS由gold正确性分流，summary refinement不是真值。Qwen2.5VL7B/verl/B128/8rollouts、max14轮、2epoch；3602 QA，T3 57.7→59.7(data)→60.8(BGAS)→63.4(SPAI)→64.9(both)→66.8(refine)，160/200/225 steps非同总compute，N10%低于5%。Ch33同prompt baseline与正确子集辅助/完整group分账已有原则；此局部重权配方尚不足以新增稳定credit设计。hardware/precision/完整长度/concurrency/SLO ND，未复现，待独立处置。

### 2604.19267v1 — Multimodal embodiment-aware navigation transformer

[官方v1](https://arxiv.org/html/2604.19267v1)，实际III-A–F/Eqs14–25、IV-A–D/TableII/Discussion。2+2+2=6保护行为深入，拟仅报告。机器人width/length、视觉/LiDAR与goal条件生成候选，再由LiDAR/waypoint/尺寸的clearance head排序；门槛、无safe候选时max-min、goal masking/恢复形成局部控制分支，但预测clearance不是collision证书。Husky/ZED2i/Ouster/Orin、三Isaac环境各100goals、.5m/碰撞/10min终止；98h/35数据并有目标平台额外sim，环境zero-shot不等全部sensor未见。TableII经典TEB-Elev在部分环境成功率更高且零碰撞，full在一环境低于LiDAR-only；real85/15的样本n未披露。Ch26实际goal/dynamics/embodiment、生成候选与物理monitor主线已分权；只保尺寸条件ranking局部证据，不把实现全称Existing或保证安全。precision/完整输入长度/batch/concurrency/controlSLO ND，待独立。

### 2604.19292v1 — Location Not Found: Exposing Implicit Local and Global Biases in Multilingual LLMs

[官方v1](https://arxiv.org/html/2604.19292v1)，实际§3/4/5.1–5.2。2+1+2=5标准，仅报告提案。44语义平行问题×12语言/49locale组成2156条locale-specific QA，不是2156独立模板；16annotator双审。BUS以US答案包含率减collision-aware uniform baseline，BR是gold匹配，不是部署人群公平目标。Gemini2.5Flash judge、GPT5mini交叉检查与80人工92% agreement只证明受限grader；32models、base/instruct配对3-shot。答案multiplicity与global bias r=.95但regional r=.47/p=.146，不能归因训练；语言提示不等locale明确指定是具体测量差异。Ch66派生翻译身份/原生验证原则可复用，但不能称这一新切片实验已完整Existing；保诊断，不写通用修复。hardware/precision/长度/batch/concurrency/SLO ND，待独立。

### 2604.19301v1 — Large Language Models Exhibit Normative Conformity

[官方v1](https://arxiv.org/html/2604.19301v1)，实际§3–5/AppendixA设置。以下为此前2+1+2=5标准Only的必要源审阅，**现已由[root非作者准入复核](./V3_ROOT_19301_REVERSE_ADMISSION.md)改为贡献前关闭，不再计正式候选或评分**。Apple/Banana的初始偏好由prompt赋予，named/anonymous、未来评价/继续关系、endorsement与无关衣色作对照，A/B互换平均、每条件120生成。六模型温度/maxTokens异质，四模型publicness增强、其他模型无响应/局部反向；Llama70B-AWQ首token residual余弦仅观察关联，不能识别人类动机或唯一规范机制。无客观gold的社会呈现变量确会改变受限群体输出，但没有独立信息流、行动提交或新的controller；Ch82已有协作、channel framing、相关错误与独立verifier/commit责任。hardware/完整预算/concurrency/SLO ND；此处保留原证据作为改判审计，不否定论文局部价值。

### 2604.19334v1 — Silicon Aware Neural Networks

[官方PDF-v1](https://arxiv.org/pdf/2604.19334v1)，实际5页短文pp1–4 III-A/Eqs2–4、IV/TablesII–III。2+1+2=5，数值冲突受影响内容深入，仅报告提案。可微逻辑门的概率×standard-cell面积进入loss，再argmax成gate-level netlist，代理面积不等最终route PPA；部分逻辑映射需多cell。SkyWater130nm/Cadence低drive library/post-layout模拟，非已制造芯片；wiring约束使6×64k变18×4k。MNIST准确98.04→97.66、面积缩小，CIFAR准确60.07→58.82同有代价。TableIII 15ns/352pJ与IV-C 23.9ns/2.0nJ不一致，83.88mW÷41.8M确约2nJ；16nm FO4只外推。不采用统一latency/energy倍率，也不否定训练cell-aware目标本身。当前Ch49数值artifact→physical plan主线不能由这局部小分类macro改写普适部署判断；精度/请求shape/B/concurrency/SLO不适用或ND，未复现，待独立。

### 2604.19342v1 — Are Large Language Models Economically Viable for Industry Deployment?

[官方v1](https://arxiv.org/html/2604.19342v1)，实际§3–5.2/Tables1–2。2+2+2=6标准，仅报告。PTQ/QLoRA的局部能耗/质量工作点与break-even公式是可检查材料，不采用无条件部署经济性。双T4/16GB、Llama/Qwen、PEFT r16/alpha32、FP16/INT8/INT4、vLLM.6.3/B1/100requests、100ms NVML、20runs；模型列表8B/表7B及1.5B/表1B等口径需保留。Nbreak=(train+setup)/(API−infer)需正节省，API费率与等质量/SLO未绑定；IPW作者任务复杂度代理不是通用成本排序。device NVML/VRAM密度不含host/全容量，intro/Table能耗倍率不同，不合成统一优势。Ch70实际负载/idle/有用成功/host-device成本正文已经承载一般选择，本篇具体局部配方只作报告，不假称完整算法Existing。长度/concurrency/tailSLO ND，待独立。

### 2604.19395v1 — 前分母关闭：Self-consistency 的 subject 切片未改变选择责任

[官方v1](https://arxiv.org/html/2604.19395v1)，实际§3.1–3.3/4.1–4.3/Limitations，完整题摘已读。MMLU subject-level knowledge/reasoning标签为启发式，SC3–20与CoT比较；知识切片5-sample 87.85对CoT87.12只.73pp但增加调用，SC20 Med77.41反低于SC5 77.67，consensus/correctness相关.4不是校准。Ch20实际majority/diverse-errors→external verifier链已明确更多samples需coverage/可靠selector；材料新增的是该成熟方法在一个混合subject分组的局部工作点，未提出新的筛选机制或足以改变既有有效性判断的边界。故具体前关闭而非因医学或负面结果拒绝；不评分、不列候选、不追完整发表史，待否定側代表性独立抽核。

### 2604.19438v1 — Malicious ML Model Detection by Learning Dynamic Behaviors

[官方v1](https://arxiv.org/html/2604.19438v1)，实际§2.5/3.1/4.2–4.7/5 Tables5–10/6。2+2+2=6保护行为深入，仅报告提案。按model-task tag聚类后以Docker/strace加载的syscall presence/frequency训练OCSVM，具体task-dependent profile边界值得报告；top2000 likes不能成为无恶意真值。n2-highmem4CPU32GB/python3.10、25k主要synthetic，真实malware25/4/17与feature13/17检测分开，不能将25k称真实攻击；text/classifier/feature 200+200分层。无anti-debug假设、不可覆盖未列/低人气/别hub/逃逸，不由正常trace推合法执行。Ch72实际模型文件反序列化/隔离builder/sandbox/固定digest正文分开sensor与发布权限；本配方未给新的充分防御，不声称全部Existing。precision/LLM请求长度/生产SLO ND或不适用，待独立。

### 2604.19457v1 — Four-Axis Decision Alignment for Long-Horizon Enterprise AI Agents

[官方v1](https://arxiv.org/html/2604.19457v1)，实际§3–6.5/7。2+1+2=5标准，仅报告。新增受限enterprise决策测量：factual retention、causal reconstruction、response/abstention分开，摘要事实正确不等decision正确；gold先合成再LLM造doc/人工审，不保证真实机构独立效度。Stage2同10case×3budget=30，agent/judge同Haiku4.5；5case sprint与DPM5+10+10不作大样本。BM25 raw chunk缺事实使比较反向，不据此否定所有raw memory；VM2/10 commit虽两次均对，过度abstain不等安全保证，Summ10/10对不能隐藏。Ch66 outcome/protocol与Ch77 typed-retention原则已有；只保局部失败/成本诊断，不写成普遍memory机制或正式四轴正交。hardware/precision/完整matched-budget/concurrency/SLO ND，待独立。

### 2604.19461v1 — Involuntary In-Context Learning: Exploiting Few-Shot Pattern Completion to Bypass Safety Alignment in GPT-5.4

[官方v1](https://arxiv.org/html/2604.19461v1)，实际§4.1/4.4/5.1–5.4/6.1–6.7。2+2+2=6保护行为深入，仅报告。把有害内容换抽象operator framing、穿插良性few-shot的具体攻击对照成立，不采用普遍alignment失效或induction-head因果解释。abstract58对direct0，interleaved76对harmful-first6，benign数量14/36/76/56/94非单调；operator任务50/50与HarmBench24%[18.6,30.4]两个目标分开。3479=1550 ablation+220 HarmBench+10 detail+1699 ten-model，不是同分母全GPT5.4。judge GPT4.1mini0–4/harmful flag与探索后选择最优配置不等独立heldout；temp46–56/p=.891不证明等效，未验证工具effect。当前Ch72结构化context/pattern与独立action权限原则继续；本地攻击recipe只报告，不声称所有context攻击均已算法覆盖。硬件/precision/完整长度/B/concurrency/SLO ND，日期邻界仍待日级核。

### 2604.19473v1 — TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation

[官方v1](https://arxiv.org/html/2604.19473v1)，实际§3.2–3.4/Eqs1–11、§4.1–4.4/Tables1–4。2+2+2=6，确认知识缺口触发深入；已在Ch24运动条件后落实完整prompt下按frame×subject/event interval局部消费条件的窄增量，[root实际写后非作者复核](V3_ROOT_19473_WRITE_AFTER.md)通过。全文prompt仍是共同text context，event intervals由user/GPT4mini/均分分配；subject mean-attention/erosion3是区域proxy。早denoise T2V20%/I2V40%对cross-attention pre-softmax bias按时段的verb和subject-frame query调整，不是删其他text或后验/物理保证。Wan2.1/2.2、CogVideoX、单A100、480×832/81frames、StoryEval423；GPT4o/Llava72B judge、I2V首帧由QwenImage重写生成。Wan2.2 48.3→56.2且仅EAM51.9；846→863s含平均GPT分段2.65s，多段baseline81×n不是严格等负载。现Ch24原有帧/chunk提交、静态condition prefix身份与跨模态条件接口有一般原则，新段补足“同一full prompt、不同frame query按subject×event interval作局部条件消费”的窄分支；保mask误定位、分段失误、temporal cost/quality和原full-context无bias回退。precision/B/concurrency/tailSLO ND，未复现。

## 原162题摘集合对账：首五项必要审阅恢复

此次是原记录尚未完成的具体潜在信号，不新增515宽库存或题摘数。早v1字段与既有slot/连续ID联合推断仍待日级日期核；不以Updated单独证明首次公开。五项均等待有限非作者裁决，不预签Books或整日Gate。

### 2604.18587v1 — Compile to Compress: Boosting Formal Theorem Provers by Compiler Outputs

[官方v1](https://arxiv.org/html/2604.18587v1)实际§3.2–4.3、§5.1–5.4/Tables2–6：refinement消费当前problem、失败proof和带行号compiler信息，不累积完整失败历史；该信息有损，非已证明充分统计量。value来自成功路径顺序/失败分支相对root标签，不等校准成功概率。Kimina8B/Goedel32B、采样预算64/128/256下存在局部收益与退步；refine19.4k/22.4k和direct37k/43k训练量不同，样本预算不等总token/编译/value成本。Ch75任务相关保真/原文回退、Ch79 canonical state与完整trace分责已承载一般判断；局部compiler-conditioned recipe仅报告，不宣称整个算法已有覆盖。2+2+2=6标准；hardware/precision/B/concurrency/SLO未取得披露，未复现。v1 Updated=04/22T00:00:08Z，无本库存OAI直接项，早邻界仅作联合推断。

### 2604.18660v1 — Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial Student Attacks

[官方v1](https://arxiv.org/html/2604.18660v1)实际§3.1–3.3/4/5.2–5.3/Table3：攻击器自己给答案与tutor泄漏是两种失败，不能据弱prompt攻击低泄漏推防御稳健。训练1000 GSM8K对话/LoRA3epoch、测试240题/至多10turns；Qwen7B攻击器、六tutor及选定跨域，Llama70B judge先digit过滤、两类各30人工校准κ=.88/.81。Table3微调攻击使三个pedagogical模型tutor leakage升高，但judge同源/条件检测及教学效用未匹配，防御降低泄漏不证明教学质量或普遍安全。2+1+2=5，保护评价触发深入必要范围；Ch66攻击预算和trace/outcome原则保留，受限攻击/防御配方仅报告，不写教育应用通则。hardware/precision/完整length/B/concurrency/SLO未取得披露；未复现。v1 Updated00:01:58Z/OAI04-22联合推断。

### 2604.18718v1 — Towards Optimal Agentic Architectures for Offensive Security Tasks

[官方v1](https://arxiv.org/html/2604.18718v1)实际§4–6/Table1/Limitations：同20个Docker目标、5topology×3model×2source-visibility=600core，另60stress不混入。ground-truth非LLM verifier区分partial与动态validated；whitebox只开放同目标source。SAS更便宜/快，独立多Agent更高validated，whitebox置信区间重叠，不能推出单一最佳topology。M1Max/64GB/remoteAPI、2并发/1800s外限/300s工具限；不同拓扑多调用本来不是同总compute，post-hoc路由不作为独立部署验收。2+1+2=5标准，仅报告这个受控排序/代价反证；实际Ch82协作/verification成本与Ch66机会/结果分账覆盖一般命题，非该算法完整Existing。precision不适用本地CPU编排、provider推理precision/SLO未披露；未复现。v1 Updated00:04:05Z/OAI04-22联合推断。

### 2604.18803v1 — LLM-as-Judge Framework for Evaluating Tone-Induced Hallucination in Vision-Language Models

[官方PDF-v1](https://arxiv.org/pdf/2604.18803v1)实际pp6–9/14–18，23页已解析，临时复用`/private/tmp/apr22-18803v1.pdf`；必要身份与数字对照不展开版本史。800图×5tone固定图/任务、9VLM，rule H-Rate与image-blind GPT4omini severity分账；审后只717/800符合设计，但主结果明确仍用全部800，不把717写成最终实验分母。Table2和紧随Overall ranking的InternVL/DeepSeek均值冲突，headline统一排序不采用；保非单调局部tone证据，synthetic absence不能自动成为逐图truth。2+1+2=5，评价/数值纠错触发深入；仅报告受限控制与测量边界，不据此写通用因果或安全率。hardware/precision/长度/B/concurrency/SLO未取得披露，未复现。v1 Updated00:10:21Z、当前OAI04-28晚更改仅provenance；归属仍由早字段/邻界联合待核。

### 2604.19354v1 — Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Capture The Flag Challenges

[官方v1](https://arxiv.org/html/2604.19354v1)实际§3.1/4/Table3/5/6.2及§6记录：原最小消歧的“仅新CTF任务”不足，3summarizer×4judge的受控表确实提供测量边界；Grok summary四judge均负κ，换judge不恢复已丢证据，但60trace人工一致性不证明全开放trace效度。10model×10CTF×3run、60step/default provider；writeup checkpoints不等全任务success，tokencost不同不冒称等compute。§6一例target VM停后agent继续host活动，已由作者停止并patch，但未披露可采用完整防护实现；只记录episode边界失败，不外推发生率或修复充分性。2+2+2=6，具体保护失败触发深入必要范围。Ch66 extractor/最终judge分责、Ch82 immutable archive/按需segment已有一般原则；局部交叉评价和失败案例仅报告，非完整系统Existing。hardware/precision/B/concurrency/SLO未取得披露；未复现。v1 Updated00:51:11Z、OAI05-07仅晚元数据，早邻界联合待核。

### 19540 最小贡献关闭与19503/19533日期保留

19540[官方v1](https://arxiv.org/html/2604.19540v1)实际§3.3–3.4/4：CAT7固定字段、role相似性bandpass、content hash/parent-ancestor lineage DAG、receiver remix属于已知memory admission/provenance组合；14波生产观察/线缆capture未给新受控失效或有效性变化，具体前分母关闭，不因日期晚而拒绝，也不追发表史。

19503 ReaLB v1 Updated04/22T01:01:28Z/OAI05-12、19533 CyberDefenseBenchmark01:03:44Z/OAI04-24均晚于截点，仍有具体贡献线索但本窗归属未证；不列确定候选、不评分、不写Books。前者需该版本09:00前官方公开依据，后者需同类公开依据及必要log/QA协议正文（HTML本次不可取）；可由带日期官方公告/项目原始公开事件补核，定点重开各家族，不要求恢复全年。

## 原162题摘的最后七项必要处置

同一原始有限信号集合，不扩515宽库存。七项均实际核官方v1必要方法/关键对照，当前表为工作判断而非已冻结候选；早字段与slot/连续ID/OAI仅联合有界归属推断，仍待独立日级核验。五Only、一窄D、一具体Ch5普通提案，不把所有算法都写Books；无单篇/日级预支PASS。

### 2604.18804v1 — Geometric Decoupling: Diagnosing the Structural Instability of Latent

[官方v1](https://arxiv.org/html/2604.18804v1)。精确v1 §3.1–3.5/4.1–4.3/5/6及Appendix I。random-subspace有限差分Jacobian、主方向旋转LC与其Laplacian方差PHFE是操作代理；同seed normal/OOD的相关性改变不证明语义失败由曲率引起。§6.1/Table9 的SD3.5设计集为500 Normal＋500 OOD，LC/PHFE AUROC .816、裸LC .427、LS .199；“annotation-free”仅指推理评分不需逐图标注，AUROC仍须设计集的Normal/OOD标签。Appendix I 明确Jacobian估计成本妨碍实时使用、未显现结构失败时指标不触发。SD3.5/FLUX有限样本中LC–PHFE相关下降；Base/Turbo更换训练pipeline而非单独操纵曲率，作者也承认还需专门训练干预。5分中心因果主张必要深入；仅报告局部诊断，不作普遍root-cause/发布sensor。未复现，配置不足不补造；[apr20 有限非作者审阅](./V3_APR20_THREE_18718_19354_18804_INDEPENDENT.md)在本补证后通过，非日Gate。原v1 Updated00:10:28Z/OAI04-22。实际方法的LS为子空间log谱，LC为邻域主方向旋转，PHFE为投影方向高频方差；三个都不直接拥有semantic truth。§4.1配对500与4.2两池900/子采样500分开。Base/Turbo不是仅曲率改变，保观察、隔离摘要结构根因的因果外推；无需追全附件。

### 2604.18842v1 — Multi-Domain Learning with Global Expert Mapping

[官方v1](https://arxiv.org/html/2604.18842v1)。精确v1 III-A–C/Algorithms1–2、IV-B/G/H/J。LP affinity/capacity→静态domain/class map不同于在线token质量保证，DINO/ViT有限结果可保留。原m=n=2例不符合III-B的m>n，已被下述有效域例替换：m=3、n=2、c=(2,2)，w行(1,0)、(1,0)、(0,1)，唯一LP最优的三项均1，L=ceil(log2 3)=2。Algorithm1 b(k)=floor(x*2^L/2^(L-k)) mod2对x=1所有位0，无fallback，返回全零而OPT=3；完整assignment/Eq6任意ε<1和Eq9效用桥不成立。Algorithm2有未赋值fallback，是另一流程，不能反补Algorithm1。6分纠错深入，仅隔离这组保证，不断言实际code同错或否定有限经验。原v1 Updated00:12:22Z/OAI04-22仅作联合日期原字段。apr01必要原文/有效域反例有限非作者通过，见V3_APR01_FOUR_19071_18842_DISPOSITIONS.md；重开需明确所运行算法、端点1处理及对应证明。hardware/precision/完整成本与线上SLO未取得，非日Gate。

### 2604.18845v1 — Dual-View Training for Instruction-Following Information Retrieval

[官方v1](https://arxiv.org/html/2604.18845v1)。v1 §2–4/Tables1–2。同文档正负对在互补instruction下交换标签，DV替换等量样本，不把双视角当完全等总训练成本。305M gte/bge-m3、30hard negatives、512长度、温度.02；100生成样本单annotator审后无进一步filter。Ins-DV改善pMRR而general Score21.33→19.73/InstructIR89.16→87.97，混合数据才部分兼顾。5标准，仅报告标签控制与取舍，不宣称所有语言/检索任务最佳或全部合成标签可靠。 原v1 Updated00:12:35Z/OAI04-22；Qwen3Next80B合成监督、480k和880k两种匹配对照分开，更多数据上下文与指令反转不是同一因素。Ch27具体synthetic/目标混合原则与Ch76 query语义/排名责任可解释一般条件，本配方仅报告，不假称整个算法已Existing。hardware/precision/B/concurrency/SLO未取得披露，未复现。

### 2604.18867v1 — Hierarchically Robust Zero-shot Vision-language Models

[官方v1](https://arxiv.org/html/2604.18867v1)。v1 §1/3/Eqs10–16/Theorem1、§4/Tables3–4。把image/text hierarchy和PGD训练层级结合，leaf防御对superclass攻击的失配是实际保护边界；hyperbolic log-margin是固定角度/范数条件下几何量，不等输入空间认证radius。CLIPViTB32、ImageNet训练、14zero-shot集合、3-step训练PGD/20-step及CW/AA测试和半径分开。6保护深入，仅报告这条有限攻击/收益分支，不作全威胁覆盖或全规模VLAsafety承诺。 原v1 Updated00:14:19Z/OAI04-22。实际§3.3层级cross-modal loss、textprojection更新与Theorem1条件、4训练/测试setup已读。Theorem1中一般非零βc极限只依赖角度ratio，不能把特例βc→0的无穷margin推广为任意安全半径。主表均值收益保留，不混医学应用任务；Ch72 sensor/威胁切片与Ch23表示分权仍成立，不称该算法完整Existing。完整hardware/precision/B/concurrency/SLO未取得披露，未复现。

### 2604.18897v1 — Less Is More: Cognitive Load and the Single-Prompt Ceiling in LLM Mathematical Reasoning

[官方v1](https://arxiv.org/html/2604.18897v1)。v1 §4–9/Tables2–7。45+prompt在可见69/200/400标签split反复设计、子集筛选与全量结果不同，不能当独立heldout泛化或信息论上限。AN45c本地hard3 79.25%（n=400、Together AI bf16），但§9/Table7官方hard3仅55.5%（n=20、DeepInfra bf16），低于同官方无cheatsheet基线56.3%；题集/提供方/seed不同，不能将反转单因果归于prompt或服务提供方，也不能用本地79.25%称稳健增益。AN38官方65.3%仍只属该小样本配置。Gemma2048→8192 token的错误退出与模型能力分开；非单调和规则合并退步可报告，但§8的有限搜索不能证明任意静态prompt无法条件路由，normal recall不能推出hard任务92%理论ceiling。5分中心解释必要深入，窄Only不否定所有实测。原v1 Updated00:17:43Z/OAI04-22。actual4 provider/T0/长度、5表、6.3预算及8–9边界已读；少数n10/20价格/多模型均值不外推。难题自适应prompt搜索、rawprompt纠错重跑与较大split不可视为未见测试，undecidability也不约束此有限题集可达率。Ch74prompt竞争与Ch66选择/预算/测量分账已有一般论点，本经验Only不是全文Existing。root定点复核18867/18897/18942/19334本批后确认该Only限域，未复现实验。

### 2604.18907v1 — Gradient-Based Program Synthesis with Neurally Interpreted Languages

[官方v1](https://arxiv.org/html/2604.18907v1)。v1 §3.1–3.4/4.1–4.5，leave-one-out IO监督、primitive复用正则、Gumbel-codebook和共享循环executor；测试优化程序latent而非改executor权重，最终执行soft表示不宣称硬符号真值。三seed固定20长度Shift/Comp任务中base/先验search不能替代gradient search；去recurrence/interpreter离散化明显退步，DeepCoder新生11.6M与有gold程序baseline分开，LPN另有更强重排序。5分实际Ch5组合计算缺口触发深入，拟窄正文，待独立，不先计I。 原v1 Updated00:19:16Z/OAI04-22。actual Ch5‘compositional usefulness’与filler/role段区分表示绑定/可用性，却未明确‘训练学primitive/executor、部署只搜索program latent’这一替代分工。不是仅因为codebook名新就gap；受控分支对照改变如何把组合性放入架构与测试计算。温度退火/多起点和gradient steps有成本，不能称任意长度无界、程序唯一可解释或通用LLM编程胜出。准备两段literal在同节后提案，尚无共享锁；硬件仅TRC/Modal支持而完整model/precision/runtime/SLO未取得披露，未复现。

### 2604.18942v1 — Disparities In Negation Understanding Across Languages In Vision-Language Models

[官方v1](https://arxiv.org/html/2604.18942v1)。v1 §2–3/Tables1–2。COCO5914四caption选择翻译七语言，每语言仅30人审，不叫全量人工truth。英语τ=.92的SpaceVLM在Chinese/SigLIP31.9→12.4、Arabic/Multi40.6→34.5、Russian/Multi43.3→36.3退步；修复不是所有语言稳定改善。形态、脚本、训练频率未分离，不采用typology单一因果或重新训练建议已验证。5标准，仅报告这组修复迁移反证，主线不是仅新增benchmark。 原v1 Updated00:22:30Z/OAI04-22。实际compact全文核心§2/3已读；翻译/人审抽样、英文阈值和4choice分母完整。Ch23统一语义接口/跨语言校准与Ch66派生标签/切片原则已有一般边界，本地反证Only而非claim整个实现Existing。hardware/precision/请求batch/concurrency/SLO不支撑性能主张，未取得披露不补造；未复现。
## Books 提案的最小增量反向复查：Ch5 三项

2026-09-28恢复后作者实际顺读Ch5“compositional usefulness”、filler/role绑定、信息存在/读出/使用、参数移植与activation relay的不同对象及两侧内容。未重新读取未变化的必要v1附件，也未写共享正文。以下是作者侧反向建议，不是独立采用PASS，不改变表中当前未决状态或评分。

- **19052拟改具体已有覆盖：**现filler/role段已用“同词不同施受关系”区分语义内容与绑定、并限定角色方案、解绑定条件和行为泛化；本次只采用entity×relation索引不能压成entity语义相似这一一般认识时，这段已有实际承载。局部PLS坐标/合成domain的具体方法仍仅作论文证据，不把整篇算法称已存在。若拟采用更强的cell坐标机制，应先指出超过既有绑定模型的稳定新结论，而非因双索引名词没逐字出现就新增。
- **19117拟改具体已有覆盖或受限仅报告：**实际参数移植段已把参数单元充分性、activation relay、anchor恢复和最终行为分开，且明确粒度/上下文/冗余限制；probe证据阶梯也不以共享位置证明唯一机制。本次“共享位置不能推出同方向或同表达行为”的最窄采用被这些论点承担。相反方向zeroing的新反证可在Daily保留，不必另追加通用“granularity需分账”原则；非作者若确认仍有重要任务方向缺口再写。

**18907维持窄提案，待非作者判断：**compositional usefulness只说后续层组合，并未区分“训练学可复用primitive及executor”和“部署冻结executor、优化program latent”的机制分支。拟插该小节末两段，而非把程序合成方法写成框架手册：

> 当组合泛化成为瓶颈，端到端模型可以继续依靠数据与共享参数形成隐式组合，也可以把组合规则的表示与执行拆开：训练阶段共同学可复用primitive的连续codebook及共享循环executor；面对新输入输出例子时，冻结这些执行参数，搜索或优化程序latent来选择组合。这样把新任务适应从“重新改整套权重”转为“在学得执行语义中选择程序状态”；神经解释器的可微路径让输入输出误差能反传至该状态，但这不是模型已经拥有唯一的人类符号程序，也不是离散真值执行器。

> 这条分工用训练时primitive复用、循环执行及测试时梯度搜索的额外成本，换取有限任务中的组合泛化；多起点、温度与搜索步数都属于请求成本。受控Shift/Composition例子中，只增加递归或从先验采样并不等价于梯度搜索，部分重排序仍不如已有latent-program基线；固定可表达程序长度与训练语言也限制外推。任务无法由该语言表达、可微执行误差失配或预算不足时，仍保留端到端模型、外部符号验证及其他搜索方法，不能从这组结果推出任意LLM编程或无界长度能力。

该literal只源→owner提案，无锁、无实际写入、无独立写后核；不计I14。原v1 §3.1–3.4/4.1–4.5的训练/测试职责、有限受控消融及退步为必要依据，不追加无关附录。

## Books 提案反向复查：Ch24 五项

作者本轮实际对读ASR的CTC/位置接口两段、语音coarse/fine生成分支、训练support与off-trajectory纠偏、Few-step DMD coverage和energy-selected teacher target正文及相邻handoff，复用未变精确v1必要方法/反证；以下仍需非作者采用裁决，未改正式处置、未自授共享锁。

- **19009拟收窄为仅报告：**当前Few-step正文已区分student实际访问状态、teacher构造target与仅训练期energy选择target，并把energy偏差、diversity和额外compute纳入回退。若本次只采用“reward应评价构造的训练target而非早期raw sample”这一分工，它在既有target-construction/selection主线中成立。具体real/fake-score implicit regression及target-group正负policy可在Daily保留，不因为DMD实现未逐字列出就再追加一般target责任原则；若非作者认为其对蒸馏目标定义确有重要缺口，须采用更具体命题而非重复分权句。
- **19141拟收窄为仅报告：**当前训练support正文已明确synthetic/own-rollout状态的覆盖不同、局部correction不覆盖全部推理分布，并以off-trajectory校准和原sampler回退限制采用。最大patch时刻不能被均值替代，是LTG/DualLoop这组有限配方的重要具体反证；但一般“训练必须覆盖部署起点”并非现章缺失。保本局部采样/代理与负例，不把未逐字写max-statistic当必须修改长期知识；不因此删候选/分数或否定真实增量。
- **19079仍拟窄gap：**CTC整句重排/位置语言分布段目前是解码消费接口，而本文研究两个可见context模式下最终Transducer的完整(t,u)词表分布训练一致性；辅助CTC一致反会伤streaming RNNT，说明只在辅助输出head对齐不能替代实际decoder lattice合同。最窄新增是选择受一致性约束的输出对象，保双模式forward/kernel重算成本、短context退步与SM/pure-streaming回退，不写成普遍KL更好或免费推理。
- **19330仍拟窄gap：**现音频coarse-AR/fine-refinement只说粗细声学层，而时间轴decimation与RVQ residual-codebook层级改变的是不同条件对象；前者粗时序状态并未替代utterance-length预测。可在原语音层级主线用两段区分分解轴与各level状态/cost，保粗错误传播、单level方案和SeedTTS退步，不追加完整codec框架。
- **19473仍拟窄gap、需非作者确认重要性：**现camera/运动条件和stage schedule能承载条件控制的一般原则，但全文prompt保留、不同frame query按subject×event interval消费条件这一具体边界尚未出现。只能拟条件消费分支：interval/region是proposal而非真值，pre-softmax bias不是文本删减、joint posterior或物理因果。若原论证已足以解释其有限operating point，则可仅报告，不要求为该方法名强写两段。

以上两项反向建议和三项窄gap不是冻结或独立通过，仍位于同一16项普通Books队列。共同目标是核是否改变真实长期设计判断，不靠降低固定比例或追加paper列表让pending归零。

## Books 其余八提案：当前正文对读后的最小采用范围

本轮作者实际读当前各章具体段落及相邻交接，复用前面已保存的精确v1必要方法、主要对照和反证。以下不是独立采用PASS或实际写入；只缩小待非作者裁决的命题，普通队列仍为16项。篇名与新参数不是缺口理由，也不要求将整套方法写进章节。

| 家族 | 实际已有正文 | 拟采用的最小差异及边界 |
| --- | --- | --- |
| 18933 / Ch26 | Episode state段已有curator admission、history sensitivity与warranted choice分账；后段已有finite-horizon risk sensor | 本项不是首次读门或校准原则，而是以独立memory-on/off政策的action-error ratio离线拟合binary读门、冻结门后再训练完整policy。可以只补“读门的监督代理与最终policy必须分开验收”：比率不是同policy的因果必要性，history/action-noise支持、额外拟合成本和联合regularization反益就近保留。若该具体训练分支不足以改变正文设计判断，保持局部Only，不泛称全部已有。 |
| 18963 / Ch29 | Teacher选择、capacity/表示兼容、predistill基线、共同正确样本交集已有实际对照责任 | 狭义差异是让teacher本身成为先经校准的可更新监督资产，再分别验收teacher发布效用与student可教性。不同tokenizer评分文本不等逐token概率一致；utility/RKL反向与额外teacher校准成本保留。仅在该监督来源更新分支确有长期价值时补两段，不写undistillable或IP保护保证。 |
| 19033 / Ch28 | 逐样本残差Jacobian/伪逆、旧函数动量重投影已有 | 原文改变的是选择更新单位：先声明当前输出或衰减trace聚合的目标变化，再沿已选参数方向以局部导数反解scalar步长；不是另一个完整batch伪逆。仅拟在现坐标段前增加这条替代分支，保分母/非线性/旧tangent、action-dependent偏差与非KL-hardcap，不采用LLM预训练或长期稳定优势。 |
| 19047 / Ch66 | RAG pipeline阶段身份及receipts、Claim Graph的alternative evidence path和相关来源分组已有 | 相同information可能由不同chunk独立支持，固定document-ID gold不总是唯一truth；需把required information→可替代support映射作为benchmark identity，并区分部分并集覆盖与all-required覆盖。其LLM等价映射误差、atomization与预算影响保留，all-required不保证生成正确；不采用CRRF框架或E2E−PerfRecall作为参数知识因果量。 |
| 19083 / Ch72 | Projector软channel供应链、sensor与effect分权已有；现ETC段另负责扰动资产与恢复module依赖 | 窄诊断反证是全ΔW谱/单neuron统计阴性不否定matched clean/poison input的输出残差ΔE低维可干预结构。只在资产诊断中分开两个测量对象和行为干预，保需clean对应资产、rank非单调/utility退步与未知trigger，不采用norm普遍因果律或完整后门修复。 |
| 19018 / Ch31 | Prompt/当前token conditional actuator、feature组合失败及可撤销控制已有 | 本项不是首次feedback或安全authority分离。拟补offline局部层传输Jacobian→固定Riccati gain、online feature-error反馈的实现路线；层深horizon不等未来AR内容计划，linear setpoint不是语义真值，utility/TPS退步和Jacobian/gain/每token执行成本保留，超校准区回退。 |
| 19021 / Ch22 | GDN-2 channel decay与erase/write解耦、训练chunk recurrence与decode一致已有 | 新粒度不能直接继承旧并行代数：naive left-channel gate破坏原rank-one对称形式，双边key/value约束缩放保留DPLR/WY lowering。只补表达自由度×代数兼容分支，保投影/kernel成本、部分质量退步与标量gate/Attention共存；不重复erase/write从无到有或照录冲突hybrid比例。 |
| 19254 / Ch30 | Fixed recurrent S0 launch资产、Merge与attached adapter两种资产策略已有 | 新对象是跨层随base hidden更新的shadow state；固定launch state不等该depth-conditioned计算，detach后的预测器也不保证等价attached版本。只分开state/coupling/schema、attached/detached身份与额外backbone成本，保真实质量退步、reset/布局失效、LoRA/S0共存，不写可merge或更少trainable=更少总compute。 |

非作者可以据上述真实差异改判Only/Existing或授最窄写入；不能把本作者对读结论当独立PASS。当前不新增候选、评分、来源扫描或完整附件审阅。

## 关闭侧有限反向检查：六份题摘、三项最小机制消歧

本轮只复核原162题摘内18975/18976/19048/19055/19086/19124的完整题摘，并对18975、19048、19124补到决定贡献判断所需的机制与主要对照。没有扩展515库存、全文队列或版本史。下面是作者侧准备包，不是独立排除Gate；原筛选理由保留在V3_REVIEW_CHECKPOINT，必要限定在此纠正。

- **18975 [Gated Coordination](https://arxiv.org/html/2604.18975v1)：**实际§3.2–3.5/4.1–4.2及A.4确有事件状态、代价门、灰区裁决、冷却/局部回退和组件比较；不能将初筛的“摘要没有新条件”误写成论文没有受控证据。现Ch82选择工作视图、按需委派和coordination tax已承载一般控制分工；五类ordinal信号及其阈值组合给出有限Minecraft操作点，强历史惩罚还会漏升级。维持具体组合关闭建议，不采用绝对无死锁、near-zero latency或全场景最佳；若独立审阅认为这条冷却失败分支实质改变现有可行性判断，应只重开该命题。
- **18976 STAR-Teaming：**完整题摘的semantic-community采样减少重复攻击探索，但ASR/成本结果未建立新威胁覆盖有效性或攻击成功判定边界。保持受限黑盒搜索组合关闭建议，不因研究安全就自动入选，也不声称该论文无学术价值。
- **19048 [SAMoRA](https://arxiv.org/html/2604.19048v1)：**实际§4.1–4.3/Eq3–8及Table1/2；共享A、cosine专家keys、task scalar和正则是具体条件化adapter配方，不因router/scale名新就改变现Ch30已有容量/路由/初始化认识。作者初算LoRA≈89.3067有误，经apr01独立重算实际Table1同九任务等权均值为SAMoRA89.45、LoRA88.64，后者与打印一致；SAMoRA打印91.71未获解释。同支持集增益0.81pp而非打印3.07pp，且逐列最大1.60pp，共享非负归一权重不能单独产生3.07pp。纠错影响中心效用比较，因此撤销本项原前分母关闭，单项恢复为3+1+2=6深入审阅、仅报告可复算局部结果并隔离打印Avg；不据此称原始代码或所有单任务实验错误。需同分母聚合定义或修正表才重开该幅度，详见[V3_APR01_SAVOIR_NEXUS_SAMORA_INDEPENDENT](V3_APR01_SAVOIR_NEXUS_SAMORA_INDEPENDENT.md)。
- **19055 ATRIE：**完整题摘区分静态timbre量化、动态prosody flow及teacher蒸馏，但仅模块组合和persona指标尚不足建立新的codec接口、泛化失败或成本成立条件。保持该具体摘要关闭，不按speech/anime标签拒绝。
- **19086 MUCOCO：**完整题摘的语义保持mutation与多任务code一致性检查属于成熟metamorphic测试扩展；一致性提高不自行获得程序正确性或mutation等价证明。保持具体测试组合关闭，不采用15%为新的oracle有效性保证。
- **19124 [HSPD Detox](https://arxiv.org/html/2604.19124v1)：**实际§4.2–4.4/5.1–5.5及Tables1–2：差异logit干预、多温度候选、毒性classifier与embedding相似度重排后训练复用，确有局部对照，不写成无验证。Ch27当前data transform、语义保真和独立下游效用责任已明确；此配方的代理分数不能证明原语义完全保持或训练毒性单一根因。主表毒性降低同时diversity/部分任务效用退步，仍是已有治理原则的一种受限操作点。维持关闭建议，不采用fundamental suppression宣传；独立复核只需判断这些条件是否超出现有原则的真实边界。

六项都未以本作者检查自动签排除通过；19048中心比较信号、19124保护范围与18975设计失败边界需要有限非作者确认，其他三项题摘按理由抽检即可。无需将六项全送全文或全恢复候选。

## 四反向独立裁决后的三条 literal 提案

已实际读取apr01独立审计：19117仅报告通过，正式表同步；19052/19009/19141的一般覆盖理由未通过。以下三条保留其真实局部机制而非恢复泛化模板。源→当前owner独立依据为V3_APR01_REVERSE_FOUR_BOOKS_AUDIT；literal仍待root限定采用/授锁，未写Books、不计实际I。

### 19052 / Ch5，插现 filler/role 段后

> 多句话中同一实体可以同时参与多种关系，因此仅记录“哪个实体”还不够：一个受限机制假说把属性的绑定地址分成entity与relation两个索引。在受控文本中，以属性token的activation拟合这两个索引，继而只沿拟合子空间替换或扰动，检验输出是否按所选绑定改变。这比语义相似或角色标签多一步局部使用证据，但拟合出的cell不是网络拥有物理表格或唯一符号地址的证明。
>
> 同一关系结构跨语境也不保证沿用同一读出坐标。作者的有限两家族/合成域对照中，原投影跨context可能退化，按相同索引的activation差拟合translation后可以恢复部分读出；这增加配对数据与校准成本，并依赖上下文和干预范围。因而可迁移几何、局部行为作用与开放任务泛化要分别验收；坐标失配或patch连带改变其他功能时，保留行为测试和原模型，而不把probe升级为通用编辑器。

### 19009 / Ch24，插 Few-step DMD target construction 相邻处

> Reward评价生成样本与评价准备写入更新的构造目标，不是同一个接口。分布匹配蒸馏的一条分支把当前学生输出detach，再加入固定real-score与在线fake-score的差，形成stop-gradient regression target；将这个target经VAE解码，比较它与原样本的reward，才调节正负更新。这样把target生成器、评价对象与学生更新拆开，而不是让早期raw sample的低分自动否定准备采用的更新方向。
>
> 构造target仍是近似监督，解码reward也不是梯度正确性或人类偏好的独立真值。Fake estimator、VAE、分组和reward调用增加训练成本；受测SDXL指标并非全面优于teacher或其他后训练配方，同NFE也不等于相同总compute。估计器失配、target偏离可解码支持或效用回归时，应保留原DMD、普通reward后训练与独立质量检查，不承诺消除全部梯度冲突。

### 19141 / Ch24，插训练 support 两段后

> 把一个图像各patch的噪声时刻改成独立变量，会改变训练状态的联合分布。只平衡平均噪声，仍可能让几乎每个训练样本含有接近clean的patch；其他位置依赖这份信息时，从纯噪声开始的部署起点就没有对应支持。因此一条替代采样分支先选择允许的最干净patch时刻上界，再在更噪一侧采各patch，而不是只约束均值；上界不意味着每个有限样本都有patch恰好取等号。
>
> 这项支持控制与后续自适应去噪应分开验收。额外difficulty head只提供相对误差代理，让较易patch先推进以提供条件并不保证全场景有效；受测组合有FID反例，同NFE不等同wall-clock，训练head与异步调度也有成本。质量或成本不成立时，统一时刻、同步sampler与既有生成路径仍合理，不从一个proxy推出最优资源分配。

## 日期集合的机器一致性检查，非首次公开证明

实际对账早期正式108唯一ID全部存在本窗原库存且v1 Updated字段早于01:00Z：00:00:08Z～00:59:56Z；当时82项当前OAI为04-22、26项为其他/空值。这只检查现有组合推定的内部边界，不把任一字段改称first-public，也不是逐篇成功公告日志。批次邻界19485为00:59:56Z、19487为01:00:18Z；晚字段例外19503/19533仍隔离。官方slot、连续身份及原字段的联合推断须由独立日级日期审阅最终核；本作者不签该Gate。

19105 前分母关闭后的有界重算：正式表当时107个唯一工作身份，原库存对应的该项OAI日为04-22，因此当时81项OAI04-22、26项其他/空值；所有身份仍在上段已核的早字段范围内。随后18724反向恢复加入，**该阶段**正式108=81项当前OAI04-22、27项其他/空值（18724为后者）；再后的19053恢复使正式表成为109，该ID的当前OAI归属仍须同一日期规则核，不能把旧阶段计数写为最新终态。这一数量变化不增加首次公开精度，仍待非作者日期 Gate。

供独立日期抽核的27项非04/22当前OAI索引：原 replay receipt 的OAI字段为空12项：18587、18701、18724、18738、18747、18933、18995、19001、19021、19047、19238、19461；字段为其他日期15项：18655、18739、18803、18901、18951、18966、18970、18978、19092、19117、19234、19245、19330、19351、19354。这里的“空”只表示该份 receipt 未存该字段，“其他日期”可能是后续更新；两类均不作首发反证或免审依据。它们全部在本日早字段和已核身份序列内，仍须按官方slot、版本事件与可能例外作有界日级复核。

最新107项正式候选机器重算（19059、19342前关闭后）：§3提取107个唯一arXiv ID，107个均能在原515身份 receipt 定位；原字段 `v1_updated_timestamp_revision_metadata_only` 全落 `2026-04-22T00:00:08Z～00:59:56Z`，没有字段晚于01:00Z的正式候选。当前OAI字段含04/22的79项，其他或空的28项（其中空13项）；上段27项索引是此前108候选阶段快照，新增19053当前OAI为空，故变28项。本检查只说明候选集合与早字段、相邻ID批次的内部一致性，**不证明逐篇首次公告**；官方公告slot、连续身份及例外仍须独立日级核验。

本次102项正式候选的最新机器对账（覆盖上段107项历史快照）：102个ID均在原515身份 receipt 内，`v1_updated_timestamp_revision_metadata_only` 仍全部落在 `2026-04-22T00:00:08Z～00:59:56Z`；当前OAI列表里74项含04/22、13项为空、15项为其他日期。OAI为空/其他日期不自动推翻首次公告，v1 Updated也不单独证明首次公告；只有官方时段规则、连续ID边界、当前OAI及原版本字段的联合有界推断可交非作者日期Gate。本次对账不改变工作候选102、关闭66、日期隔离2的语义判断，也不将旧107的OAI计数当最新。

## 19018 实际写后终态

先前 19018 的 literal 是写前准备，不是当前待办。root 已独立重开 exact-v1 必要方法/反证，并对读 [Ch31 实际正文](../../../../../books/part-04-training-system/31-rlhf.md)及相邻论证；[实际写后审计](./V3_ROOT_19018_WRITE_AFTER.md)通过。正文明确离线按层局部 Jacobian/Riccati gain 与 runtime feature-error feedback 的两阶段责任、网络层深而非未来 token horizon，保留局部漂移、gain/在线计算、Gemma PPL 8.95→12.26 与安全 authority 边界。此项为真实整合，当前 108 工作集合中 23I/9E/67Only/4D/5 普通提案；日期/分母/整体独立 Gate 仍未通过。

## 19254 实际写后终态

先前 ShadowPEFT 的拟案不是当前待办。root 已定点核 exact-v1 §3.1–3.3、Table1 与 Ch30 固定 S0→Merge 链，指出初稿同层先后顺序可误读；现正文明确进入第 `l` 层时以已有 `s^(l-1)` 与 `h^(l-1)` 的差注入 base 得 `h^l`，然后更新 `s^l` 供下一层。经[修正后实际写后审计](./V3_ROOT_19254_WRITE_AFTER.md)通过。detached 与 attached 非等价、额外 shadow 执行与部署 schema/reset 责任保留；当前 108 工作集合为 24I/9E/67Only/4D/4 普通提案，仍未通过整日 Gate。

## 18907 实际写后终态

root 已定点重开[官方 exact-v1](https://arxiv.org/html/2604.18907v1)§3–4及 Ch5 compositional usefulness 主线，授权最窄写入；[实际正文写后审计](./V3_ROOT_18907_WRITE_AFTER.md)通过，并纠正初稿“连续身份”为离散 codebook 与端到端对照歧义。训练期 primitive 身份/共享递归 executor 与测试冻结执行器优化 program latent 分工现已入 Ch5，保自建有限程序语言、搜索计算与行为验证成本。当前 108 工作集合为 25I/9E/67Only/4D/3 普通提案；未签整日日期/来源/分母 Gate。

## 19105 贡献准入反核：从工作候选降为前分母关闭

本项并非只看标题或因“具身领域”标签排除。重新核[官方 exact-v1](https://arxiv.org/html/2604.19105v1)完整题摘、§III 两阶段接口、§IV-D1/Table II 与 Table III：先用RVQ motion token监督VLM，再冻结它条件化latent diffusion生成器；joint tuning 在同一Nymeria任务中语义检索较高、FID/脚滑较差，且训练时间差异很大。论文把这一结果解释为梯度冲突，但没有独立量测共享参数的冲突方向；阶段拆分、token监督、模型更新范围与总训练成本同时变化。作者结果作为受限 motion-generation 比较成立，不能推出新的通用语义/动作监督选择规则、物理闭环成功或服务成本边界。

实际对读 Ch23“理解与生成也不必被迫共享全部参数”段（约289–295行）已明确共享语义接口、独立生成 head、分阶段冻结/解冻、loss ratio、双路径成本和 joint pretraining 共存；Ch25 的状态/动作 outcome 分账及分治成本也不由本论文的新任务重写。EgoMotion 在单一 egocentric human-motion 任务上重组已知 RVQ语义桥与latent generator，局部指标不足以改本项目当前长期机制或评价合同；按《研究合同》§3把它记录为具体 family-specific pre-denominator closure。原题摘、方法、反证及 apr01 对局部 Only 机制的审读仍保留在本文件前段和既有独立审计；此次只重判准入门槛，不称论文无学术贡献或原实验无效。当前工作集合 107=25I/9E/66Only/4D/3普通提案，尚未冻结或获得日级非作者 Gate。

root 已按[单项非作者准入记录](./V3_ROOT_19105_FINITE_ADMISSION.md)重开官方 exact-v1 §III/IV-D1 和实际 Ch23，确认该项前分母关闭；这只闭合19105，不表示其余107项或日级 Gate 已通过。

## 三条原普通 Books 提案的实际写回与非作者复核

2026-09-28：19052、19009、19141 保留上方 exact-v1 必要方法、反证与 apr01 的 source→owner 反向校准。root 再定点核原文和真实 Ch5/Ch24 相邻论证后批准窄写；作者只改获锁的共享章节，并在每章完成后释放。root 非作者逐段顺读实际正文和前后交接，三条写后均通过；这些结论不是实验复现或整日语义 Gate。

- `2604.19052v1`：实际 [Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md) filler/role 后约175–177行；entity×relation 双索引的受限局部 patch 与跨 context translation 分开，合成域/PLS 不推出物理表格、唯一地址或通用编辑器。root 已核 exact-v1 §3.1–3.3、正文与 probe/causation 邻接，写后 PASS；章末 Review note 已同步。
- `2604.19141v1`：实际 [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 训练 support 后约107–109行；patch 最干净噪声时刻的抽样上界不等平均噪声，也不保证有限样本恰取该上界，difficulty/固定 NFE 不升级校准不确定性或 wall-clock。root 已核 exact-v1 方法/反例及前后衔接，写后 PASS；章末 Review note 已同步。
- `2604.19009v1`：实际同一 [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) Few-step target 选择链约1135–1137行；从 detached student 输出构造 implicit target，再解码评分，不把 reward 当目标梯度真值。fake estimator、VAE、target group/reward 成本和反向质量结果就近保留；root 核 exact-v1 与段落邻接写后 PASS，章末 Review note 已同步。

当前107个工作家族的作者侧处置为28实际整合、9具体已有覆盖、66仅报告、4窄争议；普通 Books 采用待办0。107尚未冻结为最终候选分母：来源、日期、负侧抽检及其他未完成的单篇独立终态仍须由非作者日级验收，不能将本节的三个写后 PASS 写成全日 Complete。

## 邻日报日期反查：2604.19857v1 不归本窗

04/23 宽库存提出 [2604.19857v1](https://arxiv.org/abs/2604.19857v1) 的日期重核；其 v1 submitted `2026-04-21T17:21:08Z` 落本日时间窗，但 submitted 不是 first-public。定点核 [arXiv 官方历史月列表](https://arxiv.org/list/cs.LG/2026-04?skip=1500&show=50)：本日末段 `2604.19485` 是 item1501，`2604.19857` 是 item1530；该页面只有 **April 月标题，没有逐日公告 heading**，只能证明身份顺序，不能单独证明哪天公开。[官方 OAI 19857 GetRecord](https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai%3AarXiv.org%3A2604.19857&metadataPrefix=arXivRaw) 当前 datestamp `2026-04-23`、仅 v1；同入口 `19485` datestamp `2026-04-22`，紧邻 `19856` 也为 `2026-04-23`。[旧 replay receipt](../arxiv-owner-replay-20260903/20260423/arxiv-owner-receipt.json) 的 `v1_updated_timestamp_revision_metadata_only=2026-04-23T00:02:42Z` 与 DataCite created `2026-04-23T01:51:45Z` 同向；这不是 arXiv API Atom 的 `updated`（后者仍显示投稿时间）。当前 OAI、replay Updated、DOI 任一项都不是单独的公告日志，且有别篇后续更新造成 OAI datestamp 漂移。

按 [arXiv 官方规则](https://info.arxiv.org/help/availability.html)，ID 在公告时分配，常规美东周三20:00对应北京时间04/23 08:00，提交可因审核延期。上述官网月列表身份顺序、仅v1的官方 OAI 日期、原版本字段与常规公告槽联合支持 **04/23 08:00～09:00 北京时间的有据批次推断**，不支持从04/21投稿时间将其迁入04/22。因历史月页没有可逐篇定位的日公告 heading，04/23 的独立日期 Gate 仍应核能否接受此范围推断或维持其 Date Hold；19857 仍保留在04/22旧515条**日期未清洗的宽库存**作为审计痕迹，但不计入本日现有170份题摘、109工作家族、评分或Books，不处理其中心理论争议。

## 原宽库存的定点负侧重开：2604.18724v1

原始515个身份并非515个正式候选；现有162份完整题摘筛选记录之外仍有标题浏览后未展开摘要的身份。旧 `screening-ledger-final` 的排除标签不构成V3证据，因为其中还错误排除了本日已实际整合的家族。作者对这部分标题中可能涉及模型/Infra评价合同的项目做有界反向抽检，发现 [2604.18724v1](https://arxiv.org/abs/2604.18724v1) **Beyond One Output: Visualizing and Comparing Distributions of Language Model Generations** 不应仅凭标题前关闭。官方 [exact-v1 正文](https://arxiv.org/html/2604.18724v1) 的核心是把多个生成样本的分支与重复片段汇成 token graph，同时保留原始输出路径；它改变的是评估人员检查生成分布时可见的证据界面，而非模型的生成分布本身。§6.2 的受限配对实验中，graph 改善相对多样性判断（均值准确率差 +0.12、95% CI 0.03～0.21），但原始列表更适合单分布细节（graph 差 -0.057）及细粒度双分布比较（graph 差 -0.10）；三类任务不能合成“图表总体更好”。§8 明确实验室界面、样本量增长后的 graph hairball、未测混合界面与生产部署边界。

当前 Ch66 已分开样本、分布与校准结论，但未明确“压缩后的分布概览 vs 可回查的原始输出”这一评价证据界面取舍；可能是窄幅 Evaluation owner 增量，也可能只是局部 HCI 操作点。作者仅把该家族列为**前分母重开、待非作者贡献准入与日期归属**，尚未评分、纳入107正式集合、提出 Books 写入或宣称整体负侧已闭合。官方 abs-v1 的 Submitted=2026-04-20T18:22:31Z 与原库存 v1 Updated=2026-04-22T00:04:21Z 只作 provenance/批次佐证，不单独证明首次公开；需与本日官方公告slot、连续ID和例外联合判定。受影响范围是旧标题层关闭中存在明确长期模型/Infra/评价机制线索者，不把其余353个身份全部升级为全文队列。

定点查旧 V3 账时还核对 18775/18789/18834/18934 的官方 abs-v1，确认它们**已在本日162份完整题摘记录中**，不能误列为新发现的标题层漏项。V3_REVIEW_CHECKPOINT 既有具体前分母关闭理由：多生成 jailbreak 检测与既有采样/检测分账、RM→policy 双修复的受限组合、EDA 脚本结构合同的受限实例、跨应用最终状态 benchmark 的任务扩展；本次复读未给出推翻那些关闭理由的新证据，不重复计数。新补的标题层身份只有 `2604.19185v1`：以 Summary Content Units 为摘要候选打分并蒸馏多模型输出；当前 Ch29 teacher 选择与 Ch66 claim/support 单元已有一般分账，题摘未明确超出摘要任务的监督来源有效性新边界，作者建议具名**前分母关闭**。这些作者判断不替代非作者负侧抽检，也不增加正式107、评分或 Books 任务。

## 宽库存标题边界的第二次定点反查：五项关闭、一项准入待校准

本小批从旧515条日期未清洗宽库存里抽出当时尚未列入164份题摘账的六个标题边界身份，实际逐篇读完缓存的完整摘要；涉及贡献疑点的 `2604.19053v1` 另定点打开[官方精确版本](https://arxiv.org/html/2604.19053v1) §4、§7–8。以下表格保留独立准入前的作者判断作为过程证据；随后root已完成有限独立校准，正式账已更新为170=109+59+2，不能再拿旧164阶段计数作当前状态，也不把515改成逐项全文队列。

| 身份 | 完整题摘后的具体判断与停止点 |
| --- | --- |
| `2604.18623v1` [FlowSG](https://arxiv.org/abs/2604.18623v1) | 用 VQ-VAE、连续 box flow 与离散 scene-graph token 联合生成是视觉关系预测的真实方法变化；但当前证据只在 VG/PSG 的 scene-graph predicate/graph 指标对照一次分类器，未建立基础多模态表示、通用生成 factorization 或模型 Infra 的新边界。Ch23/24 的混合离散—连续生成主线不能因出现一个新 CV 输出对象而重写。拟具名贡献前关闭，不否认局部 SGG 新意。 |
| `2604.18882v1` [Patent Lean certificates](https://arxiv.org/abs/2604.18882v1) | Lean 只证明预给 match scores 后的 DAG coverage core，其他 IP 用例高阶定理多为未完成 proof sketches；synthetic claim 且无判决案例验证。Ch66 已把规格有效性、kernel-check 与语义真值分离，这篇把已知形式证明边界应用到专利解释，未给模型/Agent verifier 新接口或原有原则的反证。拟前关闭。 |
| `2604.19053v1` [CHRONOS](https://arxiv.org/html/2604.19053v1) | **不因 IoT、CNN 或小设备标签关闭。** Secure FL 的 idle-phase DH/TEE sealed key、active-phase stream mask 和 dropout reconstruction 形成真实 latency-critical phase×privacy lifecycle 分支；Ch36/72 目前有 federated type/privacy 分账，未明确这一时段/密钥/恢复联立条件，拟从标题关闭集重开贡献准入，待非作者复核后决定是否列本日候选。官方 v1 §7.1仅计算 active-phase latency，明确排除约250ms idle setup，20 clients、Rock Pi 4/OP-TEE，74%仅小CNN配置；§7.1 energy 是固定6.5W×时长的估算，不是独立实测能耗；§8.4假设 honest-but-curious server。不能写成总训练74%加速或通用TEE安全。旧库存摘要的32-node/<1.1KB是后版污染；[官方v1摘要](https://arxiv.org/abs/2604.19053v1)为20 clients/<700 bytes，精确版本必须以官方原文为准。原库存该ID的 `v1_updated_timestamp_revision_metadata_only=2026-04-22T00:30:21Z` 只作日期联合佐证，不能单独当首次公开。 |
| `2604.19057v1` [HSSPS](https://arxiv.org/abs/2604.19057v1) | 同一 SQL plan 因共享 buffer-cache 被挤出，逻辑分区+谓词注入+无会话 page token 改善的是通用多租户云安全记录查询。论文没有大模型训练/推理数据路径、Agent 检索记忆或本项目平台 workload 的独立验证；把缓存压力类比 Ch54/71 不等于主线贡献。拟前关闭，保作者在原任务的有界生产观察。 |
| `2604.19337v1` POLAR-PIC | Field Interpolation 外积矩阵化、粒子物理顺序布局与 Deposition 通信重叠服务等离子 Particle-in-Cell 求解器；不是 AI 模型的 kernel/训练算子。本项目 AI for Science 暂缓，不能由 Exascale、MPU、重叠比例类比 Ch36/49而恢复领域应用。拟范围前关闭。 |
| `2604.19448v1` [Crash-free Deductive Verifiers](https://arxiv.org/abs/2604.19448v1) | AValAnCHE 用 fuzzing 改善 VerCors 等通用演绎 verifier 的可靠性是软件验证工作；题摘未给 LLM 生成程序/证明的特有错误、checker 责任或 model release gate 的新增可检查机制。Ch66 已要求 verifier 本身版本化/故障审计；此处未给会改写该主线的反证。拟前关闭，非称 fuzzing 没价值。 |

六项已由 root 作有限独立准入复核：五项按上表具名范围/贡献理由前关闭，CHRONOS 因相位与秘密状态责任重开为受限候选；这不是其正面安全保证或 Books 已通过。正式处置及 exact-v1 的中心反例见下节与当日日报；此抽样不证明515条宽库存的全部排除正确。

版本污染的定点范围核（2026-09-28）：除已据官方 v1 重核的 CHRONOS 外，另外五项也分别对读官方 `abs/...v1` 的标题及完整摘要；`18623` 的官方 abs 页面由命令行实际取得，其余 `18882/19057/19337/19448` 的官方页面实际可读。五项的研究对象、证据范围与上表贡献关闭理由一致；这只是标题—摘要核对，不是五篇全文、日期或最终前分母独立 Gate。特别是 `18882` 的 Lean 保证条件明确为预给 ML match score 之后的 DAG coverage，`19057` 是云安全 SQL 工作负载，`19337` 是等离子 Particle-in-Cell，`19448` 是一般演绎 verifier fuzzing；不能因形式证明、数据库、HPC、验证器这些词可映射章节就自动恢复本项目主线。

### CHRONOS 受限准入后的 exact-v1 中心安全反查（作者侧，待非作者裁决）

root 对 `2604.19053v1` 的独立题摘准入认可其 **FL 更新的 idle setup→active mask→dropout recovery 时段/秘密状态分工**，因此不再以 IoT/CNN 标签前关闭；拟 DD2/SR1/Dur2=5 标准，Ch72 primary、Ch36仅作 handoff。作者随后定点重开[官方 exact-v1](https://arxiv.org/html/2604.19053v1) §4.1–4.5、§5.3–5.4、§7.1、§7.6、§8.4，并实际对读 Ch72 隐私/TEE 条件链及 Ch36 Federated Tensor Type 段。该方法能把一次性 setup 转移出受测 active latency，但 B4 software-only 对照表明这种相位拆分不是首次出现；TEE 分支的新成本是密钥/sealed seeds、硬件 counter/RPMB flush、恢复 shares 与硬件信任边界。作者的 `74%` 仅小 CNN `D=50k`、20 Rock Pi 4 的 active aggregation，排除约 `250ms` 每 epoch idle setup；`6.5W × latency` 能耗是估算而非独立功率测量，20 clients 的 Secure World measured `632B` 随 `N` 增长，不可写成对所有参与方数量常数。§7.6只测 small CNN/CIFAR-10、100图、三种观察条件，不能证明任意梯度或未来历史消息安全。原缓存 `32-node/Orange Pi 5/<1.1KB` 与官方 v1 `20 clients/Rock Pi 4/<700B` 不符，正式证据仅按 v1。

更重要的是现有安全主张存在**同一 epoch 的前向恢复→历史泄露反例**，不是仅 §5.4 已披露的伪 dropout/延迟消息或 §5.3 防未来 rejoin：§4.5 明示合法 dropout 时 server 获得客户端整 epoch 的 `sk_i`，可计算该客户端本 epoch 的**任意** round mask `m_i(r')`；§4.1 的保密目标却是不让 server 重构任何单客户端梯度。取同一 epoch 两轮 `r1<r2`：客户端 `i` 在 `r1` 正常发送 `g_i(r1)+m_i(r1)`，server 保留这条自己收到的 masked update；`i` 在 `r2` 真实掉线，`N-k≥t` 时 server 按协议从 shares 恢复 `sk_i`。用 `sk_i`、公开 peer keys 与 `r1` 重算 `m_i(r1)`，即可从旧消息得到 `g_i(r1)`。server 无须伪造 dropout、改变已完成轮次或攻破 TEE；普通 honest-but-curious server 记录收到的消息即可。§5.3 的“本 epoch 掉线后拒绝再次参与”只防 `r2` 后未来消息，epoch-boundary rotation 只保护此前 **epoch**，两者不保护 `r1` 的本 epoch 旧消息。§7.6 的 masked-gradient inversion 测试没有测试合法恢复后的历史回算。作者尚未发现 exact-v1 中有会使这条历史 ciphertext 不可保存/旧 mask 不可重算的机制；若有可信修正，应以具体协议步骤定点重开。

root 已独立定点复算并确认上述两轮反例：正式将本项列为 **2+1+2=5、强制深入、中心保证窄争议、Books 暂缓**，不把论文的保密/安全聚合保证作为正面 Books 证据，也不自动给 Ch72/36 写入。相位调度和 fail-closed 准备仍是可报告的局部机制。正式题摘账现170=109工作家族+59前分母关闭+2日期隔离，109中含本项，Date/Source/日级Gate仍未过。日期上本家族在旧库存早字段连续段：`v1_updated_timestamp_revision_metadata_only=2026-04-22T00:30:21Z`，仅同官方20:00 ET公告槽/相邻ID共同作有界批次推断，不能把该字段当 first-public 日志。

## 下一组标题边界的作者侧完整题摘查漏（暂不改正式 170 分母）

从旧 515 身份库存中，按 Agent 工作流、代码评价、联邦训练/隐私和训练网络等容易被通用旧标签误排的不同理由，定点选取下列 8 个此前未计入 170 的身份，实际读完各自缓存的完整摘要。选择是高风险定向抽样，不是随机样本或对其余标题层的全量证明；旧 `pre_denominator_closure` 模板未作本轮判断依据。`19399` 另定点对读[官方 exact-v1](https://arxiv.org/html/2604.19399v1) §I–II 的约束，不把卫星名词直接当否定理由；`19219` 官网原文这次未能取得，暂只使用缓存完整摘要，不据此宣称 exact-v1 深审或冻结日期。

| 身份 | 题摘所给实际问题、与当前 owner 的差异 | 作者暂定，待非作者校准 |
| --- | --- | --- |
| `2604.18883` EvoGraph | IDE 把人与 AI 的分支交互、代码变化做图状历史，20 人受限用户研究报告探索与认知负担；[Ch81](../../../../../books/part-07-agent/81-workflow.md) 已区分 branch lineage、外部状态隔离、评价和 promotion，[Ch84](../../../../../books/part-07-agent/84-agent-platform.md) 已有 typed Session branch/merge。原文摘要未给 Agent 自主执行状态、effect 冲突解决或可迁移发布门槛的新条件；图状 IDE 是有用的人机界面，不因名称包含 Agent 就改知识主线。 | 拟具名前分母关闭，保局部 HCI 价值。 |
| `2604.19081` 多窗口 GUI defect | 主动切换 Android 窗口布局、SoM 对齐 widget、VLM 检测视觉遮挡，50 app 的 F1/误报用于软件测试；没有让 Agent 的观察—动作权威、pre-dispatch 状态校验或 UI effect 验收发生新变化。[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 的 GUI grounding 不是所有 GUI 测试自动准入。 | 拟前分母关闭；50 app 和检出率不等 Agent 安全结果。 |
| `2604.19086` MUCOCO | 对代码题构造语义保持程序变体，再比较 Code LLM 的输出/测试失败；四任务七模型的约 15% 输入暴露不一致。这是实际评价信号，不能说只是普通新 benchmark；但[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已要求语义保持 mutation、执行测试、原始与变体成对及 verifier 敏感度分账，论文摘要尚未显示新的 evaluator authority 或需要改变的 release 决策。 | 拟受限前关闭，**请非作者定点核是否仍有模型一致性而非单题正确性的新边界**；不能以 Code LLM 领域标签拒绝。 |
| `2604.19118` DP-FlogTinyLLM | 联邦优化＋DP＋客户端 LoRA 用于 Thunderbird/BGL 日志异常检测，摘要承认隐私机制增加计算开销；没有披露改变 DP 会计、secure aggregation、联邦模型状态或大模型训练选择的独立条件。系统日志是输入任务，不因 Tiny LLM 一词自动进本项目。 | 拟具体组合前关闭；不声称作者方法无效。 |
| `2604.19219` 多方隐私实体对齐 | 对 VFL 把 PSI 暴露 intersection membership 改为多方 PSU 的 universal index，并加入 typo-tolerant 对齐；确有训练数据 join 的 privacy/equality 机制，当前 Ch27/36 未直接承载。但完整摘要主要证明特定 VFL 身份匹配协议，未建立 LLM 训练数据路径或跨机构大模型平台中的采用前提/性能边界；**不能因经典密码学或 VFL 名称直接关闭**。 | 暂作贡献消歧：仅在获得 exact-v1 可读协议/威胁模型后决定是否有本项目当前长期增量；不评分、不扩大附件。 |
| `2604.19315` MOCKMILL | 从开发者既有 test doubles 的 stubbing/interaction 生成可执行 Java 测试，10 classes/6 projects/4 LLM 的 coverage 与 mutation 改善是有限软件测试配方；[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已把 mock、执行与 mutation 作为 oracle 的不同证据。没有新模型训练、Agent 执行权或评价真值边界。 | 拟具名前关闭；不把局部 mutation gain 否定。 |
| `2604.19399` 动态卫星 FL routing | 分发全局模型与收集本地更新是两个通信阶段，官方 v1 §I–II 以可预测、间歇的卫星时变图、segment routing、deadline/client selection、单/多模型、可/不可分 flow 分类 tractable/NP-hard。这个数学边界可能迁移到动态 relay 训练网络，但本文目标仍是特定 in-orbit FL；[Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) 已把训练 collective/拓扑/phase 与 optimizer-step identity 分开。 | 暂作贡献消歧：定点核哪条复杂度分界能改变当前大模型/WAN训练的真实设计选择，而非仅把卫星路由定理类比入书；不自动候选。 |
| `2604.19454` 宏观 IP 风险 | 摘要只称层级 self-stabilizing algorithm 处理知识产权维度与次优风险解，未定义模型权重/训练语料 license provenance、模型发布风险或 Agent effect 授权的新机制与可验测试。 | 拟标题+完整摘要后前关闭，保其一般治理问题。 |

本组是作者侧 `6` 项拟前关闭、`2` 项贡献消歧；在非作者有限准入校准前不将 8 项追加正式报告计数，也不把 19219 原文获取失败冒作来源已覆盖。若对 19086/19219/19399 发现具体长期差异，只重开受影响身份，保持其他判断与已读证据；本组没有让 515 变成逐篇全文队列。

root 随后对三项争议边界作了有限非作者复核，替代上表中这三项的“待消歧”状态，但**不是八项或整批宽库存的独立验收**：

- `2604.19086v1`：exact-v1 §2–3 将同义代码查询下“两边都错、失败原因不同”也计为 inconsistency，确实不是单题正确率的同义词。现有 Ch66 已承载语义保持变体成对、执行 oracle、verifier 敏感度及 release evidence 分账；该论文未改变 final correctness/release 的权威归属。按受限 code-LLM consistency campaign **具名前分母关闭**，不称其局部测量无价值。若后续发现 Ch66 缺的是独立的长期测量责任，再定点重开，而不以新指标名称自动准入。
- `2604.19219v1`：作者本轮未取得官方正文；root 另从[官方 exact-v1 PDF](https://arxiv.org/pdf/2604.19219v1) 读到 VFL 多方 PSU/PSI、noisy identifier 与 universal row index，例子是银行、医疗及反欺诈。它有真实隐私实体对齐机制，但未给当前 LLM 数据/模型生命周期单独的采用合同；按**具体范围前分母关闭**，不是因 PDF 可达性或 VFL 标签而拒绝。
- `2604.19399v1`：官方 exact-v1 的分发/回传复杂度界依赖卫星时变图及特定 segment routing；Ch36 已分 topology、phase 与 step identity，尚无改变大模型 WAN 训练选择的可迁移约束。按**特定卫星 FL 网络算法前分母关闭**，保留这次跨域高风险反向查漏的事实，不将其定理改写为通用分布式训练保证。

这三项有了具名非作者准入口径，仍未增加正式 170 份题摘或 109 工作家族；余五项仍只有上表作者侧理由，最终负侧 Gate 由非作者按受影响范围验收。

## 两项原受限 Only 的反向准入（保留证据，不作零分候选）

root 定点重开 `2604.19059v1`、`2604.19342v1` 的官方题摘、上文必要方法与当前章节命题后，独立认可两项具名贡献前关闭。`19059` 在受限 UAV 五任务用固定权重、小 latent 在线适应动力学 mismatch；相同 checkpoint 的局部对照、ID 退步、推力上限失败及 MiniLM 任务映射均保留。Ch26 当前已把动力学状态、在线更新数据/回退、实际控制执行权分开，本项未给大模型 VLA 控制的新长期责任或可迁移性能保证。`19342` 的双 T4、三工业任务与 PTQ/QLoRA 的局部能耗/成本操作点可复算，但 Ch70 已要求同等质量、全成本/能耗与 SLO 同分母；旧卡、device-only NVML、正节省时才有意义的 break-even 公式不改变该合同。两篇的 exact-v1 作者审阅保留在上方，撤回的只是“值得纳为本项目长期贡献候选”的判断，不否定局部研究价值。

两项从正式 §3/4 移到具名前分母关闭后，当前170份完整题摘=107工作家族+61具体前关闭+2日期隔离；107=28真实整合+9具体已有覆盖+65仅报告+5窄争议。root 此次只是两项有限非作者反核，不等于其余负侧、来源和日级 Gate 通过。

## 余65项 Only 的作者侧反向贡献检查（不直接改正式分母）

本轮重新逐行对照正式 §3 的65个 Only 准入命题、上方 exact-v1 决定性证据与对应章节真实 owner。**证据后不入 Books**与**题摘原本不应进入候选**不同；不能仅因实验规模小、负面结果、已有章节、5分或任务名称而前关闭。对下列10项，作者认为原准入理由主要落在局部任务或成熟组合，应交非作者定点重判；在其结论前均保留原65条候选、评分和证据，不把“拟关”冒成通过：

| 身份 | 重判所需的具体边界，作者暂拟 |
| --- | --- |
| `18857` | Fisher 对角保护＋reflect/prox 协商是持续学习的局部优化配方；原审读已隔离非凸收敛/零遗忘保证，Ch29/28 的可训子空间与参数保护责任未变。若没有独立失效条件，拟前关闭而非仅因方法名准入。 |
| `18978` | 随机冻结critic＋低秩feature块的排序证据只在非语言模型的 SAC/FastTD3 控制任务；bootstrap条件的局部正则化不自动修改 Ch30/32 的 LLM PEFT 或价值估计选择。拟前关闭，保静态回归与shift反转。 |
| `19071` | 树状写作 rubric 的权重/扰动操作点有价值，但 Ch66 已分子评分、权重版本、原reference和verifier；局部genre反益未提出新的发布/真值责任。拟前关闭，不称研究“只是一张榜”。 |
| `19087` | 训练期可见 gold next-token 的特权 option encoder 与部署只读 hidden 的policy不同，这是可指出的 oracle gap；但§4把部署 RL policy 留未来，缺其成效/失败证据，Ch20 已有 sensor/controller 分账。若中心只有未验证的 option 优越性，拟前关闭。 |
| `19201` | 强模型草稿→弱模型 apply 及两阶段目标是真实代码编辑配方，但 Ch56/78 已要求阶段目标、功能验收与总成本同分母；DSV3总token和质量反向，未建立改变现有cascade采用边界的稳定条件。拟前关闭，保局部比较。 |
| `19267` | 尺寸条件候选/clearance排序属于特定机器人导航安全层；Ch26 已分物理状态、候选生成与monitor，作者的三Isaac环境和有限实测未给可迁移碰撞保证或新权责。拟前关闭，非否定安全目标。 |
| `19301` | Apple/Banana无客观 gold，社会呈现变量只给六模型的受限行为差异；首token方向关联不能识别规范动机，Ch82 没有因此改变协作/信息合同。拟前关闭。 |
| `19321` | RDP 轨迹选层的proxy与几何加权容量是受限LoRA selector 配方；同表 selected uniform 反胜weighted/reduced，Ch30 已要求任务/base/budget条件，未有新训练状态或容量责任。拟前关闭，保反向对照。 |
| `19440` | 固定EA设置下 novelty、breakthrough、fitness 的轨迹关联不能给稳定 operator/controller 因果选择；Ch79 已有探索预算与verifier分账。拟前关闭，不因LLM优化主题自动准入。 |
| `19457` | 合成企业制度的 retention/decision/abstention 分账在 Ch66/77 已有；10 case×3 budget 与同Haiku agent/judge给局部对照，却未形成新的证据身份或真实业务effect验收条件。拟前关闭，保小样本反例。 |

其余55项的正式 §3 准入句与上方必要源审读仍指出可影响模型/训练/推理/Agent 的具体机制选择，或评价、发布、安全证据的有效性边界；即使本篇证据只允许 Only，也**不因本轮缩分母而关闭**。逐项身份是 `18592, 18995, 18607, 19012, 19049, 19157, 19351, 19485, 18728, 19089, 18913, 19031, 19305, 18738, 18811, 18835, 18663, 18697, 18756, 18880, 18946, 18970, 19001, 19015, 18966, 19048, 19108, 19117, 19024, 19149, 19162, 19234, 19295, 19444, 19167, 19090, 19145, 19238, 19245, 19264, 19292, 19334, 19438, 19461, 18587, 18660, 18718, 18803, 19354, 18804, 18845, 18867, 18897, 18942, 18724`。这不是声称55篇结论获独立复核：对仍写“待独立”的单篇继续按原证据/具体 owner 终核，反向准入仅重开上表受影响身份。若非作者认为某项10篇仍有独立长期验证或设计反证，应保持候选并写清该命题，不按比例删除。

## 反向贡献准入的首批非作者结论（2026-09-28）

root 独立对 `18857/19071/19201/19321/19440` 的官方题摘及各自 Books 现有命题作有限核验，同意上表五项按具名理由从候选转为前分母关闭：局部 prox 持续学习配方、写作评分树的受限聚合、代码编辑两阶段训练与费用排序、LoRA 几何选层 proxy、固定进化搜索中的轨迹关联，都未建立足以改变本项目当前长期设计或评价合同的独立条件。此前 exact-v1 审读和局部反例仍保留在本文件及其他独立审计，不把“前关闭”解释为论文无价值或零分候选。`18978/19087/19267/19301/19457` 五项仍只是作者侧拟重判，未获此项独立准入结论；其他保留候选、负侧样本、日期及14来源也未通过整日日级 Gate。

此次仅同步五项身份的正式 §3/4 及分母：170份已读题摘=102个未冻结工作家族+66个具名前关闭+2个日期隔离；102=28实际Books整合+9具体Existing+60仅报告+5窄Disputed。515 raw仍只是宽标题查漏库存。旧107/61/65数字是此前阶段快照，不再代表当前工作分母。

## Only 再一组题摘反向校准线索（作者侧；不改正式分母）

依据本轮实际重开[19145v1官方题摘](https://arxiv.org/abs/2604.19145v1)、[19238v1官方题摘](https://arxiv.org/abs/2604.19238v1)、[18804v1官方题摘](https://arxiv.org/abs/2604.18804v1)，以及上方已完成的各篇必要 exact-v1 审阅与当前 Ch23/24 实际正文，额外圈出三项供非作者**贡献准入**定点核，不把这一步算作重新全文审稿：

- `19145`：多视角 ring-view 与时间先行剪枝是驾驶摄像头布局下的具体算法，PDF-v1 的 DriveMM/RTX PRO6000、10% token 局部退步均留存。Ch23 已要求在预算内保存不能被别的模态替代的证据，并计 selector 误差/成本；此篇是否提出更可迁移的多视角 token 身份或受控新失效条件尚未在题摘/原必要审阅中成立，作者拟具名前关闭，不因驾驶标签本身拒绝。
- `19238`：Real-SR 的 LR 来源与一阶 flow 起点不匹配、速度场蒸馏是具体生成任务，现 Ch24 已区分训练支持、部署起点、step/NFE 与最终质量。原 v1 中 ATM 去除后 PSNR/FID 反向、50–200×仅为 NFE，不能作为普遍单步机制优势。作者倾向前关闭，但“few-step prior collapse 的可迁移条件”可能仍是独立长期警告；需非作者核这一点，不因超分领域一刀切。
- `18804`：随机子空间 Jacobian 曲率与 PHFE 在 normal/OOD 同 seed 的相关性变化是诊断观察；作者的结构根因说法未由单独操纵曲率识别。Ch24 已有模态界面局部敏感性和“几何诊断须与真实模型质量、成本对照”的边界。若此篇没有新增可用的发布 sensor 或特定条件反证，作者拟前关闭；保留其受限观察及对因果外推的反证，不把负面/纠错信息抹去。

三项目前仍在正式102工作候选中，原评分、§4必要证据及 apr01 对19145/19238的有限源核均有效；未获非作者准入结论前不改变表、比例或统计。其余Only亦不能从这三项推定可关，不按比例压缩分母。

作者复读当前 `RESEARCH_CONTRACT.md` §3 后收窄上面三项提议：`19145` 的跨时间与 ring-view 剪枝仍是多视角视觉 token 预算的具体机制，`19238` 的 LR 初态与单步 flow 轨迹偏移仍是生成路径的具体条件；局部任务或 Ch23/24 已有一般原则都不足以单独作贡献排除理由。撤回对这两项的作者拟关闭，保持正式受限 Only 及 apr01 已做的必要源核。`18804` 也只留下“其几何诊断是否超出 Ch24 已有敏感性认识”的定点问题，未作前关闭裁决。此修正不把论文推为 Books 增量，更不让比例决定准入。

当前102身份与原始收据的只读复算：§3唯一 ID `102`，均能在本日515宽身份原收据逐一匹配；其中当前OAI日期列表含04/22者`74`、OAI日期列表为空者`13`，余`15`为其他日期/修订状态。102项的 `v1_updated_timestamp_revision_metadata_only` 字段范围为04/22 `00:00:08Z～00:59:56Z`，无一超过 `01:00Z`。这些只能与官方公告槽、连续身份边界合用作有界批次归属，不是逐篇 first-public 精确日志；缩分母后其余日期/机构隔离条件未自动解除。正式日期 Gate 仍交非作者核。

apr20_resume 的[四项有限独立审阅](./V3_APR20_FOUR_19024_18845_INDEPENDENT.md)另对 `19024/19295/18803/18845` 核 official exact-v1 必要方法、决定性反证与实际 Books owner，四项受限 Only 判断均通过，不计 Books 新写入或整日 Gate。`18803` 官方 PDF-v1 p15 Table2 的 InternVL14.40、DeepSeek52.18、Gemma4 2.05 与相邻正文3.42/61.80不能合成一致总体排序；主800张与事后717张设计审计分母也不能合并。该纠错已同步正式 §4，其他19项显式待独立仍未由作者自审冒充通过。

## 19274 HarDBench：从旧前关闭重开贡献准入的作者侧证据

[官方 exact-v1](https://arxiv.org/html/2604.19274v1) §3.2–3.3 以1,204条验证过的有害草稿建集，从四类各固定抽100条作测试；单轮prompt将同一草稿置于“编辑/扩写”任务包装，与不带任务包装版本比较。§5.2 Table1 八个受测模型在CoJP下的ASR均高于相应无包装CoJP；例如GPT-4o在同表从23.50%到96.75%，而直接有害查询17.75%。这不是仅多一个安全任务条目：输入内容有明显危险线索，但任务包装改变了受测完成行为，因此直接有害提问的拒绝率不能代替协作编辑场景的验收。现Ch72已要求不可信输入、pre-guard与post-generation guard及安全/效用分账，但未明确这种**有害草稿可见而编辑角色改变行为**的受控评测条件。作者侧建议重开贡献准入，暂拟 Design Delta2/System Reach1/Durability2=5、安全失效条件触发窄深入；是否构成长期Books增量、正式日期归属及分母变化均等非作者复核，当前正式表和66关闭账目未动。

反证/范围同样重要：§3.2的草稿由模型生成并由GPT-4o校验，四域、固定手工task模板和每域100测试项不代表开放攻击分布；§5.1 HS/ASR同样依赖GPT-4o judge，不能读成独立地面真值。Table2标题称unsafe response rates，§5.2解释却称prompts classified，需隔离该指标的检测对象，不把85%→22%写成已验证生产moderation漏检率。HQ与CoJP又同时改变文本长度与草稿内容，只有CoJP有/无task framing是更窄的包装对照。§5.2 Table4 的安全/写作效用受具体模型、训练recipe和多个不同judge影响；不能据此断言所有模型、所有benign draft或所有KTO/GRPO训练同时安全且不退步。初筛旧理由“只有成熟balanced preference optimization”遗漏上述安全评价盲点，须经非作者正反准入校准而非静默提升。

[apr01 有限非作者准入审计](./V3_APR01_19274_ADMISSION_INDEPENDENT.md)已重开 exact-v1 决定性方法/表与 Ch72 guard、窗口、persuasion 相邻正文，确认旧前关闭理由漏掉同草稿任务包装失效，支持 `2+1+2=5` 与安全评价边界窄深入。该审计不含首次公开、Books 采用或日级 Gate；上文“当前正式表未动”记录的是准入审计前状态。作者现据此将该身份从66项前关闭移入103项工作候选，§3/4已更新；普通 Books 待办继续公开，不预支正文写入。

apr01 接着对[原显式待独立的五项](./V3_APR01_PENDING_FIVE_INDEPENDENT.md)做必要 exact-v1 与实际owner独立复核。19087 的特权 gold-next-token encoder/最优 option ≈70%不能证明部署 policy 的同预算改善，现由原标准Only具名前关闭，原阅读证据不删；19444/19167/19264受限标准Only和19267保护深入Only均通过，尤其不能把尺寸条件候选排序与无safe候选回退仅因Ch26一般分权而前关闭。该单篇批次使本日170已读题摘变为102工作家族+66前关闭+2日期隔离，工作家族中28实际I、9E、59Only、5窄D和19274一项普通Books待决；仍非来源、日期、其余10项或整日Gate通过。

随后 root 实际在 Ch72 Guardrail 论证中写入 19274 的同草稿编辑任务包装配对验收、前/后 guard 与良性编辑效用分账，以及多变量/judge/线上外推限制。书稿非写作者 apr02 对[官方 exact-v1](https://arxiv.org/html/2604.19274v1) §3.2–3.3/§5.1–5.3、实际新增正文与相邻衔接完成[写后独立核验](./V3_APR02_19274_WRITE_AFTER.md)，结论 PASS，未复现实验。当前 102 工作家族的 Books 对账是 **29 I / 9 E / 59 Only / 5 D，普通 Books 待办 0**；上一段的 28 I / 1 待办是写入前快照，不覆盖此状态。十项其他候选的单篇非作者核及日期/来源/负侧整日 Gate 仍开放。

随后 root 对 19292 LocQA 的 exact-v1 §3–5.2/Limitations 与 Ch66 现有翻译保真段独立对读，确认“显式地区知识”与“仅由语言推断默认地区”属于不同评价对象，按原主线窄写 `SF-2026-ARXIV-2604-19292`。非书稿作者 apr02 复查官方 exact-v1、实际段落和前后衔接，[写后核验](./V3_APR02_19292_WRITE_AFTER.md) PASS。论文的44个语义平行问题、12语言/49地区、2156 locale-specific QA和32模型只是受限评测范围，自动judge/80人抽核并非开放真值；书稿对澄清策略的验收是明示设计推论而非论文实验，训练因果不采用。本项因真实Books采用升级为5分**深入完成**，当前102工作家族=**30 I / 9 E / 58 Only / 5 D**，普通Books待办0；尚有9项非作者单篇审阅和本日来源/日期/负侧日级Gate，不据单篇通过称Complete。

## 19457/18660 反向准入归档（不删除原审阅）

root 对 `2604.19457v1` 与 `2604.18660v1` 另作[官方 exact-v1、Ch66/72 实际 owner 的有限非作者复核](./V3_ROOT_19457_18660_REVERSE_ADMISSION.md)，两项从原 Only 改为具名贡献前关闭：合成企业四轴评价没有新增 Ch66 已有的 reference/process/outcome/abstain 责任；教育 Tutor 泄漏需要的攻击者自知、受测系统披露、judge 事件分母已由 Ch66/72 承载。上方单篇方法、数字和反例仍作为查漏证据保留，不再当正式评分候选。最新170=99工作家族+69具名前关闭+2日期隔离，99=30I+9E+55Only+5窄争议，普通Books待办0；六项显式单篇独立终核与整日日级 Gate 仍开放。
