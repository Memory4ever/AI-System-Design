# Jun16补遗漏作者记录

作者 `supp_jun16`；唯一reader `jun16_review`。只补2026-06-15 BJT自然日，保护原100候选及其日期/评分/小时窗/有效证据；不写State/index，不stage/commit/push。已完整重读本日AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、来源使用与Daily/arXiv组、统一Prompt、ROADMAP、本日State路由。使用using-agent-skills的范围与验证原则；本任务是现有合同研究补查，不另起软件开发规范。

## 1. 实际来源发现层与首批准入

实际请求脚本 `SUP_FETCH_20261026.py` 记录URL/主题/参数，原响应 `SUP_RAW_*_20261026.raw`。其中DataCite四主题组为titles.title常见同义表达，分别返回LM81/System31/Agent85/Multi53，一页size1000各自total等于返回数；跨组去重214身份。这是Jun15 registered发现集合，不是214篇已落窗或已读全文，不把宽分类/月列表作逐项关闭队列。日窗参数为 `registered:[2026-06-14T16:00:00Z TO 2026-06-15T15:59:59Z]`，client-id=arxiv.content。Jun15为BJT周一，对应周日ET20:00正常公告；启动即时消息的一次日历口误已当场更正，从未用于记录/处置。

日期按精确v1提交+官方公告/公告时发号规则+同DOI findable arxiv.content registered联合限定；created不作最晚上界。目标日较早提交的材料最早界可能早于Jun15，不因此把registered改称公开日；此类拟入选先记具名日期恢复缺层。历史规则复用合同指定2025-01-06官方snapshot有效层；当前规则本次下载轻核。最终以具体原字段和检查结果为准。

### 首批P（潜贡献明确，实验可信度待必要正文核验；尚未宣告证据完成）

以下完整题摘已从DataCite descriptions(Abstract)逐字读完，原件身份可直接按DOI查询；两准入入口同标准，不设比例。

| family | 旧约束 → 实际增量 → 重新考虑的选择 | 日期层 | 拟分 |
| --- | --- | --- | --- |
| 2606.13795 DiPOD | diffusion policy ELBO代理可能与真实log-likelihood/return梯度双漂移 → on-policy ELBO正则+自蒸馏维持tight bound → RL更新不能把代理优化等同策略改进 | Jun11 18:06:04Z v1至Jun15 01:41:02Z registered，完整区间Jun15 BJT | 3+2+3=8 |
| 2606.13796 Recursive diffusion | 即便完美score/采样也可能因reverse early-stop递归丢失高阶模态 → limiting distribution+Hermite谱与渐退截断定理 → 递归合成数据退化不能全归因拟合误差 | Jun11 18:06:26Z→Jun15 01:41:03Z；同Jun15 | 3+2+3=8 |
| 2606.13814 TASR | learned retrieval stop绑定模型/任务 → 答案连续稳定+校准margin固定阈值，在32配置/预算对照中检验 → 可审计stop sensor与泛化/校准代价 | Jun11 18:35:14Z→Jun15 01:41:26Z；同Jun15 | 2+2+2=6 |
| 2606.13815 Poker Arena | scalar胜率混同多维策略/记忆贡献 → chips与9轴排序不一致+记忆受控反侧 → leaderboard不能替代维度分离；仍需核轴定义/对照 | Jun11 18:39:25Z→Jun15 01:41:27Z；同Jun15 | 2+1+2=5 |
| 2606.13817 FlowMo-WM | action-only瞬时运动遗漏隐藏慢漂移 → 短运动态/长外因context分解+zero/shuffle干预 → world state需承载不可见外因但不等同因果识别 | Jun11 18:46:43Z→Jun15 01:41:30Z；同Jun15 | 2+2+2=6 |
| 2606.13861 TBS | denoising搜索无法修复已提交空间轨迹/BoN重弃正确前缀 → temporal verify/restart保留prefix，matched-budget反侧 → 视频推理compute应按已验证时序分配 | v1/registered待精确helper复算 | 2+2+2=6 |
| 2606.13862 SuperThoughts | 连续latent失监督/不稳 → 两离散token压成latent+MTP双decode且保留训练监督，低置信退普通 → 推理压缩需质量/吞吐/回退同核 | v1/registered待精确helper复算 | 2+1+2=5 |
| 2606.13873 NULLs | source参数隔离与共享学习相冲突 → shared backbone+source sinks禁用式unlearning及relearning反侧 → 删除能力应在训练因子化中设计，不可把停用等同法律删除 | v1/registered待精确helper复算 | 3+2+3=8 |
| 2606.13877 ContactWorld | 低prediction error未必提高闭环操控 → 固定WM/训练/planner的视觉触觉表示比较+900真机试验 → 表示选择需闭环证据且触觉收益非普遍 | v1/registered待精确helper复算 | 2+2+2=6 |

### 日期必要缺层（潜贡献，不先评分/列确定当窗候选）

**撤回纠正：13856不再拟入选，不评分、不采用、不进入Books。** reader首批校准发现current DataCite dates明确Withdrawn，作者即时打开官方 `https://arxiv.org/abs/2606.13856` 确认 `This paper has been withdrawn by Jeffrin Sam`；v2 Aug25撤回，Comments说明reference错误且继续开发novelty。前一拟分未冻结，现清除，仅保留原始排除链。同批轻核还发现14066 FastContext官方元数据Withdrawn v4（IP issues），后续不送准入。

13685 judge重复波动/位置与prompt混杂；13686欺骗GUI注入；13705稀疏神经元loop修复及doom-loop反侧；13706证明通过与检错/真空/核心覆盖不同；13707决策对齐GRPO；13708 memory-side ISA折叠paged KV寻址依赖；13709 support-gated多方向MoE拒答干预；13715 WorkBench能力/有害动作共同变化；13731可执行BI state/log与同backbone消融；13733 task constraint cut通信上界；13737 future-aware streaming guard；13740 NPU双路修订与address remap；13757 PR narrative误批安全；13763 coding agent语言成本/cheating验证；13768 entity-temporal双RoPE；13769跨embodiment 3D trace。
它们较早Submitted最早界跨日，registeredJun15不能单独定日；将依具体官方公告证据恢复，不无限追假想早稿。13683个性portrait+NRPA需核是否真新policy适配机制才准入，暂未定。

### 代表N（已读完整题摘）

- 13692 Agentic Data Quality：intended-use→多agent生成规则→feasibility→确定性执行是既有步骤组合，摘要未新增gate算法、可靠性成立条件或足以修正判断的具体反证；适配同数据集场景不足。日期未核，不影响前N。
- 13722 YeasierAgent：symbiotic/narrative/scene概念与跨平台app组合；无可核新执行机制或可靠性证据，不能把新名词作为平台增量。日期未核。
- 13725 memory lab：DRAM Bender基础设施更新，题摘没有通向模型训练/推理的具体新约束/机制，只泛称memory bottleneck；不可仅因Ch54映射准入。日期未核。
- 13735 VHDLSuite：Verilog→VHDL基准合成和已有VUnit/GHDL执行验证，主要新语言覆盖/200题；摘要未见改变模型/系统判断的具体盲区证据。日期未核。
- 13747 BigPower：以LLM表示作CPU功耗surrogate的领域应用，没有服务LLM计算的编译/kernel/训练机制；范围外。
- 13751 inheritance reasoning：共享任务模型比榜+提示策略，未新增主线机制/可复用边界。
- 13760 political orientation：11模型20次问卷描述性分布，没有隔离训练/architecture/moderation因素的机制或评价混杂新结论；不能把提及run variance自动算可靠性贡献。
- 13840 MAEAD survey：汇总400篇，指出simulation/real-time safety未证实；未发现新的实证反证或可验证维护机制，主题相似不等于增量。
- 13844 Ramulator2.1：新增HBM/LPDDR等标准及配置/验证基础设施；题摘未给LLM workload下改变内存系统设计判断的机制/约束，不以version或硬件名准入。

当前仍普通待办：剩余主题命中完整题摘与有界标题补检、日期缺层、全部P必要证据/owner/最终六节；不得把普通未做写成终态。

