# 2026-04-21 贡献初筛（V3）

这是作者实际题摘判断，不继承旧泛化 closure；原库存题摘先作线索，拟采用项仍须核官方 exact-v1、撤回状态、first-public 组合与必要证据。宽库存不是候选或全文待办队列。

## 首批：标题范围浏览 0～209；完整题摘 35 家族

| 家族 | 当前题摘裁决与具体依据 |
| --- | --- |
| 16304 | 前分母关闭：19位实践者访谈提出评估结果难转行动的组织问题，未新增可检验 evaluator / 模型 / runtime 机制或足以修正既有设计的结果；不把访谈人数当贡献门槛。 |
| 16306 | 前分母关闭：position paper 主张 artifact 审阅优先于文字品质，重申现有证据审查原则；无新增原始机制/有效性条件。 |
| 16310 | 前分母关闭：动态用户生成→对话过滤→评估组合，摘要的验证主要确认能检测系统修改及与静态趋势一致，未指出此实现改变既有交互评估的哪一有效性边界。 |
| 16312 | 前分母关闭：作者及apr02实际核完整題摘、§3.1/Table2；document-local/bounded window/source-span与粒度移除只支持组合互补，未建立受控missing/spurious-noise有效性条件；不足以改变当前检索解释。不是因owner存在而关闭。 |
| 16314 | 前分母关闭：11种任务上代码生成/集成热扩展的流水线可行性，摘要没有新增热状态兼容/执行承诺的机制或反证，不因 runtime 名词即保留。 |
| 16318 | 前分母关闭：作者及apr02实际核IV-B/IV-C、TableII/VI-A；MiniLM+FAISS pool与fullcatalog不matched，同pool HR .011→.008而nDCG .004→.005，不是所有质量下降。局部coverage/domain mismatch没有改变成熟边界的新证据，不维持原潜在候选。 |
| 16320 | 潜在贡献：程序变换/输入扰动/异常分支揭示原CRUXEval高准确率的边界；需核是否为合法等价干预和exception归因。 |
| 16322 | 潜在贡献：actor反馈决定constraint-schema探索终止并与schema composition共同演化，改变合成数据难度/覆盖的控制对象，非只新增coding数据集。 |
| 16323 | 前分母关闭：以intent telemetry/causal graph命名流程可解释性，摘要未提供可检查的新因果辨别或控制机制证据；不因global drift措辞retain。 |
| 16324 | 潜在贡献：激活rank sketch保dX与近似dW的分离、balanced hashing/energy norm机制，改变训练显存-梯度误差取舍；exact/variance保证需定点核。 |
| 16331 | 前分母关闭：working/episodic/semantic三级经验总结与检索在具身规划的应用验证，题摘未分离不同于现有记忆演化的有效性条件/机制或反证。 |
| 16332 | 潜在贡献：annotation disagreement下LoRA与full FT逐样本loss出现不同方向，跨25条件/seed对照修正adapter学习动力学认识；不把关联当原因。 |
| 16335 | 前分母关闭：rubric GRM筛轨迹再RFT对比terminal rejection sampling，摘要未新增区别于既有process/rubric反馈、proxy-vs-outcome的机制/边界，不能因GRM名称保留。 |
| 16339 | 前分母关闭（必要消歧后）：SIG/CDE/CRP确有结构，但§5.3规则和§6.2框架配置模拟、预校准judge没有分离新的重要执行保证/失效边界；不将workflow完成率推为完整治理。独立必要证据已核。 |
| 16349 | 潜在贡献：可执行web程序维护动态groundtruth并区分lazy retrieval/temporal re-anchor错误，需核oracle更新与修复污染边界。 |
| 16351 | 潜在贡献：构造结构负例改善匹配却损失zero-shot retrieval，MaxSim reranking也不拒绝near-miss；需要分离recall接口与identity verifier。 |
| 16358 | 贡献候选、标准完成/仅报告：on-policy多轮视觉攻击与prefix min/mean轨迹reward是具体受限训练分支；已核聚合、helpfulness和共享judge误差，但未形成发布/保护行为变化，不因标题含安全自动深入。 |
| 16363 | 题摘曾提出 query-only lineage 信号；必要正文与独立复核后为 2+2+2=6、标准完成/仅报告：Beta 是 probe argmin 投票频率，不是身份 posterior 或所有权证明；没有具体保护行为变化，不由安全标签自动深入。 |
| 16368 | 潜在贡献：cross-tokenizer UAG在unified-memory上draft/verification带宽分账、specialized draft反收益，使高acceptance≠speedup的选择有具体反证。 |
| 16378 | 前分母关闭：医疗表格文本LM和RF互相提供embedding/reward，复用混合预测/反馈融合产生领域指标收益，未显示新的训练有效性边界或独立机制。 |
| 16382 | 前分母关闭：temporal instruction/curriculum诱导五个纵向任务ICL收益，摘要未分离具体学习机制或改变现有ICL/指令学习选择的独立条件。 |
| 16383 | 潜在贡献：rubric granularities×backbone下completeness判别接近随机、90%recall仍需几乎全人工审查；同verdict不同reason可改变judge准入与triage效用判断，而非仅医学榜单。 |
| 16385 | 潜在贡献：同Web任务基线配受控layout/interaction semantics/execution disruptions三轴，核clean score是否对真实操作可靠性有辨别力；不把perturb数量作贡献。 |
| 16391 | 潜在贡献：forward video与inverse latent-action分离使用不同无标签数据源再联训，改变VLA表征/动作预训练耦合成本；需核数据、真机与counterfactual。 |
| 16395 | 潜在贡献：context append/update arrival改变prefill preemption、LCP失效与shared-resource准入，是可复核 serving state 新边界。 |
| 16400 | 潜在贡献：FL PEFT和inference共用replica参数、shadow adapter及双时间尺度协调，改变shared GPU训练/推理隔离假设；版本质量/SLO边界必须核。 |
| 16401 | 贡献候选、标准完成/仅报告：§4.1/Table3比较GraphRAG-first、LLM-first与one-time路由；实际先选框架预期granularity、再选LLM、调用pair后才取证，并非actual-evidence admission。apr02已独立核顺序、pool和1/2/4成本proxy边界，只保留受限顺序结果。 |
| 16402 | 潜在贡献：predicate bucketing GPU-native layout、local/remote graph及append更新改变hybrid ANN执行机制；不采用CPU240×作为架构一般胜利。 |
| 16405 | 潜在贡献（安全深审）：事故/手册risk chain生成约束与worldmodel危险后果缺失/严重度失配，改变imagined rollout安全准入证据。 |
| 16410 | 潜在贡献：matched-LR控制下CLIP FT/LoRA transfer/attention drift排序及underfit条件，修正只按方法均值比较的结论；不称attention因果解释。 |
| 16420 | 潜在贡献：允许AST暂时invalid再LLM repair扩大可搜索对象，相比thought-code始终合法是一项具体搜索设计分支；仅TSP/binpacking，后审决定长期处置。 |
| 16421 | 潜在贡献：同几何问题多等价表示配对、invariance metric与capacity-dependent convert-then-solve干预，区分accuracy和representation sensitivity。 |
| 16423 | 潜在贡献（安全深审）：PPS梯度方向与IP解释噪声路径不同，且IP不修已学trait，为防御训练共存/失败条件提供具体差异。 |
| 16424 | 潜在贡献（安全深审）：SSM recurrent state的spectral增益、delayed trigger、容量饱和三条实际攻击/保证线索；领域部署不是准入依据，机制/理论需核。 |
| 16426 | 最小消歧（纠正旧过宽关闭）：activation-region匹配有模型身份主线关系，不能以组件成熟关闭；独立§10.4同hash签名Hamming均值却声称fixed realization可违反三角不等式，定义/声明窄冲突。§11.3只两toy网络/16k sample无参数扰动稳定性直接对照，不能采稳定canonical宣传；作者须据可支持命题决定具体关闭或窄争议，不自动正面采用。 |

上表不是冻结分母，来源、贡献最小消歧、exact-v1与公开时间尚在收口；不将潜在贡献直接写为Books新增。

## 第二批：已读 28 个完整题摘

