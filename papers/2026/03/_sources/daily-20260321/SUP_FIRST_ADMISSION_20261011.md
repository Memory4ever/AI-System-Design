# 03-21补03-20：首批准入校准请求

仅本日；作者 resume_mar18，非准备者/root校准待授。2026-10-11实际fresh合同/原报告/本日STOP。原0候选/原09→09窗口与连续§4冻结，新批次不是继承旧19/20队列。必要Source/评分/actual Books比较尚未执行，以下潜在增量只支持准入，不采摘要数字或保证；未冻结最终家族分母。

## 有限入口和实际停止

原四个API主题query（systems、learning、multimodal、agent）均submittedDate:[202603181800 TO 202603191800]，start0/max80/submittedDate升序。systems15/15、learning39/39、multimodal27/27实际XML完整；agent广义evaluation/memory入口108/request80但本地工具输出中间截断，只解析67（不可声称80完整或108全审），保留SUP_API_AGENT原截断raw，仅线索、不变必审队列。发现agent入口过宽后收窄成agent serving/agent memory/agentic reinforcement/rollout/tool execution/retrieval augmented/alignment evaluation/reasoning evaluation与LM语义并集，samewindow/start0/max50，实际18/18，原JSON为SUP_API_AGENT_NARROW。模型/训练/推理与多模态发现元数据重合不相加；目前只以下具名12完整题摘，不声称其余AB或Source已读。

精确v1 ID API一次请求12，只返回10；DBB18444与Beam18855分别通过官方abs/v1（Beam current也是v1）补原AB，不猜API遗漏原因。SUP_FIRST_EXACT_AB原JSON10条（其中cuGenOpt代表EX），SUP_FIRST_ARXIV_DATE_FIELDS实际DataCite10潜在项，current官方abs/history/comment已轻量打开；没有看到withdraw/correction/safety等具体说明，不为版本号遍历修订。PASTE首版标题与摘要48.5%不同current v3 43.5%，SVOO首版标题亦不同current v2；只采用以下v1身份，后续结果不用来证明本日firstpub。

## 日期夹证（推断而非精确公告时间）