## 2. 后续完整题摘准入（2026-10-26；未以摘要计Evidence）

下面均已读完整题摘；当前DataCite摘要可能是后版，须回exact-v1采用。此处为候选增量提案，不声称实验可信或Books已通过。除早提交组外，v1均Jun11 18:00Z后至Jun12 18:00Z前，正常最早公告Jun15 00:00Z；仍由helper逐项核findable/client/同DOI/唯一v1和精度。全部下述P的唯一必要首备为作者，reader做定点独核，不另起平行Methods。

| family | 具体新增命题：旧约束 → 增量 → 改变的选择 | 拟分 |
| --- | --- | --- |
| 13872 Avatar V | 固定identity embedding丢动态特征 → full-reference token与稀疏非对称attention线性条件化 → 身份一致性须含行为且核reference长度成本 | 2+2+2=6 |
| 13878 AnyGoal | closed-set detector/稠密3D记忆约束 → persistent贝叶斯value-map融合VLM与探索UCB → navigation须分探索与goal verification反侧 | 2+2+2=6 |
| 13883 aerial reliability | clean训planner错把反光等当证据 → distill VLM可靠性热图为虚拟障碍cost → perception confidence需入控制预算/不等于真安全 | 2+2+2=6 |
| 13884 RACG | predictive confidence不等于action risk → counterfactual risk gate+分布无关条件界 → 需核因果假设/shift后保证范围 | 2+2+2=6 |
| 13886 PhysVLA | temporal smoothing不修物理不一致 → phase FSM+选择性动力学gate且冻结backbone → runtime与模型权责/额外state oracle边界 | 2+2+2=6 |
| 13904 SANA | end accuracy混search/planning/analysis/policy错 → 同budget gold工具替换消融 → 剩余gap只能条件归因policy | 2+2+2=6 |
| 13905 ADORE | 生成式query扩展会drift → corpus retrieval/relevance反馈强化与抑制词项 → 扩展需实际语料闭环而非反复自写 | 2+1+2=5 |
| 13931 DLawBench | 静态legal问答不测缺事实获取 → personality/信息elicitation分层及指导不足反侧 → 信息需求越强时的交互能力不能由单轮score代理 | 2+1+2=5 |
| 13944 deployment values | prompt paraphrase不足以确证固定model preference → 控制deployment framing的1.2M决策 → value测量需绑定task context，不外推安全保证 | 3+2+3=8 |
| 13945 LatentDx | raw KV通信仍泄露prompt → same-backbone蒸馏/跨family latent对齐+reconstruction对照 → latent压缩不能先验等同隐私 | 2+2+2=6 |
| 13949 MINIM | full UI外发泄露无关敏感信息 → trusted local必要/敏感双score三态披露 → privacy最小视图需保action affordance | 2+2+2=6 |
| 13964 CaricHarmony | identity/shape条件互相污染 → 三并行纯/合成diffusion路径以attention能量融合 → conditioning冲突需隔离且计算/identity tradeoff同核 | 2+1+2=5 |
| 13968 STREAM | HPC batch控制通道不适合token流 → dispatch与WebSocket relay解耦并加密 → TTFT必须分队列/relay/模型且不能由路由judge自证质量 | 2+2+2=6 |
| 13982 ANTS | 固定top-p阈值跨budget不稳 → entropy控制logit邻域+不截断回退 → sampler是训练/推理分布控制且code低预算有反侧 | 2+2+2=6 |
| 13989 CTMC TTS | 单调unmask早承诺难纠正 → conditional coupling+schedule受限remask → 低NFE语音条件化需revision而非盲并行 | 2+2+2=6 |
| 13994 DeCompBench | 单步安全不阻benign子任务组合恶意 → 图式decomposition-by-design对照 → 安全评估单位需跨完整执行意图 | 2+2+2=6 |
| 13995 Dialogue SWE | autonomous coding分数不测dialogue → persona用户模拟+schema agent且coding强不等于dialogue强 → 交互可靠性单独评价 | 2+1+2=5 |
| 14000 Lean audit | kernel acceptance不保原命题忠实 → semantic/Mathlib/crossfile审计见弱化假设等 → verifier通过不等价需求满足 | 3+2+3=8 |
| 14024 ViT-Up | 外部浅图像guide引入feature leakage → 从ViT中间state构造continuous coordinate query → dense upsampling需backbone空间一致而非视觉锐利 | 2+1+2=5 |
| 14027 SOPGuard | script SOP不覆盖agent跨origin信息流 → BrowserOS执行级SOPGuard/bench → browser安全principal须含agent通道 | 3+2+3=8 |
| 14037 directional compliance | 单向抗pushback测量混 helpful/harmful → 双向asymmetry发现CoT同步放大两侧 → alignment不能只压compliance率 | 2+1+2=5 |
| 14047 KG memory | similarity弱于entity state/relations → 动态KG与分memory融合对照 → long-context外置state需核建图端到端成本/准确率 | 2+1+2=5 |
| 14048 WAM4D | dense4D解码拖慢action且未来geometry泄漏 → train-only register读出+causal mixture visibility → 训练几何监督/部署action路径必须分离 | 2+2+2=6 |
| 14058 ReactSim | simulator联合控制AV掩盖reactivity → 独立偏离log的AV输入及重新规划频率 → WM闭环评价需干预可控主体 | 2+2+2=6 |
| 14061 visual repo | vision-only缺符号细节增加query → 文本+结构图受控对照且stage差异 → 视觉补充不能直接替代symbolic工具 | 2+1+2=5 |
| 14084 SDN | 扩散noise随机性关联spurious cue/动作抖动 → 分散noise候选+trajectory一致选择 → testtime稳健需核候选预算与动作反侧 | 2+1+2=5 |
| 14106 AGMem | screenshot全图memory降state错却增action错 → actioncrop记忆及故障类型对照 → memory表示须绑定恢复动作而非相似画面 | 3+2+2=7 |
| 14117 associative interference | refusal混任务正确性 → compliance/classification两阶段模型 → 心理范式迁移需条件分母而非统一bias结论 | 2+1+2=5 |
| 14122 UTF8 | byte模型perplexity稳不代表结构有效 → 控制协议发现validity滞后与频率反转 → tokenizer训练验收需另测编码有效 | 3+1+3=7 |
| 14125 SimEdit | 文本条件调velocity几何/跨支attention → 条件精修与tokenwise不对称控制 → inversion稳定性不只是采样公式 | 2+1+2=5 |
| 14127 CoRe | offline reward未对齐部署rank融合 → 真实融合代数reward/phase sync/subset DPO及reward-hack gate → reward与部署及promotion需同版本 | 3+2+3=8 |
| 14142 PauseRec | SID破坏自然语言接口 → 分解grounding/rationale原因+隐式pause推理 → 非语言标识的CoT收益不可从文本任务迁移 | 2+1+2=5 |
| 14150 pruning vs scratch | 只比recovery budget偏向pruning → token匹配与全pipeline token匹配的granularity反侧 → 压缩是否便宜需明pretrain sunk cost | 3+2+3=8 |
| 14153 encoder scale | 小backbone最优encoder不转移 → frozen graft/native/shuffle多seed对照 → graft包装器非中性且offline MSE非闭环 | 3+2+2=7 |
| 14154 SkillMutator | 静态scan语言或code漏跨模态交互 → mutation反馈攻击+四阶段蒸馏scanner → install检查须联合语言/执行语义但不宣称安全证明 | 3+2+3=8 |
| 14155 GTBP | 多LLM prompt优化credit不清 → DAG反传target discrepancy/stage update及条件收敛 → prompt图优化需显式local target/优化器假设 | 2+2+2=6 |
| 14162 VideoWeave | 显式depth监督把重建错传generator → geometry隐latent与video联合denoise → 几何条件可变软但不等价真实动力学 | 2+1+2=5 |
| 14168 MUSE | 全scene重生成损非目标内容 → requirement状态+局部操作/外部preservation checks → 编辑评价需分goal与未授权改变 | 2+2+2=6 |
| 14179 CacheRL | fuzzy缓存rollout会改环境与reward真值 → tier-aware mask/reward → 降live成本要显式缓存不确定性/离策略限制 | 2+2+2=6 |
| 14199 OdysSim | helpfulness posttrain改变用户模拟行为 → 行为轴与RL judge hack检测、OOD真人reaction对照 → simulator拟人相似不等于真实交互分布 | 2+2+2=6 |
| 14200 trust conditional | global score忽略异质技能 → 条件信任相图+借证据的laundering攻击 → 统计效率收益与零证据routing风险同核 | 3+2+3=8 |
| 14210 split leakage | input-only隐私评估漏response → dualside patch inversion+localadapter/MI防护 → split activation需双端威胁面 | 3+2+3=8 |
| 14211 RefGRPO | outcome reward不校准post-feedback自评 → reflection/outcome bonus+dynamic coeff → self-verifier仍依环境真值不能自证 | 2+2+2=6 |
| 14219 PMR | remote reasoning延时使全程调用不适飞行 → local安全loop+learned invocation value gate → agent只能提有限恢复skill、运行时验收 | 2+2+2=6 |
| 14240 Affordance20Q | explicit object identity泄漏affordance捷径 → 隐藏身份/IG诊断及KB rule → physical属性推理不可由命名知识替代 | 2+1+2=5 |
| 14243 DMoE | 参数更新破cache/forgetting → base/router/expert解耦且末层FFN注知识 → 模块可更新性须与KV lineage并核 | 2+2+2=6 |
| 14249 HarnessX | static scaffold难归因/优化 → typed substitution algebra/trace evolution/model信号闭环 → 必须核类型代换约束是否超成熟流程组合 | 2+2+2=6 |
| 14269 ScoreGate | fixedK/single score漏语汇错配 → bi/cross encoder score融合自适应cardinality → 成本/recall应同看且零FP不可安全外推 | 2+1+2=5 |
| 14278 Judge-LS | English结果外推跨语言judge → label-preserving翻译/切换的pair/tie probes及审计 → preference flip不等价英语偏爱 | 3+1+3=7 |
| 14302 RePro | 直接progress prompting反降task → hindsight轨迹差分与online alignment → dense selfreward须核未来信息仅训练/credit反侧 | 2+2+2=6 |
| 14314 CPE | communication仅text不测UI/task/persona取舍 → channel对照+rollout prompt演进 → 交互协议是可优化policy但不等同新执行模型 | 2+1+2=5 |
| 14317 CausalMotion | implicit视频prior不保物理约束 → VLM关键帧/轨迹中间表示软引导 → VLM物理解释不是真动力学oracle | 2+1+2=5 |
| 14347 language geometry | 语言非独立概念 → covariance-adjusted inner product分离/家族结构残差 → 跨语言intervention需防共享子空间side-effect | 2+1+2=5 |
| 14368 OPCoD | one-way distill可能损强域 → on-policy peer/correct自身rollout+认知gate/anchor → mutual Pareto需核两学生与反馈可得性 | 2+2+2=6 |
| 14375 EQRL | 固定query预算/chunk忽略状态难度 → 联合latent/NFE/chunk macro-RL与chunk discount → VLA计算分配须按真实控制时长约束 | 2+2+2=6 |
| 14388 low-rank interventions | 单行为编辑外溢 → principal-angle overlap与decision子空间的方向非对称 → 线性可分不保独立控制 | 3+1+3=7 |
| 14390 diffusion memorization | 全球平均memorization掩同模型局部共存 → KDE/local coverage高维界 → 数据覆盖几何需局部而非全量规模代理 | 3+1+3=7 |
| 14397 Gauntlet | 常用app任务饱和错估agent泛化 → temporal/3D/graph professionalapp与human对照 → 饱和benchmark不能外推复杂GUI | 2+1+2=5 |
| 14398 MoE routing theory | 连续mixture不解释离散语言任务专家化 → template/字典的一层构造 → specialization须绑定可表示性假设非训练必达 | 2+1+2=5 |
| 14470 GitOfThoughts | memory成功混近复制/迁移 → 预注册重试与五store/相似度对照的负结果 → auditability不等价新题方法迁移 | 3+2+2=7 |
| 14476 tool deference | agent+GNN误被当额外判断 → 能力/工具替代动作与heldout gate反侧 → selective invoke受信息上界而非规模自动出现 | 3+2+3=8 |
| 14507 coordinate lists | 高容量LoRA重复tail并非普遍输出坏化 → structure-axis/容量/家族/record stop对照 → adapter验收须绑定结构终止控制 | 2+2+2=6 |
| 14517 guardrail DoS | reasoning guard只评拒答率漏availability → transfer与E2E资源放大 → guard必须硬预算/隔离共享资源 | 3+2+3=8 |
| 14528 BayLing Duplex | VAD turn boundary限制重叠 → vocab少量状态token让单AR同时听说停 → duplex要协议状态而非外置话轮闸 | 2+2+2=6 |
| 14530 hidden correctness | pregen probe可能只是prompt长度 → residualize+50外split → hidden信号不等于个例正确性保证/可修复性 | 3+1+2=6 |
| 14535 SCDP | 单相机缺wrist细节 → 预测EE轨迹为diffusion内的feature采样anchor → visual控制焦点可依中间action而非固定crop | 2+1+2=5 |
| 14551 TRACE | current视觉非充分state且time索引不稳 → order-sensitive path signatures路由固定latent证据 → cue内容与trajectory key分离 | 2+2+2=6 |
| 14571 StreamMem | stored/recall不等未来帮助 → 同anchor initial/followup四分指标 → memory验收需实际反馈复用而非写入 | 2+2+2=6 |
| 14574 SIMMER | action执行不抛错仍latent不可逆失效 → symbolic世界hazard/postcondition检查+反事实foresight → 执行完成不等目标/安全完成 | 3+2+3=8 |
| 14589 fail-plausible | tests通过无法发现用户侧无actionable错误 → incident溯源发现LLM把错误包装成功叙事 → 观测必须从真实副作用到用户交付闭环 | 3+2+3=8 |
| 14591 AudioDER | 拼公开audio corpus重复声学信号 → acoustic去重+等/更少量对照 → 多模态数据规模需按源重叠而非样本数 | 2+1+2=5 |
| 14598 INT8 GEMM | INT8产物实际dequant-bf16不执行INT8 → fused int8accum/epilogue与Ampere反侧 → quantization标签不等compute/端到端收益 | 3+2+3=8 |
| 14647 LEAF-X | raw attention不保faithfulness/temporal grounding → entropyhead/rollout+因果ablation → attribution需干预核而非视觉稀疏 | 2+1+2=5 |
| 14657 HPSv3++ | 固定旧model reward不稳跨capability/RL迭代 → 梯度正交保旧+条件signal/无监督std引导 → reward要适应policy分布而不放任漂移 | 2+2+2=6 |
| 14667 Memento | nextshot合理不保证memory保identity → memory-only reconstruction+dualquery → longvideo记忆需受重建监督而非单步质量 | 2+2+2=6 |
| 14668 RRDA | knowledge edit只学写会伤无关query → relevant edit/irrelevant locality双adapter和router反侧 → suppress路径需独立训练/评估 | 2+2+2=6 |
| 14672 Parallel Synthesis | text concat重prefill丢并行cache结构 → KV mapper+adapter并支缓存消费 → cache接口需训练/位置语义对齐不免费拼接 | 2+2+2=6 |
| 14674 AgentSpec | 单模块分数不保组合 → typed替换受控实验发现nonuniform memory/reason/reflection/RL交互 → scaffold兼容性须在部署组合下验证 | 3+2+2=7 |
| 14691 CORA | answer reward不保trace语义一致 → consistency RM+HRAS双advantage → traces“忠实”仍须RM/因果边界而非同文 | 2+2+2=6 |
| 14694 AdaSR | 静态readthenreason延迟大/全序列单advantage粗 → streaming/deep两层HRPO与budget奖励 → partial observation与最终deliberation要分credit | 2+2+2=6 |
| 14700 RepFusion | MLLM只encode clean text视觉prior未用于denoise → noisy repr对齐+重复MLLM条件化预算对照 → 预训练prior能否抵新增denoiser成本须控制推理预算 | 2+2+2=6 |
| 14701 RATS | cls-token聚合丢part结构 → head隔离register compress/communicate/broadcast瓶颈 → 可解释parts是架构prior但非人工标签真值 | 2+1+2=5 |
| 14702 OmniVideo | 独立clip/audio-caption切断实体跨模态证据 → entity全局script+clue先行QA → 合成数据需跨片段referent/provenance一致 | 2+1+2=5 |

