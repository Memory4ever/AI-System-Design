# Jun03 / MODEL B6 必要Source与owner提案

只补2026-06-02 BJT。恢复已完整重读AGENTS、当前研究/Report合同、Sources使用说明/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State及MODEL当前路由；Books提案前读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE。B5、00476/02031等有效必要/POST层沿root通知复用，不第三审。R26/R28余48完整题摘准入及联合日证不是48 Source完成；本轮按原表首01400准备单篇即交，不扩四定义/DEPOT/交接/别日。无Books/Report/State/index写权，不预I、Source通过或DAY，年度153/279不变。

## 01400 Consistent and Distinctive — 2+1+2=5 / 最小测量差额，图覆盖保证不采用

[exact-v1 PDF](https://arxiv.org/pdf/2606.01400v1) / [保存PDF](SUP_MODEL_B6_2606.01400v1_20261024.pdf) / [HTML原件](SUP_MODEL_B6_2606.01400v1_20261024.html)。HTML在§3后大量乱码，未将其当可读正文；本轮回精确PDF必要§3–7/Tables1–6、Limitations，PDF文本与HTML尚可见式联合核方法方向，未看图像像素、全附录、代码或复现实验。2026-10-24本轮实际打开[当前官方abs](https://arxiv.org/abs/2606.01400)，title/history唯一v1，所见无withdrawn/removed/erratum，不是无任何纠错的全网保证。日证沿R26/R28及原V1/DC有效原件：v1 `Sun, 31 May 2026 18:45:12 UTC`，同DOI `10.48550/arxiv.2606.01400`、arxiv.content查询限定/findable、registered `2026-06-02T04:14:40Z`；适用发号/公告规则最早界Jun02 00Z至登记最晚界全落Jun02 BJT，不将提交/登记单字段叫实际公开，不重复GET日期原件。

### 采用命题与分数

Design2：压缩评价的seed间排名concordance与相对全量排名fidelity应分开度量，内部稳定可与目标排名偏移共存；Reach1为evaluation subset-builder/测量组件；Durability2为可复用的两种参照人口分责，总5。不把MIS、embedding或一般“评估要版本化”成熟原则计分，不为复杂性机械升deep；具体owner差额及方法冲突受影响域已定点读足。拟只采用两轴测量边界，不采用最大分散、去偏或净省费保证。

### 必要方法、对照和直接反侧

原prompt转embedding、按pair measure/percentile threshold构图，再以CPLEX、GREEDY、Online-MIS或ReduMIS求独立子集。原文§3直接规定**edge在distance d≥θ时存在**，故独立集中任意两点d<θ；这一数学对象不是通常近邻连边后的分散点集。紧接“半径θ/2区域最多一点”并不由它推出：两个相同/极近embedding在θ>0时无边、可同时选择且处同球，即是简单反例。§4又并列cosine similarity、Pearson correlation distance、standardized Euclidean distance，未给统一转向定义；不能自行把≥改≤、把全部distance改similarity或由标题MIS补齐真实构图实现。不同段声称coverage均匀、每区域只取一点、rank变化纠偏及embedding隐含领域真实性均不采用。此为具体未闭的方法/保证冲突，不是访问失败；代码/数据仅称可向作者索取，当前不为可选实现无限追索。

排名测量则明确分两人口：每子集按其中各模型平均分排名，对全量排名算Spearmanρ；对随机求解器五seed的各排名算Kendall W。确定性CPLEX/GREEDY不报W。定义本身允许各seed稳定地选出同一种偏置人口，不应把W高当ρ高或更正确排名。Table4作者汇总p10 W=.9901而ρ=.905，p80 W=.9993而ρ=.992，说明其报告的两轴并不相同；Table3 IFEval Online-MIS W=.9907、ρ=.921。这里只采用这种有限对照/分责，不把aggregate当每配置保证，不把低ρ自动认证全量有偏或子集更公平。§7将低ρ有时解释为feature，仍无独立构念/领域真值验证，无法以同seed认可替代该证据。

§4的评价基于HELM既存逐题/模型scores，四个英文single-turn benchmarks：GPQA446、IFEval541、MMLU-Pro1000、Omni-MATH1000；66模型panel。不同模型的HELM prompting可不同，非受控统一重跑；原文快照声称May2025/mid2025，但当前模型名单/引用不据此认证精确historical model版本。六embedding有encoder510-token分块加权及decoder≤4096 full/chunk两视图、L2归一；阈值用10000随机pair估计p10/20/50/80/90/95，选择embedding不等任务难度或受测能力的外部truth。2592 grid实际2563，未完成配置保缺口；不把2 failing、99.2%等混合统计倒算成已核精确全部人口。随机solver五seed是subset选择复验，不是66模型答案采样/生成seed复验；未见独立held-out model-family验证，不授新model迁移或新scorer稳定。

原文1000node局部solver约CPLEX30–120s、GREEDY<1s、Online/ReduMIS600s；未绑定完整硬件/embedding精度与服务length/batch/concurrency/SLO，不采用生产净加速。benchmark每题保存分数可以离线replay，少选题不等真实请求/总费用同比下降；embedding、pairwise建图、solver/调threshold、五seed、anchors与完整审计全计费。Limitations明确embedding不分离的子域仍可混淆、English及固定panel，未验多语/code。保留原完整基准、分层随机/固定subset为回退，不以均匀几何代真实任务权重。

### actual-owner与逐字PRE提案（未独核或授写）

唯一owner `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。实际读当前Benchmark-compression三段与SQL/evaluator-design直接前后，Ch65/67开篇职责；精确01400/题名无现family。已有正文要求rank consistency、heldout family、score/ranking fidelity分验与全量回退，但未明确**重复subset种子之间的concordance，与对完整基准的fidelity**两种rank参照。只在已有compression artifact总段之后补一自然段，两旁不改；不另开图算法教学或复制Ch27数据筛选。

上锚完整直接段：
> Benchmark compression 本身也要成为版本化 evaluation artifact。Compact subset 应绑定完整 anchor logs、subset builder、score error、rank consistency、held-out model family 与失效条件；无法给出 fidelity budget 时，就只能作为加速 preview，最终 release 回退完整 benchmark。压缩减少重复运行，却可能删除极端 slice，并且先跑完整 anchors 的成本没有消失。

上锚后的既存独立marker `<!-- source-family:SF-2026-ARXIV-2609-12475 -->` 留原位；拟段放该marker之后。

拟融合单段：
> 压缩子集的排名稳定还须声明参照：不同selection seeds之间的concordance，和每个子集相对完整benchmark的ranking fidelity不是同一量，多个seed可能稳定地偏离原人口。[受限图选择研究](https://arxiv.org/pdf/2606.01400v1)报告了这两轴的分离，但其距离连边方向与分散覆盖论证不一致，不能据此采用去重均匀或纠偏保证；低baseline相关也不自动表示子集更公平。应分别保留每seed的实际题目/权重、完整anchor排名及held-out模型回归，把embedding、建图、求解与调参都计费；两轴或关键slice失配时回完整基准或已验分层subset，不由内部重复性给压缩后的能力排名签字。<!-- source-family:SF-2026-ARXIV-2606-01400 -->

下锚完整直接段：
> 压缩 benchmark 还须区分当前执行的观察、历史 verdict 的复用与未执行题目的重构。固定难度或分层 subset 可以并行执行并按声明权重估计；adaptive Fisher selection 则把先前回答变成下一题的控制输入，选中的题目不再是代表性随机样本，其 raw mean 不能直接当完整分数。IRT 可以用模型重构未执行题目的通过概率，cache 则取决于旧 verdict 是否仍适用于当前 subject；这三条分支分别承担 estimator、selection state 与 freshness 的假设，不能合成一个“少跑题仍准确”的证书。

**采用边界与停止：** 两种rank参照的定义/有限作者对照可独立于错误coverage保证成立，拟仅这一最小差额；由reader独立判断是否足以采用，不预Source/PRE PASS或I。图构造机制/coverage保证重开只需精确pair measure方向、真实adjacency规则及原始subset与模型score记录或作者纠错；不发布可执行MIS去重recipe、不授生产表现。01387及其后仍只有有效AB/date，未本轮notice/Methods/评分/owner；单篇ready即交root/reader释放本阶段，不等待无关48或四定义齐。未改共享Books/Report/State/index，未stage/commit/push。

## 01387 Fail-Closed Lowering of Resident KV Claims — 2+2+2=6 / 必要Source与Ch45最小PRE

恢复事实：据root本轮直接通知，01400 R63首次独核、root真实SAVE/R65唯一actualPOST已整合生效，不第三；上节“01387未Methods”由本节覆盖。已重读当前AGENTS、研究/Report合同、Sources适用使用/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State和精确停点；owner提案前已读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE与实际相邻。只Jun03补Jun02 BJT，不读其他日期。

[exact-v1](https://arxiv.org/html/2606.01387v1) / [保存HTML](SUP_MODEL_B6_2606.01387v1_20261024.html)。2026-10-24本轮实际打开[当前官方abs](https://arxiv.org/abs/2606.01387)，所见唯一v1、comments为24pages/2figures/publicartifact、无withdrawn/removed/erratum，不作全网无纠错保证。准入/联合日证沿R26/R28及原V1/DC复用：v1 `Sun, 31 May 2026 18:23:21 UTC`，精确DOI `10.48550/arxiv.2606.01387`、arxiv.content查询限定/findable、registered `2026-06-02T04:14:21Z`，适用公告/发号规则最早Jun02 00Z至登记最晚界全落Jun02 BJT；不把submitted/registered单独叫实际公开，不重复GET日证。

实际读§3–5/Tables1–5/lowering判定、§6具体runtime反侧、§7完整patched connector witness、§8/Tables7–8及mutation/归因控制、§9/Table9、§10直接限制及§12artifact provenance。未遍历完整附件、未打开代码/patch、未运行checker或复现实验。D2为从抽象ResidentClaim到可计数义务/adapter深度的具体lowering接口，Reach2跨外部registry/telemetry与scheduler、allocator、restore消费者边界，Durability2为观察不能代enforcement及同claim有序结果责任，总6；不为现有claim字段、普通fail-closed或多runtime名称加分。具体既有owner缺口定点深入，非给所有材料套全deep。

### 支持命题与关键反侧

原有priority、TTL、存储/offload或KV-aware route是有用substrate，不自动接受未来reuse责任。本文将mode的每项obligation分别要求anchored evidence、允许提供该义务的adapter深度及其前提，任何一项缺失不得升级。结果标签区分native、adapter-observational、controlled-pressure adapter-policy、backend-patch、approximate/rejected/unknown；`sound`是curated descriptor字段核对用词，不是证明全部未审runtime路径正确。

`telemetry_join`只能在预登记claim、独立tokenizer-derived request map、固定materialization predicate、同model/tokenizer/hash/runtime/namespace/adapter/blocksize身份、具名观察点和可排序events下重建claim-scoped materialization；post-hoc命名、wrongclaim、重复owner、缺events/order或cacheidentity冲突均不升级。它不能凭日志创造victim exclusion、显式冲突动作、demotion/expiry责任边界或restore failure outcome。hard_protected须相应scheduler与allocator两侧证据（或明确替代contract transition），单一深hook标签不够；storage/restorability又须同claim恢复先于predicate-satisfying reuse，并在失败时先有claim-scoped结果。重算可作回退，但不是offloaded state恢复成功。

§7的正例是local patched vLLM pydev OffloadingConnector真实in-process store/load/transfer与invalid-KV-load路径，不是standalone模拟器；native部分供真实搬运/invalid-block propagation，补丁供pre-request claimmetadata、有序lifecycle join、受控同claim CPU→GPU load failure、scheduler-boundary failure及含blocking_claim_ids的active-refused outcome，analyzer只事后核顺序/身份。这个“refused”在invalid-load处理与terminal finished/error之间，不是initial admission拒绝；也不意味着upstream有用户ResidentClaim API。先offload→hit448→restore required→同claim load失败→scheduler failure/refused→terminal的顺序才是witness，generic error、wrongclaim failure、fallback recompute不通过。

作者§8报告131/131 subprocess事件有效，其中30/30成功观察、30/30受控同claim失败结果、41个false-positive controls中0个被当有效失败结果；这些是不同gate人口，三者不强凑成131全部分类。16/16 descriptor mutation控制只说明对所改anchor/scope/identity/order等敏感，不证明手工descriptor完整或未采路径无bug。双claim归因控制3/3只有target被归失败/拒绝，non-target成功恢复，支持窄归因而非任意并发安全。源码provenance原文区分vLLM base `9b9d5d...`、patched head `0b129d97...`、clean0001–0003与邻接0004未出现在三轮rawtrace，不混成upstream版本；本作者未核这些commit/artifact，引用只作为作者报告证据边界。

直接外部反侧：TensorRT1.3.0rc14/15所测priority与pressure支持adapter-policy而非hard protection；active no-evict仅当前request，不持未来resident。15s/60s duration探测未给claim expiry责任事件；同prompt hash tier0→1→0也不自带claim failure责任。SGLang/HiCache `bbe9c7e` 的cold/warm/wrongprefix cachetokens0/35/0可支持受限telemetry join，storage flags不代restore success/failure；Dynamo只有docs-backed route comparator，不升级runtime conformance。“未建立native”不等证明该runtime永远无法支持或全部版本缺能力。

§10限local small in-process singleGPU semantic mechanism；controlled injection不覆盖任意真实故障，TTFT/statlogger不可用（作者称metrics serialization需disable_log_stats=True），所读域完整model/dtype/length/batch/concurrency/SLO未给可统一泛化配置。没有生产性能主张，不补成低延迟/吞吐收益；registry/join、metadata、hooks、trace/order核验、failure处理与回退重算/recall全部计费。必要命题只为lowering资格，不需为采用它遍历全部实现或复现131runs；没有声称实现已核或生产ready。

### actual-owner/PRE（未独核或授写）

唯一owner `INFER-KV-CACHE` / [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。已实际读Future Reuse Intent整组三段和上方lossy-draft/fullcommit、下方prefix-refresh交接，Ch44/46开篇职责。精确01387/题名无现family；现有`2605.24259`同一ResidentClaim概念已含typed identity/materialization/lifecycle/feasibility/telemetry及失败显式降级，故不再复制claim字段或另建Ch50/56第二owner。尚未承载telemetry-only vs enforcement-bearing adapter深度、sameclaim restore-before-reuse/failedrestore先于terminal、backend patch不等native这组具体lowering界限；只补一自然段，不另贴runtime feature表。

上锚完整直接段：
> 无法满足 claim 时必须显式降级为 recompute、cold-tier recall 或普通非驻留 cache，而不是继续承诺 future reuse。单进程、短生命周期或复用价值很低的 workload 仍可使用简单 hint。`arXiv:2605.24259v1` 的 §3 与 §5 支持这组 claim 字段及作者 active-pressure 合同，§6 不证明所有 cache manager、分布式故障或生产 tail-SLO 都满足该 conformance。

既存独立marker `<!-- source-family:SF-2026-ARXIV-2605-24259 -->` 留原位，新段放marker之后。

拟融合单段：
> 把这份合同落到已有runtime，还须区分“观察到了什么”和“谁能兑现义务”。预登记claim、稳定cache身份与有序events可让外部adapter重建materialization，却不能凭遥测创造victim exclusion、冲突动作或恢复失败结果；这些要由实际scheduler、allocator或storage路径分别提供。[受限lowering机制](https://arxiv.org/html/2606.01387v1#Sx8)要求同一claim在reuse前恢复成功，失败时先于terminal handling给出claim-scoped结果，不能把wrong-claim错误或fallback重算算成restore。作者local patched vLLM在invalid-KV-load边界展示了这条顺序，不是upstream支持或pre-admission拒绝，手工descriptor checker也不证明未审路径完整。Registry、joins、hooks和失败回退都付费；身份、顺序或执行深度不足时保留approximate/unknown与显式重算/recall，不由priority、TTL、tier movement或routing名称签发未来reuse保证。<!-- source-family:SF-2026-ARXIV-2606-01387 -->

下锚完整直接标题：
> ### 双向更新会撤销“共享 Prefix 永远不可变”的前提

### 01387阶段交接与普通下一停点

单篇必要Source/6分与actualowner最小逐字PRE已保存交root/reader，尚未独核Source/PRE通过、不授Books写入或I/DAY。01281及其后只有R26/R28有效AB/date，未本轮currentnotice/Methods/评分/owner；不将其普通待办称外部受阻，不等余47或四定义齐。仅本文件与必要HTML新原件；未改共享Books/Report/State/index，未stage/commit/push，年度153/279不变。

## 01281 POPO — 2+1+2=5 / 必要Source与Ch33最小PRE

据root本轮通知，01387 R66/68真实Ch45保存/唯一actualPOST已生效，行政由root处理，不第三审；本节覆盖01281旧停点。启动已重读AGENTS、当前研究/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State与本日B6停点；owner前重读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE及当前具体正文/相邻。只Jun03补Jun02 BJT，不扩四定义/其他日期。

[exact-v1](https://arxiv.org/html/2606.01281v1) / [保存HTML](SUP_MODEL_B6_2606.01281v1_20261024.html)。2026-10-24本轮实际开[当前官方abs](https://arxiv.org/abs/2606.01281)，所见唯一v1、无withdrawn/removed/erratum，不保证不存在其他纠错。AB准入/联合日证沿R26/R28，不第三：v1 `Sun, 31 May 2026 15:06:38 UTC`，同DOI `10.48550/arxiv.2606.01281`、arxiv.content查询限定/findable与registered `2026-06-02T04:11:47Z`，适用公告/发号规则最早Jun02 00Z至登记最晚界全在Jun02 BJT；提交与登记均不单独叫实际公开。

本轮实际读§4.1–4.3/Eq5–10/Algorithm1、§5.1–5.4/Tables1–2/直接消融说明、§6、Appendix C及D.2必要训练口径；未读全理论proof、图像像素、完整附件、代码或复现。**Design2**为whole-group有效性补槽与behavior/proximal比值分责的具体接口，**Reach1**限训练batch/更新组件而不借RLVR全栈加分，**Durability2**为replay选择人口、陈旧性与trust-reference分离，总5。标准必要层读足；针对actualowner差额与筛选偏差作定点深入，不采用通用收敛、无偏或完整生产recipe。

### 方法及不可继承的保证

每步仍均匀取B个fresh prompts、各生成k条；只将reward std>0的组送入本步更新，缺少的组由capacity B的FIFO历史有效组尾部最新项确定性补齐，更新后再把本步fresh有效组入buffer。重放单位是同prompt同生成policy的完整组，不是只取历史成功response混组；这保留组内行为policy身份，却没有取消按reward波动筛组及按年龄选组对人口的条件化。fresh prompt均匀不等最终update prompt均匀、全组有效不等每条推理正确或新能力有覆盖。

Alg1初始buffer为空，却直接索引B−fresh有效组数的历史项，所读域未定义库存不足/首步冷启动、重复取样或实际缩batch guard；不照录为每一步必满的完整实现。工程上须先声明缺槽回fresh/缩batch/跳步等处理，但这些是本项目要求而非已核作者实现。Lemma4.1的TV≤εn/2依赖**所有state/action每次更新**的ratio都落[1−ε,1+ε]，PPO sampled clipping不是这个硬全域约束，年龄只能是便宜proxy，不能宣布FIFO保证KL/TV安全。

Eq10把current/behavior比值分成old/behavior的外权重和current/old的PPO clipped项；同一old快照作proximal参照而不把每条历史behavior都当clip锚。固定分母且两处均未clipped时是代数相同值/梯度，不授filtered-group、prefix/state分布与历史相关性已被完整校正。Appendix C实作又把old/behavior外权重upperclip到2，进一步改变目标；单个action ratio不提供筛选后buffer/历史mixture密度、也不能替完整序列支持与prompt人口作IS。所有group同policy仅支持可追溯behavior身份，不采其“因此统计正确/完全纠偏”的扩大解释；clip也不是全局trust-region证明。

### 评价、反侧与费用

DeepScaleR40k上的DSR-distill-Qwen1.5/7B、Countdown20k上的Qwen2.5-3B、Geometry3k上的Qwen2.5-VL-3B；8×A100 80GB/VeRL。训练k8、T1/top-p1、B256（math/countdown）或512（geometry），minibatch128/64/256、输出上限8192/1024/1024；无reference-KL，clip低.2/高.28，Countdown entropy .001，其余0。Math二值reward，Countdown/Geometry错误但格式正确还给.1，因此std>0也可能只是格式差而非正确/错误混合；不把三域统一叫binary mixed-correct groups。评估T.6/top-p.95，pass1由多次generation平均；完整dtype、服务并发/SLO及训练seed不确定性所读域Not Disclosed，不能补为生产配置。

主对照GRPO、ARPO、MoPPS与高rollout预算DAPO，Table2 Countdown POPO60.4低于DAPO61.5，Geometry50.0低于50.6；不是全部任务同质量。Math1.5B avg55.1同DAPO但若干子任务较弱；7B avg63.3对63.2不授统计显著普胜。作者runtime1.5B16h对DAPO30h、7B34h对55h，而7B GRPO31h；Countdown3.2h/205krollouts对DAPO5.6h/877k、Geometry6.8h/492k对11.2h/1438k只属各自所测质量与配置。不用headline“无额外计算”遮掉旧组存储、行为logprob/current或old评分、全部fresh失败生成、replay训练与独立回归；更长response也可令其比GRPO更慢。

§5.3 Countdown消融：同replay换old-only目标可collapse、behavior作为clip参照较慢；随机取更大旧池stale10 collapse，stale1略差，replay无效组也退化。POPO-KL用5B候选buffer显式排序、3.2h对4.8h比较同时改buffer大小与selection计算，不认定recency在同预算所有分布等价KL筛选。§5.4群大小/补槽比率与PPO/RLOO兼容仍是Countdown有限证据，不把“可组合”升级全算法/任务保证。近组proxy、buffer支持或独立质量失配时，缩短/停replay、fresh-only或匹配预算补采仍有效。

### actual-owner/PRE（未独核或授写）

唯一owner `TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md)。实际读trajectory生命周期/阶段化replay、FIFO horizon/reuse完整组、成功轨迹只作正则、非均匀priority/行为ratio与弹性replay组以及前后；Ch32/34开篇职责已核。精确01281/题名无既存family。已有FIFO/reuse的长期tradeoff及filtered buffer不等完整分布警戒，不重写；尚缺**std>0整组替零方差空槽、最新有效组与行为/proximal双参照**的具体接口，建议FIFO tradeoff第二段后加一自然段，后接“旧轨迹只提供正则”的替代分支。Ch32不重复写特定group补槽，Ch36不接管其样本统计资格。

上锚完整直接段：
> 增加reuse降低每次更新分摊的生成成本，也使样本影响未来参数，再被同一参数轨迹重复使用；importance ratio纠正边际policy mismatch并不自动消除这种历史相关性。更大buffer可能增加旧policy多样性、缓和过拟合，同时增加staleness；过高reuse又会降低局部样本多样性并退化。应在匹配学习率搜索后比较达到同一质量所需的采样、更新、估算GPU-compute与实际wall-clock，不能只比较gradient steps。受限Qwen0.6B/7B数学实验和有smoothness/bias/variance/correlation假设的理论支持这一条件分支，不提供生产最优buffer常数或frontier-model保证；生成便宜、相关性强、off-policy方差高或证据不足时，fresh-only与更短buffer仍合理。<!-- source-family:SF-2026-ARXIV-2604-08706 -->

