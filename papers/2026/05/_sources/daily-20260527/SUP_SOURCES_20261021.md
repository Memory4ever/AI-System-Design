# 2026-05-27 遗漏补查原始依据（2026-10-21）

## A1 实际基线与范围

作者：supp_may27_author；唯一非作者 reader：root（独占 SUP_REVIEW）。已实际重读本日适用 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES 用法/每日组/arXiv 主题、CODEX_RESEARCH_PROMPT、ROADMAP，以及 LEARNING_STATE 最新 2026 路由。采用 using-agent-skills 的范围与核验约束；本轮不是代码实现。

只补 BJT **2026-05-26 ～ 2026-05-26**，保护原小时窗 `2026-05-26T09:00:00+08:00 ～ 2026-05-27T09:00:00+08:00`、94 条原候选完整行（93 arXiv + MiniMax）、原日期/评分、连续旧 §4。原 61 整合/33 已有覆盖及 2026-09-16 R3 的有限写后 PASS 复用，不复活旧 633/64 库存或无差别重读原候选。旧完成不是本次补查完成。

实际开始状态：新增候选0；新增证据/Books判断/来源自然日覆盖/六节DAY/保存态FINAL均未完成。共享Books、LS、索引、合同、脚本均未改；不stage/commit/push。原 MiniMax 同 URL 同事件只去重，不因当前可见日期重搬归属。

## A2 正在执行的原始入口与局部发现

执行时间：2026-10-21（Asia/Shanghai）。网页实时取回，不继承其他日来源成功。

- OpenAI Research 首屏到 2026-09，不能证明 May26 无命中，继续官方 RSS/窗口定点恢复。
- Anthropic Research 主页当前203条首屏仅到Sep4，转实际链接的 team/alignment、team/frontier-red-team、team/economics、team/interpretability、team/societal-impacts及 Engineering。Engineering首屏已跨 May26（May25 *How we contain Claude across products* / Apr23）；Interpretability跨界 Jul6 / May7；Alignment跨界 Jul8 / May8；Societal跨界 Jun12 / Apr30。仍未将此扩大为全站无遗漏。
- Google Research官方月目录 `https://research.google/blog/2026/05/` 实际四条：May28、May27、May19、May1，无May26；DeepMind仍待。
- arXiv `.../list/cs.CL/2605` 为错误历史参数，不能当零命中；`.../list/cs.CL/2026-05?skip=0&show=50` 成功，2845个月级标题仅作查漏线索，不是全量关闭队列。Availability官方2026假期不含May25，不以美国节日猜测零公告。
- 搜索发现Anthropic RSP v3.3（May26有效，修订阈值与off-cycle更新）、February Risk Report May26纠错；已开官方RSP changelog，正读精确增量，未提前授予候选或日期通过。

## A3 首批准入与代表排除校准包（待root实际独核）

完整官方核心说明已读，不以机构/章节关键词准入。