### 后续N与一小段核心待判

- 13940医学编码：具体ICD任务上的prompt/SFT/GRPO对比，PHI只被称诊断curriculum而未给新一般机制或超该任务边界；不是因医学标题自动排除。若小段PHI显示可复用GRPO改变，再定点重开；当前不宣告最终N。
- 14010 RT-VLA：multi-level监督蒸馏与离线解释/实时控制拆分，仅报告teacher/student场景local收益；是否增加可复用实时约束需一小段核心判，不先冻结P/N。
- 14093：一般shared-memory因果观测定理及NUMA计数器，无模型训练/推理/Agent的直接机制，只能类比，不按trace章节映射准入。
- 14119 FactoryLLM：本地RAG/现成RAGAS+judge接线、30工厂query指标；没有新可靠性机制，“本地”等同safe的宣称不能充增量。
- 14130/14693：一般非LLM多agent RL逻辑shield/多目标traffic，未建立foundation/LLM系统主线的直接增量；不以agent命名扩大一般博弈/控制研究。
- 14164 fuzz-oracle：LLM生成metamorphic关系后现成fuzz的应用效果；新增在软件fuzz目标而非模型/Agent机制；若核心证实oracle审定新可靠性路径可重开，暂需小段判。
- 14172 CoMAG：一般多模态attributed graph学习，无foundation/language model系统切片，不能因图有text/image自动归多模态主线。
- 14192 DRIVE：广告bidding offline RL，现有distribution/action retrieval/value选的任务组合，未见模型系统新边界。
- 14222 ORCA：time-series领域预测黑盒残差适配；摘要未支撑LLM/foundation训练系统通用增量，generic forecasting不是LG主线全收。
- 14233 obfuscation：off-the-shelf LLM在Android检测任务与prompt/threshold探索，无具体新机制或可修正系统判断的反证。
- 14261 security workflow：Planner/Analyzer/Fixer/Verifier+CodeQL既有步骤组合，25漏洞task指标不建新执行/验证机制。
- 14312 PLRTune：LLM hint+TD3数据库旋钮应用；不是面向模型训练/推理的资源调度机制。
- 14327 automotive assurance：已有安全标准映射与Talk2Drive个案，摘要未给新assurance论证机制/严格条件；只作已有风险解释不凭标准名准入。
- 14357 canonical code：30–500倍明示hypothesis，QLoRA试验只学canonical轨迹/禁词，不证明行为保持/成本；目前是研究计划非成立mechanism/反证贡献，前N不按巨大数字准入。
- 14445 tap：file保留+notify+worktree既有设计组合；自用review缺陷率的heterogeneous/homogeneous关联不隔离选择/任务，未出现新可靠性条件；前N。
- 14639 antispoof MoE：标准FFN→expert/gate转换在speech detector上EER局部收益，未见新MoE机制或可迁移边界；不把应用指标当MoE增量。
- 14697 ClinHallu：medical trace按vision/knowledge/integration拆分+stage replacement，可能是可迁移评价混杂控制，需一小段核心判其干预/标签可识别性；未因医学先排除。
- 14409 HyVLA：摘要只有全stack组件枚举，无具体贡献；须小段官方核心恢复，不能据名字/腾讯声望P或据短摘要N。

