# Jun03 增量补查 — Agent / 多模态

## 2026-10-25 当前接续

原Agent/Multi具名必要余0，02436 R169/R170实际Ch25已成；有限发现收束仍普通，不预DAY；02449 R168正式5分/actualCh66具体NC已成；02494 R160仅first-public资格缺口隔离、不评分/Methods，02459 R163/R166实际Ch23已成；02553 R157/158实际Ch25、01166 R153/154实际Ch72、02060 R151具体NC及01212 R146/147实际Ch76已成。下方2026-10-24的38项是当时范围，不复活已完成/明确排除材料。真实有效层及有限发现/date边界见本日Report§4–5/最新独核。


## 2026-10-24 当时恢复停点（历史范围）

首4及01139/02320有效Source/Books/POST不重做。本轮Agent batch2 13项全部经过独立准入、必要Source、实际owner与Books判断：12真实整合并通过非writer真实完整POST，00756为Ch77具体已有覆盖；采用以[本批必要原件/提案](./SUP_AGENT_B2_RESUME_20261024.md)和[独核R3–16](./SUP_RESUME_REVIEW_20261024.md)为准。首4/01139/02320原采用分别见既有独核，不继承旧临时owner。本切片未授完整Coverage/DAY，没有已授待写或待POST窄位。保护并发和index，不stage/commit/push。

已存64项官方exact-v1完整题摘/history＝首4＋Agent batch2/3/4各15＋Multi batch1 15；01581/02507两个代表排除使用current DataCite完整AB，不冒v1。原题摘/提案及历史初分继续保留，下方旧表不替代当前层次或最终分母。

当前38具名普通恢复项（不是候选分母或全来源池）：
1. 后34原拟准入仍待独立贡献校准及必要Source/actualowner/Books：
   - Agent batch3 11：01287、01317、00566、00376、02240、02380、01365、01326、01619、01304、02132。
   - Multi batch1 13：00299、00267、02486、00773、00435、01380、01285、00515、01914、01600、00232、01027、00959。
   - Agent batch4 10：00804、01770、01212、02060、01166、02553、02494、02459、02449、02436。
2. 四决定性最小补读：01138 AMP是否有具体operation/governance增量；00476 v1短AB的reasoning/conclusion/action测量；02031 OpenWebRL核心设计消融；02536 skilldiff标签是否有真实behavior验证。未决定准入，不预评分。
3. 01139/02320已完成不在队列；02470维持贡献前排除。batch2这13项不重做；任何后续新反例只恢复受影响层。

五日期资格另列：00189、00135、00152、00094、00096，尚需有限公告/作者原文恢复；完整可能区间仍跨BJT，不靠ID或提交补公开，不提前当终态外部项。02502 CRAM/02576 ProtoAda归MODEL唯一接手，不跨切片重复收录。

来源发现仍普通未完：[Agent248导航](./SUP_AGENT_NAV_20261023.json)/[Multi214导航](./SUP_MULTI_NAV_20261023.json)均page1/size1000到尾，只有标题线索，不是462强制逐项关闭队列。继续收窄与ROADMAP机制相关的未读题意及官方目标日有界标题补检，保实际停止依据；不重读已有效AB或全部窗外正文。

## 首4逐字PRE草案（仅准备，不是已写正文）

供root/reader一次性审阅，writer按actual owner/邻接再确定；未获写权不自行落Books。02357的NC以552–556实际正文为据，无造diff要求。

### 02483 / Ch78 SIA投机段后