| 家族 | 题摘裁决与待核的具体贡献 |
| --- | --- |
| 16430 | 前分母关闭（必要消歧后）：§4–5是energy/C-DLA feature选择和logistic probe；无feature intervention因果验证，只有Gemma局部检测工作点，不支持新幻觉因果阶段。不是因SAE/probe成熟即排。 |
| 16431 | 潜在贡献：离线gradient avalanche probe的dimension轨迹、ungrokked/shadow负控，增加generalization transition诊断对象；toy任务不证明普遍critical manifold。 |
| 16434 | 前分母关闭（完整题摘复审）：是一般belief arbitration概念架构和最小重复交互模拟，没有直接研究基础模型学习、生成或AI Infra的实际控制机制；support-resolution/resource-cost叙述能类比Memory，但类比不构成当前项目贡献。不是因为没有LLM大实验硬排，也不否定其一般认知模拟价值。 |
| 16453 | 潜在贡献：完整序列reward target的prefix approximation和lookahead exact marginals区分、SMC rejuvenation，改变采样目标及成本；不以headline胜GRPO为依据。 |
| 16456 | 潜在贡献：同场景mid-speech interruption与half-duplex配对对照，区分状态改写错误与任务难度；三类post-interruption失败为可迁移评估切片。 |
| 16462 | 潜在贡献：intrinsic视觉冗余与backbone相关saturation分离，揭示LLaVA剪枝不能直接迁移Qwen；熵proxy及FLOPs/时延仍需限定。 |
| 16469 | 潜在贡献：single-tool speculation→bounded future subgraph，按critical-path reduction/slack/interference而非概率排名改变实际资源/提交边界；内部Thor实测不证明生产收益。 |
| 16471 | 潜在贡献：proof-system closure fidelity与vocabulary mismatch给deductive compression/broadcast不可消除边界；必要理论假设须对应形式实例而非自然语言语义。 |
| 16475 | 潜在贡献：gamma-SQP分两步spike编码、对称双向encoding与membrane clip改变LLM低精度执行选择；能量估算/实硬件必须分清。 |
| 16479 | 潜在贡献：相同compression ratio下频域latent压缩vs直接减channel的重建/生成收敛取舍；需核生成收益是否实际测量，不能只根据动机采用。 |
| 16481 | 潜在贡献（安全深审）：t-mixture低秩concept分布/affine transport anchor+MoE模块/投影噪声，明确白盒移除攻击和保留内容的冲突边界。 |
| 16483 | 潜在贡献（安全深审）：敏感语义anchor与cross-attention闭式校正，需核‘well-posed optimal’仅目标函数内成立及benign drift/攻击边界。 |
| 16484 | 潜在贡献：latent目标、双状态TTT和physical execution遮蔽denoising共同改变world-action model状态规模/延迟链；strict O(1)/sim-to-real/efficiency law需核实。 |
| 16485 | 前分母关闭：用大模型关注位置训练小attention预处理器降视觉输入，是既有selective attention/distillation的局部应用；未给改变可行性或代价排序的具体新证据，非因小模型拒绝。 |
| 16487 | 潜在贡献：邻域Hungarian结构一致性和query-conditioned contrastive steering区分ranking/可控检索的局部几何，而非只增finetuning指标。 |
| 16492 | 潜在贡献：layergroup×timestep×JVP span三维cache决策，浅深velocity异质性使全Transformer单一刷新规则失效。 |
| 16498 | 前分母关闭：四阶段capture/优化/IR/liveness allocation与device scheduling复用成熟compiler过程；摘要的IntelNPU比较没提出新的语义/调度有效性机制或可迁移边界，不因编译器标签/9×retain。 |
| 16499 | 潜在贡献（标准）：black-box VL retrieval攻击同时降低正对/提升负对相似度、layer-guided初始化提供受限objective变体；不把counter-fitting substitute等同语义严格保证，后审决定仅报告。 |
| 16502 | 撤回排除：当前官方abs明确This paper has been withdrawn，v2/2026-06-04说明未署名复用方法/代码。撤销潜在准入，不评分、不保留selected、不进Books；原始题摘与排除依据保留，不因此删除其它证据。 |
| 16503 | 潜在贡献：video生成role-specific backbone+shared crossattention+早期frozenencoder对齐，在预算约束下的capacity组织分支；不能混合不同训练数据比较作组件因果。 |
| 16514 | 潜在贡献：progressive block merging与小block dVLM anchor阶段蒸馏；AR→diffusion直接distill可能损害而同regime anchor有效的新teacher兼容边界。 |
| 16515 | 潜在贡献（安全深审）：visual perturbation覆盖显式price constraint并诱导coordinate action；whitebox/singleturntransfer与cleanaccuracy代价必须分账。 |
| 16519 | 潜在贡献：likelihood-free positive-advantage local drifting是online generative policy更新替代机制；未披露实验证据不能采用proactive prevention等保证。 |
| 16521 | 潜在贡献（安全深审）：session PII co-occurrence registry与retroactive masking试图处理跨turn组合可识别性；重点核已向外披露是否可被回溯遮挡，不能说全utility/隐私保证。 |
| 16524 | 潜在贡献（安全深审）：versioned policy→ConsentRecord→peraction AdherenceEvent与协议兼容/TLA生命周期；clauses引用日志不能证明实际理解或遵从，需要核其形式property范围。 |
| 16529 | 潜在贡献：longcoding rollout summary保假设/进度/失败，再递归小组tournament或condition后续rollout；比较单位/状态复用与短answerBoN不同。 |
| 16535 | 潜在贡献（标准）：小calibration set的hidden-state scorer提供BoN选择成本/质量折中；需要actualtraining/inference预算而非8,000×参数宣传。 |
| 16536 | 潜在贡献：unlearning测试的mediated path、cancellation、subgroup masking使单attribution检查不充分，budgeted causal intervention引入具体oracle对象；proof-of-concept范围不能泛化。 |

## 第三批：已读 14 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 16538 | 前分母关闭：Lean编译/库检索/expert draft的factorial量化，摘要未给改变既有tool/semantic witness判断的具体效应方向或新机制；不是因formalization领域拒绝。 |
| 16542 | 前分母关闭：台湾语言数据适配guard改善F1/FPR，复用现有distribution/slice-specific校准；没有新的安全路径或设计成立条件，非把该区域性能当通用失效反证。 |
| 16543 | 潜在贡献（安全深审）：单项benign trigger与被攻remote agent模板经routing合成激活，组件guard看不到联合恶意的新trust boundary。 |
| 16548 | 前分母关闭：long-term memory安全生命周期survey/五个VMG primitives总结现有provenance/version/policy/rollback原则；摘要未给新的综合证据解决具体争议，非因为survey标签拒绝。 |
| 16555 | 潜在贡献（标准）：hierarchical code-mined tree由算法决定宏观探索、LLM只补残余自由度，改变Agent对执行合法搜索的控制权；小图像NAS任务限定。 |
| 16557 | 潜在贡献：GRPO全失败group注入groundtruth anchor并给maxreward，为稀疏探索开新conditional objective分支；必须核off-policy/bias而非采catastrophic forgetting宣传。 |
| 16565 | 潜在贡献（标准）：forward mask/backward reconstruct稳定度作dLLM diagnosis/selection/reward的proxy；需核同模态自一致不等同truth。 |
| 16571 | 潜在贡献（标准）：PyTorch到netlist多入口统一verification IR及SMT/BTOR/AIG输出是一项跨语义层执行验证分支；不能称整个deployment已proof。 |
| 16574 | 前分母关闭：OBD/Taylor saliency复用于FL个性参数选择并将score计算移server，摘要未给相较已知saliency/global-local分账的新重要约束或反证；不以非LLM/小模型作拒绝门槛。 |
| 16576 | 潜在贡献（标准）：30datasets/混合效应控制的reasoning-specialization tax与synonym-vs-typo/corpus poisoning切片，提供retriever选型/稳定性具体反证。 |
| 16583 | 潜在贡献：cache resident控制router探索成本且router控制feedback，双时间尺度bandit+force探索的理论条件/实paging改变adapter serving控制关系。 |
| 16584 | 潜在贡献：spec先randomized validation→verification obligation分解→不同证明模式，实测reference defect揭示certified code不等于spec正确的准入边界。 |
| 16585 | 潜在贡献（标准）：JEPA连续state→grid snapping的rollout纠错分支与random-walk exploration，需核适用结构而非‘causal discovery’普遍保证。 |
| 16587 | 潜在贡献：learned causal-region estimator从attention signals摊销干预代价，区分即时attention图和经干预目标校准的可视归因，真实faithfulness/cost需审。 |