明确领域外标题（science/物理/化学/医学领域预测等）的其余命中仅作有界标题范围关闭；尚未把214全称full-AB筛选完成。待最终筛选记录列具体身份与理由；没有为了审阅耗时缩P池。

## 3. 有界官方标题补检差额（非全分类队列）

CL月页目标ID13682–14702在全月索引907–948，共42标题；LG在1476–1566，共91标题。初次大页原件下载超时，只取已越过目标段的导航线索，不冒称整页完整；CL合法窄页skip900/show100，LG原skip1400/show300为错误页、已改合法show250取完整250标题，不能沿用旧错误页停止证明。ID跨度是查漏定位并非公告批次完界，两侧日期/主题边界另核（见SOURCE_CHECK），其他月份/分类不扩队列。对标题语义相关/不明的39个增量身份定点DataCite恢复：TITLE_EXTRA8和LG_EXTRA31，均meta.total等于data数/无next，完整题摘已读。主组214+39=253唯一发现身份，不等于253个当窗候选；其中40个日期区间跨日，213个helper合法同Jun15。此机械摘要不替代原件/贡献核验。旧100候选与此发现集合交集0，不搬旧归属。

### 标题差额P提案（实验可信待exact-v1；作者唯一必要首备）

| family | 原约束 → 增量 → 改变的选择 | 拟分/日期 |
| --- | --- | --- |
| 13808 Culture Funnel | inference文化对齐假设已有知识 → 跨pretrain/SFT/RL/reasoning数据tag见文化信号流失 → multilingual不等文化覆盖，data lineage需跨阶段 | 2+2+2=6；同Jun15 |
| 14391 disfluency ASR | fluent训练省略hesitation/新tokens伤旧能力 → tokens启动再continual与跨attention机制反侧 → speech adaptation须同时测marker/旧域 | 2+2+2=6；同Jun15 |
| 14512 systematicity | meta-compositional任务分数被外推满足系统性 → 近OOD规则/部分ID仍失败的具体反证 → learnedcompositionality验收要对称依赖/规则覆盖 | 3+1+3=7；同Jun15 |
| 14626 cultural narratives | marker变化被当整体文化localization → 去区别词后的跨国家同模板对照 → evaluation需分surfacemarker与plot结构，不能把lexicaldiversity当语义覆盖 | 2+1+2=5；同Jun15 |
| 13753 grokking norm | norm阈值相关不证因果 → normclamp/LayerNorm开关发现exp delay非禁用generalization → scale/norm与LR作用要干预区分 | 潜P，日期跨Jun12–15，不先评分 |
| 13767 sparse adaptation | lowrank效果混参数预算 → fixed factor/structuredcolumn sparse限制+参数匹配/theory → PEFT限制空间可比budget仍竞争但不普适 | 潜P，日期跨Jun12–15，不先评分 |
| 13801 structured noise | ANN噪声多忽略相关结构 → covariance-conditionednoise对natural/adversarial迁移反侧 → “noise robustness”需绑定协方差/shift类型 | 2+1+2=5；同Jun15 |
| 13803 neural slack | violation-only梯度对未违约位置无信号 → jointlylearned validaux target回归 → soft约束验收不能把densegrid零违约当形式保证 | 2+1+2=5；同Jun15；与main具体直连仍需reader校准 |
| 13867 Muon^p | full谱flatten丢适配信息 → fractional谱powers/双变量matmul迭代及Schatten条件 → optimizer几何/预训和finetune不能共用一谱偏好 | 3+2+2=7；同Jun15 |
| 13894 Gefen | optimizer state两全buffer与手工block → 初始squaredgrad推断共享v块/DPcodebook量化m → memory节省需统计同质性而非架构硬码 | 3+2+3=8；同Jun15 |
| 14022 post-LN scale | LN前正scale被消 → 严格placement identity/同backbone控 → 结构magnitude信号与normalization先后是机制不是scale数值调参 | 2+1+2=5；同Jun15；需main直连校准 |
| 14040 dense scaffold SAE | sparse dictionary假设全residual稀疏 → parallel低秩dense瓶颈+causal remove反侧 → feature稀疏不等完整model computation被解释 | 3+2+3=8；同Jun15 |
| 14078 backdoor unlearning | shallow安全表征不等去后门 → sequential忘却必要条件/EMblindinversion → unlearning需恢复触发行为威胁面而非短期ASR | 3+2+3=8；同Jun15 |
| 14108 number embedding | learnedtoken embedding未保算术结构 → real+p-adic训练免费表示保运算 → 数值input表示与model算术generalization需分验 | 2+1+2=5；同Jun15 |
| 14187 Zeta | Muon NS rawmomentum条件不良 → coordinate再spectralwhitening次序+condition/error分析 → optimizer前处理顺序不能互换/不当单超参 | 3+2+3=8；同Jun15 |
| 14259 Adam-SGD gap | 单vocab/attention机制解释被普遍化 → controlled反例与batchcrossover → optimizer选择需数据/架构/batch共同协议 | 3+2+3=8；同Jun15 |
| 14334 metric matching | graph/kNN几何估计难扩 → carré-du-champ条件扰动回归amortizedoperator → 学习表示几何可不显式全图但需核估计假设 | 2+1+2=5；同Jun15；main直连待校准 |
| 14344 tactile LESS | global触觉state弱于组合泛化 → localgrid recurrent encoder重建多inclusion → 模态局部归纳偏置须按组合控制 | 2+1+2=5；同Jun15；main直连待校准 |
| 14346 SqueezeRelease | mask稀疏不缩dense部署 → 保函数结构minimize/CompensatedLN+release重用零位 → pruning与artifact重写及训练循环不同验收 | 3+2+2=7；同Jun15 |
| 14354 MUFFLe | update重复patterns被quant/sparse忽略 → generalizeddedup于FedAvg通信 → 本地压缩费/重复覆盖与E2E通信单位分账 | 2+1+2=5；同Jun15；不因WIP/MNIST排除 |
| 14463 EM-NeSy | symbolic端到端梯度需可微推理 → posterior E-step/神经M-step可容近似symbolic → 学习/符号推理边界及误差不能靠端到端名义消失 | 2+2+2=6；同Jun15；main直连待校准 |
| 14518 unlearning audit | dishonest owner与curious auditor双不信任 → behavioral audit准确度与retained membership泄漏几何下界 → 审计不是免费隐私保证 | 3+2+3=8；同Jun15 |
| 14533 PCA risk shadow | 保variance不保tail决策信息 → exactcounterexample/尾部加权covariance → representation压缩须rare-event条件验收 | 3+1+2=6；同Jun15；main直连待校准 |
| 14536 PS2RL | invariant set显式求解难扩/softconstraint无hard保证 → learnedbackup rollout隐式集合+projection → runtime安全要动力学/backup条件非reward自证 | 2+2+2=6；同Jun15；main直连待校准 |
| 14620 DiffusionGemma commits | parallel/block术语替实际commit测量 → ties/EOS/nonmonotonic/granularity/任务信号控制 → order结论需测量协议而非架构标签 | 3+2+2=7；同Jun15 |
| 14673 CC not superposition | toy100ReLU/50neuron优势被当compressed computation → 标签mixing移除/半非负矩阵baseline消优势 → 解释需排任务标签伪影 | 3+1+3=7；同Jun15 |
| 14688 verifier vs taste | formalvalidity不证数学价值 → nestedlanguagegeneration精确density/finite-vs-infinite trivia条件界 → 证书能移错不能替未知价值oracle | 3+1+3=7；同Jun15 |
| 14695 PersonaPruner | general pruning删persona traits → 单persona条件子网络选择/保留 → personalization压缩需persona与通用能力双验 | 2+1+2=5；同Jun15 |

