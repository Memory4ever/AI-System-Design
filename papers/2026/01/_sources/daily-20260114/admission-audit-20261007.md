# Jan14 增量独立窄 PRE（2026-10-07）

复核者 jan10_books_audit，非 Books 作者。新单日上下文已重读 AGENTS、Research/Report/Prompt、Sources 使用说明/每日组、ROADMAP、相关 checkpoint 与 Books 学习/呈现约束。只审 root 指定 owner 提案，不授题摘池覆盖、整日 DAY 或实际写后 POST；不改 Books/报告/README/LS，不 stage/commit/push。精确 HTML 优先，复用作者定位但不把提案当原证。

## 首批：06403 / 06959

| 项目 | 必要原证与关键反侧 | 实际 owner 局部邻接 / 具体差额 | PRE 处置 |
| --- | --- | --- | --- |
| 2601.06403v1 | [exact HTML](https://arxiv.org/html/2601.06403v1) §3.1 Eq3–4：同 checkpoint、同 user 和同一已生成 prefix，两条 system 条件 logits；输出是目标 logits 加 alpha×目标/default 差，alpha=0 仍是目标 system。§3.2 Eq5 可另选明确 negative baseline。§4–5 Table1：Qwen7/14B alpha2 的 strict accuracy 与域内接受率均有反侧；更强 steering 非普遍更好。 | MODEL-SAMPLING / Ch20，实际顺读222–302：token/序列校准→预算/反馈→hidden vector/subspace→answer-first。既有原理不承载同一 prefix 的双 system 条件 logits 及 baseline 身份。应紧接语义 steering 局部：从 hidden-access 干预转入只需两条件 forward 的 logit 分支，再交 answer-first。 | Integrate 窄机制；只写连续相对强度、baseline 与生成成本/任务回退。不要把 default 视为无条件空 prompt、alpha0 写成 default、双分支写成独立生成，或授正确/安全保证。 |
| 2601.06959v1 | [exact HTML](https://arxiv.org/html/2601.06959v1) §2.2 Eq2–5 / Algorithm1：按 channel scale 归一，diag-H magnitude proxy 选 Ω，先将 body 的 Ω 置零再 VQ；稀疏项保存 normalized original 减去量化 body 在 Ω 的值，不是直接存原值相加。§3 所有 codebook/index/scale/residual 计 BPP；只有 SmolLM2-1.7B-Instruct / WikiText2 PPL。Table1 的10.12 vs10.04并无区间支持“统计无损”；§4 部署/架构泛化是推断，未展示执行 kernel 或吞吐/延迟。 | INFER-TENSORRT-LLM / Ch49，实际顺读110–142与1015–1050：已有压缩≠执行、additive codebook 二阶校准、原始目标补偿和动态 correction。缺少先隔离敏感元素→量化 body→扣去 body reconstruction 再加 residual 的合成关系。可放入 Post-quantization Recovery 的 additive-codebook 邻接，不另讲一般量化。 | Integrate artifact 合成顺序与总存储账本；diag-H 仅 proxy，Ω近似恢复不等全模型无损。只采用明示结构，不授统计无损、完整能力保持、通用架构或执行提速；普通 VQ / 更高精度 / 已验 kernel 共存。 |

准备到必要机制/反侧与局部 owner 差额即止；根授写锁，实际写后由非作者 POST。

## 第二批：07526 / 06794

| 项目 | 必要原证与关键反侧 | 实际 owner 局部邻接 / 具体差额 | PRE 处置 |
| --- | --- | --- | --- |
| 2601.07526v1 MegaFlow | [exact HTML](https://arxiv.org/html/2601.07526v1) §2.3：任务分为独占实例创建/执行/回收与 persistent pool 复用；API-rate、distributed semaphore、admin quota 分别限制不同对象。lifecycle/完成事件与随后 API metadata、异步 artifact 回收不是同一完成证明。§3.1–3.4 的 small1任务 vs big50任务、Alibaba配置与低CPU/memory占用，不支持同资源纯算法、普遍高利用率或跨云收益；正文宣称 perfect isolation/strong consistency 未给协议/恢复证明，不采用。 | AGENT-PLATFORM / Ch84，实际顺读590–648与1014–1048：cgroup tool资源域→harness/artifact→跨run lane/provider额度→resume，末段另有 intent sandbox预热。缺少资源实例粒度与 ephemeral/persistent 寿命的二轴选择与准备/驻留/重置分账。放 Scheduling 不只是 GPU 的 cgroup 分支附近，保持资源控制与任务完成/副作用恢复分权，不复述已有一般限流。 | Integrate 两轴执行模型；“独占实例”是资源分配机制，不是 perfect security。补创建启动回收与池驻留/清洁重置成本、事件后仍验完成artifact。保留共享实例/按需创建；不授 exactly-once、强一致、完整隔离或所有云32%成本提升。 |
| 2601.06794v1 ECHO | [exact HTML](https://arxiv.org/html/2601.06794v1) §3.1–3.3 Eq1–9：同一初始(q,trajectory,score)→N诊断→N条件修正；critic用log剩余headroom比值，actor用修正score，各角色组归一同步更新。可加性是telescoping代数，不等折扣MDP策略不变保证。§5.2 Table2 frozencritic与§5.3 SA消融非同人口：SA只WebShop/SciWorld非binary reward；选10batch散点排除初始score1。Limitations明确同一外部reward噪声/偏差同时传给两角色，不能给诊断正确或causal改善保证。 | TRAIN-GRPO / Ch33，实际顺读2444–2485：teacher support/staleness→ICRL outcome绑定critic→Second-order同policy评判→冻结专家训练Inspector→advantage数值尺度。共同训练已覆盖，但没有按剩余空间的非线性credit shape。放ICRL后/Second-order前的同一分支；保留线性gain和冻结critic，不另起共同训练摘要。 | Integrate 明确headroom transform与角色reward身份；近1同delta放大仅对校准有意义的[0,1]score与eta条件成立。N次诊断/修正、外部评估、双模型更新计费；“同训练预算”不替代总token/环境账。不写全任务SA收益或策略最优不变。 |

## 第三批：07185 / 06428（原六项完成窄 PRE）

| 项目 | 必要原证与关键反侧 | 实际 owner 局部邻接 / 具体差额 | PRE 处置 |
| --- | --- | --- | --- |
| 2601.07185v1 | [exact HTML](https://arxiv.org/html/2601.07185v1) §3.3/4.2/4.3 与 Tables1–5、§7：全benign任务拼接、trigger存在/移除与task accuracy/refusal分测支持回归切片。H1双题vs单题同时改长度/负载，不能授位置唯一因果；H2标准safe3978与InjectGuard113并非同人口，Table3 Mistral+SecAlign无正gap；Table5同trigger集移除更接近有限干预。§3.3声称topic拆分与Table4明确no explicit topic split冲突，且SecAlign drop算术不符，不授独立topic泛化因果/该数值。细粒度拒答规则未用于本窄采用，不扩B.5。 | PLATFORM-SECURITY / Ch72，实际顺读585–675：routing sensor→policy-as-data/authorization→stateful guard→guard组合→benign偏好更新→refusal-prefix/full行为→authority边界。已有一般benign utility，却无位置/触发词反事实切片合同。适合 guard组合与其utility段之后、Preference Data Admission前：从总utility验收转向具体输入扰动，不改确定性权限owner。 | Integrate 有限诊断合同；只写保留benign语义、位置/触发词分开比较并记录任务质量与拒答。不得把摘要“所有防御shortcut”或信息论假设写成证明，topic泛化和效果数字隔离；多轮、安全任务语义及实际部署需重验。 |
| 2601.06428v1 DSC | [exact HTML](https://arxiv.org/html/2601.06428v1) §4.1固定theta*只训head；§4.2用更腐坏状态的预测注入较富context状态，sensor对象是固定部署generator而非共同漂移generator。FCA提供训练错误/context覆盖，不证明部署gap消失。Eq4.1 target1=correct，§4.3/Eq4.2却同g作error并取highest，方向冲突；§5.1 Table1与文字65.2/60.56不符，因此不采完整dynamic recipe或争议增益。§4.3 block-index queue与§5.2 LLaDA8B/500k/OpenCode、block32/max1024/EOS早停/iteration账本支持付费边界，iteration非壁钟。 | MULTIMODAL-GENERATIVE-PARADIGMS / Ch24，实际顺读446–480与732–760：模型预测噪声/soft-state→reveal路径分歧/局部remask→其他软state；另有刷新、永久lock和cache attention视图。缺少固定SFT generator身份与专训sensor/FCA错误来源的分责，不是再讲“允许重写”。可放路径分歧局部之后，先从inference-only sensor转入training-covered sensor，再交其他soft-state分支。 | Integrate 结构与训练分布窄链；不写topK/阈值可执行配方、不暗修1−g、不给冻结权重等于最终输出质量不变的保证。Head训练/计算、remask、queue及更多iteration付费；保守unmask/AR/原checkpoint继续共存。 |

首项成本补核：06403 exact-v1 Limitations 明示约2×FLOPs，KV sharing/caching属于未来；不把作者“相对微调可忽略”或可接受延迟当实测服务承诺。以上六项仅采用具体机制并隔离争议，不授整篇 Evidence PASS、Books POST 或 DAY。

## 授权新增两项：07359 / 06843

root 明确追加本日两项，未自行扩池；与原六项保持独立准备，不等待全部题摘分区。

| 项目 | 必要原证与关键反侧 | 实际 owner 局部邻接 / 具体差额 | PRE 处置 |
| --- | --- | --- | --- |
| 2601.07359v1 DualPD | [exact HTML](https://arxiv.org/html/2601.07359v1) §3.2选择邻层visual-attention变化最大的basic layer、§3.3按softmax前map norm筛head并软抑制；§4.3/4.4/4.6 Tables3/5支持受限选择/强度取舍：过度抑制退步，静态层在某数据集更好；组件消融无充分随机head或独立因果对照。§3.2有Delta logits但§3.4最终argmax只写tilde z(L)，未连接两者；perhead词表投影与跨head/query概率归一未明确。不得拼完整可执行recipe或把attention/norm当grounding真值。 | MULTIMODAL-REPRESENTATION / Ch23，实际顺读550–625：压缩/attention proxy→视觉几何稳定与读/更新分权→decode重选→active acquisition/staticcrop。已有attention不是因果与contrast一般原则，缺少邻层visual-attention变化作layer-selection sensor及head norm/软衰减的局部选择。放读/更新分权与decode重选邻接，明确这是内部选择候选而非新增Observation或证明裁剪。 | Integrate 窄sensor接口/静态与动态选择代价，未连recipe隔离；不写完整logits执行公式、普遍更grounded/无训练即无成本。取attention、中层logits、head统计付费；不能验证head接口或任务收益时保留原decode、静态层与完整视觉路径。 |
| 2601.06843v1 TRUE | [exact HTML](https://arxiv.org/html/2601.06843v1) §3.1/3.3 Eq2/causal mask：visual/text各自连续position编号，仍约束能读的video/history，从编号上去掉未知回答长度对下一视觉段的依赖。§3.4固定offset是GIPE替代分支。OSPE Eq1右侧自引用E(i+1)+ki，ki>0无有限解，不能静默修正式；GDPE不依赖该式。§4.4/4.6为Qwen2.5VL、20k、2fps/5–30s、waitK3与testRandom；Table1 streaming GDPE CIDEr低于Interleave，fluency不等语义正确。§4.7 sum→max/约2x只是理想吞吐与重叠分析，硬件级parallel仍Future。 | MULTIMODAL-REPRESENTATION / Ch23，实际顺读694–764：timestamp/provenance→三轴频段/可读时间→音频时间接口→时窗gaze→资产撤回→temporalprobe→routing/Serving交接。缺少input/output编号相互独立与跨模态causal mask仍约束读取的表示合同；放三轴/可读timestamp后，不归WorldState或把request lifecycle当owner。 | Integrate GDPE位置/mask窄分责；新增编号空间/训练与访问身份须验，时钟/provenance仍不被position替代。OSPE recipe与实测并发/2x低延迟隔离；额外runtime/KV/sync资源交推理层验收。保留原interleave/离线/普通位置；不称所有指标更好或编号已自动实现真实并行。 |

## 本次停止点

指定原六项及明确追加两项的必要精确原证、采用/隔离命题与实际owner完整局部邻接已核，八项均仅有窄 Integrate 差额。未遍历无关附件、未复現实验、未写Books或报告、未授全题摘池Coverage/整篇Evidence/POST/DAY。后续由root授写锁与非作者实际POST；本复核任务到此停止，不自行转日或接其他候选。

## 续授：批3/4/5 的89份完整题摘准入校准

同Jan14续授，八项有效PRE不重做。实际完整读 `increment-abstracts-3/4/5-20261007.json` 全部27/35/27题名与摘要；合计89，不是89候选。下列拟准入只表示“若具体命题成立可改变设计”；指标/机制仍待作者按当前合同核必要证据/日期/评分，绝不将AB当方法Evidence。含糊列给决定准入的最小事实，不因全文/实验待读关闭。未自行扩池。

### 批3：27项

| exact-v1 ID（2601.前缀） | 分区 | 具体设计入口 / 关闭理由 / 最小待决事实 |
| --- | --- | --- |
| 06389 | 拟准入 | learned query token routing与ANN接口；若成立改变late-interaction完整比较预算，不采用30x通用SLO。 |
| 06490 | 含糊 | global persona反向校准local memories是否仅普通反思组合；需明确冲突时原facts/provenance优先级及独立差额。 |
| 06692 | 关闭 | 成熟weighted replicator重新参数化，未建立可信可转移friction→工程控制边界；必要Eq13/14调制取消，详下。 |
| 06377 | 含糊 | Topic×surprise双渠道与reconsolidation具体决策未在AB说明；需异于普通事件分段/冲突更新的规则。 |
| 07125 | 拟准入 | RL inverse-retrieval/NDCG pooling到单vector，明确只恢复部分multi-vector质量，改变index容量选择。 |
| 07183 | 拟准入 | Euclidean冗余assignment考虑方向、shared-cell list layout去重复距离，改变recall/计算的同一账本。 |
| 07136 | 关闭 | commit/issue比例与维护分布描述，无新协调/执行/测试设计条件；不因MAS题名归入。 |
| 07152 | 关闭 | prompt edits→judge critique是成熟优化组合；必要core未给可信新增结构保证，详下。 |
| 06799 | 含糊 | 多chain保留＋triple→sentence→passage已有原理；需history integration/升级gate的新增规则或新反证。 |
| 06424 | 拟准入 | 文本consumer按自身信息需求给VLM描述偏好；若成立改变只面向人类caption评优的训练目标，非text feedback等视觉真值。 |
| 07004 | 含糊 | TEE/attestation/五层memory组合不足；当前core有dummy-bucket与残余泄漏，需确认新隐私边界/协议差额而非ownership重命名。 |
| 07023 | 含糊 | 多年非对话trace的新数据不是自动贡献；需evolving-state任务/连续性控制揭示不同于已有时间记忆评估的失败。 |
| 06282 | 含糊 | 叙事memory/离线semanticization为成熟路径；momentum规则或coherence retrieval需具体新差额。 |
| 06842 | 拟准入 | semantic-match与factual-consistency双encoder/self-answerability三信号拆分后softprompt，改变conflict fusion而非仅相似度。 |
| 07190 | 低分报告 | 可行性＋scaffold依赖负侧，1/1/2=4建议；仅选择scaffold gain≠自主策略命题，Books Existing/NoChange具体位置见下。 |
| 07058 | 拟准入 | paraphrase greedy一致性与correctness分开，pruning降低variance仍可稳定错答；改变可靠性发布两轴而非以一致性授真值。 |
| 06789 | 拟准入 | core把初观察症状Index与修复Resolution分层、先搜索再浏览；改变memory检索可见信息，LLM checklist不授真实修复证书。 |
| 07055 | 拟准入 | hop相似问题共享group baseline而非每query重复评难度，改变自演化采样/credit预算；非无任何数据与免费。 |
| 07072 | 拟准入 | retrieval trigger与malicious objective分离，暴露retrieval成功率与取得执行控制权两级安全验收；不授任意query保证。 |
| 07048 | 拟准入 | streaming insertion、GPU RaBitQ与greedy kernel数据路径改变动态ANN索引更新/随机访存，非一般GPU更快。 |
| 06407 | 拟准入 | ask/act按expected utility gain与user cognitive cost，替代confidence阈；reward/response模型假设需核，不授无参数成本。 |
| 06899 | 拟准入 | 背景suppression与target-size Gaussian center/edge目标分离，改变GUI localization监督；attention≠因果点击安全。 |
| 06860 | 含糊 | data flywheel/两阶段behavior calibration尚无规则，不能因accuracy+efficiency指标或tool node留；需具体奖惩/阶段职责。 |
| 07192 | 拟准入 | query证据图从原文本latent relation pool按需实例化，KG与潜在relation共同筛选，改变预构图缺边repair接口。 |
| 06328 | 拟准入 | 可控制tool中断/状态故障与planner/actor能力错位诊断，改变只最终答案测tool-use的回归合同；新工具数本身不作贡献。 |
| 06663 | 拟准入 | 原core同类任务QA风险识别与IF执行遵守分测、benign误报校准，暴露knowledge≠alignment；不因职业标签关闭。 |
| 06676 | 拟准入 | reference-grounded user simulator＋interaction收益/turn/token成本joint evaluation，改变完全自主final-only研究agent评价。 |

### 批4：35项

| exact-v1 ID（2601.前缀） | 分区 | 具体设计入口 / 关闭理由 / 最小待决事实 |
| --- | --- | --- |
| 07525 | 含糊 | free reasoning到trigger constrained decode是成熟两phase；需新trigger/协议或同预算反证，而非加grammar自动新机制。 |
| 07506 | 拟准入 | swapped reference×候选一致性反事实暴露judge内知识覆盖reference，改变reference-conditioned评价身份。 |
| 07234 | 关闭 | 人类reference UI对缺失类别识别HCI实验，不产生本项目model/training/runtime/agent机制。 |
| 07208 | 拟准入 | terminal-hidden conductor contextual bandit选multiobjective weights，以group advantage训练scalarization policy，改变固定reward配比。 |
| 07806 | 含糊 | Gender-ECE是否只是ECE按gender切片重算；需新校准目标/公平误差关系而非榜单新任务。 |
| 07780 | 关闭 | 逻辑/完整性/伦理/替代四成熟prompt反思组合；未给可转移新增触发/信用/验收条件。 |
| 07212 | 拟准入 | MI hidden transition与DPI contiguous-block重要性/组合选取，改变独立block pruning；global最优需必要理论核。 |
| 07200 | 拟准入 | OT样本weight同时pull safe anchor/push harmful reference，改变instance筛选为distribution objective；geometry不授安全证书。 |
| 07430 | 拟准入 | rationale有/无条件预测KL与KG路径监督，改变仅模仿rationale为部署无rationale知识使用约束。 |
| 07411 | 拟准入 | distributed lowrank parameter ablation削弱correct/wrong区分同时保持LM质量，改变离散模块归因；选择性需真实反侧。 |
| 07468 | 拟准入 | event occurrence time≠dialogue time＋durative state，改变记忆时间索引与duration查询，非仅加timestamp。 |
| 07224 | 拟准入 | gradient spatial concentration作为SFT/RL分流proxy，改变按surface难度分数据；非认知冲突真值。 |
| 07507 | 拟准入 | 冻结原weights跨subspace结构modulation提高update rank/少参数，改变LoRA低rank容量限制；实际结构必须核。 |
| 07782 | 含糊 | decompose/iterative retrieval＋SFT/RLVR为成熟组合；需tool-composition可验证reward/停止的新规则。 |
| 07645 | 拟准入 | 视觉token逐层mask诊断plateau后选择base-LM参数merging，改变按固定layer恢复language branch；probe不授grounding因果。 |
| 07329 | 含糊 | Bayes/DS跨modal pair corroboration可能是成熟融合；需可计算association/依赖条件与不同于cosine的有效差额。 |
| 07309 | 拟准入 | role-conditioned activation选择neuron transplant用于multi-turn expert merge，改变静态wholeexpert mixing；role归因需核。 |
| 07264 | 拟准入 | evidence tool噪声vsverification feedback的confidence分歧，accuracy/calibration联合RL，改变跨tool复用置信口径。 |
| 07263 | 拟准入 | web诱导context与goal一致性pre-effect supervisor，检验非显式注入social engineering；需独立utility/攻击口径。 |
| 07351 | 拟准入 | soft token distribution轨迹＋continuous trajectory supervision，改变hard commit/revision接口，不因soft state主题已有关。 |
| 07449 | 拟准入 | pointwise scorer表征→lightweight list-level score residual，避免full token listwise，改变长list计算/交互分责。 |
| 07779 | 含糊 | milestone memory＋browser视觉tutorial取用组合尚无granular curation/更新新规则；benchmarkheadlines不替贡献。 |
| 07395 | 拟准入 | 未调用恶意tool metadata诱导合法高privilege工具，双evaluation/detection反馈搜索，改变只验证实际被调用tool的安全边界。 |
| 07320 | 拟准入 | low-prob segment boundary后只聚合segment transitions advantage，改变token-level GAE的偏差/状态预算。 |
| 07226 | 拟准入 | 非恶意distractor导致工具过信/越算越坏，rationale-aware reward对照outcome-only；反证可改变budget/reward选择。 |
| 07477 | 含糊 | trace judge rank责任→局部workflow编辑是否仅成熟failure localization+opt；需rank分配依据或可信新对照。 |
| 07516 | 拟准入 | future-observation latent action code＋text-only crossmodal cycle扩coverage，改变只paired image-text构动作空间；需泄漏/代理反侧。 |
| 07651 | 拟准入 | 在线选择task×agents评价排名、task比例不同改变ranking误差采样预算；不是只新Atari榜单。 |
| 07711 | 含糊 | Enhanced/Agentic经验比较AB无具体条件；需成本×能力×失败条件，而非泛称两类各有取舍。 |
| 07582 | 拟准入 | event boundary semantic作为层级定位anchor，改变固定unit切片与flat retrieval；必要源核边界规则。 |
| 07260 | 含糊 | query/keyphrase补检迭代成熟；需overshadow detector实际信号及异于普通query expansion的反证。 |
| 07577 | 含糊 | DAG supervisor/planner/executor scoped context是成熟组合；需新的dependency/replan边界或反侧而非task解耦命名。 |
| 07470 | 拟准入 | 冻结task模型仅DPO memory-copilot学abstraction、转移管理skill不一定转移具体memory，改变负迁移/跨任务reuse单位。 |
| 07347 | 拟准入 | bidirectional DLLM仍reverse curse，whole-entity masking×对称data/relation干预；改变bidirectional objective自动解决关联的预期。 |
| 07422 | 拟准入 | question/answer anchored truth signal分拆与attention knockout/token patching，改变单一truthprobe适用知识边界。 |

### 批5：27项

| exact-v1 ID（2601.前缀） | 分区 | 具体设计入口 / 关闭理由 / 最小待决事实 |
| --- | --- | --- |
| 07041 | 拟准入 | 跨language conflict task不同导致resource abundance/linguistic affinity分支，改变一律高资源优先的证据fusion。 |
| 06943 | 拟准入 | video-web长chain初始视觉anchor漂移令Agentic非恒优，改变长检索goal/persistent-anchor回归。 |
| 06451 | 拟准入 | 已核force/material regression限制VLA刀速与contact触发style转换，模拟force预测≠真实安全边界；不因食品域关闭VLA。 |
| 07821 | 拟准入 | IR-human介入failure分测、world-model safety critic与offline recovery约束online探索，改变只成功率posttrain预算。 |
| 06931 | 拟准入 | real-photo仅face counterfactual保background，task formulation影响bias，改变visual confound audit控制。 |
| 06599 | 拟准入 | context使truth-vector方向/幅度和knowledge conflict改变，改变无context固定probe/vector可复用假设；非几何等真实。 |
| 06748 | 拟准入 | deployment task-progress dense reward更新VLA且保prior，改变固定inference与training安全责任；需online效果/预算。 |
| 06521 | 拟准入 | 去语言知识优势仍基本visual primitive弱的反证，改变knowledge-heavy VQA代表纯感知的评价假设；不是规模人类排行。 |
| 06649 | 关闭 | 已有energy-aware metric应用；RMS功率、固定benchmark TFLOPS与非共同PPL不支持新可转移token能耗/效率律，详下。 |
| 07054 | 含糊 | SFT/CPT/RAG对比可能只是成熟知识注入差异；需novelknowledge cutoff×reasoning支持/同训练预算的具体新条件。 |
| 06965 | 拟准入 | 各task专用concept-token subspace与knowledge replay跨理解/生成/edit传播，改变统一personalization共token干扰。 |
| 06605 | 拟准入 | inpainting reference style+maskedtarget＋semantic/style attention reweight，改变inversion/retraining与conditioning conflict选择。 |
| 07291 | 拟准入 | visual-evidence prefix候选权重引导vocab partition/watermark bias，改变视觉无关随机token扰动；检测/grounding须分验。 |
| 07060 | 拟准入 | affordance/contact/placement/motion锚＋continuous subtask progress负责transition，改变反复动作/提前终止控制。 |
| 07737 | 拟准入 | 语法合理但agent-patient/physical feasibility反common scenes，暴露语言pattern与视觉语义分离；需生成伪影反侧。 |
| 06604 | 关闭 | 必要core为成熟slots/GNN+EZV2/MCTS组合，有限任务与EZV2近似相同；未显出可迁移新选择边界，详下。 |
| 06566 | 低分 | 成熟fusion本身不准入；定点TableII发现相同Regular/LLaVA下LLM aggregation在MSR-VTT退步、YouCook2/QA获益，重开为局部反证1/1/2=4；不进一步Books采用。 |
| 07331 | 拟准入 | structured activation-subspace noise proxy与speech-denoising可反退，改变audio frontend以传统SNR目标评优的假设。 |
| 06496 | 含糊 | CLIP/3D encoder＋contrastivecaption＋reward TTS成熟组合；需scene-summary reward/搜索或OOD边界的新事实。 |
| 06944 | 含糊 | handdrawn grading新benchmark任务不自动贡献；需diagnostic error vs solve protocol/噪声symbol失败类别。 |
| 07868 | 日期隔离 | author已保v1 Jan14 registered/Updated界，不按Submitted自动投Jan13；贡献机制潜力保留，勿补全文或自动挪日。 |
| 07219 | 拟准入 | edit-target/background split conditioning配noise inversion保unedited，改变单prompt editing背景污染路径。 |
| 06474 | 拟准入 | sparseoccupancy query唯一vision-language bridge＋anchor score/denoise分责，改变dense occupancy token爆炸；openloop≠closedloop安全。 |
| 07290 | 拟准入 | core slow/fast帧预算、离散frameID时间输出与SEG→SAM2 masklet接口，改变时间文本与空间mask分责；非新dataset数。 |
| 07366 | 拟准入 | ASR语义作scene/event compression anchor、TemporalCoT到chapter边界，改变纯视觉token预算与summary时间丢失。 |
| 06972 | 拟准入 | 控制架构probe显示phoneme等不同深度策略，改变Transformer/Conformer表示相同或可同点early-exit的假设；probe非实测低延迟。 |
| 07298 | 拟准入 | visual meta-action trajectory bootstrap与diversity→DAPO阶段探索/利用，改变multiimage只finalanswer监督；人类类比不作证据。 |

### 代表性负侧定点复核与准入校准

以下只读各拟采用/排除命题所需的 exact-v1 节位，不代表遍历全文或所有附录。准入不等于 Evidence Gate、日期 PASS 或 Books 差额 PASS。

- **Focus 07190：低分关闭判断，Books Existing/No Change。** [v1 §III-B、IV-A–C、V](https://arxiv.org/html/2601.07190v1) 的初始被动prompt仅1–2次压缩；最佳设置明确强制开始探索前start、10–15工具调用后complete，且15次未压缩追加提醒（HTML L124–137），不是自主触发效果。N=5不作为排除理由；同3/5完成、22.7%总token减少及pylint重探索代价均保留。拟选择的“scaffold改变行为，不能把harness收益归因模型自主能力；压缩有损失/再探索成本”已由实际 `Books/part-07-agent/75-context.md` L228–258，尤其L239–241、249–257承载；预算/authority/摊销还见L267–271。仅这个选择命题判Existing，不宣称所有checkpoint结构已逐项覆盖。评分1/1/2=4，不为新书稿增分。
- **Consent 06692：贡献前关闭，但有定理。** [v1 §3](https://arxiv.org/html/2601.06692v1) Theorem3.1后的说明（L885–891）明确weighted replicator-mutator本身非新；Eq13把源行各目的地乘同一个`1+lambda*epsilonbar(tau')`，Eq14再行归一（L946–952），该行常数取消，不能执行成“熵高提高off-diagonal迁移”。不静默修公式，不以无定理排除；当前可核新kernel标签/consent映射未产生成立的调度选择边界。
- **TinyScale 06649：贡献前关闭。** [v1 Methods/Results/Limitations](https://arxiv.org/html/2601.06649v1) 固定A10G/1.1B/batch1、三条件150trial并非规模排除依据。NVML60秒采样后RMS功率（L68）不是积分能耗；PPL默认/备用随机prompt，极少回退训练batch（L69），不是共同heldout；TFLOPS常数是固定benchmark（L70）。不采用由这些量导出的通用token效率/能耗律，未发现超出成熟指标应用的新可信边界。
- **AoD 07152：贡献前关闭。** [v1 §3.3 L230–264](https://arxiv.org/html/2601.07152v1) 是自然语言judge反馈→autoregressive prompt edit成熟优化组合。局部Lipschitz/有界edit本身不保证Theorem1所称全局最优收敛；Proposition0所给前提也不推出DLLM优于AR的KL不等式。仅隔离这些受影响声明，不扫完整proof；不能把未成立保证当新设计条件。
- **PR-CoT 07780：维持贡献前关闭，新增实证隔离。** [v1 §3.1–3.3、Introduction](https://arxiv.org/html/2601.07780v1) L124–175仍是CoT→四预设视角prompt→综合prompt，无新增验证触发/credit规则；安全/伦理视角也未使组合自动准入。L98明确自称实验为“fabricated yet plausible”，因此§4收益表不作为实际测得结果，不升级证据。
- **ObjectZero 06604：贡献前关闭。** [v1 §4–5 L108–145](https://arxiv.org/html/2601.06604v1) 预训练冻结slots、GNN dynamics、EZV2/MCTS组合；两个环境3seed的规模不是排除原因。L140与EZV2表现接近，L142–143保真实场景分解与slot平方复杂度边界；未见可迁移的新机制/选择条件，不采用object-centric普遍胜出。
- **QCaption 06566：负侧推翻原贡献前关闭，改低分候选。** [v1 §III-A–F、IV-F TableII](https://arxiv.org/html/2601.06566v1) 基础三阶段成熟，但同Regular采样/LLaVA对照中加LLM后MSR-VTT CIDEr36.5 vs无LLM52.3，YouCook2反向26.3 vs21.3，ActivityNetQA63.3 vs55.9（L214–232）。这是答案/标注粒度与aggregation收益反向的局部证据，可修正“聚合器总有益”选择；原文把一词关键信息丢失作为解释而非独立因果证明。1/1/2=4，低分关闭判断、无新增Books采用；不借整套成熟fusion升分。
- **MAS 07136 / HCI 07234：题摘层明确关闭。** 前者commit/issue比例维护观察，后者人类交互UI参考框架；没有摘要所述可改变模型/系统设计的具体新机制。按明确范围/贡献停止，不为证明关闭补全文或追时间。

### 反证/安全信号不按领域自动关闭：定点有效入口

- **MemGovern 06789** [v1 §3 L78–122](https://arxiv.org/html/2601.06789v1)：Index只初始symptom/diagnostic，Resolution保留rootcause/fix，Search索引再Browse细节，防未来修复信息进入检索表征；stars/closedPR与最多3次LLM checklist refinement仅质量代理，不是真值证书。拟准入的是可见字段分工，而非给memory card改owner。
- **SafePro 06663** [v1 §4.4 L188–204 Table6](https://arxiv.org/html/2601.06663v1)：原benign prompt下QA风险判断与IF执行风险分开、benign FPR<4%；GeminiFlash分别73.1/32.7、GPTmini81.5/44.4、Haiku92/77.7。支持“能认知风险不等于在任务中阻止风险”的窄反证，不以专业标签准入或排除；类别扩展结果不能混同原baseline，不授harness因果隔离。
- **CulinaryCut 06451** [v1 §4 L206–234](https://arxiv.org/html/2601.06451v1)：material/velocity→simulated force regression、力约束求速度上界，contact classifier再调BC style，存在具体物理控制边界而非菜谱任务移植。预测上限不是实际安全保证，不采用无条件通用力阈值。
- **VideoLoom 07290** [v1 §3 L107–129](https://arxiv.org/html/2601.07290v1)：slow/fast预算分配、输入输出离散frameID，SEG表示到SAM2 masklet；采用representation/interface具体差异，不把frameID称连续物理时间，不以数据集数量构成贡献。
- **MemTrust 07004：仍含糊，未因安全主题升入。** [v1 §III-E、IV-B、V-C–D](https://arxiv.org/html/2601.07004v1) 给k−1 dummy buckets、RA-TLS/OIDC custom client、CMOV/cache-pinning；原文L484自限best-effort statistical protection、非fullORAM，L492–498还保AMD/guest kernel/codebase/Python TCB及diskIO/working-size/network泄漏。决定准入缺事实仅为：超出成熟TEE+混淆组合的实际新protocol/threat boundary或可转移代价条件；不是要求整套安全proof或全附录。

### 本轮分区停点

89完整题摘 = 27+35+27，逐项唯一ID均记录。定点负侧后的分区为 **60拟准入 / 19含糊 / 7贡献前关闭 / 2低分关闭判断 / 1日期隔离**；QCaption从原8关闭中改为低分，Focus保持低分。19含糊的每项决定性最小缺事实已在对应行，不批量投全文队列。60拟准入须继续精确版本证据/评分/实际owner差额，不能将主题对应或成熟组合改名当作已通过；本轮没有授DAY、Evidence全池PASS或BooksPOST。

之后仅按root续授接作者已准备的小组必要原证/actual owner PRE，8已通过PRE不重做，不自换日或扩大来源发现。

## 续授小组 PRE：Monkey 06356 / PDR 06827 / PEFT-RLVR 06677

作者提供的 exact-v1 必要core及当前提案已独立读，实际owner完整局部邻接已读：Ch30 L86–127、205–263，Ch72 L257–317。以下评分沿拟采用命题2/1/2=5，不因Books是否有差额调整。

### Monkey 2601.06356v1：窄 Integrate，TRAIN-LORA / Ch30

必要原证：[exact-v1 §3.1–3.4、§5.1–5.3、§8](https://arxiv.org/html/2601.06356v1)，可复用本日 `increment-core-2601.06356v1-20261007.json`；§3与§8完整必要机制已实际读，§5必要对照/配置/消融定点读，未为窄采用扫描各附录。fresh HTML L194–220核了EMA、sequencewise边界与成本/理论异形问题。

- 原文实际增量：一个block既有不同projection adapter充当implicit experts，每个projection仍执行冻结base，只有adapter contribution被gate。Eq4为所有E中心的cosine/temperature logits先softmax，再TopK mask；不对选中k重归一。Kmeans初始化与非梯度EMA中心是额外state；空assignment不更新。这个分支不新增trainable router，也没有增加每projection的expert副本。
- 采用差额：实际Ch30条件rank及hypernetwork/两adapter硬选邻接已有“动态artifact身份与成本”，但没有上述跨既有projection的梯度外router。可在L227–241条件容量到hypernetwork过渡加入这一独立分支，明确选择从“多少rank/生成什么权重”变为“哪个既有projection增量对当前token起作用”。Center snapshot、初始化/更新规则、tau、k、共享projection和base/adapter共同定义执行身份；这是接口推断，勿伪称作者已交付完整生产artifact协议。
- 关键反侧：O(Ed) buffers、O(TEd) similarity/selection及初始化forward不免费；input-dependent gate不能静态merge成固定增量。§8 fixed expert count/聚类假设/初始化与超参敏感保留。§5.1 7/8B质量5run、§5.2 0.5B rank2/H100 batch8 acc2效率是不同人口，不拼成通用SLO或所有质量更好。不采用§4把不同shape projection当同空间sum的无条件表达力结论；不采用last-token sequencewise路由配方或互信息最优保证，其fullsequence状态复用于前token不授因果执行正确性。路由/质量/成本回归时静态LoRA保留。

### PDR 2601.06827v1：窄 Integrate，PLATFORM-SECURITY / Ch72

必要原证：[exact-v1 §4.1–4.3 Eq5/8/9、§5.1–5.3 Tables1–3](https://arxiv.org/html/2601.06827v1)，可复用本日 `increment-core-2601.06827v1-20261007.json` 的已读S4/S5必要段。fresh HTML Table3 L210–218独立核到与正文“after selection更优”不一致的普通Min-k局部值，隔离如下。

- 实际机制：先由raw/unweighted logprob选Min-k集合，后按这些token的原位置乘递减w，再以|S|聚合；全序列PDR-Loss以T聚合，不以权重和归一。改变selection先后、长度/alpha或归一口径即不同score，不能静默替代。
- Owner差额：Ch72 L279–308完整论点已要求loss/control identifiability、cue/entropy nuisance与Unknown，但没有position prior及“raw选集合→原position权重”的score接口。可在membership sensor的entropy correction前后同局部加入position-weight分支，保留raw score、同source controls与stress人口；不能以常见loss原则换新owner词语，真正新增是score顺序和适用人口条件。
- 关键反侧：§4.1明确跨位置不同随机变量，conditional entropy定理不推出逐token必然单调或早token即memorization。MIMIR Avg*排除Arxiv/HackerNews，不能写完整MIMIR均值改善；T32非默认alpha1。Table3 Pythia6.9B/T128普通Min-k Base69.5、Before68.1、LPDR-after67.8，故声明顺序并不在每种baseline优于反顺序或原分数；Min-k++才是Base69.8、Before70.3、after72.4。采用score身份而非顺序普遍最优，部分WikiMIA退步同时保留。额外logits/position/corpus calibration付费；未获得memorial truth、copyright、通用FPR或隐私保证，失准仍回原score/provenance/canary/Unknown。

### PEFT-RLVR 2601.06677v1：Existing / No Change，TRAIN-LORA / Ch30

必要原证：[exact-v1 §2–4、Limitations](https://arxiv.org/html/2601.06677v1)，本日 `increment-core-2601.06677v1-20261007.json` 必要机制/对照/限制实际已读。A40 48GB、24h约300updates、OpenRS7k、五≤1.5B checkpoint、rank8/64/256、rollout8/3584；MATH500用于选rank/checkpoint，AMC/AIME才后验heldout。单seed固定LR/alpha，作者自承collapse可能由更保守LR或alpha/rank ratio缓解；entropy降不等正确，preoptimized先验刚性未被因果隔离。

拟采用的有限设计反侧是“rank配置与初始化更新强度/尺度/稳定窗口必须分别核；固定数值同LR/alpha的rank或checkpoint比较不能证明结构性刚性/最优rank”。实际Ch30 L107–115已经逐项要求更新强度/方向≠rank、匹配预算独立LR/scale搜索、稳定窗及rank/batch/target/scaling/schedule/数据绑定；后续L117–125还有scale/初始化分支与独立sweep。无需再加一篇名称/有限人口重复该论点，判Existing/NoChange。该判断不撤其贡献准入、不降5分，也不自动吸收作者“warmstart/relaxclip/rank256”等未验证recipe；本轮未作entropy或RL另owner的扩展书稿。

本小组只完成上述最小命题与实际局部的非作者PRE，Books锁与实际写后POST交root。没有Books写入、末注编辑或全日完成授权。

## 续授小组 PRE：Circuit 06338 / ArenaRL 06487

本轮已刷新AGENTS/Research/Report/Prompt、daily来源用法及本日停点；只加载Jan14，不重做八项及上一组三项的未变化证明。

### Circuit 2601.06338v1：窄 Integrate，MULTIMODAL-REPRESENTATION / Ch23，3/1/2=6

必要证据：[exact-v1 §3–5及§6必要讨论](https://arxiv.org/html/2601.06338v1)，复用本日 `increment-core-2601.06338v1-20261007.json`；S3/S4/S5实际完整必要机制已读，S6截至References讨论已读，不将其尾接附录算已核。两对象/三shape/两color/八relation灰背景，从零训练不同DiT规模，96prompts与cv2识别构成受限合成证据。

- 原文增量：RTE的relation head先写image positional tags、后object head读tag生成shape；head-specific attention消融与VO注入支持这条局部因果链。T5 contextual encoder却将relation混入shape2/shape1表示：遮关系词无明显影响，遮shape2同时伤shape/binding/relation；shape2表示减原relation factor、加2倍另relation vector可改布局。因而“关系词attention/消融阴性”不等关系语义不存在，encoder身份改变可见诊断单位。
- 实际owner邻接：已完整顺读Ch23 L1100–1155。L1120附近object hallucination分write/read，后PIH分人口/head干预，随后whole-sequence vs last-position patch分干预单位；尚没有上述跨text encoder导致关系信息迁移/关系词阴性这一具体失效边界。可在write/read后、PIH前补该分支，让encoder/被读token/被改head先定义，保留后面不同patch单位论点；不另建“电路章”或重复一般attention≠因果。
- 反侧与停止：同训练模板ID关系准确不等鲁棒机制相同，T5轻加`the` filler约40%关系退步，不能写成预训练语义总更稳；T5因果改向只在该toy embedding factor操作内成立，拟合/投影variance与可视化不证明自然图像通用线性可控。RTE非pos版permutation失败、tiny nano亦不同，不授一个head所有模型复用或因果唯一。白盒读取、聚合/扫描、消融与向量拟合有成本；encoder/任务/扰动失配时回归行为评测及输入级反事实。必要支持/关键反侧到位，未扫所有训练/图库附件。

### ArenaRL 2601.06487v1：窄 Integrate，TRAIN-GRPO / Ch33，2/1/2=5

必要证据：[exact-v1 §3.3、§4.2–4.6 Eq3/6/7、§5.3、§6.1–6.4及AppendixA](https://arxiv.org/html/2601.06487v1)，复用本日 `increment-core-2601.06487v1-20261007.json` 与 `increment-necessary-extra-2601.06487v1-20261007.json`。S3/S4/S5必要段实际已读；S6配置/拓扑/条件评价/一致性已读，不采用业务宣传尾段。未因局部judged benchmark而关闭，亦未把摘要名次当证据。

- 具体机制：同prompt组含greedy anchor，先N−1 anchor比较做seed，再N−1 single-elimination比赛，以survival depth与同tier既往平均分排序；rank0最佳，`r=1-rank/(N-1)`，再本组mean/std标准化。每match按交换presentation order作两次judge调用；2N−2是match数，不是API调用总数或token费用。新差额是用比较拓扑产生组reward，不是发明GRPO归一。
- 实际owner：已完整顺读Ch33 L55–140（reward来源到group-relative mean/std、小例/零方差组）。有reward proxy≠truth和组归一，但没有anchor seeding→linear tournament→rank quantile这一接口；可在Group-relative advantage前的reward来源尾部加窄分支，再交回既有标准化。Anchor/sampled人口不同、match协议、tie-break、judge/context和topology要绑定；排名不能凭产生非零std保证真有质量差额，这是设计审计推断，不称作者已证明noise-free。
- 反侧：pointwise基线同judge/rubric但只给answer，Arena给process-context；收益不能唯一归于pairwise或topology。拓扑比较N8/K8；main OpenTravel/Writing N16/K8，DeepResearch N8/K4，不能混人口。AppA冷启动32H20/3epochs，RL8H20/Adam1e−6；多judge/rollout/长trace都有费用，不授所有预算公平。DeepResearch winrate仅valid outputs人口，必须同时保valid rate，73.9%human agreement不认证无judge-overfit。Swapping减position bias不证明完全消除；roundrobin排序也非无噪声gold truth。有限5topology均值不能授全局最优或所有subtask最好。比较一致性、可核outcome或费用不合算时保留pointwise/outcome reward及独立评价。

两项仅完成窄非作者PRE，root负责写锁与实际POST；本轮未改Books/Report/LS。

## 19项含糊准入：决定性事实定点收束

以下继承89完整AB的原始分区，但不继承AB为方法证据。仅实际读精确v1决定准入所需节段，未把19项全部投全文/附录队列。拟准入仍待评分、必要证据尾段及实际owner PRE；贡献前关闭不是“没读实验所以排除”，而是已读具体规则没有超出成熟组合的新增机制/条件。低分判断保留实证反侧，不将小规模、局部、负面或领域本身作关闭理由。关闭是本次采用范围的判断，若作者有具体新增反例可重开；不是断言全文不存在任何贡献。

| ID | 本轮处置 | 已读必要原证与决定事实 → 采用范围 / 停止边界 |
| --- | --- | --- |
| 06490 BiMem | 贡献前关闭 | [v1 §4.2–4.3、§5.3 Tables2–3、Limitations](https://arxiv.org/html/2601.06490v1)：LPA聚facts成scene，再蒸馏persona；冲突时LLM生成Δscene追加，facts不校准，检索作父子spreading activation。已核真实条件，不只是摘要名词；但这里仍是层级摘要＋派生视图反思＋邻接扩检，未见不同于成熟策略的新冲突仲裁/验证条件。表中Fact+Persona甚至不优于Fact-only，但不由此断言persona无用；稳定persona假设亦不能推出动态偏好安全修订。无需把同一组合换“authority”词语收入Books。 |
| 06377 HiMem | 拟准入 | [v1 §2.4–2.5、§3、§4.4](https://arxiv.org/html/2601.06377v1)：不是仅topic/surprise OR分段；明确以Note独自不足 **且** Episode足够的双条件触发reconsolidation，随后分独立/可延伸/矛盾执行ADD/UPDATE/DELETE，episode保留。可采用该条件化更新接口，不能把LLM sufficiency当事实验证；forgetting非已验证增益，latency仅retrieval口径、Adversarial人口排除保留。 |
| 06799 CIRAG | 拟准入 | [v1 §3.4–3.5、§4.5](https://arxiv.org/html/2601.06799v1)：triple→sentence→document逐层试答，首个不输出指定refusal者停止，全部refuse仍回document回答；history integration过滤并提出下一查询。可采用粒度升级的具体gate与task-dependent单粒度反侧，不能称support verifier、可靠abstain或第一非refusal必正确；不以级联名词本身准入。 |
| 07004 MemTrust | 低分判断，拟4 | [v1 §III-E、IV-B、V-B–E](https://arxiv.org/html/2601.07004v1)：RA-TLS/session、TEE内多path/noise/dummy bucket组合；V-C明确非fullORAM、仅best-effort，k2搜索付双CPU/理论半QPS。V-D保留guest kernel/Python/硬件TCB、I/O工作集和流量泄漏；V-E还有客户端quote验证与签名依赖链。可报告“confidential payload不等oblivious access、成本口径不得将透明加密与dummy检索混成<20%”的有限反侧；未见新安全协议/保证，暂1/1/2=4，不因安全主题升候选，不授具体微秒/百分比跨平台通用。 |
| 07023 CloneMem | 拟准入 | [v1 §3–6，尤其Table6](https://arxiv.org/html/2601.07023v1)：状态/阶段生成trace，semantic evidence units与trace多对多；控制器关闭后同retriever比较。k20下memory semantic recall较好却raw-context QA85.98高于memory-only69.50/combined69.20，足以改变“检索记忆指标更高即答案更可靠”的局部设计判断，不靠新avatar任务准入。Table2 1183与§4.1约5000人口冲突隔离；synthetic生成/groundtruth相关性、固定retriever/disabled control边界必须保留。 |
| 06282 Amory | 拟准入 | [v1 §3、Alg1、§4 Table2](https://arxiv.org/html/2601.06282v1)：非仅叙事tree；连续一段无相关update才inactive consolidation，可重激活；外围事实semanticize，plot仍绑定。Table2 temporal分数no/rapid/inactive为83.1/82.3/87.7，支持“何时整理”不是越快越好这一具体选择。未给出的turn阈值不编；局部LoCoMo反侧不推出普适叙事优势。 |
| 06860 ETAgent | 拟准入 | [v1 §4.1–4.2](https://arxiv.org/html/2601.06860v1)：group question selection同时用正确率std和tool-call-count std，经Pareto front/crowding选题；相比仅正确差异筛题，新接口保留效率存在差异的训练组。采用信号身份/双轴筛组，而非将熟悉NSGA或两阶段RFT称新发明；同组tool/length reward不保证正确率不降，不授一般工具最优。 |
| 07525 InWriting | 贡献前关闭 | [v1 §3–4](https://arxiv.org/html/2601.07525v1)：预定义trigger切入regex FSM，推理不受限、最终format受限；此前混合delimiter方案已在相关工作承认。已核trigger是配置而非新学习/停止协议，此采用范围是成熟两phase constrained decode，没有新的validity边界或受控反证，不能仅因格式FSM收入。Alg2未刷新α的循环亦不暗补成可执行recipe。 |
| 07806 GenderECE | 贡献前关闭 | [v1 Gender-aware calibration定义](https://arxiv.org/html/2601.07806v1)：按预测male/female组各算普通bin ECE再平均，target是人类bias标签。具体量不是新校准目标或已验证公平误差关系，而是成熟group calibration切片；榜单/职业性别场景不能单独触发系统增量。校准对人类bias亦不意味着规范性公平。 |
| 07782 ToolQP | 拟准入 | [v1 §3.2–3.3](https://arxiv.org/html/2601.07782v1)：teacher query去目标tool-name并逐步加信息至可检索，保失败→成功query轨迹；RL对整条query序列聚合tool集合算nDCG/Recall，而不是逐step给分，另有format/plan regularizer。可采用tool-composition集合覆盖的credit接口，不把检索覆盖当实际工具执行正确/安全；不能把GRPO或普通query decomposition本身称增量。 |
| 07329 BayesRAG | 低分判断，拟4 | [v1 §2.3、§3.2–3.3 Table5](https://arxiv.org/html/2601.07329v1)：cosine→DS mass→BetP likelihood，再乘graph/layout prior是成熟证据融合组合；没有校准概率或独立模态证明。真实有限反侧是§3.3声称“isolate Bayesian”却将visual候选Top20改Top512，再posterior rerank，主收益混候选池；linear fusion40.6与full44.1仍可作该配置局部观察，不因此抹去实验。检索76.6与生成44.1亦非同指标可相减。拟1/1/2=4，只报归因/接口边界，不把新modal任务或Bayes名词升候选。 |
| 07779 OSSymphony | 贡献前关闭 | [v1 §3.2–3.3](https://arxiv.org/html/2601.07779v1)：milestone图片保留、其他摘要，pre/post/zoom VLM复核分类，独立browser收教程再distill、grounder/coder协同；实际主规则仍是熟悉的checkpoint摘要/视觉验证/工具隔离组合。没有据本次拟采用范围找到新可检验的milestone更新/责任边界；不以OS任务/多agent数量和排名自动准入，亦不把VLM分类当独立环境真值。 |
| 07477 JudgeFlow | 贡献前关闭 | [v1 §3.2、§4.3 Table3](https://arxiv.org/html/2601.07477v1)：仅failed traces由judge排各block责任，Borda汇总选最差block，用其worst logs改prompt；消融83.8→无block81.8/无judge80.6。已核规则及消融，不因实验待读排除；但所选命题仍是失败定位＋聚合noise＋局部优化的成熟组合，汇总责任一致性本身引用前作，未提供新rank有效性条件/新失败边界。不能将rank等同causal责任。 |
| 07711 AgenticRAGcompare | 拟准入 | [v1 §5.4、§6](https://arxiv.org/html/2601.07711v1)：同Qwen系列比较中FEVER F1降低28.8被归于错误intent route；query rewrite约+2.8NDCG，但增加retrieval iterations无额外收益vs rerank；FIQA/CQ input/output费用约2.7×/1.7×、3.9×/2×。可采用组件级routing/rewriting/iteration差额与失败条件，而非泛称Agentic各有取舍。65.4%judge-human agreement及5%样本312pairs限定，one-tool harness不推全体agent。 |
| 07260 ActiShade | 拟准入 | [v1 phrase detector / training方法](https://arxiv.org/html/2601.07260v1)：候选phrase embedding加Gaussian noise，用池化generated-output distribution最大cos选择变化最小phrase，再补检；训练分Q+phrase正、仅Q半正、皆无负的双contrastive项。新入口是遮蔽检测信号与半正层级，不是通用query expansion。最大cos是sensor不是“真正不重要/被忽略”的因果证明，perturb预算/稳定性与retrieval side effects待作者必要证据。 |
| 07577 TDP | 贡献前关闭 | [v1 §3.2–3.4、Alg1、§4 Table1](https://arxiv.org/html/2601.07577v1)：DAG ready nodes、node-scoped历史、局部replan、batch后修unfinished graph均为成熟依赖调度/隔离/repair；未定义新的dependency invalidation或完成节点失效传播协议。已读实际主表而非仅看标题；TravelPlanner平均分上升却GPT4o FinalPass0、DeepSeek FinalPass0.83与CoT相同，故不授约束成功保证，但这类指标口径负侧没有将组合变成新的系统条件。 |
| 07054 SFT/CPT/RAG | 低分判断，拟4 | [v1 §IV、§V-B、TableII](https://arxiv.org/html/2601.07054v1)：2024事件晚于所选7B cutoff，DeepSeek题训练/GPT题评价；CPT读raw corpus，SFT用MCQ classification head，RAG另检索/rerank/3-shot。TableII确有CPT小增、RAG/SFT更高这一局部反侧，可限定“读新事实不自动获得该MCQ任务能力”；比较同时换objective/head/interface，不能证明知识注入方法的一般优劣。拟1/1/2=4保留，不因小模型/局部反证排除，亦不把已知训练任务匹配换场景升机制贡献。 |
| 06496 3DCoCav2 | 贡献前关闭 | [v1 §3.7–3.8](https://arxiv.org/html/2601.06496v1)：同冻结CLIP scene embedding检索text descriptor summary，采N captions再language judge据summary择优/可topk vote。已核奖励依赖同一encoder视图，不是独立空间oracle；本次规则是成熟retrieval-conditioned Best-of-N与多任务captioning组合，未提供新的搜索/奖励条件或独立OOD反证，不能以3D任务/scale名词收。 |
| 06944 SketchJudge | 拟准入 | [v1 §3、§4.3 Table4](https://arxiv.org/html/2601.06944v1)：reference改善binary grading不总同幅改善error diagnosis；CoT对三个被测模型均退，例如Gemini accuracy77.74→76.16、errorF158.30→55.68、FNR.263→.351。可采用视觉判对与诊断分离、reasoning scaffold可靠性反侧，不靠新教学benchmark准入。“CoT放大早期perception error”为解释而非已隔离因果，rubric也非全模型正收益。 |

本轮19收束为 **9拟准入 / 7贡献前关闭 / 3低分关闭判断**，没有因普通实验待读保留为不透明held。合并本组89的当前分区为 **69拟准入潜力 / 14贡献前关闭 / 5低分关闭判断 / 1日期隔离 = 89**；原60与新增9均不是已通过评分或Books候选。日期隔离不再追精确时间。下一实际PRE只按作者已准备且root授的小组，不扩大到69全文或新发现。

## 续授 prepared core PRE：DVRP 06801 / CLU 06675 / Forward–Backward DPO 07199

### DVRP 2601.06801v1：窄 Integrate，MULTIMODAL-REPRESENTATION / Ch23，2/1/2=5

实际必要原证：[exact-v1 §3.2–3.3 Eq4、§4.1/4.3 Table4、AppendixB/D及Limitations](https://arxiv.org/html/2601.06801v1)，已读本日 `increment-core-2601.06801v1-20261007.json` 方法/配置/消融/限制及 `increment-necessary-extra-2601.06801v1-20261007.json` A2/A4。未扫剩余case或无关附件；B/D必要配置已读不等于整个实现已验证。

- 精确接口：对同图/query构clean、random-patch-mask、diffusion-noise三视图；沿clean policy采到的同一trajectory，各生成步计算categorical-output token KL并求和。最大化目标中`+λnec KL(orig||mask) - λrob KL(orig||noise) - λent(Hmask+Hnoise)`分别鼓励区别、保持与惩罚高熵，交回outcome GRPO/DAPO；不是两种扰动都要求一致，不是teacher/ref KL，后者原设置关闭。使用完整输出分布的差异，不是已知答案变换关系或独立视觉真值。
- Actual owner：完整顺读Ch23 L842–908，Connector shortcut L880–888已有原始/反事实视频的“答案应变/应保持”、transform/router/Gate与strict pair correctness。尚无上面clean轨迹上的两种KL方向和entropy分支；适宜在现有paired-reward之后接受限policy-level regularizer，明确它与前文verified answer relation的不同监督接口，而不复述遮蔽/反事实原则。
- 反侧：random mask并非critical-region oracle，noise保语义是应验假设，不因扰动名字签发；最大化KL可由无关输出差异满足、低entropy不等正确，这是本次设计审计推断。AppendixD把noise consistency称safe regularizer，不能照收安全/因果语言。Table4 full总体最高但Path78.3低于mask79.2、Rad79.9低于noise80.2；Table7 medical mask从.2到.6均值74.3→71.4，不能把math强扰动移植细粒度医疗。3B/7B、Qwen家族、4A800、额外视图forward/KL/调参成本限定；平均准确率不是真实医疗有效性。B1 top-p .9与Tables5/6 .99冲突，不采可执行推理配置；不授独立noise/mask因果唯一、规模通用或无tools生产收益。
- 停止/回退：支持该有限训练接口及domain扰动反侧已足够，原outcome-only、经核paired-reward仍并存；变换有效性、原答案/能力、entropy或成本回归时停用辅助项。根协调锁及实际POST，本轮无Books写入。

### Forward–Backward DPO 2601.07199v1：窄 Integrate，TRAIN-DPO / Ch34，2/1/2=5

实际必要原证：[exact-v1 §3–7，Eq3–5、Table1](https://arxiv.org/html/2601.07199v1)，已读本日core的方法、训练/evaluation定义、结果及限制，不由摘要的“calibrated verifier”定性通过。

- 实际owner：完整顺读Ch34 L117–195（sequence logprob与same-prefix→step反事实→token/segment单位），及L421–478（固定pair/negative/pair factual validation交接）。原文要求chosen/rejected同一x，却未区分生成solution的x与给定candidate后判verdict的x⊕a；新差额是两种pair对应不同条件任务/正确标签。适宜接在same-prefix规则之后、step-level反事实之前，后面过程单位论点照旧；不称新DPO公式、不补joint训练或latent技能正交。
- 源接口：forward pair=(问题,正确trace,错误trace)，backward pair=(问题⊕candidate,正确verdict trace,错误verdict trace)。教师同Llama3.1-8B，2000题最多5次采样构实错，LoRA Q/K/V/O r16/alpha32、beta.1、1epoch约119steps；实负例权重1.2不是必要部署recipe。双任务采样/验证和额外训练都计费，hardware未披露。
- 独立可用反侧：同源表所报forward accuracy更高，却ack下降；backward FPR更低而accuracy相近，不同质量轴不能用一个成功分数互相验收。BASE/FWD350、BWD250不是同评价人口，Ack又分别条件于模型自己生成的错误集合，不能证明固定错误池上的验错因果或严格不迁移。较低FPR亦不证明错误识别好、概率校准或FAIL必可靠；ack .678→.447/.463只作有限观察，不授DPO普遍过度自信/置信度因果解释。
- **受影响证据隔离：** Eq5定义PASS-positive F1，Table1 .580/.424却由表中Accuracy/Ack/FPR重建时符合FAIL-positive。按已报四舍五入值，PASS-positive约.897/.905，FAIL-positive约.580/.424（算式核对，不是额外模型实验）。不能将表悄悄改正类、引用“CalibF1下降”作已确认校准退步，backward本来没有该值；采用的三轴分账不依赖这个冲突。Pair/verdict标签或独立评价不可靠时，保留可靠普通solution pairs、外部验证/人审或停止更新；不用模型自评赋truth authority。

### CLU 2601.06675v1：中心遗忘结果暂缓；现有审计命题 No Change，不授其成功机制 PRE

实际必要原证：[exact-v1 §3.1–3.3、§4.1–4.3、Limitations/Ethics](https://arxiv.org/html/2601.06675v1)，已读本日core；AppB仅`increment-necessary-extra-2601.06675v1-20261007.json`的reference关键词probe及表头，**不宣称完整附录已读**。probe没有把reference定义修好，停止，不扩大原UNLEARN全文或所有表。

- 实际完整owner Ch72 L348–410已有secret substrate/observer、跨channel retained utility、单通道clear≠系统遗忘及MeGU shared/unique feature不签唯一因果。语言×script×direction是合理的更细observer population；但仅把此manifest列举进既有observer合同，没有取得本源独立的迁移/删除反证时，不足以创造新的Books差额。原脚本/romanized、one-to-one/many-to-heldout-one确为本篇实际实验设计，保留来源记录，不自动提升为有效删除机制。
- 中心冲突：§3.1明写FQ是unlearned与**original**输出的two-sample p-value，p>.1为成功。按这个文字，未拒绝与原模型同分布不能认证forget-set删除；零变化也可能过这一门，这是检验定义的审计推断，不断言实际代码零更新。不能猜original其实指retrained、不能替换TOFU reference、也不把正文/表checkmark视为纠正。Table本身utility口径与“base相对1”叙述亦须隔离；不采用任何FQ成功数字、迁移非对称/romanization改善结论为已核删除证据。
- §4的shared/residual projection是以已有UNLEARN discrimination作构造，t-SNE重叠仅相关；所谓共享移除各语言成功、残差移除只目标语言成功依赖同一未闭合FQ，因此**不能仅去掉数字后改写为已证实因果机制**。抽象“shared与residual要分别干预并验retain/forget”已由实际MeGU邻接覆盖，不用ownership词语重新收。
- 本轮选择：保留准入潜力/作者拟5分，不以metric冲突将整篇贡献前排除或擅降分；但本次Books中心采用暂缓，已有独立审计通则判NoChange。重开只需官方明确reference/检验定义，或不依赖该p-value的可比forget/retain行为证据；不是无限补附件。若根选择新增manifest例子，须作为本书工程审计推导而非本源实验已验证的新长期机制，本轮不签该扩展PRE。未授全日/BooksPOST。

## 续授 prepared core PRE：Veto 07155 / FASC 07197

本轮恢复已重读AGENTS、Research/Report/Prompt与来源说明/daily组；仍仅Jan14。前八项及已通过组不重做。只使用本日core/theory-extra和当前实际owner，不读其他日期或无关附件。

### Veto 2601.07155v1：窄 Integrate，TRAIN-SFT / Ch29，2/1/2=5

已实际读 [exact-v1 §3–5及AppendixA](https://arxiv.org/html/2601.07155v1) 必要方法、Alg1、对照/配置/消融与理论；复用本日 `increment-core-2601.07155v1-20261007.json` 和 `increment-theory-extra-2601.07155v1-20261007.json`。采用概率target接口，不采用其“普遍稳定/消除mode collapse”理论宣传。

- Actual owner：已完整顺读Ch29 L238–309及378–452。L248起gold坐标、tail、hidden-subspace、latent短时监督及teacher/checkpoint选择分别改变target/表示/监督时序，L388起offline correction/teacher-student occupancy控制访问状态；这些实际论点未有同student prefix上的`Q_y = P_T(y) P_S(y)^β / Z`乘法目标。适宜接在latent短时引导后、teacher选择比较前；不要混成teacher/student rollout mixture或普通temperature。
- 窄采用：student自己采trajectory，同一已访问prefix取得teacher/student两份next-token分布，由乘法归一构Q；β0回teacher、β>0相对降低student当前低概率坐标的target份额。更新采用固定目标梯度分支，**A.3明确treat Q fixed during gradient step**，不能误写为作者遗漏此假设；原文未核code/autograd，故不声称全部实现已正确stop-gradient或将穿过Q的total derivative混为同算法。Teacher可靠但支持差异大时是可选监督分布，双方概率同意不等事实正确；学生漏掉有效mode的保护也可能成为自我锁定，这是设计推断而非本源已证明副作用频率。
- 理论与recipe隔离：A.1计算单概率项`p^β log p→0`，不是一般参数gradient界。对固定teacher/q的softmax输出，forward KL的logit gradient为`p−q`，原`P_T/P_S`比值发散不能忽略链式就授parameter-gradient必爆；此为独立算式核对，不取消有限训练观察。A.2只解固定点代数，0<β<1下温度形式不证明优化到达/收敛、β1奇点亦不能隐藏。Alg1反复`β←β(1−i/N)`与正文linear-from-initial schedule不同，不修公式、不授可执行线性schedule；reverse-RL桥不是本轮必要采用，不用它签熵/最优保证。
- 有限证据/代价：Qwen2 .5B/7B、2H10080GB、lr1e−5/3epochs、student1k与teacher7k/10k，β经grid；Gemma2另2B/9B人口不混。GSM8K accuracy、HumanEval pass@k、GPT4o-mini DialogSum winrate分别保身份；有限局部收益不证明teacher真值、summary faithfulness、普遍稳定或同总预算最优。Teacher/rollout/概率归一/搜索成本另计，完整生成长度/precision/full compute未披露。目标支持、coverage/entropy、held-out行为或预算退步时，保留固定teacher普通KD、原student或更可靠监督。支持/关键反侧已足够，不需未变化附件；可由root协调窄写及实际POST。

### FASC 2601.07197v1：中心机制 Books 暂缓；有限比较仅报告；既有PPL通则不重复写

已实际读 [exact-v1 §2–4、Limitations及AppendixB](https://arxiv.org/html/2601.07197v1) 的必要定义、配置、对照、结果与中心推导；复用本日 `increment-core-2601.07197v1-20261007.json` / `increment-theory-extra-2601.07197v1-20261007.json`。fresh精确HTML B.1 L338–345再核印刷等式，不是二手转述或抽取符号猜测；没有遍历其余附件。

- Actual owner：完整顺读Ch49 L480–540、1393–1448与1001–1054。L511–513已将output reconstruction与empirical-Fisher近似目标分开；L1407–1413已有activation whitening/SVD、保留原FFN通道、matrix rank预算及代理不授全局任务最优。具体未有本源activation-gradient cross-covariance矩阵选子空间及ρ选层，不能只凭同属压缩判Existing。但本篇拟用来签“最小loss-change/保留事实方向”的中心解释依赖以下未闭合推导，故不能只删optimal一词就改成已验证loss-sensitive机制。
- **独立反例与更早错误：** 令d2，x=(a,b)、g=(c,d)四独立等概率±1，P=diag(1,0)。二者中心化，Σxx=Σgg=I均full-rank、Σxg=0；可由平滑样本loss `L(x;g)=gᵀx+2`产生该g，符合目标里的gradient角色。遍历16种组合（算式检查，非LLM复现）：原Eq3 `E[(gᵀ(I−P)x)²]=E[(db)²]=1`；印刷Eq4 `E tr((I−P)ᵀ x gᵀg xᵀ(I−P))=E[(c²+d²)b²]=2`；Eq5右侧因Σxg0为0。因此Eq3→Eq4的收缩顺序已经错误，Eq4→Eq5亦不成立，**不只是补一个四阶→二阶独立假设**。上述反例已满足本文所列centered/full-rank条件，加Σxx的ε也不修这个等式。不得自行改矩阵/补QR/改generalized-eigen recipe授最优。
- AppendixB2自己承认empirical Fisher不同于Hessian；near-equilibrium/centered/二阶可微并不自动使任意校准分布的外积成为真Fisher或曲率等价。本轮不授其`O(||E[g]||)`、ρ是唯一知识位置、低variance是事实而高variance是语法的因果结论。ρ定义只是线性cross-covariance代理，其阈值/层函数及校准分布仍需独立验证；本轮无需继续搜所有failure appendix来补中心证明。
- 有限作者结果仍保留：C4 4096、六model families、40–80%rank；Table1 Mistral50%下SVD/FASC PPL6.12/5.65、MMLU51.5/57.8，原模型62.3；Table3 BLiMP、mLAMA、NQ对照与Table6 relation切片可作局部经验，不因理论错误虚称表实验未发生，也不推出有效容量翻倍（7B Mistral vs13B Llama2跨模型）。Table5 A100/batch32/seq512的latency/throughput不明prefill/decode/聚合口径、precision/SLO未披露；gradient采集/矩阵/sketch/校准与约1.5×SVD构建成本不化成生产Serving收益，未release code不等已核实现。
- 隔离/处置：保留原2/1/2=5及准入，不用降分/改标签消除争议。中心广义特征方向与“知识保留”解释暂缓，有限表结果仅Report。独立剩余的“PPL不保证全部任务、代理目标不授任务最优/真实kernel”已经由Ch49 L1007、1041、1049附近完整段承载；不能为这些通则制造diff，也不把这项有限Existing撤销该材料准入。重开需要官方纠正目标/矩阵/投影条件与相应证明，或明确不依赖错式的执行方案及可比任务证据；不要求通用复现或遍历附件。当前无可签的新窄Books写锁，未授DAY/POST。

## Jan14 五项定点贡献与证据裁决（root，2026-10-08 续审）

本组仅处理此前完整题摘已有的五个身份，不新增发现入口。续跑不改变原窗口或补充窗口；独立裁决与实际写后是不同阶段，不授整日完成。

- **2601.06649：贡献前关闭。** 实际读本日 admission-core 的 §3/4/6。固定训练设定的局部 token sweep 使用每分钟 RMS 功率及含 tokens/epochs 的效率分母；不是完整能耗积分，也未建立可迁移的质量—资源前沿。fallback 输入和跳过非有限 batch 又影响真实执行人口。保留原证及这些限制，不因小模型排除，不将指标随规模变化当新训练机制；不评分、不写 Books。
- **2601.06965 OmniPersona：贡献前关闭。** 实际完整题摘、[exact-v1](https://arxiv.org/html/2601.06965v1) §2/3、§4 的必要配置和 Tables1/2、AppendixB 与 E1 的必要参数分工已读。原文相关工作已有 dual soft prompts 与 self-prompting；本次把概念 prompts 路由到冻结 BAGEL experts，自己读出概念再重写生成提示，并增加 editing 任务。所核对照尚未提供超出这些成熟分支的新有效性条件；t-SNE 不识别冲突因果，CLIP-T 和长文本 PARG 对照也不支持全面优胜。保留已读证据，不因 Books 已有主题、审阅成本或样本少而关闭；不评分、不入正式候选。
- **2601.06605 Sissi：5 分，中心争议隔离。** 实际 [exact-v1 §4.3](https://arxiv.org/html/2601.06605v1#S4.SS3) Eq12–18：Eq16 两个分别按行归一的 attention 矩阵，其全元素和同为 query 数；多 query 时比值恒为1，Eq17 得0.5，单 query 的对数比为0/0。固定比例最小化与“随样本动态平衡”不是同一结论，不能替作者改 normalization。作者另核 §5 的 Full/FSSI 对照不能反向修正错式。保留准入与分数、双方证据；Books 暂缓，重开只需纠正统计量/归一轴的官方精确机制或不依赖错式的可比证据。
- **2601.06931 REFLECT：2+1+2=5，标准完成，具体已有覆盖。** 实际 [exact-v1](https://arxiv.org/html/2601.06931v1) §3、§4.1 的设置/测量/主要结果、§4.3、Limitations 和 B.2；48 原图、480 变体的配对审计不代表人口公平。2AFC 约20%被不一致或解析规则剔除，方向及有效分母须保留；脸外差异非零，年龄/表情亦可能变化，故不签 strict demographic causality。实际 Ch66:175–228 与462–503已经承载 matched intervention、self-report 权限、极性/方向、固定统计单位与条件分母；本篇是受限验证，不需新增重复正文。硬件、完整精度/运行预算未披露，未读所有图或统计附件、不称复现。
- **2601.06451 CulinaryCut：2+1+2=5，窄整合及实际写后通过。** 必要 [exact-v1](https://arxiv.org/html/2601.06451v1) §3/4、§5.2 与 D.1 支持 contact classifier 触发剩余 coarse proposal 的 style 转换，不是 force-memory 快反馈或安全 commit。作者窄写后，root 独立实际顺读 Ch26:428–468 的完整邻接、新456段及自身末注：人口改变/20次模拟、拼接索引未闭合、额外费用、材料漂移回退和 force limiter 非实机安全均近文。POST PASS，Ch26 锁释放；未核 artifact 或复现。

### 07737 / 07582 的最小 owner 决定（同日独立续核）

- **07737 UAIT：5 分，具体已有覆盖 PASS。** root 实际读原 v1 §3.2/3.3、§4.2/4.3，并顺读 Ch66:175–228、727–743。agent–patient 对换检验有向关系而非实体共现，现有 paired intervention、fixed population 与 directed-relation/Unknown 已具体承载。保留 prose/Table6 的 .79/.85 差异及 Table5/7 CLIP 标签对调，不采用排名或整体架构因果；生成的罕见图不证明训练未见，letter-only 不排除 hidden reasoning。作者余必要证据与日期记录有效复用，无 Books 修改。
- **07582 ES-Mem：2+1+2=5，窄整合 PRE 与实际 POST PASS。** root 实际读 v1 §3.2/3.3 Eq5–10、完整 §4/5，以及 Ch77:254–305、362–395。前后 summaries 与 boundary raw 构造 transition description，先匹配变化锚点，再让 ±w 邻接事件继承最大 anchor score并混合 summary score，是现有普通 anchor/SEEM source join 尚未具体承载的读取选择。只授 Ch77 一短分支与自身末注，不采用全 segmentation recipe 或 confidence/MI 真值；Tables1/2 的任务退步、Table3 未计写入维护及更高费用、Table4 异协议报告均限定采用。root 随后实际顺读 Ch77:254–308、新282段与自身2131末注，raw/flat 与短预算回退近文，POST通过，锁释放；不授日级完成。

## 同日续核：两项准备材料与贡献前关闭（root）

- **07023 CloneMem：2+1+2=5，标准完成，具体已有覆盖。** 实际读保存的精确v1 §4/5/6，并完整顺读 Ch77:295–326、1229–1253。检索指标与 reader outcome、写入损失和候选遗漏的分责已由上述实际论点承载。Table6 extracted semantic recall 不等于 raw recall，也不识别压缩的唯一因果；预处理索引、关闭交互循环与未配内容预算限制采用。保留作者已读构建/限制和公开日依据，不新增 Books。
- **06282 Amory：2+1+2=5，标准完成，仅报告。** 实际读保存的精确v1 §3、§4.1/4.2/4.3 的必要方法/对照与 Limitations；Ch77:407–447 完整已读。作者明示单 narrative 上一 iteration 无新 binding 后触发维护，不是整个会话静默；不冒称两者完全相同。该局部时机对照不足以改变长期维护合同，异步不证明 deadline、并发或全生命周期低成本。Table1/2 overall 口径及部分任务反侧保留，不把不写书误写成贡献前排除。
- **06663 SafePro：贡献前关闭，不评分。** 完整题摘与必要v1 §3 已实际读；本次改变职业任务人口、任务创建和常规 unsafe outcome judge，而未识别新的执行/授权失效路径或评价混杂机制。三个 judge 的相同模型排序不认证标签可靠。安全主题本身不触发深入审阅；保留原证及特定理由，不把本项目不收录说成没有学术价值。
- **06328 ToolGym：贡献前关闭，不评分。** 完整题摘实际读。大工具池、合成任务、故障注入及 planner–actor 分工本身不构成新增长期机制；摘要的规划/执行不一致尚未指出超出既有职责区分的新适用条件，1170与119k样本量不是可比质量—预算边界。判断只限题摘，不声称审过正文或实验；无需为没有明确增量而默认展开全文。

本组仅补既有身份的判断，来源扫描与原日期不移动；尚未完成的本日工作继续由报告停点管理。

## Jan14 续核：必要原证、最小 owner 差额与实际写后（root，2026-10-08）

本组仅复查本日已有完整题摘的身份。以下“深入”限于拟采用命题及直接反侧，不表示全部附件、artifact 或实验复现。日期及当前官方撤回/纠错说明由本日身份记录与作者轻检承接；不移动原候选。

| 精确原源 | 证据与具体差额 | 独立处置 |
| --- | --- | --- |
| [06676 IDRBench v1](https://arxiv.org/html/2601.06676v1) | 实际§3.1/3.2/3.4、§4.1 Table1、§4.4及限制；详细query、reference-aware隐藏intent与交互披露须分开，报告质量、turns、question/response tokens也非同一成本。100任务但阶段消融仅30实例，Generation-only有负切片，simulator不代表真实用户。实际Ch66:938–995及自身末注，分账差额与成本/旧自主路径近文。 | 2+1+2=5；窄整合PRE及非writer实际POST通过，新960段。未授交互普遍有效、真实human burden或DAY。 |
| [07192 Relink v1](https://arxiv.org/html/2601.07192v1) | 实际Framework的Dynamic Instantiation/Generation、Setup及Tables1/2：显式KG与sentence-backed潜在pair共同rank/beam，仅选中pair按query实例化，不是全局fact commit。五组各500题、组件消融不证明entailment或全图正确。实际Ch76:1059–1090及自身末注，原traversal/citation继续独立，图池/训练/调用/更新费用和旧chunk/static路径保留。 | 2+1+2=5；窄整合PRE及非writer实际POST通过，新1073段。 |
| [07260 ActiShade v1](https://arxiv.org/html/2601.07260v1) | 实际Framework、Setup、Results Tables2–4：逐phrase embedding Gaussian扰动，时间池化输出概率，以最高cos即最小变化提出原query+phrase补检。仅是sensor，不是忽略的causal truth；FCL双contrastive也不保证三层排序，Table3有R@1反侧。实际Ch76:106–153及自身末注，费用、噪声/域漂移、原query/hybrid回退近文。 | 2+1+2=5；窄整合PRE及非writer实际POST通过，新126段。不采用完整训练recipe。 |
| [06389 FastLane v1](https://arxiv.org/html/2601.06389v1) | 实际§3.2、§4/4.1 Table1与§5限制；learned hard query-view路由把SumMaxSim改成近似ANN查询，不签目标等价。Table1 MRR .372低于SumMaxSim .384，T4延迟112.04/14.48不是30倍；STE文字前后矛盾不采用配方，§3.2/§5 document storage口径不授常数单doc向量。实际Ch76:258–281已有multivector权衡但未有这个query路由分支。 | 2+1+2=5；授Ch76窄PRE，待actual POST；保留近似质量损失、训练/索引费用及原多向量路径，不授生产SLO。 |
| [07183 RAIRS v1](https://arxiv.org/html/2601.07183v1) | 实际§4.2、§5必要方法、§6.1–6.4必要设置/表：双IVF逻辑membership下，32项共享PQ块物理保留一次、另一list引用，tail仍可能重复；visited规则不授所有顺序exact-once。PQ SIMD前逐ID去重有解包代价。Table4不含resident refine full vectors；更新12.2%/4.4%代价及小cell回退保留。实际Ch76:288–313数据面邻接，区别于授权/逻辑副本。 | 2+1+2=5；授Ch76窄PRE，待actual POST；不授总内存/所有负载普遍改善。 |
| [07055 DrZero v1](https://arxiv.org/html/2601.07055v1) | 实际§3.2–3.4 Eq2–5、§4设置及AppendixA/B Table8；HRPO更新proposer，按hop聚合不同生成question的solver-pass奖励，solver仍普通同prompt GRPO。hop不代表同难度、不签无偏/方差定理；合成答案非oracle。Table8多跳负切片，20→5是作者rollout代理而非端到端4倍。实际Ch33:34–88同prompt rationale仍成立。 | 2+1+2=5；授Ch33条件替代分支PRE，待actual POST；不重写普通solver组。 |
| [07048 Jasper v1](https://arxiv.org/html/2601.07048v1) | 实际§4、§5与§6.1/6.3–6.6必要方法/对照；压缩率不自动决定speed，PQ lookup/解包、block并发、维度与beam有条件。A100/CUDA12.9受限；低维/MIPS负切片，PQ/RaBitQ对比还改变backend。batch建图不证明并发mutation。已读Ch76数据面，局部kernel组合尚未改变独立长期合同；不借此强造Ch49 owner。 | 2+1+2=5；标准完成，仅报告，不因不写书改为贡献前排除；可选代码未核。 |
| [07711 Agentic RAG comparison v1](https://arxiv.org/html/2601.07711v1) | 实际§4、§5必要协议、§6 Tables3–5；FEVER prose差额28.8与表87.9−64.6=23.3冲突，不引用该数字。rewrite在FIQA/CQA有退步，ranker/population改变，judge65.4%及5%312pairs限制；token proxy非8A40/CPU整套成本。 | 1+1+2=4；具体关闭判断，仅报告，保留原证，不把组件实验提升一般Agent机制。 |
| [06944 SketchJudge v1](https://arxiv.org/html/2601.06944v1) | 实际§3、§4.1与§4.3.3 Table4；overall Acc与只在gold/pred incorrect上的ebF1人口不同，CoT三模型负侧不识别perception因果。实际Ch66:137、175–228已承载评价对象/条件分母与paired诊断。 | 2+1+2=5；标准完成，具体已有覆盖，不授新rubric可靠性。 |

本组三项实际POST已于本轮独立顺读，作者继续同步报告与末注。其余PRE只是必要源及owner裁决，实际写后仍需检查；不把此表当成整日或全量来源验收。

### 06860 / 07782 实际写后补核

四项必要原证的非作者PRE由 `increment-independent-review-delta4-20261008.md` 保存；root未将另一复核者的PRE冒充其写后。root本轮另实际顺读 Ch33:127–168与自身2525注、Ch78:592–647与自身779注：

- **06860 ET-Agent，POST通过。** 新142段将前验估计与已付K16后验人口选择衔接，未改GRPO advantage。工具std不是真gradient证书、allwrong格式正确仍零reward且可能留front、费用/随机coverage/旧uniform路径近文。2+1+2=5，窄整合，不授DAY。
- **07782 ToolQP，POST通过。** 新624段接在set-level discovery之后，只保留best-rank不加性累计的差额，明确仍有best-of-many机会偏差；工具/尝试/检索身份、全费用及独立schema/permission/dependency/执行检查与回退均保留。2+1+2=5，窄整合，不授普遍最佳或DAY。

06377 HiMem、06799 CIRAG具体已有覆盖保持上述独立PRE，不新增重复Books内容。作者继续同步本日正文处置，整日仍有普通可执行工作。

### 06389 / 07183 / 07055 实际写后补核

root非写入者实际顺读Ch76:219–249、265–292及自身末注1314/1316，Ch33:50–99及自身2527注。FastLane的query近似、质量损失、T4局部延迟及STE/存储口径隔离保留；RAIRS的共享PQ块不等full-vector压缩、tail/reference非所有顺序exact-once、精化与更新代价近文。DrZero的proposer跨问题hop人口与solver同prompt更新分开，合成答案非oracle及多跳负切片保留；模型身份已明确为Qwen2.5-3B/7B。三项窄整合实际POST通过，锁释放；不能据此授全日完成。

## 余32项完整题摘的独立贡献收束（root，2026-10-08）

实际完整读取本日五份`increment-abstracts-*-20261007.json`中的下列32份题摘；题摘准入不是证据完成，Submitted字段不代替公开日期。只决定本次是否值得继续核验，不添加新发现入口、不移动原候选。以下“继续”均须作者完成必要日期、当前官方说明、三维评分及相应证据/Books判断后才成为正式增量。

| ID（2601，v1） | 题摘实际增量与当前判断 |
| --- | --- |
| 07506 | reference与judge参数知识冲突下的paired swapped-reference失效，检验评分者是否遵循指定参考；继续，不能把错误reference服从率当事实正确率。 |
| 07208 | scalarization由terminal-state Conductor/contextual bandit动态选择、与policy共同更新；继续核两层信号，不由GRPO名称授正确meta-gradient或普遍Pareto优势。 |
| 07212 | hidden-transition MI用于连续block组合选择，DPI及global-optimal宣称涉及具体可行性边界；继续核假设，不由独立block重要性推出任意组合最优。 |
| 07200 | 对safe/harmful两个reference做pull/push的distribution-level样本权重；继续核几何代理与safety-utility，距离本身非安全证书。 |
| 07430 | 同一回答在有/无KG生成rationale条件下KL一致性蒸馏，不只另加知识QA数据；继续核target及known-but-incorrect定义。 |
| 07411 | 跨模块低秩参数干预而非离散module删除，目标区分任务与LM保持分责；继续核干预是否识别唯一能力，不能从loss约束签disentanglement。 |
| 07224 | gradient spatial concentration决定数据走SFT或RL，改变阶段数据分配；继续核proxy/对照，不签认知schema或通用省3.22倍。 |
| 07645 | layer-wise vision masking诊断后选择base-LM权重回注的plateau分支；继续核诊断与合并因果，attention变化非grounding真值。 |
| 07264 | evidence工具与verification工具的置信度校准反侧，以及accuracy/calibration双目标训练；继续核noise/工具类型混杂，不把工具反馈当通用oracle。 |
| 07351 | hard assignment改为可修订soft-token演进并配连续轨迹监督；继续，属于generation-state/训练采样一致性接口，而非只有新DLM分数。 |
| 07395 | 恶意工具未调用，注册metadata却诱导合法高权限工具执行；继续核具体失效路径与成功判据，MCP命名不自动授新权限威胁。 |
| 07320 | 低概率token边界后只在segment transition聚合优势，改变估计人口而非普通GAE改名；继续核bias/variance及近似ground-truth。 |
| 07226 | 无恶意context distractor下更多test-time compute可能反退，RARE改变过程信号；继续核预算与noise对照，不由attention图签唯一原因。 |
| 07041 | 跨语言冲突中资源丰度与语言亲缘的task-dependent相反条件；继续核matching，非新增翻译题量即贡献。 |
| 06748 | 测试期progress reward更新VLA同时保留训练prior，部署时策略可变而非只动作生成；继续核反馈/费用/物理安全，不授deployment-ready。 |
| 06521 | language-heavy成绩不能认证语言知识之外的视觉primitive，具体视觉盲区；继续核任务/人评构念，不用儿童年龄比较签因果。 |
| 07291 | image-conditioned prefix代理改变watermark分区/logit偏置的视觉质量取舍；继续核代理与检测，不把visual evidence weight当ground truth。 |
| 07331 | speech-centric降噪与LALM表示/任务鲁棒性可反向，activation subspace sensor是新测量对象；继续核负侧，相关0.98非因果。 |
| 06474 | sparse occupancy queries成为视觉—语言唯一桥，planning的anchor scoring/denoising分工；继续核信息/闭环边界，open-loop成绩非物理安全。 |
| 07507 | 必要v1 §3.1/3.2、§4/§5.1–5.3实际补读后，固定W的spectral partition加Hadamard低秩modulation是具体参数化分支，继续；Eq10/12的shape、block concat和rank上界解释未完全闭合，不授实际高rank或一般新增知识能力。 |
| 07309 | 必要v1 §3.1–3.3 Eq1–8/Alg1实际補读后，parser选tool/action/final spans的activation overlap选backbone、保护初始backbone其他角色salient neurons后transplant，是具体操作；继续，不把role写成conversation role或saliency等causal circuit。 |
| 07263 | 必要v1 §III/IV实际补读后，goal-alignment人口排除合法风险行为、capability失败与refusal分开，是具体安全评价增量；继续核窄结论。Success/(Success+Refusal)为条件分母非deployment风险，78.4−55为23.4百分点不照录23%单位；本轮未审完整SUPERVISOR防御recipe。 |
| 07449 | cached逐item LLM表示上做listwise residual，相对full-token listwise可能改变资源/质量边界；只补决定准入的表示、列表对照与预算口径，再决定，不因电商领域自动排除。 |
| 06943 | agentic相对workflow非恒优、初始video anchors丢失可能是评价边界；只补该反侧的matching/control，若仅列benchmark/task现象则前关闭，不默认全方法审阅。 |
| 07821 | IR human-intervention failures与world-model safety critic/recovery组合；只补是否新增failure定义/干预机制或可比边界，不因robotics或经典RL组合自动取舍。 |
| 06599 | 上下文使truth-vector方向/幅值变化；只补是否建立probe跨context传递失效或实际选择边界。几何描述本身不等truth oracle或新部署保证。 |
| 07060 | 四affordance teacher与连续subtask progress；只补progress如何改变切换控制及其可比反侧。成熟辅助蒸馏组合的任务涨分不足以继续。 |
| 07219 | scene-graph、split prompt及inversion组合；只补有无超成熟组合的可比质量/预算条件，不从20–30秒对6–10分钟签等配置优势。 |
| 07366 | ASR引导scene/event token compression；只补跨模态选择/压缩的具体变化或代价边界，新增电商叙事dataset本身不足。 |
| 06972 | 24encoder的architecture fingerprint可能修正处理层次；只补architecture与pretraining/人口是否可分，depth百分比不证明streaming latency。 |
| 07290 | 贡献前关闭：完整摘要为新localized数据、组合benchmark及既有video理解指标，未指出新的学习/执行机制、原设计失效条件或可比资源边界。不评分，不称正文/实验已审。 |
| 07298 | 贡献前关闭：五种具名视觉reasoning动作、tree冷启动及diversity→DAPO成熟组合和任务分数，没有超组合的新机制或成立条件；不以“human cognition”及超过某模型作长期贡献。不评分，不称正文/实验已审。 |

本表22项有明确待核验增量、8项只需决定性定点、2项贡献前关闭；不是22项已证实贡献或全部全文队列。07507/07309/07263的已读必要核心必须复用，除拟采用命题所需的未读反侧外不重复展开。root实际读Ch66:2070–2135，已有条件分母、proposal/effect/final-output、runtime/refusal/cost operating curve；07263拟窄已有覆盖仍须精确对应全部采用命题，不能用主题相似代验收。

## 2026-10-08：两项标准审阅独核（root）

07506 实际完整读取 `increment-necessary-core-2601.07506v1-20261008.json` §2–6/Limitations。四种reference/candidate配对的正确性定义是reference compliance，不是事实truth；TC语义类型混杂和Evaluator-Knowledge仅取judge原答错且人口随judge变化，不支持参数知识唯一因果。CoT的RPAG有改善也有恶化，Direct仅缓和，无通用修复。2+1+2=5标准Only通过，保留局部diagnostic和未证明内容，不冒称Books已完整实现本协议；不新增书段/POST。

07264 实际读取 `increment-necessary-core-2601.07264v1-20261008.json` §3–6/Limitations，未遍历附件。题集、工具与训练协议共同变化，MCIP共同错误交集与印刷单设置集合定义不闭合；λ=1低ECE伴准确率退，MSCR部分准确率及Serper AUROC反侧必须保留。严格原始reward margin不证明校准：β不等时期望reward最优q的偏移是依据原公式的代数推导，不能称作者已证明proper calibration。2+1+2=5标准Only通过，不采未给全fallback的recipe，不授长报告/自治规划或所有规模工具的可靠性。当前Ch66:1036–1061已实际读各用途/不同题集分责，但不将通则冒作本文全部实现；无新增Books写入。

两项采用身份/精确版本/命题未变，已核本日公开日期与current说明按原包复用；只授具体标准结果，不授来源全覆盖或日级Gate。日期、评分、§4和处置由报告作者同步。

## 2026-10-08：三项必要证据与 owner 终判（root）

精确版本均v1；当前官方页的轻量说明与公开日期依据复用 `increment-current-identity-root3-20261008.json` 及 `increment-date-bounds-rest-20261007.json` 的具名记录。正常公告日界与正式注册上界共同支持Jan13自然日，不把注册或提交时刻单独当首次公开。以下三项均2+1+2=5，不授日级验收。

- **07309 ARM：窄整合PRE通过，actual POST仍待。** 实际§3.1–3.3 Eq1–8/Alg1、§4.1–4.3及Table1/2。共享架构/tokenizer的pool中，按选定action/tool/final spans求逐层MLP平均绝对activation及TopK，用AOS选backbone、held-out弱bench选donor；固定初始backbone在其他bench的salient union，移植donor TopK减保护集对应输入row/bias/输出column，gated模块需对应。角色是解析的操作跨度，不是conversation role；saliency与重叠不是能力因果独占，保护集不随中间移植刷新。699任务/1240校准轨迹与测试分开；Qwen3平均44.6高于oracle44.2却有Web/τ/Office退步，Qwen2.5也有OS反侧，不授逐任务保证。多模型capture、dev搜索、校准/移植及回归有成本，完整端到端预算未披露。实际Ch30:610–628有答案token差分mask与可选SFT，但未承载固定其他任务保护集合与role-span分工；授权只在该邻接增加最小机制段及自身末注，保独立adapter/已核静态merge回退，不宣称训练复现。
- **07507 SMoA：中心Disputed终态，通过隔离而非采用。** 实际§3 Eq9–16及相关已读评价。Eq10全尺寸SVD重构mask作Hadamard、Eq11拼接、Eq12两因子同时写r/K×d/K与Eq16 block-rank主张不能共同重构出一致形状；后续因子另一形状没有说明如何闭合前述全尺寸调制。Hadamard秩上界也不证明实际达到该秩，更不证明超过矩阵维度。不得用这些式子解释可执行增秩机制或把线性working model当所有PEFT知识边界。必要重开材料是该精确版本的修正维度/块布局与可核实现或勘误；来源可读不是访问受阻，不因争议改成贡献前关闭。当前不入Books、不支持正面机制/性能断言。
- **07263 AgentBait：标准具体Existing通过。** 实际§III-A/B与§IV-A–D，采用范围只含goal-aligned injection与评价人口边界，不采用未审SUPERVISOR防线。20向量×5patterns×5scenarios的500模板页面、同GPT4o×5框架结果以action-log匹配判成功，不是真实金融effect；aligned78.4与55差23.4个百分点，不能照录为相对提升23%。26克隆真实页×4selected高ASR vectors为104条件样本，Success/(Success+Refusal)排除capability failure，不能冒作部署风险；authority pretraining解释也未被因果识别。实际Ch66:2065–2138的attempt/conditional人口、proposal/effect及refusal分责，Ch72:700–719的goal alignment不授来源authority/组合权限，具体承载窄采用命题。无新增Books或POST；不把已有覆盖冒作整篇攻击taxonomy与全部防线实现。

07309后续已实际写入；root非写入者顺读Ch30:608–634完整09398→role-span→ACT-Mat邻接及自身末注933，actual POST通过。新段同坐标/gated索引、固定初始保护union、相关性非因果、任务反退/费用/回退与必要源一致，未扩成通用能力保持或性能保证；作者同步正式结果，Ch30窄锁释放。Table3/AppC是作者额外实际读取范围，不冒称root重复全部附件。

## 2026-10-08：07351与07320必要独判（root）

换为独立Jan14上下文，重读当前AGENTS及适用合同/Prompt/每日源和本日停点。原17不搬日期、不重评分；已通过的题摘准入与当前身份说明复用，实际读取两ID的date-bounds/current字段，正常公告规则与ID上界支持Jan13，不将登记独立当公开证据。

- **07351 EvoToken：5分标准Only通过。** 实际v1§3/4、Table1、C2/3与Limitations，实际Ch24软状态/训练/commit邻接。TopK均值、四状态、块内历史最大confidence提交与轨迹监督是局部替代；四步训练和逐配置择优搜索不证明等预算，局部退步、AR初始化困难及缓存适用范围保留。现文已解释可修订软输入、训练兼容和提交退路，但不冒称完整配方Existing；不追加重复Books。
- **07320 SAE：5分差额深入、Ch32窄PRE通过。** 实际v1§3、§4 Eq5–10/固定分段定理假设、Table1与§5.3.2/3，实际Ch32 GAE邻接及相关Ch31/33交接。采用已采token低概率的二值trace gate、仍逐token递推，不等语义/因果分段。限定原γ=1/terminal reward；固定分段界非动态保证，端点Monte Carlo参考非真实token credit，AMC反侧及不同训练步数保留。仅授GAE后最小分支与自身末注，保critic/阈值身份、费用与普通GAE回退；写后peer实际POST，不授DAY。

## 2026-10-08：剩余具名必要终判（root，非作者）

复用本日有效题摘校准；actual necessary evidence、current identity及公开日期依据来自本目录具名 `increment-deciding8-core1/core2/asr`、`increment-necessary-core-*`、`increment-current-identity-deciding7/last4`、`increment-date-bounds-rest`。只采用v1和拟支持命题，不追全版本史、未复现或核全artifact。正常公告日界结合必要ID上界支持Jan13；注册不独立证明公开。以下均2+1+2=5，只有具体知识差额升级为必要深入，不为处置倒改分。

- **07449 RLPO：标准仅报告。** 实际§4.1/5.1–5.2/AppD和Ch76 reranking邻接。独立item表示上的listwise残差、可学初值0的alpha是局部结构；freeze与full-parameter叙述冲突，per-review与per-list成本不能拼。K50边界及非总匹配训练预算保留。现文已有表示域list交互和独立读取成本，不为新配方重复写书，也不称完整RLPO已有覆盖。
- **06943 VideoDR：标准仅报告。** 实际方法与同100题、各模型表，Ch77 compact anchor/历史保留邻接。workflow和single agent均不能研究期重看，调用预算并未配平；部分模型相同或反退，不能因果推出external memory总更好。有限评价人口/anchor组织观察留报告，不把主观轨迹与模型差异变新永久机制。
- **06972 ASR层次诊断：标准仅报告。** 实际v1 PDF必要p2–8/p14及Ch23探针可读/使用/因果邻接。24encoder、架构控制回归不能控制全部训练目标/数据差异，depth0还在卷积frontend之后。29%层数的低延迟/early-exit属于待验预测，不是测得服务加速；保有限相关诊断，不冒称具体实验已有覆盖。
- **07821 FARL：Ch26窄整合PRE。** 实际§III/IV-A/B Eq1–12及VI-A/B1/B3，Safety邻接缺少冻结world model/recovery与可更新task policy的消费者分责。只采用task动作短预测过滤、必要时由recovery替换真实执行动作、实际反馈供后续更新；不采未读proof/实机headline，不授off-policy无偏或模型阈值为安全概率。训练失败数据、额外forward、校准与恢复费用保留，仿真碰撞代理非损伤证明，真实世界不能rollback。
- **07060 PALM：Ch26窄整合PRE。** 实际§3.4 Eq8–10/Table1/AppA.1–A.3/C.1与subgoal stack邻接。动作与progress联合输出可提议终止/换阶段，区别progress只触发fresh检查的分支。EPIC/RoboCerebra分步标注及942轨迹半自动continuous labels仅证明监督来源，未披露完整插值/归一协议；不把90%读数当物理完成或通用阈值。局部no-progress/阈值反侧、teacher/训练/DiT费用及旧检查路径共存近文。
- **06748 TT-VLA：Ch26窄整合PRE。** actual§3.2–3.3/4设置与反侧/Limitations及OnlineRL和test-time更新邻接。progress delta直接成为episode内LoRA更新的即时reward，去critic、gamma/lambda=0下A=r，不是长程价值无偏。clipping不保证SFT prior/安全；原代数只在指定remaining-progress V成立，p=1不支持严格负号普遍说法。progress误差、非单调任务、弱base及费用/deadline与冻结policy回退近文，不重写通用PPO。
- **07219 VENUS：Ch24窄整合PRE。** 实际§4.2–4.3 Eq4–7/5.2/5.4与reference冲突邻接。原/编辑scene graph交集作保留source，新关系加交集作target；语义条件的保留边界不等pixel mask、几何不变或背景保真。source ablation主要支持局部保真代理，EditVal accuracy低于SGEdit、不同backbone反退保留，GTTP模式不混成同一graph-diff实验。解析、inversion、prompt上限和质量回归成本近文，不授普遍速度。
- **06474 SparseOccVLA：标准仅报告。** 实际§3.3/4表及Ch26 proposal/trajectory邻接。LLM给18anchor评分、diffusion回归并选对应轨迹是具体局部接口，但有限open-loop验证未新增实际commit/闭环验收合同；不将稀疏表示/三个任务指标拼成安全或因果证明。不冒称完整配方已有，不为主题owner创造diff。
- **07291 VISA：标准仅报告，null保证隔离。** actual§3/4+A/C和Ch72 provenance邻接。视觉权重/entropy偏置有限质量—检测取舍可留；固定green cardinality不能保证null条件质量为1/2（两词P(a)=.9反例），未给完整detector重建/校准。局部AUC、clean退步及固定256token费用不是普遍统计认证；重开需对应null校准与检测定义，不把Only作为消掉争议的标签。
- **07331 SEE：中心争议终态，Books暂缓。** actual§3 Eq6–12/§4/Limitations；最大absolute的文字与signed max式不一致，SVD等价符号翻转可改变选择；Eq7输出形状未说明丢零列操作。不能自补abs/shape并采noise-only或semantic-preserving机制；GSR只对clean输出一致，非truth。重开需exact-version修正selector/shape与可核artifact或matched语义保持证据，不因可读即采纳。
- **07366 HiVid：中心争议终态，Books暂缓。** actual存储§3.4/4.3/App8，另定点打开官方v1§3.3：输入确有时间标记，但replicated event query/shared context的公式未说明frame-specific注入，之后拼timestamp不证明对应帧细节已经可区分。不能宣称代码必错，也不能暗补实现。segment分母384称dimensionality与主文全序列S+N(1+E)口径未闭合；82.59%不支持总资源收益。重开需该版本frame绑定、实际视觉token计数或可核实现；有限layout/表留报告，不正面采用中心保真/压缩保证。

四项整合仅授对应Ch26/Ch24窄写锁与PRE，实际写后由非作者检查邻接/证据，未授POST、全日完成或279份无遗漏。

### 四处实际写后复核

root（非写入者）已实际顺读 Ch26 的 Online RL 完整邻接286–302、Subgoal Stack邻接541–556、Safety/Dreaming邻接903–925，以及三项自身末注；Ch24 reference条件完整邻接175–195及VENUS自身末注。TT-VLA的progress差奖励消费者、PALM的joint progress阶段提议、FARL的冻结恢复器/实际执行动作反馈、VENUS的source交集/target关系分别落入现有机制，未把代理读数当完成、安全或像素保真。费用、反侧和旧方案回退均在对应正文附近，未删去原有有效内容，四处actual POST通过，窄锁释放。源审阅继续复用上面的具名必要原件，不声称artifact已核或实验已复现。FARL评分文字待作者与正式记录统一；全日报六部分验收仍是下一步，四处POST不替代DAY。

FARL评分核对：首次具名裁决为2+2+2=6，预测风险/执行动作替换/真实transition训练跨越系统边界，保留该评分。上段“以下均5”是后续汇总概写错误；只更正汇总，不改变原评分或因整合提高分数。其余此批十项仍按5分及必要差额审阅，formal Report、源笔记和Books末注由作者统一。