## 第四批：已读 12 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 16591 | 潜在贡献：由undesired generation触发、但未给定forget/retain分区时，用线性化influence、hash与随机antipodal搜索选择遗忘对象；改变选择对象与保留损失的联合优化，而不是再给一个unlearning榜单。 |
| 16592 | 前分母关闭：以人类功能划分world model的七项taxonomy与intrinsic motivation议程；摘要未提供改变当前生成/物理闭环设计的具体机制或可检验证据，不把概念议程列为已确认缺口。 |
| 16593 | 前分母关闭：整合多词词汇语义任务、给顺序评价与class interpretation变体，未指出既有评价测不到的重要能力/混杂因素或新的有效性条件；不是仅因语言学主题拒绝。 |
| 16606 | 前分母关闭（安全消歧后）：二值聚合sum可推median，不能误称算法不可算；但HBC server的密钥/解密owner未闭，IND-CPA不能推任意inversion固定PSNR上界。成熟隐私模块组合未形成可靠新机制，过强保证本身不是贡献；具体争议保留在独立记录。 |
| 16607 | 潜在贡献（标准）：22个AI文本detector在七种英文设置和creative writing下排名随metric/dataset改变、novel human text失败，提供判断器domain/metric选型的独立反证；不采用通用检测不可能结论。 |
| 16615 | 潜在贡献：音频条件通过低秩参数variational posterior和异方差噪声进入LLM，pooled context一次计算、逐层head派生，而不是常规input fusion；需要核训练/推理成本与条件信息损失。 |
| 16617 | 前分母关闭：两种单模态teacher合并reasoning traces后做SFT cold-start和RL，跨模态再改善单模态指标；题摘未分离相较既有teacher-trace融合/RL路线的兼容性条件或独立机制，非因音视频范围拒绝。 |
| 16620 | 潜在贡献（标准理论）：不受限variance与mean-square条件下的oracle complexity下界、Halpern/Tikhonov anchoring匹配上界；具体优化条件值得保留，但不能外推现代Transformer训练保证。 |
| 16625 | 前分母关闭：失败memory、synthetic task generation、tree search精修/重生成组合kernel搜索；摘要的speedup没隔离新增验证边界或重要设计反证，不因kernel标题或benchmark收益直接retain。 |
| 16646 | 潜在贡献（标准）：固定22套框架配置下reasoning backbone与orchestration的质量/耗时/费用分账，retry/context开销可反转质量选择；核真实预算和配置归因，不把框架数当贡献。 |
| 16654 | 前分母关闭：reclaimed-slur标签的社群/语境分歧与现成toxicity detector比较，是已知规范依赖/label disagreement的场景研究；摘要未给值得本项目改变的独立评价机制或边界。 |
| 16656 | 潜在贡献：vocabulary expansion先按可解释性而非频率选词，再由逐层subword detokenization初始化embedding；提出词表选择与初始化耦合分支，需核非拉丁token预算与质量/成本。 |

## 第五批：已读 16 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 16657 | 潜在贡献（已最小消歧）：与16615为不同ID、global-vs-token posterior路径，不因同作者合并；§2.2逐token text-query/audio-frame条件化E，shared-KV变体分成本。拟5分标准仅报告；AUC不是校准，MC多次forward代价保留。 |
| 16659 | 潜在贡献（安全）：benign audio FT在三种架构中的语义/声学距离轴不同，encoder/projector状态与后端refusal电路分离；实际干预及过滤失效条件可能改变音频安全准入，不把内部representation关联当因果。 |
| 16677 | 前分母关闭（必要安全消歧后）：CQR error-ranking+state Mahalanobis应用未新增有效的安全成立条件；Eq6把α=.1下分位写成90%上覆盖，Eq9/10共用offset不改变argmin，marginal不传给postselection，TableII未分离rawQR/CQR。保留经验及具体问题，不把错误保证新造为长期贡献。 |
| 16678 | 潜在贡献（标准理论）：闭式线性/RKHS alignment替代minibatch contrastive迭代是一项objective/优化分支；必须限定fixed encoder/kernel与learned nonlinear representation的区别，不采用全面免backprop保证。 |
| 16682 | 潜在贡献：Agent进度/并发/多实例placement与GPU频率共同控制，低频延长context residency造成KV thrash与能耗反收益；需要可归因测量而非仅省电headline。 |
| 16683 | 潜在贡献：action-chunk重叠一致性检测与演示checkpoint恢复、实际rewind共同改变执行状态；要核物理可逆性/安全恢复，与只重置policy隐藏状态分开。 |
| 16684 | 潜在贡献（标准理论）：piecewise-stationary reward/transition的变化检测与learning controller分账，给tabular/linear MDP明确条件的minimax边界；不是现代LLM Agent的已验证保证。 |
| 16686 | 潜在贡献（已最小消歧）：§3两流JS+margin门使连续logit tilt转为显式baseline backoff，不需gold在线oracle；只在共同prefix被选步一致，全串需每步backoff，非correctness。拟6分gap深入；AppB无heldout调阈值/两forward成本保留。 |
| 16689 | 潜在贡献（标准理论）：解释query的容量与可达估计/实际OLS或Lasso分离，预算足够不等算法可辨识；定点核noise、curvature、sparsity限定，不推广为所有LLM不可解释。 |
| 16694 | 前分母关闭：consecutive-hidden-state rank作difficulty proxy，再router调用强模型或filter steering vector，是新局部scorer与成熟route/steer组合；题摘没有改变proxy有效性/控制条件的独立机制或明确设计反证，速度质量排序不能单独保证准入。 |
| 16697 | 潜在贡献（安全）：同模型能直接识别漏洞但生成代码时未执行该检查，format competition与最后层steering的干预需核；可区分安全知识readout与实际生成约束，不以漏洞数/模型数直接保留。 |
| 16700 | 前分母关闭：语音伪造检测review与未来neural representation建议未给新机制或综合证据解决本项目具体设计争议；非因review类别统一排除。 |
| 16706 | 必要评价消歧后保留6分纠错Deep暂缓：官方v1题名/2,300trace不同旧库存，已核abs/HTML/PDF；九模型不显著Spearman不证独立，两臂同heuristic不自动抵消误判，保留有限协议/经验，不正面采用两项中心保证。 |
| 16714 | 必要理论消歧后保留5StdOnly：平方密度合法性和正负期望差采样是不同职责，抵消方差与safe component/VI预算有具体取舍；仅条件基础推断，不据最优proposal宣称Transformer通用方案。 |
| 16715 | 必要执行消歧后保留6StdOnly：节点AG复制K/V与head-A2A复制全图形成不同graph/activation/通信成本；稀疏foundation训练入口明确，两8GPU单机证据不推dense LM普适选型。 |
| 16725 | 前分母关闭（实际必要方法后）：bucket拉排序操作与in-place reclaim确是GPU动态有序key-rowID map新算法；原研究未建立大模型计算、向量检索或训练/Serving约束的直接贡献，仅类比runtime不足，非否定算法学术价值。 |