### 差额N与窄核心待判

- 13977 Creative Integration：创造性压缩标准/四gate与跨领域corpus，未建立模型形成/训练/推理/Agent系统的具体机制或设计边界，只是一般创造性判定；不以formal或“decidable”自动收。
- 13818 thesis：DVIP/VaLLA/FMGP及PAC-Bayes等多项既有工作汇总，完整题摘没有区分本次新独立事件相对原论文的具体增量；不把学位提交当全部内容新公开。无具名新节前N，日期未另追。
- 14325 Text2Cypher：syntheticKG数据提升小模型这一题摘未披露新grounding/verification机制，仅新增task数据/指标；前N。
- 14600 LoSoNA：新群聊norm任务+四种prompt多模型比榜，明示效果不一但未指出新的可靠性条件或经控制的误判来源；前N不是“不值得研究”。
- 14386 explicitly scientific discovery/symbolic regression/金融factor discovery的研究路线，按ROADMAP AIforScience暂缓，不经Agent或evaluation泛节点重新引入。
- 14361 SemPiper：demo declarativesemanticops+LLM合成/evolution界面，题摘无新增执行验证约束或优化机制，前N。
- 13748 FedSPC只将已有control-variate限定sharedparameters，14416 FedCONST“globalstrength/convexconstraint”须小段core判是否超已知局部组合；14235 IVRS implicitproposal+discriminator rejection/IR-ELBO也需小段core判与当前模型主线直连，未凭一般Bayesian题名自动P。
- 14459 MoDiCoL模块化联合作用/continual curriculum是否揭示真实迁移/忘却反侧须小段core判，不因新dataset名P。

当前本日普通工作仍很多：上述P、窄core、必要/actualowner/写入与来源终核都未结束。真实已完只有A1一项I/唯一POST；不借此计日。

## 4. 精确事件跨Daily去重（覆盖前文拟P，不迁旧日期）

reader发现首9中的旧同v1后，作者立即对**本轮已独立发现253个ID**与2026已有Daily候选表做identity/exactversion窄匹配，没有从别日候选反推本窗发现。Jun16旧100交集0，Jun15当前43中有36个同exact-v1事件：

`13685 13686 13708 13733 13740 13769 13814 13817 13861 13873 13886 13949 13968 13994 14027 14106 14122 14150 14154 14179 14200 14210 14211 14219 14243 14470 14476 14517 14518 14571 14574 14589 14598 14620 14672 14674`（均2606前缀）。

这36项前文拟分/潜P由本段去重结论覆盖，不列Jun16新候选、不重复评分/Methods/Books。已读[Jun15](../../15/README.md)对应机制/受测条件/反证与具体owner采用结果，身份/v1/采用命题未变；当前官方abs实际轻核无撤回或纠错重开信号。后来版本号/改标题本身不重审v1。共享已完成层复用，不借旧日期字符串证明本窗新公开；其原日期/评分/小时窗保持。13708/13733/13740/13769等早提交旧事件也由同event去重，不再作为新增日期请求。13814在发现去重前作者已定点读v1标准核心，读到24config而非current32、per-round校准并非无训练/免数据、固定排名非queryrewrite、P95及Devstral反侧；这些不扩旧采用、不再继续其owner/Methods。

**撤回例外13856**不在当前36之中：current官方撤回使旧Jun15采用链失效，根协调/reader§10精确授权下已实际移Ch29唯一heading/两段/binding与Jun15该行/正面块，剩43行与§4扣撤回块前后hash严格一致。current有效43=12I31NC，其余旧完成层不重跑；原件保留，不把撤回当访问故障。唯一reader实际POST待回；14066已撤回但无既有采用链，无须另删Books。

目前实际新I已两项：13795 reader§6、13796 reader§9唯一POST生效。其他真正新潜P继续按前述校准/必要缺层，不为审阅时间改判；来源最终覆盖仍需本日十三源记录与外部边界收束。

## 5. 已请求短核心的决定（到事实即停，不把贡献排除与证据争议混用）

