# Mar02 补查首批准入校准

作者 supplement_20260302；目标补充窗口北京时间2026-03-01自然日。原0候选、原日期推导与完成标签只冻结复用。32个新精确v1完整题摘实际已读，均API首次Submitted不晚于本窗右端，但Submitted不授公开日；没有完整证据审阅或评分。原四个具名题摘与Qwen小尺寸有效审阅不重读。本表供root非作者校准，不是自行验收。

五个主题API提交邻域02/28–03/02：model104、system10、multimodal54、agent103、theory43；model/agent100尾页实际各4/3，其余一页读完。宽入口只浏览相关标题并剪枝；本窗右端后提交且无实际提前作者公告线索的身份关闭本次arXiv事件，不读题摘或立日期请求。医学应用/科学/传统领域应用的明确标题不组成逐项AB队列。只核下列32具体机制或含糊标题，未声称全量目录初筛或无遗漏。API原件和查询在SUP_FETCH_api/abstracts.json。

## 全部拟保留潜力（尚不是确定本窗候选）

| v1身份 | 原约束 → 完整题摘的实际增量 → 需重新考虑的选择 |
| --- | --- |
| [2603.00824v1 Gauge Theory of Superposition](https://arxiv.org/abs/2603.00824v1) | 全局单dictionary解释假设 → 局部语义chart及Fisher交互/transport障碍可计算 → 全局解释器跨context适用边界；只保留待核理论，非术语类比 |
| [2603.00829v1 Constitutional Black-Box Monitoring](https://arxiv.org/abs/2603.00829v1) | synthetic监控能否transfer → ControlArena外部轨迹中prompt sweep饱和/更强优化过拟合 → 监控优化预算与分布外有效性 |
| [2603.00888v1 Probabilistic Learning and Generation](https://arxiv.org/abs/2603.00888v1) | 大序列Bayes近似与prior难选 → attention/sparseGP近似与HiPPO inducing point → 架构归纳偏置能否替代通用近似；thesis不自动新贡献，日期及旧篇重复仍待核 |
| [2603.00907v1 KVSlimmer](https://arxiv.org/abs/2603.00907v1) | KV非对称经验+昂贵gradient Hessian → QK/V谱解释及forward变量闭式merge → merge计算预算及误差条件 |
| [2603.00910v1 Curvature-Weighted Capacity](https://arxiv.org/abs/2603.00910v1) | layer score无法直接满足硬件budget → inverse curvature gain及双convex allocation/pruning → global约束下层级capacity决策；当前API v3已收窄v1强支配/泛化措辞，不采用旧强结论 |
| [2603.00963v1 Logits Convexity](https://arxiv.org/abs/2603.00963v1) | PPO/SFT稳定差异 → logits方向性分析与LCO目标匹配 → 稳定性是否来自objective而非仅clip |
| [2603.00977v1 HiMAC](https://arxiv.org/abs/2603.00977v1) | flat planner/executor信用与非平稳 → bi-level相对advantage及交替co-evolution → 层级Agent RL训练分工 |
| [2603.01025v1 One-Token Verification](https://arxiv.org/abs/2603.01025v1) | verifier和multi-sample延迟 → learnable token+LoRA探测KV correctness → 可增量终止的正确率/成本边界 |
| [2603.01058v1 TriMoE](https://arxiv.org/abs/2603.01058v1) | non-hot不全memory-bound → hot/warm/cold映射GPU/AMX CPU/NDP与动态relayout → offload层级与scheduler |
| [2603.01068v1 LLaDA-o](https://arxiv.org/abs/2603.01068v1) | text/image不同diffusion及fixed-condition冗余 → MoD离散/连续分离共享attention与数据length adaptation → omni生成路径与cache取舍 |
| [2603.01089v1 CARD](https://arxiv.org/abs/2603.01089v1) | 静态通信图无法应变能力/资源 → conditional variational graph与environment信号 → 多Agent拓扑适配的设计，而非通用state词替换 |
| [2603.01096v1 V-SONAR/V-LCM](https://arxiv.org/abs/2603.01096v1) | 语言concept空间不直接表示vision → post-hoc vision alignment、English-only LCM跨视觉transfer与同latent-diffusion目标 → 跨模态统一潜空间能否复用语义能力 |
| [2603.01097v1 LoRA Knowledge Memory](https://arxiv.org/abs/2603.01097v1) | LoRA存储/组合操作边界不明 → 系统capacity/composability实证设计空间 → parametric memory与RAG/ICL取舍；非仅宣布LoRA可作memory |
| [2603.01106v1 DIVA-GRPO](https://arxiv.org/abs/2603.01106v1) | 全对/全错group advantage消失 → variant difficulty及跨local/global group归一 → 采样难度与梯度信号质量 |
| [2603.01162v1 GRPO U-Statistic](https://arxiv.org/abs/2603.01162v1) | group estimator方差与groupsize缺理论 → U-statistic MSE/oracle渐近与组大小law → group采样budget；未采用universal宣传 |
| [2603.08743v1 Zipage](https://arxiv.org/abs/2603.08743v1) | token eviction难与paging/prefix并用 → compressed PagedAttention调度、prefix和async compression → 并发与quality取舍；无数字采用 |
| [2603.00724v1 RLAR](https://arxiv.org/abs/2603.00724v1) | static reward OOD退化 → 动态reward tool检索与程序verifier合成 → reward选择在训练分布变化下的治理与有效性 |
| [2603.00729v1 Qwen3-Coder-Next report](https://arxiv.org/abs/2603.00729v1) | 小active参数Agent能力训练 → 可验证task/env规模合成mid-training与RL recipe → 训练信号而非单size数字；精确报告不直接等同Feb3模型release，尚未去重旧全文 |
| [2603.00812v1 Wave-Attractor-Tree](https://arxiv.org/abs/2603.00812v1) | attention序列成本 → 二叉GLU merge O(n)work/logdepth及结构依赖局部对照 → 归纳偏置适用边界，未外推通用LLM替代 |
| [2603.00822v1 ContextCov](https://arxiv.org/abs/2603.00822v1) | instruction文本无法enforce → AST/shell shim/architectural validator可执行检查合成 → 权限执行与文本遵循的边界；syntax validity不视正确性 |
| [2603.00823v1 Multi-Turn Unlearning](https://arxiv.org/abs/2603.00823v1) | single-turn看似遗忘 → self-correction/上下文恢复与更强遗忘的rigidity → 遗忘评估协议与knowledge erase claim |
| [2603.00825v1 COMBAT](https://arxiv.org/abs/2603.00825v1) | static世界不能反应另一Agent → 无opponent action标签的局部输入训练产生对手响应 → 部分观测下action-conditioned行为建模 |
| [2603.02271v1 VLA Edge Bottleneck](https://arxiv.org/abs/2603.02271v1) | 边缘VLA只看vision/params → MolmoAct action-generation实测memory瓶颈与模拟 → action延迟预算；100B属于projection未证实部署 |
| [2603.01012v1 FastCode](https://arxiv.org/abs/2603.01012v1) | full-text探索token开销 → lightweight结构scouting与cost-aware内容消费分离 → repository检索粒度与成本归因 |
| [2603.01045v1 Silo-Bench](https://arxiv.org/abs/2603.01045v1) | 多Agent交换信息不等于推理融合 → sufficiency后仍不能integration且规模抵消parallelism → 评价应拆通信与reasoning瓶颈 |
| [2603.01082v1 MCMR](https://arxiv.org/abs/2603.01082v1) | global/single-condition similarity评价 → 复合约束中模态早precision/长尾排序非对称 → 多模态retrieval评价混杂与rerank归因；不因商品领域排除 |
| [2603.01070v1 Faire](https://arxiv.org/abs/2603.01070v1) | plot-solution SFT表面模仿反降效 → 三种functional RL约束 → 多模态推理objective与干预有效性，不因几何题判范围外 |
| [2603.00983v1 EFS](https://arxiv.org/abs/2603.00983v1) | 平坦frame采样遗漏events → DINO event proxy/query-anchor/MMR协同 → video token coverage/relevance/diversity取舍 |
| [2603.00926v1 DAM-VLA](https://arxiv.org/abs/2603.00926v1) | 统一动作头难兼精细/粗运动 → action routing与arm/gripper双尺度weighting → 控制粒度与VLM/low-level衔接 |
| [2603.00732v1 UniHM](https://arxiv.org/abs/2603.00732v1) | morphology/task缺human数据transfer → shared dexterous codebook与physics dynamic refinement → action表示跨手形和可行性 |

以上30项潜力清楚，访问实际v1 abs只给Submitted/history，不给可用于本窗的首公开日；一次官方月list恢复仍待实际结果。未因缺公开日读全文，也不按ID月份/Registered推日。外部隔离先不采用、不评分、不进Books。

## 代表性负侧与含糊项

- 2603.01152v1 DeepResearch-9K：完整题摘提供9K旧multi-hop重合成、Tongyi trajectory与支持多种既有RL/reward的框架，再报SOTA；未指明新机制或修正数据/训练适用条件。拟贡献前EX，不以benchmark名称/低分关闭。
- 2603.01145v1 AutoSkill：完整题摘仍以抽取/维护/注入skill能力陈述为主，决定准入事实含糊；只一次必要v1 core查技能冲突/更新/反馈治理的实际新机制，不为证明实验或日期读全文。
- 标题范围负侧：2603.00746 SpectroFusion-ViT(speech emotion既有encoder应用)、2603.00854 GeMi(scroll paintings recommendation)、2603.00757临床trial响应、2603.02273阿尔茨海默gene graph、2603.01137 heat demand、2603.00857 MultiPUFFIN分子属性（AI for Science暂缓）；日期未核且无可见撤回纠错信号，不为范围明确负侧追日期。

当前精确v1页面均未见withdraw/deleted/erratum公告；这是轻量当前页检查，不证明完整版本史或安全。2603.00910的v3 abstract确实收窄v1强claims，记录为必要反证信号并仍隔离，无Books采用。

## 必要消歧与相关标题补漏追加

AutoSkill仅一次v1 core §3.4已实读，不读实验：query-only extraction（assistant非提取evidence）、nearest-neighbor比较后add/merge/discard、sameidentity versioned semantic union并限定非冲突新增。拟保留有限潜力为用户证据污染边界和局部更新治理，而非“versioned state有价值”；没有采实验或生产保证。至此原32中31潜力、1具体EX，待root校准。

官方月页CL/DC仅各首100项标题，无day announcement字段；不继续其他month页、不将200项转AB。6条相关新标题定点API身份核验，再完整读精确v1题摘：

| v1身份 | 有限贡献链 |
| --- | --- |
| [2603.00356v1 Token Management](https://arxiv.org/abs/2603.00356v1) | 请求rate忽略成本 → token/KV/concurrency entitlement共用admission/autoscaling模型、debt公平 → promises与provisioning一致性 |
| [2603.00357v1 SPARe](https://arxiv.org/abs/2603.00357v1) | restart-dominant失败成本 → redundant shard stacking/执行reordering与checkpoint joint optimization → replication资源和恢复时间的取舍；SimGrid不视60万GPU真实运行 |
| [2603.00025v1 TAB-PO](https://arxiv.org/abs/2603.00025v1) | DPO近似pair/semantic token-skew → token-weighted reference advantage+conditional barrier → preference margin、likelihood squeezing、gradient dilution；medical实例不掩盖通用训练mechanism |
| [2603.00026v1 ActMem](https://arxiv.org/abs/2603.00026v1) | 事实retrieval不能处理冲突 → causal/semantic graph+counterfactual/commonsense completion → 历史与当前意图推理边界；未将推断当事实 |
| [2603.00029v1 Anisotropy](https://arxiv.org/abs/2603.00029v1) | massiveactivation只当artifact → magnitude识别domaincritical dimension并定向steering → 解释/干预单位与域边界 |
| [2603.00030v1 SimpleTool](https://arxiv.org/abs/2603.00030v1) | structuredfunction AR延迟 → specialtoken兼结构压缩/mode selector与name/args并行 → 弱参数依赖成立时实时性取舍 |

这些是月页相关标题定点查漏，不假造window内事件。API原始Submitted分别Feb27(前2)/Feb3或Feb4(后4)，与ID年月不一致正说明不能用ID或提交授首公开；尚无本窗首公开证据。一次精确官方abs/月页恢复不给首公告日，全部隔离为精确日期/同事件重复需核的潜力，先不全文、不评分、不Books。若真实首公开落窗后，仅恢复该身份；若原已有效审阅为同事件则复用去重。

实际总数：38个新精确v1完整题摘、一次AutoSkill必要准入core；37潜力日期隔离、DeepResearch-9K 1具体EX。当前没有确定新增候选。首批30、AutoSkill core和新增6均送root独核，作者未自行授准入/Source/DAY Gate。

## root 首批校准修正与 LoRA 一次必要结果消歧

上述初判保留为过程，不作为最终候选数：root实际核32个v1全AB及AutoSkill§3.4，DeepResearch9K具体EX通过；AutoSkill改为具体EX，理由不是date/实验量：query-only/neighbor add-merge-discard/保持identity版本是prompt内成熟来源与去重纪律，缺新的冲突/反馈有效性条件、执行约束或效用反证，具体流程存在本身不授长期增量。core和旧判断保留可复查。

LoRA memory2603.01097v1仅一次必要core§6/Q8–Q11与AppendixO/P相关结果读：在固定总可训练参数预算下，oracle routing多模块分片胜single；实际embedding routing明显退化可低于single；top3 TIES略胜naive linear与top1，DARE随机drop在密集factmemory劣化，CAT无alignment合并最弱；关键反证Q11即使保证正确相关模块在集合内，merge N=1→5仍逐步退化，区分routing漏召回与composition干扰。该明确的新受限证据改变“召回更多adapter即可提升memory”的选择，因此仍保有限潜力；不采用其具体accuracy/latency，不把本次准入消歧当Evidence审阅。日期原入口恢复仍未证，本窗不评分不Books。

最终待root差额准入验收：38新完整v1 AB、2次必要准入core；36明确潜力日期隔离（原29＋LoRA具体条件1＋月页6）、DeepResearch9K/AutoSkill2具体EX、0确定新增/0Books。

ActMem2603.00026v1再由root指出准入决定仍含糊，仅一次必要§3 core（SUP_CORE_ACTMEM.txt168–238）读：centroid单pass cluster内先LLM生成candidatecausaledge，再以GPT2Large计算‘fi.As a result,fj’条件 vs neutralprefix的目标fj NLL差，按阈值保留边；initialvectorretrieval后以query负后果counterfactual作为二次召回查询，最终union facts和推断context。有限潜力来自“candidateedge生成之外有显式model-scoregate”及隐含约束二次检索；不把该score的关联性视因果证明，不声称有真实因果保证、更新一致性或部署效用。准入消歧到此停止，不读实验。故最新实际为38新完整AB、3次必要局部准入core；候选0，36日期潜力/2EX暂待ActMem差额及DAY独核。

最终root非作者实际复核全部38新v1完整题摘、三次必要core，ActMem有限gate接口准入通过且NLL非因果验证反侧保留；全部36日期潜力与DeepResearch9K/AutoSkill两具体EX校准通过。Source全部14有限stop及六部分DAY随后实际验收通过，已同步日报完成态；普通待办0，不把题摘/准入core算Evidence完成，不授全Coverage或无遗漏。前述过程初判/待验标签留为改判轨迹，不是当前最终候选统计。