## 第六批：已读 26 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 16733 | 潜在贡献：主动sensing action先决定可观察证据，4D retrieval/temporal support与条件生成共同估计query-conditioned observation；与仅完整world rollout不同，需核极端viewpoint下证据支持而非生成逼真即物理正确。 |
| 16734 | 最小消歧：prefill结束后压缩不能限制峰值，须核sequential structure-aware压缩是否新增区别于已有流式KV预算的具体执行/质量边界；仅固定budget目标本身不够。 |
| 16736 | 前分母关闭：生成结构化数据后由template渲染、按估计输出预算决定chunk/defer，是成熟格式成本分离；摘要的OGC命名与token节省未提供独立capacity测量或新的生成有效性条件，不能以always theorem措辞代替贡献。 |
| 16745 | 潜在贡献：受控多种pairwise score共同cliff与深层ranking稳定度，提出error amplifier和unary/triage分账，可能改变视觉token reduction信号选择；O(N²)扰动不自动证明一般失稳，需核必要模型。 |
| 16752 | 潜在贡献（标准）：同请求最小反事实改变clarify/support/abstain三种延期条件，scalar confidence坍缩而typed action改善的受控证据；单context dual-persona/heuristic仅上限，不能当真实自主运行保证。 |
| 16753 | 前分母关闭：parametric/source confidence分账、skill card和延迟offload组合，在Gemini单context静态评测没有分离新增可信度/供应链保护机制或重要失败条件；元认知名称不等于新的可迁移保证。 |
| 16762 | 前分母关闭：non-exportable capability、可信broker、schema HTTP/SSH和anti-replay复用已有least-privilege/secret mediation机制，摘要明确只是prototype与evaluation plan，尚无改变当前设计的原始安全反证或新增有效性条件。 |
| 16774 | 潜在贡献（标准）：admission validity与后续retention consequence独立状态，controlled compression/pressure将遗漏与hoarding分开；需要核是否超出已有重要性/失效代价权重，不能只因新strength变量保留。 |
| 16778 | 前分母关闭：本地reasoning traces中心聚合/蒸馏为跨任务insight库，复用共享经验与记忆检索；摘要指标没有隔离隐私泄漏/跨域泛化条件或不同于成熟library形成的机制。 |
| 16787 | 潜在贡献（标准）：UNK造成进入模型前信号消失，与完全in-vocabulary噪声的训练分布错位用不同干预恢复；提供tokenization vs augmentation选择的受控反证，限定ELECTRA/RoBERTa/NLI。 |
| 16788 | 潜在贡献（标准）：实机器人longhorizon按fully-observable执行与ambiguity-context两regime拆分，memory并非稳定改善后者；若配对控制成立可修正长序列失败自动归于记忆的判断，而非因1000episodes retain。 |
| 16790 | 潜在贡献（标准）：相同代码下单presentation cue改变judge preference和模型排名，要求accuracy之外报告bias sensitivity；关键核human-equivalent干预/gold与重复方差分账。 |
| 16801 | 潜在贡献（标准理论）：local spatial/parameter slow-fast flow与宏观散逸/主空间对齐桥，需核具体假设及何谓unconditional，不能把Riemannian极限等同现代Transformer保证。 |
| 16804 | 前分母关闭：standard optimization form合成数据→solver reward→课程bootstrap用于OR formulation，是已知verifiable synthesis/RL/curriculum的任务应用；摘要未分离独立curriculum机制或足以改变方法成立边界的控制证据。 |
| 16809 | 潜在贡献（标准理论）：normalization导致effective LR缓慢增加，白化square-loss下延迟onset与自稳定条件不同于固定过大LR早期发散；明确stylized机制不外推一切loss spike。 |
| 16812 | 潜在贡献（安全）：同base不同植入行为finetunes上联合训练一个LoRA introspection adapter，再迁移识别隐藏/加密FT行为，改变自报告检测的训练身份与覆盖；仍需外部标签/heldout与false-negative边界，不称模型自知。 |
| 16813 | 前分母关闭：household state/task生成和tools测reactive/proactive，复杂性/partial observation造成下降是已知失败因素；题摘未给新的受控有效性边界或可迁移机制，不因personalized benchmark新增条目保留。 |
| 16824 | 潜在贡献（安全）：hidden safety state跨turn预测与CUSUM累计信号、attack/benign imagined future，控制对象从当前拒绝变为未来检测lead；要核干净false alarm/训练泄漏及何谓worldmodel，而非采用90%背景攻击率。 |
| 16826 | 潜在贡献：LoRA A/B非对称merge interference、共享B方向去强调再rescale提供不同于合并整体ΔW的机制；需控制basis/gauge身份和跨slice负例，不采用全task胜宣传。 |
| 16830 | 潜在贡献：privileged-context teacher success不等deployment confidence target，student rollout校准再OPD建立训练/部署信息边界；需核entropy/optimism理论限定与新增推理预算。 |
| 16832 | 前分母关闭：不同秘密输入的动态instruction mix trace比较是已知trace-based side-channel检测；摘要perfect detection只为有限examples，未提出新的低层泄漏模型/覆盖保证或重要反证，不能将工具名当新validation contract。 |
| 16834 | 最小消歧：batched HE-friendly网络算法与pipeline可能改变packing/memory临界路径；摘要没有具体新算子/调度，须只读这一必要机制，不把512batch的摊销收益当独立创新。 |
| 16838 | 最小消歧（安全）：摘要含proof-carrying effect/refinement/bounded model checking与运行时load recheck，须核保护覆盖和proof依赖是否不同于现有admission机制；大量test count/regulated包装不是准入依据。 |
| 16839 | 前分母关闭：Hebbian co-activation episodic graph、hub总结成semantic memory加similarity/spreading retrieval，是既有association/consolidation组合；LoCoMo收益没有改变这些方案的适用边界或独立反证。 |
| 16845 | 潜在贡献（安全）：difference分类准确率改善但自由解释harm drift增加，再用baseline-relative audit repair区分label与生成副产物；需核伤害oracle/分布及因果，不将accuracy和safety不冲突推广为一般保证。 |
| 16850 | 潜在贡献（标准）：时间加速改变接触动力学，逐步调速并由tracking error更新reference减小早期失稳，实际轨迹再训练IL；核物理reference有效性而非把10×速度当通用机器人可行性。 |

## 第七批：已读 15 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 16854 | 前分母关闭：COD foreground/background certainty决定停止token更新并将被删token压成prototype，复用置信度early-exit/merging补偿；摘要没有隔离新有效性条件或改变该方案选择的重要反证，不因foundation model/pruning关键词保留。 |
| 16855 | 潜在贡献（标准）：shared activation range由heavy-tail background主导使weak boundary进入zero-bin，再约束group clip步长/dispersion及零质量；若实验证实可细化token范围与信号损失关系，仅COD两model条件，不自动泛化LLM W4A4。 |
| 16861 | 前分母关闭：class-orthogonal block representation的soft regularizer与Fisher ratio联系、label-noise/corruption提升，摘要未给区别于成熟判别几何正则的新适用边界或重要反证；robustness emergent措辞不等新的保证。 |
| 16864 | 潜在贡献：semi-structured KV hierarchical layout与sparse tensor-core kernel同时用于prefill/decode，改变unstructured sparsity不能兑现速度的执行选择；必须核质量/真实attention与端到端成本，非据4.57×headline。 |
| 16870 | 潜在贡献（安全）：kernel MCP路径强制mediation但部分ring3 syscalls仍ungated，probe语义分类成本与覆盖分账；需要核interpose范围和bypass保证，不能把kernel位置本身等同安全。 |
| 16871 | 前分母关闭：LLM弱概念定义再环境RL refinement是成熟grounding/weak supervision组合，Atari收益与high-level goal取舍未在摘要分离新的概念有效性或控制保证；不因RL小任务拒绝。 |
| 16880 | 潜在贡献：ring流水step进度与congestion signal结合，只throttle超前flows令落后赶上而非独立拥塞公平，是collective-aware网络控制分支；AstraSim与Tofino原型范围需区分。 |
| 16881 | 前分母关闭：entity reward/轻量结构gate训练跨文化translation、unseen entity收益，属于现有RLVR在语言任务的应用；摘要未分离新探索/优化机制或可信reward有效性边界，不因14B/7k指标retain。 |
| 16883 | 潜在贡献：sink fixed-point与error-control为head跳过近零output提供依据，再用block branching/SplitK兑现执行；须核fixed-point假设与实际approximation，不能以sink或长context主题直接关闭。 |
| 16886 | 前分母关闭：partial-observation interactive任务、primitive/composition与低成本采集pipeline提出新benchmark，但摘要只给visual-motor gap概括，没有新的受控混杂分离/有效性条件；任务数量与benchmark自称essential不够准入。 |
| 16888 | 潜在贡献（标准理论）：未知参数甚至未知可验证上界的grid search由self-bounding确定范围，竞争tuned rates；须核oracle预算、ensemble选择与convex/nonconvex假设，不采fully parameterfree普遍口号。 |
| 16889 | 前分母关闭：gradient-write attribution+synergy rerank后比较KL fidelity/解释预算，是新局部score组合；摘要只给K50≈K75 operating point，未新增可迁移因果解释有效性或重要失效边界，不因CLT/patch词保留。 |
| 16890 | 潜在贡献：semantic-step marker和动态truncated rollout改变group-relative length penalty对象与探索状态，须核confidence stop的offpolicy/bias及token/step度量，非采用32%普遍预算收益。 |
| 16892 | 前分母关闭：在图像/文本embedding之间做noise-free flow matching用于DG，是成熟transport/anchor alignment的任务适配；摘要competitive榜单未分离flow路线成立条件或修正contrastive选择的独立反证。 |
| 16893 | 前分母关闭：offline decoding缓存、task reward routing、mixed offline-online、pixel budget与异步评估复用成熟video训练工程，摘要未给新的状态兼容/数据有效性/调度机制；框架名称和1.47×预处理收益不能独立准入。 |