- **13905 ADORE→P，2+1+2=5。** exact-v1 §3.2/Eq2–5及6.1：feedback pool对原query给grade、只给未评topK新doc打分，各轮retrieval只消费当轮expansion（非累加旧词），终止按新doc连续不足/grade饱和/预算。这是可辨的feedback-state/更新人口/停止机制，而非只重命名Rocchio。进一步必要仍需对照与反馈judge/全迭代成本反侧，尚不称Evidence完。
- **14047 KGERMAR→N。** exact-v1 §2.3–2.4已足决定：标准R-GCN/LM拼接与三bank TopK、固定learned线性权重融合，银行分层沿既有ERMAR而来；未新增实体一致性维护/版本更新/选择可靠性条件。摘要的graph提升/省memory只是该组合local结果，不建立新长期机制或边界，不能凭“graph胜similarity”过门槛。Eq6单标量softmax/embedding形状疑问不作为缩池理由，也不采其性能；如有具体新维护机制原证才局部重开。
- **14172 CoMAG→P，2+2+2=6。** exact-v1 IV-C/IV-D/Alg1/V：modality-specific hop轨迹保early/late state，跨modality不必同步hop、加距离penalty，再分shared/private；propagation收缩仅线性core/row-normalized/正residual前提，不等真实非线性全网。改变跨模态证据的receptivefield对齐与保留，不因无LLM排。
- **14222 ORCA→P，2+1+2=5。** exact-v1 §3.2/3.4/3.5：外部API冻结，adapter条件为input+base prediction，EMA base/adapter误差路由同时给output-space历史prior正则权重；这是blackbox参数权限/反馈时钟/稳定-塑性接口。MSE conditional expectation是成熟工具，不计作新理论；EMAsoftgate不能确保每次不劣，真实标签延迟及Bayes surrogate资格待必要。此次改P源于具体新增机制，不因放宽非LLM门槛。
- **14639 anti-spoof MoE→P，2+1+2=5。** exact-v1 §5.2–5.4/6：固定WavLM实验中early/full插专家反退、late较好；more topK不总提升，E2/top1以较小权重仍接近E4/top1；三corpus routing JS不支持按synthesizer特化。可修正“鲁棒收益即来自来源专家化/更多专家算力更好”的实际判断，不采最佳EER为普适规律；不是只将标准MoE应用到speech。
- **13940 PHI→P，2+1+2=5。** exact-v1 §4.3/Eq3–4：hintfree训练集推理刷新per-example missed-label池、empty池跳过、rare/lowrecall加权随机hint子集、reward仍完整gold、test不带hint。新增是groundtruth提示下采样/课程人口与自由生成分验，不仅医学ICD分数；训练型hint对部署无hint是否有效仍待必要，不授临床能力。
- **14010 RT-VLA→P，2+1+2=5。** exact-v1 §3.3–3.4：student/teacher不同chat template按targetspan对齐KL，先训drive再冻结driving branch，以student greedy rollout由frozen teacher监督language分支。新边界是onpolicy explanation更新不改实时动作路径，不是蒸馏越小越好；posthoc文字非动作因果解释，后续必要核对消融和真实延迟条件。
- **14249 HarnessX→P，2+2+2=6。** exact-v1 §3.2/5.3：同hook eventtyped processor仅五结果并验read-only，真正新增拟采用是crossharness GRPO按task分组、各trajectory在其原harness prompt/tool/context下求current logprob，oldbehavior pertrace与固定reference分开。改变采样人口/组比较与replay身份，非只把typed组合叫algebra；mixedbuffer偏差/5.4待必要。
- **14269 ScoreGate→P，2+1+2=5。** exact-v1 §4.2–4.3/5.3：4区分embedding/crossencoder同意与两方向分歧，B2/B3用不对称阈值；存在reranker-only与singlefusion对照，非只固定K改阈值名字。显著性段b4/c0却报chi²6.02/p.014、同reranker表间率不一致，尚不背书该统计/零FP保证；后续读必要支持域后决定能否只保有限设计/中心争议，不能因可信度问题回改N。
- **14317 CausalMotion→P，2+1+2=5。** exact-v1 §3.2–3.4：对象state(v/contact)经稀关键帧推断与运动段插值，greedy时间单调IoU定位，再把时序对齐的邻keyframe/previous appearance anchor按local mask注入latent。区别是显式state→timeanchor→generator局部更新接口，不把VLM“物理”输出当真正守恒oracle；guidedlatent也不保原全局distribution，必要反侧待核。
- **14397 Gauntlet→N。** exact-v1 §3.4短核心仅列completion误判、grounding、protocol与invalid/loop四类既有故障；正文新贡献在换五专业app/更难135任务与低成功率，未出现能修正现有评价解释的新混杂控制/机制证据。按与其他新benchmark相同门槛关闭，不以低分/领域或数量排除。
- **14164 MetaFOE→P，2+1+2=5（reader具体反证使原N重开）。** 原先§4.1/6.2只看到成熟过滤pipeline，不足以关闭全文已有的评价反证。精确v1 §5.5/RQ5、T3/T4：相同五prompt比较下，COT的valid driver数量1389与valid比例56.2%最好，EXP最差；实际edge/crash fuzz效用却EXP最好、COT最差。这可修正“生成有效率越高即下游更有用”的评价选择，不只是新fuzz场景分数。COT的MR生成数量不受20条限制而其余四种受限，故不是等生成预算的prompt纯因果排序；采用最多是本协议下中间proxy与下游效用的排名反转。后续必要仅核T3/T4可比条件/已见过滤与3h campaign，不重全Methods。
- **14697 ClinHallu→P，2+1+2=5。** exact-v1 §4.3 Eq9–14：分别固定upstream reference后重新生成后级，按干预条件定义stage错率，不只自然trace错误打标签。这改变视觉/知识/整合stage的评价条件，可直接支撑模型评估；reference/LLMjudge/teacherforcing分布及“直接reflect固有倾向”过强因果需必要收窄，不引入医学诊疗结论。
- **14409 HyVLA→P，2+2+2=6。** exact-v1 §5.3 Eq12–17：async延迟chunk先丢staleprefix、在retained内部选可估futuretangent的连接点、用历史/未来方向Bezier接回，按embodiment调比例。确有stale action/runtime拼接边界而非“全stack”枚举；切向平行只支持几何平滑，不能直接继承真实时间速度C1或安全保证，必要仍待。

以上是窄core准入决定，不等所有P证据/Books完成。与旧事件匹配的13968不再重判。

### 标题差额与早提交短core（压缩恢复后只接已读决定点）