投机的撤销还应区分任务状态与观察者状态：一个尚未选中的只读检索即使最终被弃用，服务商也可能已经保存查询意图，删除本地结果无法撤回它。一个[受限运行时分支](https://arxiv.org/html/2606.02483v1#S4)在调用出界前为参数、目的地和观察者绑定合同，选择改写投影、可信本地替身、延后至分支晋升或拒绝；日志、cache、重试队列与审计sink也必须在这个边界之后。它新增的是issue-time的观察责任，而非让read-only或allow-list认证隐私；原型依赖完整中介、正确标签与动作保限制，敏感参数labeler仍很弱，远端planner provider又被信任，不能据局部排序保证绝不泄漏。错误标签、替身质量、额外调用和误延后均有代价；无法约束出界通道时，保留不投机的已确认调用路径，而不靠commit后scrub补发隐私保证。

### 02479 / Ch25 MemCam分支后

逐目标视野重叠仍可能反复取回同一片区域；固定reference预算下，另一分支先用深度与pose把历史像素投到目标视图，再贪心选择尚未被当前context和已选reference支持的残余区域。局部深度估计与滑窗缓存提供比整view评分更细的选择依据，却不是长期全局3D地图或真实可见性证明。[受限对照](https://arxiv.org/html/2606.02479v1#S5)中，细覆盖配独立top-n反而退步，必须与残余互补选择联合；强图像退化也可输给原FoV检索。深度模型、投影、扫描候选和cache都计费，检索慢于FoV而非免费替代；生成漂移、几何不准或预算不合适时，保留原pose/view bank、短可信context与新观测校正，不由重访一致性签发真实动态或物理行动安全。

### 01435 / Ch77结构字段匹配段后

候选已经取回，仍要区分“哪些记录语义匹配”与“当前问题要求哪种决议”。当原源明确给出版本总序、问题确实询问当前值时，可以让LLM抽取全部匹配记录及其版本，再由确定性代码按声明策略聚合，而不是把过滤、先验抑制、版本比较和回答生成挤进一次prompt。[有限FactConsolidation证据](https://arxiv.org/html/2606.01435v1#S5)支持这个后检索组装分工，但whole-pipeline对照也同时改变prompt、格式和temperature，不能归因max算子；LongMemEval小样本总体并未更优，历史、计数、Yes/No和部分序更新也不应强用latest。严格抽取会过拒，多跳早期错误会传播；索引版本字段、抽取、逐hop调用和独立验收均计费。字段缺失、策略不明或原源冲突时，应保留候选集合、回读或澄清，不把较大序号升格为事实真值，也不据一个task认定复杂存储普遍无用。


## 第四批精确v1准入校准准备

[15项官方精确v1完整AB/history](./SUP_AGENT_EXACT_BATCH4_20261023.json)已读；00096跨日资格保留，其他正常最早Jun02 00Z到导航同日registered。02031/02536为普通可执行最小补读，不冒外部缺口。

|ID|初步处置|唯一owner|具体贡献或排除理由|
|---|---|---|---|
|2606.02320|本轮必要Source/唯一owner/实际整合与POST通过；2+2+2=6|PLATFORM-EVALUATION-SYSTEM|figure/caption/上下文与source分开审计，检索预算可能挤占chart fulfillment，暴露纯文字评价盲区；非仅100任务/9系统榜。准入不等judge/因果成立，原拟排理由已由R13纠正。 当前最终证据/限定采用见[SUP_TVIR_20261024.md](./SUP_TVIR_20261024.md)与SUP_CHECKPOINT_REVIEW_20261024 R2–4；原初筛未审状态仅历史。|
|2606.02031|普通最小补读待判；不预评分|AGENT-WORKFLOW|online livewebsite RL明确工程路径，但v1AB仅列pipeline组件/小初始化与SOTA，没有给决定性新增设计选择与成立边界；定点读核心ablation后判断，不以开源/SOTA准入。|
|2606.00804|拟准入6=3+1+2|AGENT-MULTI-AGENT|冻结1440矩阵拒绝原预注册exactwinner/CI与语言一致性假设，compliance单agent更好；nearbest不是必胜routinglaw，局部负结果改变固定拓扑选择。|
|2606.01770|拟准入6=2+2+2|AGENT-MEMORY|持续单harness更新早峰后衰退→evolution/adaptation分loss+tree路由/人工信号→固定offline优化与开放stream生命周期分责。|
|2606.01212|拟准入6=2+2+2|AGENT-RAG|单query局部投毒不覆盖跨主题影响→semanticquerynetwork预算调配→检验discourse级corpus影响，作者mitigation无效须收窄条件。|
|2606.02060|拟准入6=2+2+2|AGENT-REFLECTION|末答不能定位有害推理span→claim证据状态跟踪/firsterrors与normal exploration分离→span级auditor不同于每failedsearch判错。|
|2606.01166|拟准入6=2+2+2|AGENT-WORKFLOW|静态promptguard失配多步execution威胁→公开新威胁转可执行任务与trajectory监督再训练guard→更新循环具体替代分支，待去重/holdout。|
|2606.00096|日期资格保留；不预评分|AGENT-TOOL-CALLING|toolcollapse/entropydiversity有潜力，但v1May25 13:06Z正常最早May26至Jun2reg跨日。v2Jun2提交非已公开事件。|
|2606.02553|拟准入6=2+2+2|MULTIMODAL-WORLD-MODELS|recentwindow自我漂移不可回顾→selflatent可检索history+WindowTemporalDelta loss抑制局部冗余→另一content-addressed memory分支。|
|2606.02536|普通最小补读待判；不预评分|AGENT-MEMORY|68个skilldiff标签的embeddingtrait预测可能仅重述文本标注非真实agent行为；需看labels/behavior验证才决定具体新增，不以91.2%自签safeupdate。|
|2606.02494|拟准入6=2+2+2|AGENT-WORKFLOW|220合成run注入taskerror被structuraldefect掩蔽→区分within/cross/structural监测与成熟阶段→不能把taskmonitor无异常当integration可靠。|
|2606.02470|独立校准R13维持贡献排除；不评分|AGENT-MCP|完整精确v1题摘只扩展个人应用/账号/MCP目录并笼统称struggle，未给具体新机制、混杂或失效边界；不自行将个性化外推成权限/状态一致性证据，具名新证据到达才定点重开。|
|2606.02459|拟准入6=2+2+2|MULTIMODAL-REPRESENTATION|passive/spatial稀疏reward→objectposition/orientation map+Python SAC逐步验证dense反馈→可执行spatial状态与language推理分工。|
|2606.02449|拟准入5=2+1+2|AGENT-TOOL-CALLING|CAPTCHA答案recognition不等界面动作合法trace→受控GUI/现实干扰/tracecondition score反例→识别与grounded process分验；仅封闭bench不执行真实CAPTCHA。|
|2606.02436|拟准入6=2+2+2|MULTIMODAL-WORLD-MODELS|implicit压缩无geometry约束→cameraqueryable head由frozen3D teacher蒸馏固定memorytoken、prune+推理丢teacher→geometry约束训练/消费边界。|


## 多模态第一批精确v1准入校准准备

[15项官方精确v1完整AB/history](./SUP_MULTI_EXACT_BATCH1_20261023.json)已读。00094为跨日日期资格保留；02502已协调转model；其他13的v1均Fri18Z后/周末/Mon18Z前，最早Jun02 00Z至同日registered落Jun02 BJT。所有页有限信号未见withdrawn/erratum。准入/Source仍待非writer，不因映射owner自动算入。

|ID|初步处置|唯一owner|具体机制/边界|
|---|---|---|---|
|2606.00299|拟准入6=2+2+2|MULTIMODAL-WORLD-MODELS|全3D cache而非visible-shell支持camera/entity分控，soft spatial aligned injection+normal-map桥接；不得采eradicating ambiguity绝对宣传。|
|2606.00267|拟准入6=2+2+2|MULTIMODAL-WORLD-MODELS|nominal imagination漏highimpact尾部→初noise语义gradient+OOD plausibility双目标→受限stress-test非真实风险概率。|
|2606.02486|拟准入6=2+2+2|MULTIMODAL-EMBODIED-VLA|观测到动作延迟遇移动物体→frozen VLA feature未来patch/velocityaccel+uncertainty horizon→预测式补时接口，待检查实时/不确定门真义。|
|2606.00773|拟准入7=3+2+2|MULTIMODAL-EMBODIED-VLA|binarysuccess漏unsafe-success→task-aware STL/unsafe-success与worstdepth拆分→改变只用成功率验收；仅模拟后验而非shield。|
|2606.00435|拟准入5=2+1+2|MULTIMODAL-REPRESENTATION|缺视觉证据却自信作答→CLIP中间patch-question trajectory+blank/route/selfassessment ensemble提出answer/abstain；待拆主要归因/任务泄漏。|
|2606.01380|拟准入5=2+1+2|MULTIMODAL-GENERATIVE-PARADIGMS|one-step inversion初latent分布与caption-gap→iterative noisealignment/learned suffix双变量→模型免训练不等perinstance免优化，待对照。|
|2606.01285|拟准入5=2+1+2|MULTIMODAL-GENERATIVE-PARADIGMS|画质不测试事实/操作步骤→information-seeking video prompts与human-aligned事实/helpfulness指标→改变仅fidelity的生成评价。|
|2606.00515|拟准入8=3+2+3|MULTIMODAL-EMBODIED-VLA|low-rate VLA不能directplant→compliance proposal与高频独立energytank/passivity gate分责→可验证port contract，需严核sampledpassive假设不当完整物理安全。|
|2606.01914|拟准入7=3+2+2|MULTIMODAL-REPRESENTATION|二元正确加无关第三空间词却错→vision证据仍内部可读，语言侧channel/activationpatch与LLMonly DPO→不能自动归visualattention不足。|
|2606.01600|拟准入5=2+1+2|MULTIMODAL-WORLD-MODELS|valid/safe指令评价漏constraint/counterfactual/adversarial→真实DROID起态分层六维13准则→图像连贯不证明任务constraint/physics。|
|2606.00232|拟准入6=2+2+2|MULTIMODAL-REPRESENTATION|feedback共同看当前输出可被幻觉污染→独立observationgraph/claimgraph+claimrisk局部修补→区分证据抽取和修补选择；收敛须核假设。|
|2606.02502|转交model唯一owner|TRAIN-LORA|CRAM增量expert/adaptiverank/centroidrouting更靠训练参数持续适配；已发peer，本文不重复审。|
|2606.01027|拟准入7=2+3+2|MULTIMODAL-WORLD-MODELS|sharedvideo骨干分jointactionfuture与candidate动作condition simulator/progress消费者，modalitymask和lowqualityrectify→区分可生成action与可评价后果。|
|2606.00959|拟准入6=2+2+2|MULTIMODAL-REPRESENTATION|alignment/accuracy混淆modality贡献→decision PID unique/redundant/synergy与intervention预测、languagecontrolled sensoryPID→改变融合依赖评价。|
|2606.00094|日期资格保留；不预评分|MULTIMODAL-GENERATIVE-PARADIGMS|discrete patch score+softtopk/sampler有潜力，但v1May25 08:43Z最早May26至Jun2reg跨度，不能确认补窗。|


## 第三批精确v1准入校准准备

[15项精确v1完整题摘/history](./SUP_AGENT_EXACT_BATCH3_20261023.json)已实际读。00135/00152跨日联合界仍为日期资格保留，不预评分、不列确定候选。其余v1在Fri18Z之后/周末/Mon18Z前，Jun02 00Z→各自导航registered同Jun02 BJT。所有页未命中撤回/erratum，只作有限当前页信号。01138/00476准入仍需决定性最小补读，不属于外部阻塞。

|ID|初步处置|唯一owner|具体贡献或问题|
|---|---|---|---|
|2606.01287|拟准入7=3+2+2|MULTIMODAL-REPRESENTATION|latent slot/marker/format拆分反证视觉证据memory解释，marker保留78–100%gain；直接改变latent token机制归因，待消融条件。|
|2606.01317|拟准入6=2+2+2|AGENT-WORKFLOW|拒答/局部动作不覆盖持久workspace→按最终环境状态与原因分类验收，重新审视多步操作安全。|
|2606.00566|拟准入7=3+2+2|AGENT-TOOL-CALLING|matched same payload仅换user/metadata/output渠道→agentnative与general相反信任偏置；v1仅6模型，当前10模型affordance匹配不能回填。|
|2606.01138|决定性接口补读后再判；不预评分|AGENT-MEMORY|v1题名AMP而当前memorywire；作者承认既有RRF/FSM/diffapprove的协议包装。需看5操作/治理是否提供具体新兼容/commit约束，不能凭跨adapter/微基准准入。|
|2606.00135|日期资格保留；不预评分|AGENT-TOOL-CALLING|seed/prompt/history carry评价混杂有贡献潜力，但v1ThuMay28 22:21:47Z正常最早Jun1 00Z至regJun2跨BJT；不能按ID归日。|
|2606.00376|拟准入7=3+2+2（中心理论待严核）|AGENT-PLANNING|宣称decoder capacity界/Deterministic Horizon与工具必要性，直接改变延长CoT选择；v1强theorem/architectural ceiling不得用v2温和结论代核，须检查假设/证明与干预。|
|2606.00152|日期资格保留；不预评分|AGENT-TOOL-CALLING|acquisition而非outgoing audit有价值，但FriMay29 04:55:12Z正常最早Jun1 00Z至regJun2跨日，需精确公开证。|
|2606.02240|拟准入6=2+2+2|AGENT-TOOL-CALLING|toolresponse integration分布与chatguard训练错配、maintainer-mediated immutable评测版本隔离→明确新guard训练/评价边界；v1 ASR69.9→2.4/FPR.37%，不混当前75–77pp holdout。|
|2606.00476|决定性补读再判；不预评分|AGENT-REFLECTION|v1完整AB实际只有3句，提reasoning-conclusion/conclusion-action相反但未给判定机制；当前v2显式tag/22–26%抽取伪差不能回投，需v1必要正文定点。|
|2606.02380|拟准入6=2+2+2|AGENT-WORKFLOW|reported plan与真实工具action压力配对→拆自报一致与执行结果，不先接受strategic deception标签/内在意图外推。|
|2606.01365|拟准入5=2+1+2|AGENT-MULTI-AGENT|165同caps轨迹中execution成功无useful output/evidence availability与sentencegrounding分裂→cheap online与semantic audit互补；v1无后版58.1%postwarning/pilot改善不能回填。|
|2606.01326|拟准入6=2+2+2|AGENT-CONTEXT|保程序语义minification仍42%token减/12ppresolution损→不能把程序语义不变等同模型读入/repair行为不变；局部负结果直接改变压缩选择。|
|2606.01619|拟准入6=2+2+2|AGENT-MEMORY|skill版本与演进policy冲突→GRPO组内控制版本对照+discounted Thompson选择→联合skillpolicy演进而非静态库。|
|2606.01304|拟准入6=2+2+2|AGENT-RAG|生成流畅负例可按source捷径损害retriever→信息需求反事实扰动+source互信息抑制→改变直接加入LLM hardnegative训练。|
|2606.02132|拟准入6=2+2+2|AGENT-TOOL-CALLING|uniform penalty压掉有益探索→group引入toolfree并difficulty shaping/confidenceweight→区分是否必要而非仅降call数。|


## 第二批精确v1准入校准准备

[15项精确v1完整题摘/history](./SUP_AGENT_EXACT_BATCH2_20261023.json)已实际读。除下述00189，其余v1在FriMay29 18Z之后/周末/MonJun01 18Z前，最早Jun02 00Z；导航原件均exact DOI/arxiv.content/findable/Jun02 03–05Z registered，联合区间落Jun02 BJT。无撤回/勘误命中，只作当前页有限信号核查。02461v2Jun02 03:07:54Z、01139v2Jun02 08:41:20Z提交不等已公开重要修订；未据版本号新增事件，若实际贡献变化需原事件证。

|ID|初步处置|唯一owner|具体准入/排除理由|
|---|---|---|---|
|2606.00820|拟准入7=3+2+2|AGENT-MULTI-AGENT|answer flip混淆自反思、stance conformity与reasoning persuasion；v1对照与无标签干预不改善准确率，改变以共识当收益的评价。|
|2606.00756|拟准入6=2+2+2|AGENT-MEMORY|轻edge本地isolated经验/长上下文约束→语义subgoal索引的异步cloud critic/跨agent guidance→改变本地记忆与在线参数更新二选一；不预认任务普胜。|
|2606.00547|拟准入5=2+1+2|AGENT-MEMORY|单horizon retrieval无法服务initial planning和local action→episode/turn双层learned retrieval+PRM局部proxy→重新考虑固定相似度/terminal-only credit。只限交互SQL范围。|
|2606.00914|拟准入7=3+2+2|AGENT-CONTEXT|固定model/persona/finalprompt仅变前10轮feed构成/顺序→default-bound三个响应区/剂量与generator-swap→检验上游ranker不能只测终端prompt。仅v1原2,785rollout。|
|2606.00341|拟准入7=3+2+2|AGENT-WORKFLOW|benign任务中纠正/中断/shutdown仍被绕过，且父corrigible不推出subagent→必须区分任务完成与可纠正控制、委派约束传播。v1缺后版text-only新对照不补。|
|2606.02461|拟准入6=2+2+2|AGENT-MEMORY|naive流不知道复用关系→controlled compositional/reusable vsnaive/heldout流→区分塑性收益与记忆诱导退化，不以长期任务顺序本身证明continual learning。|
|2606.01314|拟准入6=2+2+2|AGENT-MEMORY|固定tool与独立skill效用忽略相互作用→skill/tool原子bundle+pairwise interaction pressure+anti-pattern veto→上下文库可联合改工具且需保协同/冲突。版本当前DataCite与v1贡献有漂移，采用v1。|
|2606.00644|拟准入6=2+2+2|AGENT-RAG|普通research答案引用可trace却判断对象错→cutoff-aligned evidence/生成模型precede cutoff与隐藏未来验证→区分evidence支持和前瞻decision alignment。AI研究判断非暂缓Science应用。|
|2606.02388|拟准入6=2+2+2|MULTIMODAL-WORLD-MODELS|只有reward的agentRL缺action后果监督→同policy的onpolicy transition辅助WM，entropy选择/耐噪loss/reward配比→无额外推理环的训练替代分支。|
|2606.02314|拟准入5=2+2+1|AGENT-MCP|跨组织discover元数据查询约束→把discovery语义与metadata尺寸实证映到DNS单UDP预算→重新考虑discover链，不证明安全或实际毫秒SLO。|
|2606.00189|日期资格保留；不预评分|AGENT-WORKFLOW|restricted-context recursive pseudo-tools与固定workflow学习有贡献潜力，但FriMay29 16:02:26Z最早Jun1，registeredJun2，完整区间跨日；需公告或作者原始公开证。|
|2606.01139|本轮必要Source/唯一owner/实际整合与POST通过；2+1+2=5|AGENT-MEMORY|失败需先证skill-level defect才编辑、原则与执行证据绑定并保已成功行为，区分搜索版本与最终best-observed返回；不是无条件反馈循环。准入不等收益/Books已成立，原拟排理由已由R13纠正。 当前最终证据/限定采用见[SUP_SKILLREVISE_20261024.md](./SUP_SKILLREVISE_20261024.md)与SUP_CHECKPOINT_REVIEW_20261024 R2–4；原初筛未审状态仅历史。|
|2606.02372|拟准入6=2+2+2|MULTIMODAL-WORLD-MODELS|固定textWM与演进policy分布失配→futurefeedback可靠性reflection+onpolicy轨迹selfdistill循环→改变冻结WM消费；待核实际更新/无verifier范围。|
|2606.00660|拟准入5=2+1+2|AGENT-REFLECTION|稀疏正确轨迹/单总分校准不足→按显式子check对每candidate同准则验证后聚合→改变多数投票/单judge分选择，待固定生成与judge费用。|
|2606.00510|拟准入6=2+2+2|AGENT-TOOL-CALLING|skill相关不等当前应invoke→shared-prefix invoke/skip配对+两粒度偏好→把检索相关与调用效用区分；有限跨域而非通用迁移。|

其他导航还在按主题实际筛选，未冻结池、未完成Source或Books；不将未读条目标成排除或终态。首15以外的所有日期资格仍未批授。广谱Agent切片中纯领域应用（医疗/材料/无线/金融决策等）不因Agent命名进入；有可迁移机制/失效边界者仍须完整AB而非一刀排。

执行：2026-10-23；补充窗口 Jun02 BJT。仅写本文件与必要原件；未授 Books 写权，不自签 DAY。

已完整重读 AGENTS、Research/Report 合同、Sources每日与恢复说明、Prompt、ROADMAP、State本日路由及日报；旧87/719只作点查身份，不作队列。使用 using-agent-skills 作范围与验证路由，无代码实施。

## 来源入口与当前停止点

DataCite只作导航及精确联合日期的登记上界，不以Submitted/created冒公开。registered:[2026-06-01T16:00:00Z TO 2026-06-02T15:59:59Z] AND prefix:10.48550；首个未加主题的2580只诊断接口，未逐项筛选。随后有界Agent词族248（page1,size1000,totalPages1）与多模态词族214（同分页）标题导航；导航未等于贡献完成，继续按题意收窄。

Agent query titles agent/agents/agentic/RAG/retrieval/memory/tool/tools/workflow/workflows/multiagent/multi-agent OR description language agent/tool calling/retrieval augmented。
多模态 query titles multimodal/multi-modal/vision-language/VLA/world model/world models/diffusion/generative/video generation/image generation OR description foundation model AND video/image/robot。

查询API：https://api.datacite.org/dois 。当前仅首批以下完整题摘已读；其余导航非已审、不是待强制关闭总数。实际公开窗口资格待每项精确v1及官方schedule联合证明。

## 首批准入校准原件

### Reliable Post-Retrieval Assembly for Agent Memory: Separating Evidence Extraction from Policy Execution — 10.48550/arxiv.2606.01435

- 原件：[arXiv exact v1](https://arxiv.org/abs/2606.01435v1)；[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2606.01435)。
- 登记：client=arxiv.content；state=findable；registered=2026-06-02T04:15:29Z；created=2026-06-02T04:15:28Z；dates=[{"date":"2026-05-31T20:13:43Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-06-02T01:23:37Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-08-02T16:06:48Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-08-04T01:12:26Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-06","dateType":"Available","dateInformation":"v1"}]；version=2。
- 判断：拟准入7（3+2+2），AGENT-MEMORY：same top10/chunking/backbone拆分extraction和policy控制，并以LongMemEval无显著优势限制局部成立；精确v1待核。

完整题摘（DataCite当前原始元数据；精确v1题摘/当前纠错信号仍待核）：

LLM-based memory systems can retrieve relevant evidence yet still fail when answer generation entangles semantic filtering, conflict resolution, prior suppression, and output generation in one step. We study this failure as a problem of post-retrieval assembly. In the MemoryAgentBench (MAB) release used here, FactConsolidation explicitly states that newer facts have larger serial numbers, yet the best reported retrieval/memory result is 54% single-hop and all 22 reported systems score at most 7% multi-hop. We evaluate a structured assembly interface in which an LLM first extracts semantically matching evidence into a candidate representation and a separate stage executes the required answer policy. At 262K, this pipeline reaches 82%/93% single-hop and 27%/41% multi-hop with gpt-4o-mini/gpt-4o, exceeding every result reported in the MAB v3 FactConsolidation comparison. This is a task-level result, not a claim that the evaluated memory architectures are broadly inferior. A controlled whole-pipeline comparison, with identical backbone, retrieved top-10 evidence, chunking, and n=100 per cell, improves single-hop accuracy by 10.8 percentage points (pp) on average and 21 pp at 262K. A targeted comparison using the same extraction setup shows that changing only the final policy executor contributes 2.0 pp on average and 0 pp at 262K. Most of the gain therefore comes from separating evidence identification from final policy execution rather than from the freshness operator itself. A LongMemEval check finds no significant overall advantage (26/45 versus 29/45; paired exact McNemar p=0.45), bounding the result to current-value questions with explicit version metadata. The evidence identifies post-retrieval assembly as a distinct reliability boundary between retrieval and answer generation.

### Agent System Operations: Categorization, Challenges, and Future Directions — 10.48550/arxiv.2606.01581

- 原件：[arXiv exact v1](https://arxiv.org/abs/2606.01581v1)；[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2606.01581)。
- 登记：client=arxiv.content；state=findable；registered=2026-06-02T04:19:01Z；created=2026-06-02T04:19:01Z；dates=[{"date":"2026-06-01T02:26:39Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-06-02T01:31:14Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-09-06T14:00:30Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-09-09T01:03:11Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-06","dateType":"Available","dateInformation":"v1"}]；version=2。
- 判断：明确贡献排除：survey分类与四阶段AgentOps框架，完整摘要未提供新增机制或受验证的失效边界，不以框架命名/owner可映射入选；无明显纠错信号，日期未进一步核。

完整题摘（DataCite当前原始元数据；精确v1题摘/当前纠错信号仍待核）：

As the reasoning capabilities of Large Language Models (LLMs) continue to advance, LLM-based agent systems offer advantages in flexibility and interpretability over traditional systems, garnering increasing attention. However, despite the widespread research interest and industrial application of agent systems, these systems, like their traditional counterparts, frequently encounter anomalies. These anomalies lead to instability and insecurity, hindering their further development. Therefore, a comprehensive and systematic approach to the operation and maintenance of agent systems is urgently needed. Unfortunately, current research on the operations of agent systems is sparse. To address this gap, we have undertaken a survey on agent system operations with the aim of establishing a clear framework for the field, defining the challenges, and facilitating further development. Specifically, this paper begins by systematically defining anomalies within agent systems, categorizing them into intra-agent anomalies and inter-agent anomalies. Next, we introduce a novel and comprehensive operational framework for agent systems, dubbed Agent System Operations (AgentOps). We provide detailed definitions and explanations of its four key stages: monitoring, anomaly detection, root cause localization, and resolution.

### Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains — 10.48550/arxiv.2606.02357

- 原件：[arXiv exact v1](https://arxiv.org/abs/2606.02357v1)；[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2606.02357)。
- 登记：client=arxiv.content；state=findable；registered=2026-06-02T04:37:24Z；created=2026-06-02T04:37:24Z；dates=[{"date":"2026-06-01T15:04:25Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-06-02T02:16:30Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-08-27T10:57:33Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-08-28T00:45:44Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-06","dateType":"Available","dateInformation":"v1"}]；version=2。
- 判断：拟准入7（3+2+2），AGENT-TOOL-CALLING：同源ToolFree/PureText、loop/format/result对照反证工具trace不等tool信息贡献；精确v1待核。

完整题摘（DataCite当前原始元数据；精确v1题摘/当前纠错信号仍待核）：

Tool-augmented multimodal agents show strong benchmark gains, often taken as evidence that agents have learned to use tools. We argue that this interpretation can be premature: a tool-call trace alone does not show whether the tool supplied answer-critical information. We study two representative ``thinking with images'' agents, Thyme and DeepEyesV2, across real-world understanding, OCR, chart understanding, and mathematical reasoning. Each agent is compared with its Tool-Free counterpart and with a Pure-Text Reasoner trained from the same source pool without tool-calling trajectories. Tool access yields little consistent aggregate improvement, does not reliably reduce generated-token cost, and leaves only a small tool-only solved set: 93% of DeepEyesV2's tool-solved problems and 96% of Thyme's are also solved by at least one non-tool setting. Mechanism ablations further show that the full tool-use loop does not consistently outperform either the tool-call format or the returned execution result alone. In the settings we study, the analyzed agents appear to learn tool-calling patterns more reliably than tool-contributed capabilities, suggesting that evaluation should distinguish tool availability from whether tools actually expand what agents can solve.

### Retrieve What's Missing: Coverage-Maximizing Retrieval for Consistent Long Video Generation — 10.48550/arxiv.2606.02479

- 原件：[arXiv exact v1](https://arxiv.org/abs/2606.02479v1)；[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2606.02479)。
- 登记：client=arxiv.content；state=findable；registered=2026-06-02T04:40:20Z；created=2026-06-02T04:40:20Z；dates=[{"date":"2026-06-01T16:49:58Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-06-02T02:23:03Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-06","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}]；version=1。
- 判断：拟准入6（2+2+2），MULTIMODAL-WORLD-MODELS：target-view residual coverage selection替代粗pose/FOV或完整3D重建，待匹配实验。官网v1已核Jun1 16:49:58 UTC，正常最早Jun2 00Z至registered全在Jun02 BJT。

完整题摘（DataCite当前原始元数据；精确v1题摘/当前纠错信号仍待核）：

Maintaining long-term geometric consistency remains challenging for long-horizon autoregressive video generation. Memory-augmented generative models address this by retrieving historical frames, but their effectiveness depends on two key design choices: what 3D-geometric evidence should represent past observations, and how memory frames should be selected from this evidence. Existing methods often rely on camera poses or field-of-view overlap, which are lightweight but too coarse to reason about pixel-wise visibility, or use explicit 3D reconstruction, which provides fine-grained evidence but is costly to maintain over long rollouts. We propose Coverage-Maximizing Retrieval-Augmented Generation (COVRAG), a depth-based memory retrieval framework that uses pretrained 3D priors to construct a target-view coverage map as lightweight 3D memory evidence. For frame selection, COVRAG maximizes residual coverage gain, iteratively retrieving frames that explain target-view regions not covered by the current context or previously selected memories. To improve scalability in long-video generation, we introduce sliding-window depth caching for efficient geometry estimation. Experiments on RealEstate10K and DL3DV10K show that COVRAG improves long-horizon geometric consistency while maintaining low latency compared to baselines.

### Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools — 10.48550/arxiv.2606.02483

- 原件：[arXiv exact v1](https://arxiv.org/abs/2606.02483v1)；[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2606.02483)。
- 登记：client=arxiv.content；state=findable；registered=2026-06-02T04:40:26Z；created=2026-06-02T04:40:25Z；dates=[{"date":"2026-06-01T16:53:19Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-06-02T02:23:21Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-06","dateType":"Available","dateInformation":"v1"},{"date":"2026","dateType":"Issued"}]；version=1。
- 判断：拟准入8（3+2+3），AGENT-TOOL-CALLING：issue-time参数/目的地投影在外部观察不可撤回条件下的隐私机制，待机制证据限定，不借成熟issue/commit原则加分。官网v1已核Jun1 16:53:19 UTC，正常最早Jun2 00Z至registered全在Jun02 BJT。

完整题摘（DataCite当前原始元数据；精确v1题摘/当前纠错信号仍待核）：

Tool-augmented language agents speculatively issue likely future tool calls to hide latency, but those calls leak inferred user intent to external services before the agent commits to the branch. Every external observer that received the call retains the disclosure after the agent abandons the branch. Timing is the issue, not authorization: no commit-time cleanup, read-only restriction, or access-control allow-list unsends what an observer already holds. We call these invocations ghost tool calls and propose Speculative Tool Privacy Contracts, a runtime abstraction that treats observation before commitment as a first-class effect, distinct from state mutation. We implement the contracts in a prototype runtime and evaluate twelve policies across three corpora. Speculative dispatch increases what an observer can infer about user intent; post-hoc filters, read-only restrictions, and access-control allow-lists leave that inference intact; only issue-time policies that change or suppress the speculative call's argument or destination projection before dispatch reduce it.

### Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design — 10.48550/arxiv.2606.02507

- 原件：[arXiv exact v1](https://arxiv.org/abs/2606.02507v1)；[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2606.02507)。
- 登记：client=arxiv.content；state=findable；registered=2026-06-02T04:40:59Z；created=2026-06-02T04:40:59Z；dates=[{"date":"2026-06-01T17:20:55Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-06-02T02:25:09Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-08-21T12:16:45Z","dateType":"Submitted","dateInformation":"v2"},{"date":"2026-08-24T00:39:10Z","dateType":"Updated","dateInformation":"v2"},{"date":"2026-06","dateType":"Available","dateInformation":"v1"}]；version=2。
- 判断：范围排除：inverse materials design属于当前暂缓AIforScience，不通过生成/闭环词汇重入。

完整题摘（DataCite当前原始元数据；精确v1题摘/当前纠错信号仍待核）：

Inverse materials design is shifting materials discovery from forward prediction toward targeted proposal of candidates that satisfy objectives under physical constraints. Here, we review advances in generative crystal structure modeling, multimodal learning, and closed-loop design pipelines for crystalline solids. We survey how generators learn chemical-structural priors from databases to enable controllable sampling of periodic structures, comparing variational autoencoders, normalizing flows, autoregressive models, and diffusion models. Across these families, we examine where feasibility constraints and physical priors enter, from representations and training objectives to sampling-time guidance, screening, and relaxation. We also discuss multimodal learning combining crystal structures, thermodynamic and electronic information, microscopy, spectroscopy, processing context, and scientific text to construct materials representations. Inverse-design strategies integrating conditional generation with latent optimization, Bayesian optimization, reinforcement learning, and active learning are also examined. We highlight recurring failure modes, including surrogate exploitation, diversity collapse, distribution shift, and the stability-synthesizability gap, and outline evaluation based on validity, novelty, uniqueness, stability, and cost. To support credible claims, we define a nine-rung discovery-credibility ladder and propose a minimum reporting standard: declared matching tolerances and database snapshots; separate reporting of uniqueness, training-set memorization, and external rediscovery; novelty as a continuous distance distribution; energy-above-hull distributions with functional and hull version; relaxation-survival and dynamical stability rates; and validation cost per credible hit. Headline validity or S.U.N. rates without these disclosures should be treated as uninformative.

## 精确v1核验与准入更新

精确官方原字段与AB抽取：[SUP_AGENT_EXACT_BATCH1_20261023.json](./SUP_AGENT_EXACT_BATCH1_20261023.json)。抓取2026-10-23，四项官网未见撤回/勘误标记；仅作当页有限检查。

### 2606.02483 exact v1

Title: Ghost Tool Calls: Issue-Time Privacy for Speculative Agent Tools

From: Bardia Mohammadi [ view email ]            [v1]
        Mon, 1 Jun 2026 16:53:19 UTC (249 KB)

Abstract: Tool-augmented language agents speculatively issue likely future tool calls to hide latency, but those calls leak inferred user intent to external services before the agent commits to the branch. Every external observer that received the call retains the disclosure after the agent abandons the branch. Timing is the issue, not authorization: no commit-time cleanup, read-only restriction, or access-control allow-list unsends what an observer already holds. We call these invocations ghost tool calls and propose Speculative Tool Privacy Contracts, a runtime abstraction that treats observation before commitment as a first-class effect, distinct from state mutation. We implement the contracts in a prototype runtime and evaluate twelve policies across three corpora. Speculative dispatch increases what an observer can infer about user intent; post-hoc filters, read-only restrictions, and access-control allow-lists leave that inference intact; only issue-time policies that change or suppress the speculative call's argument or destination projection before dispatch reduce it.

### 2606.02479 exact v1

Title: Retrieve What's Missing: Coverage-Maximizing Retrieval for Consistent Long Video Generation

From: Minseok Joo [ view email ]            [v1]
        Mon, 1 Jun 2026 16:49:58 UTC (7,613 KB)

Abstract: Maintaining long-term geometric consistency remains challenging for long-horizon autoregressive video generation. Memory-augmented generative models address this by retrieving historical frames, but their effectiveness depends on two key design choices: what 3D-geometric evidence should represent past observations, and how memory frames should be selected from this evidence. Existing methods often rely on camera poses or field-of-view overlap, which are lightweight but too coarse to reason about pixel-wise visibility, or use explicit 3D reconstruction, which provides fine-grained evidence but is costly to maintain over long rollouts. We propose Coverage-Maximizing Retrieval-Augmented Generation (COVRAG), a depth-based memory retrieval framework that uses pretrained 3D priors to construct a target-view coverage map as lightweight 3D memory evidence. For frame selection, COVRAG maximizes residual coverage gain, iteratively retrieving frames that explain target-view regions not covered by the current context or previously selected memories. To improve scalability in long-video generation, we introduce sliding-window depth caching for efficient geometry estimation. Experiments on RealEstate10K and DL3DV10K show that COVRAG improves long-horizon geometric consistency while maintaining low latency compared to baselines.

### 2606.02357 exact v1

Title: Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains

From: Jiawei Guo [ view email ]            [v1]
        Mon, 1 Jun 2026 15:04:25 UTC (1,002 KB)
              [v2]
        Thu, 27 Aug 2026 10:57:33 UTC (1,002 KB)

Abstract: Tool-augmented multimodal agents show strong benchmark gains, often taken as evidence that agents have learned to use tools. We argue that this interpretation can be premature: a tool-call trace alone does not show whether the tool supplied answer-critical information. We study two representative ``thinking with images'' agents, Thyme and DeepEyesV2, across real-world understanding, OCR, chart understanding, and mathematical reasoning. Each agent is compared with its Tool-Free counterpart and with a Pure-Text Reasoner trained from the same source pool without tool-calling trajectories. Tool access yields little consistent aggregate improvement, does not reliably reduce generated-token cost, and leaves only a small tool-only solved set: 93% of DeepEyesV2's tool-solved problems and 96% of Thyme's are also solved by at least one non-tool setting. Mechanism ablations further show that the full tool-use loop does not consistently outperform either the tool-call format or the returned execution result alone. In the settings we study, the analyzed agents appear to learn tool-calling patterns more reliably than tool-contributed capabilities, suggesting that evaluation should distinguish tool availability from whether tools actually expand what agents can solve.

### 2606.01435 exact v1

Title: Don't Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution

From: Vikas Reddy Challaram [ view email ]            [v1]
        Sun, 31 May 2026 20:13:43 UTC (33 KB)
              [v2]
        Sun, 2 Aug 2026 16:06:48 UTC (17 KB)

Abstract: LLM-based memory systems increasingly maintain facts that evolve over time, where a recurring failure is conflict resolution: when a fact has multiple contradictory values, which should the agent return? MemoryAgentBench (MAB; Hu et al., 2026) makes this explicit in its FactConsolidation task: facts are numbered, the counterfactual has the higher serial, and agents are told newer facts have larger serials. Yet every published system underperforms: HippoRAG-v2 reaches 54% on single-hop (FC-SH), BM25 48%, Mem0 18%, and the temporal KG Zep/Graphiti just 7%. Multi-hop is near-unsolved (at most 7% across 22 systems).
 We argue the bottleneck is the assembly step: baselines leave conflict resolution to LLM-mediated retrieval or generation rather than version-aware aggregation. A matched-setup comparison (same backbone, retrieval, chunking, TOP_K) shows that replacing the LLM-judgment answer pipeline with candidate-extraction plus Python max(serial) yields +10.8 points on FC-SH (gpt-4o-mini), widening from +8 at 6K to +21 at 262K. This is a whole-pipeline effect (resolver, prompt, format, and temperature vary jointly); isolating the resolver is future work. The recipe reaches 78.0% on FC-SH (gpt-4o-mini), 94.8% (gpt-4o), and 30.2% on FC-MH (gpt-4o-mini, rising to 51.5% with gpt-4o) via a per-hop deterministic extension of Self-Ask. At matched-262K, it beats HippoRAG-v2 by +28 points and the best published FC-MH result by +20.
 The implication is corrective for the subfield: the bottleneck on conflict resolution is assembly (post-retrieval aggregation), not storage. A LongMemEval knowledge-update check shows the mechanism ports from max(serial) to max(timestamp) but only ties LLM judgment (57.8% vs 64.4%, n=45): deterministic aggregation is the right primitive for current-value conflicts and must be composed with question-type-aware handling for broader memory QA.

01435当前v2题名/isolated executor结果不可反投v1。v1准入仍是post-retrieval assembly边界的matched whole-pipeline反证，不能归因max(serial)单算子；作者曾提出收窄6分，但root R2实际完整校准保留原初3+2+2=7，已按必要深入读，不为处置减分。v1 LongMemEval只支持n45局部无优于对照，不能以v2 p值补造。

四项日期联合：v1提交May31或Jun01，均在Mon Jun01 18Z cutoff前，官方常规最早公告Jun02 00Z；对应registered 04:15:29/04:37:24/04:40:20/04:40:26Z为同一Jun02 BJT内上界。当前DataCite exactDOI/arxiv.content/findable原字段已核；无需假定正常schedule就是实际公告。官方适用历史schedule/发号规则由root集中核验，此处引用研究合同已载明2025-01-06版。联合界不证明全球首公开或v1逐字历史，未发现具体更早正文线索。

## 首四项必要Source与实际owner比较（作者准备；未自签独核）

root R2已实际完整读首六题摘及exact batch1四v1，通过四项准入和两排除；首四分8/6/7/7不变。下列为后续证据准备，不等于日级或Books验收。已完整读Books上下文PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE，实际读owner命中段及必要前后交接。

### 02483 — Source准备/Books具体差额

[exact-v1](https://arxiv.org/html/2606.02483v1) §3–5、Limitations完整中介/label/provider，必要读取到决定性反侧即停。Runtime把每次speculative event绑定observer/argument/destination/confidence/audit，前置五动作与按observer的issued-vs-committed投影；soundness仅A1完整中介、A2标签正确、A3动作保限制三假设。原型sensitivity label macroF1仅0.10(n394,Opus annotator)，remote planner provider在trusted边界内；未测多租户争用等通道，latency非生产保证。配对回放/HTTP与AgentDojo局部排序支持投影前置，不证明绝对隐私。未核artifact/复现。

AGENT-TOOL-CALLING当前Side-effect Class 408–419只说read-only仍泄漏，Evaluation 565附近SIA仍要求错误分支可撤销，未拥有observer在issue时已保存、日志/队列/telemetry也须前置中介的责任。建议窄整合在该SIA段后：把可撤销状态effect与不可撤回observation分开，投机调用在出界前决定rewrite/shadow/defer/block；明确三假设/label低可靠反侧，计入额外calls/误defer和替身质量；不合格时保留no-spec串行。非模型或PLATFORM-SECURITY第二owner。待root必要Source+PRE，不写书。

### 02479 — Source准备/Books具体差额

[exact-v1](https://arxiv.org/html/2606.02479v1) §4 Eq2–6/Algorithm1、§5.1–5.3/T1–2、AppB2/T4–5、C。Depth+pose回投生成binary target覆盖，贪心只取未被context/已选mem覆盖的增量；固定局部VGGT窗口和depth cache不等全局3D地图。相同DFoT/memory conditioning、2 frames预算；RE10K256²、40帧loop-close及DL3DV100帧有限比较。强图像退化L4使MEt3R .154劣于WorldMem .141，几何估错、生成漂移和非全局一致近文。检索比WorldMem慢，附录40→120帧端到端均值+7.3%；不是加速或实时SLO。训练8H100，推理具体硬件/精度Not Disclosed于已读必要域，未核代码/像素/复现。

MULTIMODAL-WORLD-MODELS 883–916既有view/implicit memory与MemCam逐目标frustum overlap，但未解释pixel residual互补覆盖。建议MemCam后接一窄分支：从独立top-n到depth target-pixel residual set cover、缓存不等全局几何、取景/depth误差的退路。既有几何proxy边界保留；不可授真实动态或行动安全。待root必要Source+PRE，不写书。

### 02357 — Source准备/已有覆盖提案

[exact-v1](https://arxiv.org/html/2606.02357v1) §3.1–3.4、§4.1–4.3/T3–6。ToolFree是同模型禁工具的OOD诊断，PureText是同source pool但53K改写SFT/30K筛选RL的辅助参考，非严格训练对照；format/result干预既有trajectory，改变后续分布。Qwen3-VL-30B judge有40%人工抽样，Thyme chart仅16/推理123条tool-called样本，不能以93/96% union覆盖作因果必要性结论。有限对照说明trace不能独自归因工具信息收益，未核代码/复现。

AGENT-TOOL-CALLING当前552–556的semantic-body-binding已明确no-tool/call-shell/result、confirm/repair/harm/no-effect、额外费用、非严格因果、重放失败时离线fixture/只读shadow退路；实际承载拟采用受限命题，建议具体已有覆盖。保留OOD/PureText不匹配及小样本原证边界在报告，暂无新增正文必要；由root非writer复核而非本作者自签NC。

### 01435 — Source准备/Books具体差额

[exact-v1](https://arxiv.org/html/2606.01435v1) §3/4、§5.3–5.7、§6.4。Fact-level metadata→LLM匹配subject/predicate候选→Python max(serial)，多跳SelfAsk每hop同流程。相同mini/BM25top10/chunking，pipeline prompt/temp/format/task共同改变；+10.8pp不可归max单算子，published22系统未重跑。当前值显式总序才适用，partial-order不可直接max；LongMemEval45总体57.8<64.4，Yes/No/historical/count需不同handler；FC中10.5%只LLM正确，抽取过拒、hop1级联失效。API成本估算非部署吞吐；未核代码/复现。

AGENT-MEMORY 222段已有字段匹配重排/版本歧义，246已有supersession返回，1315–1326有CAS/conflict-set；尚无读取后candidate抽取与policy执行分责。建议222段后单段，在版本字段真实/明确当前值策略下确定性聚合，保whole-pipeline非归因、LongMemEval非优势/部分序/抽取失败与原文澄清退路；不把旧序号高直接授事实真值。待root必要Source+PRE，不写书。

首4Source补充最小域：02479 §5.2–5.3/T2实际完整补读。FoV+independent=.141 MEt3R，改residual=.130；depth targetcoverage+independent反而=.149，joint depth+residual=.100。故只替换更精细geometry并不足，需联合残余互补选择，不能用“深度一定优于pose”表述。02483 §5setup实际核固定byte-identical frontier与30task×3seed静态committedplan，primary adversary Opus4.7；labels仍rule-based不可靠。01435 §3.1实际核JSON候选保存serial/text/entity、include-all且不比较serial/选择best，空集返回noanswer；不能将结构化字段等于真实事实。

### 当前恢复层（2026-10-24，前文准备态不作待办重复）

batch2十三项已Source/Books处置；[B3十一项](./SUP_AGENT_B3_20261024.md)又完成10实际I/唯一非writer POST及00376中心证明争议隔离，证据见[本批独核R1–20](./SUP_NEXT_REVIEW_20261024.md)。原后47提案余23（Multi1十三/batch4十）待贡献校准，另01138/00476/02031/02536四决定性准入补读，共27普通项；五日期资格有限恢复及剩余有界发现仍未闭。上文早期Source/PRE准备标签只属历史过程，不重做已经真实验收的层。462导航不是全文配额；完整DAY未授。