## 第八批：已读 15 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 16902 | 原版采用关闭：官方v2 Comments已实际恢复data error affects main results，v3恢复另属04/29版本事件，不回填原版。原拟贡献不评分/selected或入Books；不误称当前全家族仍withdrawn，保留必要官方处置依据。 |
| 16909 | 潜在贡献（已最小消歧）：不采用语料/模型cutoff预设KE/KM与attention图作为内部知识因果oracle；§4.1 Table3同1-shot下reasoning SFT改善RE却降低KE/KM/IFE是具体跨维反收益，沿训练/预算条件继续必要审阅。 |
| 16911 | 前分母关闭：spec format lint与共享assets skillset/hierarchical package scope复用成熟编译诊断/包管理；摘要未给新跨skill语义有效性/执行身份保证，不把format compliance当可靠行为。 |
| 16913 | 潜在贡献（标准）：同frozen Qwen显式toggle reasoning出现nonconvergence/latency与consensus稳定性反收益；定点核trial/gold/停止条件，不采用System1结构性全面优于System2或100%安全宣传。 |
| 16915 | 前分母关闭：region chunk、domain contrastive encoder、query expansion、多跳retrieval与posthoc verification是成熟visual RAG组合；摘要高precision/grounding与渐进ablation未指定值得改变既有选型的重要有效性条件或独立失效机制。 |
| 16916 | 潜在贡献（安全）：全部unsafe选项的forced-choice移除拒绝空间，同请求open-ended对照与约束强度非单调；结构化决策的admission边界必须保留，不外推一般选择题必不安全。 |
| 16917 | 潜在贡献（标准）：同input跨语言trajectory训练/每项选择，数学规模减差异而文化任务仍依赖语言；需核知识边界固定与轨迹控制，不把语言选择全部因果归于文化prior。 |
| 16918 | 潜在贡献：PER priority时效与policy drift不同，age decay由ESS条件作用于旧priority，保留昂贵agent rollout时避免高priority陈旧垄断；要核importance correction/新objective，非普通stale-policy门槛重命名。 |
| 16919 | 潜在贡献（标准）：把deterministic reverse map作为noise-space HMC生成约束，避免measurement-guided off-manifold proposal；须核target/Jacobian/noise估计与额外compute条件，不采用免调参普适主张。 |
| 16923 | 潜在贡献（标准理论）：base/aligned likelihood ratio与偏好步骤组合、entropy weighting的检测统计；严格支配FastDetect/无条件variance改善需必要公式，不据45.82%泛化全部检测。 |
| 16929 | 前分母关闭：明确AI4Science测量抽取，通过领域taxonomy/process supervision与curriculum改善MeasEval；当前科学应用暂缓，摘要未给超出领域抽取的新基础生成/安全机制。 |
| 16930 | 前分母关闭：answer-option语义引导router、reweight专家及contrastive option比较，是conditional routing的VQA局部应用；摘要没有新负载/梯度或稳定性有效性机制与重要反证，不以MoE名称保留。 |
| 16931 | 前分母关闭：reasoning trace tree特征训练classifier并retry异常轨迹，摘要的低complexity指标提升仅新局部correctness proxy operating point；未新增可迁移判断器有效性/搜索边界，不因结构proxy命名保留。 |
| 16933 | 前分母关闭：Git commit/test-context绑定Parquet runtime观察实现semantic diff，属于通用软件版本遥测/回归诊断；摘要没有直接研究模型/AI Infra新机制，成熟观测档案可类比本项目不构成准入。 |
| 16937 | 潜在贡献（标准）：跨10语言4任务的translation-vs-native选择与resource level控制，prompt selfrouting反收益、翻译质量非唯一因素；可修正多语prompt选择条件，需heldout格式/selector预算，不称任何翻译都有效。 |

## 第九批：已读 12 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 16940 | 潜在贡献：SFT data规模改变delta幅值/谱/entropy，再用1bit主结构+residual lowrank，修正delta压缩可忽略训练规模的条件；需核不同layer/architecture实际控制，不采用生产最优策略宣传。 |
| 16941 | 前分母关闭：import mapping、Python2 detector、semantic analyzer和memory tips使LLM最后fallback，是成熟confidence cascade的dependency应用；摘要成功率未给新的可靠性/状态兼容机制或重要反证。 |
| 16943 | 前分母关闭：activation importance识别language-specific/agnostic neurons后selective FT，是成熟saliency参数选择在image translation上的应用；摘要没有隔离activation proxy有效性或保留知识的新条件，不把neuron分组命名当机制突破。 |
| 16952 | 最小消歧：物理非同源模态在高分辨率强行对齐造成负迁移，gradient buffer/降质重建可能改变alignment目标；须核是不是只为SAR/optical做局部recipe与理论口号，而非跨模态成立条件证据。 |
| 16955 | 必要消歧后前分母关闭：实际官方v1完整题摘中五种同架构conditioning与近点后验仅落实成熟input-distribution matching/低熵可少采样原则于纵向retinal操作点，未新增基础生成机制或判断低熵的可迁移有效条件；不因医学标签或小模型拒绝，不否定学术价值。详V3_BATCH_16952_16972.md，独立定点裁决待回。 |
| 16957 | 潜在贡献：压缩域int4 KV fused Metal执行与angular quantization依赖attention scale而非modelsize的新失败条件；需核精度/内存/速度基线，top1同不等全分布exact。 |
| 16964 | 前分母关闭：multiplier-free approximate sqrt与Artix7成本/错误比较、Sobel/Kmeans验证，摘要没有具体新算术机制或实质改变基础模型硬件设计的证据；局部PDP operating point不能独立准入，非因FPGA拒绝。 |
| 16965 | 潜在贡献（已最小消歧）：§3.1–3.4 CPU/DRAM双时钟ceil舍入与ZSim Bound阶段一周期响应的不可回补请求时序错误，给内部DRAM统计不等application性能的具体反证；不是泛‘模拟应校验’，只核Skylake/ZSim/Ramulator分支。 |
| 16966 | 日期终态隔离：图像→持久memory→未来planning有安全信号，但official Submitted Apr18、当前v1 Updated July13不能支持本窗首次公开，后者也不单证July owner；不评分、不采用错版HTML为April原版performance。恢复单家族官方first-public/精确正文公开范围，详V3_BATCH_16952_16972.md。 |
| 16968 | 潜在贡献（安全）：纯benign experience的执行偏好诱导危险场景过度行动，refusal经验恢复却overrefusal，是experience-driven adaptation的重要负证据；必须核base/任务/检索控制。 |
| 16972 | 潜在贡献：GRPO全正确group零adv仍漂移、majoritycorrect权重缩小，通过仅mastered hingeKL与query weighting分离consolidation/exploration；需要实际objective/预算及反例，不能以passK变高保证一般diversity。 |
| 16979 | 前分母关闭：off-the-shelf text quality/CLIP alignment筛选与adaptive long-tail sampling复用成熟pretraining数据筛选；摘要未指出改变selector有效性或selection bias边界的控制证据，不为免训练filter目标重复retain。 |