- **13683 portrait NRPA→N，日期未核实而停止。** exact-v1 §4.2使用既有NRPA nested online planning，以portrait-conditioned LLM模拟user作score；短core没有新增内层更新/可靠性或可复用适用边界。用户模拟任务组合本身不足准入，不为此继续复杂日期恢复。
- **13707 Orchestra→潜P。** exact-v1 §3.3把offline GRPO单位改为decision-state，不执行完整subagent rollout；rubrics以groundtruth/expert结合评decision/action/tool等，data rewrite另有anchor/modal bypass。具体训练人口/credit与成本接口值得核验，不只DA-GRPO命名。日期跨日仍缺，不评分/不先列当窗。
- **13803 neural slack→P，2+1+2=5。** exact-v1 §3将valid slack设为有限容量辅助网络的输出并与模型联合回归。若逐点精确投影便退回既有hinge；有限共享容量即使当前位置未违约也未必残差零，提供持续形状锚定梯度。它改变模型约束训练的信号，不仅finance任务换场景；容量过小欠拟合/过大不稳、离散网格非形式保证，仍待必要。
- **14022 post-LN scale→N。** exact-v1 §3.1/4.6–4.7决定事实仍是既有LN正标量不变性（epsilon除外）及placement应用于graph；GAT改善但PNA已有degree aggregators时成对近等，方差归零丢magnitude也属已知机制。局部graph控制没有建立超出该已知恒等式的新模型机制或适用边界；不因无LLM排、不因标题norm自动P。
- **14334 metric matching→P，2+1+2=5。** exact-v1 §3.1–3.4以Gaussian扰动的conditional CDC回归代替显式marginal operator，条件MSE与目标仅差theta无关项；低秩PSD表示用小r×r算子/投影差向量避免D×D构造。新增是学习表示几何的可训练/计算接口，不仅一般流形估计；rank条件及噪声近似仍限域。
- **14344 tactile LESS→P，2+1+2=5。** exact-v1 IV-A/V-B将局部触觉半径、grid center与共享GRU参数但独立cell state绑定，再拼局部image logits/force预测；单inclusion训练到多inclusion OOD反侧，ID不必最佳。可修正跨局部对象组合表示选择，而非医学imaging指标本身。
- **14354 MUFFLe→P，2+1+2=5。** exact-v1 III-B明确不是只接既有lossless GD：整数更新去恒定位后保g个最高非恒定位、相同截断base字典+ID、舍弃deviation，形成lossy update codec。独特base数随round变，成本nb*g+d*ceil(log2 nb)另有未计metadata；无error feedback。实际loss/字典重复率与通信折中可核，不因MNIST/WIP排。
- **14533 PCA risk shadow→P，3+1+2=6。** exact-v1 II-E/III给expectile-weighted reconstruction/IR covariance与联合P,h目标，不仅重复“方差不等任务信息”。但平方残差导数式17漏残差、stationary不强制leading eigenvectors、无界背景可支配rare feature，普遍严格支配未获上述推导支持。进入证据层以明确反证/收窄，不因证明不可信回改N，也不背书普遍支配。
- **14536 PS2RL→P，2+2+2=6。** exact-v1 §4.2/4.4以safe-arrival折扣value训练backup扩隐式invariant set，冻结backup后BCBF-QP约束投影policy动作，mesh约束数随horizon线性。直接改变物理policy执行安全接口；只对backup集合内初态、已知smooth dynamics/采样ZOH等条件，不是泛reward安全保证。
- **13748 FedSPC→N，维持原成熟组合理由。** exact-v1 §3.1仍是SCAFFOLD式control variate仅放共享参数块，私人块不校正/不传输，非参与client参考不变；短core未出现full-correction相对shared-only的受控失效条件或新估计状态责任。“权限/状态边界”是自己的系统复述而非新原证，不能支持N→P；不为它继续复杂日期恢复。若具名新对照事实到达，仅重开该事实。
- **14416 FedCONST→P，2+1+2=5。** exact-v1 §3.2–3.3以global magnitude作strength proxy，local梯度中心化并对冻结round-global weight正交投影；线性约束可在聚合后保留。具体全局参考/局部约束接口，不是仅convex一词；sum为零不等向量update为零/统计无偏，proxy资格与控制待必要。
- **14235 IVRS→P，2+2+2=6。** exact-v1 §3.3–3.4隐式q经density-ratio discriminator接受采样，IR-ELBO用Jensen处理logZ；理想比率下M增大改善posterior KL却压acceptance。直接是VAE/BNN训练proposal/下界与拒绝预算边界，非与主线只有类比；估计比率不自动真下界，待必要。
- **14459 MoDiCoL→P，2+1+2=5。** exact-v1 §2.2/3.1/4受控多因素/三顺序显示compound不必最难，mean WER与median/hallucination outlier可分离，replay比例/顺序改变稳定性，梯度近正交不保representation稳定。增量是混合shift及评价proxy/遗忘控制反证，不是只新ASR数据集；条件/repair与不等预算待必要。

这些是到事实即停的准入决定，尚不称必要/Books完成；reader只需校准新决定事实，不重复先前有效层。A3已由唯一reader§14标准必要/具体已有覆盖通过，无Book改动。

**14130 circular contracts局部重开→P，2+2+2=6。** reader指出原“非LLM多agent RL”排理由过宽；作者实际读exact-v1 §4/定义8–13/Th4.1、§5.1/5.3后确认新接口：对整个local-obligation tuple在精确有限safety abstraction上作greatest-fixedpoint认证，选全笛卡尔积后继均closed的rectangle再投影local masks，避免先独立factorization漏安全协同行为。执行无需中央逐步controller另需local mask identifiable信息资格；bandit仅在预认证library内且episode reset换tuple，不是训练中任意切换也不承诺bandit收敛/全球最优。这直接支撑模型驱动策略的执行安全组合，不因无LLM排。合法同Jun15日证：v1 Jun12 05:30:53Z→findable同DOI arxiv.content registered Jun15 01:48:10Z；current官方abs无撤回纠错。贡献层明确后原分未冻，新6分进入必要；不能由安全定理名称授真实环境/LLM安全。

## 6. 根授权具名旧链恢复：SMEPilot16332（非新增）

reader§27传达root明确授权：原canonical `candidate_cells`实际读取为date2026-06-15、3+3+3=9、retained/deep_complete/Integrate、INFER-TENSORRT-LLM；原review_cells有exact-v1 §3/4/5/7必要。只恢复本日被旧泛N误删的原一行与§4指向，不改旧N原件、不移原日期/小时窗，不作为本轮新池/新I。原旧100+恢复旧1=101。当前官方arXiv Jun16仅核验说明，按保护旧归属规则不迁移。

Jun17作者已在Ch49真实保存，root作为唯一非writer actualPOST通过，原件为[Jun17独核§9–10](../daily-20260617/SUP_REVIEW_20261026.md)；作者实际读这两节与本日canonical identity后，仅在本日报行政接纳原9分旧I，未第三Source/Methods/Book正文或写入，不代签其POST。本日唯一reader只核报告恢复与既成原件，不再第三Book审阅。其余有效层继续复用，普通新候选继续。

## 7. 同一错误范围理由的另一具名修复：14693 PCMA

此前与14130同句的“非LLM/traffic”理由不能单独否决通用policy优化。作者只定点完整AB与exact-v1 §4.1/§5.1–2（并核原定理的alignment假设），不是复扫所有MARL。实际新增为每agent的Dirichlet preferenceplanner，team+vector双critic提供actor组合advantage，planner按teamadvantage加pairwise preference diversity训练；区别于统一一组静态reward权重或只是traffic应用。**改P，2+2+2=6**，合法Jun15：v1 Jun12 17:55:28Z、same DOI findable arxiv.content registered Jun15 02:00:04Z，当前abs无撤回纠错。

准入不借普遍定理：firstorder diversity增益先假设centered preference已与team梯度贡献按正κ对齐，算法仅鼓励分散不保证这个alignment；证明忽略o(η)也不授任意步长严格下界。该可信度问题进入必要层收窄/争议，不回N缩池。旧14192 DRIVE仍具体N：已有distributional action+historical retrieval+value选择在bidding的组合，题摘未给新的泛化/计算/可靠性边界；不是无LLM标签排除。

## 8. 当前官方具名早文信号：只重开两项日期，不扩2025

14108/14673当前官方abs分别明确NeurIPS2025 MATH-AI/MechanisticInterpretability workshop，故本轮Jun15 arXiv公告联合区间不再支持全球首次正文。仅定点恢复这两个具体信号，不因其他文章没有早文标记而遍历历史。