拟融合单段：
> 整组reward无差异时，还可保留fresh有效组，再用近期FIFO中reward有差异的完整prompt-response组补更新空槽；组内同behavior policy保留了来源身份，却不让筛组和确定性取最新组恢复原prompt人口。[POPO的受限分支](https://arxiv.org/html/2606.01281v1#S4)另将old/behavior权重置于current/old的clipping之外，分开历史样本校正与proximal参照；逐token比值及其额外上限仍不纠正全部选择、prefix与相关性偏差，年龄也不是硬trust-region保证。Cold buffer不足须明定缩batch或fresh回退，不能假定每步都有足够历史有效组。旧池过陈可collapse，部分任务仍弱于补采基线；buffer/logprob、全部fresh与replay训练均计费，信号、支持或净质量失配时保fresh-only、缩短重放或匹配预算补采，不由更满的有效batch自签无偏、正确性和免费训练。<!-- source-family:SF-2026-ARXIV-2606-01281 -->

下锚完整直接段：
> 旧轨迹也可以只提供正则参照，而不再携带一份直接强化成功答案的 reward 优势。一条[受限动态 replay 分支](https://arxiv.org/pdf/2603.16157v1)保留近期成功轨迹和生成时的逐 token log-prob，按年龄退出 buffer，并在训练早段扩大接纳、随后收缩；当前策略重新读这些 prefix，以 current/behavior token-ratio 形成局部正则，online 组仍按原 GRPO 更新。这里的参照是被成功、难度与年龄筛选的样本及其来源 policy，不是完整旧分布；单个行为 log-prob 不提供过滤后 buffer 或历史 mixture 的密度，因此不能由逐 token 锚自动授完整序列 JS、无偏 off-policy 或语义多样性保证。保存状态、current 前向/反向与超参数搜索均付费，较强正则和更大年龄窗口可能退步；需分别保存选择人口、loss reduction 与 policy 版本，联合验收独立质量、探索和达到目标的全部训练费用。支持失配、正则过强或费用不利时，缩短/停用 replay，保留 current-only、原参照约束与直接 replay 的受控对照，不由概率排名批准能力保真。<!-- source-family:SF-2026-ARXIV-2603-16157 -->

**单篇停止/交接：** 01281必要Source/5分与actualowner最小逐字提案已保存，仍待reader首次必要核/PRE，不授Books写入或I/DAY。下一01168及其后未本轮notice/Methods/评分/owner；四定义由root已校准的题摘/贡献/日期不第三读。未写共享Books/Report/State/index、未stage/commit/push，年度153/279不变；本阶段ready即结束释放槽。

## 01168 HAB — 2+1+2=5 / 必要Source与Ch29最小PRE

root直接通知01281经R69及root原稿真实SAVE/R72唯一actualPOST生效，行政由root负责，不第三；本节覆盖01168旧停点。恢复已重读AGENTS、当前研究/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State与本日停点；owner提案前重读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、目标与相邻职责。不扩root正处理的四定义/negative/CRAM/ProtoAda或任何别日。

[exact-v1](https://arxiv.org/html/2606.01168v1) / [保存HTML](SUP_MODEL_B6_2606.01168v1_20261024.html)。2026-10-24本轮实际开[当前官方abs](https://arxiv.org/abs/2606.01168)，所见唯一v1、11pages/4figures/3tables，无withdrawn/removed/erratum，不保证所有渠道无纠错。准入/联合日证沿R26/R28复用：v1 `Sun, 31 May 2026 11:20:00 UTC`，同DOI `10.48550/arxiv.2606.01168`、arxiv.content查询限定/findable与registered `2026-06-02T04:08:58Z`；适用公告发号规则最早Jun02 00Z至登记最晚界全落Jun02 BJT，不重复GET日证、不把submitted/registered叫实际公开时刻。

实际读§3.1–3.4/Eq1–10、§4.1–4.3/Tables1–3及Broader/ablation正文、§6限制，未看图像像素、未核代码/全附件或复现。D2为题目级step-range与step内压缩监督两层接口，Reach1限适配数据/生成器训练组件而非推理服务全栈，Durability2为预算标签、代理监督与部署控制的分责，总5。按标准必要层已核问题/机制/对照/反侧，具体拟入书差额及未闭训练链定点深入，不借成熟LoRA/Fisher名字或平均token节省加分。

### 机制与不采用的扩大解释

Stage1让Qwen-Max为每题生成不同step数候选，对照gold最终答案过滤、取**已采候选中**最少step作为标签，非证明最少必要步骤；无成功候选的题目被排除。平均每step字数约束只减少表面格式影响，不证明step对应逻辑原子。MATH桶1–2/3–4/5+，GSM1/2/3+；LoRA router CE学习三桶，部署将预测桶映为prompt的step-range指令。范围提示不是runtime硬配额或答案验证器。作者明确Qwen-Max CoT仅供category标签、不直接作下游trace；不能写成教师链原文蒸馏。Stage2训练trace具体producer/生成协议所读域未完整绑定，不自行补成Qwen-Max traces。

Stage2以训练数据准备时的step平均tokenNLL之exp作PPL proxy；对同题step pair做margin ranking，PPL越接近者权重越大（逆差加ε后sample内softmax），head分数再经learned affine+sigmoid给retention ratio。PPL依赖模型/prefix、罕见词和格式，不是intrinsic难度真值；小差pair的高权重也可能放大噪声，未限制affine斜率符号不自动保证难step保留更多。再把各step ratio统一减δ=.05、重算pruned-context NLL差，以有限扰动斜率调quality/efficiency权重；名称是Pareto probe，但不是证明真实frontier曲率或全局最优。

训练期用quality loss对token embedding梯度的平方范数作importance，按每step的floor(Lr)保top tokens；这是局部敏感度proxy，非经期望定义的完整Fisher、更不是token逻辑必要性证明。Eq6仍按原tokens求NLL而条件为pruned历史，实际删减/target对齐及floor/topk到allocator的梯度路径、detach或surrogate未完整给出；不发布可执行端到端训练recipe。支持的接口差异仅是训练期细粒度压缩引导，部署称由生成器参数internalize，**不在线运行PPL/Fisher剪枝器**；更短输出也不证明被删逻辑忠实保留。两阶段CE后pair+probe loss顺序不等已证明梯度冲突消失。

### 评价、反侧与总费用

双A80080GB；Qwen2.5-7B-Instruct/Llama3.1-8B-Instruct，attention q/k/v/o LoRA rank16/alpha32/dropout.1。Stage1五epoch/lr3e-5/batch4/accum2、weightedCE，Stage2三epoch/lr2e-5/λpair.03/λpareto.01/margin.5/δ.05；AdamW decay.01、gradclip1/maxseq512。所读域完整dtype/解码seed、温度、训练独立重复与不确定性、路由和全生成wallclock/并发/SLO未披露，不补为生产净加速。

数据先经teacher成功过滤再split：MATH500由500变233/77/78，GSM原抽2000变1007/434/462；不是标准原500或原GSMtest的全人口成绩，teacher无解的难题不在验收。MATH Qwen准确率79.49→82.05、平均tokens482.2→327.3只是78题条件人口，Llama46.15→51.28但TokenSkip48.72/282.2tokens比HAB424.8更短；GSM Llama83.16→87.23、244.5→232.2，但fixed-length Type2准确率89.18更高/290.8更长。Table3短固定桶也可用更少tokens牺牲部分质量，不采所有配置Pareto支配。Broader AIME又为15/5/12过滤split、LogiQA1172/381/331，不能headline外推独立标准AIME泛化。

主基线含zero-shot CoT、TokenSkip、CoD/SoT/Sketch、O1-Pruner，改变训练/提示/生成结构与准备预算；Table3只改固定depth桶，未分别隔离PPL pair、probe、Fisher、两阶段及普通等预算SFT，不能将质量差额唯一归因全部新组件。训练本身用teacher标签/gold过滤，不能说无额外监督；候选多次生成、gold校验/丢弃、router、PPL/成对O(N²)监督、probe额外前向、梯度importance及两阶段适配全计费。§6仅称额外训练开销modest未量化，不补为净省；线性CoT限制保留，遇proxy/质量或budget失配仍保固定范围、完整可信trace或普通适配。

### actual-owner与逐字PRE（未独核或授写）

唯一owner `TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md)。实际读条件接口/数值属性段、长trace监督mask/IG/AlphaToken完整组、XS-CoT删条件历史段及其前后，Ch28/30开篇职责。精确01168/题名无现family。已有XS-CoT讲删历史与loss-mask不同，IG/AlphaToken讲监督选位及proxy，不含题目级depth标签+训练期step retention的两级预算分责；只补这一自然段接XS-CoT后、trajectory repetition前，不给Ch20新增在线pruner，也不在Ch33复制PPL/Fisher目标。

上锚完整直接段：
> 减少学生可见的中间文本，是另一种demonstration schedule，而不是只少算几处loss。一个跨语言语音指令分支先以目标语言指令、核心语言指令、核心语言响应和目标语言响应作四段监督，再按epoch逐步压缩前面三类文本：按句保留前若干词组并标记省略，最后仍预测目标语言响应。它同时改变teacher-forced条件历史、监督长度和部署时生成的中间token；被删内容不再像loss mask中的token那样继续供后文读取，因此不能称为逻辑原样转入隐状态。[受限XS-CoT对照](https://arxiv.org/html/2504.20835v1#S3)中，压缩节省中间token却降低部分任务评分，原ASR、翻译和指令能力也须单独回归；合成语音与代理judge不认证自然流量或推理忠实。应绑定分段/删减schedule、阶段checkpoint、监督格式与生成预算，并计入翻译、语音制备、过滤、多阶段训练和质量验收成本；质量或协议失配时，保留完整可信轨迹、普通目标语言demonstrations与原checkpoint，不由token更少签发墙钟或能力保持。<!-- source-family:SF-2025-ARXIV-2504-20835 -->

拟融合单段：
> 预算监督还可分成题目与步骤两级：先从教师已采且最终答对的候选中取最短step数，分桶训练router，在部署prompt中给step-range；再在训练期以step-PPL相对排序、收紧retention后的局部NLL差及token embedding梯度敏感度提出step内压缩信号。[HAB的受限接口](https://arxiv.org/html/2606.01168v1#S3)不把这些代理变成真实难度、最少必要步骤或Pareto最优，部署也不在线执行Fisher剪枝。教师无成功链的题目已被排除，过滤后小测试集的准确率与token数不能当原benchmark全人口或组件单因果；候选生成、校验、router、PPL/probe、梯度求值及全部适配均计费。Hard选择的反传/对齐未闭时不补完整训练recipe；代理、质量或总费失配时，保固定范围、完整可信trace与普通SFT，不由参数内化或更短输出批准逻辑保真和净加速。<!-- source-family:SF-2026-ARXIV-2606-01168 -->

下锚完整直接段：
> 一次看到更多不同样本通常提高 coverage，但长 reasoning demonstration 中真正决定策略的稀有转折可能只出现
> 一次，容易被大量常规 token 稀释。重复同一 verified trajectory 能增加它在经验风险中的权重，却不会创造新证据：

**有界停止：** 01168单篇必要Source/5分与actualowner最小提案已保存，仍待reader首次必要/逐字PRE，不预PASS、Books写入、I或DAY；下一01155未本轮notice/Methods/评分/owner。四定义/negative/CRAM/ProtoAda沿root独立新层，不扩本作者任务。未动共享Books/Report/State/index，未stage/commit/push，年度153/279不变，ready即释放本阶段。

## 01155 When Data Is Scarce — 必要原证与具体已有覆盖提案 / 2+2+2=6

2026-10-25同一Jun03阶段恢复：root通知01168 R74/77真实Ch29保存/唯一POST已生效，不第三；R75已校准CRAM/ProtoAda准入/date及01693/00486范围N，四定义root新层不再挂未校准，不扩本项。已重读AGENTS、当前研究/Report合同、Sources适用说明/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State与本日停点，owner前读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE及实际相邻。只Jun03补Jun02 BJT，年度153/279不变。

[exact-v1](https://arxiv.org/html/2606.01155v1) / [保存HTML](SUP_MODEL_B6_2606.01155v1_20261025.html)。本轮2026-10-25实际打开[当前官方abs](https://arxiv.org/abs/2606.01155)，唯一v1、comments Accepted ICML2026，所见无withdrawn/removed/erratum，不从发表标签推贡献或保证全网无纠错。R26/R28完整AB及联合日证有效复用：v1 `Sun, 31 May 2026 10:51:18 UTC`，精确DOI `10.48550/arxiv.2606.01155` 的arxiv.content查询限定/findable/registered `2026-06-02T04:08:40Z`，适用公告/发号规则最早Jun02 00Z至登记最晚界全落Jun02 BJT；不把提交/登记单独叫公开、不重复GET日证。

本次定点读§3.1–3.3/Eq3–13、§4两种resource frontier、§5/Eq14–16及Appendix F直接限制；不遍历全部拟合附件、剪枝实现、代码或复现。D2为unique data受限时稀疏度与重复饱和共同改变资源最优选择；Reach2为数据可用量、模型active/总容量与compute计费边界联合，而非单参数大小扫描；Durability2为可复用的局部拟合/预算分责，总6。分数与本次NC独立，不因Books覆盖降分；已有同family正文不计第二次Books产出，**不据旧trace认定已审duplicate或排出本日候选**。root具名定点查06-02 README未命中01155/该alias，只有Ch28旧trace记旧Daily；报告候选去重/保留由root负责，本作者不改其他日归属。

### 必要机制、评价及反侧

LLaMA2类C4预训练，unique tokens520M/1.3B/2.6B、重复1/2/4/8/16epochs，总处理至41.6B；active N15M–960M、稀疏S0/.5/.75/.875/.9375，dense-equivalent N/(1−S)拟合范围至1.92B、留出外推至7.68B。500训练runs是partial grid，大active模型最高稀疏项未全覆盖；不能当全组合全尺度验证。batch512/Adam/bf16/μP学习率/前1%token warmup；固定稀疏率但magnitude prune+random regrow刷新mask，不是MoE routedexperts也不是训后一次剪枝。本轮不核DST全recipe。

Eq9的参数项以((1−S)^ε+PS^μ)/N′^α描述稀疏容量取舍；有效data/parameter项对重复暴露用饱和指数，R*d(S)、R*n(S)各有S的一次/二次经验修正。核心是重复token不按fresh等价线性增加，中等稀疏可在所测域延迟饱和，但极高稀疏收益变小/可退步。它是L-BFGS拟合的phenomenological law，不是机制定理；fitted/validation R² .982/.914不证明未知数据/规模唯一模型或无过拟合。本文没有给frontier通用系数；代码/多语语料、optimizer/schedule与mask过程换了须重校准。

资源问题有不同条件：固定unique数据/iso-loss可比较增N与增epochs；iso-FLOPs另分理想sparse C=6ND与dense-equivalent计算，稀疏active少不证明硬件真省。§5的loss-optimal在不约束总compute下联合找最低拟合loss；compute-optimal则以达到dense最优拟合loss的最少compute为目标，非同一“最优稀疏度”。其约.45–.5和.6–.75以及13B/130B unique数据的最优点包含超出实际2.6B数据域的拟合外推，不采用固定50%或8×净提速配方；验证loss也不代下游能力、隐私或安全。作者F明确C4/非frontier范围、硬件稀疏低于理想收益、理论解释尚缺；kernel/完整GPU配置/墙钟及服务SLO并非本采用命题已证，未补造。

这里的最小长期命题是同一data-saturation boundary内联合冻结unique volume、repetition、active/容量与sparsity，再对不同预算问题看边际收益；全部训练sweep、mask刷新、拟合/选点和真正稀疏执行均计费。数据充足、低重复或稀疏执行路径不合时，普通dense/单遍语料仍是有效旧分支；不把“重复更有效”说成更多epochs一定更好。

### actual-owner：同family具体已有覆盖，不造新PRE

唯一owner `TRAIN-PRETRAINING` / [Ch28“数据受限的 Scaling 必须把 Unique Data 与 Repetition 分账”](../../../../../books/part-04-training-system/28-pretraining.md)。实际读该节完整两段及前方压缩/对齐末段、后方loss与能力交接；Ch27/29开篇职责已读。不是仅关键词相似：正文在semantic-body-binding `SF-SPARSE-REPEATED-TRAINING`下逐项承载本次最小长期命题；末注同family明确primary `arXiv:2606.01155v1`，既有旧Daily标识只作精确去重，不沿该标识第三研究或搬归属。

现有完整第一段：
> 经典 compute-optimal 分配隐含一个近似前提：新增训练 tokens 仍带来足够的新信息。语料受限后，同一批 unique tokens 会被重复消费；此时把训练 token 总量继续当作独立数据，会把记忆化收益、数据饱和与模型容量混成一个轴。更完整的实验身份应同时冻结 unique-token volume、repetition count、effective parameters、sparsity、数据质量和 optimizer/schedule，再比较同一预算下增加模型、增加重复轮次或改变稀疏度的边际收益。

现有完整第二段：
> 这条分支把“稀疏模型能容纳更多参数”与“重复数据还能提供多少新信号”放进同一 data-saturation boundary。它能避免直接套用 dense Chinchilla 分配或把理论 FLOPs 节省解释成真实硬件收益，却增加 scaling-law 拟合、语料多样性估计和跨配置 sweep 成本。拟合范围之外、token 质量改变、optimizer 或稀疏 kernel 改变时，原最优点必须重新校准；unique data 充足、重复率低或稀疏执行没有硬件支持时，普通 dense scaling 与单次语料遍历仍是更清楚的基线。现有 exact-v1 证据只覆盖论文披露的模型尺度、语料、稀疏过程和 compute regime，不证明 frontier-scale mixture 或生产硬件效率。

对应差额比较：第一段已区分unique/处理token并要求active/sparsity/优化器身份与联合预算扫描；第二段已给共同饱和边界、sparse-vs-hardware成本、不确定外推/重校准与dense回退。它们没有照搬50%或13/130B外推数，正符合本次不采用的精确配方边界。§5两种优化目标细分可存Source，既有正文已以预算条件与边际比较约束“最优”，不必为附一个经验最优点再造平行知识段。Ch7拥有通用scaling视角、Ch21拥有MoE组件，但此处不迁owner、不另写稀疏重复定律。

**本次Books提案：具体已有覆盖（待reader独核），无新增段/PRE/写入请求。** 不把NC签成新整合，也不把原family旧日期标签当新的公开证明；本日候选/事件去重由root按有效原记录处理。无需重读同family旧方法或为diff挖其余附件。

**有界交接：** 01155单篇必要证据/6分与actualowner同family NC包已保存即交；下一01062未本轮notice/Methods/评分/owner，仍普通待办。无共享Books/Report/State/index写入、无stage/commit/push、不预Source/Books独核通过或I/DAY；本阶段ready即释放槽。

## 01062 DAG-MoE — 必要原证与actual-owner最小提案 / 2+1+2=5

2026-10-25同一Jun03恢复：01155 R78六分/actual Ch28具体NC已经有效且root已融Report/State，不第三。本轮完整重读AGENTS、当前Research/Report合同、Sources使用说明/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State与本日精确停点；owner前读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、Ch21具体上下文及Ch20/22开篇交接。仅Jun03补Jun02 BJT，R26/R28完整AB准入与联合日证有效复用，不重复GET/证明日期，不将submitted或registered单字段叫公开。本项之外余42仍普通必要待办，不预DAY/年度推进。

[exact-v1](https://arxiv.org/html/2606.01062v1) / [保存HTML](SUP_MODEL_B6_2606.01062v1_20261025.html)。本轮实际打开[当前官方abs](https://arxiv.org/abs/2606.01062)，唯一v1、comments Accepted ICML2026，所见无withdrawn/removed/erratum；发表标签不加分，不保证全网无纠错。实际必要读§3.1–3.4/Eqs3–12、§4.1–4.4/Tables1–5、§6及直接配置B.1/Tables6–7；未读全部理论证明/DP worked example、可视化像素、全部微调附件、代码或复现。拟采用的是可实现的输出组合与成本边界，不采用所有DAG注入编码/严格表达力定理为已验收结论，故不为理论主张另遍历证明。

Design Delta2：选定相同数量/配置experts后，以跨深度的成对非线性消息组合代替一次weighted sum，是独立于继续细化expert/router的替代机制；System Reach1：拟采用命题属于单MoE block输出组合，局部吞吐反侧不将其变成跨runtime生产结论；Durability2：选择、组合深度、实际执行费用分责可复用，总5。分数由实际增量给出，不因规模小、已存在MoE章或审阅成本降分。现有aggregation正文承载选集/权重分责，但没有本次跨输出结构迭代机制，故对这一具体缺口补必要深入，仍不机械全篇deep。

### 必要支持与直接关键反侧

§3.1–3.2先把专家输出和router score固定为讨论对象：标准weighted sum对这些带权输出的排列不变，改变AGG的中间连接才引入另一组合轴。这不是说随意换expert ID会保持原输出，更不是训练时冻结原experts/router权重。实际§3.4先按原Top-K得到每个expert输出，只执行这些expert一次；初始化节点为`g_i E_i(x)+x/K`，每轮LayerNorm、降维，将当前节点i与前一深度节点j拼接，分别学习向量edge gate和message、相乘后求和，上投影并加节点residual，最后求和全部末层节点。每深度固定K节点，只连接上一深度；向量gate没有另行离散剪边规则，不能把学习到小gate登记成省略pairwise计算或额外稀疏dispatch。`x/K`使最终残差总贡献归一、zero-init up projection用于稳定，不应把末端求和误读为没有非线性结构组合。

§3.3理论明确以足够强的injective AGG为假设；DP存在性还要求给定问题计算图、足够迭代深度与随输入条件增长的attention heads。正文Remarks与§6明确：实际受限图类的语言训练不保证学到某个DP图，最优结构学习仍未解，不能由多轮消息传递称“已证真实多步推理”或常数深度解决任意DP。§3.4先说迭代共享同一module，而Eqs8–11及§4.2参数计数按L增长；本采用不照搬权重共享配方，只保留实际重复顺序计算/需绑定训练产物与L的边界。

§4.1/B.1为Llama3.1式缩小模型，从头训练：s/m/l分别4/6/8层，hidden512/512/1024；s有32expert/Top4或64/Top8，m/l用32/Top4；标准baseline保持相同expert/router配置和训练配方，以新增shared expert匹配参数。实际router score用Sigmoid（B.1），不能套成已核Softmax实现。Pile约12B(s/m)/40B(l)、seq2048、global batch256/256/512、AdamW+WSD、balance0.01/Z-loss0.001；DeepSpeed ZeRO-2/8×NVIDIA A100。GPU显存型号、precision、EP/TP、完整训练时间及服务输入输出/concurrency/SLO未披露于必要域；不补造，服务指标不属于本文实证。

直接对照在§4.3：Table2相同新增393K参数下ΔPPL为shared0.433、CoE0.480、DAG0.587；Table3 naive concat-MLP mixing的eval loss2.8406/2.8006反差于baseline2.7168，而DAG37K/74K为2.6948/2.6899。这支持有限配方下结构偏置不等于随便加MLP，不证明唯一最优结构或消除训练混杂。Table4 s/Top4/12B、上述同hardware/loading，baseline0.7744M tok/s，L1为0.7627(0.985×)、L2为0.7404(0.956×)，参数/FLOPs接近；作者给1.51%/4.49% overhead，表舍入与百分比不当高精度换算，采用只说吞吐下降。L、成对K²消息与projection/activation、训练和原dispatch均计费，不由相近FLOPs称免费。699M/40B的Table1 PPL改善也不代真实推理效率；Table5同三epoch SFT后HellaSwag25.90→25.73、MMLU24.17→24.03实际反退，正文“六/七”表述与表中两项下降不能照抄，未披露方差不称显著。§6明确尚不能外推billion-parameter/trillion-token规模。

### actual owner与逐字最小PRE提案（待独核，未授写）

唯一owner `MODEL-MOE` / [Ch21](../../../../../books/part-02-model/21-moe.md)。实际读开篇/Top2输出、active/total与capacity/All-to-All、粒度扩展/atomic units、支持集与贡献/Dispatch–Aggregation小节及其完整检索router交接；Ch20是轨迹选择、Ch22是序列容量，均不迁owner。当前没有01062/DAG-MoE或同family marker；现有`expert-dispatch-vs-aggregation-ownership`三段具体讲保留expert IDs后另学组合权重，而不是多个expert输出间成对非线性迭代；atomic机制改变expert粒度/调度，当前内容并未承载此缺口。只补一段承接既有aggregation分责，不另造小节或复制通用MoE解释。

完整直接上锚（保留原段及其独立family注，新增紧接注后）：
> 拆分增加一个 head 和校准状态，也可能在小模型上得不偿失；传统 router 在路由稳定、实现简单优先时仍合理。该结论来自有限模型，不应外推成所有 MoE 必须解耦，但系统监控和负载均衡不能把 aggregation weight 误当 dispatch identity。
>
> <!-- source-family: arxiv:2608.08853v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: expert-dispatch-vs-aggregation-ownership -->

拟新增完整单段：
> 组合还可以改变被选输出之间的计算结构，而不继续增加 expert 数量或改 Top-K 规则：把各带权 expert 输出与按 K 均分的输入残差作为初始节点，在降维空间中以成对特征学习向量门与消息，逐深度聚合并残差更新，最后求和。这不是重新顺序执行 experts；新增的是输出间的非线性组合和顺序深度，实际模块固定每深度 K 节点且只连前一深度，也没有由小门值自动跳过计算。[有限参数匹配对照](https://arxiv.org/html/2606.01062v1#S4.SS3)区分了它与新增 shared expert、简单拼接 MLP，但理论 DP 构造要求给定图与足够深度，不认证语言训练学到了推理算法；expert/router 配置相同也不表示训练权重被冻结。成对消息、投影、训练与原 dispatch 都计费，近似相同 FLOPs 下增加迭代仍降低训练吞吐，部分下游任务也反退。组合深度、质量或净执行费不合时，原加权求和、较浅组合与原 dense/shared 路径继续合理，不把更多组合空间称为免费推理或规模外保证。<!-- source-family:SF-2026-ARXIV-2606-01062 -->

完整直接下锚（原样保留）：
> ### 从参数化 Router 到带检索记忆的 Router
>
> 训练得到的 parametric router 是最稳妥的起点：它没有外部索引，前向路径短，模型版本一旦冻结，
> 路由语义也随之冻结。在训练分布稳定、在线延迟严格或缺少可信参考样本时，这种设计仍然最合理。
> 它的边界是，遇到 distribution shift 时只能依靠参数中已经学到的决策面，不能直接复用“相似 token
> 曾经怎样路由更好”的局部经验。

拟本人Review note仅在root新授写时采用：`SF-2026-ARXIV-2606-01062` — Daily2026-06-03补Jun02，exact-v1 §3–4/6及B.1直接配置，2+1+2=5。只采选后成对结构组合/深度与费用分责，保受限图/向量gate非稀疏执行、DP非实训保证、共享配方歧义与任务/吞吐反退，不采严格表达力证明、最优图/规模外或生产收益；未看图像素/核代码/复现。当前仅必要Source/actualowner/逐字PRE待reader首次独核，未授写或签POST。

**有界停止与交接：** 01062单篇必要包/5分/actualowner最小PRE已保存即交root与唯一reader；只本文件和必要HTML原件变更，无共享Books/Report/State/index写入，不预Source/PRE/Books PASS、I或DAY，不stage/commit/push。下一01007尚未本轮notice/Methods/评分/owner；余42仍普通，ready即结束本阶段释放槽。

## 01007 Task-Aware Grouping — 必要原证与actual-owner最小PRE / 2+2+2=6

2026-10-25同日恢复：01062已R84必要/PRE、root真实Ch21保存与R87唯一actualPOST成I，行政由root融Report/State，本作者不第三。已重读AGENTS、当前Research/Report合同、Sources使用/Daily/arXiv/恢复、统一Prompt、ROADMAP、本2026 State与本日停点；owner前重读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、Ch21实际placement完整上下文及Ch20/22、Ch52职责交接。只Jun03补Jun02 BJT，R26/R28有效完整题摘准入/联合日证复用，不重证日期，不将submitted/registered单独称公开。

[exact-v1](https://arxiv.org/html/2606.01007v1) / [保存HTML](SUP_MODEL_B6_2606.01007v1_20261025.html)。本轮实际开[当前官方abs](https://arxiv.org/abs/2606.01007)，所见唯一v1，无withdrawn/removed/erratum；不保证所有渠道无纠错。必要实际读§3/Eqs1–15、§4.1–4.5/Tables1–2、§5、A校准预算、D直接配置、H指标；未遍历所有超参/数据集/证明/Checklist或图像像素，未核代码/复现。拟采用图重权与负载取舍，不采用完整在线副本调度实现或精确性能配方。

D2：在既有共激活placement中保留task条件并软重权边，是具体部署机制替代，不是仅换任务跑指标；Reach2：把模型routing traces/task人口转换为固定设备placement，并分开部署与运行负载；Durability2：任务混合、共激活与物理局部性的条件关系可复用，总6。规模、已有章和审阅成本不参与降分。当前实际owner缺这条task-conditioned graph边界，必要域针对该缺口深入，不扩完整附录。

### 核心支持、比较与关键反侧

§3.2固定4个已知task family（code/query/math/complex_reasoning）、16个EP serving units，按family预留不交叠设备组，但不把expert硬归某family。§3.3统计每层各family的expert dispatch frequency与同token pair coactivation，以相对其他family的优势作逐层z-score，softmax成expert的family preference P。`P Pᵀ`只是软偏好一致性kernel，不是专家语义或task真值；`Atilde=(1−α) Ahat+α (P Pᵀ⊙Ahat)`只重权原共激活边，不引入未观察到的新边。α=.25且kernel≤1，因此这里是相对保留/衰减，原文“amplifies”不应抄成相对原A的绝对增大。谱聚类后以overflow greedy repair满足primary专家数容量；这是离线启发式，不采用其最优/严格泛化或单凭monotone bounded objective便保证精确容量终止的主张。

§3.4 GESR另以centrality、跨family coactivation consistency和specificity penalty选少量generic experts，保primary并在兼容secondary设备放副本，router选择expert的语义不改。近期dispatch load guard筛candidate，空可行集退回全candidate set，故不是硬无超载保证。正文说明locality/load-aware choice，但Eqs13–15只闭合guard与负载更新，没有完整最终候选排序细则；本次不补猜已核实现。Primary exact-size expert容量已饱和时，副本仍要额外真实memory；§5声称hard per-GPU memory bound，必要方法未给副本budget扣账/完整resident-layout验收，不由“少量”认证全副本满足同一预算。这是完整部署资格未闭合，不影响采用图重权的有限机制；不授已实现全runtime/硬内存或最优调度保证。

§4/D三模型DeepSeek-MoE-16B、Qwen1.5-MoE-A2.7B、Moonlight-16B-A3B；16 GPU目标、每family4卡，64专家模型每卡4primary，Qwen60专家每family组{4,4,4,3}。校准与evaluation streams分离；代码mbpp/humaneval/apps-intro、query sql/spider、math gsm8k/numina、reasoning bbh/legal。A预算扫描仅DeepSeek、每family少量样本/约9–2k tokens，不能由几百token的局部plateau推出所有任务trace稳定。GPU具体型号/互联、precision、batch/concurrency、输入/输出长度、墙钟、TTFT/TPOT/SLO与完整trace实现未在必要域披露（Not Disclosed），不填补为实机端到端测试。

H的Comm是所定义跨卡dispatch/hop代理，不是bytes、链路占用或latency；Jain和MaxVio均基于GPU dispatch计数而非服务时间。其“每个跨卡layer记一个hop”的字面描述与Table1大于模型层数的Comm数值缺具体分母/累计口径，本次不照录绝对Comm作为可复算计数。Table2相同协议平均值：完整Comm.Red31.39%、Jain.9975、MaxVio.0736；无task preference为21.41%/.9537/.2416；无GESR为24.23%/.9825/.2763；去guard通信减幅更大35.87%但MaxVio恶化.1422。采用有限协议下通信代理与派发负载不能单目标优化的反证，不称实际网络省31.39%或普遍Pareto最优。§4.3固定部署扫13混合/phase/burst流量只支持已测task比例变化，不是未知task或跨域安全。§5仍是静态offline placement，快速漂移/在线重分组、memory co-design及专用expert泛化未解；校准、图统计/谱分解、repair、权重搬迁/副本驻留、一致性、load跟踪和选择均有成本。

### actual owner与逐字最小PRE（未授写，待唯一reader）

唯一 `MODEL-MOE` / [Ch21“Router选择Expert，Placement决定这次选择能否低成本执行”](../../../../../books/part-02-model/21-moe.md)。实际已有TAOT的demand/topology/replica plan、2512-23995的输入浓集×placement/模拟与延迟分责、2602-21626跨层affinity anchor/近期load以及2507-06567同token组合缓存；它们不等于按task-family soft preference重权同层共激活边。当前01007/TACG/GESR无命中。只补下列一段，不迁Ch52控制面owner、不重复既有epoch/安全段或硬造完整调度知识链。

完整直接上锚：
> 这增加输入分布扫描与 placement 重验成本，也不能穷尽恶意输入。受测 router 模拟、本地 MoE kernel 和远程 API 的 TTFT 是三种不同证据：远程延迟还受网络、缓存及 provider 路径影响，不足识别隐藏模型是否为 MoE 或采用多少 EP 设备。更分散的 placement、在线负载重平衡或异常输入筛查都需另验质量、误拒与响应窗口，不从模拟覆盖率签发防御保证；低风险稳定流量仍可采用原均衡与固定布局，出现分布漂移再重开受影响 epoch。

拟新增完整单段：
> 多任务流量还会让全局平均的共激活图隐藏条件结构：可先按已知 task family 分别统计 expert 使用与同 token 共激活，用相对其他 family 的优势得到软偏好，再按两端偏好的一致程度重权原有共激活边，离线分组并修复 primary 容量。这不是给专家授语义身份、硬分任务，也不改变 router 选择；没有共激活证据的边不能仅因标签相近就新造。共享热点的少量副本与近期负载 guard 是另一项运行取舍：[有限对照](https://arxiv.org/html/2606.01007v1#S4.SS4)中去掉 guard 虽使通信代理更低，却加重最热设备的派发负载。校准人口、task 划分、图与 placement epoch 应绑定，统计/规划、搬迁、副本驻留和选择都付费；primary 专家数容量不自动覆盖额外副本内存，guard 无可行候选时回全候选也不保证无超载。Hop 代理与派发 Jain 不等实测带宽、排队或端到端时延；新任务、漂移或完整费用不合时，保留原布局、全局共激活规划与经核的负载均衡，不由已测任务比例变化批准普遍鲁棒部署。<!-- source-family:SF-2026-ARXIV-2606-01007 -->

完整直接下锚：
> Placement 还可分开跨层 transition affinity 与每层近期 activation load：先将筛选后的少量 affinity-linked experts 固定到人工指定 anchor GPU，再把其他 experts 按新负载 greedy 分布，并按 epoch 刷新。它优先降低跨层搬运，却可能增加 anchor 局部 imbalance；容量不足时必须收紧 threshold/top-E、裁 affinity pool，不是所有关联都可同时驻留，也不是昂贵 MILP 已获在线最优。随机输入 profile 不认证真实流量依赖，计数可陈旧，迁移、参数 identity 与生效 epoch 仍由 runtime controller 负责。有限实现的 baseline 与实现版本不同，主性能关闭 prefix cache，不能与另一人口的缓存 hit 提升合并为质量/SLO 保证。Profile、调参与搬迁付费，稳定负载或容量冲突时保留固定 placement、普通 EPLB 与原 dispatch。<!-- source-family:SF-2026-ARXIV-2602-21626 -->

拟本人Review note仅待新授：`SF-2026-ARXIV-2606-01007` — Daily2026-06-03补Jun02，exact-v1 §3–5/A/D/H必要，2+2+2=6；仅task条件共激活重权→primary placement与负载取舍。保软偏好非语义、原边不新增、启发式非最优、副本容量未闭/guard非硬保证、指标分母/代理与完整费用；不采完整调度实现、硬memory/净速或未知task鲁棒性，未看像素/核代码/复现。当前必要Source/actualowner/PRE待独核，未写Books或签POST。

**有界停点：** 01007必要包/6分/actualowner最小单段与完整直接两锚已保存，ready即交root及唯一reader并释放本阶段；下一00997未展开，余41仍普通必要待办。只新必要原件及本节，不写共享Books/Report/State/index，不stage/commit/push，不预Source/PRE通过、I或DAY。

## 00997 Chain-Rule Deviation — 必要证据与actual-owner最小PRE / 3+1+2=6

2026-10-25同一Jun03恢复：按root通知01007 R92/94与00435 R95/96真实整合生效，Report80/70行政由root负责，不第三。启动已完整重读AGENTS、当前Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State与本日精确停点；State尚在前一行政快照不推翻后到有效层。R26/R28完整AB/Jun02联合日证有效复用，不再逐篇GET日期，不用submitted或registered单字段充公开。只本日，未变PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE复用本作者前轮实际完整阅读；actual Ch24及Ch23/25职责/直接邻接本轮实际读。

[exact-v1](https://arxiv.org/html/2606.00997v1) / [保存HTML](SUP_MODEL_B6_2606.00997v1_20261025.html)。本轮实际打开[当前官方abs](https://arxiv.org/abs/2606.00997)，唯一v1，所见无withdrawn/removed/erratum，不保证所有渠道无纠错。必要实际读§3/Eqs1–2/Thm3.1条件与Jensen sketch、§4.1–4.4/Tables1–4、§6、B协议及B.1直接content统计/相关；未读全理论证明/全部robustness附件、图像像素、代码或复现。采用目标固定时的条件相容性诊断和均值/方差联合报告，不采用完整均匀定理作为实际LM可靠性定律，故不扩全证明。

D3：修正“固定目标的路径似然可按同一joint内容难度解释”这一具体比较结论，原条件缺相容性时路径自身改变读数；Reach1：同一checkpoint的块内单位置解码/诊断，不把可联想的serving链加分；Durability2：目标概率与自产token confidence、路径条件和诊断/验证分责可复用，总6。不是为已有章/附件工作量降分；针对实际长期测量缺口深入以下必要域，不机械整篇deep。

### 必要支持与直接反侧

§3.1固定prompt和目标x*，若各条件来自同一coherent joint，则沿任意合法揭示顺序的target-probability乘积由链式法则相同；一个训练network能接受不同mask不自动满足这一跨条件相容性。§4.1–4.2单一LLaDA-2.1-mini、block32、每forward仅揭示一token，块间严格L2R：C4 validation固定1000例、prefix32+target128（四块），比较Forced-AR、Reverse、Random与三种依赖已知target的oracle排序。固定目标的平均log probability约−3.00至−3.49nats/token，支持所测learned conditionals不是顺序无关joint的精确因式分解；不是证明所有OALM必然不相容，也不是全局任意位置置换。Forced-AR仍允许模型读同块MASK，不等真正causal AR。

§3.2 uniform optimum只在固定乘积、greedy-success可按单步函数分解、log f(exp y)严格凹等假设下由Jensen得出。它不把实际greedy成功变成q的普遍函数：竞争token残余分配与跨步依赖仍重要，真实路径总乘积本就可变。即使满足该条件，均匀profile是极值也不自动将所有非均匀profile按一个Var标量完全排序；因此不采用“同mean较低Var必更可靠”的充分条件、theorem已证task accuracy或可实现最优在线排序。无需以未经采用的强理论供给本项分数。

§4.3生成时每策略产出自己的continuation，q改成自产argmax token概率，不再是固定target q；EOS须分账。C4 Max-prob/Top-margin对比Forced-AR低Var但EOS更多，内容order近L2R只指block0且排除EOS后的Spearman89.1%/80.7%，不是任意样本已等价AR；模型为何偏L2R的mutual-information归因没有独立因果干预，不采为定律。Table1 Max-prob Var.286低于Forced.392，Distinct3却.907低于.928；低Var不认证多样性。

§4.4/B同checkpoint、greedy一token一步、block-causal KV driver、max16384/EOS早停/无correction，各策略同prompts。HellaSwag10042例为greedy CoT后按候选normalized logprob选项；CMath1098 numeric extraction；MMLU-Pro12032 regex答案；IFEval541规则评分。Table2 Forced-AR在前三任务准确率高于更低content Var的CF，例如CMath91.71 vs Max-prob90.26，MMLU54.78 vs53.12；因此不能由随机路径差而授CF普遍更好。逐cell Table3 correct的平均Var低于incorrect，但IFEval相关弱，Forced与Random的单侧MW p=.068/.059不达.05；不称全部显著或控制了长度/难度因果。Table4“matched mean lowVar never worse”正文有明确反例：IFEval低mean桶lowVar64.7低于highVar67.3；且median桶不是精确mean配对。保表格反侧，不照抄文字。Prompt级min-V selector必须先生成并记录多条策略轨迹，其增益不是单条线上policy或免费best-of。本文§6自己定位diagnostic非新deployable算法、单模型scale、parallel批量commit待后续；GPU/precision、batch/concurrency、完整墙钟/SLO未在必要域披露（Not Disclosed），不从步骤数补造速度。日志、词表概率/位置选择、所有候选轨迹和外部评分均付费。

### actual owner与逐字PRE（未授写，待reader首次核）

唯一 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24“生成范式差异要拆成Objective与Commit Policy”](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际比较现Objective/commit、训练bound/生成测量段，以及early convergence/high-confidence、同条件joint marginals前提段：现文有不由confidence认证正确和proxy/质量分责，但没有固定同一target、跨揭示顺序的learned conditional乘积相容性检查，也未区分target与自产token q的统计。TUBE拥有latent路径密度bound，并不替此条件一致性诊断；不另写通用Jensen/variance章，Ch20自回归选择也不接管masked条件合同。Ch23表示、Ch25环境转移交接实际读。

完整直接上锚：
> 这些观察只覆盖所测语言模型和 evaluator，不证明某种范式普遍更有创造力或更可靠。无法隔离变量时，应回退端到端质量、延迟和 exactness 合同，不从文本风格反推内部机制。

拟新增完整单段：
> 同一 masked 模型允许不同揭示顺序，也不保证其学得条件来自同一个相容联合分布。可先冻结 prompt 与目标，改变块内单位置揭示顺序，检查目标 token 条件概率乘积是否一致；若不一致，路径似然便混入顺序效应，不能只解释成内容难度。自由生成时则要另记自产 token 的 confidence，并将 EOS 与内容分开，同时报告 log-confidence 的均值与方差。[受限单 checkpoint 对照](https://arxiv.org/html/2606.00997v1#S4.SS4)支持这种诊断，但固定乘积与成功率函数等假设下的均匀极值，不认证实际任务正确，也不能让一个方差标量给所有路径排序；较低方差仍可伴较低准确率。先跑多条轨迹再选 min-Var 也须支付全部生成与日志费用，不是免费在线策略。模型、block、目标/自产概率口径或预算变化时重校准，保留原已验收顺序、完整质量评价与独立答案检查，不以低方差批准并行提交、精确分布保持或可靠性。<!-- source-family:SF-2026-ARXIV-2606-00997 -->

完整直接下锚：
> 跨范式比较还要把训练 bound 与生成测量分开：mask 与 uniform corruption 的 variational bound 松紧不同，较低 NELBO 或其 perplexity 不自动给实际输出质量排序。一个可复核的接口是在明确训练预算、数据和模型规模/结构的比较口径后，扫描各自 sampler 的步数，再绑定同一外部 scorer、输出长度、数值精度/entropy 与真实吞吐预算，比较各自达到质量目标的可行点。[受限 dLLM 对照](https://arxiv.org/html/2602.15014v1)使用 Llama2-7B GenPPL 和单 H100 80GB 上各模型可容纳的最大 power-of-two batch 拟合跨规模 Pareto；这是该 scorer、无条件生成和适配 batch 下的选择，不是一般质量定律或公平生产 SLO。另一个数学评价让所有 family 单 token 从左到右、batch 1 生成，因而不证明并行 diffusion 的数学吞吐优势。扫描、调参及外部评分都有成本，低 GenPPL 也不认证任务正确性；目标、评估器或预算变化时重测 frontier，条件无法对齐时保留已验收 sampler/AR，而不从一个训练 bound 或 step 数宣布范式胜负。<!-- source-family:SF-2026-ARXIV-2602-15014 -->

拟本人Review note仅待新授：`SF-2026-ARXIV-2606-00997` — Daily2026-06-03补Jun02，exact-v1 §3–4/6/B直接协议/统计，3+1+2=6；仅固定target的路径条件相容性与mean/Var诊断口径。保单checkpoint/block32/一token一步、target与自产q分责、uniform假设非任务证书、IFEval桶反例/弱相关及全候选费用；不采普遍低Var最优/在线policy/净速，未核像素/代码/复现。必要Source/actualowner/PRE待首次独核，未写Books或自签POST。

**有界停点：** 00997单篇必要Source/6分/actualowner最小单段与直接完整两锚已保存即交root与唯一reader，未预PASS/I/DAY；下一00946尚未展开，余40普通必要待办。仅本节与必要HTML，不写共享Books/Report/State/index，不stage/commit/push，ready释放阶段。

## 00946 Lodestar — 必要原证与actual-owner最小PRE / 2+2+2=6

2026-10-25同Jun03恢复：00997 R97必要/6分/原单PRE已通过，root负责真存与唯一POST，本作者不第三或预写后通过。启动已完整重读AGENTS、Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State及本日停点。R26/R28有效完整AB准入/Jun02联合日证复用，不重复GET/论证日期、不把submitted或registered单独叫公开；未变PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE沿前轮本人实际完整阅读复用。本轮实际owner Ch56及Ch55/57职责交接已读；保护dirty Books，不写共享。

[exact-v1](https://arxiv.org/html/2606.00946v1) / [保存HTML](SUP_MODEL_B6_2606.00946v1_20261025.html)。本轮实际开[当前官方abs](https://arxiv.org/abs/2606.00946)，所见唯一v1，无withdrawn/removed/erratum，不保证所有渠道无纠错。必要实际读§4.1–4.4、§5.1–5.6及Appendix B/Algorithms3–4；只支持拟用在线数据/路由/安全退路分责与直接评价反侧，不遍历所有baseline附件、全部性能图像素、代码或复现。

D2：用决策当时cluster snapshot与已选instance实测TTFT训练共享reward predictor，再以近期与多样回放两池持续更新，是cache/load路由的具体替代机制；Reach2：请求路由、engine状态/KV画像与异步训练接口，非多生命周期平台通则；Durability2：策略改变数据分布、即时奖励与长期cache成本分责可复用，总6。不由吸引人的TTFT倍率、框架名或大批量待办加分，不因已有延迟模型章降分；针对现正文窄gap深入必要域。

### 核心机制、直接比较与限制

§4 gateway在每request到达时保存cluster snapshot，请求与响应按request ID对齐；label是已选instance的负TTFT，不是所有未选instance的反事实实测。共享3×128 MLP读取input tokens、各候选expected prefix hit、running/waiting request数、inflight prefill/decode tokens、GPU memory utilization/GPU model类别，不读instance ID；类别GPU型号仍是特征，不能称完全硬件无关。按候选批成[N,d]做一次前向，主决策最大预测reward；B/Alg4还列ε-greedy探索，不能写成全程只有greedy或已证消除选择偏差。Prefix hit是gateway路由历史/radix估计，不是engine承诺实际命中；内部queue/memory背景100ms scrape，per-token负载gateway追踪，无锁snapshot不等全局一致/零陈旧。Policy改变cache分布与load、后续label又变，不能把固定旧policy收集的offline监督误当新policy性能证明。

§4.3每1000新sample异步重训；FIFO5000保近期，FIFO满后被挤出的样本经residual加权last-hidden activation的gradient-coreset准则择入5000 replay，训练两池并集、总存储10000封顶。不是完整历史，也不是随机旧数据无限留存；没有样本覆盖或校准/ regret保证。训练/推断异步与atomic pointer swap避免阻塞，但训练仍付费；request records每100条best-effort flush，drop可延后更新。独立routing service失败/慢不应拖gateway，gateway事先计算Prefix-cache-and-load-aware heuristic并限时RPC；冷启动、normalization统计失配、逐特征超训练buffer范围或timeout/error退回heuristic。Range guard只检查坐标边界，不能发现所有联合分布shift、cache错误或反馈拥塞；timeout也仍有等待预算，原“fallback adds no latency”只可解为不再重算选择，不写成请求无任何延迟。

§4.1明确即时greedy TTFT不优化长期全局cache：全群KV饱和且长prefix共享时，选择当前最佳可能驱逐未来有用KV。一个补充分支将prefix group consistent-hash至少量候选，再取预测最佳；正文80% saturation、K2仅作者配置。Alg4还多prefix-benefit阈值/探索/tiebreak，最后near-best条件以乘法施于负reward，不能不加核对写为完整可执行无歧义配方；本采用不依赖该精确tie规则或硬candidate隔离。优化TTFT不等TPOT/e2e/公平/可行性/SLO admission，endpoint仍需执行其容量合同。

§5.1/5.2主实验Llama3-8B/FP16、vLLM v1（具体release/commit未披露），chunked prefill+prefix cache；8×A30 24GB同构中1张给Routing Service、7 serving，异构7×A30+8×V100 32GB（V100禁prefix cache，不能把全部收益归硬件速度学习），另7×L20+8×A30对照。public-cloud K8S；A30 Xeon8336C/28cores/240GBhost，V100 Xeon8260/8cores/32GBhost。Mooncake conversation/toolagent/synthetic与自造10/30/50/70%及mixed sharing，input1k–10k、output正态mean100/std10，medium→saturation RPS；无披露可外推的并发/业务SLO、失败/质量资格。另prefill-only是P池路由，不证明完整PD端到端。

§5.3中途20krequests/第10k将sharing5%→50%，持续更新胜mid-frozen支持已测shift下适应；不证明5分钟对所有工况收敛。§5.5同一shift的两池对比new-only与all-history，分别报告mean/P99 TTFT更低（2.39×/2.50×与1.21×/1.11×），代价是高于纯FIFO的训练预算，all-history成本随轮次增长而两池封顶；没有独立重跑/seed置信区间，不授通用最优数据选择。§5.6 ToolAgent/RPS12去K-filter使mean1865→3209ms、P9910528→18686ms，直接支持即时预测≠长期cache最优的反侧。§5.4 10–80RPS routing mean约3ms/tail约4.5ms，其他TTFT实验证称包含routing overhead，但专用A30、采样/数据库/训练与运维仍是完整费用，不从critical-path低成本说总成本免费。泛化/未知负载或heuristic的安全与服务端最终准入均未由此证成。

### actual owner与逐字最小PRE（未授写）

唯一 `INFER-SCHEDULING` / [Ch56“全局Routing需要延迟模型”](../../../../../books/part-05-inference-system/56-inference-scheduling.md)。实际读routing/placement/autoscale分责、PB prefix×load、DLB两完整段及后低带宽交接；Ch55定义PD机制、Ch57拥有平台接口，不迁owner。现DLB已讲latency function、freshness、delay/shift和保守回退，不能再造一段泛泛“学延迟”。具体缺口是所选request决策快照/反馈的policy-dependent训练人口，以及有界FIFO+diversity replay和独立gateway预计算退路这组接口；现文没有00946/Lodestar同family。补一个窄段解释现延迟模型如何受控持续学习，不宣称DLB与Lodestar同实现/直接谱系。

完整直接上锚（新增在原独立marker之后）：
> 分布式 probing 消除集中控制面的响应瓶颈，但只能生成带 freshness 和 uncertainty 的 observation；它不能成为强一致库存，也不能替代 endpoint 的最终 admission。学到的 latency function 能吸收 model、hardware 和 request-shape 差异，却会引入 delayed feedback、探测开销、模型漂移和拥塞振荡；当反馈过期、network partition 或未知 workload 超出校准域时，应回退到保守容量阈值、本地队列或静态 cell affinity。`arXiv:2609.21079v1` 提供了 Google DLB 的两层 router、P2P probing、延迟模型、流式/离散 routing 分支与 22 个月部署案例；作者的 latency 降幅只属于披露的迁移和内部基础设施，不是通用 SLO 保证。
>
> <!-- source-family:SF-2026-ARXIV-2609-21079 -->

拟新增完整单段：
> 延迟预测器若持续从在线请求学习，训练人口也会被自己的路由改变：选择影响后续 prefix 驻留与负载，只有被选 endpoint 才产生这次实测 TTFT，未选项不是反事实真值。一条受限分支将决策时请求/实例快照与观测负 TTFT 对齐，用固定大小的近期 FIFO 加按残差与表示多样性保留的 replay 联合更新共享预测器，再异步替换推断版本；这避免只留近期而遗忘旧工况，或保存全部历史却让旧分布与训练费用无限增长。独立 gateway 事先计算 heuristic，冷启动、特征越训练范围或 RPC 失败时回退，但逐特征范围不认证联合分布内、实际 cache hit 或容量可接收。[有限在线对照](https://arxiv.org/html/2606.00946v1#S5.SS5)支持这种更新分工，不保证无偏、普遍收敛或全局最优：贪心 TTFT 仍可能驱逐未来共享 KV，长 prefix 的候选收拢也需另付校准与局部拥塞代价。状态采集、推断、训练/回放、数据库与专用资源均计费；反馈陈旧、cache/工况失配或净预算不合时，保留原 prefix/load heuristic、固定池与 endpoint admission，不由学得即时奖励替代 TPOT、完整响应和 SLO 验收。<!-- source-family:SF-2026-ARXIV-2606-00946 -->

完整直接下锚：
> ### 低带宽拓扑要联合预算 Hops、Bytes 与 Steps
>
> 单数据中心、高带宽互联中，固定 pipeline placement 与局部通信优化通常足够，稳定拓扑也让故障和 tail latency 更容易解释。GPU 分散在低带宽、跨地域节点后，只看空闲显存或单跳带宽会失真：少放一个 transformer block 可能增加每个 decode step 的跨节点 hops；为了减少 hops 而 offload KV，又会引入 host-memory traffic；lossless compression 改变每跳 bytes，speculative decoding 则可能改变完成同样输出所需的串行 decode steps。

拟本人Review note仅待新授：`SF-2026-ARXIV-2606-00946` — Daily2026-06-03补Jun02，exact-v1 §4–5/B必要，2+2+2=6；只policy-dependent快照/所选反馈、有界近期/多样回放与heuristic退路。保range非OOD全保证、贪心/cache反侧、tie配方边界、V100功能混杂及全部费用，不采无偏/收敛、完整调度recipe/全局最优或生产SLO；未核图像素/代码/复现。当前Source/actualowner/PRE待reader首次独核，不预写入或POST。

**有界停点：** 00946单篇必要Source/6分/actualowner最小单段与完整直接两锚保存即交root和唯一reader；不预PASS/I/DAY。下一00888未本轮notice/Methods/评分/owner，其他待办不作数量目标。仅本节及必要HTML，不写Books/Report/State/index，不stage/commit/push，ready释放阶段。

## 00888 SMET — 首次必要证据与actual Ch28具体NC提案 / 2+2+2=6

2026-10-25同日Jun03恢复：按root通知00946 R100/102、00997 R99、01380 R104均已真实生效，行政由root合并，不第三研究。启动完整重读AGENTS、Research/Report合同、Sources说明/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State与本日停点；只Jun03补Jun02 BJT，R26/R28完整AB准入/联合日证有效复用，不重复GET、不把submitted/registered单独叫公开。未变PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE沿本人前轮完整阅读复用；本轮实际读Ch28对应完整三段及前后、Ch27/29职责开篇。

[exact-v1](https://arxiv.org/html/2606.00888v1) / [保存HTML](SUP_MODEL_B6_2606.00888v1_20261025.html)。当前官方[abs](https://arxiv.org/abs/2606.00888)本轮实际所见唯一v1、comments Accepted ICML2026、无withdrawn/removed/erratum，不从发表加分或保证所有渠道无纠错。实际必要读§3–4/Eqs3–11、§5开头/主表1、§5.1–5.2/5.5–5.6/Tables2–3、C配置/Alg1与G直接限制；未读所有proof、完整额外数据/推理速度附件、图像像素、代码或复现。只核最小长期机制与现有覆盖，不为增量挖其余附件。

D2为拓扑regrow后Adam局部时钟/矩冷启动的具体稳定机制；Reach2为optimizer数值/支持集迁移与active-only梯度/状态存储接口；Durability2为可复用的稀疏拓扑—optimizer身份约束，总6。Books已覆盖不降分、不排除贡献，也不将NC计第二次整合；不据同family marker单独称已审duplicate或改旧日期归属，事件归并由root按真实原记录决定。

### 必要机制、比较与直接反侧

§3.2剪枝无regrowth与保留regrown Adam states的局部消融减轻尖峰，支持新连接状态冷启动是所测的重要来源，不是所有loss spike唯一原因。§3.3假设成熟局部梯度统计慢变；新连接m/v从零而沿用large global t、忽略epsilon时，首次更新尺度约`α(1−β1)/sqrt(1−β2)`，β=.9/.999得到约3.16α。这个近似只适合所设状态/非零梯度与epsilon可忽略，不是任何新参数的无条件精确更新。

§4.1 reset新连接local timestep恢复Adam bias correction，另线性warm-up W步至目标LR；§4.2按density设`αs=α0/sqrt(d)`，用于稀疏fan-in/保守更新补偿，不是通用μP结论。§4.3只保active gradient和m/v，block-wise timestep/index metadata摊销；C/Alg1剪掉旧indices时丢其state、接入新indices再warm-up。该描述支持active-state存储与映射管理，不声称所有forward/backward都由sparse kernel直接执行、全dense权重/activation消失，或resume/checkpoint原子迁移实现已经验收。现书的原子身份要求是由此提出的系统设计责任，不是作者已测故障恢复。

§4.4 L-smooth局部上界把regrown update norm控制到Ct后限制一/二阶项，只作局部稳定解释；不保证负loss变化、全Adam收敛或任何regime无尖峰。无需为未采用完整更新界再遍历全proof。

§5/C LLaMA60M–1B、C4，BF16、seq256、batch512、embedding/outputhead保持dense；主训练1.3B–13.1B tokens/10k–100k steps，350M配置50k主表与§5.5–5.6的20k/2.6B消融是不同budget，不能混为等训练时长。Adam β=.9/.999，global前10% warm-up再cosine到10%LR；topology ΔT100、ratio.2、local W10，uniform density。Table1 baseline来自外部论文不是作者本轮所有seed重跑，且主表tokens1.1/2.2/6.4/13.1B与C表1.3/2.6/6.5/13.1B口径并不全同，不采精确等budget跨方法性能优胜；1B SMET15.61仍高于dense15.56。

直接Table2 LLaMA350M/C4/2.6B/20k：SMET随机regrow PPL21.61/22.93/23.93/25.85改善对应SET24.71/26.38/27.87/28.96；SMETgrad在d=.3为24.01，仍劣于static23.55，非所有regrow/密度普遍胜static。Table3 warm-up与LR各单独都不及完整组合，单LR d=.5为24.79反高于Adam24.71；更长warm-up、过高/过低topology频率也不自动更优。只支持所测稳定/进度分工，不能把scale-up视为独立总有效原则。

§5.2内存拆账BF16/batch1/gradient checkpointing关，减少activation影响；图caption为estimated memory，正文称measurements，采用仅保active-state存储机制和该配置拆账，不称已独立复算峰值显存。GPU型号/完整训练墙钟、并行布局、训练实现/内存峰值测量细则未在必要域披露（Not Disclosed）；G明确unstructured/简单blocks、Adam-only、hardware-aligned实际加速及SFT/RLHF仍待后续。索引/timestep、mask更新/重排、warm-up与LR搜索、全部训练/稀疏kernel适配均付费；不由少optimizer bytes签更快或推理收益。

### actual owner具体已有覆盖（待reader首次核，无新PRE/正文请求）

唯一 `TRAIN-PRETRAINING` / [Ch28“Dynamic Sparsity的Topology Update也是Training State Transition”](../../../../../books/part-04-training-system/28-pretraining.md)。实际完整正文三段如下（same family `SF-2026-ARXIV-2606-00888`）：

> Dense training 或静态 mask 让一组参数持续积累 Adam moments，状态身份简单且恢复路径成熟；dynamic sparse training 周期性 prune / regrow 后，新激活连接没有历史一阶、二阶矩，却若沿用全局 late-training step，首次更新可能远大于成熟参数。此时 loss spike 的 owner 不是 collective，而是 `mask/topology revision + regrowth initialization + local optimizer timestep/moments + learning-rate phase` 这一组训练状态。
>
> 一个受限稳定分支是在 regrowth 时重置新参数的 local timestep，并让它们经历独立 linear warm-up；随后再按 density 调整目标 learning rate，以补偿稀疏层有效 fan-in 和 warm-up 带来的保守更新。若目标还包括训练内存，gradient、Adam moments 和 timestep/index metadata 只为 active parameters 保存，并用 block-wise metadata 摊薄索引开销。mask 与 active-index owner 必须和 optimizer-state owner 原子迁移，否则 resume、regrowth 或 checkpoint restore 会把旧 moment 绑到错误连接。
>
> 它以 topology/update metadata、稀疏 kernel 适配和局部 schedule 复杂度换取较小的 cold-start spike 与 active-only state；random regrowth、density rule 与 optimizer warm-up 都是需要单独消融的分支，而不是 dynamic sparsity 的通用定理。论文只在 Adam、披露的 LLaMA/C4/OpenWebText、unstructured 与简单 block sparsity 范围内支持该机制，局部 smoothness 分析也不等于全局收敛或实际硬件加速。结构化稀疏未被 kernel 支持、非 Adam optimizer、拓扑变化不值得其控制成本或恢复一致性优先时，应保留 dense training 或静态 sparsity 作为 correctness fallback。

具体覆盖比较：第一段已承载late global step与新连接无moments的cold-start压力，未硬抄3.16倍或唯一因果；第二段完整承载本次拟长期保留的reset+localwarm-up、density补偿及active-only state/metadata机制；第三段已有单项消融、Adam/模型/图形范围、局部非全局/非硬件收益、费用与dense/static回退。正文没采用主表不等budget胜负、精确显存headline、通用μP或全局收敛，正好避开本次不采用的扩张。现有前方looped/局部梯度路线不等DST，后方SNACK是COO直接算子支持/不是动态regrow，00888这组三段仍是具体唯一owner。Ch27管数据、Ch29管指令监督，不为补差复制到两章。

**Books提案：具体已有覆盖NC，待唯一reader验收；不新增段、不改原有效正文、不请求多层PRE/写入。** 必要Source与本次NC不等同旧事件已审去重，不搬旧Daily归属；原三段的系统推导不冒称作者已验证resume/故障恢复。未遇新矛盾需重开既成Books层。

**有界停点：** 00888单篇必要Source/6分与actual Ch28具体NC包保存即交root及唯一reader；不预PASS/I/DAY。下一00846未本轮notice/Methods/评分/owner；其余普通待办不是数量目标。仅本节与必要HTML，不写共享Books/Report/State/index，不stage/commit/push，ready释放阶段。

## 00846 CUPID — 必要Source与actual-owner最小PRE / 2+1+2=5

2026-10-25同一Jun03恢复：00888 R105六分/actual Ch28具体NC、01285 R107五分/actual Ch66具体NC已有效，不第三。启动完整重读AGENTS、Research/Report合同、Sources说明/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State与本日停点；R26/R28完整题摘准入/Jun02联合日证复用，不重复GET/论证日期，不把submitted/registered单独叫公开。仅本日，未变PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE复用本人前轮完整阅读；本轮实际Ch66偏好/自适应比较全文段与Ch65/67职责交接已读。

[exact-v1](https://arxiv.org/html/2606.00846v1) / [保存HTML](SUP_MODEL_B6_2606.00846v1_20261025.html)。本轮实际开[当前官方abs](https://arxiv.org/abs/2606.00846)，唯一v1、comments38pages/11figures，所见无withdrawn/removed/erratum，不保证所有渠道无纠错。实际必要读§3.1–3.3/Eqs1–6/Alg1、§4.1–4.4/Tables2–3、§5、B.2–B.3直接设置；不采用完整regret/后验正确性保证，未读全证明/所有实验附件、人像/图像素、代码或复现。

D2为在选模时分开用户目标belief与各目标下模型utility，并由两者共同决定下一对comparison；不是仅用成熟bandit跑新排行榜。Reach1为单个用户的候选选择/交互评价机制，不因可连到gateway/release便加跨层分；Durability2为偏好证据/假设、查询分配与资源约束分责，总5。实际owner缺个人latent目标的主动比较接口，针对该具体差额深入必要域，不因尺度小或成本/理论附件降分。

### 采用范围与直接关键反侧

§3有限model pool，用户在同prompt下比较两份候选响应。GP/probit给latent utility及近似后验的不确定性，另维护目标z的belief b，按目标条件均值/uncertainty加权成belief-aware UCB来提下一对；这些z不必是可解释真实心理维度。Kernel里的model similarity与目标条件utility支持须有实际制备，不从“latent未知”推断无需metadata/先验：§4.1实际用25模型、34属性metadata，CUPID不见名称却见objective metadata，judge更见全部属性和指定目标。后验Laplace近似不等精确Bayes或用户真正偏好的唯一辨识；Eq4含当前数据索引与其后的normalization表述不作为本次完整可执行后验recipe。

§3.2.4 optional语言由辅助Grok4.1Fast+metadata映为arm indicator，再加language bias；它只改变探索方向，不是独立真实capability或安全标签。其scale式有非零下限，SD小时不能仅凭“cap”词授永不压过intrinsic utility的硬保证，§3.3定常bounded shaping与实际逐轮auxiliary反馈也不能不核假设合并成普遍regret结论。此处只采用方向性辅助、保其可能错配，不采用全部语义/收敛主张。

§3.2.5预算价格乘penalty，实际比较花费ct后才按`max(0,rt+η(ct−B/(T+τ)))`更新r；这可以调预算节奏，却不是事前扣减余额/拒绝超支的硬admission。Alg1明确for固定轮数T，未展示每轮剩余B的预检，不将“strictly control budget”照录为硬上限。查询两模型、辅助语言解析、GP更新/选择与用户时间均要另计；用户偏好高也不证明事实/领域正确，§5明确high-stakes verification未解决。

§4.1模拟25模型/34已知属性、A1–A4各5次（20模拟用户）主要支持metadata/judge给定目标中的选择取舍，不是恢复真人未表述心理机制。去language反而成本更低，去cost更快但更贵，故完整组合不叫各轴都优。§4.2另37模型/AIME、17模型/MMLU有限榜分作best oracle，10个AIME prompts不能支持开放域；17模型Table2 CUPID成本.031±.005高于ε-greedy.026±.014，CP100%高于80%，是质量/查询费用取舍非始终最低成本。Auxiliary router约30%总成本，不能漏掉。

§4.3 pool5/25/75/125的GP+UCB/belief overhead .035/.094/.267/.719s（含辅助LLM则1.833/3.485/2.595/4.618s）；更大pool的time-to-selection更短因恰有更快候选，不是随规模必加速或辅助成本零瓶颈。B.3 Colab/Python3.12.12/botorch.10.0，API/模型版本、pool与价格/延迟是该测量身份，不外推当前报价或生产SLO；hardware/并发等未在必要域披露，不补造。

§4.4 51参与者、A/B blinded within-subject文本及text-to-image，先battle选模型、再新prompts评价并打quality/budget Likert，H1明确目标至H3/H4自由目标；这支持有限人群的交互选择，不等各类用户总体效果。H1作者明确可冗余；LMA不罚成本而CUPID权衡费用，较低成本不能单独证明隐目标belief唯一增益。未读完整人群附件/原数据，不给细分显著性或精确通用win率，用户评分不能替任务oracle。§5 cold start还要求初始direction，不能写完全无先验/无表达负担。必要支持与反侧足够拟用窄接口，停止不扩全38页。

### actual owner差额与最小单段PRE（未授写）

唯一 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。实际读偏好非传递/群组portfolio、Robust Lotteries、LLM-PO两段及后比较图校正；现有主动采样优化的是冻结task/judge下区分winner，现群组异质性描述的是人口矩阵。它们尚未承载“一个用户不知如何明确目标时，同时估utility与目标belief以提下一对”的接口；没有00846/CUPID同family。只补这条有限交互选择，不把通用GP/UCB再讲成新理论；Ch65资源scheduler与Ch67metrics不接管偏好选择。

完整直接上锚：
> 分配规则与停止证书须分别核验。[LLM-PO的条件分析](https://arxiv.org/html/2604.08779v1)把有限集合、iid/stationary comparison及unique Condorcet winner等作为识别条件；有maxmin候选不等于一定存在逐对胜出的Condorcet winner，偏好环或judge漂移会改变问题。结构化分支还需模型、探索support与信息矩阵成立，Fisher只提供local surrogate。作者实跑的heuristic停止阈值未获同一理论直接支持，有限小任务的PCS与较少query不能认证任意预算δ-PAC或全prompt最优；真实oracle也来自有限预采样，rule/LLM judge仍有条件偏差。预采样、候选生成、judge、分配求解与复验全计费；支持不足、环关系或测量身份变化时，保留均匀预算、原始pair evidence与Unknown/并列，重新定义选择目标而不硬停授予winner。

拟新增完整单段：
> 用户若尚不能明确各项目标的权重，主动比较还可同时维护两份不确定性：按目标条件估计候选模型的效用，再由同 prompt 的配对选择更新目标 belief，用 belief 加权的效用与探索项提出下一对。可选语言提示只辅助偏置探索，不使推断出的目标成为用户真实意图或模型能力标签。[有限选模研究](https://arxiv.org/html/2606.00846v1#S4.SS4)支持这条交互分支，但 metadata/judge 模拟与有限真人偏好须分账；目标明确时它可能冗余，偏好匹配也不认证事实或专业正确。花费后提高价格惩罚只调预算节奏，不替每轮剩余额度的硬准入；双模型响应、辅助语言解析、后验更新和用户时间都付费。候选池、反馈模型或目标支持不足时，保留明确 rubric、固定比较与人工选择，并允许 Unknown/并列，不由后验收敛或更低账单签发部署、安全和硬预算保证。<!-- source-family:SF-2026-ARXIV-2606-00846 -->

完整直接下锚：
> 比较图还可以用于修正既定context人口下的score差估计，而不只分配下一次比较。在contextual Bradley–Terry模型中，先拟合每个候选的context score，再把已观测边上的比较结果减去预测胜率，以Fisher加权图的节点potential差聚合这些残差，并用交叉拟合将nuisance拟合与被校正样本分开。[受限图估计接口](https://arxiv.org/html/2509.05852v1)借间接路径利用已有比较，不创造缺失的真实对决，也不消除judge共同偏差；所估的是按声明人口定义的score差泛函，不是条件win probability、准确率或真实质量。连通性、score规范、比较独立性和同一context支持需先成立，均值中心化不能补跨分量的位置。Potential表示不等有限样本精确区间或全运行时线性，误差率/图谱/渐近条件亦不能由五模型的小图示例代验；原全局p值后的逐项拒绝与shift权重/variance口径未闭，这里不采用其多重检验、迁移recipe或保证。每context的权重/图求解、score训练、cross-fit、bootstrap和全部judge比较都计费，重复同题/同judge不成为独立新问题。模型、图支持、人口或推断条件不足时，保留描述性BTL、直接比较、可信人工anchor与Unknown/并列，不由修正后的分差批准模型发布。

拟本人Review note仅待新授：`SF-2026-ARXIV-2606-00846` — Daily2026-06-03补Jun02，exact-v1 §3–5/B.2–3必要，2+1+2=5；仅个人目标belief/条件utility的主动配对选择，保latent/metadata/judge非真意图、偏好非正确、soft预算非hard admission、明确目标冗余及全调用/人工费用；不采完整GP/regret配方、普遍最优/安全或当前成本，未核像素/代码/复现。当前Source/actualowner/PRE待首次独核，未写Books或预POST。

**有界停点：** 00846单篇必要Source/5分/actualowner最小单段及完整直接两锚保存即交root/唯一reader，不预PASS/I/DAY。下一00819尚未本轮notice/Methods/评分/owner；原38含本项是普通待办、不是保留/数量配额。仅本节与必要HTML，不写共享Books/Report/State/index，不stage/commit/push，ready释放阶段。

## 00819 DeLask — 必要Source与actual-owner最小PRE / 2+1+2=5

2026-10-25同一Jun03恢复：按root通知00846 R108/111实际Ch66与00515 R109六分/Ch26具体NC已生效，不第三有效层；行政由root合并。启动完整重读AGENTS、Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State及本日停点。R26/R28完整AB准入/联合Jun02日证复用，不逐篇重复GET/日期证明，不把submitted/registered单字段叫公开。只本日，未变PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE复用本人前轮实际完整阅读，本轮实际读Ch17 residual/相邻分支及深度诊断、Ch16/18交接。

[exact-v1](https://arxiv.org/html/2606.00819v1) / [保存HTML](SUP_MODEL_B6_2606.00819v1_20261025.html)。当前[官方abs](https://arxiv.org/abs/2606.00819)本轮实际所见唯一v1/comments5pages，无withdrawn/removed/erratum，不保证所有渠道无纠错。必要实际读§2.1–2.4/Eqs1–7/Alg1、§3/T1、§4/T2–3；未读参考论文证明、图像像素、代码或复现，不补泛泛layer=gradient descent论证。

D2为从相邻层词表预测分布变化的方向关系触发当前hidden增量衰减，非仅新任务套成熟skip；Reach1为局部decoder层内干预，不将生成/事实评价的关联加跨系统分；Durability2为diagnostic proxy、computed-layer输出修改与实际执行省量分责，总5。原准入“具体新增机制”继续成立，但采用收窄到这一可核干预，不采深层普遍引起幻觉/真梯度理论或普适可靠性。

### 必要机制、直接评价与关键反侧

§2把同一个最终linear head应用于各层hidden，softmax得p^j；Δ^j=p^j−p^(j−1)，再算连续两份Δ的cosine c。c<负阈值τ只说明在该readout下变化方向反转，不是真实loss gradient、语义偏离真值或因果幻觉layer标签。模型最终head只以末层训练，中间readout可能失配；§2.2例外正是最后层跳过会破坏对齐。摘要的“conditionally equivalent to GD”在本文没有可用于任意Transformer的假设/势函数证明，不把比喻转成已验模型训练/优化事实。

§2.4/Eq6当c<τ时令`h^j←αh^j+(1−α)h^(j−1)`，相当于`hprev+α(h−hprev)`的残差增量衰减，α=sigmoid(βc)，β>0。原Eq6后一句称更大α更依赖前层，与式矛盾；后Eq7解释c更负α更小、前层占比更大，与代数一致，本采用按公式/后一说明限定，不自补反向recipe。所选β=.01、负c∈[−1,0)时α约.4975… .5，仍约保留一半当前增量，不能称完全skip或强度覆盖0…1。

为计算c已经需要当前层输出与多个词表projection/softmax，因此不是计算前免做该layer，更不能从“layer skipping”名称给吞吐/能耗收益。Alg1输入全hidden，循环只显式算p^(j−1)，未完整列p^j/p^(j−2)制备、修改后下游重算/传播、KV/cache一致性和零Δ范数处理；不将它当已闭合runtime实现。采用可定义的局部插值候选与有限行为对照，不授精确cache recipe、原checkpoint分布保持或全模型幻觉检出器；若部署须另验propagation/cache/数值与完整质量费用。

§3 LLaMA2-7B/LLaMA3-8B，regular/DOLA/ITI/UAD/AD对照、lm-evaluation-harness默认配置、batch1；TruthfulQA/FACTOR是benchmark定义的factual任务，MMLU/ARC-C、TriviaQA/GSM8K/CoQA是各自多选/开放任务，分数提升不识别唯一幻觉机制。T1 LLaMA3较好但LLaMA2 MMLU45.54→45.47反退；TruthQA-MC2的DOLA53.17还高于DeLask52.27。缺seed/区间、具体checkpoint revision、harness commit、prompt/输出长、precision、GPU/完整latency费用（Not Disclosed），不能称广泛显著/生产可靠或加速。

§4手调τ/β、LLaMA3 TruthfulQA最优τ−.15/β.01，T2 τ−.05 MC2=56.91低于baseline57.10，β.1/.001分别56.82/56.62亦反退；未披露独立holdout调参资格，不把同测试表最优当固定跨域阈值。T3从早层4/8启用会明显伤质量，16最优但非所有模型的安全midpoint；公式/Alg1的N/2−1…N−2与表16是索引约定未完整闭合，不拷成普适层号。全部原layer、extra heads/softmax、Δ缓冲/归一、插值、阈值搜索与独立质量回归都计费。已足支撑局部候选干预及反侧，停止不扩参考文献/所有理论。

### actual owner与最小逐字PRE（未授写）

唯一 `MODEL-TRANSFORMER-LAYER` / [Ch17 Residual connection](../../../../../books/part-02-model/17-transformer-layer.md)。本轮实际读residual完整主干/其后有条件势函数和coarse/anchor/Depth-Attention分支，以及recursive depth诊断；现文已分表示变化与能力，不授真梯度/收敛，但没有以相邻层词表Δ方向提案衰减当前residual增量的具体机制，同family00819/DeLask未命中。Ch44拥有token执行主干，不为名称“decoding”迁去复制局部干预，Ch16/18交接保留。只拟一段，明确不是梯度理论或物理skip，不新建杂章。

完整直接上锚：
> 即使 `dF/dX` 在某些方向很小，梯度仍有 identity 路径。Residual 不能保证任意深网络稳定，却显著改变了优化条件。

拟新增完整单段：
> 保留 identity 也允许对已经计算出的层更新作较窄干预：用末层词表 head 读各层状态，比较相邻两次预测分布差的余弦；方向明显反转时，将当前状态与前层状态插值，相当于衰减当前 residual 增量。这是 readout 条件下的方向信号，不是真实 loss gradient，也不能把被选层命名为幻觉来源；中间表示与末层 head 的失配仍可能改变读数。[有限层内干预对照](https://arxiv.org/html/2606.00819v1#S4)显示启用层段、阈值和混合强度会改变质量，部分任务/配置仍反退。计算信号前已执行该层，还增加词表投影、softmax 与插值，不能因称作 skipping 就登记省算；修改后状态传播、cache 和零差向量的数值处理须另验。代理、质量或完整执行费不合时，保留原完整层栈、末层读出与独立任务评价，不由低方向一致性签发事实、无损分布或加速保证。<!-- source-family:SF-2026-ARXIV-2606-00819 -->

完整直接下锚：
> 若目标是给整个 block 的输入扰动一个可证明界，就要收紧分支本身，而不只保留 identity。一条条件构造把更新写成凸势的负梯度 Euler 步：MLP 为 `x−τWᵀReLU(Wx+b)` 且 `τ≤2/‖W‖²`；attention 把 value 与约定的投影绑定为 `V=A`，以 `x−η softmax(xᵀAy)Ay` 更新，在固定 compact domain 上限制 `η≤2/sup‖Ay‖²`。这样的 query 非扩张性依赖 tied weights、符号、步长与逐层域；普通自由 Q/K/V 的正向 residual 不自动满足。context 则有自己的 Wasserstein-1 Lipschitz 常数，不继承 query 的1。<!-- source-family:SF-2026-ARXIV-2602-15503 -->

拟本人Review note待新授：`SF-2026-ARXIV-2606-00819` — Daily2026-06-03补Jun02，exact-v1 §2–4/Eqs1–7/Alg1/T1–3必要，2+1+2=5；仅readout Δ方向→已算residual增量插值候选。保α文字与公式按代数收窄、中间head失配、非真实gradient/幻觉label、早层/参数/任务反退及propagation/cache/零范数未闭和全费；不采深层唯一幻觉源、完整recipe、lossless/加速，未核像素/代码/复现。当前Source/actualowner/PRE待唯一reader，不预写入/POST。

**有界停点：** 00819单篇必要Source/5分/actualowner最小单段及完整直接两锚保存即交root和唯一reader，未预PASS/I/DAY；下一00813尚未本轮notice/Methods/评分/owner，原37含本项仍普通、非数量目标。仅本节与必要HTML，不写共享Books/Report/State/index，不stage/commit/push，ready释放。

## 00813 Cross-Generational Transfer — 必要Source与actual-owner最小PRE / 2+1+2=5

2026-10-25同日Jun03恢复：按root通知00819 R112必要/5分/actual gap通过，但仅reader修后单段获批、原作者稿未批，传播未闭不能由结果表冒充完整路径；本作者不改其已成层、不预SAVE/POST，root负责。启动完整重读AGENTS、Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State和B6精确停点；R26/R28有效完整AB/联合Jun02日证复用，不重复GET日期、不用submitted/registered单字段称公开。只本日，未变PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE及Ch65/67职责交接复用本作者前轮实际阅读；本轮实际读Ch66攻击预算/自适应身份、clean result预算、相关安全评价与Ch72开篇职责。

[exact-v1](https://arxiv.org/html/2606.00813v1) / [保存HTML](SUP_MODEL_B6_2606.00813v1_20261025.html)。当前[官方abs](https://arxiv.org/abs/2606.00813)实际所见唯一v1/comments8pages/3figures，无withdrawn/removed/erratum，不保证所有渠道无纠错。必要实际读§3–4、§5.1–5.4/T2/迁移矩阵文字与图注、§6直接讨论/二judge审计/限制；未看图像像素、代码/攻击payload或复现，不追无关外部证明。

D2为先对各目标独立自适应搜索，再冻结归档在共同judge下source×target交叉重放、分开search adaptation与迁移的评价接口；Reach1为有限模型版本的安全行为评价，不借安全全生命周期常识加跨层分；Durability2为攻击producer/target/judge/搜索与重放预算及分母身份可复用，总5。原准入的具体评价反证保留；不凭近期模型名/非单调headline加分，不因书已有红队主题或审阅费时排除。对actual窄缺口补必要深入，不扩全部artifact。

### 必要支持与直接反侧

§3 MAP-Elites按strategy/encoding/harm类别保存各niche最高fitness攻击，fitness由自托管Llama3.1-8B-Instruct judge对refusal/harm/relevance三轴读出。各source模型各3seed独立搜索后，冻结archive A(i,s)重放到其余target j，产生T[i,j,s]，报告per-entry/per-category及seed均值/方差。Diagonal是其各自自适应归档，off-diagonal才是在同一source archive上换target；不同source归档并非同一固定400题人口，不能把对角/非对角百分比直接叫能力真值或统一攻击难度。

§4 4个Gemma checkpoint标签7B/9B/12B/31B且架构/参数量同时变化，不是等参数可控alignment实验。文中声明vLLM.19.1/BF16/temp0、single H200141GB顺序serving，judge在RTX409024GB；Evolution batch50、200generations、concurrency5、mutation.3/crossover.7，三seed42/1337/2718，36个source-target-seed重放。原3.1说7semantic categories，4.2 grid6×6×8=288却seed pool仍7类；具体额外类别/空格处理未闭，不照录288为已验证有效覆盖或复制完整计数recipe。约60 GPU-hours是作者全流程估计（含额外70B审计），不补造完整精度/预算公平、prompt长度/max输出或独立运行。统一judge使口径一致，不等full reproducibility/独立真值。

§5.2各source归档在Gemma3目标约44–46%、在Gemma4约14–18%的迁移读数支持本协议下受体差异，而不是保证新模型全面安全。§5.1 self archive整体59.4/45.5/68.7/33.9%（3seed mean）；只4个checkpoint不fit scaling/U-shape定律。统计正文p=.030为作者仅3seed/未校正paired bootstrap，未实际复算，不能给强人群显著性或唯一代际因果。类别内分母也变：Gemma4 harmful只有2seed（另1seed无该类entry），cybercrime三seed2.8/50/91.7%极散；总体低不代表所有切片更好。摘要“cybercrime近100% across all generations”不合T2 Gemma4 48.1，采用表格而非宣传。§5.1 raw-seed固定400prompts已观察同样非单调且evolution再加7–14pp，所以“不靠adaptive看不到/静态完全miss”过强，不采用。

§6二judge audit用52份已存response、Llama3.1-70B，refusal agreement96.2%却harm κ=.15；copyright 8B判100%对70B仅50%。这是judge敏感性，不是70B已被授gold或全部cell校准完成，不能将52小样本外推per-category真实harm率。架构由text到multimodal与回归同时发生仅是猜测，训练数据/后训练recipe/capability对搜索空间的影响未排除；只测text，不测vision。自动harm评分更不等真实违法行为/执行副作用。三seed/单家族/搜索子空间与HarmBench有限支持，不给无攻击成功=安全、全版本单调或倒退的普遍结论。Archive制备、全部搜索/重放、judge/第二judge及人工分歧审计、版本维护均计费；不运行真实攻击或提供payload。

### actual owner与最小逐字PRE（未授写）

唯一 `PLATFORM-EVALUATION-SYSTEM` / [Ch66“攻击预算是一条风险曲线”](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。现正文已绑定model/sampler/attack distribution/budget并分攻击器在线训练与冻结重复采样；clean result节也已有无发现≠无风险。实际没有00813同family或source archive→多target交叉重放接口；只补“归档生产/受体与judge”这一评价身份差额，不再讲通用安全原理，不搬Ch72授权/防护实现。

完整直接上锚：
> 安全评估若只测一次采样，会低估攻击者重复尝试的能力；直接穷举大 `N` 又昂贵。更完整的 subject 是
> `model/sampler/attack distribution/budget`，输出应是带 uncertainty 的 `risk(N)` 或达到风险阈值所需预算，
> 而不是把小样本最大值当作模型固有属性。统计外推依赖 exchangeability、分布拟合和 benign/unbreakable
> mixture；自适应攻击、并行相关性或 sampler drift 会破坏这些假设。高风险区仍需实际大预算验证，模型、
> sampling policy 或 attack corpus 改变后必须重估。

拟新增完整单段：
> 跨版本比较还可把攻击归档的生产者与被测受体拆开：分别针对各 checkpoint 在固定搜索预算下产生 archive，冻结后将同一份 archive 重放到多个目标，并保存 source、target、seed、judge、有效条目与类别分母。对角线测的是针对本模型搜索的结果，非对角线才描述该 source 攻击的迁移；各自搜索后的 ASR 不自动来自同一难度人口。[受限跨代重放研究](https://arxiv.org/html/2606.00813v1#S6)暴露了这种差异，但少数 checkpoint 的参数/架构同时变化，不能唯一归因 alignment 或模态，也不证明新一代全面更安全。统一 judge 只固定量尺，第二 judge 可在 refusal 高一致时仍对 harm 明显分歧；须留原响应、切片和未决标签，不能把较大 judge 直接授真值。全部搜索、重放和分歧审计都计费；类别缺样、量尺或预算不可比时，保留固定原始题、局部矩阵与 Unknown，重校准受影响部分，不从较低迁移率签发零风险或跨代安全定律。<!-- source-family:SF-2026-ARXIV-2606-00813 -->

完整直接下锚：
> 攻击预算曲线还应声明攻击器是否在测试期间更新权重。冻结攻击器的上下文搜索，与每个 behavior–victim 对重置 adapter/optimizer 后在线适应，是不同威胁身份，不能用相同 query 数抹平本地训练、reward/classifier、token 与墙钟费用。[Red-TTT 的授权红队对照](https://arxiv.org/html/2610.05282v1)只支持其可更新攻击器、sampling-only victim 的受限配置；replay 保留原 reward 不等无偏 off-policy 估计，奖励与评价共享 classifier 也不是独立安全真值。不同 query 分配有反退，不能把总体提升归给任意单组件或宣称所有在线适应必胜。保存 reset 作用域、训练与全部查询费用，并保留独立 judge、合法任务门禁和 frozen 重复采样基线；预算不可比或评价不可靠时不外推生产安全。<!-- source-family:SF-2026-ARXIV-2610-05282 -->

拟本人Review note待新授：`SF-2026-ARXIV-2606-00813` — Daily2026-06-03补Jun02，exact-v1 §3–6必要，2+1+2=5；仅source归档/target交叉重放与judge/类别分母分责。保3seed/单家族、grid类别口径、空类、第二judge52样本弱harm一致、rawseed已显非单调及全费用，不采安全排序普效/模态alignment因果/统计强保证或零风险；未核像素/代码/复现/攻击payload。当前Source/actualowner/PRE待唯一reader，不预写入/POST。

**有界停点：** 00813单篇必要Source/5分/actualowner最小单段及完整直接两锚保存即交root和唯一reader，不预PASS/I/DAY；下一00801尚未本轮notice/Methods/评分/owner，不预减root尚待00819 actualPOST计数。仅本节与必要HTML，不写共享Books/Report/State/index，不stage/commit/push，ready释放阶段。

## 00801 Quality-Diversity Evolution — 必要Source与actual-owner具体NC提案 / 2+1+2=5

2026-10-25同日Jun03恢复：root通知00813已R117真实POST/I生效，其行政由root负责，不第三有效层。启动重读AGENTS、当前Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State与本日精确停点；R26/R28完整AB准入/联合Jun02日证有效复用，不再逐篇日期GET，不将submitted/registered单字段叫公开。只本日；未变PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、Ch65/67职责交接复用本人前轮实际完整阅读，当前Ch66相关完整段重新实读。不写共享Books/Report/State/index。

[exact-v1](https://arxiv.org/html/2606.00801v1) / [保存HTML](SUP_MODEL_B6_2606.00801v1_20261025.html)。当前[官方abs](https://arxiv.org/abs/2606.00801)实际所见唯一v1、9pages/6figures/Workshop comments，无withdrawn/removed/erratum提示；不保证所有渠道没有修订。必要实际读§2.1–2.3/Alg1、§3/T1/图注与分析、§4全部直接限制，针对fitness与覆盖分母只追加A/T2、C；未读B攻击实例，不看图像像素、代码、Rust实现或复现，不执行或改造攻击。

评分对象是按语义描述符保留多个局部最优攻击、以有限类别profile代替只找一个最高分的具体评价分支，而非MAP-Elites通用成熟原理或模型名：D2（改变攻击候选保留/解释接口），Reach1（局部安全评测搜索），Durability2（可复用的有限归档/量尺边界），总5。原准入继续有效；NC不降贡献分，不把actual已有覆盖倒称原论文无增量或同事件重复。对照不足限定效力主张，不以小预算本身排除。

### 必要机制、收益权限与直接反侧

§2.1把primary/optional secondary strategy、encoding、persona组成genome，再由模板渲染；变异发生在这些可解释字段而非任意token。§2.3/Alg1以primary strategy×encoding×length bin定位cell，只在空cell或fitness更高时保存候选，再选择/变异产生下一代。它实现“保留多类局部最优”这一设计提案；genome字段空间与archive描述符空间不是同一个完整语义空间，语法有效/模板可解释不证明语义无损、独立失败类型覆盖或现实威胁完整。

§3为4个指定目标，population30/generations30、6×6×6=216cells；A/T2补Devstral仅20代。单generic placeholder seed，不是标准有害行为全集；§4明确MultiTurn只是结构framing，每次仍单次query，不能当真实多轮/Agent交互证据。§3报告36/216=16.7%填格、约20代plateau；这是有限grid、搜索预算与该judge下的观察，不能把收敛停滞说成没有新漏洞、把36种strategy×encoding组合说成216cells均充分测试，或由填格比例认证语义安全覆盖。原图注“暗格”同时含未探索/拒绝，须留两种状态，不能由同色补成已测试。无单目标/token搜索/随机预算匹配的受控比较，不据本文认定MAP-Elites提高真实攻击效力或各组件因果贡献。

关键量尺冲突留原证：§2.2与Alg1 line7仅定义fitness {0,.4,1}，§3/T1却有.8，A/T2另列{0,.4,.8,1}，仍未给.8判定规则/完整语义。不能把.8补造为多样本均值或真实80% ASR。Heuristic refusal短语judge的50份人工抽查约12%错判是作者小样本估计；未观察false positive不等全体无false positive，也不能把没有refusal短语当已发生有害行为。§4自认不区分harm程度，不采用模型安全排名、内部filter架构或encoding绕过机制的因果猜想；Claude uniform .4/预算plateau不证明不可攻击。

C把6类retention比例pool到所有模型，Roleplay8%小于Authority9%，与正文/C称Authority最少不一致；不照录类次序或由pooled比例推出每个模型同排序。§3末也明确所谓cross-model共同exemplar不是controlled transfer experiment，不能仅因相似genome出现在多个archive就证明实际迁移。以上影响经验排名/完整测量recipe，但不否定Alg1可定义的分cell保留机制；本次不以泛化安全结论绕开冲突。

所有候选制备、目标query、判分、archive/描述符维护、独立复验与人工审计须计费（项目判断）；论文没有足以核完整token/墙钟净费、模型精确revision、重复seed区间与全参数口径的披露，Not Disclosed。必要支持与直接反侧足够，停止，不为消除所有未知遍历代码/附件。

### actual owner具体承载比较：No Change提案，不新增正文/PRE

唯一 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。本轮actual实读“攻击预算是一条风险曲线，不是ASR@1”完整主体、当前00813段、Red-TTT直接下侧及“Adversarial Coverage不能由一个比例代表”完整段/上下标题。不是仅凭章节名或00813同作者判NC；00801是独立Source Family，不标已审duplicate。

具体承载段一（当前actual全文）：
> 搜索到多少 behavior cells、每个 cell 找到多强 exploit、已覆盖区域上的 repair error，以及未覆盖区域的 metric radius 是不同量。质量—多样性搜索可以保留各 cell 的最严重 correctness-flipping edit，却不能从“覆盖率高”推出全域安全；aggregation rule 改变时 exploit surface 也会变化。更细分解提高运行与 archive 成本，低风险回归仍可保留随机扰动，但 release claim 必须把未覆盖空间显式留作限制。

此段已具体承载00801可支持的长期主张：按cell保留不同局部最优而不是只报一个峰值；cell数量、局部质量、未覆盖区域与release权限分开；更细分解/归档有成本。00801的strategy/encoding/length与模板genome是该接口的一种有限实例，本次没有独立控制证明其带来须改写现有判断的更强保证。不能为新增字段名称硬添“语义空间天然完整/更快收敛”的未经支持正文。

具体承载段二（当前actual全文）：
> 跨版本比较还可把攻击归档的生产者与被测受体拆开：分别针对各 checkpoint 在固定搜索预算下产生 archive，冻结后将同一份 archive 重放到多个目标，并保存 source、target、seed、judge、有效条目与类别分母。对角线测的是针对本模型搜索的结果，非对角线才描述该 source 攻击的迁移；各自搜索后的 ASR 不自动来自同一难度人口。[受限跨代重放研究](https://arxiv.org/html/2606.00813v1#S6)暴露了这种差异，但少数 checkpoint 的参数/架构同时变化，不能唯一归因 alignment 或模态，也不证明新一代全面更安全。统一 judge 只固定量尺，第二 judge 可在 refusal 高一致时仍对 harm 明显分歧；须留原响应、切片和未决标签，不能把较大 judge 直接授真值。全部搜索、重放和分歧审计都计费；类别缺样、量尺或预算不可比时，保留固定原始题、局部矩阵与 Unknown，重校准受影响部分，不从较低迁移率签发零风险或跨代安全定律。<!-- source-family:SF-2026-ARXIV-2606-00813 -->

此段已具体承载00801测量边界：archive类别/有效分母、judge身份、固定归档重放才承担迁移，以及分歧/Unknown/全费。§2.2–A/T2分值矛盾、generic seed、结构MultiTurn与C排序冲突保在本Source供报告准确限定义务，不把该局部未采用经验排名硬加进Books；未采用的.8不要求现正文替它定义。两承载段合起来已足够，不新建Review note、不为已覆盖分支再写多层PRE。NC仍待唯一reader首次必要/实际覆盖独核，不预宣通过。

**有界停点：** 00801单篇必要Source/5分/actual-owner具体NC提案已保存，立即交root和唯一reader，未预NC通过/I/DAY；下一00735尚未本轮notice/Methods/评分/actualowner，不扩其他MODEL/四定义或别日。仅本节与必要HTML，不stage/commit/push；本准备阶段ready释放。

## 00735 ViBE — 必要Source与actual-owner最小PRE / 2+2+2=6

2026-10-25同日Jun03恢复：root通知00801经R120必要/5分/actual Ch66具体NC已通过，行政由root采用，不第三原件或有效层。启动重读AGENTS、当前Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State与B6精确停点；R26/R28完整AB准入及联合Jun02日证复用，不再逐篇日期GET。只本日；未变PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE及Ch55/57相邻职责复用本作者前轮实际阅读，当前Ch21 placement主干与Ch56相关完整段重新实读。仅本必要包writer，未获共享Books/Report/State/index写权。

[exact-v1](https://arxiv.org/html/2606.00735v1) / [保存HTML](SUP_MODEL_B6_2606.00735v1_20261025.html)。本轮[当前官方abs](https://arxiv.org/abs/2606.00735)实际所见唯一v1、无withdrawn/removed/erratum提示，不保证所有渠道无纠错。必要实际读§3受控token/硬件分析、§4.1–4.2全部具体机制、§5.1–5.5/T2/F8–15文字与图注；因动态recipe前后张力，只追加直属A.2/Alg1–2，不读代码、图像像素或复现，不扩外部理论。

评分为D2（同型号设备的负载相关时延差异使token均衡与execution-time均衡分离，具体改变专家放置目标），Reach2（kernel逐卡profiling→EP placement→服务SLO的实际执行接口），Durability2（负载/硬件共同校准、静态/动态费用与失效条件可复用），总6。不借芯片变异常识、NP-hard成熟结论或可联想跨生命周期加分，不因actual已有通用measured-rate原则降分。采用仅负载条件下的逐卡耗时模型与窄规划边界；不采完整在线最优recipe或标题中的所有扩规模保证。

### 必要机制与可支持结论

§3在8×MI325X/DeepSeek-V3/EP8/Sonnet观察层间expert热点与同型号设备执行差异。其固定均匀token对照仍有kernel耗时差，依据measured performance给快卡较多token后完成时间更接近，支持“token均衡不充分”这一窄反证。功耗受限/DVFS差异在compute重的prefill较明显、decode/低负载弱；不能由遥测唯一证明全部差异来自制造工艺，或把时钟均匀直接叫任务质量/全系统利用率真值。

§4分别profile每卡在稳态、固定fused-MoE kernel下的负载→耗时`f_g(n)`，再对代表输入记录每层expert activation。给定布局S_g，估该卡负载为所放expert负载之和，层耗时为`max_g f_g(n_g)`，跨层目标求和。主张是把负载分布和设备耗时共同放进放置成本，不修改router的token→expert语义。Greedy用单一参考负载N/E处的逆耗时作速度、按速度分token目标，再将高负载expert依目标缺额分配；这不是求解完整非线性makespan的保证。Profile的kernel、phase、token计量/负载单位与实际执行须一致，不能将relative activation无条件代入绝对token耗时曲线（项目接口要求）。

§5.1主实验单节点8×AMD MI325X(256GB/1000W)、vLLM0.14.2/PyTorch2.9.0/ROCm7.0/AITER；DeepSeek-V3与Qwen3-235B均FP8，dense TP8/MoE EP8/top8；vLLM contiguous/EPLB/ViBE三布局，每卡expert数相同以固定显存使用。主布局均离线profile后固定，不能把主图收益算作动态recalibration贡献。ShareGPT5000请求平均219.2in/200.8out、Sonnet1000请求1024in/128out，Poisson fixed-rate replay；TTFT阈值250/350ms，TPOT DeepSeek125/Qwen100ms，报告90%合规前沿。阈值与请求人口是作者配置，不是通用用户体验标准。

Prefill/Decode在同节点分别模拟：prefill长输入/单输出，decode预热prefix cache、除最后16token block外命中100%。这是隔离阶段的部署代理，未实测完整P/D网络与KV transfer，不称端到端disaggregated系统认证。§5.2报告相对EPLB的SLO前沿Qwen约15%/DeepSeek约12%、特定DeepSeek Sonnet P90 TTFT最高45%下降；均绑定图中QPS/人口，未复算像素，不把摘要14%当统一协议结果。§5.3给kernel gap与遥测支持局部straggler改善，但All-to-All、denseTP与排队不自动消失。

直接反侧是§5.2低QPS时EPLB可持平或略优（举Fig9b QPS2）；decode compute轻且hot experts同卡时，内存/通信争用可能压过耗时均衡收益。不能由每卡更均匀或kernel更快签发所有phase、QPS与SLO都改进。主结果未给足重复seed/统计区间或独立质量等价测试；重放不改逻辑expert选择是设计意图，不等已实测所有数值路径bit-identical。校准、数据采集、solver、统计维护、权重搬迁和完整回归都付费，未披露完整部署净费不补造生产收益。

### 动态路径与扩规模：具体冲突隔离

§4.2.1称固定GPU的`f_g(n)`可一次profile保留；§4.2.4主要刷新送入模型的n/负载分布，而非定义完整温度/干扰改变时的f再拟合。§3要求batch量级与latency imbalance共同触发，具体§4/A1算法却只列100sample向量、每10passes、cosine distance>.05触发；若当前向量仅是reference的正比例放大，cosine不变（公式直接推导），不能检出论文自己强调的纯强度漂移。不得声称已实现所有workload/performance drift监测；采用耗时模型时，纯量级/实际误差须另验（项目推论），不是偷偷补原实现。

§4/A.2/Alg2称从当前布局迭代交换最慢/最快GPU的expert，按f预测收益择最好swap，至max≤1.03mean或无正收益即停；无正收益停止不保证达到3%容差，更不证明全局最少搬迁或最优布局。§4称典型5–30swaps而全解重排200+/256slots；§5.4却把减少开销的incremental/speculative updates列future work，未足闭合表明其在线实验实际用了哪条增量路径。交叉profile(SG→SN/SN→SG)下adaptive的合规前沿恢复与迁移引入短时TTFT尖峰可以作为作者有限结果；不把它授完整Alg2已实现净收益、无中断或在线最优保证。该张力不影响静态f_g(n)+放置目标的采用，不用动态headline绕过。

§5.5另有MI300X节点较温和变异与对MI325X GPU0修改V–F曲线造成最高13%偏差的受限对照，不是自然生产全分布。Rack-scale用10×8 MI300X的实测逐卡profiles，再重放ShareGPT token计数投影；更大卡数还复制部分profiles。它不是80+/rack端到端serving实测。EP更大一方面扩大设备差异，另一方面减少每卡expert数/放置自由度，16–32sweet spot及64以上趋同只属此模型/投影条件，不采“硬件差异影响随规模永远增大”的单调结论。支持与直接反侧已足，停止不读全附件或代码。

### actual owner差额与最小逐字PRE（未授写）

唯一 `INFER-SCHEDULING` / [Ch56“Expert Mapping还要吸收设备速度的时间变化”](../../../../../books/part-05-inference-system/56-inference-scheduling.md)。Ch21 actual placement段已分router/placement并拥有demand/capacity/topology与epoch，不再在那里复制runtime控制。Ch56 actual已有“same token count≠same time、measured service rate、迁移与静态回退”完整论证，不能用ViBE重写这条成熟原则；缺的是同型号设备在负载强度区间内的逐卡kernel耗时曲线、曲线与expert需求配对、非线性greedy/阶段反退及scale布局自由度的具体边界。仅拟现有短段之后一段，不新开H3，不写完整动态recipe。

完整直接上锚：
> 按平均负载固定 expert placement 在设备稳定时合理；频率、干扰和通信带宽变化后，同样 token count 会产生不同完成时间。runtime 应用 measured service rate 更新 expert-to-device mapping，并限制迁移频率；收益是降低 straggler，代价是测量噪声、迁移成本与控制震荡。变化慢时保留静态映射。<!-- source-family:SF-2026-ARXIV-2605-19945 --> exact-v1 §3–5 只支持作者设备与模型，§6 不证明所有 variability 都能在线补偿。

拟新增完整单段：
> 平均速度还可能掩盖负载强度的影响：名义相同的 GPU 在接近功耗上限时可出现不同耗时曲线，应在固定 kernel 与执行条件下逐卡校准 token 负载到耗时，再结合每层 expert demand 估计最慢卡完成时间，而不只均分 token。[ViBE 的受限对照](https://arxiv.org/html/2606.00735v1#S5)支持这条放置分支，但单点速度生成的 greedy 布局不保证非线性目标最优；低负载或 Decode 中，热点同卡的内存/通信争用还可能使其反退。纯量级变化不一定改变路由向量角度，因此仅有 cosine 漂移信号不足以签发 profile 仍有效，实际耗时误差与搬迁尖峰须另验；这里不采用其尚未闭合的完整在线增量 recipe。更多 EP 设备也会减少每卡专家数和放置自由度，逐卡 profile 投影不能当大规模服务实测。采样、校准、规划、迁移与回归全计费；条件失配或净收益不足时，保留原 token-balanced/static placement 与独立 SLO 压测，不改 router 语义或授普遍加速。<!-- source-family:SF-2026-ARXIV-2606-00735 -->

完整直接下锚（标题及首完整段）：
> ### MoE 并行形态从部署配置演进为运行时状态
>
> 当请求并发长期稳定时，部署阶段固定 tensor parallel 或 expert parallel 是合理的：它减少运行时重排并让容量规划可预测。约束变化在于 MoE decode 的并发会连续跨越两种并行方式的优势区间，静态选择会把阶段性通信瓶颈固化。因而调度状态需要增加并行形态、切换阈值、byte-identical expert weight/KV 的固定地址映射和 in-flight request epoch，由运行时只在 decode step 边界提交切换。论文在 8×H200、Qwen3-235B-A22B 上报告 215–434 ms 切换、2.4% memory overhead 与 RL rollout 1.16–1.25× 吞吐收益；这不证明未测模型、互联、并发轨迹或生产 tail latency 下仍安全。切换成本、地址一致性和抖动是新增 failure mode；证据不足或状态校验失败时继续使用静态 TP/EP，旧路径与动态路径按稳定性区间共存。

拟本人Review note待新授：`SF-2026-ARXIV-2606-00735` — Daily2026-06-03补Jun02，exact-v1 §3–5/T2、必要A.2/Alg1–2，2+2+2=6；仅逐卡负载条件耗时/EP placement的静态分支及实际反侧。保单节点FP8/阶段模拟、低QPS/Decode反退、单点greedy非全局最优、cosine量级盲区、incremental文字前后未闭、迁移尖峰与rack投影非实测及全费，不采动态完整recipe/质量等价或通用SLO；未核像素/代码/复现。当前Source/actualowner/PRE待唯一reader，不预写入/POST。

**有界停点：** 00735单篇必要Source/6分/actual-owner具体差额、最小单段与完整直接两锚保存即交root和唯一reader，未预PASS/I/DAY；下一00674尚未本轮notice/Methods/评分/actualowner。仅本节与必要HTML，不改共享Books/Report/State/index，不stage/commit/push；ready释放准备阶段。

## 00674 Outcome Optimization — 必要Source与中心争议提案 / 3+1+2=6

2026-10-25同日Jun03恢复：root通知00735经R124/126必要及实际Ch56唯一POST生效，行政由root同步，不第三。启动重读AGENTS、当前Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP、本2026 State及B6精确停点；R26/R28完整AB准入/联合Jun02日证复用，不重复GET日期或以submitted/registered单字段叫公开。只本日，未变Books方法上下文复用本人前轮实际完整阅读；本轮actual读Ch31终值/trace与PRM完整相关段。只本必要包writer，不改共享Books/Report/State/index。

[exact-v1](https://arxiv.org/html/2606.00674v1) / [保存HTML](SUP_MODEL_B6_2606.00674v1_20261025.html)。当前[官方abs](https://arxiv.org/abs/2606.00674)实际所见唯一v1，无withdrawn/removed/erratum提示，不保证所有渠道没有纠错。必要实际读§3全部定义/假设、§4.1–4.3三theorem及其直属完整proof/Remark1、§5.1–5.4/T1/必要probe文字与图注、Limitations；针对实验是否支持中心claim只追加A.1–A.2与B硬件说明，未读外部参考证明/图像像素/代码或复现。并非按附件数量扩读。

原准入的潜在命题是：训练reward被shortcut筛蔽时，同支持域增样本不消除OOD风险，过程监督可能改变可行解，而不只是密集credit。若有有效条件定理，这会改变对ORM/PRM的设计判断；D3、Reach1（一个训练监督/表示分析接口，不借所有LLM生命周期加分）、Durability2（监督支持域/验证器条件可复用），总6。中心争议不通过降分/范围排除规避，也不借成熟IB/SCM原理加分。当前提案为**争议/暂缓，无正面Books采用**，仍待唯一reader首次必要独核，不预本窗终态或DAY。

### 必要原主张与证据

§3设X=g(C,S,noise)，C是不变推理结构、S仅在训练分布预测标签的捷径。Assumption1是训练reward R⊥C|S、OOD失效；Assumption2是学习S的optimization complexity远低于C。§3.3明确`−I(Z;R)+βI(X;Z)`是概念surrogate而非真实训练loss，不把它替换成已证SGD或RL动力学。原theorem目录称“inevitability”，但Th1正文仅称训练**admits** reward-sufficient shortcut-dominated Z≈h(S)。它给定这种表示后I(Z;C|S)=0/近似小；这个条件信息不等I(Z;C)=0，因为S本身可携带C信息。Proof从样本复杂度不对称跳到具体optimization偏好，没有真实SGD选择概率、收敛轨迹或近似ε界，不能由此证明必然坍塌、C物理消失或全部outcome RL均有同一机制。

Th2定义商空间Ω/∼（同causal logic为一类）及任意概率measure μ，以训练shortcut在各类非spurious的覆盖η度量，接着对OOD风险按η/1−η分区，主张R_ood≥(1−η)δ且不随N消失。按全概率将风险分区本身合理，但必须证明η就是该OOD人口中aligned区域的概率，原μ与D_ood没有这样的明确对应；“同逻辑”也不自动意味着shortcut关系类内恒定。Eq6直接写misaligned期望loss≥H(Y)+KL(Ptrue||Pshortcut)>δ>0，未先定义loss为何种proper score/条件分布、δ从何来；独立或错误相关不单独给任意loss的正熵下界。交叉熵特例的熵/KL分解也不能无条件代任意classification risk，更不能在η可变而未估的情况下成为真实LLM泛化证书。**需要保留的双方是原Eq3–7主张与缺失前提，不自行补成已经成立的coverage定理。** 若另行假设misaligned区域确有固定δ下界，则Eq7只是由这些假设推出的条件分解，不证明本文的SGD/语义定义会满足它。

Th3先以`max Σ_t I(Z_t;R_t)`定义process目标，proof Step1/Eq8却换成`Σ E log P(R_t=1|Z_t)`，未给二者等价。最大化正确标签似然与最大化互信息不是同一目标：当R_t恒为1，完全正确亦有H(R_t)=I(Z_t;R_t)=0，故“正确链必满足每步I>ε”需额外随机性/测量定义，不能由正确性本身推出。Step2从S低复杂度直接说它缺乏足够entropy生成合法链，又用I≈0推高step loss；这两步均需附加条件。低复杂度的有效算法可产生正确多步过程，表面步骤也可能与verifier共用捷径。即使假设某S不能通过每步验证，也还需写明policy class、可达正确链、loss/权重与全局最优条件，才可证明全部PRM最优解与该shortcut集合不交；有限实际optimizer更未因此被“迫使走到C”。

Remark1另称generator/verifier failure modes不完全对齐、流形disjoint或orthogonal即可避免joint collapse，但未定义可检验角度/失效事件及其如何控制全部joint error，没有独立定理证明“异构PRM就安全”。不把这段话当oracle问题已解决，Limitations本身也承认所需逐步互信息verifier昂贵且难构造。

### 有限实验不能补中心证明

§5/T1给Qwen2.5-3B/7B、Llama3-8B的ORM/PRM对照：472个solvable样本，5次run均值/误差；标准准确率和反事实准确率的差在3模型均较小。A.2说明从MATH test500去掉unsolvable至472，同一保留子集生成对照，Gemini2.5Pro改算术规则并重写；不是无语义变化的普通paraphrase。作者称保持原结构，但未给足逐题人工audit/反事实gold生成校核与去除准则，生成器或筛选偏差仍影响结论。A.1只给LLaMA-Factory与“official defaults”、probe用EasyR1；没有本必要原文足以核对的具体训练数据/过程标签、ORM/PRM优化算法与reward消费、训练步数/曝光预算或精确revision，不能从框架名称推定是真实等预算outcome-RL与process-RL因果试验。

T1可作为作者报告的有限描述，不足认证Th1实际因果、Th2与N无关下界或Th3拓扑过滤。§5.3以重命名符号/运算正交probe测试S/C，只有单run（A.1明确）；线性probe低准确不等隐藏态绝对没有C，也不估I(Z;C|S)或内部因果必要性。实验只是3B/7B/8B与人工规则反转，Limitations也限定不能外推frontier或真实捷径。B说明4×A10080GB、PyTorch/Transformers；precision、输入输出长度/采样/训练总费用与完整配置未披露则Not Disclosed，不能借默认值补齐。构造/筛选、监督、训练、多run、probe与验证全计费，不据有限表格批准PRM普遍更省或已排除捷径。

### actual owner与采用边界：不是NC，不新增PRE

唯一候选owner为 `TRAIN-RLHF` / [Ch31](../../../../../books/part-04-training-system/31-rlhf.md)。本轮实读“Outcome相同也可能走了错误Trace”、终值checker/保义双检及“Process Reward必须携带有限证据强度”的完整相关段。实际已有终值与trace、局部reward与最终outcome分责，但**没有本文声称的η风险下界、强制PRM解集分离定理**；因此不能说该中心理论已具体覆盖从而躲开争议。

当前actual的有关边界（完整段）：
> 证据更强还不能修复目标排序本身的错位。令某段 history 为 `h`，`Q_proc(h,a)` 表示选择动作 `a` 后按定义续行的累计 process 价值，`Q_out(h,a)` 表示最终 outcome 价值；若要任意 process 最优选择都保 outcome 最优，就须有 `argmax_a Q_proc(h,a) ⊆ argmax_a Q_out(h,a)`，不能只要求存在一个共同最优动作。把错误终局动作与正确动作并列最高 process 分，同样不满足这条条件；局部步骤分数提高或 concentration 增大也不证明累计排序已经对齐。[受限形式化分析](https://arxiv.org/html/2610.23051v1)只在明确的历史、动作及目标条件下支持此边界，不保证真实 PRM 满足它。实际系统仍需付 continuation、独立 outcome 与排序校准费用；无法检验目标兼容性时，保留标量 PRM 作为搜索提示，终态验证与固定预算回退另行负责，不把 process 最优当作成功证明。<!-- source-family:SF-2026-ARXIV-2610-23051 -->

此段不是用于替本文背书或判同事件重复，只说明不能用“PRM是更密集反馈”通用段落绕过具体理论gap。原准入、6分和有限实验全部保留；中心bound/filter当前隔离为未采用的作者主张，不以它支持Books、普遍性能/安全或覆盖结论。不产生最小PRE/新末注，也不为制造diff只加理论警告。

**精确重开条件：** 取得针对exact-v1理论的作者勘误/补证或可核严格替代证明，至少闭合：(1) μ与OOD人口/等价类良定义、loss与统一δ及适用预测族；(2) MI目标与实际process loss的关系、R_t取值人口、verifier soundness与全部最优解排除条件；若仍主张真实optimizer坍塌，则需Copt到其动力学的连接。若拟改采有限实验因果，另需具体ORM/PRM训练/标签、等曝光预算、472gold/audit与probe协议，而不是再给一张同均值表。替代证据只恢复对应子命题，不全盘重跑已有效准入/date；本轮原件已足解释争议，非访问故障，不无限追附件/代码。

**有界停点：** 00674必要Source/6分/actual-owner与中心争议、采用隔离及重开条件已保存，立即交root和唯一reader，未预争议终态通过/I/DAY。下一00654尚未本轮notice/Methods/score/actualowner；不改共享Books/Report/State/index，不stage/commit/push，ready释放本准备阶段。

## 00654 Invitation Trap — 必要Source与actual-owner最小PRE / 2+2+2=6

2026-10-25同日Jun03恢复：root通知00674 R128中心争议已正式隔离采用，不第三；其有效原证与重开条件保留。启动重读AGENTS、当前Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、完整ROADMAP、本2026 State、MODEL末节/B6精确停点。R26/R28完整AB准入及联合Jun02日证复用，不重复GET/日期证明。未变PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE复用本人前轮实际完整阅读；当前Ch72 trigger邻域/上下分支、Ch71/73开篇职责实际读。只本日必要包writer，不改共享Books/Report/State/index。

[exact-v1](https://arxiv.org/html/2606.00654v1) / [保存HTML](SUP_MODEL_B6_2606.00654v1_20261025.html)。本轮[当前官方abs](https://arxiv.org/abs/2606.00654)实际所见唯一v1/29pages，无withdrawn/removed/erratum提示，不保证全渠道无纠错。必要实际读§3.1/3.3–3.5威胁/交互形式/模拟与部署身份、§4.1–4.3/T1实验与直接消融、§5.1–5.3防御/真实日志代理、§6限制；只为judge可信度追加直属D.2/T7，不读全部payload taxonomy/具体恶意示例、全部prompt/附件、图像像素或代码，不执行攻击或复现。

评分D2（触发机会由受污染助手自己的建议内生地产生，而非只等外部输入；暴露过程须纳入威胁模型），Reach2（助手建议→用户回流输入→输出/动作信任转换），Durability2（诱导/接受/条件触发与effect分开验收的稳定边界），总6。评分不借通用least privilege、人格理论或较高ASR宣传；不是因有backdoor主题就入书或NC。拟只采用这一防守视角的交互边界，不采用完整植入/诱导recipe、认知控制因果或现实攻击概率。

### 必要机制与权限前提

§3.1明确攻击者须先取得模型/上下文污染能力；训练数据污染、RAG/direct instruction/ICL是列举路径，本实验主要为ICL poisoning。§3.5/4.2以BadChain式few-shot上下文部署，8例含攻击成功/失败与benign例，而非本次实测权重训练后门、正常未污染模型自然变恶或攻击者无需初始写权限。后续推理不持续操控不等没有上游控制。本文拟用机制是：受污染助手在回答后给相关扩展/深化建议，用户后续回流输入中的trigger与接受意图共同作为条件；不接受时保持诱导、无关问题保持正常。这样触发暴露不是用户原始分布的固定外生事件。这里仅记录状态关系供防守测评，不保留恶意载荷或可执行攻击模板。

§3.4/4.2两个LLM agent模拟对话，persona只取agreeableness/openness与expertise组合成novice/generalist/expert三类，最大5轮；每方法200 user agents。它们是prompt条件的synthetic population，不是经真实用户分布校准的人格代理或人类易受骗率。§4.1说明主要coding200话题、另两辅助域各100、benign200话题，均由DeepSeek-V3.2生成；医疗/法律仅作安全测评样本，不采领域知识。主backbone也是DeepSeek-V3.2，闭源调用不能补当前API行为不变或原精确revision；硬件/precision/完整采样温度、token/延迟总费Not Disclosed，不从模型品牌补造。

§4.1 Eq3把EASR定义为`AIR×ASR=P(Accept)P(Success|Accept)`；概率链式法则成立须同一目标人口/条件定义。实际§4.2把ecological simulation AIR与few-shot deployment的ASR列为两阶段实验，所读必要域未建立逐条同一accepted conversation到成功输出的联合观测/重权。因此T1 coding AIR78.9%、ASR92.7%、EASR73.1%是作者的分阶段乘积汇总，不自动等实测真实用户joint风险；这不否定存在受限交互路径。Novel exposure loop而非该百分比是拟采用命题。

§4.3/T1去诱导后AIR22%/EASR20.9%，固定动态trigger后AIR15%/EASR12.5%，对本构造支持相关组件的局部作用；对照同时改变可选trigger/适配任务的自由度，不能据此证明所有真实对话中每个组件必需或唯一因果。常见词baseline AIR82.5%还高于PAB78.9%，其ASR/误触发取舍不同，不能把更高EASR说成每个阶段都赢。CACC100%只是作者benign集及judge下的有限读数，非完整用户效用无损；TRR以道歉/修正/重新信任代理定义，不证明实际长期存活或人类已恢复信任。

直接反侧：正文说自然trigger可被模型语义过度解释，隐含引用前文建议也可能算触发，故严格字面匹配与意图接受必须分开审；FPR coding4%不等任意域固定误报。GPT5.1在作者该ICL路径未受影响，Qwen3.5Plus对主payload拒绝又可能在替代payload退步，不能按单样本/可见thought block授内部逻辑识别或所有模型可被同样部署；§6“只在一闭源模型评价”与跨模型小测试可理解为主生态实验范围有限，不把小测试合并为跨模型真实user验证。

### 真实日志与防御并未闭合现实风险

§5.2 WildChat-1M筛选含具体keyword建议的子集N2958、文字称qualified conversations的30%；观察到近半用户接受建议。这是既有真实对话中的接受代理，不含已植入PAB的配对攻击、真实恶意执行或随机总体人口；不能将其与主表ASR相乘当已测真实事件率。D.2作者10%日志样本的多数投票是同作者人审校核，不是独立外部人类实验；T7 PAB-ASR仅30例、人审/LLM agreement93.3%，Real-Life300例agreement87.3%，有限一致不消除judge与合成集共同偏差或给出真实危害标签。

§5.3在500例已知条件比较输入异常、内容/效用guard及Anti-PAB重写接受输入的分支。Anti-PAB用较泛化的接受表达替换原trigger措辞，作者报告阻断已测trigger-matching阶段；但原模型已能把隐含接受解释为trigger，该防御不能据此获得语义trigger、未知适应性PAB或全部正常任务无损保证。本文自身也要求继续研究更复杂变体；不复制其“ubiquitous safeguard/不损功能”的普遍宣传。输入匹配、会话state、模型可见历史与effect gate是不同控制面；模型自己提出的建议和用户同意继续，不自动获得危险外部动作权限（项目防守推论，不冒称论文实现过权限gate）。

所有合成话题、对话、多次模型调用/判分、日志筛选、人审和防御回归都付费；没有净费证据则不称training-free就免费或比供应链防护更便宜。支持与直接反侧已足，只采暴露闭环与验收边界，停止，不继续全部prompt、具体payload、personality附录或artifact。

### actual owner差额与最小逐字PRE（未授写）

唯一 `PLATFORM-SECURITY` / [Ch72“Backdoor Evaluation必须测Trigger邻域”](../../../../../books/part-06-ai-infrastructure/72-security.md)。当前actual已有trigger precision/action propagation/benign utility分责，也有提示中协作拓扑/审阅条件与独立audit；没有助手主动制造建议、用户回流接受使trigger暴露内生化的具体链。不是因同有backdoor词就NC。Ch66已拥有分阶段比例与联合人口的通用测量边界，不在那里再写一次risk公式；Ch72只补此暴露来源/权限边界，Ch71租户与Ch73生产门禁不复制。

完整直接上锚（段及其紧接marker）：
> 邻域测试提高发现泄漏触发的概率，却依赖变换集合和 agentic workflow coverage，可能漏掉更远但语义等价的 trigger。覆盖不足或 executable action 风险高时，应拒绝发布或限制 capability；低风险、无外部动作的模型仍可使用传统 probe 作为第一层筛查。现有证据限论文的视觉语言 Agent 与威胁模型。
> <!-- source-family:SF-2026-ARXIV-2606-12586 -->

拟新增完整单段：
> Trigger 的暴露机会也可能来自已被污染的助手，而非独立用户输入：助手提出下一步建议，用户接受并回流相关表达后才满足触发条件，因此回归应保留建议、接受意图、后续输出与真实 effect 的完整链，分别测暴露、条件触发、误触发及合法任务效用。[PAB 的受限研究](https://arxiv.org/html/2606.00654v1#S4)主要依赖 few-shot 上下文污染与模拟用户，不证明未污染模型会自然产生同一后门；人格 prompt 和普通对话的接受率也不是现实攻击成功率。改写接受措辞只测试已知匹配路径，不能代替语义变体与适应性复验。由此推导，建议的来源与后续动作权限仍须独立核验，用户同意继续不替模型建议授予危险 effect；会话重放、独立标注与防御回归都付费。污染来源、用户人口或真实后果不可核时，保留原输入/建议与 Unknown，限制外部 capability 并人工确认，不由高 clean accuracy、道歉或一次 trigger 改写签发长期安全。<!-- source-family:SF-2026-ARXIV-2606-00654 -->

完整直接下锚：
> Trigger 还可绑定提示描述的协作拓扑和审阅条件，而不只是任务字符串：在任务字节相同的条件下交叉改变单体/多体及有无人工审阅，再加入拓扑术语 placebo，能检查可疑适配是否只在特定上下文改变行为。[受限后门对照](https://arxiv.org/html/2610.05793v1)支持这种描述条件触发，不证明真实多 Agent 环境会自然触发或所有协作都危险；独立 bandit analyzer 的检出率低于任务专用 checker，广窄信号对照还混入训练量差异。二元审计在 clean control 上也有高假阳性，不能把猜中一次触发叙事当可靠检测器。适配来源、触发邻域、配对任务、真实 effect 与独立审计须共同保存，全部训练/重放和标注计费；覆盖或误报未过时保留来源门禁、受限 capability、人工核验与 Unknown，不由未触发或一次审计批准安全发布。<!-- source-family:SF-2026-ARXIV-2610-05793 -->

拟本人Review note待新授：`SF-2026-ARXIV-2606-00654` — Daily2026-06-03补Jun02，exact-v1 §3.1/3.3–3.5、§4/T1、§5–6及必要D.2/T7，2+2+2=6；仅被污染助手主动制造trigger暴露的交互链与独立effect权限。保ICL/模拟人口、分阶段乘积非实测joint、WildChat接受非攻击、模型/载荷切片差异、隐含触发与重写防御边界及全费，不采现实ASR、永久防护/无损或内部机制因果；未核具体payload/代码/像素或复现。当前Source/actualowner/PRE待唯一reader，不预写入/POST。

**有界停点：** 00654必要Source/6分/actual-owner具体差额、最小单段及完整直接两锚已保存，立即交root与唯一reader，未预PASS/I/DAY。下一00651尚未本轮notice/Methods/score/actualowner；不改共享Books/Report/State/index，不stage/commit/push，ready释放本准备阶段。

## 00651 MESA — 必要Source与actual-owner最小PRE / 2+2+2=6

2026-10-25同日Jun03恢复：root通知00654经R131按actual Ch72同family完整两段具体NC正式采用，撤原新增PRE，原6分/日期与必要Source不变；本节只记录新停点，不第三其有效层。启动重读AGENTS、Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、完整ROADMAP、本2026 State及MODEL/B6停点。R26/R28完整AB准入与联合Jun02日证复用，不重复日期GET。未变Books方法上下文复用本人前轮实际完整阅读；当前Ch21功能/负载/编辑相关主干、Ch20/22开篇交接与Ch72路由攻击面实际读。仅本日必要包writer，不改共享Books/Report/State/index。

先定点查Books精确`2606.00651`/family marker及MESA，未命中现有正文；本日旧必要记录也没有其已完成Source。随后文件名定点恢复发现`papers/2026/05/_sources/daily-20260531/exact-v1-html/2606.00651.html`旧raw，本次HTML与之`cmp`逐字相同；该旧目录Markdown定点查00651/MESA无审读判断命中。旧raw可作原件复用，不等有效审读链、同事件已审或旧日期有效，不扩读May31其他研究。因初次文件名查只限本日未命中，本轮已另保存同字节HTML；不再次GET有效正文。

[exact-v1](https://arxiv.org/html/2606.00651v1) / [本日保存HTML](SUP_MODEL_B6_2606.00651v1_20261025.html)。当前官方abs的浏览接口失败一次，改用官方同URL直接读取成功，见[保存abs](SUP_MODEL_B6_2606.00651_ABS_20261025.html)：唯一v1，所见无withdrawn/removed/erratum，不拿HTML可读替代notice核验。必要实际读§2.2、§3.1–3.2、§4.1–4.2/T1–4、§5及直属B限制；为比较预算只追加E/T5。未采用两理论bound或最大熵推导，因此不扩C/D/F证明、全部超参/图像像素/代码或复现。

评分D2（把专家更新域选择与双流router目标配对，改变只加强原safety head或全专家统一更新的选择），Reach2（expert适配与router消费路径/安全-效用回归共同接口），Durability2（频率代理、选择与实际路由/回归分责可复用），总6。不借通用OT/低秩/曲率理论加分，不因小模型、已有MoE主题或Books决定改分。采用是受限训练分支，不采“安全能力已被严格去中心化”“tail必脆弱”或生产防护保证。

### 核心训练机制及可支持范围

§2.2/3.1用安全/一般输入的expert激活频次排序作代理，主张只加强安全高频head收益受限、极低频tail适配也可能损害效用。成本曲线偏向mixed排序的shoulder，用shifted Beta-rational形状作选择代价；这是原启发式设计及有限组间对照，不把激活排名授专家真实语义，也不认定β形状唯一最优或最大熵论证已验。Th3.1参数更新下界依局部假设，Th3.2退化上界还额外假设曲率随稀疏度超线性增长；上界大本身不证明所有tail实际损失必爆炸。本采用不依赖这些定理为一般MoE担保，未核其全证明，不在正文传播其普遍因果说法。

§3.1.3以base经验activation prior为参照，成本加KL正则的transport提案决定高值expert子集；§3.2安全输入用非零cost形成偏向所选容量的软router目标，一般输入cost置零，目标退回冻结reference router分布。选中expert的安全SFT与router KL共同训练；这把“哪些参数学安全”和“输入能否到这些路径”分开设计。此处dynamic是训练时输入条件目标，不是额外部署实时OT solver或放置控制器。原Eq7矩阵L×N与polytope B×N/marginal符号、Top-w到具体更新mask的实现资格尚不足拷为完整执行recipe；只采可解释的选择/目标配对，不补行列边际、零prior处理或保证无mode collapse。

§4.1安全/一般数据各15K、合计30K；统计子集各500共1000。实际两个backbone是DeepSeek-V2-Lite与Qwen3-30B-A3B，judge为Octopus-SEval-14B安全率和GPT4.1一般任务准确率。E/T5给8×H20-141GB、ZeRO3、bf16、maxseq1024、globalbatch256、AdamW/TRL。MESA LR1e−4/500steps，SFT2e−5/500、GRPO1e−6/250且选90step饱和checkpoint、SafeX LoRA r16/1e−4/500；STAIR还换含reasoning的数据并增加30K偏好对/DPO300。相同30K条数/部分相同步数不是等训练曝光或compute/LR/监督，不能由跨方法均值唯一归因OT。§3称SFT只读safety stream，而E/T5把MESA train data标mixed/full finetune；不据“full”补成所有expert都更新，也不冒称精确gradient mask已实现核验。本文没有给足重复seed/区间和完整token/latency净费，Not Disclosed。

### 关键对照与直接反侧

T1 DeepSeek MESA较base在多安全slice和GSM8K改善，Qwen也在部分安全/代码slice改善；但Qwen MBPP+75.60→69.40、GPQA-D54.04→49.49、MMLU80.15→79.31，不能叫无alignment tax或全任务无损，Qwen SR-Pair90.73还低于部分baseline。正文把SFT Strata92.00误叙为77.70（后者是WildJB列），采用表头/表格，不以叙述数字替表作保证。

T2分别只调router、调全部expert、所选expert、所选expert+router与完整方法，支持组合责任需分账：只router在Qwen Strata88→78及一般任务反退，说明改流量不自动给expert安全能力；所选expert+router也不是每项都优于expert-only。T3的E_OT相对middle-rank选择有局部优势，但T2/T3重复命名E_ALL等分数不同，完整MESA与E_OT+Router的具体额外preservation/配置不可仅由标签补齐。T4 shift选择有模型/任务依赖，不能宣称一个最优曲线通吃。只采用训练分支和有反退的有限证据，不授精确配方/各组件普遍必要性。

§4.2/F4在随机mask、按R_safe高频mask及路由攻击下有受限韧性结果；屏蔽专家是结构干预，不等真实攻击都会避开同一组，Top5/10、mask层/攻击预算和剩余效用都应绑定。DeepSeek F-SOUR该设置观测ASR0不等没有未知攻击或真实环境安全；不运行/复述攻击构造。§5专家overlap变化是行为/使用代理，低overlap不证明没有某能力，高overlap不证明安全知识已因果写入coding expert。

B称OT开销training-only且墙钟可忽略、推理保持稀疏执行；保留Top-k数量不保证dispatch负载、内存通信或end-to-end latency原样，需另测。统计/solver/reference、候选专家适配、路由训练及完整安全/效用/负载回归均付费（项目验收推论），不由solver迭代快自签零总费。有限16B/30B、固定数据与judge不认证更大MoE、未知类别或部署同效。支持与直接反侧足够，停止不以理论标题扩全附件。

### actual owner具体差额与最小逐字PRE（未授写）

唯一 `MODEL-MOE` / [Ch21“为什么负载均衡是模型正确性的一部分”](../../../../../books/part-02-model/21-moe.md)。精确family及MESA全Books定点未命中，不以没有marker自动判gap：实际读COAX软容量prior、CNN-MoE鲁棒性、activation≠routing sensitivity和MoEEdit保留完整段，现有机制分别处理可学容量、诊断和编辑preservation，没有按适配代价提出expert更新集合、并对安全/一般输入设置不同router目标的训练配对。Ch29拥有通用SFT数据/更新训练，Ch72拥有输出/工具权限与路由攻击诊断，不在那里复制该MoE内部容量训练设计。只在现CNN-MoE反侧marker后加一段，再接“同样，某expert…”的频率诊断，不新开论文H3。

完整直接上锚（完整段与紧接marker）：
> 负载是否均衡、单个expert在受扰输入下是否可靠，以及带router的完整模型是否可靠，也不是同一判断。一个[受限CNN-MoE对照](https://arxiv.org/html/2509.05086v1)在对抗训练后观察到路由集中，同时某些固定expert的受扰准确率高于原gate组合；这提示router可能未选择最耐受的路径，不证明集中本身有益、均衡必然有害，或该结论可迁到语言MoE。应在同一明确攻击与输入人口下分别验clean质量、固定子路径、原gate系统、负载和实际执行费，并核清攻击是否适配被测forward；子路径的较好读数不能替整模型取得安全资格。专家曝光、auxiliary权重、位置、激活数量与对抗训练全部计费，有限FLOPs也不等完整latency；受扰质量、负载或原任务回归失败时，保留原router/均衡约束、已验证dense路径与独立质量门，不从少数专家被频繁选中推导其语义身份或防护保证。
> <!-- source-family:SF-2025-ARXIV-2509-05086 -->

拟新增完整单段：
> 若要扩大可承担安全行为的路径，训练还可把专家更新域与路由目标分开后配对：从安全/一般输入的经验使用排序提出适配代价，以原 activation prior 约束的重分配选择待更新专家；安全流让 router 接近重分配后的软目标，一般流则约束它接近冻结 reference 的原分布。[MESA 的有限对照](https://arxiv.org/html/2606.00651v1#S4)支持这条选择与路由共同适配的分支，却不把高频、shoulder 排名或代价曲线变成专家语义真值、普遍曲率定律或最优更新集合。只改 router 不自动产生安全能力，保留一般流目标也不保证旧函数不变；部分安全和效用切片仍会反退，mask 韧性与零观测攻击成功都不授全面防护。统计、参考前向、求解、专家/路由训练和独立回归全计费，Top-k 数未变也须另验负载与实际执行费。数据、分配或安全/效用验收失配时，保留原 router、已验证的局部或普通对齐与输出/动作门禁，不由路由更分散批准发布。<!-- source-family:SF-2026-ARXIV-2606-00651 -->

完整直接下锚：
> 同样，某 expert 在一个领域中经常被选中，并不等于它对该领域输出最重要。可以在固定输入与冻结模型下分账测量：先记录原 router 的选择频率，再对某个 expert 的 pre-softmax gate logit 作规定幅度扰动，观察输出分布 KL 的变化。[受限 MoE 探测](https://arxiv.org/html/2601.10159v1)因此把 domain activation 与 routing sensitivity 配对，而不是用热门 expert 直接命名“数学专家”。后者仍是局部扰动敏感性：logit 改变可能同时改变 Top-k membership 和其他 expert 的相对权重，不能视为隔离单 expert 功能的因果干预。<!-- source-family:SF-2026-ARXIV-2601-10159 -->

拟本人Review note待新授：`SF-2026-ARXIV-2606-00651` — Daily2026-06-03补Jun02，exact-v1 §2.2–5/T1–4、必要B/E/T5，2+2+2=6；只采expert更新域与双流router目标的配对训练分支。保rank/overlap代理、理论不作担保、跨方法预算/标签差异、全参/mask未核、切片反退和Top-k不授执行无损及全费，不采普遍去中心化安全/曲率或完整OT实现recipe，未核proof附件/像素/代码/复现。当前Source/actualowner/PRE待唯一reader，不预写入/POST。

**有界停点：** 00651必要Source/6分/actual-owner具体差额、最小单段及完整直接两锚保存即交root和唯一reader，未预PASS/I/DAY；下一00600尚未本轮notice/Methods/score/actualowner。不改共享Books/Report/State/index，不stage/commit/push，ready释放准备阶段。

## 00600 ReBias-Lens — 必要Source与actual-owner最小PRE / 2+1+2=5

2026-10-25同日Jun03恢复：root通知00651 R134/136实际Ch21整合已生效，行政由root同步，不第三。启动重读AGENTS、Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、完整ROADMAP、本2026 State与MODEL/B6停点。R26/R28完整AB准入与联合Jun02日证复用，不再GET日期。先定点精确family/ReBias查全Books及本日必要记录，无已成Source/实际正文命中；2026文件名查只有不同月份的00600日期文件，不因短号相同扩读或判重复。未变PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE复用本人前轮实际完整阅读；当前Ch66相关完整段、Ch65/67职责与Ch80反思边界实际读。仅本日必要包writer，不改共享Books/Report/State/index。

[exact-v1](https://arxiv.org/html/2606.00600v1) / [保存HTML](SUP_MODEL_B6_2606.00600v1_20261025.html)。[当前官方abs](https://arxiv.org/abs/2606.00600)本轮所见唯一v1，无withdrawn/removed/erratum提示，不保证所有渠道没有纠错。必要实际读§3/ Eq1–3、§4设置及RQ1–3/Eq4/T1–2/相关图注、Limitations；只为运行身份追加B。F reflection instructions仅图注，未看图像像素，因此不声称已核全部精确prompt/treatment，不据此采用唯一机制因果；不扩全部seed词/分类表/代码/复现。

正式评分D2（将整体投影离散度与组别标准化差异分开，改变“全局变平即逐组消偏”的评价选择），Reach1（局部模型表示/行为测量，不借公平治理全生命周期加分），Durability2（scale、构念代理与逐组effect分责可复用），总5。不因四模型或社会公平主题加分，不把SVC成熟模块组合本身算贡献；原准入的宏观改善/局部反退具体证据仍值得采用，但收窄为测量边界而非自反思内部机制定律。

### 必要机制、指标对象及有限结果

§3.1对固定中性属性词的上下文替换对立社会类别，前一阶段刻板/快速回答，后续加入反思；§3.2从25pleasant/25unpleasant seed训练linear SVC，以权重方向v对属性词hidden作`u(E)=E·v`。这是valence投影代理，不是全部偏见的真实强度，也非自动获得因果/公平标签。原文称scalar projection但式中未除v范数，按实际dot product理解，不自补归一recipe。

Global-VF Eq2是全交叉context投影相对中心的均方离散度（原σ如此定义，不改成标准差）；Local-VF Eq3是两组投影均值之差除两组pool的标准差，带方向，绝对值大被作者解释为更强association。二者对象不同：若所有u同时变为a·u+b且a>0，Global均方离散度变a²倍而Local保持不变（直接代数推论，不是作者已经完成该干预）；因此global更平不逻辑推出逐组标准化距离更小。分母为零/极小或projector尺度改变须另有处理规则，不能静默改成公平改善；本次不复制未披露的数值阈值。

§4四个7B/8B instruct模型（Llama3/Llama3.1/Mistralv0.3/Qwen2.5），12类Western社会属性的二分组合；不是全球群体本体。T1用Bellezza valence词典相关性选last-subword而非mean/max/first，作者相关系数约.75–.87。这个lexical validation支持情感读出，不验证context组合、公平行为或跨层同尺度；同词典选pooling并报告相关也不是完全独立的迁移评估。每层/模型的projector、提取位置、tokenization与尺度需绑定（项目测量要求），不由SVC名称保证可比。

T2三种E1/E2/无外部指导W/O提示下平均Global-VF相对降幅约73–88%，§4.3报告Local绝对值下降的实例比例约53–70%，并指出若干类别局部反退。这支持本文有限测量中“总变平与局部残留/增强可并存”，不等真实偏见下降同样百分比或所有反思均有效。所谓W/O仍为反思条件，不是无prompt/等上下文长度控制；额外指令、话轮、位置与任务本身可同时改变表示。F精确模板未读，不采用E1/E2语义等价、纯格式已排除或内部slow/fast机制唯一因果的更强说法。

§4.2从连续后层Global低于baseline识别l*，在l*±3窗口逐层独立zero weights；proxy对这类局部ablation相对稳定，是该干预/读出下的观察，不证明“分布式反思机制已识别”、其他层无作用或深层普遍更鲁棒。没有等范数/替代读出与完整任务损伤控制，不能把读数变化或不变化独归消偏回路。§4.3对每类从2^11=2048属性pairs抽1000，bootstrap1000次并给95%CI，区间是属性样本人口而非训练/模型seed不确定性；共享属性、多个类别/提示/层比较不能自动当独立重复或同时有效检验。

行为侧的中性选项迁移与拒答不同：§4.1本身说Llama3.1某提示拒答、另一提示直接答，较低VF可同时出现两类输出。选择中性、拒绝回答、真正无不当差别或开放生成公平性不能互换。原文局部选项例子仅有限受控问题，不采身份类别的实际心理/社会判断，更不把hidden投影相关当部署歧视或公平特性因果。Limitations明确只有单类别切片分析、valence一维而非competence/warmth多维，并限discriminative任务，未验长程/开放生成。

B给Transformers、temperature0、单RTX3080、single run；precision、完整输入输出长度、模型精确revision、统计/生成净费Not Disclosed，temperature0不消除pipeline、prompt或测量构念的不确定性。Seed/lexicon准备、hidden采集、SVC/层窗消融、各提示重复调用、bootstrap与行为/人工回归都付费。必要支持与直接反侧足够，停止不追全部图像/附件或具体biased例句；未声称复现或内部机制已核。

### actual owner具体差额与最小逐字PRE（未授写）

唯一 `PLATFORM-EVALUATION-SYSTEM` / [Ch66表示/偏见测量邻接](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。精确family/ReBias全Books未命中后，实际比较现跨语审计完整两段：它已有“均值趋中可能逐item重排、配对方向/距离和本地标签”及token计分边界，不重复通用“平均值掩盖切片”。尚无**hidden valence总离散度与组别标准化effect在统一scale变换下不同、projector与行为公平分账**这一具体接口。Ch80拥有反思候选/独立验收流程，本项不新增reflection控制算法；Ch65/67不接收模型公平性定义。不新建H3，只在完整跨语审计两段后补一个窄段。

完整直接上锚：
> 这一审计还依赖scorer真正读到了被比较的内容：从数据metadata重建候选角色，不由选项顺序猜标签；按完整输入的字符offset核对continuation边界，并decode实际计分tokens，防止首个差异token被漏掉。逐token平均似然的归一化分数不是回答选择概率，也不能混用成另一benchmark的官方分数。[受限跨语审计](https://arxiv.org/html/2610.20479v1)只覆盖所述量化小模型与翻译人口，翻译judge、重述和配对统计都增加成本；缺少native审校，不能把模型关联变化与翻译构念变化完全分离，亦未测量化效应或生成行为公平性。对比单位、翻译对立或评分边界不稳时保留原始item、分项结果与人审，不由更低总分批准消偏。<!-- source-family:SF-2026-ARXIV-2610-20479 -->

拟新增完整单段：
> 用内部表示审计反思前后变化时，还须区分全体投影的离散度与组别标准化差异：由情感词训练方向、对属性词 hidden 做投影，得到的是 valence 代理，不是公平真值。[ReBias-Lens 的有限诊断](https://arxiv.org/html/2606.00600v1#S4.SS3)观察到全局波动下降仍伴局部类别反退；从其指标定义还可看出，统一正比例压缩投影会降低全局均方离散度，却不改变组均值差除以联合标准差的 effect。因此 projector、层/位置、尺度、词表与分母须共同冻结或重新校准，再分别验逐组读数、真实回答、拒答及独立公平标签。单次模型运行和局部层消融不识别唯一反思回路，中性选项增加也不认证开放生成已消偏。表示采集、投影/消融、提示与行为审校全计费；构念或对照不稳时，保留原配对题、分项结果与人审，不由更平滑的 hidden 读数批准公平发布。<!-- source-family:SF-2026-ARXIV-2606-00600 -->

完整直接下锚（完整段及紧接marker）：
> 本地考试题与翻译题并列时，还要把语言自然度、知识答对与多选协议分开：同一道题删除一个错误选项，候选支持与均匀猜测基线已改变，准确率提高不表示模型多掌握了知识；按年级划难度而选项数量也随年级变化时，更不能由总分差独归课程或文化。[受限原生语言评价](https://arxiv.org/html/2509.03162v1)同时提供这种选项干预和原生、翻译题的语言审核，但后者比较不同题源，只评流利度与术语，并不认证答案正确或排除难度混杂。应共同保存原题、删选项规则、候选数、题源/年级、翻译审校人口及likelihood或生成解析协议，分别报告配对协议变化、语言质量与答题结果；相关性也不代概率校准。标注、翻译、额外配对调用与解析回归均有费用，样本、计分器或本地审校资格不齐时，保留原始协议、逐来源结果和独立人审，不用一份更自然的题库或删选项后的高分签发通用跨语能力。
> <!-- source-family:SF-2025-ARXIV-2509-03162 -->

拟本人Review note待新授：`SF-2026-ARXIV-2606-00600` — Daily2026-06-03补Jun02，exact-v1 §3–4/Eq1–4/T1–2、Limitations及必要B，2+1+2=5；仅valence总离散度/组别标准化effect与行为公平分责，scale关系标明代数推论。保单run/一维probe/12Western二分属性、拒答/选项非公平、额外prompt及局部消融非唯一机制、bootstrap非多seed和全费；未读F图像精确treatment/代码或复现，不授普遍消偏。当前Source/actualowner/PRE待唯一reader，不预写入/POST。

**有界停点：** 00600必要Source/5分/actual-owner具体差额、最小单段及完整直接两锚保存即交root与唯一reader，未预PASS/I/DAY；下一00570尚未本轮notice/Methods/score/actualowner。不改共享Books/Report/State/index，不stage/commit/push，ready释放准备阶段。

## 00570 参数知识编辑的相对几何风险 — 必要Source与actual-owner最小PRE / 2+2+2=6

2026-10-25按root接续：00600 R137/139真实Ch66已成，00651/00654/00674既成层不第三读；00570的完整题摘准入与Jun02联合日证沿R26/R28和原件复用。启动读取AGENTS、当前Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP及本日README/State与MODEL/B6精确停点；owner提案前读取PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、实际Ch5知识编辑整组及Ch4/6交接、Ch66相关测量段。仅本必要包与原始HTML写权，不改Books/Report/State/index。using-agent-skills用于范围和验证，不引入软件开发流程。

[exact-v1](https://arxiv.org/html/2606.00570v1) / [保存HTML](SUP_MODEL_B6_2606.00570v1_20261025.html)。本轮打开[当前官方abs](https://arxiv.org/abs/2606.00570)，唯一v1，所见无withdrawn/removed/erratum，comments称ICML2026 accepted，不以发表状态证明贡献。原v1 `2026-05-30T06:44:40Z`、精确DOI `10.48550/arxiv.2606.00570` 的findable/registered `2026-06-02T03:54:39Z`及arxiv.content限定查询原件复用；最早Jun02 00Z至登记上界整体落Jun02 BJT，不把提交或登记叫实际公开时刻。无具体早稿信号，不扩假想首发搜索。

实际读§3–6/ Eq6–17、Th4.5与T1–3、必要C.1/C.5/C.6、T33–34、D/T42–43及E/T44–46；图只读caption，不声称看过像素。未读全B谱统计、全部结果附件、代码、原始log或复现。必要命题与直接反侧已足，停止。

### 正式评分与采用边界

原筛选`3+2+2=7`留在原JSON不覆盖。按证据支持的窄命题核定D2（参数改动的绝对大小与相对原表示尺度分责，提出具体诊断/验收边界，不接受普遍不可能性或必然崩溃的设计纠错）、Reach2（参数更新、表示诊断与下游生成/保留验收接口）、Durability2（相对尺度、累积方向和行为有效性分账），共6。调整源于原宏观命题被证据收窄，非为了省深审或配合Books决定；因具体长期gap仍深入核了假设、主要评价和反证。不把已有“须验保留/泛化”、成熟RAG或多模型名单重复计分。

### 几何机制支持什么，不支持什么

中心化参考hidden矩阵`H=UΣVᵀ`的第k方向RMS为`σk/√n`，把编辑后同方向变化`ck`除它，得到`Rk=√n|ck|/σk`（仅σk>0）。相同绝对变化落到较小原尺度方向，相对量会更大；这是分母尺度效应，不是证明绝对扰动能量被放大、该方向拥有语义功能或必然改变输出。Eq11首个分子未取绝对值而右式取绝对值，本次按后文magnitude解释，只采明确的非负比值，不静默宣传符号精确无误。小参数扰动的一阶Taylor解释另依小扰动假设；固定参考基下净变化可望远镜求和，但随编辑数线性增长还须coherent同向累积，反向可抵消。原文承认基会漂移，不能因此推出漂移一定更坏或把线性近似变成长期定律。

§4.4明确大R不是行为失败证明；T2的MEMIT/ROME若干负相关支持局部关联，AlphaEdit各轴未显著、Gen甚至正ρ=.636(p=.0656)，WISE也不是各轴显著。不能由相关或谱尾小直接认定reasoning collapse的唯一病因。本文总结/摘要普遍措辞超过这一可证明范围，本采用不依赖它；不发布“所有参数编辑不可行”的结论。

### 评价身份、关键反证与真实成本

主要基准为ZsRE、WikiData_counterfact及ELKEN，四个7/8B模型并有13/14B验证，EasyEdit；主实验8×A800，C.6 original AlphaEdit另单H20 96GB。Instruct最大输出50token、reasoner1024，以Qwen2.5-72B语义judge判目标一致；250随机样本与人工96%一致是有限audit，不给全部slice真值资格。1/10/100-edit设置取前100items：100次独立单编辑、十组十编辑、一次百编辑，不能当100独立连续流或多编辑顺序复验。precision、完整输入长度/batch/concurrency、seed/区间与完整端到端费用未披露，不补服务SLO。

§3 locality公式表述before/after保持，但C.1正式四轴语义分实为与ground truth匹配；T3 pre-edit locality只有15.50，不能把该低答分全说成编辑损伤。C.5另作before/after token match，pre-edit按定义100，才提供有限行为保留对照；SCR sequential exact-match45.96、WISE67.18、GRACE100，直接否定“SCR每一保留指标都最好”的宽说法。四轴平均把不同对象混合，不能替真实更新/保留/迁移独立验收。

T33 reasoner数学均值base53.47，AlphaEdit百编辑53.12，十编辑53.92；T34较广任务base54.24、AlphaEdit百编辑52.88，且ARC_c87.80→88.05。这些是摘要“全方法持续破坏核心能力”的直接反侧；ROME/RECT百编辑接近零不抹去AlphaEdit相对韧性，也不证明算法在任意数据/调参下必然崩溃。C.6阈值固定.02只试L2=1/10，支持特定实现/模型的敏感性，不证明架构根本不兼容。

ELKEN参数分支由GPT4o转triples、外部memory保留原event文本，存在表示/信息与分解混杂，不把差额全归是否改权重。D给同top3检索增强参数方法，仍不是等训练/推理预算；T43 N10的AlphaEdit+SCR Gen87高于SCR86、N1000 reliability85.3高于84.8，不拼“全轴全设最好”。E的memory100/1000与top1/3/5/10有限扫描不证普遍稳健。§5 latency固定greedy50输出并相对base归一，D T42 AlphaEdit14.07编辑时间与SCR0只是其时点口径；SCR把费用转移到索引/检索、更多context与推理。E的局部MB/秒不补完整索引构建、所有回归、并发、输出长度混合和生产净效益。表示采集/SVD、编辑/调参、全部生成/judge、检索构建与保留回归均须计费。

### actual owner与最小逐字PRE（未授写/未独核）

唯一owner `WORLDVIEW-REPRESENTATION` / [Ch5“参数知识更新必须同时验收获得、保留与泛化”](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。现完整组已有ordered acquisition/retention/generalization、规则/实例层组织、低曲率Bregman保留约束与teacher-forced/free-generation/capability分验；故不重复泛化验收或RAG备选。真实小gap是**小weight更新与相对原尺度的表示变化不同，低方差方向比值及coherent累计不拥有行为崩溃证明权**。Ch66已有事实答分与before/after locality分账，仅在证据保此反侧，不再复制一处正文owner；Ch29不接收一般表示谱风险。

建议仅在规则编辑段后、Bregman约束段前融一自然段，不开论文H3。

完整直接上锚：
> 更新对象还可以是同一规则的公式、文字描述与多个实体实例，而不只是一条事实问法。一个受限分支先以共享的多层更新同时处理规则的两种形式，再把实例更新放在另一个层范围；这将跨形式组织与实例传播分开，测试必须同时保存 form、instance、edited layers、顺序和未编辑行为。[有限规则编辑对照](https://arxiv.org/html/2604.08284v1)的早/中层恢复信号与四种组织方案支持该替代假设，不证明规则唯一存于早层或可逐字照用矩阵更新公式；其 tracing 重复也不是独立规则人口，部分模型编辑可靠性和 locality 仍弱。构造、定位、连续编辑与回归都计费；层范围失配、改写不泛化或关联行为受损时，保留原模型、较小更新与外部 versioned memory/RAG，仍按获得、保留及跨实例泛化验收，不让“更分布式”自己批准参数发布。<!-- source-family:SF-2026-ARXIV-2604-08284 -->

拟新增完整单段：
> 局部改动的参数很少，还不等于表示变化相对原尺度很小：固定参考样本与层，对中心化 hidden 做谱分解后，同样大小的方向变化，除以更小的原方向 RMS 会得到更大的相对变化。[受限编辑分析](https://arxiv.org/html/2606.00570v1#S4)据此提出风险诊断，但小分母不证明该方向语义重要、绝对扰动被放大或输出必然崩溃；连续编辑近似线性累积还要求变化同向，参考基漂移后更不能沿用固定基定律。应绑定样本、层、参考基与尺度，同时检查自由生成、新旧知识和通用能力，而不让谱比值替行为签字。有限实验也有编辑后推理能力近于原模型的反例，检索分支则把费用转移到索引、额外上下文与调用；表示采集、分解、编辑和双侧回归都付费，诊断或保留性失配时保原checkpoint、较小更新或可追踪外部memory，不从局部编辑成功或谱尾脆弱性推出全局无损或参数编辑必然失败。<!-- source-family:SF-2026-ARXIV-2606-00570 -->

完整直接下锚：
> 在继续验收获得、保留与泛化的前提下，编辑也可把保留对象显式放进更新约束。普通 capability loss 的二阶展开若假定 checkpoint 已收敛，可能漏掉非零一阶项；以原模型输出为 reference 的 Bregman divergence 在该 reference 处一阶为零，局部二阶可写为 Gauss–Newton 曲率，再限制更新进入低曲率子空间。[一种受限实现](https://arxiv.org/html/2602.15823v1)用 K-FAC 的分块 Kronecker 近似和阈值矩阵运算避免构造巨大投影矩阵，因而 curvature artifact 必须绑定 reference/checkpoint、保留数据、edited layers、近似与阈值；它不是完整模型的精确非破坏证明。缓存构建、分解、编辑和回归均付费，原 wall-clock 口径未明确全部 offline 成本，不能签端到端普遍加速；有限基准也有单项能力退步。Teacher-forced 编辑成功、自由生成效果与 capability regression 应分别检验，局部近似失配或无法定义可信保留分布时，应回退原模型、外部 versioned memory/RAG 与独立行为测试，不让投影自行批准参数发布。<!-- source-family:SF-2026-ARXIV-2602-15823 -->

拟本人Review note待新授：`SF-2026-ARXIV-2606-00570` — Daily2026-06-03补Jun02，exact-v1 §3–6/Th4.5/T1–3、必要C.1/C.5/C.6/T33–34/D/E，正式2+2+2=6，原初分7保留；仅相对表示尺度与同向累积的受限风险诊断，不采必然崩溃/唯一因果/检索全轴最优。保AlphaEdit能力韧性、semantic-locality为GT答分而非保持、event/triple及预算混杂、超参有限与全费；未核全B/图像/代码或复现。

**有界停点：** 00570必要Source/6分/actual Ch5具体gap与最小原单段已准备，交root/唯一reader首次必要独核，未预PASS/I/DAY。下一00544仍普通notice/必要Source/评分/owner未做，不先累计未POST草稿。共享Books/README/State/index均未改，不stage/commit/push。

## 00539 GNMR — 必要Source/2+2+2=6，actual Ch28同family具体已有覆盖提案

2026-10-25按root新停点：00570已R142/143实际Ch5、00544已root必要/R148/149实际Ch27，复用不第三。本节仅Jun03补Jun02 BJT；重读AGENTS、当前研究/Report合同、Sources适用使用/Daily/arXiv/恢复、Prompt、ROADMAP、本日README窗口/最新停点与State。owner前读取PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、Ch28完整相关组和Ch27/29职责；using-agent-skills用于范围/验证，不扩软件开发。旧候选日期/评分不搬，只own本包与必要原件。

[exact-v1](https://arxiv.org/html/2606.00539v1) / [保存HTML](SUP_MODEL_B6_2606.00539v1_20261025.html)。本轮[当前官方abs](https://arxiv.org/abs/2606.00539)唯一v1、comments29pages/4figures/15tables，所见无withdrawn/removed/erratum，不作全网无纠错保证。AB/date沿R26/R28有效层复用：原v1 `2026-05-30T05:11:13Z`，同DOI `10.48550/arxiv.2606.00539`、arxiv.content限定查询/findable、registered `2026-06-02T03:53:55Z`；适用规则最早Jun02 00Z至登记上界全落Jun02 BJT，非单字段实际公开时刻。不第三抓日期或追假想早稿。

实际读§2–5/7、Alg1–2、Eq3–7、T1–7，必要C.1假设、D内存预算及E.1–5设置/对照/T8–11；E.4嵌入T13/15也保直接反侧。未核全证明、B算子展开、E.6/7全部附文、图像像素、代码或复现。正式D2（双时域自历史归一风险到受预算恢复路由的具体替代方案）、Reach2（监测统计与backend可恢复执行接口）、Durability2（monitor/action/预算分责可复用），总6；与原未冻结初分相同，不按已有覆盖降分。

### 核心机制、预算语义与理论权限

GNMR是当前local gradient norm除此前历史均值；Alg1首步或历史均值零置1，否则分母加epsilon。短窗Δ-GNMR再除此前δ个ratio的均值，窗口不足置1；它不是已校准故障概率，均值更新/窗口/冷启动共同属于状态。以`max(GNMR/α, Δ-GNMR/β)`排名，越阈者与仍锁定者进入candidate pool，再取最多maxO个active units走高保真路径，其余继续低成本。锁定是进入候选池的短期资格，不是不可抢占或每个已锁单元必保T_lock；超budget会被排名挤出、lock清零。backend先声明可恢复单元及两条兼容路径；固定高精度、embedding/norm/head等不自动进入action域，block内路径不相容时整block作单元。

maxO是**active数量上限**而非新admission数量；它不是直接的总bytes/FLOPs或时间预算。D用固定batch/seq与各unit saved-activation footprint将其转换成额外activation内存上界，不包含全部参数/optimizer/cast/workspace/通信和碎片，异shape单元同count不等价。梯度监测依赖backward可见信息，不能把Alg2的step记法擅自补成修复尚未发生的同次forward；§4明确跨t→t+1的selected-risk persistence。本文采用控制接口，不拷完整调度recipe或授同步时序正确性。

Th1是L-smooth、理想SGD noise及可加perturbation upper envelope下的**one-step上界差**；假设目标风险域recovery gap非负且所选风险在下一步以一定概率持续，非证明高ratio就是最大真实recovery收益或实际loss必降。Oracle按不可见gap排序，GNMR只是可观测代理。Th2在另有尾部条件下解释历史均值不确定性，非实际非平稳LLM固定阈值的普遍报警保证；不为采用控制分支遍历全部proof。

### 关键评价与直接反侧

Activation stress用C4-en/LLaMA-style60M–1.3B，BF16权重/optimizer，只对attention/SwiGLU projection的saved activation作token-wise量化，非整模型原生4bit训练。E.1 maxseq256/globalbatch512；T1与E.1/T8的60M/130M/350M token数口径不一致（如130M2.2B vs2.6B），不拼成已核matched精确预算。T1 1.3B固定4bit不收敛，4/8恢复PPL15.71接近8bit15.68/BF16 15.56，支持局部受控恢复但不是严格质量相等；350M也有8bit18.59优于动态18.84的反侧。T3越阈比例<.2%不等active duty cycle，因为lock/selection另有状态。

DeepSeek-style保固定16/32bit单元，TE hybridFP8为低成本/BF16恢复；另4/6bit是BF16栈上的quantization simulation，不授原生低bit kernel倍率或DeepSeek全规模已训练。§5.2 maxO6称最多25%层，但T9规模的层数不一，不据该百分比外推全部模型。T2终点动态6/8 PPL15.20、固定8为15.18，动态8/16为15.10、固定16为15.06；T4同栈1.264s动态vs1.266s固定8，仅极小局部差，未给多run区间，不能认定普遍更快。T6 maxO4终PPL23.54而8为23.63，更多恢复非单调质量收益。

E.4静态对照只是proxy ADAPT-style：BF16 warmup500步后按平均ratio固定top25%blocks，非原ADAPT完整实现或已公平穷尽所有静态配方。E.5 shared actuator/maxO4，但GNMR是阈值稀疏恢复、GSNR/Jacobian每步填4，故PPL23.685/23.729/23.750和时延/峰值同时混合signal、选择政策与实际duty，不唯一归因norm ratio；E.5 LR3e-3又与E.1表2.5e-3不一致，保各设置不跨表合并。GNMR峰3732MB高于Jacobian3682，不能称全资源最优；无always-low同表不直接算净开销。

13B是冻结base+LoRA r8、两A10080GB的微调stress，不是13B full pretraining。E.3 AdamW/LR2e-5/clip1、maxO10/40层、lock1、短窗5；T7动态GSM8K15.01仍低于BF16 15.09、WikiTextPPL5.4511略差5.4503、MMLU持平，HellaSwag略升64.67 vs64.62；不同生成提取/likelihood/PPL协议不能混成统一能力分，无重复不确定性不签无损。13B适配数据/完整训练token与服务length/batch/concurrency/SLO及预训练计时硬件等Not Disclosed，不补。嵌入T15的PanGu4bit+GNMR终loss3.076仍高于BF16 2.913，也非全精度一致。所有norm reductions、历史/window、校准、route/casts、恢复、峰值headroom、调参与独立质量回归都付费，未核实现/复现。

### actual owner的具体覆盖，不凭marker或旧trace

唯一 `TRAIN-PRETRAINING` / [Ch28“Operator-normalized Risk 把异常信号变成有预算的 Recovery Proposal”](../../../../../books/part-04-training-system/28-pretraining.md)。全Books精确family命中后，实际连续读该标题**完整三段**与前一Architecture Warm-up/后一分层训练证据组：

- 第一段从全局norm基线为何合理出发，明确raw跨算子排序混淆长期scale，逐unit historical baseline、长ratio/短delta、sensor只提风险、backend声明monitored/recoverable粒度与两条路径，实际承载本项新增设计，不是泛“低精度需稳定”。
- 第二段明确hard recovery budget/threshold/lock的稀疏路由、未选低成本执行，不改变loss/format/optimizer权限，统计/阈值/预算/实际route进入checkpoint/trace；同时保reduction/history/fragmentation及不可恢复单元传播漏检。这是正常机制正文，不是Review note或trace完成标签。
- 第三段明确backend observability/compatible recovery约束、均值污染/阈值漂移/预算不足/频繁lock反侧，绑定activation stress/DeepSeek-style/13B三评价族、不授通用跨后端稳定，并给clipping/loss-scaling/skip-retry/整步高精度回退。

因此本次拟具体**已有覆盖**，不是因Books有主题就关闭贡献。正文未宣称原生4bit加速、lock不可抢占、数值等价或理论收敛，故上述必要反侧收窄作者宣传而不构成现文纠错；count到bytes的具体固定配置界、精确表格值/实验协议和理论假设保本研究证据，不为每个实现细节追加长期段。不新增PRE/Review note或第三owner；Ch27拥有数据，Ch29拥有监督目标，均不接管该数值runtime控制。

**有界停点：** 00539正式6分、必要Source与actual Ch28同family三段具体NC交root/唯一reader首次独核，不预通过、不授DAY；无Books写入/POST待办。下一00516未本轮notice/必要/评分/owner，不累计下项。只本包+必要HTML，未改Books/README/State/index，不stage/commit/push。

## 00516 Threshold-Based Exclusive Batching — 正式3+2+2=7 / actual Ch56同family具体已有覆盖提案

2026-10-25按root续派：00539 R150具体NC已过，不第三；仅Jun03补Jun02 BJT。已重读AGENTS/当前Research与Report合同/Sources适用使用、Daily、arXiv与恢复/Prompt/ROADMAP、本日README窗口及停点/State，owner前读取项目背景、学习理念、写作指南及实际Ch56三段与直接前后、Ch55/57职责。using-agent-skills用于范围/验证，不展开实现流程。R26/R28完整AB/date有效复用，不第三抓日证：v1 `2026-05-30T04:11:08Z`，精确DOI `10.48550/arxiv.2606.00516`、arxiv.content限定查询/findable/registered `2026-06-02T03:53:22Z`，按适用规则最早Jun02 00Z至登记上界全落Jun02 BJT；非submitted/registered单字段实际公开时刻。

先查同family实际正文与旧链：May31 writeback-plan只是拟Integrate不能自证保存；Jun02 `V3_EVIDENCE_BATCH_02.md`本身份段已有主线/crossover、饱和与回退的有效受限概括，可复用，但把Evaluation位置写成§6–7，与本exact-v1实际§4不符，且未给关键对照/性能条件；本轮只补这些必要位置，不由旧“已有覆盖”标签直接闭合。未改旧报告、归日或分数，也未引入别日材料池。

[exact-v1](https://arxiv.org/html/2606.00516v1) / [保存HTML](SUP_MODEL_B6_2606.00516v1_20261025.html)；本轮[当前官方abs](https://arxiv.org/abs/2606.00516)唯一v1，comments37pages/12figures/ICML2026，所见无withdrawn/removed/erratum，不作全网保证。实际必要读§3–4的核心/模型验证/主对照/latency/EB+与平台反侧，定点A.4校准、D.6 gate、F.3 SLO；未读全部B/C/D证明、其它附件/图像像素、代码或复现，支持与直接反侧足够即止。

### 正式评分和机制资格

D3：通过同栈局部对照和有成本项的crossover推翻“混批在这些条件仍默认占优”的具体选择，将干扰与固定launch摊销比较后决定EB/MB；Reach2：iteration模式与queue/slots、KV容量和实际engine执行接口；Durability2：硬件/workload依赖的phase竞争与可行性可复用，总7，与原未冻结初分相同，不因具体NC降分。分数不借一般在线控制成熟原则、设备名或“普遍最优”加分。

EB在N slots饱和/backlogged队列中累计k个完成空槽才prefill，未完成请求停Decode但保KV；k小损固定prefill摊销，k大付空槽与排队成本。模型以线性prefill/decode时间、i.i.d.输入长度和输出completion hazard分解。CFR几何输出+fluid/大N的θ0解只依p0αp/αd，IFR采用线性hazard的小η一阶修正，联合(k,N)是先阈值后容量的近似，不是任意非饱和流/有限batch/重尾或任意hazard的精确最优。旧正文说joint选择是控制接口，并未声称全局精确解，不能将本文“closed form”倒填成那种保证。

近期输入/输出窗口估hazard，阈值与N采用一轮滞后的fixed-point更新；EWMA occupancy和实测mixed marginal cost让EB+在边际干扰超过固定launch摊销优势时取EB，否则MB。A.4 mixed cost须按硬件/模型用少量ratio profile拟合，δ按费用尺度定，非免profile/免调参。理论memory bound依CFR与估计，D.6独立检查即时free KV blocks并推迟refill以等已有请求完成，属于runtime gate；不把概率模型的N*或经验reserve授无OOM硬保证。profile/窗口/估计、control state、mode与headroom、全部grid和排队费用均需计入。

### 关键评价与直接反侧

§4.1同vLLM build/BF16，v0在饱和下相当k1的EB、v1 decode-maximal mixed，PagedAttention不改；主Qwen3-8B与30B-A3B，RTX PRO6000/H200，L40S/B300有限扩展。具体build SHA、软件全栈/精确并行配置与重复seed/区间未完整给出，不自补。Synthetic输入/输出均匀在均值0.5–1.5倍：128/1024、512/512、1024/128；ShareGPT约105/≤500、LongBench1k–4k/20、Numina122/800–4k、WildChat≥6轮且输出截断。默认c2048、每配置4000请求（WildChat3000多轮约27900请求），不是开放到达流或生产人口。

§4.2 H200 geometric模型验证中fixed-k sweep限定N1024，而adaptive同时改N；其较最佳fixed-k高8%等不能唯一归因阈值解析式。§4.3各scheduler均grid tokenbudget4096–18432/maxbatch256–2048并取最佳throughput，含各自config优势与调参成本，不是同一个固定batch的净算法差额。T2 RTX Qwen8B平均RPS+7.9%，但30B-A3B ShareGPT -3.1%、Numina -7.7%；H200 MoE平均-2.9%、Numina -8.2%。41.9% headline来自L40S WildChat Qwen8B（14.70 vs10.36 RPS），不拼成所有低带宽GPU/模型收益，也不以TFLOPs不同设备的跨卡差距单独识别bandwidth因果。80%/20% decode-ratio是所测profile现象，不是通用切换常数。

v1通常更低TTFT；EB偏TPOT。T3 RTX c512 EB+ TTFT5.1s仍高于v1 1.2s，即使throughput更高；H200分布shift EB+ throughput21182高于20396，却TTFT69.7s差于41.2s。其“接近较好mode throughput”不等逐指标同时最好、也不是oracle随时切换或尾SLO保证。F.3 RTX c512严格TPOT<50ms时joint attainment仅约0–1.3%；放宽<100ms且TTFT<10s EB+80.3%、EB77.3%、v1 5.8%，TTFT<2s反而v1 4.9%优于EB+1.2%。保不同SLO的失败人口，不能只采80.3%。D.6 gate将部分H200 MoE负差收窄但未消除，支持容量回退而非“加gate就总优”。未读PD全部附件或授PD普遍劣势，未运行性能测试。

### actual owner三段的具体覆盖（不是名字/marker/旧计划）

唯一 `INFER-SCHEDULING` / [Ch56“Exclusive Batching 的 Phase Switch 是 Workload-dependent State”](../../../../../books/part-05-inference-system/56-inference-scheduling.md)，本轮实际连续读完整三段和前一GPU抢占/后一live-layout交接：

1. 首段解释MB在带宽充足/可共批时仍合理，具名P/D interference和固定priority失效条件，列busy/idle slots、保留KV、输入分布、output hazard、bandwidth/model与headroom，已经承载所改变的设计选择，不只是“按workload调度”。
2. 次段以累计idle slots的k解释过早/过晚成本、近期窗口估计、阈值+memory-safe batch、KV feasibility gate，并写hybrid随crossover切mixed/exclusive，没有普适支配或精确最优保证。
3. 三段把收益连回phase interference/空槽/KV同决策，保hazard/window/mode-switch状态和漂移/估计/振荡/tail偏置、RTX/H200/model/budget/batch sweep/饱和绑定，并保高带宽大模型、低并发/严格tail或未校准时MB/固定阈值/PD回退。

这组正常机制正文已具体承载本项受限长期贡献，拟**已有覆盖**；不因有相似标题就NC，也不为补表格、解析式或更多配置细节造正文diff。新必要反侧与精确位置留本证据，既存正文没有被其否定的普遍性能/SLO断言。Ch46拥有基础continuous batching、Ch55拥有PD跨池状态，本项不另设第二owner。无新PRE、Review note或Books/POST请求。

**有界停点：** 00516正式7分/必要层补齐与actual Ch56同family三段具体NC交root和唯一reader首次独核，不预通过/DAY。下一00426未开始本轮notice/必要/score/owner，不扩Methods或全证明/性能复现。只本包与精确HTML，未改Books/README/State/index，不stage/commit/push。

## 00365 SPARQLe — 正式2+2+2=6 / actual Ch49最小PRE

2026-10-25按root恢复仅Jun03补Jun02 BJT；00516 R152、00426 R155/156、00392 R159、00382 R161有效层复用，不第三。已重读AGENTS、Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP及本日README/State最新停点；owner前读项目背景/学习理念/写作指南、Ch49实际稀疏/表示/metadata/执行衔接及Ch48/50职责。using-agent-skills限范围与验证，不扩软件实施。R26/R28完整AB/date复用：v1 `2026-05-29T21:07:27Z`，同DOI `10.48550/arxiv.2606.00365`、arxiv.content限定查询/findable/registered `2026-06-02T03:49:49Z`，适用日程最早Jun02 00Z至登记上界全在Jun02 BJT，非单字段实际公开时刻。没有早稿新线索，不扩假想日期搜索。

同family旧`legacy-reports-before-created-owner-reconciliation/2026-05-30.md`定点身份段只给摘要/泛条件、方法/评价章节导航和旧NC标签；旧actual依据是Ch49 static-weight→dynamic-activation→shared sparse address合同，不能代本项位平面机制。只复用原件身份/方法位置，不复活旧日期或把trace当保存。全Books精确family/SPARQLe/MSB/LSB无对应本机制正文，不能据此单独判gap，以下另作实际对照。

[exact-v1](https://arxiv.org/html/2606.00365v1) / [保存HTML](SUP_MODEL_B6_2606.00365v1_20261025.html)。本轮打开[当前官方abs](https://arxiv.org/abs/2606.00365)，唯一v1、所见无withdrawn/removed/erratum，不作全网无纠错保证。实际读§3.1–3.3/Eq1–3/Alg1、§4/T1、§5.1–5.3/T2与相关图注；未看图像像素、代码、RTL、运行实验或复现，不扩附件。正式D2（dense低位+sparse高位与消费者联合执行的替代表示）、Reach2（校准/packing跨存储与PE算术接口）、Durability2（表示等价与有损增强、metadata/执行分责可复用），总6，与原初分同，不借hardware名字或宣传加分；因actual长期gap定点深入。

### 核心机制与严格采用范围

普通W4A8仍要处理8bit activation；本文把8bit码分成dense LSB4、每值1bit Precision Bitmap、仅PBM1位置存MSB4的稀疏流，在同一PE上先dense低位、再按bitmap执行高位，将后者partial sums移4位后累加。非零activation也可能只需低位，因此它不同于把整activation置零或剪掉其column。分解不改原整数码时，完整高低位和正确signed/shift/accumulator语义可保原码算术；不能把作者“保A8精度”推广到下面的有损clip或原浮点模型。

Eq1计入bitmap后，若s为可省高位比例、忽略padding/scale等，8bit表示每值`4+1+4(1−s)=9−4s`bits，需s>25%才比8bit payload省（代数条件）；Eq2声称半位跳算的operation减少s/2，不是latency同比。§3.2明确two's-complement高4位全零范围[0,15]，不自动含负小值的sign-extension；不能把sign bits全当zero、把LSB0–15未经验证送入signed INT4或自补完整signed PE实现。本采用只讲码值分解与consumer义务，不给未核signed datapath执行recipe。

Sparsity增强按对应weight-row L1选低重要性activation columns，仅这些列把边界附近码clip进[0,15]；global通过校准sweep，layerwise冻结base weights、训练clip bounds，用输出MSE减去mask稀疏奖励。冻结weights不等模型函数不变；MSE也不保证全部任务保持，离散mask/bounds反传的具体估计器未详披露，不提供可直接运行优化配方。clip mask、bounds、scale/zero、signed rules与layout共同成为artifact；预计算importance不等runtime clip/编码/解码免费。

Unified PE把dense/sparse pass串行共享MAC/输出累加，load与drain带PBM压缩/分流；需要专门consumer，不能由普通TensorRT/GPU INT4 kernel名称获得支持。原文§3.3用iso-area叙述“约多50%PE/约30%稀疏度摊销”，但实际§4/T1是iso-MAC两边均256PE、2048MAC/cycle和同1.5MB SRAM，不把两种比较拼成一个iso-area实测。Int8×Int8需4round，Int8×Int4需2，元数据/串行pass也有费。

### 关键评价与直接反侧

§4 BitNet3B W2A8KV4、Llama2-7B/Llama3-8B W4A8KV4，WikiText与LM-Harness、maxseq2048；训练split校准，BitNet layerwise23iterations、两Llama global，k50%作中间操作点。主性能比较是量化模型dense accelerator vs hybrid，不是不同真实GPU服务；W4A4精度比较引用不同PTQ分支，也不能单独归因表示格式。完整batch/concurrency/实际输入输出长度、clock/SLO/重复seed与区间未给，不补。

§4明确7nm RTL综合估area/power，energy-latency由analytical per-layer model估算，跨层顺序执行，**DRAM读写能量/时延排除**。故16–24.3%prefill、13.5–23.4%decode latency下降是作者局部建模结果，不是GPU实测或完整online TTFT/TPOT；片上metadata在模型内不补被排除DRAM费用。T1“DRAM1GB”也是模型配置，不补模型驻留/多die、offload可行性。5.5%area/7%平均power增加必须保，不能由energy下降叫零overhead。

T2直接反驳无损A8质量宣传：Llama3 PPL6.72→7.05、ARC-E80.72→75.88、ARC-C52.05→46.92；Llama2 PPL5.67→6.0；BitNet PPL10.21→12.19、PIQA60.7→56.43。少数题持平/改善不抹整体有损，优于相应A4也不等保A8。§5.3 k增大带稀疏/质量取舍；不把校准MSE或weights冻结当证明。约44–62%平均高位稀疏、不同层收益与未受影响的activation×activation attention路径共同限定收益，均值超过30%不证明每层全部shape都适合。实际部署还须支付mask/bounds校准与冻结、clip/bitmap编码、padding/scale、两pass/移位累加、buffer与完整质量/请求回归，失配保原A8/dense执行；不声称复现、核实现或生产ready。

### actual owner差额与最小逐字PRE（未授写）

唯一 `INFER-TENSORRT-LLM` / [Ch49“粒度与校准决定谁共享同一份误差预算”](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)。实际Ch49 static/dynamic sparsity完整组是按整值/列support跳算；quantization组已讲affine网格/scale metadata、StagQ可截取prefix位平面与weight side records，但未承载**同一activation码dense低位+sparse高位联合执行、bitmap break-even与可逆分解/有损增强的区分**。旧泛NC不能覆盖这个具体接口；不新建论文H3或移到Ch54/50。只在现metadata基段后、StagQ分支前补一自然段。

完整直接上锚：
> Per-tensor 用一个 scale 覆盖整块张量，接口最简单；per-channel 沿指定轴使用不同 scale，避免幅度大的通道拖累所有通道；group/block-wise 再把轴上的元素分成更小的共享组。粒度越细，通常越容易贴近局部分布，却需要更多 scale、可能的 zero-point、解包和 kernel 索引。轴、group size 与物理 layout 必须一同约定，不能把同为“4-bit”的 artifact 直接互换。若每组 `g` 个 `b`-bit 值另存 `m` bits metadata，忽略 padding 时每值实际成本为 `b + m/g` bits；例如每 128 个 4-bit 值保存一个 FP16 scale，是 `4.125` bits/value，而非恰好 4 bits。这只是容量算式，不是吞吐结论。

拟新增完整单段：
> Activation 不为零，也可能只有低位需要稠密执行：把一个整数码拆成稠密低半位、逐值 bitmap 与稀疏高半位，可让同一窄 datapath 先后计算两份部分和，再按原位权移位累加；这不同于丢弃整个 activation。保留全部码位且符号/累加语义正确时，拆分本身可保持原整数计算，但 bitmap 也占空间：8bit 拆4+4时，若可省高位比例为 s，忽略其余开销也需 `9−4s` bits/value，s 超过25%才省 payload。[SPARQLe 的受限协同设计](https://arxiv.org/html/2606.00365v1#S3)还裁剪低重要性列来提高高位稀疏度，这一步即使冻结 weights 仍改变函数，须与无裁剪格式分开验质量。Bitmap 编解码、符号/scale 处理、两轮执行、buffer与校准都有费用，普通低bit kernel不自动支持该格式；其综合/成本模型排除DRAM，任务分数也有反退，不能当完整服务加速或无损A8保证。稀疏度、质量或consumer不合时，保原A8码与dense执行，不由平均高位稀疏率批准发布。<!-- source-family:SF-2026-ARXIV-2606-00365 -->

完整直接下锚：
> 多个目标精度也可共享同一份分组metadata：以2bit affine base加逐层dyadic bitplanes形成可截取前缀，加载时再repack为一个kernel消费的精度；这与分别存每个精度的独立artifact不同，也不等于在线免费切换。[StagQ 的受限格式](https://arxiv.org/html/2610.05977v1)还保存pre-grid原值与post-grid残差的稀疏side records，所有精度都要读取，不能只用prefix bits计算实际成本。Guard并非逐项改善，部分5/6bit廉价对照更好；physical padding也高于logical bpv，3bit unfused路径可更慢。选参、校准、side records、packing和加载转换全部计费；质量、真实存储或目标kernel不合时保留独立精度artifact、成熟格式与更高精度，不由A100 batch1合成权重微核推全模型/服务收益。<!-- source-family:SF-2026-ARXIV-2610-05977 -->

拟本人Review note待新授：`SF-2026-ARXIV-2606-00365` — Daily2026-06-03补Jun02，exact-v1 §3–5/Eq1–3/Alg1/T1–2，正式2+2+2=6；只采dense低位+sparse高位表示/consumer和bitmap break-even，分解等价与有损clip分开。保signed/LSB范围未补配方、isoarea/isoMAC不同、7nm综合/成本模型排DRAM、T2质量损伤、两pass与全费；未核像素/RTL/代码或复现，不授原生GPU支持及完整SLO。

**有界停点：** 00365必要Source/正式6与actual Ch49最小单段+完整两锚ready即交root/唯一reader首次独核，不预PASS/I/DAY；不猜或读下一Methods。不改Books/README/State/index，不stage/commit/push。

## 00334 TPS — 新具名FLAIRS首正文资格保留；已读必要原文保留，不预评分/Books

2026-10-25仅Jun03补Jun02 BJT，按root续派；00365 R162/164修复后R165、其余已成层不第三。已重读AGENTS、当前Research/Report合同、Sources适用使用/Daily/arXiv/恢复、Prompt、ROADMAP、本日README/State最新停点。using-agent-skills约束单项/证据与停止，未扩NAV/其它日期或软件开发。原完整AB准入与R26/R28联合Jun02日证保持：v1 `2026-05-29T20:19:49Z`、DOI `10.48550/arxiv.2606.00334`、arxiv.content限定/findable/registered `2026-06-02T03:49:06Z`支持该arXiv公告在Jun02 BJT，不由新线索否定这一层，也不单独把它当全球首正文日期。

### 本轮新增首正文渠道及有限恢复

本轮[当前arXiv官方页](https://arxiv.org/abs/2606.00334)唯一v1，所见无withdrawn/removed/erratum；但明确Journal reference `The International FLAIRS Conference Proceedings, 39(1) (2026)`、Related DOI [`10.32473/flairs.39.1.141843`](https://doi.org/10.32473/flairs.39.1.141843)。这是具名正文出版渠道，不是为假想早稿扩搜。

精确[Crossref记录](https://api.crossref.org/works/10.32473/flairs.39.1.141843)正常GET成功，[原件](SUP_MODEL_00334_FLAIRS_CROSSREF_20261025.json)核得：title `Isolating LLM Lexical Bias`与subtitle `A Curation-Free Triangulated Metric for Preference-Stage Learning`合成同题；三作者Xiaoyang Ming/Jose Hernandez/Thomas Stephan Juzek匹配；publisher `University of Florida George A Smathers Libraries`、container FLAIRS/39/1。`published-online.date-parts=[[2026,5,6]]`、`published.date-parts`同值；`created.date-time=2026-05-06T13:17:28Z`只是登记创建，不是公开时间。license start May06也不是另一份正文公开证明，不补成午夜或用它替发布日期。

记录的`resource.primary.URL`为[官方article141843](https://journals.flvc.org/FLAIRS/article/view/141843)，`link`提供[官方PDF147188](https://journals.flvc.org/FLAIRS/article/download/141843/147188)，`content-version=vor`。DOI正常HEAD返回302到同landing。web打开DOI不可访问；landing正常web与直接GET均403，随后精确PDF正常web/直接GET均403，没有得到landing发布日期字段或可读VoR。未绕过访问控制、未遍历会场/issue/镜像或换身份重试，未把403响应/下载失败说成读到PDF。Crossref的publisher-deposited online字段是具体更早线索，但**本轮未用它单独认证May06已有可读正文**；也不凭搜索/ResearchGate“May2026”补日界。

因此只重开本家族首次正文资格：当前Jun02 arXiv层有效，原候选旧日期/分数不迁、不改；新补查不得预认当窗首发、正式评分、NC/PRE或Books采用。原筛选`2+1+2=5`仍只是原提案，未因访问/工作量降分或冻结。精确外部需求是上述官方article/PDF的可读VoR、首次公开/上线字段或能将该同题正文公开日限定在目标BJT日一侧的官方历史记录；若证实更早同正文，按真实日期定点恢复而非倒迁旧候选，若证明仅后发或实质新版则定点审事件差额，不复扫本日其它材料。

### 资格重开前已实际读到的必要层（保留但不作本窗正面证据）

[exact-v1](https://arxiv.org/html/2606.00334v1)已正常打开并[保存HTML](SUP_MODEL_B6_2606.00334v1_20261025.html)；本轮在发现并有限恢复关联出版信息期间，读§3.1–3.3全部定义/生成与清洗协议、§4/4.1关键验证、§6讨论、§8限制，未看图像像素/完整词源分析、代码或复现实验。此已读层保留不删，不声称资格或完整独立Source/Books通过。

42K PubMed2012–2021 abstracts按sentence boundary近半切开，前半给base/instruct续写、后半human H；六模型族（Gemma4B、Yi6B，其余7/8B）。Base raw continuation而instruct另有system wrapper，greedy/T0、EOS suppression最少120/最多200token、4gram no-repeat；H/B/I均regex后由GPT4o-mini做deletion-only清洗，spaCy3.8标lemma+UPOS。对每prompt三元组按相同百分位取M4个K-token windows，任何一路太短即整组排除，再记窗口内词是否出现、按文档平均并作Jeffreys平滑。相同百分位非同语义位置，过滤与LLM删除也可能改变人口/词频；“无手工词表”不等无策展/无测量干预，PubMed是语言测量样本，不采用医学机制或领域性能。

定义`wTPS=min(lI−lH,lI−lB)−max(0,lB−lH)`。它是三参照的词汇差，不是受控隔离preference-only干预；§8明确observational且不能分离SFT与preference优化，与摘要强“归因偏好阶段”须分开。uTPS对词元wTPS平方再RMS，方向被去掉，不能把较高corpus RMS全叫正向overuse；按式的正分条件也比“I同时高于B/H”更强。直接代数例H=.1/B=.4/I=.5时两差都正但wTPS=.1−.3=−.2，这是本项目反例，不是作者已测人口。不能从负分的平方贡献判“偏好新增加词”。

§4报告所有族R=cTPSI/cTPSB>1与Falcon1.73等，是其生成/清洗/窗口/词频人口的描述；没有preference-stage-only训练checkpoint对照，无法将族间差归独立RLHF算法。K40/50/60与window seed43–46 top词排名近稳，只验窗口重采，不是generation/multiseed训练、stage因果或跨域迁移；与既有文献22/30 content词重合亦非独立gold。§8承认单Scientific English域、LLM cleaner artifacts及词源二分/“prestige”解释未定，不采社会地位因果或词表真值。GPU/precision、总调用/生成时延与完整费用Not Disclosed，不补性能或SLO；12模型续写、清洗、POS、窗口/表与独立人审都付费。

ROADMAP暂路由`PLATFORM-EVALUATION-SYSTEM`/Ch66仅供后续资格恢复定位：本轮没有用现有泛平均/归因原则替本文补因果，也未给actual-owner NC/PRE；资格新层先交独核，必要时再读实际相关完整组/相邻职责以决定受限测量是否还有长期差额。

**有界停点：** 00334新的具名FLAIRS first-public资格与已读必要层ready交root/唯一reader首次日期新层核，未预当窗候选/正式分/NC/PRE/I/DAY。已穷尽本轮正常已知官方article/PDF入口，保明确外部重开；不扩下一Methods/NAV、不写Book/Report/State/index，不stage/commit/push。

## 00306 温度与KL方向联合选择 — 正式3+1+2=6 / actual Ch29最小PRE

2026-10-25仅Jun03补Jun02 BJT，00334 R167first-public有限隔离及已成层不第三。恢复已重读AGENTS、Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP、本日README/State停点；owner前读项目背景/学习理念/写作指南、Ch29蒸馏实际前后组及Ch28/30职责。using-agent-skills用于范围/验证，不扩软件开发。R26/R28完整AB/准入/联合日证有效复用：v1 `2026-05-29T19:32:21Z`，精确DOI `10.48550/arxiv.2606.00306`、arxiv.content限定/findable/registered `2026-06-02T03:48:26Z`，适用规则最早Jun02 00Z至登记界全落Jun02 BJT，非单字段实际公开时刻。无更早正文新线索，不扩假想日期请求。

[exact-v1](https://arxiv.org/html/2606.00306v1) / [保存HTML](SUP_MODEL_B6_2606.00306v1_20261025.html)。本轮[当前官方abs](https://arxiv.org/abs/2606.00306)唯一v1，无所见withdrawn/removed/erratum；root仅§1–2早段导航不代本轮必要层。全Books与报告精确family未见旧真实必要链。实际读§2/Eq2–4/Prop2.1–2.2、§3、§4/T1及A实施/选点协议；只定点核公式所需代数，不遍历全部证明、案例、附件/代码或复现。正式D3（在已测离线设定下温度调节会反转FKL/RKL次序，纠正由τ1直接决定目标选择的结论）、Reach1（蒸馏loss与比较组件，不借训练全生命周期加分）、Durability2（目标/梯度尺度/评测条件分责稳定），总6，与原初分一致，非按拟写书或工作量改分。

### 必要机制与数学边界

相同词表/固定prefix下，teacher/student logits经同一τ softmax为pτ/qτ；FKL梯度是`(qτ−pτ)/τ`，RKL可写`qτ[Δ−E_qτΔ]/τ²`，Δ=z_student−z_teacher。FKL直接追softened teacher目标；RKL仍以温度依赖的qτ给centered logit-gap加权，故“主要conditioning”不等只是全局乘常数、完全不改方向或目标。改变τ确实也改变RKL概率分布，不能把摘要对比句当不受温度影响的定理。

中心化有限logits在τ→∞时，两种梯度首项同为Δ/(Vτ²)+O(τ^-3)；这是固定prefix、full-vocab、渐近logit匹配，未乘τ²时梯度也同时趋零，不证明任何有限τ、容量受限学生、参数优化轨迹或下游行为相同。若实现再乘τ²，会取消领先梯度衰减但不取消有限τ的p/q变化；与CE/其他loss混合时相对权重也改变。本文公开数学式是不带该补偿的KL，A没有独立说明完整实现是否另加惯例τ²，不把未核代码补成已知规范。Loss定义、τ、补偿/系数、LR、reduction和prefix人口须一并绑定（项目实现要求），不能由τ调参收益唯一排除有效步长变化的作用。

### 评价与直接反侧

A明确off-policy fixed teacher-generated responses，非student rollout/online KD；Dolly14K train/500 validation/500 test，先fine-tune teacher再蒸馏，teacher/student同family词表坐标。主GPT2XL1.5B→Base120M、OPT6.7B→1.3B；§3另有Medium趋势，不把它补成主表完整设置。4×A10040GB、batch32、20epochs、maxinput512，LR GPT2 5e-4/OPT5e-5。训练precision、teacher生成长度/采样与代价、teacher微调全部预算、净wallclock和服务SLO未完整给出，不补。

每epoch保存，以validation ROUGE-L选checkpoint，评价decode temperature1（不等训练KDτ）。ROUGE-L跨五seed{10,20,30,40,50}汇总；没有明确把seed的全部训练/生成随机性拆开，不能当独立数据人口或事实/安全真值。τgrid1.5/2/2.5/3/3.5/4取“best-performing”，τ选点具体人口未另明确，不自行认作已证明完全独立测试集；共享训练设置/原方法默认超参与六点温度搜索不等全部objective均经等费用最优调参。A声称same hyperparameter budget，不替代teacher生成、多个候选/每epoch评价与选择的完整成本核算。

§3图是五instruction benchmarks平均，T1 Avg只Dolly/Super-NI/UnNI，不能混作同一均值。T1 GPT2 FKL19.70→25.53、RKL23.21→23.70；OPT FKL25.00→29.08、RKL25.17→28.63，支持这些相同数据/预算设定下τ改变排名，不是FKL普遍支配。OPT UnNI RKL+τ31.29仍低于原teacher31.39，Dolly也低于其FKL；JS/AKL等部分均值又高于FKL+τ，不能把“简单KL竞争性”写成最优新目标。§3较大τ的GPT2 RKL可反退，图示SFKL等不稳定；更多温度不是单调收益。高温tail更丰富不证明teacher尾部真值/可教性或更高质量，ROUGE-L/五固定instruction人口也不授code/math/OOD/对话安全或生产能力。

结论仅为KL方向须和蒸馏τ共同选择，并绑定该固定teacher-response人口。Teacher预训/微调与生成、两模型前向、全词表概率、20epoch、τgrid/checkpoint选择及独立任务回归都付费；未复现实验、未核代码或全样例，不授任意on-policy/跨词表目标与有限温度全局收敛。

### actual owner差额与最小逐字PRE（未授写/独核）

唯一 `TRAIN-SFT` / [Ch29“Distillation 不是‘Teacher 越强越好’”](../../../../../books/part-04-training-system/29-sft.md)。实际完整读现gold质量转移、FKL head/tail加权、RKL target/tail耦合与截词表梯度、跨tokenizer组，保前方verified lesson交接。现文已有teacher错/尾部不一定正确与支持/权重影响，但尚无**蒸馏温度和KL方向共同定义目标及梯度、τ1排名不可直接用来选目标**；Ch28预训目标/Ch30低秩更新表示、Ch35checkpoint分别不拥有这个KD目标选择。不建新H3，仅在本蒸馏H3下、gold局部修正段前插一自然段，先建立温度与方向的共同基线再接已有tail分支。

完整直接上锚（标题）：
> ### Distillation 不是“Teacher 越强越好”

拟新增完整单段：
> 同词表、同prefix的概率蒸馏还要联合选择KL方向与训练温度，而不是沿用τ=1时的排名。把teacher和student logits同时除以τ后，forward KL直接追踪softened teacher分布，reverse KL则以温度相关的student概率加权两端logit差；后者也会改变，不能只解释成统一梯度倍率。[有限离线蒸馏对照](https://arxiv.org/html/2606.00306v1#S3)观察到调温后FKL/RKL次序反转，但高温下两者趋于同一logit-matching首项只是渐近结果，不证明有限温度或训练轨迹等价。τ²补偿、loss系数和学习率须共同声明，目标温度也不等生成/评价温度；教师回答人口、选τ/checkpoint的验证集与全部搜索费用应一起固定。固定teacher响应上的ROUGE-L改善不授student-rollout、教师尾部真值或通用能力；尾部噪声、质量或净预算失配时，保留经验证的原温度/FKL或RKL、可信监督与原student，不由一种KL名称批准蒸馏替换。<!-- source-family:SF-2026-ARXIV-2606-00306 -->

完整直接下锚：
> 当任务给出可信的已知标签 `y`，teacher 的错误 top-1 也可以作为 target 修正的局部门槛，而不必用 temperature 同时改变所有 dark-class odds。设其概率为 `p`、错误 top-1 为 `k*≠y`，选择 `δ=min(η p_k*, m(p_k*−p_y))`，其中 `0<η<1`、`0<m≤1`，只从 `k*` 减去 δ 并向 `y` 加回，其他坐标不变；直接代数保证非负、总质量与未涉及类别之间的 odds，不保证任意 entropy/semantic-neighborhood 约束、wrong-mass 阈值或正确性。它新增 gold 标签、门槛及目标版本的依赖；[原始有界机制与反侧](https://arxiv.org/html/2602.12687v1)只在受测分类 teacher/student 中提供局部支持，AGNews 有退步，soft entropy loss 也不是 hard bounds。原稿 A.1 把含 entropy 上界的可行集视为凸集，其一般 unique projection 推出仍有争议，不能借给这条质量转移分支。标签不可靠、任务不满足单标签坐标或 held-out utility 退化时，保留原 teacher target、普通温度蒸馏或原 student。<!-- source-family:SF-2026-ARXIV-2602-12687 -->

拟本人Review note待新授：`SF-2026-ARXIV-2606-00306` — Daily2026-06-03补Jun02，exact-v1 §2/Eq2–4/Prop2.1–2.2、§3–4/T1及A，正式3+1+2=6；仅温度×KL方向的共同目标/梯度选择。保有限τ非全局等价、RKL q权重亦变、τ²实现未核、离线teacher-response人口/选点费用、3/5bench均值不同及质量/τ反退，不授on-policy/全域最优或复现。

**有界停点：** 00306必要/正式6/actual Ch29具体gap、最小原单段与完整两锚即交root/唯一reader首次独核，不预PASS/I/DAY，不展开下一Methods。只本包+必要HTML，不Book/Report/State/index，不stage/commit/push。

## 00251 CSA — 正式2+2+2=6 / actual Ch66自评标签随能力更新的最小PRE

2026-10-25仅Jun03补Jun02 BJT，root通知00306 R171/173与02430 R172/174已成，复用不第三。恢复重读AGENTS、Research/Report合同、Sources使用/Daily/arXiv/恢复、Prompt、ROADMAP及本日README/State停点；owner前读项目背景/学习理念/写作指南、Ch66 score/校准组与Continual Update完整组和Ch65/67职责，Ch29/33仅核训练目标边界。using-agent-skills用于范围/验证，不扩软件实施。原完整AB/准入与R26/R28日证保持：v1 `2026-05-29T18:32:14Z`，精确DOI `10.48550/arxiv.2606.00251`、arxiv.content限定/findable/registered `2026-06-02T03:47:08Z`，适用公告最早Jun02 00Z至登记上界全在Jun02 BJT；非submitted或registered单字段实际公开时刻。

[exact-v1](https://arxiv.org/html/2606.00251v1) / [保存HTML](SUP_MODEL_B6_2606.00251v1_20261025.html)。本轮[当前官方abs](https://arxiv.org/abs/2606.00251)为Sep26 v2且题名变为Capability Self-Assessment in Large Language Models，所见无withdrawn/removed/erratum；只用v1原题Teaching LLMs to Know Their Limits与内容，不把后版摘要/实验倒填。版本号/改题本身不证明本窗重要修订，不扩v2比较。

旧May30 legacy identity段仅摘要、§1机制导航与泛Evaluation contract/NC，actual所谓coverage甚至只列Ch66元信息，不承载本项具体updated-capability标签；不借其旧8分/日期/完成标签。此次实际读v1 §3–4/Eq1–4/T1–3、F限制与D.1–6设置/指标/T6–8，未核应用完整原件、prompt、图像像素、代码或复现。正式D2（固定旧能力label与训练后重探测的双参照验收改变设计）、Reach2（assessment训练、同model solver与下游采用边界）、Durability2（可解性标签producer/目标随revision变化可复用），总6，与本轮原提案一致；不借通用GRPO或所有模型“自知”加分。

### 核心训练与评价责任

先对有gold的题让原model采K5次，Math任一次正确即Self-Solve，Science需≥3/5且逐次打乱选项，否则Delegate；训练标签固定。三SFT分支分别bare label、给定label条件下self-rationale或Qwen235B teacher-rationale再label；给定label的解释不是独立证明该能力存在。RLVR按预测label与同一固定标签相等给±1，GRPO前对初始G16 rollouts含两类label的queries做DFW，再完整数据训练。DFW筛的是已有组内类别diversity的题，不是把跨query奖励混成一组，也不保证更新后每组永远有variance；OLMo2无需DFW，Qwen0.6B还需early stop，不能称普遍必须或RL永不collapse。

关键验收是训练后模型M'按同K/aggregation重新求可解性标签，分别检查decision对新标签的M-F1、Self/Delegate两组solve gap的CDS，以及独立post/pre solve accuracy的CR。旧标签一致性提高可与新标签一致性及solver能力下降共存。K5 any-correct不是单次实际回答可靠率，Science多数正确也不是无限预算真理解；模型、采样预算/温度、答案解析与聚合都构成标签身份。重新label不能单独免责：若solver退步到大量不可解、同时更多Delegate，可能让自评变容易，因此还必须保原能力参照与逐slice/coverage结果，而非只报告一份新F1。

CDS是两组比例差的unpooled z统计，依赖组数/大小，NA可能来自delegate≤10；不是校准概率、固定coverage的风险或能跨不同n直接当同尺度效应。M-F1与整体Self-Solve比例也不认证逐题决策正确，CR均值接近100不证明每题/每域保留；base accuracy小会使比值更不稳。本文拟采用这一测量责任，不采用“RL学会真正自知/SFT只能记忆”唯一内部因果。

### 关键评价、直接反侧与成本

D为Qwen3 .6/1.7/4/8/14B、OLMo2 7/13B，Math2260train/490test、Science3266/700；Science四MMLU-Pro类别仅作模型选择/可靠性测量人口，不采用领域AI机制。vLLM inference temp1/top-p1/top-k−1；自评每题一次，标签K5，CR前后均五独立生成run均值，不等五次独立训练或完备能力。SFT/GRPO都是bf16全参/TRL/ZeRO3，但LR1e−5 vs1e−6、perdevice batch8 vs16，GRPO G16另有warmup/采样；同epoch不等同token/compute预算。SFT单B200（13/14B双卡），GRPO四B200，warmup步数依model变化，不能把差额全归SFT或RL目标。完整生成长度、prompt、总训练/rollout费用与统计区间本轮必要域未完整给出，不补服务SLO。

T1 RL Math平均CR100.4/Science99.8支持有限均值保持，但Qwen.6B Science CR86.8、CDS−.03，M-F1 .487低于SFTSelf .586；Qwen14B Science RL M-F1 .566也低于SFTSelf .610，不能说所有模型/轴RL全优或无能力损失。SFTSelf在Qwen8B Math CR98.7、SFTTeacher102.3，亦非所有SFT必灾难遗忘。T2跨域只有这两个测试域，Science→Math Qwen8B SFTLabel CDS11.96还高于RL11.35；不认证任意OOD、coding、多语或没有surface difficulty shortcuts。F承认领域/model有限、采样标签/aggregation敏感及数据选样可能pretrain污染。

§4.4固定旧label vs当前重探测与solver性能的checkpoint轨迹是本项直接证据；总体Self/Delegate比例接近而逐题仍错，支持分责而非单一“calibration error”更小即更可靠。T3有/无DFW提高reward std与CSA是有限4/8B Math对照，不同额外warmup预算未控制成普遍因果。本文不采用未本轮完整核的local-cloud收益或数据选择数字，不由中心诊断补上线routing权；五次探测/重探测、rationale采集、teacher、G16训练/DFW、全部solver回归与真正delegate服务均需计费。保原模型/原policy、独立任务验证与人工/可靠外部解题器为回退，未声称复现或生产可靠性。

### actual owner小gap与最小逐字PRE（未授写）

唯一 `PLATFORM-EVALUATION-SYSTEM` / [Ch66“Continual Update 需要同步推进 Calibration State”](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。现完整组已有model+threshold/conformal/calibration transaction、score distribution在accuracy未报警时漂移及配置变更；前score组也已区分读出对象/排名/校准。但尚未承载**当同model被训来自评时，solver能力本身改变可解性标签，需要原能力参照与新标签同时验收**，不是再说普通threshold会过期。Ch29/33分别拥有监督/GRPO通用更新，不在那里复制CSA评价合同；Ch67只记录健康读数，不拥有可解性gold。

只在现Continual Update的exchangeability解释完整段后、推理配置变更段前补一自然段；保持起始解释与原code流程连续，不新建H3或论文段列举。

完整直接上锚：
> 这把 uncertainty 从一次性 benchmark 变成 release state，却依赖 calibration sample 与部署分布的 exchangeability。现有结果覆盖三类 model family、八个以 classification/MCQ 为主的任务序列；`m=200`、低于 1% replay 的结论不能外推到开放式 generation，后者在论文中仍属探索。Exchangeability 或 coverage Gate 失败时应冻结 promotion，回退上一组 model/calibration artifacts；accuracy 与 coverage 两条 Gate 必须并存，不能相互抵消。

拟新增完整单段：
> 若更新的目的就是让模型判断“自己能否解题”，过期的还可能是可解性标签，而不只是score阈值：训练前按规定采样预算得到的solve/delegate标签，绑定的是当时solver；自评训练改变同一模型后，旧标签上的一致性提升可能伴随解题能力下降。[受限CSA对照](https://arxiv.org/html/2606.00251v1#S4.SS4)因此在新checkpoint重新探测可解性，同时对照原任务能力，而非只验旧标签分类率或整体委派比例。采样次数、温度、答案解析与any-correct/多数正确规则都须进入标签身份，多次中一次答对不认证单次回答可靠。新标签F1、逐题选择风险与原能力保持要分账，不能靠能力下降后多委派使自评看似更准；少量模型/域中的均值保持也不授所有切片无损。探测、rationale/rollout训练、重标与独立solver回归均付费，能力或标签不稳时保原checkpoint、独立验证与可核外部求助，不让自报决策自行取得routing或发布权限。<!-- source-family:SF-2026-ARXIV-2606-00251 -->

完整直接下锚：
> [Calibration state](https://arxiv.org/html/2610.28937v1)的失效触发还包括推理配置改变，而不只checkpoint更新。若quantization或token-logit temperature改变了同一任务的nonconformity score分布，固定数据分布和训练权重也不能让旧threshold继承matched coverage；变化可能导致欠覆盖，也可能过覆盖，不由某个bitwidth推单调风险。应把实际score计算、quantization/backend与temperature纳入producer身份，分别声明已知固定配置、稳定mixture或未知但有限配置集的目标。Pooled校准只保证其混合人口；对每个已列配置分别校准再取最大threshold可保守保护，代价是较大的prediction set，latent配置推断还另付错误预算与校准费用。有限label小模型实验不授开放生成真值或任意未见配置可靠性；配置、支持或exchangeability无法核实时，保固定已校pipeline、重新matched校准或停止coverage声明，不以accuracy未降批准旧calibration。<!-- source-family:SF-2026-ARXIV-2610-28937 -->

拟本人Review note待新授：`SF-2026-ARXIV-2606-00251` — Daily2026-06-03补Jun02，exact-v1 §3–4/Eq1–4/T1–3、D.1–6/T6–8与F，正式2+2+2=6；仅同model自评训练改变可解性标签、re-probe与原solver保持双参照。保K/aggregation代理、CDS依分母非概率、RL/SFT预算/优化配置不同、.6B塌缩/单域退步与跨域反侧、全费；不倒填v2、不授真正自知或普遍RL优越，不采用未完整核应用性能，未核prompt/代码/复现。

**有界停点：** 00251首次必要/正式6/actual Ch66小gap与最小原单段ready交root/唯一reader，待首次独核不预PASS/I/DAY；不读下一Methods。只本包与必要HTML，不Book/Report/State/index，不stage/commit/push。


## root采用00334资格层

R167仅新FLAIRS精确渠道/first-public缺口有限核已实际采用Report§5及路由；不把May06 publisher登记当已读全文公开，也不以Jun02 arXiv日证排除更早正文。原必要阅读保留，未正式评分/Books，不迁旧候选或扩venue。

## root实际采用00306

R171必要/正式六分/actualCh29原单段PRE通过后，root在Distillation标题后/gold完整段前真实保存，R173唯一actualPOST通过。Report与本人注已行政采用，未第三有效层或授DAY。