## 第十批：已读 20 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 16986 | 前分母关闭：Scala compile-time结构witness与Spark sink runtime schema比较，是通用typed-data pipeline小artifact；nested optionality规则并未直接研究大模型/AI Infra的新数据语义，不能为schema比喻自动retain。 |
| 16987 | 前分母关闭：正反agent debate、MDL explanatory burden和KB结合video真假判断，摘要没有可执行真值或新的discriminator有效性条件；可解释trace与unseen generator指标不能证明debate产生truth。 |
| 16988 | 潜在贡献（标准理论）：未知change-point与已知时刻的信息等级决定Transformer层/参数复杂度，再用同linear任务验证可行性，分离context统计与旧证据失效；真实时间序列例证不作现代大模型普遍适应保证。 |
| 16993 | 前分母关闭：城市规则constraints加VLM mental-map/detour，复用navigation policy与permission约束；摘要CVR/TC改善未分离新的可执行规则有效性或perception故障边界，不因安全任务名称保留。 |
| 16995 | 潜在贡献：用on-policy轨迹作demonstrations，交替RL与IRL重塑概率集中而非只加entropy项；需核inverse目标、额外预算和PassK上界条件，不声称任何consolidation都会抑制exploration。 |
| 17000 | 潜在贡献（安全/评价）：PII content与speaker identity分别处理，并将pretrained detector效用与从匿名数据重新训练ASR/TTS/SER分账，可能改变隐私数据发布评价；生成换身份不等匿名保证，需attack oracle。 |
| 17009 | 最小消歧：Agent-as-Tool同action协议、并发state feedback与小orchestrator SFT/RL是否新增具体异步执行/协议有效性；不能只凭planner/solver分权与并行任务指标保留。 |
| 17010 | 潜在贡献（标准）：equivalence proof和inequivalence counterexample两个label渠道，SEQ/SINQ消融显示proof贡献不同于data volume；需核评估泄漏/形式语义边界，不将Haskell验算扩为全部跨语言正确。 |
| 17014 | 前分母关闭：functionally-correct集合内的security-failure条件比率、static错过但dynamic触发的定义，已有独立functional/security witness原则；原文自限framework statement/no实证，不因FSC命名新增候选。 |
| 17016 | 前分母关闭：HRPL bug/fix合成LRPL并做跨语言课程，是成熟verified synthesis/transfer/curriculum在APR的应用；摘要没有新的defect语义兼容条件或重要反证，BLEU/ROUGE不足以改变修复正确性机制。 |
| 17019 | 潜在贡献（标准）：同task不同instruction granularity的controlled variants、planning width与U-shaped表现揭示coarse rebound可能shallow grounding；需核instruction语义等价与训练mix，不能直接给最优prompt字数。 |
| 17020 | 前分母关闭：persona×interest×harm策略合成压力测试，属于成熟persona redteam/动态数据生成；摘要难度/diversity提升没有暴露新的检测有效性条件或具体漏检路径。 |
| 17022 | 潜在贡献（标准）：gold聚合前用多annotator criterion judgment区分boundary不稳与category重叠，改变schema设计而非只平均disagreement；保留domain小样本与不可唯一真值边界。 |
| 17025 | 前分母关闭：atomic decomposition/context firewall、机器assertion registry、rollback/state locking复用已知closed-loop harness与typed execution；摘要可靠/自托管产业主张和组件消融未指出新的执行保证或独立失效边界，不因determinism口号建立全文队列。 |
| 17030 | 前分母关闭：缺模态条件重建+logit attribution用于ADNI诊断，是领域multimodal imputation和解释组合；没有基础表示/生成有效性的新机制或可迁移控制证据，不能把clinical evidence命名当系统evidence。 |
| 17031 | 前分母关闭：借persona interpretability讨论哪种实体是mind，属哲学个体化论证，题摘未提供模型表示/安全机制原证据或值得本阶段改变的系统设计。 |
| 17040 | 潜在贡献（标准）：matched spike/dense checkpoints上device实际延迟/能量和Nsight launch/kernel分账，事件稀疏不减少dense work产生反收益；限定Jetson/Darcy任务，不当neuro硬件一般失效。 |
| 17041 | 潜在贡献（安全）：query-only ownership fingerprint被semantic divergence识别/过滤，语义对齐distillation再robust perturbation改变可检测性威胁模型；必须区分未改参数/secret与all-model修改保证。 |
| 17051 | 前分母关闭：task/general importance分core/noncore再冻结，复用成熟重要性selective optimization缓解忘记；摘要没有新的importance估计有效性或保留能力保证，不能以innovation自述准入。 |
| 17052 | 前分母关闭：streaming history hierarchical event+短context先推理、uncertainty触发semantic refinement，复用成熟hierarchical memory/cascade retrieval；摘要没有具体新的event状态/执行成本或重要检索失败边界，指标不等具体机制增量。 |

## 第十一批：已读 15 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 17053 | 前分母关闭（安全消歧后）：§5.3 ASR是伦理gold-label翻转，不是执行禁止操作；D.3有norm对照但未分离新的权限/执行路径，成熟framing压力测试不能外推通用jailbreak。 |
| 17054 | 潜在贡献（标准）：one-token MLLM隐状态作为多模态embedding、SVG结构语义rewrite使symbolic视图不被rasterization丢弃，是训练/提示控制两条检索表示分支；需核生成预算与对照，不把一次token当免compute。 |
| 17055 | 前分母关闭：PR/Jira/日历/MCP/A2A观测聚合的开发工作台与自身readiness评分，属于工具整合；自测48→98不建立模型/Infra可靠性或新的评价有效性。 |
| 17056 | 潜在贡献（标准）：固定mention graph工具下证据scatter与controller强度决定LLM探索收益，discovery与vector ranking分开；GraphRAG局部差异不显著/strongcontroller才显著的反证收窄Agent控制选型。 |
| 17064 | 潜在贡献：不fork container engine、只在scheduler/image access/host injection分层进行HPC integration，CrayGH200匹配Enroot/Pyxis scale性能而startup变化；需核image缓存/多容器语义和训练条件，不从workloads推生产普胜。 |
| 17066 | 前分母关闭：coherent infrastructure/supply-chain状态概率的reference-state MonteCarlo分类，主要使用batched matrix加速风险估计；题摘研究传统可靠性应用而非模型优化/基础设施执行机制，不能因矩阵运算借力ML保留。 |
| 17067 | 潜在贡献（标准理论）：沿实际轨迹而非全域的PL/errorbound/quadraticgrowth，active polyhedral face的Hoffman常数决定local convergence；需核可验证轨迹保持与假设，不外推Transformer优化保证。 |
| 17068 | 潜在贡献：consecutive denoising KL稳定度参与unmask score，改变单step confidence提交选择；KL对剩余masked信息的严格下界是中心保证，必须定点核conditioning，不默认所有temporal instability不安全。 |
| 17072 | 前分母关闭：递归outline重写、AVR intent布局和cognitive-load metric组合已有research写作/多模态layout方法；摘要排行榜没有分离新的state兼容或evaluator有效性机制。 |
| 17073 | 潜在贡献：RLVR同时训练answerability、明确abstain和正确missing-info clarification，改变generic refusal reward不足的目标；需核clarification oracle与calibration，非模型规模自然自知。 |
| 17074 | 前分母关闭：query-centered reference graph和difference aggregation用于video quality，复用comparative quality/图消息传递；摘要仅数据集指标/跨集泛化，没有改变reference有效性或相对评价选择的重要条件。 |
| 17078 | 潜在贡献（标准理论）：task-feature specialization、weight disentanglement与taskvector几何之间的因果/充分条件桥；orthogonality作为可控proxy不自动保证functional independence，需核OrthoReg理论的逆向成立限定。 |
| 17079 | 前分母关闭：Reddit叙事逐turn揭露与SSBC/probe描述distress相关support策略，是社会支持应用观察；未新增基础模型机制、因果辨别或可迁移控制有效性条件，不把probe相关性当心理state真实拥有。 |
| 17082 | 最小消歧：primitive surface绑定3DGS appearance、deformation控制rigid articulation与adaptive primitive count是否新增明确表示/状态约束；摘要fidelity优胜不足以建立worldmodel/物理闭环贡献。 |
| 17085 | 前分母关闭：新IIE三元组pipeline和人机隐含推断覆盖/保守度比较，属于pragmatics局部任务与labels研究；摘要没有受控生成机制或足以修正长期能力判断的独立有效性边界。 |