14108：作者[lab页](https://aiml-k.github.io/publication/2025neurips-mathaiworkshop/)标October2025、同作者标题/完整AB，原件`SUP_RAW_EARLY14108_LAB_20261026.raw`；由该页直接打开[2025作者PDF](https://aiml-k.github.io/uploads/files/2025/NIPS2025-bae-lee.pdf)，实际读首页与§2，AOE构造及workshop2025脚注均同该事件。PDF已保存。故**窗外既有正文**，不列Jun15新候选/评分/Books；不追October具体日或改写任何2025报告，无具体重要修订信号则不作整篇versiondiff。

14673：FAR官方[具名研究页](https://www.far.ai/research/compressed-computation-is-probably-not-computation-in-superposition)标Dec5 2025，同四作者/完整AB，原件`SUP_RAW_EARLY14673_PAPER_20261026.raw`，FullPDF实际指OpenReview iVeOIeHDP1；其BibTeX误指另一paper，明确不使用。OR PDF/API1/API2实际challenge403（原件保留），未谎称取到历史PDF。定点进一步打开[四位作者原创正文](https://www.lesswrong.com/posts/ZxFchCFJFcgysYsT9/compressed-computation-is-probably-not-computation-in)，真实页面标Jun23 2025，同作者/标题，实际读正文Summary/Methods/Quantitativeanalysis/Mechanism段，其mixing term、去M反侧及SNMF已公开。已足判**窗外既有正文**，不需因OR拒绝无限追渠道；不将贡献改N、不在本窗评分或改2025档。公开时间只保原2025日期精度，不补时刻。

## 9. 17005 原旧链行政恢复

reader明确授原candidate Jun15/3+3+3=9/deep/Integrate恢复；作者实际读本日canonical唯一该记录和Jun17独核§11–12既成必要/PRE/实际POST，不第三Methods/Books。Jun17作者已SAVE/root唯一实际POST，故仅本日报行/§4与证据引用接纳，无新Book/注写入。旧100+16332+17005=102，不计新Jun15候选/I；16494仍等必要，不预签。

14673原件权限补注：`SUP_RAW_EARLY14673_AUTHORPOST_20261026.raw`是curl所得Vercel checkpoint，**不是有效全文**。上述作者正文实际依据为web直接打开同一公开URL的277行正文：标题/四作者/Jun23'25日期在页首，Methods/去M与移植/Mechanism的SNMF在正文中段均实际可读。reader可从同URL重开；若其访问仍受限，FAR官方Dec5'25具名研究页/同AB与workshop信号也已足隔离Jun15首次，不将失败raw冒作全文或无限追渠道。

## 10. 有限来源/筛选停止后的实际新候选分母

唯一reader§44有限Source停止/13具名跨日安全日期保留已过；本轮新候选冻结为**95家族**，不是253发现身份、214主题命中或134外侧日期身份的全文配额。其为已经逐项完整题摘准入校准及合法联合日证的98提案，扣当前具名早文恢复的14108/14673两个窗外正文及13904旧SANA链；具体贡献/原三维分沿前节与reader已过层，不为当前工作量重分。36个已独立发现的旧same-v1仍复用，旧16332/17005仅报告恢复、16494等既成旧链必要不算新候选；13跨日潜贡献不评分/不确定入窗。

精确当日新候选ID（均2606.v1）：

```text
13795 13796 13801 13803 13808 13815 13862 13867 13872 13877 13878 13883 13884 13894
13905 13931 13940 13944 13945 13964 13982 13989 13995 14010 14024 14037 14040
14048 14058 14061 14078 14084 14117 14125 14127 14142 14153 14155 14162 14164
14168 14172 14187 14199 14222 14235 14240 14259 14269 14278 14302 14314 14317
14334 14344 14346 14347 14354 14368 14375 14388 14390 14391 14398 14409 14416 14459
14463 14507 14512 14528 14530 14533 14535 14536 14551 14591 14626 14639 14647 14657
14667 14668 14688 14691 14693 14694 14695 14697 14700 14701 14702
```

至reader§55已闭24为I10/NC13/中心安全保留1，71仍ordinary（A26/27已唯一首备待reader）；报告六节已同步24新结果、95分母及13跨日具名隔离，V3/限定diffcheck通过。后续仅完成这些已明确贡献候选的必要命题/直接反侧与唯一owner，读到足以支持采用边界即停，不遍历无关Methods/附件、重复旧层或重新扩宽发现。后续发现真正身份/撤回/早稿信号只重开影响层，不以冻结阻止具体纠错；未授DAY。

## 11. 16494 / 15874既成旧链接纳

已实际读本日canonical两个具名item的candidate_cells：16494原dateJune15、15874原dateJune14，均3+3+3=9/deep_complete/Integrate，resolvedownerJun16。亦实际读Jun17review§32–34，Jun17作者唯一首备/实际SAVE，root唯一非writer必要/PRE及真实POST已成，不第三Source/Methods/Book。reader16§64直接窄授只恢复两报告行/证据引用；已真实SAVE，旧102→104，不计本轮95新池/I。15874原June14不在baseline、V3预计只1个日期兼容例外，保旧字段不伪造baseline或改checker；待reader报告接纳，非DAY。

## 12. 最后三旧链仅报告恢复

实际定点读canonical15099/15405/16364整item，原date分别June13/June13/June15、均3+3+3=9/deep_complete/Integrate，resolvedJun16；实际读Jun17review§36–37的必要/actualowner/PRE/唯一真实POST，不第三Source/Methods/Books。reader16§70直接窄授仅报告恢复三行与采用边界/既成链，已真实SAVE。旧104→107，95新池/I不增；当前V3三具名旧日期兼容例外在README§1/6如实保留，未改date/baseline/checker。16494/15874此前行政读回已由reader16§65通过，§11待reader文字仅历史时态；最后3待报告接纳，不预DAY。

## 14. 当前实存续跑点（以此节覆盖前述阶段快照）

至reader§183，实际新92逐项闭合＝57真实I/32具体NC/3中心安全H，普通研究/Books/单项POST待办0、窄位全释放；最后A95 NC§176/A96 I§180/A97–99 I§182已实际通过，A91/92 NC§171/172与A93/94 I§175有效。本日六节当前92+旧110=202唯一家族，自包含来源/分母/处置/限制/22N分层复核，14688正式title与MUFFLe原5深入措辞已行政修正。唯一整体DAY§183已实际通过，并直接窄授最终行政SAVE；作者据此将报告状态改完成，终存2026-10-26T19:49:07+08:00。原100行/完整旧§4/小时窗保护，518localrefs缺0/限定diffcheck通过，V3恰五原date兼容例外、不称全pass。202行中15870用精确v1 PDF链接而非HTML，202唯一identity无重复；先前HTML-only正则201不是缺项。只行政终存、未再改技术/候选/Books；同一reader最终保存态读回后通知root完成，不新Methods/全书审阅，不写State/索引，未stage/unstage/commit/push。

root/reader§89指定的三个旧误删链均闭合：A47 15345旧June13/9真I §96 POST；A48 16190旧June15/9深入当前具体NC §97（旧I缺body不能自签）；A49 15306旧June13/9真I §99 POST。报告旧107→110终存已§100实际接纳，368localrefs缺0，V3恰15099/15405/15306/15345原June13与15874原June14五授权兼容错误，不改date/baseline/checker、不称全pass，不计新92。15306/14199下载partial中必要完整章节已定点实际读足，不冒整稿下载成功或不必要尾部受阻。Jun15四恢复47=14I33NC/四date例外在§80/82闭合，root纯计数改14sources已SAVE，不重DAY/研究/Book。

旧过程曾记录的“14240必要继续/14235待POST”已由后续逐项必要及真实POST闭合，不是当前待办；前述阶段计数均以本节当前终存与reader§183为准。未写State/index、不stage/unstage/commit/push；新旧分账及当前真实报告为权威。

## 13. 三个具名旧owner去重修复

reader16定点join实际发现95身份与邻日canonical，14000/14130/14249有resolvedJun15 retained整行；root确认后§73直接窄授。本日新95扣3为92；§10代码块已按这92当前身份列出，§10前言95与进度24仅历史冻结快照，以本节和逐项后续为准。至§74当前扣已完成I14130/NC14000，新I17NC14H1=32，余60普通；14249未第二Methods，先复用旧same-v1有效层与actualowner。已从Jun16表/§4移14000/14130两块，Jun15保原June11/June12、9分恢复两行与必要采用；14130仅本人新增trueH2注改旧owner/原date9，body/旧trace未动。Jun15当前46=14I32NC、三日期兼容例外，原44行/§4与时窗保持，待reader终读；七Jun16旧链报告接纳§72已成，旧107，不新计95/92或I。未更State/index。

至§77新92已闭34=I19/NC14/H1是历史阶段。当前至§88新92已闭39=I23/NC15/H1，53普通；A39–43五行/对应§4已同步README，四新I均真实POST，A43具体NC无Book。A44 MUSE整体PRE§90已按精确gap真实SAVE待唯一POST，未预计。A38恢复的Jun15已由§80/82真实SAVE终读闭合47=14I33NC，四日期兼容例外；不重DAY。新增15306/15345/16190三具名旧误删链root授权/reader§89身份已核，先复用真实必要与actualowner，仅缺层再补，旧107尚未预增110，不计92新池；不扩旧池/不以完整旧标签代证据。