1. **Anthropic RSP v3.3，2026-05-26**：[官方版本/有效日及变更说明](https://www.anthropic.com/responsible-scaling-policy)，[精确v3.3](https://www-cdn.anthropic.com/files/4zrzovbb/website/c11e84981d0a7281a1b229f3fa6af0da66eaf43f.pdf)，[官方redline](https://www-cdn.anthropic.com/files/4zrzovbb/website/dd0ec579bee2cd144069c478ede3e35ea080ad02.pdf)。原来以最近周期Risk Report为比较基线 → §3.1（PDF p10）改为所有已有公开风险分析的模型基线，并明确内部模型风险增量触发30日内发布 → 需要区分发布节奏、已公开证据集合及内部部署事件，不因版本号就重评全政策。拟2+2+2=6，因实际安全/发布约束变化读到深入；只采用更新触发规则，不采用完整CB阈值细节、不宣称已实施或有效。原件已保存 `sup_rsp_v3.3.pdf`。Books判断待具体owner比较，可能仅报告。
2. **Anthropic February Risk Report May26纠错，2026-05-26**：[更新版105页PDF](https://www-cdn.anthropic.com/097c63b5fe7dd8b14866e1f15bb1910ec713658a.pdf)，保存 `sup_risk_report_feb_updated_20260526.pdf`。旧摘要把16名参与者当作全部回答且遗漏scaffold限定 → p105更正其中1人未直接回答，恢复“modest”条件；§3.4/p61与p31援引同步 → 能力rule-out证据必须保留有效回答分母、问题阈值与脚手架预算，不能从未回答或受限scaffold推论模型普遍无能力。拟2+2+3=7，实际纠错深入，但只核受影响调查/引用/限制，不重新审全105页，不把更正写成能力新实验。调查为内部主观样本，部分使用非final checkpoint，不能给替代研究员的统计保证。Books比较待。

代表排除/日期恢复：

- [How we contain Claude across products](https://www.anthropic.com/engineering/how-we-contain-claude-across-products)：Engineering实际可见日期May25，窗外线索，不搬到本补窗；未宣称本窗已审重复。
- Google Research May27 *Private analytics via zero-trust aggregation*：官方月目录日期May27，窗外，不在本日筛选/评分。
- Anthropic RSP May26修改的CB专业操作阈值仅为核对同一release真实变化的背景，不引入AI-for-Science研究路线，且不为整份政策内所有内容再造候选。
- 纯产品/活动目录搜索命中（May26销售Cowork webinar、OpenAI Forum活动）无新增模型/系统机制或评价证据，范围/贡献不足，不进入候选；不为其日期追时。

## A4 原日期区间反例与本轮采用边界

实时DataCite精确DOI原字段显示 `2605.24798` state=findable、registered=`2026-05-26T03:23:33.000Z`，唯一v1 Submitted=`2026-05-24T01:01:43Z`；与当前官方最终ID只在announcement分配及公告日程合证落在May26 BJT。另`2605.26116` registered=`2026-05-26T03:55:05Z`、v1 Submitted=`2026-05-25T17:59:53Z`，同样约束在May26。原§1的“24798..26116为May27公告批次”不能用作本补窗真实日期边界或无遗漏证据。

按用户授权仍保留旧94完整行/日期/评分，不展开94项重定时；同精确事件已在旧94的只去重。新增拟入选逐项独立核公开日期，不以ID区间单独定日期。早于本日的宽标题线索只作窗口路由，不转成全部身份关闭队列。

## A5 arXiv首批准入（完整题摘已读，必要Source未完）

本批五篇当前abs均只有唯一v1，当前官方页未显示撤回/勘误。精确v1题摘/HTML已打开；精确DOI原件分别保存 `sup_datacite_2605.<id>.json`，v1提交均在Friday May22 18:00Z之后、Monday May25 18:00Z之前；findable registered均在May26 BJT内，结合官方2026公告规则限定最早May26 08:00 BJT与最晚登记，整区间同日。登记不冒充实际发布时间，也不声称无更早全球正文。

| 身份/精确v1 | 准入链与拟分 | 后续必要证据 |
| --- | --- | --- |
| [24173 Infilling Extraction](https://arxiv.org/html/2605.24173v1) | AR前缀探测不覆盖DLM任意位置denoise → 以任意二元mask统一抽取协议，发现mask几何改变泄漏及SFT未消除 → 需改变DLM隐私审计面；2+2+3=7 | §3任意mask/威胁面、§4.1–4.4训练与scale对照、4.7 SFT、A硬件/预算；不把最高倍率当普遍风险 |
| [24218 QUEST](https://arxiv.org/html/2605.24218v1) | deep-research可验证训练数据难跨任务统一 → rubric树合成任务/奖励并接midtraining/SFT/RL和上下文管理 → 比较训练任务覆盖与reward有效性；2+2+2=6 | 方法、八任务评价与关键消融、合成数据及预算；Work in Progress，不凭8K任务/排行保真 |
| [24579 WhenLoss](https://arxiv.org/html/2605.24579v1) | 固定预算端到端失分混淆丢写和漏取 → 固定reader下TFC/OE/CSM/RM四条件分解，并只改变write端EPC → 先定位write/retrieval瓶颈再投资检索；2+2+3=7 | §3指标非因果注意、§5固定budget/reader、§6.4人为降级、6.7成本匹配及7边界 |
| [24697 TraceLock](https://arxiv.org/html/2605.24697v1) | confidence承诺token难跨step/窗口设置复用 → 从完整trace未来稳定性产生标签训练冻结backbone的commit controller → 比较可学习commit轨迹与置信度规则；2+2+2=6 | §3标签只在训练用future、4对照/配置/消融、D实际wallclock与limitations；不把步数减少当吞吐提升 |
| [24793 CoSpec](https://arxiv.org/html/2605.24793v1) | target在每token都正确不成立 → RL仲裁允许mismatch选draft、改变目标输出分布换取任务效用 → 必须区分lossless SPD与utility偏置多模型推理；3+2+3=8 | §3随机/greedy语义、§4对照/仲裁消融、F吞吐/overhead、G限制；不声称保原target分布 |

入口有限恢复事实：主题API查询12分类+Submitted May22 18Z～May25 18Z的完整响应应1106项，但45s超时，仅保存507个完整entry及末尾截断；不能算完整覆盖。它只提供本补窗可能相关题摘/身份线索，不把1106或507当待逐项关闭队列。cs.CL月标题页成功；cs.LG/CV首2000未跨到目标ID，不能当补检完成。已识别缺口，后续改窄原始入口/分页。

## A6 精确去重纠正与首个Books差额/PRE（尚未获写权）

从现有Books的精确family marker定点回查相邻05-26原候选表，确认A5中的 **24579、24697、24793 同一v1已有效审阅**，现有Ch77“用干预矩阵定位写入、检索与阅读失败”、Ch24“Commitment Policy可以从未来稳定轨迹学习”、Ch48“当Draft可能优于Target，系统进入效用仲裁分支”实际承载同命题。三项转为同事件去重/有效层复用，不作为05-27新增，不重评分、不新写Books；A5准入理由只是本轮曾考虑的校准依据，不能计新增。24326/24425/24432/24517/24578/24786等亦命中05-26原表，后续只作精确事件去重，不扩扫重跑相邻日。24173、24218未命中该原表。

Anthropic两项已由root实际核必要域；RSP只采用当前§3.1，内部30日从**确定风险显著超出**起算，不从部署时刻起算。本作者已读官方redline的对应§3.1，旧比较基线可保为作者观察；reader未独核的红线比较不冒充双人通过。February Risk Report按重要纠错事件，不重复全家族评分。

已实际加载PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、ROADMAP与本日最新路由，读取Ch66当前能力/response-rate/发布时效论证，及邻章Ch65/67开篇交接；为安全owner比较亦读Ch71/73开篇。不写共享Books，等待root窄位授权。

- **RSP v3.3：拟仅报告。** 本次可确认的是特定机构有效政策的触发条件，不是已经验证的安全工程实现或跨机构普遍机制。Ch66“能力结果还必须绑定时间”已拥有release/elicitation/tool scaffold与证据版本有效性；Ch73 Evolution proof obligation拥有线上证据回到新评估/变更的控制闭环。无需将版本化30日期限复制成长久规则；报告保留当前§3.1语义及机构自我判断边界。
- **February Risk纠错：拟整合最小差额，Owner `PLATFORM-EVALUATION-SYSTEM` / Ch66。** 当前“Observed Capability与Elicitation Ceiling必须分开”解释低分与能力上界，Response Rate小节针对生成响应人口；均没有明确专家调查的参与者/有效回答分母与问题限定被删后的rule-out误读。不是添加机构能力结论，而是收束证据对象。

拟窄位：Ch66小节 `### Observed Capability 与 Elicitation Ceiling 必须分开` 第一个正文段之后、现有“解释低分之前，还应把响应位置的集中与题目内容敏感性分开检查”之前。前锚段原文：

> 固定 prompt 下的最高分最容易比较，但弱 supervisor 无法可靠验证全部输出时，低分可能来自能力不足、策略性隐藏或 elicitation 失败。Evaluation 需要把模型当前自然行为、给定监督预算可诱发的最好行为，以及 supervisor/evaluator 的识别上限拆成不同证据对象。

逐字拟段（PRE，尚未写入）：

能力排除若依赖专家调查，参与人数不能代替有效回答数，未直接回答必须单列；问题中的工具与脚手架改进幅度、时间范围和概率门槛也属于测量对象，不能压缩成“无人认为模型有能力”。[一处公开更正](https://www-cdn.anthropic.com/097c63b5fe7dd8b14866e1f15bb1910ec713658a.pdf)恢复了“有限脚手架改进”的条件，并说明16名参与者中1人未直接回答，部分使用还不来自最终checkpoint。它改变证据可如何被引用，不是新能力实验：内部主观判断只支持该样本、问题和配置下的意见，不能由零支持票或缺答推出模型的普遍能力上界。保存原题、回答人口和checkpoint增加审计成本；条件缺失时保留Unknown与独立能力测量，不把缺答填成否定。<!-- source-family:SF-2026-ANTHROPIC-RISK-REPORT-20260526-CORRECTION -->

对应章末Review note拟一条：`SF-2026-ANTHROPIC-RISK-REPORT-20260526-CORRECTION`，精确2026-05-26修订PDF p105 changelog、§3.4/p61及p31援引；只采用调查分母/条件更正，不采用整份报告的安全结论；未重现调查，无跨机构/当前能力保证。待root PRE/实际POST后再宣称整合。

## A7 24173必要Source与Ch72最小差额/PRE

作者实际读 exact-v1 §3定义/五mask/指标/诱导记忆，§4.1–4.4/T1–4对照、§4.7 SFT、§5限制及A硬件；root必要Source独核通过。采用mask geometry属于隐私审计面，不采用DLM架构普遍更不私有：训练语料不可得，以FT/LoRA/SFT诱导记忆；LLaDA-8B、Dream-7B及LLaMA2-7B只是scale/tuning matched，不能识别架构唯一因果。普通五mask固定揭示token预算，targeted只maskPII、给全周边，是另一个最强对手，非等量预算比较。ASR=逐字恢复，TER=masked token匹配比例，entity recall另列，不能混叫泄漏成功率。SFT仅LLaDA该流程部分PII持续，不证明所有post-training无效。训练4×H100-80GB，评价4×L40S；未核实现/复现，不采用生产性能数字。

具体owner已读Ch72开篇、memorization/adaptive-extraction段完整两侧和Ch71/73交接；已有论证区分影响/抽取与攻击预算，但未解释双向denoise允许的mask几何怎样改变受测攻击面。因此拟 `PLATFORM-SECURITY` 整合一段，不复述Ch24生成范式。

唯一窄位请求：Ch72 `<!-- source-family:SF-2026-ARXIV-2608-27782 -->` 之后、现有“视觉隐私审计还要分开公开可见性”之前。

逐字PRE（未获权，不写）：

审计接口还要覆盖模型实际允许的条件化方式。对只能从左到右续写的模型，前缀抽取是合理基线；支持任意位置去噪补全的模型则应把可见token预算与mask几何同时固定，再比较前缀、后缀、两端和分散上下文。只遮住敏感实体、公开全部周边文字的targeted infilling属于更强的信息权限，必须与普通等预算探测分账；逐字恢复、局部token匹配与实体召回也不能合成一个泄漏率。[受限DLM实验](https://arxiv.org/html/2605.24173v1)通过微调诱导记忆，支持“prefix单测可能漏掉泄漏渠道”，不证明真实预训练语料泄漏率或架构唯一因果。额外mask、解码配置和训练后复测增加成本；没有相应接口时保留可执行的前缀基线并声明未覆盖面，不能从一次低抽取率或后续SFT签发隐私保证。<!-- source-family:SF-2026-ARXIV-2605-24173 -->

本人Review note拟：exact-v1 §3、§4.1–4.4/4.7、§5/A；仅mask几何/指标/信息权限分账，保诱导微调与非架构因果、单流程SFT边界；未复现，root必要Source/PRE及真实POST分层记录。

### A7修正：具体已有覆盖，不写上述PRE

root指出并由作者实际补读Ch72完整直接后续段：当前“同一组已训练参数还可能因采样路径不同而暴露出不同的逐字恢复率”已明确冻结**初始mask/context、reveal order、每轮共同恢复位置集合、总查询预算**；下一段明确DLM恢复率不是全部训练数据泄漏率、模型曝光/训练预算差异不识别生成范式因果。上方Post-training accessibility段也已把SFT/refusal、targeted/free-recall和pre/post audit分开。因本次经证据收窄的长期命题就是mask与信息权限属于audit identity，并非新的安全机制，**24173最终拟已有覆盖：`PLATFORM-SECURITY` Ch72上述具体两段及Post-training段**。A7前述gap判断不成立，PRE撤回、未写任何Ch72；不因证据成本改分，7分深入及完整Source结果保留。不需要用另一份DLM实验制造重复正文。

## A8 来源恢复局部事实（尚非DAY）

- Hunyuan当日bundle恢复真实host `https://api.hunyuan.tencent.com`、POST `/api/blog/publicList`，`pageNum=1,pageSize=1000,renderType=0`，EN9条、ZH11条，均全部返回（totalNum对应）。EN最近跨界Jul6/Apr30，ZHJul6/May21；raw保存在sup_hunyuan_publiclist_p1.json及sup_hunyuan_publiclist_zh_p1.json。注意Hy3 preview显示Apr23但publicAt为July，不能拿displayPublishTime冒充首次公开；与本窗无May26项，不扩附件。
- Seed当日main恢复 `/api/get_article_list_v2`，Publication=1、Blog=2；**实际必需header `x-tt-locale: US`**，不是query `locale`。Publication年2026/page_token0、20/count20/order_desc=true两页已保存；page0两条标May26（1617 MoA→2605.26647；1615 Scale Vectors→2605.26895），page20首May16，已跨窗口停止。两个ArticleMeta当前UpdateTime在July1，官方catalog日期与arXiv首次正文公开需分层，不把May26目录日直接当完整论文首次公开；正定点核必要日期/事件。其余窗外标题只路由，不逐项筛全部年表。Blog仍待独立跨界页。

## A9 QUEST必要Source与具体已有覆盖

作者实际读v1 §2 rubric-tree/query/verification链、§4.3–4.4 session/rollout与reward、§6.1(T1–2)/6.3训练消融、§7失败；root已实际独核对应必要域通过。保留：8K仅SFT/RL任务，MT另有百万级样本且teacher/tool费用未消失；citation-supported分母排unknown，不等所有陈述事实正确。SFT会过拟合允许工具集合；RL对部分reasoning任务反退；组合阶段消融不单独识别rubric树的因果，不采用通用冠军或small-model普遍等效结论。未核代码或复现。

拟已有覆盖 `TRAIN-DATA` / Ch27：已实际读“**Synthetic data：从先生成再打分到Specification Compilation**”前后衔接，以及“**从样本数量到Coverage Contract：Curriculum必须同时管理内容、能力与环境**”完整论证。正文已明确任务合成/组合→独立verifier/rubric execution→accepted training row与lineage，并把rubric formation、criterion execution、final-answer correctness分离，且保同源blind spot和held-out边界。QUEST统一树是这些机制的具体实例，当前证据未支持更强普遍因果；因此不为paper/benchmark配置另追加正文。其session去重/上下文实现不是本项准入拟采用命题，不为制造新gap扩整份附录。

February correction已按root授权真实写Ch66一段+本人note，root R4实际POST通过且窄位已释放；本人note只行政同步既成事实，不重读有效Source/POST。本轮现有真实Books改动1项，仍未日级DAY/FINAL。

## A10 第二批完整题摘贡献筛选（尚未Evidence完成）

下面题摘来自本轮实际恢复的完整Atom entry，后续采用必须回精确v1。既有原94与相邻日原表同v1先去重；此表不宣称余下宽列表全部关闭，也不把abstract准入计深入完成。评分只针对具体增量，不借用通用原则加分。

| arXiv身份 | 原约束 → 本文增量 → 设计选择 | 拟分/投入 |
| --- | --- | --- |
| 2605.24110 EvoCode-Bench | 单轮参考起态掩盖累积回归 → 持久workspace/累计测试与reference-completed round分测 → 区分单步能力与长期维护 | 2+2+2=6 标准 |
| 2605.24117 SkillEvolBench | replay改善不证明形成skill → acquisition后冻结部署、context-shift/shortcut/composition与raw-trajectory对照 → 判断抽象是否丢失可用线索 | 2+2+2=6 标准 |
| 2605.24140 HyperGuide | 搜索/中间value打分付分支费 → 双曲state encoder预测转移方向、作为virtual token单轨生成 → 比较训练指导成本与运行搜索成本 | 2+2+2=6 标准；精确v1待 |
| 2605.24144 EVA | VQ仍有GEMV利用率与bank冲突 → input-codebook先点积、结构化lookup → 比较预计算/存储与解码执行计划 | 2+2+2=6 标准 |
| 2605.24154 Palette | 单一refusal策略难分授权域 → 独立域轻适配并参数组合 → 验证局部放宽与域外安全的冲突 | 2+2+2=6 安全必要域深入；精确v1待 |
| 2605.24168 Context Sparsity | dense decode成本是否必要未分模型/任务 → 20模型五family极端稀疏与kernel对照 → 重新检查质量/稀疏/实际硬件可行边界 | 2+2+3=7 深入，不采“密集不合理”的普遍断言 |
| 2605.24171 PromptAudit | prompt方案比较混入模型/解析差异 → 固定数据decode/parser单改prompt，揭示recall/abstention tradeoff → evaluator保prompt条件 | 2+1+2=5 标准 |
| 2605.24183 AvalancheBench | workflow执行不证明解释数据 → 已知latent world生成observations评分恢复结构并追错误传播 → 区分pipeline成功与分析正确 | 2+2+2=6 标准 |
| 2605.24197 Agentic Misalignment | workflow proxy utility可能不同于目标 → Bayesian失配分析与trajectory外部evidence attribution → 检查所谓posterior collapse假设/可识别性 | 2+2+2=6 标准，精确v1待；不采可靠性保证 |
| 2605.24202 Multi-Agent RL | 共享policy被当统一稳定解 → topology/role梯度压力解释独立terminal cliff与共享role capture → 按workflow/task/scale选择参数共享 | 2+2+3=7 深入，精确v1待 |
| 2605.24203 Afford-VLA | 外部视觉规划弱耦合动作 → AFF token生成mask并以紧凑affordance embedding条件化action联合训练 → 比较空间接口与动作训练耦合 | 2+2+2=6 标准 |
| 2605.24213 Evaluation Harnesses | 评价错误常被只归metric → 57 harness/16560 issues五阶段root-cause分解 → 将specification/provisioning/assessment责任分开 | 2+1+2=5 标准 |
| 2605.24216 Agent-ToM | monitor每条轨迹重来、intent不显式 → belief/intent假设+verify/refine及跨episode guardrail memory → 比较学习monitor与静态ensemble | 2+2+2=6 安全必要域深入 |
| 2605.24217 Measurement Bias | client排队可伪装server退化 → client M/G/1论证、多进程与时延指标分解 → 先验证压测器再归因engine | 2+2+3=7 深入，精确v1待 |
| 2605.24219 Trajel | final-only漏中间幻觉 → 多种step-level标签与共现/细类型误检 → 评价层级不能被binary平均替代 | 2+2+2=6 标准，精确v1待 |
| 2605.24220 Polar | harness移植丢token训练信号 → 代理LLM调用重建token-faithful轨迹/异步独立训练消费 → 界定重建正确性与吞吐收益 | 2+2+3=7 深入 |
| 2605.24229 Constitution Audit | 静态spec不能证明多轮遵守 → atomic tenet+多轮adversarial及浅失败补检 → 比较spec coverage与公开system-card边界 | 2+2+2=6 安全必要域深入，不把世代差因果归spec训练 |
| 2605.24239 Apple PCC Analysis | 公开规范与闭源binary可能不一致 → 逆向实际接口、独立模型query → 区分规范privacy主张与可观察实现/能力 | 2+2+2=6 安全必要域深入 |
| 2605.24248 Attested MCP | MCP自报toollist无server信任范围 → 离线签名clearance+pin根+默认deny pertool+强制模式/日志 → admission不等全tool授权 | 2+2+3=7 深入，精确v1待 |
| 2605.24259 Resident KV Claims | write no-admit未保resident免active eviction → materialization/lifecycle/feasibility及blocking-claim归因 → 把硬保护拒绝变成调度可见契约 | 2+2+3=7 深入，不采生产加速 |

本轮代表性明确排除：完整题摘 `2605.24484 SPACE` 是车辆路径求解器的对称/非对称VRP表示改进，无foundation/LLM机制关系；`2605.24395 AvAtar` 是OT主动监督在多网络/点云对齐的通用应用，尚无支持本项目模型/系统主线的具体约束链，不能只因“alignment”就映射RLHF/多模态；两项不评分，不为无关日期追索。`2605.24134 ProofAgent Harness` 尚未关闭：题摘只列既有多轮/多juror/trace步骤与笼统失败，决定新增机制的事实不清，后续只定点读方法/对照后准入或具体排除，不把它当已采用候选。

### A10精确v1恢复及局部修正

root已实际读A10完整题摘，要求当前v5/v2不能冒充v1。作者已逐篇恢复并保存 `sup_abs_<id>v1.html`：24140、24154、24197、24202、24217、24219、24248，均完整题摘实际读回；官方当前history信号保留，不做全部版本diff。

**24140存在实质摘要差异**：v1不是当前v5的“minimum-cost direction virtual-token单轨guidance”表述。v1实际是轻量head将hidden映射双曲空间，再对自己的推理尝试交互微调LoRA以使用注入信号，利用距原点/角度的几何表示。A10该行的具体机制撤回，准入收窄为“树搜索成本→几何progress信号与交互适配→比较单轨推理的训练/elicitation取舍”，暂保2+2+2=6，必须按v1必要方法与局部对照审，不能采v5新增方向预测器。其余六篇v1完整题摘与A10拟命题一致；并不证明主张成立，仍待必要Source与精确日期。

### A10二十项日期原件已恢复（待root日期独核）

全部精确DOI `sup_datacite_<id>.json` 原件已存，身份/登记方 `arxiv.content`、state=findable、唯一v1 Submitted核对；提交均为2026-05-22 18:17:28Z～22:25:31Z，登记2026-05-26 03:07:09Z～03:10:41Z。Friday 14:00 EDT之后提交的最早scheduled公告为Monday May25 20:00 EDT（May26 08:00 BJT）；官方2026 deferred-mailing名单没有May25，且即使审核延期也不可能早于该界。最终ID/DOI公告时分配与findable registered给最晚界，各条完整区间均落May26 BJT。没有用created代替registered，登记不是实际公开时刻；v1官方API published与已恢复abs历史交叉核身份，不以ID区间给未核材料定时。后续v2/v5不改本次采用v1，当前事件页撤回/实质更正信号仍须局部处理，不以“同摘要”豁免。

## A11 有效层续接与具体Books比较

root R10已逐项实核A10二十项精确DOI/client/state/registered与官方published（七份精确v1另核），上述组合日期通过；不是待日期项。新Source普通待办继续，不因成本改判或隔离。

- **24220 Polar，拟已有覆盖 `TRAIN-GRPO` / Ch33。** 已实际完整读取当前“Agent RL还要求environment failure与policy staleness使用不同终态”链及“On-policy来源不等于Conditioning State一致”两侧：前者保存gateway actual token IDs/loss mask、generating policy version、environment outcome/reward completeness并分COMPLETE/ENV_FAILED/CANCELLED/STALE；后者保存positions、causal mask、memory/environment snapshot，要求packed reconstruction等价。这已承载经Source限定的token-faithful重建与异步消费界；复制raw tokens/loss mask不自动证明后续conditioning/logprob一致。root实际必要v1 §3、§4.1/A2通过；短三step 5.39倍、未披露拓扑与per-request reward hacking保留在报告，不采普遍吞吐。拟NC，不写正文，原7分不变。
- **24259 Resident KV Claims，拟已有覆盖 `INFER-KV-CACHE` / Ch45。** 实际完整读“Future Reuse Intent需要变成可验证的Resident Claim”三段及直接前后：已精确采用本v1 §3/5，包含future intent→materialization predicate/lifecycle/active-resident feasibility/claim telemetry、runtime实际blocks为真值、失败recompute/cold-tier/nonresident与陈旧claim/registry成本。该同事件有效论证不因补窗重写；root必要§2–5/7/9/T2–5/13–14通过。硬保护可拒active，patch-level vLLM PoC不授生产加速/跨runtime。拟NC，原7分不变。
- **24110 EvoCodeBench标准必要Source**：作者已读v1 §3.2–3.4、§4.1–4.2及AppA；root同域独核通过。26任务/227轮、5–15轮，MT持久container/session与累计测试，SR从reference-completed状态起步；MT@4按task归一且4attempt，SR按round且1attempt，差值不作纯因果。fail-stop不测恢复；小规模/可自动测试任务边界保留。Books具体差额待。
- **24117 SkillEvolBench标准必要Source**：作者实际读v1 §4、§5.1–5.3/5.6；root完整§4/5与容量费用反侧通过。Acquisition只可用本family轨迹/verifier，evaluation冻结库只读；raw-trajectory/curated对照，CSSR/ARSR/composition分开。Replay原acquisition不是transfer，较大库/频繁写库不保证泛化，token费用常升、model/task切片收益混合。Books具体差额待。
- **24144 EVA标准必要Source**：作者实际读v1 §III完整机制、VI方法与讨论，root III/V/VI表3–9和反侧通过。input×codebook先算后OC lookup/reduction，不把SIMD MAC数减少直接叫净收益；28nm/500MHz Verilog综合＋模拟器非硅片/GPU实测，作者E2E仅首Transformer block。batch>32时VQ精度/能耗优势可反转，保量化质量损失/lookup bank代价。Books具体差额待。
- **24217/24202/24248** root必要Source已通过，尚待具体owner。24217仅client queue/arrival-processing/offered-achieved分测；M/G/1是假设，simulator无模型计算非无网络开销，多进程非纯engine，NTPOT非工作量等价。24202只Qwen3 0.6/1.7/4B LoRA、单seed/cell、outcome reward/固定steps；IP每role type一个adapter非每实例，角色贡献共享，SP可role capture；诊断不识别唯一因果、非等总token/GPU成本。24248 **exact-v1 HTML masthead August24与身份冲突**，不采用该HTML；root实际打开20页官方exact-v1 PDF首页May26并读§3–7/10，采用pinned authority、offline clearance及per-tool default-deny有限协议，warn-only非硬deny、bridge fastpath另有本地信任输入；48hermetic/live fuzz/Gmail人口分开，不认证恶意已准入server/内容/多租户，不把签名哈希链当完整审计/防截尾/FIPS认证，上游MCP未接受。

新增标准Source推进中：作者已实际读24183 exact-v1 §2–5（含T2/三次trial/限制）。Known latent Z先于observations/rubric，结构conformance与LLM surface realization分开；pipeline完成不保证恢复Z，上游segment错可传播后续rubric。实验仅一synthetic world/CoCo v1.0.80+Opus4.7，LOTUS禁rankoperator与AISQL预算并不完全等价，同backbone judge未有人审全rubric/多judge稳健性，不能采真实企业准确率或编译/交互普遍排序。仅采用评价构造和错误传播诊断，非电商应用。24171已读§3.1–3.7、§4.1–4.6/5.1与5.6必要域：固定parser/数据/decode下单模板prompt干预；CVE提交before/after非每snippet真实漏洞标签，一模板/固定seed/temperature0.2无重复不确定性；fullparser lexical fallback、abstention与recall分账，不能以threshold类比识别内部reasoning因果或宣称CoT/投票普遍优劣。24213已读§3/4/7/8，仍补§5/6具体根因证据，未宣称完成。

### A11后续实际核验同步

root R11已实际读Ch33、Ch45承载正文/直接交接，24220/24259两个具体NC通过；24217亦实际读Ch66“Benchmark Client也是Measurement Instrument”两段/邻接、原exact-v1 marker，NC通过。三项不写重复正文。作者已补读24213 §5/6必要根因定义与stage人口，root R12 24171/24183/24213/24219标准Source通过：24171 accuracy排invalid而recall计UnFN、effectiveF1乘coverage，不是部署费用；24219 n=213 flags是终态posthoc，不是online kill-switch，人/LLM agreement不是人际一致性。尚待其具体Books判断，不将Source通过计作已日级验收。

## A12 HyperGuide v1必要Source与具体PRE（不写，待root）

**局部纠正A10文字**：v1自身已有virtual token（head→up-projector→residual stream额外位置），因此不能把所有virtual-token叙述归给v5。只排除当前v5的minimum-cost transition-direction predictor，不排除v1已有连续引导位置。作者实际读v1 §3全机制、§4.1–4.4/T1–4、AppE。Head以oracle distance-to-solution的radial ranking和tree-distance metric训练；冻结base/head后，DAgger在自身rollout states以tree oracle胜利operation训练LoRA/up-projector；非可枚举MATH以Monte Carlo成功率/共享前缀近似，不是开放任务完整树距。所谓OOD仍重训每dataset head，不能称零训练泛化；T3 Mistral MATH51低于OVM53，非普遍支配。Generated-token横轴不结算连续位置/全部forward，单轨不免枚举/rollout/DAgger和head适配，不采用零额外position/生产速度/通用scale保证。

当前唯一owner `AGENT-PLANNING` Ch79 已实际读“Search-based Planning的边界”及训练期teacher→runtime controller完整链（并读Ch78/80交接）。现有正文拥有离线search teacher蒸馏直接plan，以及canonical state/backtracking policy；尚未承载“每步连续progress信号必须在自身访问state上训练其消费者，而非只gold-state适配”的具体接口。拟在“Search还要区分训练期teacher与运行期controller”段后、现有Backtracking policy semantic block前插单段，前后原文不动。

逐字PRE：

训练期搜索还可以不只输出一条文本计划，而把树上的局部进展变成运行时连续条件：先让小head把当前hidden映射到几何空间，以到解的距离和状态间树距监督；再把该向量投影为每步的额外输入位置，让策略学习怎样消费它。消费者必须覆盖自己实际会访问的状态：只在gold路径上训练，部署走错后便可能遇到从未学过的引导条件；可用自身rollout加可靠oracle标注迭代适配，而不是把一个较好的value表示当作行动能力。[受限树推理对照](https://arxiv.org/html/2605.24140v1)支持这条表示—消费者分工，不证明双曲距离是真实因果进展；不可枚举任务只用采样近似，跨任务仍需新head，局部结果也有反退。它以离线搜索、标注、适配及每步条件位置换少分支，短输出不等完整费用更低；树结构、oracle或净收益不可靠时，保留普通直接计划、显式搜索和独立终局验证。<!-- source-family:SF-2026-ARXIV-2605-24140 -->

拟本人note：exact-v1 §3/§4.1–4.4/T1–4/AppE；采用几何signal/consumer自身state适配边界，非v5direction predictor；树oracle/MC、per-datasethead、Mistral MATH反退与全费保留。未核实现/复现；需root必要Source/具体PRE通过及唯一窄位后才写，实际POST另核。

新增24203标准必要Source作者已实际读§3–4/T1–3、AppB/C/F.2：Qwen3-VL4B+GR00T式FM头，AFF queries预测2Dmask，Top16 patch pooling进action condition；straight-through只训练用，部署hardtopK。离线RAGNet伪mask按episode/frame/view与action对齐，warmup4K再joint，GT不在joint pooling用。保伪mask偏差、2D非3D、有限本体/任务，SimplerEnv stack14.6低于多数对照，外部affordance96.5已改善baseline95.4，完整97.4不识别所有因果。训练4/8H200、真机A6000/两任务各20trial且reset未计费，不采通用实时/物理安全。Books具体差额待。

A12执行同步：root必要Source/当前owner完整交接/逐字PRE通过并授唯一窄位；作者已真实保存Ch79单段与本人Review note，实际完整读回及限定diff-check通过，已请求唯一实际POST，未预支通过或日级完成。

## A13 后续有界线索的完整题摘准入（日期/精确版本/Source尚待）

以下仅为已实际读到的相关线索贡献筛选，不把截断Atom507项或月列表变成全关闭队列；继续围绕具体机制而非分类/关键词。精确v1缺失者必须先修复版本，未通过日期前不进入确定当窗候选表。

| 身份 | 原约束 → 摘要实际增量 → 拟核验选择 | 拟分/必要投入 |
| --- | --- | --- |
| 2605.24266 SteER | 一次scope后长自主运行不能处理意图变化 → cost-benefit判断中途询问与继续、diversity计划及live persona → 比较交互打断费与alignment/coverage；不是只改研究流程术语 | 2+2+2=6 标准，核询问utility/对照和persona更新依据 |
| 2605.24267 DRInQ | 语言流畅不等语境推断 → 固定question表面只变context、对照生成与推断不对称 → 将context支持与模型先验分开 | 2+1+2=5 标准，不采通用social能力排序 |
| 2605.24270 Mixtral routing safety | usage频率不等安全贡献 → activation与router-gradient双信号及expert suppression → 检验所谓单一安全expert可编辑性的边界 | 2+1+2=5 安全必要域深入，局部100prompt不授通用安全机制 |
| 2605.24279 ContextEcho | 短对话稳定不代表长tool/session → snapshot-fork probe不扰main、judge-free及judge surfaces、compaction/anchor对照 → persona状态须按runtime上下文测 | 2+2+2=6，当前v2须先恢复v1完整题摘；不把identity陈述当意识 |
| 2605.24286 Faithfulness as Information Flow | CoT流畅仍可能prompt→answer shortcut → mediated/direct路径的sufficiency/completeness/necessity诊断与训练期mask/gradient干预 → 比较可监测性与训练信息流 | 2+2+3=7 深入，核低entropy KL反例、实际指标/干预控制与任务费 |
| 2605.24292 TUBE | DLM ELBO只下界不知exact likelihood在哪 → 可MC无偏估计的variational upper bound与ARM对照 → 用上下界夹住密度评价而非混比ELBO | 2+2+3=7 深入，核界的假设/证明/估计方差与精确AR可比条件 |
| 2605.24299 Individuated Metacognition | aggregatecalibration可能只共享题难度 → confidence矩阵factor与pairwise/base-rate控制 → routing/abstention不能从自信推模型相对优势 | 2+2+3=7 深入，核tetrachoric/去一致items/数学解题confound，不采绝无内省本体结论 |
| 2605.24354 SparseWorld | dense future场景表示冗余 → joint temporal/spatial attention预测map/agent latent instances并条件化planner → 比较稀疏预测状态与下游闭环质量/成本 | 2+2+2=6，当前v2需精确v1；不以nuScenes数字或驾驶应用本身准入 |
| 2605.24364 MCBoost | aggregatecalibration不保证slice与迁移 → cumulative audit span上的Bregman projection、风险/校准/早停条件与covariate-shift适用界 → 限定postprocess所能保证的函数域 | 2+2+2=6 标准，必要理论假设深入，不泛收一般公平应用 |
| 2605.24530 Unveil | 纯文本parser漏layout，纯视觉弱细字 → text+visual teacher融合再蒸馏visual-only学生 → 比较读时parse依赖与训练时语义迁移 | 2+2+2=6 标准，核teacher/student对照、parser费用与反退，不只收retrieval排行 |
| 2605.24584 LAPLEX | 可学习dense投影通常付存储或低秩近似 → implicit learnable Laplace-kernel exact full-rank operator与FFT-like执行 → 比较结构表达族/可学习几何与实际运算存储 | 2+2+2=6 标准，核exactness/结构限制/实现规模，不由10^9维或full-rank推任意矩阵能力 |

## A14 来源恢复增量（尚非完整Coverage）

DeepMind原分页参数无效后，由官方链接实际恢复 `/blog/page/2/` 与 `/blog/page/3/`，原件已保存。p2 June段后是May20 Singapore partnership、May19 Gemini3.5/Omni/Antigravity，p3 May→April跨界；只就当前可见历史news slice无May26项，不声称所有research历史。GoogleResearch May archive四条May28/27/19/1已实际跨界。

Meta官方搜索p2及Publications恢复May26“Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images”完整题摘，主张是fMRI/MEG中激活与梯度的脑层次对应不同，未提供改变foundation模型学习/系统的新增机制；按本轮主线范围排除，不评分，不能称机构零公开。表外[May26 SilverTorch官方全文](https://engineering.fb.com/2026/05/26/ml-applications/silvertorch-index-as-model-new-retrieval-paradigm-recommendation-systems/)已读核心：ANN/Bloom/filter/rerank/scoring为nn.Module、Int8融合和streaming tensorrefresh；对象与评价仍是通用推荐检索，未建立foundation/LLM/RAG新增约束，按清单“不泛化通用推荐”排除，不凭GPU/编译类比准入。附件旧May22时间戳不能替正文May26事件日期，不追无关日期。

## A15 准备好的Books层续接

root R13 HyperGuide真实POST通过，指定窄位释放；作者仅同步本人note行政时态，正文不动。本轮2项真实Books均已写后通过（Feb correction、HyperGuide），不授DAY。

root R14实际读Ch66 PromptAudit/EvoCode承载正文与交接、两个具体NC通过。24171承载于“自动prompt优化…”parser/consumer/parse-cap/内容分责段与Response Rate完整链；24110承载于连续规格扩展/自有workspace不reference替换/strict旧回归-isolated-core分测及SlopCodeBench反侧，另由Evaluation Identity绑定harness/environment/scorer。MT@4与SR分母/attempt差异保报告，不把它写成新因果原则。root R16 ContextSparsity具体NC通过，当前Ch22语料关系×访问图/NSA-DSA训练迁移/selector监督与可执行kernel三链已实际承载有限主张，rank非单射不推出dense无用。

24117具体NC由root实际读Ch77 775–810和838–855及交接通过：typed skill/immutable raw/isolated validation、同policy有无skill对照与freeze、历史版本固定probe、source→target isolatedstore/heldout迁移合同已承载。本v1 contextshift/shortcut/composition/curated-vs-raw是受限新验证，不产生额外长期机制。

**24154 Palette拟最小差额 `TRAIN-LORA` / Ch30**。已实际读LoRA组合当前论证（两个adapters公式、行为冲突段，前方cross-backbone坐标、后方HyPA/activationcomposition交接）及Ch29/31相邻章开篇。现有正文解释参数可加不保行为，缺“训练时在非目标输入上重构base使更新趋近neutral”这条可组合性的构造条件；不是添加domain放宽操作权限。建议单段插在“不同adapters可能修改同一表示方向…不能把独立任务得分当作组合行为证明”之后、现softprompt组合之前，原公式/邻段不动。

逐字PRE（未授不写）：

若希望多个域的adapter能组合，训练时也可显式约束更新的输入支集，而不只在合并后观察冲突：目标域拟合所需的局部表示变化，非目标域则重构base的原表示，使该adapter在这些输入上的增量接近零。[一条受限安全适配分支](https://arxiv.org/html/2605.24154v1)由此提出组合条件；但固定线性层、相同输入下的局部近似neutral，不证明前层改变输入后整网仍无干扰，更不证明缺失的相关负域也保持不变。参数组合只是模型行为提案，不执行真实用户授权；负域采样、困难例挖掘、每域训练和组合后的完整安全与效用回归仍付费。域边界重叠、覆盖不足或旧行为退化时，保留独立adapter、较窄作用域或不组合，再由外部权限与发布gate验收。<!-- source-family:SF-2026-ARXIV-2605-24154 -->

拟本人note：exact-v1 §3–5/AppC/rootR13；只采用目标变化/非目标base重构的输入支集与局部线性组合界，非整网无干扰/真实授权保证；相关负域遗漏、neutral近似和组合全费保留，未核实现/复现。root必要Source已过，具体PRE与授权、实际POST尚待。

24248拟具体NC，当前Ch83 Server Admission双段已精确采用本v1，注册验证identity/allowlist/sensitivity/root/conformance与effect-time授权分离、根/撤销/metadata风险及fallback完整，作者实际读回直接邻接；root待核NC。24197拟Ch80 learnedfeedback两段/成功修订不证诊断因果段已有覆盖：AEA的TV→argmax缺margin/coupling、reward未测MI/不可授posteriorcollapse唯一因果；有限learned trace-evidence作为修订提案/额外费用实证不改变现接口，root待核NC。

root后续实际核Ch83 Admission双段/邻接及Ch80 learnedfeedback/修订≠诊断链，24248/24197两个具体NC通过。Palette按A15逐字真实保存Ch30一段＋本人note，root实际POST通过并释放；本轮3项真实整合均已有POST，尚非DAY。作者仅行政同步本人note，不改已核正文。

## A16 Multi-Agent RL具体参数共享差额/PRE（待授，不写）

24202 root必要Source通过；作者已实际读exact-v1 §3/4全部必要文字，policy-sharing为每role-type一个adapter，三个同role实例仍共更新，不是each-agent独立。训练一次/seed固定、无referenceKL、组8workflowrollouts、Qwen3 0.6/1.7/4B LoRA，最高validation/全run幅度不授稳定部署或因果诊断，step匹配不等token/GPU费。原结果随task/topology/scale变，SP亦有后期rolecapture，IP亦有cliff，不能选一个通用赢家。

Owner `AGENT-MULTI-AGENT` / Ch82。作者实际读开篇、单Agent baseline、learner/执行者/传播三分段、下一通信信息与读出论证，及Ch81/83交接；现有多执行者≠多learner讲单leader训练/传播，尚未解释多role梯度是否共用一组参数及独立role内部同类实例仍共享更新。拟窄位：现“多个执行者也不意味着多个learner”整段后、下一“即使通信引入了真实的独立观察”前。

逐字PRE：

角色拓扑还必须与参数共享拓扑分开：一个workflow的不同角色可共用一份policy，也可每种role持有独立adapter；同类角色的多个实例仍可共享这份adapter及更新，不能按agent副本数推算独立learner。共享参数使多role的梯度汇入同一更新，独立参数减少这类耦合，却可能让不同角色的策略漂移不同步；两者都要按role保存行为与完整workflow结果，不能只看平均reward、gradient norm或最终答复。[受限多Agent RL对照](https://arxiv.org/html/2605.24202v1)观察到独立role的较高峰值与后期退化，以及共享policy的role capture，不识别这些诊断为唯一原因。单seed、小型Qwen3 LoRA和固定训练steps不证明大模型或等总费用排序；多份adapter、rollout、角色诊断和联合回归均付费。数据稀薄、角色身份或共同奖励失配时，保留已验共享policy、固定workflow或单Agent基线，不把参数隔离当作稳定性保证。<!-- source-family:SF-2026-ARXIV-2605-24202 -->

拟本人note：exact-v1 §3–5/T1–2/A1/A2/A5–A7，root必要域有效；只采用role-type参数共享与行为/梯度人口分开，单seed/scale/LoRA/outcomereward/step非等费、peak非稳态与诊断非因果近文。未核实现/复现；PRE/唯一窄位/真实POST分层待。

## A17 Agent-ToM具体跨episode guardrail差额/PRE（未授，不写）

root已实核24216安全必要Source；作者实际读v1 §2完整：belief/intent/expectedaction/deviation是由full trajectory推断的假设，不是读取真实mental state；Verify读取初稿再检验benign alternatives，与Refine合一所以两次call，非三独立模型。Critique/distiller利用既往labelled episode形成语义规则，memory只增不删，训练/验证与部署适用性必须分开。主张仅hypothesis→evidence recheck与跨episode derived guardrails，非已校准真概率/开放世界安全。

唯一owner `PLATFORM-SECURITY` Ch72；已实际读policy-bound-sensor/enforcement段、DeepContext同session GRU状态段/完整后续MTMCS交接及Ch71/73开篇。现有解释当前风险state跨turn累计、模型verdict不拥有enforcement，但未区分跨episode distilled monitoring rule与本episode hidden-intent假设。通用rule-library生命周期由Ch77现有“From Failure Trace…”负责，本段只解释安全monitor如何消费，不重复库实现。

拟唯一窄位：现DeepContext完整段后、现“验收历史sensor时，还可固定图像场景与其余回合”之前。

逐字PRE：

跨轮风险状态之外，monitor还可从过去已标注的episode提炼可复用的语义guardrail，但规则库与当前意图假设必须是两份状态：先从本条轨迹提出belief、intent与预期动作，再用原始证据和可能的良性解释复核偏离，历史规则只能指导检查，不能把相似攻击自动定罪。[受限Agent监测对照](https://arxiv.org/html/2605.24216v1)采用这条假设—复核接口及critique驱动的规则积累；它读取完整轨迹/可见CoT，不证明隐藏意图可被直接观察，第二次调用也不产生独立真值或天然校准概率。跨episode经验增加了规则提炼、检索、重复判断和误拒回归成本；只增不删的库还会积累陈旧或冲突规则，需按Memory既有来源/适用域/撤销合同维护。轨迹不可见、标签或规则失配时，保留原证据、静态guard与人工复核；阻断及effect授权仍由可信执行层决定。<!-- source-family:SF-2026-ARXIV-2605-24216 -->

拟本人note：exact-v1 §2–5/§7/rootR15必要层；仅hypothesis/evidence/benignalternative与cross-episode guardrail分责，保fulltrace/visibleCoT、两call非独立truth、appendonly规则/误拒/费用与静态guard退路。未核实现/复现；PRE/写权/真实POST待。

## A18 已读相关题摘的末批具体贡献筛选（尚非Source完成）

不处理余下宽列表为队列。以下是此前有界主题/相关标题中已经读到完整题摘、尚未在A10/A13归并的八条；仅其具体增量进入校准，机制/实证可信度在必要Source中核，不借用应用名或generalprinciple加分。

| 身份 | 原约束 → 题摘实际增量 → 待核设计判断 | 拟评分 |
| --- | --- | --- |
| 2605.24603 CSP-Atlas | concept circuit可能只是keyword激活 → keyword-without-syntax contrastive checker把concept/token分量拆开、跨九参数检验 → 不把共现神经元当概念特异性 | 2+1+2=5 标准，稀疏8层code transformer/106concepts限定 |
| 2605.24611 Asymmetric Hopfield | symmetric fixedpoint容量不覆盖sequence存储 → binary/synchronous非对称构造给多长cycle/噪声稳健容量界 → 判断动态记忆容量的架构/更新假设 | 2+2+2=6，必要理论假设/证明定点深入；非生物实现主张 |
| 2605.24622 PoseRefer | fusion增益可能由category/text共享参数混杂 → pose/text路径参数隔离、category access导致scalar gate翻转 → 评估多模态grounding须先隔离表示可见权限 | 2+1+2=5 标准，不以机器人场景/31.9指标准入 |
| 2605.24631 JEPA-guided minority sampling | generator density的稀有不等语义稀有 → 另一个JEPA表示隐式密度指导diffusion及近似误差界 → 将rarity参照与生成prior分开 | 2+2+2=6 标准，核指导梯度/误差条件，不采world-centric=真实世界真值 |
| 2605.24681 Mix-MoE | 平行语料微调可能干扰单语能力 → LM/MT专家分工、两阶段mono/parallel适配及Fourier-feature routing → 比较参数隔离和交互是否真减少interference | 2+1+2=5 标准，不收翻译排行为独立贡献 |
| 2605.24686 FACET | 单一EI总分混淆识别/推理和交互 → 四branch题目分解，观察认知与交互profile分离 → 不由认知答题分推交互成功 | 2+1+2=5 标准；不采RLHF因果、普遍scaling或临床共情保证，具体blindspot先核 |
| 2605.24710 μP Feature Learning | 只看宽度/参数量不解释可识别的feature自由度 → 两层noisyGD meanfield唯一性、realization symmetry下identifiability、target条件稀疏dictionary及error分解 → 将feature容量绑定architecture-data/初始化矩类 | 2+2+2=6，必要定理假设/证明深入，不外推Transformer部署 |
| 2605.24797 HCL-FF | local goodness缺层间协调且feature不受约束 → coarse-to-fine层次训练＋supervisedcontrastive aftergoodnessdecoupling → 比较局部无BP训练的表示/协调取舍 | 2+1+2=5 标准，核机制/同条件消融，不以图像应用增分 |

A10二十项root必要Source与具体Books已全部处置；R22 24202/24216真实POST通过并释放，本轮5真实整合。24213/24219具体NC与24239有限仅报告通过；不重读有效层。A13十一项日期/精确v1准入rootR17已过；R18必要Source24266/24267/24270，R19 ContextEcho/24286/TUBE已过，其余普通必要Source继续。没有从20项已完成推断本日日级完成。

## A19 TUBE的密度界差额/PRE（未授，不写）

作者实际读v1 §3完整，root R19深入必要Source已过：切线上界是population/期望对象，finite Monte Carlo单次值不必上界，更不是自动CI；随机self-surrogate与目标估计必须独立，正surrogate失配会松/高方差。限定采用密度评价接口，不采用ARM普遍优于所有DLM。现Ch24“连续embedding生成…likelihood评价拆开”及LangFlow NLL/PPL界完整两段已读，解释variationalbound非exactdensity，但尚未说明如何从密度上下两侧定位，以及无偏估计≠每次保界。已读Ch23/25交接。

Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Ch24拟唯一窄位：LangFlow两段之后、现“连续与离散文本扩散的扩容差额还须先排除…”之前，原两段/后续RePlaid链不动。

逐字PRE：

当生成次序或去噪路径是latent时，ELBO只从下侧约束log-likelihood，不能直接与AR的精确值等同。若能写成路径似然的期望，可另取正的surrogate密度ψ，用log函数的切线构造 `log ψ + p/ψ − 1` 这一上界，再与ELBO从两侧定位目标；对固定ψ，用独立路径样本无偏估计p，可得到该上界的无偏估计。[TUBE的受限分析](https://arxiv.org/html/2605.24292v1)保的是期望中的界，不是每次Monte Carlo结果都在真值之上，也不自动产生置信区间；ψ若由随机self-surrogate估计，其样本必须与目标估计独立。Surrogate失配会使界变松或方差增大，额外路径求值、参考模型或独立样本都付费。证据不足时仍可报告原ELBO及估计口径，增加样本/独立误差分析，而不凭单次上下界交叉、PPL数值或少量模型比较宣告某种生成范式普遍更优。<!-- source-family:SF-2026-ARXIV-2605-24292 -->

拟本人note：exact-v1 §3/B1/B2/5.1–5.2/D/rootR19；只采用population logdensity界、unbiased估计与independentselfsurrogate条件，不把sample界/CI/模型普适排序授出；正性、variance/松界和全部采样费用保留，未核实现/复现。具体PRE/授权与真实POST待。

A19后续：root授原PRE唯一窄位，作者已真实保存Ch24第679行单段＋本人note，完整前后两段/本人注读回及限定diff-check通过；root真实POST通过释放，本轮6实际整合。Ch82/72两本人note仅行政同步R22既成POST，不再改正文。

## A20 剩余必要Source与具体理论争议（不扩附件）

以下六项exact-v1必要HTML均保存为 `sup_2605.<id>v1.html`；作者实际读到足以支持下述有限命题的方法、直接对照和反侧，未读所有附件/运行代码/复现。root R24已独核八完整题摘/日期；Source独核待。

| 身份 | 实际必要位置与采用范围 | 关键反侧及停止理由 |
| --- | --- | --- |
| 24603 CSP-Atlas 5 | §3–7，尤其§4.2checker、§5 extraction/集合差、§6/T2–4及Limitations；冻结8层sparse Python模型，最后token的MLP output维而非内部MLP hidden unit；58有keyword概念的checker将concept-only/shared/token-only分开 | 106概念非106因果circuit已认证；无ablation，checker5类非穷尽，tokenless不自动因果。9阈值只是该测量稳定性，不外推dense/多语言。有限“共现激活须以表面token对照”已足，不追全部artifact |
| 24622 PoseRefer 5 | §III–VI/TI–III；3764 references、5-room LORO、3seeds，路径参数/类别表分开，文本无object类别时同broadcast表示无法区分对象，global gate随该信息权限改变；scalar fusion可超singletons而非由gate值认证语义 | 原文称PTnocat→PT只text category变化，但TI两侧都从无到learned；不得采该句单因素因果。GT SMPL-X/scenegraph、modifier被strip、global gate在部分非pointing组反退、n=3seed t-test，不授estimatedpose或开放场景部署 |
| 24631 JEPA-guided 6 | §4.1–4.4/§5–6/T1–3/B3/T6/C；另一个DINOv2 encoder的Jacobian log-singular-score定义rarity参照；rank截断RSVD＋stopgradient投影、deferred/intermittent guidance，denoised域差需要延后 | “world prior”只是选定encoder隐式分数，非真实世界密度；低score参考集也由同score选，不能独立证semantic rarity。Envelope等价须inner optimum，不给有限RSVD无条件exactgradient/误差保证；本轮不采用Prop4.1强理论。A100成本10.44s/样本慢于DDIM1.45/SGMS7.24，快于MinorityPrompt12.42仅SD1.5该协议；textalignment/precision/coverage有反退，conditional结构保留只有限观测 |
| 24681 Mix-MoE 5 | §III全机制/IV-A–C/V-A/C–F/TV/VII/VIII；LM/MT两组FFN专家、stage1单语→freeze LM/router、stage2parallel适配MT/router，FFT实部+hidden拼接top1各组，提供与DCT/random/无变换受限对照 | §IV称4.1M、实现称4.2M，filter阈值亦有差异；dense FullFT/LoRA仅stage2而非等两阶段总数据/费用，mixed-data baseline虽有同mono subset不代表全基线等费；translationBLEU反侧不直接测monolingual retention/唯一interference因果，FFT“语义高低频”仍hypothesis。采用参数训练权限/分工，不授无遗忘或全尺寸优势 |
| 24686 FACET 5 | §4.1–4.4/§2.1和直接Discussion；480bilingual expert-refined items，objective300 exact/multilabel与interaction subjective Elo不同population；9模型profile可在认知与互动之间分离 | Gemini2.5Pro主judge、length penalty/匿名换位、defaulttemperature未统一deterministic；prompted单次text输出不是长期真实user/临床互动，ZH/EN作为高低语境proxy不能因果定文化。RLHF/规模/训练原因未实验识别，保原文强claim不采；仅分测label知识与偏好评分，不追全任务例子 |
| 24797 HCL-FF 5 | §3.1–3.4/§4.1–4.3/T3/§5；沿DeeperForward每层local goodness与GroupNorm decoupling，先CwC预训→linearhead原型聚类得树、层深映射coarsefine，再在decoupledfeatures施加fine-label supervisedcontrastive | 树构造/预训/linearprobe/validation选layer区间都计费；hierarchy单独让CIFAR10小退，合体含augmentation，FF仍比endtoendBP慢/泛化弱，channel随class数扩，不授生物机制/LLM或整体算费优势。T3有限交互支持设计取舍，不遍历无关分类例子 |

**三个中心理论争议保持原6分，实际必要理论审阅不是未读完**。24584作者与root已各一次实际核§3 Th1与B2 Th4：P_i共n+1而u/v仅n、K为n×n；n=k=1,a=0,b=1,x=1，P1空而式给0，真实e^-1，证明又调用n+1列。一般rectangular exact reduction隔离；对称prefix递推/作者有限H100实验只是Report上下文，不由反例否定也不认证一般实现。24364实际核§3.1 Def2/Lemma1及相关edge/Cauchy/inactive/VC/variancefloor/shift-ratio条件：pointwise pinball score跨kink跳1，任意小ε不满足有限Lipschitz，原smooth适用断言无效；AppE1另有nonsmooth不能修复该断言。仅audit函数域接口为Report背景，不授无条件光滑/quantile推广或迁移。24710实际核§2.2 Def2.5–2.8/eq7–9：Fλ=R+λKL而PDE另+λΔμ，重复扩散；R=0、π标准Gaussian时SDE稳态π，纸面PDE稳态N(0,2I)，不是同一flow/JKO。中心统一保证隔离，不借既有μP原则强写。三项均暂缓/不入Books，精确重开只需修订公式/证明或独立有效替代证据，不扩代码或全版本diff。

## A21 机构真实入口恢复结果增量

Qwen由官方前端home请求与bloghook实读定位真实 `GET https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`，成功原件 `sup_qwen_articles.json` 共40 articles、响应无分页字段；实际读全部title/date，May29 Qwen-VLA→May20 Qwen3.7跨窗，无May26列表项。不是SPA空响应证明零公开。另May26AlibabaCloud regional发布核心实读：Qwen3.7Max Singapore可用性、Skills/MCP门户与云产品接入、sandbox/memory高层宣传，未披露足以改变当前模型/训练/Agent机制的新增条件，范围与具体贡献排除，不借排行榜或产品名准入。

MiMo homepage Paper8卡有日期跨June29→March；Blog15卡多数无日期。进一步实读当前webpack route frontmatter原件 `sup_mimo_route_bundle.js`，具名May30推理全链、June8TileRT、June10Code与Dec18/19安全/HSS及Sep27toolrepetition有日期，未见May26。其余V2.5/Pro/ASR/TTS与V2Flash/Omni/Pro/TTS route未给日期，不能把“目录没May26”称历史全Coverage；只处理一次可用正式入口恢复，不无限猜测日期，必要历史版本日期缺口保留精确重开。

Seed两具名正式详情页已恢复 `https://seed.bytedance.com/en/public_papers/more-expressive-feedforward-layers-part-i-token-adaptive-mixing-of-activations` 与 `https://seed.bytedance.com/en/public_papers/negligible-in-size-significant-in-effect-on-scale-vectors-in-large-language-models`，原件 `sup_seed_moa_article.html` / `sup_seed_scale_article.html`。实际完整可见May26/题摘/作者，页面只有ABSTRACT和DownloadPDF，后者指向26647/26895后稿。root R28已实际独核两页和exact-v1历史，支持May26正文/采用命题资格隔离：不列正式当窗候选、不评分/不入Books，不声称当时一定未公开或机构零研究。重开只需May26可核正文或当期正式披露＋可核当时内容，不能由目录日期/July更新倒填全文。

## A22 其余具体Books比较（不为已有覆盖制造diff）

root R27已实核A20六有限Source通过，并实读以下三个owner后接受具体NC：24279 Ch75 374–397，immutable history/后台commit后ContextEcho完整双段已有snapshot-fork/versionedprobes/role-fidelity与taskutility分测、leakage/scorer/fork不一致/成本和非全role保证；24266 Ch79 395–449完整askutility/COIL/累计约束/成功后重估/Pool/when-how链已分用户中断费、belief更新、偏好与授权以及低置信fallback，合成人设constant-answer模拟未增加长期执行机制；24686 Ch66 35–51分情绪标签/当事人偏好/第三方质量、分项排序重排、视角/人口/cluster与临床限制，有限objective与subjective-Elo分测已承载。

作者又实际读下列完整承载段及直接交接，拟具体NC/Only，待root必要独核；分数不变，不把Source通过预作Books通过。

| 身份 | 实际owner与具体比较 | 拟处置 |
| --- | --- | --- |
| 24270 | MODEL-MOE/Ch21 145–150与703–711：路由frequency与敏感性分账，gate扰动同时改TopK/其他权重不隔离因果；语义标签/方向与专家本体分开，不能裁安全subnet | 5安全必要域，已有覆盖；20routing/100干预和不同run人口只报告 |
| 24299 | PLATFORM-EVALUATION-SYSTEM/Ch66 2784–2789两完整段：self/peer预测同一target标签，完整训练人口与测试disagreement切片分开，全人口/条件AUC与覆盖分账，不推自知或全部外部observer不可知 | 7深入，已有覆盖；verbalconfidence/相对优势的受限诊断不另造内省本体 |
| 24603 | WORLDVIEW-REPRESENTATION/Ch5 17–45明确分布式表示/activation可读≠被使用，499–510保表面改语义/改表面保语义和后续因果干预；checker只是这条合同的一种受限观察实现 | 5标准，已有覆盖；不把106概念/9阈值写成因果电路清单 |
| 24681 | MODEL-MOE/Ch21 158–162旧新expert/router的训练分责，冻结旧参数不保TopK/归一化人口或旧函数；后方jointobjective与稀疏梯度责任已有 | 5标准，已有覆盖；FFT具体有限变换与translation非retention留报告，不采语义频率本体 |
| 24530 | MULTIMODAL-REPRESENTATION/Ch23 930完整字幕视觉teacher→audio-only学生及两侧，AGENT-RAG/Ch76 407–415 embeddingmatching对query/正/难负例的teacher对象/学生几何与消费回归；特权teacher训练可见性与部署输入移除不等无依赖已承载 | 6标准，已有覆盖；document双输入teacher/视觉学生为受限新验证，截图子样本/stringhit非生成正确与累积消融保报告 |
| 24354 | MULTIMODAL-WORLD-MODELS/Ch25 600–613对象persistentaddress/可修订内容/transition与真实状态确认分责、1190–1207 futurelatentforecast/critic/真实反馈与pixel-vslatent完整链已承载 | 6标准，已有覆盖；map/agent instance稀疏替代是具体架构验证，未证sparse因果胜/完整70ms或物理安全，不把应用排行入书 |
| 24267 | PLATFORM-EVALUATION-SYSTEM/Ch66 472–475固定target、cue/null与选项顺序配对，明确不能要求改变有效信息的变体同分；当前EvalSpec按可见输入绑定 | 5标准，仅报告：context固定表面问题的特定认知诊断，生成/推断人口不等不支持新的因果规则，筛出的400题与共识不当真值；不扩social任务分类 |
| 24622 | MULTIMODAL-REPRESENTATION/Ch23表示可读/语言侧可访问/输出可表达三分，PLATFORM-EVALUATION-SYSTEM/Ch66可见输入与EvaluationIdentity的既有边界 | 5标准，仅报告：有限GT-pose/scenegraph的latefusion对照，原text-only单因解释又被TI反侧收窄；未产生普适参数隔离前提或新部署接口，具体类别访问/单globalgate证据留日报 |
| 24611 | MODEL-LONG-CONTEXT/Ch22容量随计算/状态/读出合同而变，而非AGENT-MEMORY；当前Attention/固定递归状态的设计比较不适用于任意binarynetwork容量定理 | 6必要理论，仅报告：预设同步majority块循环/LCM存在性与一次初始flip，不给自组织学习规则或语义序列/LLM状态实现。其有限构造值得保留，但不足修订当前语言模型机制或建立Agent持久记忆owner；不借memory同名强写 |

## A23 Faithfulness训练信息流差额/PRE（未授不写）

24286 root R19深入必要Source有效；作者本次实际读§5/equations7–10，update mask改forward，gradient mask只detach A→P logit导数，CoTGradient限制特定linear参数入口，均不等整个信息通路已阻断。原rollout/reward/advantage不变不说明重算forward条件仍相同；FACT额外扰动另付费，本次只采用三种mask职责分开，不照完整recipe。现Ch33 563–573完整POPE/PrefixRL/PACE链解释条件采样、prefix loss mask与无prefix验收，但未区分loss-token mask、attention visibility与edge backward mask；Ch32/34邻章交接已读。

唯一owner TRAIN-GRPO，拟窄位：PrefixRL完整两段后、下一“若 prefix 由 initial policy…”之前。

逐字PRE：

屏蔽哪些token的loss，还要与改变attention可见性或局部反向导数分开。若希望答案更多依赖中间推理，可在更新时禁止answer直接读取prompt；这同时改变了重算forward的条件，不能默认仍与原rollout是同一计算。另一条分支保持forward数值不变，只停止answer→prompt attention logits上的梯度，或只让指定CoT位置直接贡献某些线性参数的更新；它们限制的是不同的学习入口，不证明prompt信息或其他间接梯度已被彻底隔离。[受限信息流干预](https://arxiv.org/html/2605.24286v1)因而须同时保存rollout协议、forward mask、backward mask与loss-token支持，并把答案正确性、CoT条件充分性及shortcut诊断分测。可监测的推理不等于已消除reward hacking，局部指标改善也不识别唯一内部原因；重算、额外前反向与诊断评价均计费。条件失配、诊断不稳或任务收益回退时，保留原outcome-GRPO、独立过程验证和显式条件合同，不把一个mask当作faithfulness保证。<!-- source-family:SF-2026-ARXIV-2605-24286 -->

拟本人note：exact-v1 §2–5/A1与rootR19，2+2+3=7；仅采用loss-token/forward visibility/backward-edge支持分责，gradientlogit mask不等完整因果阻断；保conditional/metric人口、rewardhack未消除、有限任务与全费，未核实现/复现。具体PRE/窄位授权/真实POST待。

## A24 Books必要层闭合与有界来源收尾

root R29四NC、R30 Unveil/SparseWorld具体NC及DRInQ/PoseRefer/Hopfield有限Only均实际通过；R31 Faithfulness真实POST通过释放。root授权不再写前行政往返后，作者读完Ch4局部spiking/BP-proxy→非线性交接及Ch3/5相邻，Ch24完整SCALE→Prior与Ch23/25交接，按已过必要Source的具体差额实际写24797/HCL于Ch4第205行一段＋本人note，24631/JEPA于Ch24第2132行一段＋本人note，完整读回/限定diff-check通过；root R33真实完整新增/直接两侧/本人注实际POST通过释放。24229当前Ch66 AtomicTenets完整双段/前CLbench/后localrubric实际NC也在R33通过。

本轮已处理45唯一family（41 arXiv＋2机构release＋2 Anthropic重要修订家族），具体处置9真实整合/26已有覆盖/7仅报告/3中心争议。两Anthropic是家族内重要修订而非重新首发，不重复评分；RSP原家族有效记录定点见 `papers/2026/02/25/README.md` 的Feb24 RSP v3，仅核同家族身份不重读旧Source。FebRisk也只记录May26纠错event，不把R3拟7重新算作全家族分数。现有45候选的必要Source/Books分层已闭合，尚未代替来源及六节/DAY/FINAL。

ProofAgent24134已定点实读exact-v1 §3.3–3.5/§4.1–4.5/§5.2–5.4，原件 `sup_2605.24134v1.html`。拟关闭贡献：planner→conductor→persona juror→spread阈值revote/median/逐turn evidence是既有流程组合，confidence=1−spread/10未校准；大小harness同时改变adversarial压力与评分人口，接近分数不隔离judge可靠性或新增特定失效边界，不能借auditable/certification术语准入。不是因正文费时或Books覆盖排除，题摘原不清事实已读必要域，root代表排除校准待；无关日期不再追索。

Moonshot官方GitHub release `sup_kimi_releases_p1.json`网络截断，不能称完整100返回；实际JSON decoder恢复前63个完整object（Sep22～Jan15），其中May29 1.46→May27 1.45→May14 1.44已跨May26。1.45 created May26 11:50:53Z、published May27 03:39:38Z，不能把tag/commit创建日当release；精确原件另存 `sup_kimi_1450.json`。Org42repo和KimiCode whatsnew亦为有界入口，不扩普通PR/commit。

arXiv新增模型/多模态/系统/Agent四主题×分类API p0各100及一次简化transformer查询全部原文 `Rate exceeded.`（14B），无XML/total/结果，非零命中。此失败只保访问原件，不作正面Coverage。有限替代转官方advanced search真实表单：最初transformer＋recent submitted May22–25成功50/266（`sup_search_transformer.html`），发现默认most-recent与目标v1不等；再据实际表单改original submission date。announced_date_first仅支持年月且同日from/to报错，不伪称目标日查询成功；实际改May22–25 original-date＋CS/crosslist及四主线主题，待响应后记录真实分页/停止，不把原507变待关闭队列。

## A25 有界主题恢复的首七真实差额（root R35准入/日门已过）

实际成功入口为 `https://arxiv.org/search/advanced`；参数共同为 original submission `date-date_type=submitted_date_first`，May22～25、CS/crosslist、abstract field、size50、order=-announced_date_first。这不是May26完整公告列表，日期仍逐篇核。transformer：`sup_search_transformer_first.html`/`transformer50.html`/`transformer100.html`，149返回50/50/49；agentic：`sup_search_agentic.html`/`agentic50.html`/`agentic100.html`/`agentic150.html`，180返回50/50/50/30；world model：`sup_search_worldmodel.html`17/17；LLM inference：`sup_search_inference.html`/`inference50.html`56返回50/6。原报与邻日仅精确ID/v1去重，不继承邻日候选语义池；相关标题补读完整AB，范围明确的应用标题不送全文队列。停止于这些实际末页，不扩全月或12分类union。

定点日门反例：`sup_probe_datacite_2605.<id>.json` 中23603/23872/23464/23445/23893/23871/23820/23640均同DOI/arxiv.content/findable registered May25（01:54～02:04Z），据公告发号最晚界已在补窗前，不作May26候选；26147/26154/26165登记May27不能单独判May26，留精确窗外/资格线索，不扩大本日。其余新相关差额逐一读v1，不借当前search后版文字。

| 身份 | 原约束 → 精确v1实际增量 → 拟核选择 | 分项与投入 |
| --- | --- | --- |
| 24846 Keystone | activation强不等少量必要参数 → 跨task高activation筛subset、删除行为collapse与仅更新该subset SFT → 分可读/必要/可训练支持 | 2+2+2=6，必要causal/retention对照 |
| 24312 MEntA | 现MIA模板/多query成本可侦测 → 非模板broadquery＋response-document entailment的有限membership判断 → 检验RAG隐私与检测器预算边界 | 2+2+2=6，安全必要域深入；不提供攻击操作指令 |
| 24869 Lngram | tokenizer/hash keys把查表绑文本 → hidden-state学习binary discrete symbols、multi-route ngram lookup/contextreadout → 比较静态记忆key身份与训练/部署一致性 | 2+2+3=7 深入 |
| 24856 CAZ | 单bestlayer只看snapshot → depthinterval separation/coherence/velocity和scoredboundary发现非单峰/gentlezone → 区分几何读出范围与因果作用 | 2+1+2=5；只v1含34模型/ablation主张，非后v2的35模型/删改文字 |
| 25203 Walsh | lowbit rounding对坐标噪声敏感 → WHT＋activationenergy列rescale及架构吸收修正、W2vsW4负控 → 比较表示重参数化与执行正确性 | 2+2+2=6；不采Boolean influence理论迁移 |
| 25344 MixT | dense投影存储/运算压力 → v1 tensoroperator mixture直接执行、恢复depth范围与突变 → 判断结构压缩可恢复区间 | 2+2+2=6；只v1，非v2 Hamiltonian/local-sum叙述 |
| 25225 Field | patch局部响应常只经验定位 → firstorder sensitivity与局部线性域/Greenoperator slice测量 → 判断近似归因/迁移边界 | 2+1+2=5，不凭物理比喻准入 |

七精确v1完整题摘/history raw `sup_abs_2605.<id>v1.html` 已实际读完；同DOI DataCite客户端arxiv.content/findable、May26 registered原件为 `sup_probe_datacite_2605.<id>.json`，v1 May23 00:38:59Z～May25 02:00:41Z，联合区间May26，root R35已逐项实际独核通过。当前history有v2/v3/v4者只恢复v1，未做全版本diff。必要Source原件 `sup_2605.<id>v1.html` 已备，不预记Source完成。FaceSwap24735完整AB为155 eligible apps的filters/条款audit，已知dual-use应用流行程度而未新增foundation/LLM机制/失效条件；root R35代表EX通过，不评分/不以日期继续扩追。ProofAgent EX在root R34实际必要方法/对照核后通过。

## A26 后续有限相关十二题摘/十一潜力（精确v1已读）

成功主题页余下相关标题的完整AB已实际读，决定贡献不依赖关键词/章节映射。精确v1 raw均 `sup_abs_2605.<id>v1.html`、同DOI原件 `sup_datacite_2605.<id>.json`；v1 May22 20:49:53Z～May25 03:57:38Z，findable/arxiv.content registered May26 03:09:31～03:38:01Z，身份无冲突，联合日门待root最后实核。root已实际完整读十二v1 AB，对十一具体潜力通过，准入不授Books。

| 身份 | 约束 → 实际v1增量 → 需核选择 | 拟分项 |
| --- | --- | --- |
| 25328 DIVA | 单backbone理解/生成目标互扰 → shared/unique visual factor与双信息流/MI约束 → 比较保独有信息的联合后训 | 2+2+2=6 |
| 25326 LaP | 单图直接scene估计难同时保观察/几何 → structuredlayout state上离散修正policy＋trajectoryinit/preference → 分观测一致性与几何proposal修复 | 2+2+2=6 |
| 25156 Transplant | source不识别targetcausal结构 → abduction/deduction约束族与linearreprtransplant、learneradversary → 核可识别/不变机制假设与理想极值范围 | 2+2+2=6，必要理论深入 |
| 24962 TSA | 视频像素质量不保时空关系 → 以VFM STSS转换probcorrespondence分布、动态区监督 → 检验relationteacher/物理质量的边界 | 2+2+2=6 |
| 24942 GeoSteer | 固定centroid/topology限制nonlinearsteering → outputHellinger pullback metric的schema-supervised近似/四算术task → 区分label-free与schema监督/近似路径 | 2+1+2=5 |
| 24867 KCoT | graphCoT与表征解耦 → Transformerblock/kmeans对应及thoughtcondition alignment → 核对应条件，不外推任意LLM推理 | 2+1+2=5，必要对应定理域 |
| 24816 AOEPT | observed-only prompt缺失modal信息支集 → 全局modalprior学得prompt再按instance条件化 → 分missingprior提案与真实missing观察 | 2+1+2=5 |
| 24684 SUPRA | 强frozenfoundationprior时强制图聚合可反退 → priorretain privateMLP/sharedGNN＋deep supervision → 核aggregate必要性/强弱prior适用条件 | 2+1+2=5 |
| 24210 NP capacity | 固定pool/queryreweight/selfattentionlatent容量混淆 → CNP/ANP/TNP函数类、latent不绕encoder约束 → 核假设与容量分界 | 2+2+2=6，必要证明深入 |
| 25371 FOUND-IT | 固定task/对象粒度不适应动态任务 → 几何foundationhead/层级scenegraph按当前任务改granularity → 分地图结构更新与原始观察/实际控制 | 2+2+2=6 |
| 25404 ASRcause | scalar ASRconfidence漏deletion/错分恢复原因 → ASRlatent小detector区分perception/comprehension/deletion并targetclarify → 验检测与恢复阶段责任 | 2+2+2=6；v1为30%WER/17%task，非后版31/19 |

DTO24885一项按root要求只补决定准入的方法后EX：实际读§III-A–E/Eq1–6，pᵀE softtoken经冻结BARTScore反传＋已有文献[19]Gumbel-softmax，目标只是new−old或2new−old的现成metriccontrast。没有新离散梯度通道/soft-to-discrete无偏条件；作者“intrinsically unbiased/no sampling variance”也未由方法支持。此为已有surrogate换任务损失，不因榜单或新名准入；必要事实已足，不追任务全榜/降低分数代替排除，root R38已实际必要方法EX通过。其他代表EX：25343是NMM分类/路线综述，无新机制；25232既有spec/RAG/验证流程组合，未给具体新可靠性条件；24719八人interactive-story应用既有state-transform；24249是临床数据harmonization应用，24207是一般关系DB图学习query，无foundation负载新机制。均不评分，不因日期未核再建请求。

## A27 有界末页差额及有效层续接

沿A25实际末页，完整精确v1题摘补得五项：24900 ProActor（机会窗口标签/时机与动作分责，2+2+2=6）、24830 Macaron（输入schema/typed UI输出/评价合同，2+1+2=5）、24828 TTExplore（单thinking-node间接credit，2+2+2=6）、24245 UGC poisoning（单UGC页跨query重复暴露放大，2+2+2=6，安全必要域深入）、24812 CoRe（冻结coder、每planner thought下游M代码采样testcredit；再固定planner，仅全test通过coder子集memory reward，2+2+2=6）。raw为 `sup_abs_2605.<id>v1.html`/`sup_datacite_2605.<id>.json`；root R39已逐项实际v1史和同DOI arxiv.content/findable/registered联合核May26日门。CoRe最小方法已准入，不把memory测量叫渐近空间复杂度、CG代理叫普遍协作因果；关键对照/费用仍普通Source待办。24900/24830/24828/24245必要Source亦待。24245采用v1，不倒灌后v2的13words/检索57–76%等文字。

同批PASD24352/IAD24343完整题摘是非LLM DHRL的Overcooked技能/partner reward应用，未披露基础模型/LLM机制或基本架构理论增量；root R38按范围与贡献EX，不因游戏本身排除。另三含糊只定点补决定贡献的方法：APT24949 registry suffix-Levenshtein纠错/stage binary日志、JT24414 metadata前缀+constant-LR checkpoint平均与验证择优、PCE24462假定sound/no-bypass后集合包含，root R38均实核成熟recipe组合/无新有效条件EX。不扩大到全产品史、攻击操作或证明安全。

A26十二项日期已root R36全部实际通过，不再待核；其中十一潜力候选仍须各自必要Source/Books，DTO贡献前EX。A25前七必要采用域已root R37实际通过；MEntA具体NC及Ch76唯一引用定位修复真实POST（R39后root实际读回），Field Ch5完整Jacobian/readout/intervention链具体NC通过；Lngram在Ch22容量合同后/MemoryAthena前真实两段＋本人注，root一次完整POST已通过（现十项真实整合），不授日级完成。其余四项具体owner比较继续；初始45有效层全部直接复用，不第三读。

## A28 冻结68的必要层与实际Books全部处置

本轮有界发现停在A25实际主题检索末页；冻结68＝64 arXiv＋2 API release＋2 Anthropic重要修订，不再把507/1106或全部搜索返回变待审队列。root R37前七、R43后十一及R44最后五的必要核心/评价/关键反侧均实际有限审阅通过；三中心争议只到反例判断范围，不冒称强保证Evidence通过。R45/47/49具体NC/Only与R41–42/46/48/51–52真实POST均有效，不第三读原45有效层。

最终新增Books：21实际整合（13唯一owner/22正文自然段）、34具体已有覆盖、10仅报告、3中心争议/暂缓＝68；40深入完成、25标准完成、3争议必要域已审（DAY纠正：UGC安全与Transplant必要理论的真实投入为深入，不因NC回退标准）。新评分17×5、38×6、11×7＝66项，两Anthropic重要修订不重复家族评分。MEntA只修Ch76准确章节定位，原论点与别的binding不动，root真实POST通过，仍NC不增机制整合。

21实际整合为February risk correction、24140、24154、24202、24216、24286、24292、24631、24797、24846、24869、25203、25344、24816、24684、25326、25371、25404、24900、24828、24812。其完整新增/完整直接两侧/本人注均已唯一非writer root实际POST通过、窄位生效释放；只行政同步本人注既成状态，不改已核正文/他人注。LaP/FOUND在R51、最后ASR/ProActor/TTExplore/CoRe在R52完成；所有普通Source/Books/待写/待POST/未执行授权为0。

后十一采用域严格沿R43：DIVA MI/sharedunique估计非真独立；LaP几何假设/逆扰动/assembly分账；Transplant source penalty不验证target closure；TSA STSS/VideoPhy proxy非物理真值且温度/背景反退；Geo schema/PCA权限与solver/少fact边界；KCoT显式QK/center构造非任意Transformer/CoT收敛；AOEPT globalprior非真缺失/NM²I非单调；SUPRA非无条件SNR或梯度免疫；NP仅受限encoder/decoder与GP对象；FOUND GTdepthpose定量/真实GFM演示分开，dynamic未处理；ASR clean伪oracle/合成noise/模拟user非真实认知归因或人类恢复。最后五沿R44：ProActor future-aware窗口/组内PRI/综合升仍FTR升；TTExplore单node与调用条件混杂/固定六步；A2UI schema/render/效果分验及视觉筛选分母；CoRe consumer分阶段冻结与M采样/pass-gated资源proxy/全费；UGC真实检索命中后模拟替换非线上投放，crossquery重复URL/暴露引用条件分母，封禁UGC有效用代价。正式§4逐项自包含这些有限结论。

## A29 六节归并与DAY前机械检查（尚不授完成）

正式README现六部分归并68补处理结果，原94整行顺序/日期/评分与原小时窗保持，连续旧§4共136828字符、SHA256 `5231776d444e6e1c8e7ffaba7e3be861146c26c473ef0101126c8a7e9643734d` 与运行前index逐字一致。按现有validator冻结日期兼容，保存HEAD机械原档 `baseline-before-supplement-20261021.md`（182180字符），实际与HEAD全文相同；仅本日原件，不是另建研究账本，不改脚本/原候选。OpenAI两不同release由changelog真实链接的WIF/admin官方guide区分身份，May26日期仍回changelog，不编锚点或采后添参数。

V3限定校验已通过（1份V3）；正式报告504本地引用/109唯一目标均存在，162候选＝原94＋本轮68，六个固定H2保持。README/作者SUP/基线与14个本轮Books涉及文件的限定working/cached diff-check均通过；不冒称全仓无差异或其他并发检查。本方无stage/commit/push。来源历史子层、Seed两资格和三理论中心争议保持终态隔离，不授全Coverage/Evidence/无遗漏。当前只待root实际六节DAY、随后作者保存完成态再由root有限FINAL；README仍进行中，不以写完正文为终点。

## A30 DAY反馈的范围/投入窄修正

root实际六节DAY中发现UGC24245安全必要域与Transplant25156必要理论的真实投入为深入，已仅同步新候选表/对应证据及汇总为40深入/25标准/3争议；评分、Books、原94均不变，不重读Source。24684/24270题名已去HTML作者/Thanks混入，仅正式题名；两个API独立项目用changelog真实链接的官方guide区分，不编锚点。

arXiv正式§2结果窄改已检查，仅承认实际advanced四主题/全部分页及相关标题补检。API四主题＋简化transformer 14B限流、union507/1106截断只是已执行获取方式/召回局限，不是虚构‘尚未审主题页’或从未尝试的同义词外部保留；§5已从终态材料清单移为方式说明，成功fallback组合有效，不因旧入口失败否定。无新查询/不扩68，不把剩599作队列。真正Seed两历史披露资格、MiMo/Moonshot缺段与三中心争议继续精确隔离。README研究内容其余冻结，待root仅实读有变段并结束DAY，尚不写完成。

## A31 六节DAY通过后的完成态保存（有限FINAL待实际读回）

已实际读root R53唯一独立六部分DAY：全部16来源行、68新表/全部新增§4、完整1/2/5/6及两个投入标签/arXiv有变段均已实读接纳，旧94只复用有效层；40深入/25标准/3争议，21I/34NC/10Only/3D及13owner/22段一致，普通0。root核162行、94完整原行顺序、小时窗、136828字符旧§4与504ref/109目标零缺失，V3与限定检查通过。

依root授权，仅保存README状态完成/13:01:40+08检查时刻与1/3/5/6对应时态，不改研究语义/候选/旧94/旧证据/Books。真实来源/资格/中心争议继续隔离，不授全Coverage/Evidence或无遗漏。本次完成态等待root一次有限FINAL读回，不以本作者保存动作冒称FINAL已过；无stage/commit/push、未改LS/索引/合同/脚本，不跨日。

## A32 R54完成态有限FINAL实际通过，任务交还root

root已实际完成保存态有限FINAL（R54），13:01:40+08完成字段/相应1/3/5/6时态已读回通过，V3/冻结与限定检查有效，本日全部ownership释放。68＝21真实整合/34具体已有覆盖/10仅报告/3中心争议，40深入/25标准/3争议，普通Source/Books/POST/未执行授权0。原94完整行、小时窗、连续136828字符旧§4保持，162候选与504ref/109目标零缺失；外部资格/历史子层和中心争议继续隔离，不授无遗漏或完整强保证。

本次只同步README/SUP中R54既成回执，不改研究、Books或本日之外材料；本方未stage/commit/push，未改LS/索引/合同/脚本，不自行跨日。本文先前‘待’均为分层过程状态，以本A32/root R54完成态为本日最终停点。