## 第十二批：已读 16 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 17087 | 潜在贡献：token subset用MLLM output loss/semantic diversity离线evolutionary labels，再训练小compressor；与attention/similarity heuristic不同的监督owner与离线/线上成本，要核loss真值与label预算。 |
| 17090 | 前分母关闭：skeleton识别器的gradient语义引导coarse-to-fine motion diffusion，复用classifier guidance与联合recognition/generation；13榜单没有新增生成validity/物理约束或重要反证。 |
| 17091 | 前分母关闭：atomic tools、hierarchical memory、verified SOP复用和context压缩组合已有information-budget机制；information density命名与系统排行不能作为新的状态/执行有效性条件。 |
| 17092 | 前分母关闭：provider token/cost registry、response checks与Prometheus/gateway dashboard复用成熟计费观测；工作流billing偏差<2%不改变模型/Infra设计解释，不为统一面板列论文候选。 |
| 17093 | 潜在贡献（安全）：RTL/Trojan/sidechannel请求的合法安全query过拒与语义伪装攻击漏拒，揭示generalhazard guard在硬件artifact风险的边界；需核outcome oracle而非只文本compliance，不用silicon不可逆作宣传。 |
| 17097 | 潜在贡献（标准）：同202任务6IR×3model通过compile/sim/synth多层gate，IR比模型影响大且conditional FPGA pass由simplicity-fit混杂；能改变代码representation选型与报告分母，不是单榜单。 |
| 17102 | 潜在贡献（标准）：matched decoding108配置改变RTL model排名且跨suite最佳配置近零相关；真实性能取决于configuration，需统一调优预算/selection与heldout，不照best-worst极差推广。 |
| 17104 | 潜在贡献（已最小消歧）：官方v1现为TensorHub，库存TStore保留alias；raw-bit TensorSketch→ratio预测→online base/split联合完整base成本是Ch59实际缺分支，非新系统名即保留。拟6分gap深入；192线程全内存无I/O与逻辑identity不合并。 |
| 17105 | 潜在贡献（标准）：token-syllable misalignment与phonological local/global representation、IPA FT保留能力成本，增加词表信息loss的一条受限诊断；probe关联与tokenizer因果要分开。 |
| 17106 | 前分母关闭：有限LTL公式tree的true/false/open进度监控与将来reward/exploration建议，复用成熟三值temporal monitoring；只有示例/未来RL集成，未给新的语义监控保证或实际控制有效性。 |
| 17108 | 潜在贡献（标准）：word≠mention的morphology使常规CR打分错位，subword/multiword标注协议和encoder/decoder相反趋势，直接改变tokenization/评价接口；不泛化Hebrew优势或小模型普遍更好。 |
| 17111 | 潜在贡献（标准）：concurrent API agent资源contend下retry比admission更关键的受控ablation，提出透明proxy执行机制；需核retry idempotence/额外配额和aggregate-capacity，不以OS类比准入。 |
| 17112 | 潜在贡献（标准）：单模型自一致低不确定仍共同答错，inter/intra semantic similarity差提供条件ensemble disagreement补充；需核同modelsize/生成预算与ranking calibration，不称sum=真实epistemic概率。 |
| 17114 | 前分母关闭：PubMed citation audit暴露临床答案正确但citation假，temporal KG绑定可验证来源，重申relevance/correctness≠citation provenance的成熟原则；摘要领域场景与203引用不建立新增artifact/provenance机制，不扩大当前临床应用。 |
| 17115 | 前分母关闭：opticalflow warp、entropy/forwardbackward consistency按权重blend视频mask，复用temporal smoothing与不确定融合；四序列收益未给新模型状态有效性或可迁移故障边界。 |
| 17121 | 前分母关闭（必要消歧后）：§3–5的三维递归taxonomy、serial-capacity/linearSSM表达性引用和未来议程，未新增证明/受控证据或解决具体争议的综合结论；不是按综述标签拒绝。 |

## 第十三批：已读 16 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 17125 | 前分母关闭：MCP regex/phrase/entropy分层、BGE与本地LLM fallback、输出pattern filters复用成熟classifier cascade；新攻击题库与precision/recall operating point未新增信任边界或独立保护有效性条件，不因MCP/security名称全部深审。 |
| 17126 | 潜在贡献（标准）：同DETR proposal与CLIP chooser下语义相近prompt选择不同实例，embedding距离只解释部分差异且ensemble无收益；定点核实例身份与控制，不能把相关分析直接当argmax的唯一因果解释。 |
| 17132 | 潜在贡献（安全）：拒绝token未被选择而非不可用，并以极端system prompt两分布动态调整解码，可能改变过拒/漏拒取舍；必须核真实unsafe outcome而非仅是否说拒绝，不自动采纳一般安全保证。 |
| 17137 | 前分母关闭：PageRank与common-information环境结构策略作用于传统coverage/patrol/reachability，题摘未给直接支撑大模型或其Infra的新表示、训练或执行机制，不因多Agent术语泛化。 |
| 17139 | 潜在贡献（安全）：离散回答投票与token级共享生成的耦合不同，恶意多数下诚实模型恢复力的条件可能改变通信方案；需核operator/theory前提，不把有限任务结果写成Byzantine普适保证。 |
| 17140 | 潜在贡献（标准理论）：probabilistic dependency graph的local inconsistency resolution与GFlowNet目标/收敛分支，需核新增可计算机制而非统一术语本身；不从离散合成例证推一般LLM训练保证。 |
| 17142 | 前分母关闭：LLM制造分配经temporal logic/discrete-event checker后执行，是成熟proposal→验证器在装配任务的应用；摘要未给新的语义有效性、状态兼容或独立失效边界。 |
| 17143 | 潜在贡献（标准）：闭合文档语料内的信息完整性与检索relevance分开，漏找passage可按有限inventory评价；需核section/groundtruth oracle和开放主题边界，不把查完有限语料等同世界知识完整。 |
| 17145 | 潜在贡献（标准理论）：negative momentum对minmax的全局收敛/加速条件挑战旧判断；必要假设和预算可改变特定优化分支，但不外推大模型或GAN无条件稳定。 |
| 17147 | 最小消歧：vectorized road/actor状态与cross-attention视频控制可能只是既有geometry conditioning组合；只核表示/时间约束是否新增可迁移机制，不因场景生成首次命名或质量优胜retain。 |
| 17148 | 前分母关闭：model-card选3/6专家、顺逆序debate graph消息传递及pooling是成熟路由/辩论组合；更少agent胜baseline未分离新的通信有效性或规模边界。 |
| 17153 | 潜在贡献（标准）：同法律决策模型任务中raw/SRL/I-O/联合四条件分离表示因素，I-O约束收益而冗余pass-through削弱收益，结构similarity与functional execution不同；受限控制证据可报告，不把领域总体成绩外推。 |
| 17159 | 潜在贡献（标准）：同CTF任务中environment×prompt×model组合的控制，Kali工具收益与提示反收益、planner/executor混搭无优势，可能修正Agent benchmark归因；核工具/预算后采用环境条件，不做模型榜单宣传。 |
| 17163 | 潜在贡献（安全）：空间定向noise对地点检索泄漏与效用的取舍，equal-utility全局noise追平和跨retriever负例收窄优势；需核adaptive mask与DP-style措辞，不把噪声校准写成正式DP保证。 |
| 17166 | 前分母关闭：asset-pricing因子稀疏基与组合收益研究属于金融应用；题摘未新增基础模型表示、优化成立条件或Infra执行机制，不能因非线性特征类比保留。 |
| 17172 | 潜在贡献：GPU lossless compression与P2P split-send、persistent collective融合直接改变通信/压缩重叠与内存traffic；需核bit语义、entropy、网络/SM竞争和端到端成本，非孤立压缩率与峰值收益。 |