官方[availability](https://info.arxiv.org/help/availability.html)“Final identifier assigned as part of announcement process”、Wed14ET后至Thu14ET批次Thu20ET公告；本批18UTC cutoff范围常规公告BJT03/20 08，不能继承旧09左界排除。十项official v1 header的Submitted为03/18 20:26Z～03/19 17:51Z，DataCite arxiv-issued DOI创建/registered为03/20 02:08Z～02:30Z、当前state=findable，v1 Updated均03/20 00:14Z～01:19Z。原字段不改写为published时刻；schedule/ID过程+同日已注册可检索夹证支持受限03/20 arXiv日级归属，未证明作者其他地方从未先发。只核具名必要首公开信号，不追作者全历史。代表EX日期不影响贡献关闭，不为EX补完整日期史。

## 首批拟入选：完整v1题摘后具体增量

| 材料（exact-v1） | 原约束 → 实际潜在增量 → 改变选择 | 必要审阅点/owner仅路由 |
| --- | --- | --- |
| [18383 From Servers to Sites](https://arxiv.org/abs/2603.18383v1) | 固定nameplate/static replay不能表示prefill/decode/idle切换与多机同步 → workload-driven状态转移＋configuration-specific状态功率分布，组合到server/rack/site → 是否可以跨traffic/config合成而保留相关性，区别实测能量与设施假设 | 拟核组合/相关性和真实配置反侧；PLATFORM-COST |
| [18489 EntropyCache](https://arxiv.org/abs/2603.18489v1) | 双向去噪cache会变陈旧，既有决策遍历context/depth → 新解码token分布最大entropy作重算信号＋最近k token持续波动 → 可把决策代价与长度解耦，但proxy和recompute质量成本必须验证 | entropy-drift相关/反例、最近k与基线完整费；MULTIMODAL-GENERATIVE-PARADIGMS（diffusion语义，不先写Ch45） |
| [18567 SpecForge](https://arxiv.org/abs/2603.18567v1) | 草稿训练与target前向耦合妨碍规模化 → target-draft decoupling、hybrid parallelism、training kernels及recipe对照 → 草稿能力生产和target特征服务可否拆开、通信/预计算如何摊销 | 不因框架名称或发布分数准入，核解耦具体状态/成本；TRAIN-DISTRIBUTED-TRAINING或INFER-SPECULATIVE-DECODING待actual sole比较 |
| [18897 Act While Thinking / PASTE](https://arxiv.org/abs/2603.18897v1) | 串行LLM-tool暴露工具latency → recurring control-flow和parameter依赖预测futuretool，重叠执行 → 延迟改善何时依赖预测/可投机副作用隔离，而非单个吞吐数字 | v1不是current v3；核dependency/confirm/取消与开销；AGENT-TOOL-CALLING或INFER-SCHEDULING待sole比较 |
| [18258 Logits-SAM DPO](https://arxiv.org/abs/2603.18258v1) | preferred概率下降不能由preference margin单独解释 → logit coordinate残差/curvature dynamics＋只outputlayer扰动的SAM → 是否能受限抑制squeezing且与参数SAM不同 | 核理论假设/梯度空间桥及对照成本；TRAIN-DPO |
| [18444 Discounted Beta--Bernoulli](https://arxiv.org/abs/2603.18444v1) | 小rollout点估计高方差/组方差collapse → 带折扣历史Bernoulli reward统计/有偏估计 → 非平稳policy如何使advantage尺度更稳定，偏差代价不能被历史平均遮盖 | 核posterior variance vs真实变化/zero组/预算；TRAIN-GRPO |
| [18636 SVOO](https://arxiv.org/abs/2603.18636v1) | 视频sparseattention同层统一prune或单侧QK分块 → 离线层敏感性定prune＋online双向QK co-clustering → 将profile可迁移性与runtime block形成分开核 | exact v1原题为Training-Free Sparse Attention…，current v2标题变；跨input稳定性/cluster费与质量反侧；INFER-TENSORRT-LLM或MULTIMODAL-GENERATIVE-PARADIGMS待sole |
| [19199 FASTER](https://arxiv.org/abs/2603.19199v1) | 平滑异步chunk不等于环境反应快，等待全部flowsteps才动作 → TTFA×horizon反应分析＋horizon-aware近端先收敛/stream → 近端commit与远端继续去噪的接口/质量取舍 | 均匀reaction假设、单步近端反退/实机clock而非宣传；MULTIMODAL-EMBODIED-VLA |
| [18280 Detection Is Cheap, Routing Is Learned](https://arxiv.org/abs/2603.18280v1) | highprobeaccuracy/refusalrate不足说明行为机制 → null/permutation/heldout category、direction ablation及refusal→narrative steering → evaluation必须分detect/route/generate，不能只测拒绝 | 政治主题只是受测population，非因此EX；不能外推所有对齐/因果，核方向干预和模型反例；PLATFORM-EVALUATION-SYSTEM |
| [18743 Memento-Skills](https://arxiv.org/abs/2603.18743v1) | 静态手工Agent/技能检索难跨任务积累 → stateful prompt＋behavior-trainable router与外部read/write skills演化，AB显式复用Memento2 → 新skill生成/路由能力是否独立增量、是否混杂库增长与evaluation练习 | 不把成熟reflective-loop自己计新；准入是具体router/外部能力学习验证，不授end-to-end自主可靠；AGENT-MEMORY |

## 代表排除（不是缺实验/规模小或负面即EX）

- [BeamAgent2603.18855v1](https://arxiv.org/abs/2603.18855v1)：完整AB已实际读。LLM只semantic translator，数值方法是MIMO discrete site＋continuous precoding alternating optimizer，局部raytracing明暗功率目标；将成熟“language intent→structured constraints→numerical solver”接口用到RF，不披露可复用的模型/Agent执行机制或控制反证。不是因“wireless”关键词自动排除；其具体算法新增属于该领域优化，而主线无法仅以类比准入。不评分/不Books；若独校认为dual-layer intent verification本身可改变通用Agent协议，定点该段再裁，不追全附件。
- [cuGenOpt2603.19163v1](https://arxiv.org/abs/2603.19163v1)：完整AB已实际读。CUDA block evolves one solution、searchoperator调度与JIT是一般组合优化引擎；LLM仅problem→solvercode的建模助手。TSP/VRPTW等优化不直接服务模型compute/kernel或模型runtime；不能因GPU/CUDA或有assistant映射Ch49/79而自动准入。不是实验不足/速度太高等理由，不评分/不Books。

## root非准备者首批准入校准（2026-10-11实际范围）

root已独立实际打开上述12份exact-v1 officialabs完整AB/currentheader/history；十潜力准入＋Beam/cuGenOpt代表EX正式PASS。不授摘要效果数字、Source/Evidence/Books/DAY，不冻最终分母。LogitsSAM18258原页Accepted ICLR2026是具体更早公开信号，作者必须定点同稿OpenReview first-public门，不据arxiv夹证宣家族从未先公开；SpecForge仅target-draft解耦/训练验证接口，production字样不授生产；Memento显式借Memento2 read/write旧原则，新分只对应实际新router/skill evolution及held-outpopulation/库增长混杂。Beam dual-layer intent classification是beamforming约束接口应用，未见新增通用Agent执行条件；cuGenOpt一般组合GPUengine不服务模型kernel，仅LLM助手，两个EX可停止不全文。

## 后批既有有限主题线索：题摘准入请求（尚未校准/不自动入选）

恢复只本21。此12是上述有界query已有相关线索，不是新全分类或全机构发现，不因已下载/能映射owner全部变队列。作者实际重新打开十二份官方exact-v1完整AB/header/history与具名arxiv-issued DOI原created/registered/state，未把current后版AB或提交日冒本日公开。四主题宽库不全逐项关闭；以下新增potential只求独立语义准入校准，尚无Source/评分/Books或最终分母。

| exact-v1 | 旧约束→具体增量→拟改变选择（只准入） | 初筛判断/后续必要门 |
| --- | --- | --- |
| [Semantic Router DSL18174](https://arxiv.org/abs/2603.18174v1) | crisp条件冲突检查不涵盖连续ML谓词→embedding球帽交叠检测与softmax空间分割替代独立threshold→确定何种“不co-fire”性质能由compiler保证、哪些classifier冲突仍依赖分布 | 潜在准入；需核softmax并不单独保证多个threshold cofire为零/ties/拒绝区/授权边界，production字样不授实现。 |
| [TARo18411](https://arxiv.org/abs/2603.18411v1) | 固定guidance不能适配各生成位置→stepmath训练reward与learned tokenrouter分责→冻结backbone仍付router/RM训练及token成本，核small→large迁移条件 | 潜在准入；clinical仅泛化评价不开展医学应用/知识，核机制而非AB最高数字。 |
| [UT-ACA18446](https://arxiv.org/abs/2603.18446v1) | 固定context预算忽视逐token证据需求→semantic/logit uncertainty detector累计不确定性后选择性rollback扩窗重生成→省context何时增加状态回退/采样成本 | 潜在准入；只v1，不因v3标题/后版存在遍比较。 |
| [PicoSpec19133](https://arxiv.org/abs/2603.19133v1) | edge/cloud mutual wait和vocab传输占延迟→异步SD pipeline与split rejection/sparsecompression→采样等价与网络费用能否同时满足 | 潜在准入；exact-v1后续v2非本日firstpub，核实际q/acceptance/residual consumer与配置，不授AB2.9普遍。 |
| [AFBS-BO18417](https://arxiv.org/abs/2603.18417v1) | sparse layer/head手调成本→BO全局探索＋binary局部细化并以不同长度多fidelity筛选→proxy迁移与最终quality/实费验收怎样分工 | 潜在准入；Accepted MiTA2026是必要先公开核线索，不凭会议名假定已重复。 |
| [PolicySampler18428](https://arxiv.org/abs/2603.18428v1) | 固定temperature/top-p不适配序列状态→test-time轻policy按sequential决策更新samplingparams与composite rewards→区别解码controller训练/评价泄漏和不改LLM权重 | 潜在准入；BookSum/arXiv/WikiHow只是通用摘要workload，不采最高相对数字。 |
| [AIMER18492](https://arxiv.org/abs/2603.18492v1) | expert重要性依赖校准router/activations→mean/RMS weight proxy不采样输入即可withinlayer排名→数据费移成静态proxy偏差/剪枝误差，需实际限定validity | 潜在准入；新具体statistic而非“免校准”宣传，本v1与后v3不混。 |
| [PowerFlow18363](https://arxiv.org/abs/2603.18363v1) | intrinsic reward缺显式优化分布/长度偏置→length-aware trajectory-balance对α-power目标作amortized采样→sharpen/flatten是否只变likelihood偏好而非真实正确性/创意保证 | 潜在准入；必要归一化/目标/长度桥及budget对照，不因RL术语入选。 |
| [CausalRM18736](https://arxiv.org/abs/2603.18736v1) | observational noisy且selectionbiased反馈不可直当preference→noiseaware surrogate与propensity reweight分责→何种可识别/positivity条件才可从用户行为学RM | 潜在准入；“unbiased”是待核中心条件，不先授因果/真实用户收益。 |
| [HISR18683](https://arxiv.org/abs/2603.18683v1) | outcome传播慢/turn奖励过碎→subgoal segment RM与知道终局的hindsight/actionlikelihood比聚合分责→训练奖励信息权限/credit偏差如何限定 | 潜在准入；comment Submitted ACL2026 Jan5只是投稿非已公开证明，不据此隔离或追全venue史。 |
| [ProRL Agent18815](https://arxiv.org/abs/2603.18815v1) | rollout编排和trainloop绑定阻碍迁移→fulltrajectory lifecycle API＋rootlessHPC sandbox分责→可迁移边界的真实state/identity/failure条件 | 潜在准入；原称NeMoGym open-source只是具体artifact线索，必要旧公开/接口增量核，不给成熟service拆分新分。 |
| [Box Maze19182](https://arxiv.org/abs/2603.19182v1) | AB概念memory/inference/boundary分层，新增是否超成熟proposal/constraint分责含糊→定点§1.3/3.1–3.3/4开篇后是timestamp ledger、logic-check、mutex stop与confidence事实/推断标签的既有原则组合，以LLM roleplay这些指令 | 拟代表EX待root：没有新的可复用执行/验证算法、已识别失效条件或可区分原则的设计反证。不是因n50、无实现/独立作者或负面关闭；未扩大后续全部实验审阅，若root认定stress协议具体增量则定点重开而非先锁EX。 |

十二官方v1 Submitted分别为18174 03/18 18:14:34Z；18411 03/19 02:18:40Z；18446 03:17:50Z；19133 16:51:32Z；19182 17:41:18Z；18417 02:24:38Z；18428 02:44:42Z；18492 04:54:37Z；18363 00:00:36Z；18736 10:37:34Z；18683 09:42:05Z；18815 12:08:51Z。所有同arxiv-issued DOI原created/registered均03/20Z、state=findable，published只有2026（不是日字段）：18174 02:06:29/30；18411 02:11:59/59；18446 02:12:49/50；19133 02:29:24/25；19182 02:30:33/34；18417 02:12:08/09；18428 02:12:24/24；18492 02:13:54/55；18363 02:10:52/53；18736 02:19:47/48；18683 02:18:29/30；18815 02:21:37/38。与首批相同官方availability/批次ID过程仅支持受限BJT03/20 arXiv日级推断；潜在先公开具体信号另核，不冒作者从未先发/精确公告时间。

## root 后批独立准入校准

root 实际读完上述十二 exact-v1 官方完整题摘、header/history，复用本轮不变的读取结果；BoxMaze 另一次定点读 §1.3/§3.1–3.3/§4.1 开篇决定准入含糊点。十一潜力增量准入校准通过，仍须必要日期与对应证据审阅，不由摘要授收益或 Books。SemanticRouter 的概率谓词冲突、TARo 的冻结骨干/训练 router、UT-ACA 的累积不确定性回退、PicoSpec 的异步传输与采样、AFBS 的多 fidelity 配置代理、PolicySampler 的解码 controller、AIMER 的无输入静态 proxy、PowerFlow 的分布目标、CausalRM 的噪声/选择偏差、HISR 的终局信息信用分配、ProRL 的 trajectory lifecycle 都提出可核验的具体选择，非仅能映射 ROADMAP。

BoxMaze 代表排除通过：所读协议把 timestamp ledger、逻辑检查、mutex 停止和置信事实/推断标签作为 roleplay 指令组合，未见新增可复用执行/验证机制或可区分旧原则的设计反证。不是因样本小、未实现、负面结果或作者身份排除；若后来出现具体新机制证据，仅重开其准入，不预先全读实验。其他十一项的因果、概率、迁移和性能均待必要审阅，不授成熟框架、strict guarantee 或实现已核。

日期仅复用 arXiv 公开批次/availability 与作者保存的具名 DOI 夹证的日级范围；AFBS 的会议及 ProRL 的旧 artifact 是必要先公开信号，定点核实，不追无关投稿史。HISR 投稿日期不等于公开。未冻结最终分母或通过 DAY。

### 两项具体先公开信号的定点核验

AFBS18417：官方abs/v1明确Accepted MiTA2026。exact-title搜索只恢复同稿IEEE DOI [10.1109/MiTA69365.2026.11582181](https://doi.org/10.1109/MiTA69365.2026.11582181)，不把搜索页当日期证据。实际[Crossref原API](https://api.crossref.org/works/10.1109/MiTA69365.2026.11582181) title相同、authors Arundhathi Dev/Justin Zhan、pages641–650、publisher IEEE；`published-print.date-parts=[[2026,2,24]]`、`issued`和`published`同日，event start02/24/end02/28。`created.date-time=2026-07-06T19:42:39Z`、`deposited=2026-07-07T05:07:32Z`仅后续处理；license start02/24不是公开正文证书。IEEE原document11582181 web失败、直GET未恢复正文/dateOfPublication/版本差额。会议官网本届02/24–28不等本稿公开证据，不据accepted或created单字段自动去重；必要同稿公开记录/正文版本差额待root独裁，未启动方法全文/评分/Books或把它归2025。

ProRL18815：实际[官方作者discussion#15](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/discussions/15) heading与原date字段 `Dec 17, 2025`；正文具名相同核心authors Hao Zhang/Mingjie Liu/Shaokun Zhang/Jian Hu/Yi Dong，已公开CPU agent/GPU inference/HTTP解耦、task/serveravailability/result三queue、DAPO补充/取消/重用和4B SWE/Math/Code局部实验。该Blog不是本v1同标题论文，旧artifact日期不证明本论文早发；本日[exact-v1](https://arxiv.org/html/2603.18815v1) §3.2–3.4新增/细化AgentHandler INIT/RUN/EVAL独立pool与异常结果、rootless runtime、原tokenID/logprob交付、phase-only timeout和backend/task生命周期接口，需按这些具体差额评分/审阅，不给旧服务拆分/三queue/DAPO成熟机制新分，不从本日arXiv变相重收旧2025事件。不追全部repo历史或后来Polar论文；限定原Blog与v1必要差额可复用。

root独立日期核验：实际重新取得上述Crossref JSON，核title/Dev与Zhan身份、published-print/issued/published 02/24、created07/06、deposited07/07、event02/24–28、无published-online及license02/24。这些字段不能闭合精确正文首次公开与版本关系；AFBS以必要同稿公开/版本缺口终态隔离，未评分、未作为确定新增或Books证据。接受IEEE正文首次公开日期字段、当期全文/公告或可明确版本差额的原件后，仅重开本项；不再读方法来绕过日期门，也不把会议日期直接改成论文归属。ProRL具体差额另经root必要Source/owner/PRE有限PASS，不受本项缺口阻塞。


## 四个既有限主题 raw 的漏筛纠正：仅准入收尾，不扩 query

root最终DAY定点发现窄Agent18中的具名条目没有有效关闭依据。此前仅24份完整题摘与19安全单项不能证明15/39/27/18窄入口已全部筛完；撤销“可冻19/普通0”的预期，不推倒19份不变有效Source/PRE/实际POST。作者实际回四份已有raw完整标题：systems15、learning39、multimodal27、narrowAgent18，按arXiv ID去重89个元数据身份（不是89当窗新论文/候选）。广Agent108/截断67与错误monthly仍只线索，不重新查询或全类扩波。

本轮实际按exact-v1官方abs/API逐项补完整题摘，潜在项如下；方法只18330§2–3、19008§1/3作决定准入的定点核，其余只题摘不采摘要收益。API按具名id_list首版逐批取8/9项，返回ID逐项回对；所有日期/撤回或明确先公开信号仍须必要official header/history门，不凭API published/大ID/4月份ID臆断当日或窗外。新拟潜力47（含日期必要门）+拟EX18是完整题摘后的可复核准入请求，不是自动47候选/评分/全文队列；原24身份另已有有效准入/日期/EX。每条原约束→具体潜在增量→拟改变选择写下，不仅靠owner映射。root已own18272必要准备，作者不重复其Source。

| exact-v1身份 | 完整题摘后的具体增量/决定性含糊点 | 当前层级 |
| --- | --- | --- |
| [18168 exact-v1](https://arxiv.org/abs/2603.18168v1) | 有限步残差块的depth/width/embedding联合极限→参数预算缩放误差；理论适用有界QK，拟核假设，不按理论/小模型排除。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18202 exact-v1](https://arxiv.org/abs/2603.18202v1) | decoder和增强均有成本→redundancy-reduction内部防collapse替代→world-state表示/动态学习边界。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18272 exact-v1](https://arxiv.org/abs/2603.18272v1) | 单独SFT或记忆检索外推不足→训练时消费retrieved trajectories→迁移条件；v1不含later failed-attempt保证，root准备。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18325 exact-v1](https://arxiv.org/abs/2603.18325v1) | 固定训练数据分配昂贵→按当前错误分配SFT teacher/RL burn-in→autocurriculum理论样本/预算界。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18330 exact-v1](https://arxiv.org/abs/2603.18330v1) | 未治理记忆会陈旧→FSRS/utility/auction三路径→遗忘与召回取舍；定点v1§2–3见Llama temporal过剪反退，非‘治理总更好’。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18336 exact-v1](https://arxiv.org/abs/2603.18336v1) | 预测均误差不控制风险→distributional state/backend/constraint接口→uncertainty进入sample-predict-constrain loop。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18342 exact-v1](https://arxiv.org/abs/2603.18342v1) | rollout mean会稀释风险spike→window max/振荡权重/DoF calibration→失败判别消费者而非安全控制。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18361 exact-v1](https://arxiv.org/abs/2603.18361v1) | 人造commonsense情景狭窄→两阶段合成拟改quality/diversity取舍；决定新增含糊需最小方法核，不因新数据集自动留。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18409 exact-v1](https://arxiv.org/abs/2603.18409v1) | 线性chunk丢跨段关系→SIR与抽取路由/容量审计→索引结构身份与成本分责。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18464 exact-v1](https://arxiv.org/abs/2603.18464v1) | 同步VLA rollout阻塞→physically decoupled三执行域与trainable world-model虚拟经验→policy/state freshness与质量接口。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18472 exact-v1](https://arxiv.org/abs/2603.18472v1) | 视觉符号识别弱却推理答对→同离散semantic-space分责测recognition/reasoning→评价代理是否掩盖感知失败；科学题仅受测人口。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18480 exact-v1](https://arxiv.org/abs/2603.18480v1) | 可见游戏线索不等潜在engagement→pointwise/pairwise及theory/RAG对照→评价失配是否受控；非负面自动排除。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18524 exact-v1](https://arxiv.org/abs/2603.18524v1) | 2D身份缺未见视几何→单帧空间优化与不对称多视图conditioning→geometry/motion更新隔离。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18532 exact-v1](https://arxiv.org/abs/2603.18532v1) | 实机RL多样性昂贵且scene过拟合→生成可交互3D场景+domain randomization→scene diversity与sim-real分责。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18545 exact-v1](https://arxiv.org/abs/2603.18545v1) | 单腐蚀不涵盖输入pipeline→多stage保持可读约束攻击/teacher token repair→分布组合与repair迁移；医学人口不自动EX。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18600 exact-v1](https://arxiv.org/abs/2603.18600v1) | 双流cross-attention/CFG训练采样不齐→时序RoPE/context token/task routing/UCG→同步与unconditional支持分责。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18620 exact-v1](https://arxiv.org/abs/2603.18620v1) | context自改只借模型能力→按下游性能增益训练一次edit+tree loop→test-time上下文编辑训练/执行分离。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18627 exact-v1](https://arxiv.org/abs/2603.18627v1) | open-loop图像flow累计位置错→中间latent critic/velocity steering+lookahead→critic误差/搜索费用与生成提交分责。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18639 exact-v1](https://arxiv.org/abs/2603.18639v1) | 单视视频物理运动含糊→正交foreground生成/geometry attention→background合成与跨视先验分离；v1题PhysVideo非current OrthoPhys。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18765 exact-v1](https://arxiv.org/abs/2603.18765v1) | judge会把风格当内容→同内容surface perturbation跨math/code/essay→style偏差分人口检验。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18811 exact-v1](https://arxiv.org/abs/2603.18811v1) | 手工sim资产/轨迹限制数据→视频motion prior对齐可执行机器人轨迹→视觉/运动学/几何验收分责。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18859 exact-v1](https://arxiv.org/abs/2603.18859v1) | terminal sparse缺state信用→state graph拓扑传播→代理贡献与dense reward消费，不授objective因果。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [18892 exact-v1](https://arxiv.org/abs/2603.18892v1) | 只answer准确不保空间定位→Acc@50IoU联合answer/bbox门→compositional spatial评估盲区。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19008 exact-v1](https://arxiv.org/abs/2603.19008v1) | topic相关不区分答案→hypothesis支持/对比/线索三query，假设不直接交generator→检索端anchoring与决策效用。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19025 exact-v1](https://arxiv.org/abs/2603.19025v1) | 重算/完整proof昂贵→Merkle committed trace随机抽路径→soundness/efficiency与模型身份验证假设。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19028 exact-v1](https://arxiv.org/abs/2603.19028v1) | dense空间bias/task纠缠→SAE feature区分与modulate→公平和语义保留条件。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19048 exact-v1](https://arxiv.org/abs/2603.19048v1) | FVD混动态/几何失真→静动态分开并核静态子区域camera-pose散度→metric有效性与pose proxy。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19097 exact-v1](https://arxiv.org/abs/2603.19097v1) | 源语言/英语检索不齐→两subquestion graphs合并/双语retrieval→多语言污染与预算分责。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19118 exact-v1](https://arxiv.org/abs/2603.19118v1) | self-consistency不等可信度→多sample verbal confidence/一致性联合与domain反侧→不确定性消费者与费用。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19131 exact-v1](https://arxiv.org/abs/2603.19131v1) | FLOPs/TPS不等具身总费用→压缩/稀疏/actionchunk受控对照→完成时间/jerk/energy联合评价。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19144 exact-v1](https://arxiv.org/abs/2603.19144v1) | 表示bias会跨组件迁移→attention/hidden counterfactual约束及log-space/anchor→行为/能力保持接口。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19149 exact-v1](https://arxiv.org/abs/2603.19149v1) | 固定预训练再专域缺联合预算→base与continued-pretraining loss/scaling allocation→域分叉/compute选择条件。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19152 exact-v1](https://arxiv.org/abs/2603.19152v1) | format/长度/低资源探索冲突→variable entropy advantage/asymmetric clip→约束奖励与collapse边界。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19183 exact-v1](https://arxiv.org/abs/2603.19183v1) | SAE可解释不等可迁移动作→memorized-demo/primitive指标+跨scene steering→内部特征与行为因果分账。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19201 exact-v1](https://arxiv.org/abs/2603.19201v1) | 视觉不见接触状态→tactile future/contact policy/60Hz reflex模块→预测与真实触觉误差校正责任。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19209 exact-v1](https://arxiv.org/abs/2603.19209v1) | ImageNet高不等VLM强→匹配初始化SSM/ViT与dense-task adaptation→visionencoder替代/定位稳定条件。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19219 exact-v1](https://arxiv.org/abs/2603.19219v1) | 多视2Dtoken不一致→3D deformable scene token+多头重建/occupancy→共享视觉状态编码消费者。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19222 exact-v1](https://arxiv.org/abs/2603.19222v1) | 固定noise schedule随分辨率冗余→图像频谱界与per-instance tight schedule/条件采样→推理未知输入与训练调度。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19233 exact-v1](https://arxiv.org/abs/2603.19233v1) | language敏感度表象受scene task混杂→null/wrongprompt/activation injection跨六VLA→视觉motorprogram/goal分责评价。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19235 exact-v1](https://arxiv.org/abs/2603.19235v1) | 显式3D标注稀缺→video-diffusion中间noise features/gated semantic fusion→生成prior读取不等真实几何。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [19348 exact-v1](https://arxiv.org/abs/2603.19348v1) | uniform layer预算假设→importance/ablation/recovery与growth训练对照→结构heterogeneity是否可分配预算；非小模型自动排。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [20299 exact-v1](https://arxiv.org/abs/2603.20299v1) | flat code检索不见architecture→theory/code多分辨率抽象/压缩→层级检索与cost-optimality条件；先核真实公开日期。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [20307 exact-v1](https://arxiv.org/abs/2603.20307v1) | clip去噪不能frame控制→AR sink-window/frame-condition streaming→身份缓存与帧级控制；先核日期。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [20309 exact-v1](https://arxiv.org/abs/2603.20309v1) | black-box KG schema未知→anchor grouping/bubble graph扩展+informative-subgraph问题→召回/证据比较与查询费用；先核日期。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [2604.09629 exact-v1](https://arxiv.org/abs/2604.09629v1) | 六persona合成与O-GRPO优化声称→决定是否有独立算法/数据多样性条件；含糊只最小方法，先核首公开日期，不因humor题自动EX。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [2604.13061 exact-v1](https://arxiv.org/abs/2604.13061v1) | 单output confidence不见交互耦合→raw-token双向predictability+context-response-nextprompt→结构/语义分账；先核首公开日期。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |
| [2604.13064 exact-v1](https://arxiv.org/abs/2604.13064v1) | skill registry平台风险信号不等恶意真值→submission-time可见字段预测与观测缺失→分发/准入风险评价；先核首公开日期。 | 拟潜力，待root独立准入校准及必要公开日期；未评分/Source/PRE/Books。 |

### 代表与明确范围排除请求（root待校准，非Source完成）

- [18178v1](https://arxiv.org/abs/2603.18178v1)：完整v1AB：metadata captions/LLM descriptions/VQA/CoT既有监督组合重训dashcam事件，指标从zero-shot到域adaptation未提出可复用新训练或时序条件，非因驾驶名/收益大关闭。
- [18196v1](https://arxiv.org/abs/2603.18196v1)：完整v1AB：MITRE query-library筛日志再RAG重构attack是安全分析应用；局部无RAG漏attackinfra未定位新的通用retrieval/执行条件，不给领域召回/美元数字主线贡献。
- [18256v1](https://arxiv.org/abs/2603.18256v1)：完整v1AB：de novo分子生成/性质奖励与分子diversity benchmark，AI for Science范围暂缓；不是因RL术语或小实验。
- [18266v1](https://arxiv.org/abs/2603.18266v1)：完整v1AB：actor-centric Transformer用于交通intersection轨迹/交通指标，未见新增foundation-model表示/世界state消费或通用系统条件，不能只WorldModel命名准入。
- [18294v1](https://arxiv.org/abs/2603.18294v1)：完整v1AB：health query临床人口/伪真实需求构成新领域benchmark审计，taxonomy汇总未新增通用测量/模型机制；不能只能映射evaluation收录。
- [18314v1](https://arxiv.org/abs/2603.18314v1)：完整v1AB：graph Transformer+imitation/PPO给branch-and-bound ASM选节点，是一般图匹配应用，不服务模型compute/state，也无LLM/Agent执行新条件。
- [18328v1](https://arxiv.org/abs/2603.18328v1)：完整v1AB：wavelet/tanh/softplus自适应activation用于PINN/PDE，AI for Science暂缓，不以训练词扩大。
- [18397v1](https://arxiv.org/abs/2603.18397v1)：标题足够明确：FlowMS从mass spectra反推分子结构，AI for Science范围暂缓；未读AB/方法，不声称实验审阅。
- [18641v1](https://arxiv.org/abs/2603.18641v1)：完整v1AB：CLINC150 intentclass以MIR/LwF/HAT和组合比较，结论仍replay/架构依赖的既有分类配置选择，未定位foundationmodel的新failure边界或可复用算法变化；非所有负面/小模型排除。
- [18853v1](https://arxiv.org/abs/2603.18853v1)：完整v1AB：differentiable AAV无线data-collection梯度/kinematic channel任务算法，不涉及foundation模型world-state/语言动作接口；不以worldmodel词自动准入。
- [19044v1](https://arxiv.org/abs/2603.19044v1)：完整v1AB：科学ideation方法/rigor proxy和groundtruth scientificmethod优化，AI for Science暂缓，不通过训练owner重新引入。
- [19136v1](https://arxiv.org/abs/2603.19136v1)：完整v1AB：autoencoder regime+双预测Transformer+SAC阈值/混合权重服务股价，领域预测配置而非foundation主线机制。
- [19225v1](https://arxiv.org/abs/2603.19225v1)：完整v1AB：财报/trading新金融benchmark＋常规question校准审核，retrieval跨text/time-series差异未定位通用算法或受控模型failure条件，不因金融关键词自动EX。
- [19231v1](https://arxiv.org/abs/2603.19231v1)：完整v1AB：单图articulated3D reconstruction渐进part/motion表征，领域重建算法/指标未指向foundation模态接口或通用world-action机制；不是只看名字含3D。
- [20311v1](https://arxiv.org/abs/2603.20311v1)：完整v1AB：ReQuesAct澄清意图→RAG工具生成→LLM validation是DataOps/KFP领域已知proposal/clarify/check组合，未披露新的可复用执行、effect/授权或验证成立条件；拟代表EX待root，如认为决定性core需核可定点重开。
- [22309v1](https://arxiv.org/abs/2603.22309v1)：标题足够明确：UniFluids neural operator/flow学流体，AI for Science暂缓；未读AB/实验。
- [26721v1](https://arxiv.org/abs/2603.26721v1)：标题足够明确：ECG stress分类ViT是医疗领域预测应用；未读AB/实验，不把标题范围关闭当贡献深审。
- [2604.09631v1](https://arxiv.org/abs/2604.09631v1)：完整v1AB：Jetson YOLO object/lane input故障注入资源表征，LLM/LDM仅故障样本生成，无新增model-runtime可靠性/资源机制或受控大模型系统边界。

必要首公开日期不因完成题摘自证；IDs20299/20307/20309及2604前缀有与提交query不同公告批次的可能，先定点官方announcement/注册/可靠publicreceipt，不先冒BJT03/20确定新增。未扩大venue/作者史，不因日期未解读方法绕门。未获本轮DAY/冻结新分母。

### 受影响大ID/日期信号的必要具名原字段（不是新的发现入口）

实际取得以下8份arxiv-issued DataCite JSON；保留字段原语义，不把published年份或Submitted直接改写为first-public。19235是常规03/20登记邻接对照；19348/v1更新与登记03/23，20299/20307/20309是03/24，三2604是04/14或16。与ID在announcement过程分配的官方说明合用，仅可裁对应arXiv公开批次；作者可能其他先公开须具体原event，不能沿query提交范围冒本03/20。未读这些材料方法来绕日期，待root独立限定归属裁决；不新增query/全venue。

- [2603.20299 DOI原JSON](https://api.datacite.org/dois/10.48550/arXiv.2603.20299)：created=2026-03-24T03:18:43.000Z，registered=2026-03-24T03:18:44.000Z，state=findable，published仅2026；Submitted=2026-03-19T07:41:52Z；Updated=2026-03-24T00:03:02Z；Available=2026-03。
- [2603.20307 DOI原JSON](https://api.datacite.org/dois/10.48550/arXiv.2603.20307)：created=2026-03-24T03:18:54.000Z，registered=2026-03-24T03:18:55.000Z，state=findable，published仅2026；Submitted=2026-03-19T15:15:17Z；Updated=2026-03-24T00:03:17Z；Available=2026-03。
- [2603.20309 DOI原JSON](https://api.datacite.org/dois/10.48550/arXiv.2603.20309)：created=2026-03-24T03:18:57.000Z，registered=2026-03-24T03:18:57.000Z，state=findable，published仅2026；Submitted=2026-03-19T16:00:36Z；Updated=2026-03-24T00:03:20Z；Available=2026-03。
- [2604.09629 DOI原JSON](https://api.datacite.org/dois/10.48550/arXiv.2604.09629)：created=2026-04-14T03:14:00.000Z，registered=2026-04-14T03:14:01.000Z，state=findable，published仅2026；Submitted=2026-03-19T13:12:53Z；Updated=2026-04-14T00:01:57Z；Available=2026-04。
- [2604.13061 DOI原JSON](https://api.datacite.org/dois/10.48550/arXiv.2604.13061)：created=2026-04-16T01:43:19.000Z，registered=2026-04-16T01:43:20.000Z，state=findable，published仅2026；Submitted=2026-03-18T18:10:37Z；Updated=2026-04-16T00:00:37Z；Available=2026-04。
- [2604.13064 DOI原JSON](https://api.datacite.org/dois/10.48550/arXiv.2604.13064)：created=2026-04-16T01:43:23.000Z，registered=2026-04-16T01:43:24.000Z，state=findable，published仅2026；Submitted=2026-03-19T14:31:22Z；Updated=2026-04-16T00:00:39Z；Available=2026-04。
- [2603.19235 DOI原JSON](https://api.datacite.org/dois/10.48550/arXiv.2603.19235)：created=2026-03-20T02:31:48.000Z，registered=2026-03-20T02:31:48.000Z，state=findable，published仅2026；Submitted=2026-03-19T17:59:58Z；Updated=2026-03-20T01:20:33Z；Available=2026-03。
- [2603.19348 DOI原JSON](https://api.datacite.org/dois/10.48550/arXiv.2603.19348)：created=2026-03-23T01:49:12.000Z，registered=2026-03-23T01:49:12.000Z，state=findable，published仅2026；Submitted=2026-03-19T16:59:17Z；Updated=2026-03-23T00:03:01Z；Available=2026-03。

65具名完整首版题摘的可复用原字段保存[SUP_FINITE_REMAINDER_EXACT_AB_20261011.json](./SUP_FINITE_REMAINDER_EXACT_AB_20261011.json)：官方API id_list逐项指定v1/max_results100，实际返回65/65，保留id/title/summary/published/updated/comment值，逐ID回对。XML未保存（工具中段截断的临时输出已替换），JSON是原字段投影，不声称原HTTP逐byte文件或新增Evidence。三明确标题范围项的AB只保存供非作者抽检，作者不追加其实验审阅。published仍提交口径，必需公开门另核，不冒first-public。

### root 非准备者的受影响集合准入校准

root 实际读取上述65份 exact-v1 完整 title+abstract 原字段；分0–17、18–31、32–47、48–64四个读取段，首段18765的中段截断已单独完整补读。仅针对原四窄入口89身份中漏筛的65；不重开广Agent108、不新增查询。题摘读完不代表实验审阅或首公开日期通过。

原47拟潜力的处理：38项具体增量可继续必要日期与最低充分证据审阅，18361仍需一次决定准入的最小方法核，18480改为具体贡献关闭，7项19348/20299/20307/20309/2604.09629/2604.13061/2604.13064先隔离本窗日期门，不读方法绕门。18202/19025/19097/19233/19028的既有正式发表/先稿信号只定点核事件；accepted 字样不自动证明重复，提交时间也不证明公开时间。不因必要证据可能难读而缩掉其余38，不预支评分、Evidence或Books。

保留的38项不只依靠章节映射：例如18464将VLA训练/推理/rollout物理解耦并让world-model经验进入同一异步闭环；18600给跨模态条件/无条件接口与CFG训练部署不齐提出可核机制；19209以matched初始化/密集任务适配反核ImageNet指标是否预测VLM组件质量；19233把scene/goal混杂与视觉/语言路径干预分开；19131核算VLA计算优化是否转化为真实动作费用；19048用静动态分离和局部pose散度区分视频几何与一般质量；19008改变支持/区分/线索查询人口，而不把初始假设当最终事实。这些是待证的具体设计差异或反证，不采题摘中的最高收益、全领域最优或可靠性保证。

18480完整AB仅在九FPS游戏的潜在engagement标签上比较pointwise/pairwise和六提示策略，所述perception–understanding gap尚未建立本项目通用模型机制、测量混杂的受控边界或新的检索/执行条件；不是因游戏名、负结果或小模型排除。18361题摘只说两阶段合成与quality/diversity提高，新增的数据构造机制及比较条件尚含糊，需一次最小方法后即停止准入判断。

### 18361 决定准入的最小方法核（作者准备，待 root 独立裁）

resume_mar18 实际打开 [CommonSyn exact-v1](https://arxiv.org/html/2603.18361v1) §3.2–3.4 / Eqs1–3、§4.1/4.3/Table3、§4.5/Table6–7 与直接限制 §6；只为消解题摘准入含糊，不称标准 Source / Books 判断已通过。明确新增链：原人造概念组合覆盖窄、单一生成器/直接合并候选不能同时保证 quality 与 diversity → 两 seed anchor 生成 bridge concepts，三种生成策略构成候选，先按 plausibility threshold 与同 concept 内 embedding 多样性取样，再按全池质量+多样性排序 → 可以重新考虑“只保高分句子 / 仅做全局去重 / 直接加大合成池”对训练后输出多样性的取舍。不是为数据集规模或任务名入选。

具体可核对照：Table3 单动态生成 Overall48.3 / S-Cos24.6，与多句生成40.4 / 36.3分居不同方向；统一候选47.2 / 31.4，最终CommonSyn44.7 / 34.2，不是最终方案在所有指标统治全部 baseline。Table7 Q-based46.1 /30.8、G-based41.4 /35.1、CommonSyn44.7 /34.2提示过滤信号的取舍，不能把 Pareto 广告授每项提高。Q评分器§3.4写Gemini2.5Flash、§4.5却称GPT4o，与§6避免评价模型当scorer的表述冲突；若后续准入只采受限 local/global selection 接口，须隔离精确scorer身份/配方与因果归属，不隐藏该问题。合成/筛选/训练数量、token和judge预算还需必要审阅，不提前认证成本更低、无泄漏或通用改善。§6明确global pairwise比较可成规模瓶颈，two-seed模块只适用离散keyword输入、不能直接迁到通常seq2seq；英文/teacher/evaluator proxy限制不因范围小而关闭。

作者据此建议保留具体潜力，待 root 独立准入裁决及必要日期；不自行评分/加入确定候选，不在本次继续无关prompt/附件或直接写Books。

root 已独立实际读 exact-v1 §3.2–3.4、§4.1/4.3/Table3、§4.5/Table6–7及 scorer 冲突位置；本次最小决定准入核通过：两级选择后质量与多样性仍分叉，提供可核验的数据筛选分支/条件，不仅扩数据集。只授继续必要日期与最低充分证据审阅，不授整体 Pareto 统治、精确 scorer recipe、无泄漏或全费用优势，也尚不计确定候选、Source完成或 Books。

原18拟EX全部完整题摘已读，具体范围/贡献关闭理由成立；三标题范围项仅作者未读AB，root此轮为抽检读了原AB，不授实验审阅。FinTradeBench虽有多信号分类及检索差额，摘要的金融population/数值审计组合尚未建立可迁移的检索算法或受控系统测量修正；kRAIG的clarify→retrieve→generate→LLM check也未披露新的执行/授权/验证成立条件。安全分析RAG、领域驾驶后训练和一般continual intent分类的局部配置结果不以主题关联晋升。以上不否认这些研究自身价值，也不声称已经核过所有全文反证。

本节是独立准入收尾，不是DAY；author需继续必要公开日、当前官方纠错信号与逐项Source/具体owner/写后验收。19原安全处置不重审，最终候选分母尚未冻结。

### 18202 R2-Dreamer：必要首次公开门定点恢复

作者仅在本21有限列表核[official exact-v1](https://arxiv.org/abs/2603.18202v1)完整AB/currentheader/history：v1 Submitted03/18T18:54:07Z、v2Submitted03/20T02:05:12Z，comment/journalreference具体写Published as conference paper ICLR2026。不能仅arXiv注册夹证把论文first-public当03/20，accepted也不自动关闭为2025重复。

一次exacttitle限官方OpenReview定位同稿[Je2QqXrcQq](https://openreview.net/forum?id=Je2QqXrcQq)，索引返回namedcamera-ready及[匿名PDF身份](https://openreview.net/pdf/4f83dcd766c20308dfae8be43ba831f7061cb717.pdf)完整AB相符；索引7/11monthsago仅发现信号，不作原发布日期或精确版本差额。fresh官方forum及两个PDF实际转challenge；api2 notes同ID的web请求InternalError，实际原API请求HTTP403/ChallengeRequiredError，没有取得公开cdate/tcdate/pdate及PDF版本公开记录。先一次未引用URL的curl因shell问号未加引号失败，随后正确quoted请求取得上述真实403；不将本地语法失败当外部不可达。

当前仅必要日期终态隔离提案，待root非preparer：不评分、不列确定当窗新候选、不读方法绕门或记假EX/NC。一次精确请求同identity原publicnote日期/first-public/version公开记录，或作者/出版方可靠首次正文公开及本窗实质增量说明；返回后只核first-public/必要delta与本项潜力，不扩ICLR历史/作者全史。该门不推倒已有效29安全单项，不阻止其他普通工作。

### 19025 Verifiable AI：必要SaTML/ePrint日期信号

本有限原列表[arXiv2603.19025v1](https://arxiv.org/abs/2603.19025v1)完整题摘/header/history actual核：v1Submitted03/19T15:24:27Z，Accepted SaTML2026；accepted本身不假定早发同稿。只exact-title回到[官方SaTML program](https://satml.org/2026/program/)同题/七作者，Mar23–25会议链接指arXiv，会议日不能证明首次正文。DBLP仅发现同identity[官方IACR ePrint2026/541](https://eprint.iacr.org/2026/541)，完整原摘要/七作者相同，History为2026-03-17 received、2026-04-01 revised，publicationinfo为Published elsewhere/Minor revision/SaTML；不把received直接改写为公开正文日期，也不把April修订自动当新首稿。

官方See all versions入口https://eprint.iacr.org/archive/versions/2026/541在web Cache miss，fresh真实原站请求为Cloudflare challenge；未取得各版posting/publicavailability日期与首稿可复核版本。本次仅日期门提案待root非preparer，未读方法、未评分或列确定BJT20候选，不授早发重复/EX/NC。一次精确请求同ePrint版次公开/posted日期和可访问首稿或可靠作者first-public及本窗delta；收到只重开此identity，不扩ePrint全年/SaTML全program/作者史。当前31有效单项不推倒。

### 非准备者必要日期裁定

root 独立打开 ePrint2026/541，完整原题摘/七作者及 received03-17、revised04-01 与作者记录一致，版本入口仍不可得；独立打开 Je2QqXrcQq 和 w8Mw9zJt1y 均进入官方 challenge。三项同稿身份/早发线索需公开版本日期才能决定本窗事件，必要日期隔离 PASS：一次请求对应公开 note/posting 与必要版本，不给方法分数、不纳确定新增分母，不假称已审重复、无贡献或 Books 已覆盖。限制只涉及这三项，不阻塞其他可执行工作，不遍历全 venue 或全部旧版本。

19097 与19028不同：root 实际核两 exact-v1 完整题摘/current history；DaPT 原 Crossref 同题八作者 DOI10.1109/ICASSP55912.2026.11462873 created04-21、issued/published-print05-03，SEM 官方 CVF 同题六作者记 June2026 Findings/8101–8110。这些晚于本窗，accepted标签本身不证更早正文；目前没有取得具体早发同稿日期信号，不为此虚造缺材料。可继续按本批 arXiv 官方公开日与 DOI 日级夹证核本次事件并进行最低充分审阅；不声明从未有其他先稿，也不以 Submitted 或搜索索引时间充当公开日。

### 19097 / 19028 / 19233：其余三具名日期信号的最低充分核

以上必要日期非preparer正式裁定已通过，以下是先前作者提案的原字段恢复过程；18202/19025/19233隔离，19097/19028沿本批arXiv日级夹证继续，不继承下述旧“待root裁”标签。

完整原65题摘已复用，各official exact-v1/currentheader/history实际读，不扩query：19097唯一v1Submitted03/19T16:23:04Z；19028唯一v1Submitted03/19T15:28:08Z；19233 exactv1Submitted03/19T17:59:55Z。后两作者project current内容不当March正文或原发布日，会议accepted不是自动提前公开/EX。

19097 [DaPT](https://arxiv.org/abs/2603.19097v1)同题八作者[Crossref exact DOI](https://api.crossref.org/works/10.1109/ICASSP55912.2026.11462873)由exact-title query最多3返回定位，第1title/authors相符，第2/3只是不同稿发现噪声不入队。原字段created2026-04-21T21:25:57Z；published-print/issued/published均2026-05-03；event ICASSP May3–8；resource primary https://ieeexplore.ieee.org/document/11462873/，link content-version=vor。这些为后来正式书目事件，不自行证明全网没有早稿，但没有具体先于BJT20的正文事件日期；提案保本批arXiv限定归属继续必要Source，不因Accepted ICASSP制造早发重复或无限日期追查，待root裁。

19028 [SEM](https://arxiv.org/abs/2603.19028v1)六作者同[CVF原出版页](https://openaccess.thecvf.com/content/CVPR2026F/html/Guimard_SEM_Sparse_Embedding_Modulation_for_Post-Hoc_Debiasing_of_Vision-Language_Models_CVPRF_2026_paper.html)官方搜索原正文AB/bibtex恢复为CVPR Findings2026、June、8101–8110；fresh页403保访问层区别。[作者project](https://sparse-embedding-modulation.github.io/)完整原AB及paperlink只指arXiv，无datefirst-public字段；此处仅核publication/date，不把项目宣传作为性能证据。June出版不说明March之前有公开同稿，提案沿本批arXiv限定事件继续，不认证全网首次，待root裁。

19233 [Not All Features Are Created Equal](https://arxiv.org/abs/2603.19233v1)在官方ICLR Multimodal workshop名单同题三作者，2026-04-26会期本身不是早发正文证明；official PDF identity[OpenReview w8Mw9zJt1y](https://openreview.net/pdf?id=w8Mw9zJt1y)原AB可索引恢复，但forum challenge、api2 web unavailable且fresh quoted原API HTTP403/ChallengeRequiredError，未得public cdate/tcdate/pdate/最早PDF公开版。作者currentproject已经NeurIPS2026/420k人口，而arXivv1为394k，明确不能用新版页面冒March版本原证或展开新版methods。提案一次必要日期隔离：只请求该identity原publicnote日期/first-public/version，或可靠作者首次正文公开记录；未闭合前不评分/确定候选/读methods绕门，不假2025EX/NC。以上三者各待root非preparer日期裁，不算Source或safe；当前32安全结果仍有效。

### 18545 CoDA：决定性贡献关闭，root独立校准通过

完整exact-v1题摘原件仍在SUP_FINITE_REMAINDER_EXACT_AB_20261011.json id=http://arxiv.org/abs/2603.18545v1；作者与root均实际读完整AB，作者另实际[officialv1](https://arxiv.org/abs/2603.18545v1)header/history和[HTML](https://arxiv.org/html/2603.18545v1)§3.1–3.4/4.1–4.5/Tables1–3决定性core。当前v2Apr3未有明确影响原结论的撤回/纠错信号，不遍版本diff。DataCite真实created03/20T02:15:10Z/registered02:15:11Z/statefindable，v1Updated00:39:12Z；日期只保原字段，不为了不影响贡献关闭的日期证明全网最早。

具体EX理由：实际新增是医影三种固定变换链在四medical CLIP/binary disease数据上的参数搜索、technicalqualityauditor案例与clean tokenadapter修复；未提供超出既有多扰动最坏选择、Gram蒸馏/表面相似非语义验收、固定archive不等adaptive鲁棒的新大模型主线机制或受控条件。完整AB原潜力把医学pipeline实例上提为通用新接口，决定性§3/4后纠正；不是按medical标签、negative结果、小样本、访问状态或已读工作量排除。root实际独立完整AB正式同意贡献EX，停止PRE/不评分/不列confirmed候选/不写Books；只raw保原证，不假NC缩池。

已经看到的反侧不删除但不用于扩大临床评价：Eq13为七family择最坏，Table3“fullchain”行实际与Table2winner相同，Table1 RadMRI Randomτ.9单D100而A+R+D15，不能证链始终更强或交互因果；Eq7组合符号/文字order不采recipe。SSIM/ROI门只图像相似不认证临床可读/病理不变，singlecall自挑战非独立往返，teacher按被攻击成绩选择/clean-only residualW与Gram对齐、只测旧archive不认证适配后重新优化攻击。这些是局部实例/成熟验收边界，不以假安全保证或一般控制术语重新准入；不读临床全史/全部prompt/图或code。

## 既有有限余项贡献与最低充分停止

2026-10-12有限余项的完整原AB实际回对（不新增query/名单，不把本段当Source完成）：18627具体是中间latent critic/rollout选择写回field，18639是orthogonal foreground→背景合成的几何条件消费，18811是视频motion→kinematic轨迹映射而非视频像真即可执行，18859是stategraph终点贡献传播替processRM；19048静/动态分账后局部camera pose差异修正FVD盲点，19097原语言/英文subquestiongraph合并与双语检索，19118verbal与selfconsistency在相同sample预算下的互补/域反侧，19131固定success仍完整执行费/轨迹指标反退。19144反事实attention与hidden联合约束及行为/anchor代价，19152entropy-conditioned advantage/asymmetricclip的探索取舍，19183episode记忆与可transfer primitive的steering区分，19201预测触觉与实测residual/reflex消费，19209匹配初始化及denseadapt下encoder与定位反侧，19219多视角scene token和独立解码目标，19222instance spectral噪声边界及推理时schedule可得性，19235视频中间noise特征→MLLM gate的接口。各自有题摘中明确新增机制/有效性条件或设计反证，不只主题/owner关联；后续仅读支持该点的方法与关键对照决定是否可采用、具体NC或中心隔离，不因已读AB/原潜力数自动全文。原准入独校有效复用，必要日期及证据仍各自未完。
