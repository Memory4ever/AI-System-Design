# Jun03 Agent 决定性初筛补读

root仅续Jun02补查。当前AGENTS、研究/Report/Daily来源及恢复、Prompt、ROADMAP与本日停点已重读；本记录只解决01138/02536原本含糊的准入事实，未把后续全部方法/代码审阅设为初筛默认。原完整v1题摘分别保留[batch3](SUP_AGENT_EXACT_BATCH3_20261023.json)/[batch4](SUP_AGENT_EXACT_BATCH4_20261023.json)，初筛原提案与原因不删除。下述为待独核改判提案，不预记排除生效、评分、Source/Books完成或DAY；00476/02031两决定性事实尚未补读。

## 02536：拟贡献前关闭

[当前abs](https://arxiv.org/abs/2606.02536)所见唯一v1，无撤回/删除/勘误；实际打开[exact-v1 §3–5](https://arxiv.org/html/2606.02536v1#S3)定点找labels是否连接实际behavior，以及协议是否新增具体执行信任条件。68合成skill diff来自63原文件，以作者/LLM提出后人审的文本trait标签拟合通用embedding差向量的Ridge，LOOCV与YARA/LLM对照评价的是这份文本方向标签；未运行有行为groundtruth的agent人口。部署演示是同一Hermes兼任两角色、计算日志中SSH/VM编辑得到较高分，未建立行为变化、风险概率或实际effect的验证。

server控制trait vector、B发送embedding并不认证B交付了真实/完整skill树；§4.1明确假树/隐瞒文件不覆盖，连续hash链和完整spec为未来。§5的可信server/embedding、未来HMAC/nonce也不是新的已证明执行权限机制；AppendixA将分数映为概率仍靠未来行为或top-down估计，不是现成校准。root不采用其“近零错误分数表示不确定”的解释，也不把此处一般proxy/行为分责反推成论文已新增可迁移失效证据。

拟关闭具体理由：当前增量是通用语义embedding＋线性模型对单trait合成文本标签的局部读出，以及常规trusted-mediator部署包装；既无新的agent执行/状态机制，也未用真实behavior对照改变trait-proxy或safe-update的有效边界。不是因为“实验小/论文负面/不能映章节”而排，而是原先待确认的行为验证事实未出现，不能替作者补成新安全评价机制。身份保留，不评分/不进正式候选或Books；新行为验证、完整执行承诺或具体新失效证据出现时可定点重开。日期无需为不影响该处置的时间点另设请求。

## 01138：拟贡献前关闭；版本身份边界保留

[当前abs](https://arxiv.org/abs/2606.01138)为v4，当前所见无撤回/删除；历史v1提交May31，原精确题摘title为AMP。当前[URL带v1的HTML](https://arxiv.org/html/2606.01138v1)呈memorywire并说明曾名AMP，原字段不改；不采用后来PurgeBench/recover或v3/v4事实来决定Jun02贡献。

原完整AB已明说贡献不是新算法，而是RRF、FSM、STM/LTM、diff-and-approve打包。root定点读§3.4–3.7、§4.5及§5.3的操作/权限接口与conformance解释：五CRUD/merge/expire操作通过MemoryStore与capability声明适配；写前可把原请求/structured diff交reviewer，approved后commit，读取默认无approval；多backend容错继续返回surviving结果。conformance以required capabilities跳过不支持项，68PASS/12SKIP不等五adapter完整语义等价；定点材料未给新原子commit/跨store冲突规则或可证明的整体一致性。RRF majority-benign/gold已同意的构造并非新的fusion原理。

拟关闭理由限当前准入问题：已有memory操作、RRF、FSM及批准流的共同schema/SDK包装与小规模conformance示例，未建立足以改变本项目长期设计判断的新操作语义、兼容/提交机制或新的受控有效性边界；不能由“vendor-neutral”、adapter数或开源量反推重要长期增量。不是所有协议包装均无价值，也不是按“非新算法”一词自动排除。若精确历史spec/实现出现具体新一致性/commit约束或有新边界反证，再定点重开。此拟关闭不依赖当前HTML里新增版本细节，原身份/标题与解释边界保留，不预评分或Books。

以上两项待本日独立reader对原决定性事实及具体误收/漏收风险校准，未独核前仍属普通未完成，不计终态或DAY。

## 独核后的当前采用：02536关闭，01138撤回N并继续有限证据

独核R46确认02536具体贡献前N，不评分/候选/Books。独核R47**否决上述01138 N提案**：原v1 conformance具体暴露跨adapter的user scope丢失、空ExpirePolicy变全选、synthetic id不能执行逐记录delete/merge，已经形成改变操作兼容判断的具名反侧，不是仅把成熟规则重述。原拟N理由保留为被纠正过程，不再作为当前处置。00476/02031仍待决定性补读，不将四项整体假归零。

R47实际回exact-v1 PDF第一页版本/改名说明及pp10–11 §5.3核同，兼容反侧不是v3/v4/PurgeBench/recover新结论。日期原NAV精确DOI/client arxiv.content/findable registered Jun02 04:08:15Z，v1May31 10:18:56Z，完整联合区间Jun02 00Z–04:08:15Z为Jun02北京时间；不把登记或提交写成实际公告。root已实际读回这组依据，不重GET既有日期。

### 01138 最小必要 Scope 与评分

采用命题改为：共同schema与MemoryStore签名不保证记忆操作可替换；capability-qualified测试的SKIP必须和实际scope/id/空policy语义分开验，而非笼统采纳新协议。拟2+2+2=6，D2具体兼容反证、Reach2调用层与异质存储、Durability2稳定的操作资格；不是给RRF/FSM或协议品牌加分。

root已在上述定点§3.4–3.7/4.5/5.3之后实际补读§3.2/4.2、Table5完整16×5、§5.4限制及直接§5.2受限威胁说明：SQL自有schema后端与SDK包装后端字段fidelity不同；具体skip使68PASS/12SKIP/0FAIL不能冒全80通过。forget有显式ids/filter scope不等adapter真的可删除同一记录，user_id缺失不能让agent_id/dataset静默继承用户隔离，empty-policy全选也非请求者明确批准的TTL。未核对应代码或重跑conformance，不宣称当前mem0/Letta/Cognee所有版本仍有这些行为；采用限论文v0适配快照。

作者自造小语料/单开发机、SDK支持差异与跳过集限制外推，不给生产SLO/安全证明；并行fanout丢单后端失败可继续返回不等跨store原子提交，写前approval也不保证读取权限。RRF对照预设大多数良性后端已正确同意gold，不作为任意恶意存储防御。v0.2规范提案不是实现已修；不采用PurgeBench、后版recover或所有协议一统的保证。原件已有有效版本/日期/核心反侧，经R47首事实→root实际必要域采用两角色即可，不要求reader第三读全部原域。

### actual owner / 单段 PRE（尚未授写）

唯一 `AGENT-MEMORY` / [Ch77](../../../../../books/part-07-agent/77-memory.md)。root实际读typed transition完整组、Hy-Memory迁移完整段、下方更新信任/敏感tool交接，及Ch76/78开篇；原书有cutover/import/add与authority，不含异质backend user scope、record id与空ExpirePolicy在共接口下不保真的反侧。精确01138/memorywire无既存family；Ch83只拥有跨工具协议简述，不复制记忆mutation语义。

在Hy-Memory完整迁移段及其marker后、下方“可执行的更新成功，也不等于写入内容可信”完整段前插一自然段：
> 统一SDK之后，还要逐操作确认后端能保住哪些语义，不能把共同schema、方法签名或“全部未跳过测试通过”当作可自由替换。一个[记忆适配器的受限conformance对照](https://arxiv.org/html/2606.01138v1#S5.SS3)中，能力不足的组合会跳过测试：独立user scope可能丢失，未表露的真实record id让逐项删除/合并失效，空过期policy还可能落成全选。这些是论文适配快照的具体反侧，不是所有后端当前版本的断言。调用方应绑定scope映射、稳定id、空policy和不支持操作的失败方式；capability只是声明，迁移验收仍须检查实际状态变化，不能让SKIP继承通过权限。逐后端语义回归、字段编码、失败恢复与来源追踪增加维护费，多后端容错返回也不授原子提交；合同不合时，保原存储authority、限制可用操作或拒绝切换，不以小规模零FAIL或统一接口批准隔离、删除和生产可靠性。<!-- source-family:SF-2026-ARXIV-2606-01138 -->

上下直接完整段已读，分别为Ch77 Hy-Memory迁移全段与memory-poisoning更新可信全段（含独立05504 marker）；不拆原组。本人true-H2注只记v0适配快照/必要边界、R47纠正、实际独立采用和保存/POST状态。下一仅核新score/actualowner/原单段PRE，尚未实际写入、未计整合或DAY。

## 当前01138实际采用与另两决定性准入提案

01138原单段及本人true-H2注已root在Ch77真实保存、完整新增/直接完整两侧与本人注自读，独核R48原PRE及R50唯一actualPOST均通过，6分真实I生效释放；原N已撤回，不再列普通未判。02536 R46具体N有效。尚未整体DAY/最终候选冻结。

### 00476 — 拟准入，尚未必要 Source/owner

原完整短AB见batch3，不用当前v2摘要倒填。本轮实际读[exact-v1 §3.3](https://arxiv.org/html/2606.00476v1#S3.SS3)决定性测量定义：把reasoning→自述conclusion与tagged conclusion→JSON action拆开，比较显式DECISION与自由文本regex抽取；参考是500次Monte-Carlo equity配阈值heuristic，原文自己说明非精确GTO。定点事实已足回答“有没有新测量接口”，不是只看到一个扑克应用榜。原约束是把reasoning/action差全归模型不忠实 → 同轨迹结论读出parser与推理/动作两段分账 → 重新考虑process-fidelity失败归因，故拟准入；不采用任何当前v2人口、比例或“唯一主因”，未审完v1主结果/不确定性，不预评分或Books。

[当前abs](https://arxiv.org/abs/2606.00476)所见v2，有修订但无撤回/勘误说明；仅为轻量notice，不因版本号扩大比较。精确v1 history为May30 02:02:21Z，[原Agent NAV](SUP_AGENT_NAV_20261023.json)同DOI/client arxiv.content/state findable/registered Jun02 03:52:25Z；沿适用公告日程最早Jun02 00Z，联合区间全Jun02北京时间，仍待独立准入/组合日证核。

### 02031 — 拟准入，尚未必要 Source/owner

原完整AB见batch4；为解决“只列工程组件还是有新设计边界”，本轮定点读[exact-v1 §5.4–5.5/Table4](https://arxiv.org/html/2606.02031v1#S5.SS4)。同SFT初始化、相同训练配方的context对照以15-step-only为基准，移除historical reasoning、text environment feedback或增加第二张截图的影响不同；多截图并不稳定更好。15→30 horizon课程另与fixed-horizon比较；更强/更多SFT warm-start并非后续RL更好，但该data分布也不同，不给policy-plasticity单因果。原约束是把live-web RL只看demo数/最终榜 → 具体horizon与history支持的受限消融 → 重新考虑rollout/context训练人口与预算，而非按开源/SOTA准入。拟准入，不预评分或已证实机制，后续只审拟采用接口和直接反侧/总训练费，不遍历完整36页/案例prompt。

[当前abs](https://arxiv.org/abs/2606.02031)所见v2、无撤回/勘误说明，不追全部版本；精确v1 history为Jun01 10:20:10Z，原NAV同DOI/client arxiv.content/state findable/registered Jun02 04:29:43Z；最早Jun02 00Z至登记最晚界全Jun02北京时间，尚待独立组合日证。没有把提交或登记冒实际公开，不先列正式候选/Source完成。

## R51后：00476首次必要Source与actual owner提案

R51已独核00476/02031两条决定性准入及联合Jun02日期，不再处于上节“待准入”状态；不预评分/必要审阅通过。root只继续00476，02031仍普通必要待办。重读当前AGENTS/适用研究与Report合同、Daily来源、Prompt和本日停点；改书前已读ROADMAP/PROJECT_CONTEXT/学习理念/写作指南、actual Ch66局部与Ch65/67开篇，Ch80反思/translation-fidelity仅用于明确不接管该测量owner。

**精确版本。** 本轮实际读[标v1 HTML](https://arxiv.org/html/2606.00476v1)§3–5/Table1–2及限制。因所存v1索引摘要只有三句，而HTML摘要展开了细数字，进一步定点打开[精确v1 PDF](https://arxiv.org/pdf/2606.00476v1)：可读第一页正文与页脚实际标 `arXiv:2606.00476v1 [cs.AI] 30 May 2026`，摘要与该HTML一致，均已有三模型/显式tag与自由文本抽取的描述。短metadata AB不是完整PDF正文的上限；不再假定原v1必无这些结果，也没有用v2补回。网页工具PDF首屏图像抓取cache miss，故不声称像素审图；本次只以实际可读精确PDF文本核版本/摘要，布局不影响采用命题，不循环抓图。当前官方abs轻量notice沿上节有效v2/无可见撤回勘误，不重做全版本比较。

**拟评分2+1+2=5。** 增量是把可见reasoning→自述结论与结论→JSON action拆开，单独验conclusion reader，改变将抽取噪声归给模型行为的判断；Reach局限测量组件，不因多Agent桌面或扑克应用升级跨系统。5分标准必要与拟采用具体owner差额定点深入；未核实现或复现。

**必要证据及边界。** 同一模型四策略各占固定seat，Claude Haiku4.5/Flash-Lite各200手、DeepSeek-v4-pro50手，另仅Claude作50手GTO-verbose。每手reset stack不使同手的多decision或相同seat策略成为独立随机实验；Table1 Wilson区间按decision计，不能当hand/seat聚类不确定性已控制。500次Monte-Carlo equity加阈值是固定heuristic reference，不是精确GTO或真实社会行为oracle。DECISION tag与JSON比较只测结论/动作一致，EQUITY/POT_ODDS/RULE/DECISION读出另测模型所述前提到结论；其内部真实计算不因此可见。regex从多候选语句取末命中与显式tag在可解析人口/parse rate上不同，不能把全部比例差额叫控制住所有行为条件的纯parser因果。显式elicitation自己可能改变行为，§5明确承认。

Table1三模型tag inconsistency .3/1.8/0%，free phrase 26.4/22/33.3%，相应parse rate 100/100/98%对51/76/44%；缺失与可解析分母必须另报，不能只引0证明可靠。§4.2所谓65% rule-misapplication只在Claude verbose、可解释错误decision子集，equity容差.15是作者判准；不推广所有模型/任务、隐藏意图或通用风险厌恶原因。Table2规则prompt不居最优是本桌/策略/seat配置观察，不是全部外部规则无用的定律。每步模型默认temperature，精确采样值/precision/厂商硬件/端到端length-batch-concurrency-SLO与完整seed/repeat未披露；该文主张测量而非服务性能，不补齐或采用净加速。显式读出、两parser/缺失审计、Monte-Carlo/reference、全部模型调用和独立核验计费。

**actual owner与具体差额。** 唯一 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。现文“自动prompt优化…宽松parser/严格JSON”已有格式/消费者分账，“诊断菜单/自由文本”已有映射噪声，“SMT推理reference”已有支持资格；但未把同一Agent的自述前提→自述结论→真实动作三对象分开，也无结论读出噪声能掩盖上游推断失败的这一具名反例。Ch80拥有反馈/revision而非本评价接口，不因旧初筛路由误写反思机制。精确family/标题无现正文。

拟在Ch66“自动 prompt 优化还会把评分器与实际消费者的差异放大”完整段及2610-13287 marker后、下一“对有参考答案的客观文本任务”完整段及2604-09497 marker前，仅加一个自然段：
> 对Agent的推理自述，解析器还应分开读出前提、最后声明的结论与实际执行动作：结论和动作相符，不证明结论由所述前提有效推出；从自由文字猜出一个结论失败，也不直接证明Agent没有按自己的决定行动。[受限过程忠实性对照](https://arxiv.org/html/2606.00476v1#S3.SS3)用显式DECISION与JSON、另列输入/规则的诊断暴露这两种失败，reference却只是Monte-Carlo加阈值启发式，不是精确最优行为。应保原trace、tag/parser版本、未解析人口与每层结果；显式提问可能改变行为，固定seat与同手多decision也不等独立样本，不能把少量模型的低不一致率外推成隐藏推理忠实或通用可靠。结构化读出、参考求值、调用和独立人审均计费；读出或reference资格不足时保Unknown、原始输出与外部行为验证，不靠反复要求模型复述规则签发正确执行。<!-- source-family:SF-2026-ARXIV-2606-00476 -->

上述直接完整两侧已读，保原格式与语义scorer论证，不写新小节。true-H2本人注只记该必要域与采用边界。现交独立reader首次必要Source/score/actualowner/原单段PRE，不预授写、I或DAY；不等待02031完毕。

## 02031首次必要Source与actual owner提案

00476经R56独核及R58唯一实际POST已真实整合Ch66，不重做；本节仅续02031，沿R51有效准入与Jun02联合日证/轻量notice。root实际打开[exact-v1 HTML](https://arxiv.org/html/2606.02031v1)，读§4.1–4.4、§5/Table4与§5.4–5.5、A.4–A.6相关配置及§6–7限制性说明；不遍历36页case/prompt、额外rewardbench或代码。拟评分 **2+1+2=5**，只给多轮RL的horizon与条件信息支持选择及具体消融边界，不给开放发布/SOTA/组件数量加分。

**机制与成立条件。** live browser每trajectory各自page/history，单模型response可包含多个按序执行的browser工具；每call反馈由DOM变化等提取、非原子commit或完整环境真值。policy保完整历史model response（reasoning+calls）及text feedback，仅保最近K截图，默认K1；不是额外学出的独立长期记忆，也不是删除历史reasoning。§4.4明确rollout与optimization使用相同managed context、只assistant response计loss；终奖group advantage广播所有turn，mask掉observation不把其从后续条件移除。本文与§3普通MT目标的差别还包括不除trajectory turn数、非对称clip、零方差group过滤、无KL/entropy；这些不是本次“少截图”可单独承担的全部收益原因，不顺带重写全部目标或授真实过程credit。

**必要对照与反侧。** Table4 context消融同SFT起点/配方，但只在15-step-only baseline上做；full主模型是15→30课程，不能把history/feedback消融差额全从full 74.1/67/64减出。去historical reasoning相对15-step低14.6/23.7/8.6百分点，去text反馈低5.2/8/6.6；K2对K1则-1.9/+0.3/-4.0，没有一致变好，不是“所有旧截图无用”。固定10/15/30 horizon与课程比较只支持该任务/recipe选择，增加cap同时改变探索支持与费用，不授普适阈值。§5.5的1.9K与0.4K warm start不止数据量变、分布和筛选也变，policy plasticity仅作者解释，不能作为更少SFT本身更优的因果。PPOepochs2对1/3与dynamic-sampling切片同样受任务/预算限定。

**评价合同与费用。** 主Qwen3-VL-4B-Thinking，412条/70站SFT、约2.2K live任务；LoRA不在本文默认目标中，不能沿别篇填。训练表为G5/48有效groups、maxresponse1024/context32768、T.8、clip.2/.28、Adam lr1e-6、Megatron TP4、80–100浏览器sandbox；A.5称约300 B200 GPU hours/90iteration，而§5又写90轮15step后续50轮30step，具体总计费覆盖的阶段有歧义，不合成精确统一训练预算。context段约240→400 GPU hours也不当完整pipeline净省。评估max30step、response4096、16sandboxes、SGLang bf16 TP2/DP4；official T.6/top-p.95/top-k20与去abort的T0/top-p1/top-k1协议不同，不混作同样人口。WebVoyager为FARA版595题/GPT4o，OnlineMind2Web300/o4-mini，DeepShop150/GPT4o；复用旧报告的站点时间与更长cap并不构成同预算SOTA因果。

默认训练GPT4.1或蒸馏judge，teacher标注heldout500轨迹的agreement不是独立真实成功率，格式/blocked/timeout与真正任务失败需另记；去abort分母不是现实请求可靠率。teacher轨迹、筛选、judge训练/调用、所有失败/被筛rollout、截图/token、浏览器、全部阶段更新与回归都计费；服务SLO、完整repeat/CI未给，不补生产可靠性。只采用conditioned-context和cap的实验分责，不采通用最优horizon/最小截图、judge真值、plasticity因果或整个系统已复现。

**实际owner。** `TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md)。实际读curriculum/group-size完整组及AgentGym-RL horizon段、后接稀有正确轨迹两段，另核多轮tool observation/mask组和Ch32/34开篇；Ch75精确family/标题无正文。已有Ch33课程段拥有cap选择与全预算，故不再复制15→30方法；具体缺口是多模态训练每一步的visual history/text feedback/reasoning支持与rollout/update同条件，在同horizon对照下选择。不是按原初筛AGENT-WORKFLOW直接落书，也不把ctx全部抄成Ch75第二owner。

拟Ch33 AgentGym-RL完整horizon段及其2509-08755独立marker后、下一“这里还要把能够形成相对更新与覆盖同一题稀有正确解法分开”完整段前，仅一自然段：
> 放宽交互步数，还要明确每一步保留什么条件信息，而不能只把截图数当上下文预算。[受限live-web训练对照](https://arxiv.org/html/2606.02031v1#S5.SS4)保留历史reasoning/tool calls与逐call文本反馈、仅留最近截图，并在rollout和优化重建同一managed context；丢旧图不等删除历史，文本反馈也不是完整环境真值。同起点的15步对照中，去历史reasoning或反馈会退步，增加第二张截图却有增有退，因此context消融应对同horizon基线，不把15→30课程的全部收益归给某种记忆。截图/token、browser、失败及被筛rollout、judge和训练均计费，更多SFT同时改变数据人口也不能证明可塑性单因果。条件重建、视觉支持或净质量不稳时，保留已验context/horizon与独立任务评价，不从更少截图、较高终奖或被排除失败后的成功率批准普适最优和真实运行可靠性。<!-- source-family:SF-2026-ARXIV-2606-02031 -->

已读直接完整两侧，原horizon课程与稀有模式采样论证保留；本人true-H2注只记实际必要域和状态。下一仅需同日reader首次必要Source/score/actualowner/原单段PRE，未获新窄授/未SAVE/I/DAY。该项准备好即交，不等另23准入。