## 第十四批：已读 15 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 17174 | 前分母关闭：四维心理标签联合benchmark、hyperbolic映射及alignment tuning复用成熟层级表示方法；题摘将领域hierarchy与Euclidean容量作类比，但未提供改变基础模型容量判断的独立证据或可核的新机制，不把几何口号和单榜单自动准入。 |
| 17177 | 潜在贡献（标准）：240次FT中逐层等化相对参数更新是直接干预，depth-locality在架构/目标/规模条件下保持或消失，能修正‘后层改变只是梯度大’的解释；需核控制本身改动objective/优化路径，非普遍layer定理。 |
| 17180 | 潜在贡献：branch-mutate-evaluate与持久分支并发区别于nested transaction，生命周期成本与深分支read成本的反向排序可能改变Agent探索存储选型；不采用未经工作负载绑定的5–4000倍或所有系统无可行性。 |
| 17182 | 潜在贡献（标准）：共享prefix生成中控制token identity与compile-equivalent output后分层MoE route重合，给‘context-independent routing’与搜索多样性重要限定；assembly等价只在gcc -O0条件下，不作程序语义完全等价。 |
| 17184 | 前分母关闭：SFT/RFT router与compile/static/security/public-test reward、best-K选择组合已有verified-repair机制；摘要的五模型收益未新增reward/witness有效性或新的安全修复边界。 |
| 17187 | 最小消歧：单app模型排名与硬件档次不能准入，但temperature=0采样挂起、thinking trace进入file-path parser可能是具体接口故障；只核是否有可重现输入/版本及执行机制，不以一个周末实验泛化训练数据缺口。 |
| 17188 | 前分母关闭：teacher推理trace蒸馏、staged SFT与多指标GRPO用于多角色摘要是成熟训练组合；题摘faithfulness/偏好改善未给新的监督有效性或可迁移失效边界。 |
| 17191 | 前分母关闭：LLM自然语言描述生成coordination graph，再由GCN MARL学习，是既有语义prior在MPE任务的应用；题摘没有基础模型推理/通信或prior有效性的新机制与重要反证，不因模型仅1.5B否定也不因LLM作为工具直保。 |
| 17197 | 最小消歧：fine-grained score-ranking loss能否比成熟多目标偏好/条件控制多出独立选择机制，题摘未清楚给定；仅核目标和控制接口，不以三个模型/摘要指标新增候选。 |
| 17198 | 潜在贡献（标准理论/工程）：多operand层级sparse tensor partition推广parallel merge并给load-balance条件，直接作用CPU/GPU kernel代码生成；需核保证对应工作量/分割开销，不把vendor几何均值当通用收益。 |
| 17200 | 最小消歧：GIRB与individual/average proxy若仅复用isotonic calibration不新增长期机制；只核无reference/human inference和训练groundtruth的权力区分、group条件是否改变有效性，非七数据集本身准入。 |
| 17207 | 潜在贡献（标准理论）：KL正则regret与temperature-zero decision regret评价对象不同，改变greedy online alignment的理论判断；需核finite response/噪声/识别假设，不把O(1)推广为一般RLHF计算效率。 |
| 17210 | 潜在贡献（安全）：选拒绝模板token对logit加约束是与分布KL不同的FT保护分支；需核token保护与真实安全行为/任务utility之间的有效性，不将保持拒绝词汇等同安全策略。 |
| 17211 | 潜在贡献：双音频look-ahead与因果用户交互不兼容，改为单stream、frame级listen/speak状态和调度是一条实际在线生成约束分支；需核state/scheduler和质量/延迟预算，不因四步sampling保证实时SLO。 |
| 17215 | 潜在贡献（安全）：梯度幅值选择训练样本与安全漂移/任务学习分账，可能改变持续适配数据策略；需核梯度归因、选择预算与baseline，摘要相关性不能直接证明高梯度唯一导致遗忘。 |

## 第十五批：已读 15 个完整题摘

| 家族 | 题摘裁决与具体依据 |
| --- | --- |
| 17217 | 前分母关闭：固定图像冲突文本测shortcut，再叠hard negatives/smoothing/layerLR/restarts/curriculum/augmentation，复用已有模态必要性与多组件训练方法；摘要没有归因哪项改变有效性，attention可视化不证明因果，不以toy或小CLIP单独拒绝。 |
| 17219 | 潜在贡献（标准理论）：Gibbs posterior的有限样本PAC-Bayes界用singular marginal integral表达数据/内在复杂度，可能改变过参数化generalization的可计算条件；须核先验/损失/积分可取假设，不当现代Transformer风险保证。 |
| 17221 | 必要审阅后标准Only：v1仅Coupled-BIM/Coupled-GM两种（库存三分支是后版污染）；state-input selectivity与shared state职责分离，删动态selectivity的GM才scan-compatible，不是BIM精确等价；受限任务排序与代价保留，不外推语言模型。 |
| 17224 | 具体日期隔离：官方OpenReview工作坊同题/作者正文已发现但public-note时间因challenge/403未恢复，不按April新ID重复首发或selected；必要Alg1旧Z/新Q重建桥未明仅保留风险，日期恢复后定点审，不查全发表史。 |
| 17225 | 前分母关闭：Planner/Executor/Verifier零样本CoT用于表格claim，是成熟分解/计算/验证组合；多个榜单及小模型近大模型不新增验证器truth或执行有效性边界。 |
| 17227 | 前分母关闭：cloud-native/distributed微服务、autoscaling、serverless/federated/quantum议程归纳，没有原始机制/新综合反证解决具体设计争议；不为目录和研究趋势建立候选。 |
| 17228 | 潜在贡献：controlled conditional-depth预算下删oracle utility/rank监督反而改善训练，all-future-full标签与真实gated future不兼容；直接改变gate辅助目标选择，保留157.5M/controller-only/50%预算/三seed，不外推所有aux-loss有害。 |
| 17234 | 前分母关闭：任务taxonomy、semantic/structural候选、centroid扩展与constrained LLM rerank组成MCP推荐，属于成熟检索/兼容过滤在工具目录的应用；题摘未给新的admission或兼容性保证。 |
| 17237 | 贡献准入：有标签的attention-domain preference/head选择和最深选中层执行截断，改变训练—读出—执行身份；已核v1为211query派生多对、格式非排名真值。6gap深入，Ch76普通提案待真实采用/写后，见最后批记录。 |
| 17238 | 官方撤回关闭：当前abs明确withdrawn，v2 04/25；Comments为披露时机/适当性，不是已证明攻击无效。按合同不selected/评分/采用，只保留必要原始关闭依据，不再追正文。 |
| 17240 | 前分母关闭（安全消歧后）：有限K循环仅保证终止返回fail，risk单调另需agent响应假设，安全fallback全状态可行也是假设；连续projection/离散search确有区分，但未证明新policy编译有效边界，三类企业模拟不是一般安全保证。 |
| 17241 | 前分母关闭：对象/功能区hypergraph与三视图contrastive encoder注入VLM规划，是成熟结构编码/一致性学习组合；摘要执行收益未新增可执行世界state或表示有效性条件，不因具身领域本身拒绝。 |
| 17244 | 贡献准入/6标准Only：action候选控制与token随机性分离，实际MAB/TALES反证、额外调用和Jericho退步已核；sequence logprob非环境信息增益、proxy可负，不作confidence/普适regret保证。 |
| 17248 | 贡献准入/5标准Only：真实人声开放生成与合成MCQ测量对象不同，actualv1为11模型；属性抽取/nTVD与内容/说话人、任务规范条件已核，不把分布偏移视为全部公平性/因果或排行榜真值。 |
| 17249 | 潜在贡献（安全，日期待核）：共享physical prefix-KV bitflip的选择传播/持久累积，与weight corruption不同；software ideal targeting不等实际Rowhammer exploit，checksum scheduling只在自身故障模型中限batch。v1Updated01:00:06Z跨截点，不能定为本窗；先保留具体日期例外，不因此提前正面采用。 |

以上累计实际读270个完整题摘；是有限贡献判断范围，不是270项冻结候选，更不是1,260项全部摘要/全文已读。首次公开、必要消歧和证据审阅仍分别待执行。
