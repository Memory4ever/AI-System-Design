# 2025-12-20 非作者分批独立复核

复核者：Feynman（作者Nash）。首次检查时间2026-10-02T20:11:01+08:00；最终回核2026-10-02T21:40:45+08:00。结论：通过。以下保留分批实际阅读、发现与修正过程，早期待办由文末最终一致性取代。

本日独立重读AGENTS、研究合同、来源使用说明/14每日及arXiv主题组、Report V3、Prompt、ROADMAP、CHECKPOINT。实际读取ADMISSION_CALIBRATION、当前ADMISSION_ADDITIONS、SOURCE_STOPS、BOOKS_SCOPE_PROPOSAL；没有从18/19结论推断20完成，也没有扫描周源。窗口[2025-12-19T09:00:00+08:00,2025-12-20T09:00:00+08:00)。全日查询/停止及风险负侧核验仍继续，不把部分表当最终分母。

## Gemma Scope 2首批源审

独立HTTP200原始[官方Blog](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/)字段：article:published_time=2025-12-19T12:00:00+00:00，落本窗12/19 20:00；modified_time=2026-07-06T14:01:43.888736+00:00。首次直取压缩内容解码失败，改按gzip实际读取字段成功，不用失败作零事件。当前Blog不是不可变2025快照；[官方所链报告](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/Gemma_Scope_2_Technical_Paper.pdf)首页打印2025-09-16不赋论文首次公开。

已实际读报告题摘、§2必要SAE/transcoder/skip/weakly-causal crosscoder/CLT定义、§3.1–3.3/Table1、§4.1–4.5与§5必要open problems。2+2+2=6的最小命题是解释artifact参数化与测量对象/保真权衡，而非规模或成熟SAE原则。

- Table1/§3.1明确CLT只270M、1B；全层SAE/skip-transcoder覆盖更大Gemma3模型，不能合写为27B跨层解释实验。
- 多层初始化选择较早decoder/较晚encoder点积的相近latent，降低冗余后渐减目标L0，支持具体初始化分支，不证明所有概念唯一化。
- §4.1明确FVU不考虑重建误差对下游loss的效应；同样FVU的residual SAE有更高delta loss。固定2048×1024、special-token mask与默认pretraining分布，不授OOD安全。
- §4.3解释者预测fire/nonfire，是分类测量不是概念真值。§4.4 skip增加仿射参数后FVU/L0改善；Fig5是Gemma3-1B-IT一个固定prompt的cumulative influence图，不是复杂行为因果完备性。
- §4.5初始化cosine不是受控端到端速度证据；§5 jailbreak、faithful reasoning与dark matter为开放问题，不能写已解决安全行为。未运行实验，不采用宣传倍率。

## Books具体差异

实际读Ch66当前SAE sensor段、2002–2011既有干预边界、Interpretability Graph诊断权段及Ch65/67交接。另读Ch5“证据阶梯”“信息存在/可读/被用”和“解释模型Faithfulness Budget”及后续OOD适配段。已有覆盖的是replacement不等原模型、图pruning/label/control范围及sensor不授decision；不能当作本项全部已覆盖，也不能把这些旧原则重写为新贡献。

可由root协调唯一owner `PLATFORM-EVALUATION-SYSTEM` 的局部差额：将FVU、replacement delta LM loss、auto-explanation firing预测分别登记，以及skip/跨层参数化改变归因对象的可比条件。Ch5保留基础因果证据论证，Ch66只落实measurement contract，并链接其实际Faithfulness Budget段；不在Ch66重复全部transcoder机制。认可作者两段草案的窄方向，但需保留270M/1B CLT与单prompt限制，避免把“output loss”当任务干预。当前未写Books，需root实际整合后非writer POST；不是外部受阻。

## Anthropic首批潜力

实际读[Activation Oracles](https://alignment.anthropic.com/2025/activation-oracles/)完整核心方法及末段限制：activation注入AO第1层而非任意原目标层；3/4审计任务有用并保留Secret Side Constraint反侧，oracle自身推断/猜测不等目标模型已形成该结论，非mechanistic解释。potential成立、官方仅Dec19日精度不授落窗；不因日窗未知取消普通阅读。

实际读[Bloom](https://alignment.anthropic.com/2025/bloom-auto-evals/)四阶段/seed/config/evaluator核心；相同seed配置不等相同prompt分布，elicitation不是部署风险基率。评价差额核验继续；当前不评分、不入Books，精确发布上下界仍保留。

## 剩余复核

待作者本日ordinary收束，再核四组原始停止/精确补检范围、全部拟入选与安全/设计反证、按理由分层负侧、artifact必要patch及正式README。当前只通过Scope首批日期/准入和上述限定源审，不授Coverage、全日Evidence或Books Gate。其他历史源/first-public保留按具名原记录终态隔离，不重试已穷尽接口。

## 后续独立检查与普通差额

2026-10-02T20:23:47+08:00更新。作者本日ready后实际读正式六部分、四组原始查询/页尾、全部ADMISSION记录与本日七repo GITHUB_WINDOW。LANG/SYSTEM/MM/COMPUTE分别171/9/30/37行，跨组191身份；完整题摘182为作者初筛分母，不是本窗首次公告或182确定候选。非作者不声称独立读完182正文。

独立实际读取56个唯一exact-v1完整题摘：

- 安全/设计反证及兼含关闭项16：2512.16182、16238、16272、16279、16280、16292、16307、16310、16419、16532、16538、16602、16650、16649、16698、16750。
- 分层负侧12：2512.16236、16275、16494、16425、16442、16447、16301、16344、16760、16901、17029、17060。
- 安全/评价/优化边界16：2512.16439、16523、16565、16770、16790、16816、16855、16899、16912、16914、16921、16962、17023、17053、17066、17075。
- 风险/反证与范围补样12：2512.17079、17083、17209、20662、20660、22174、2601.03265、2512.16245、16297、17146、17121、17189。20660按exact-v1题名/正文身份，不把当前别名倒填版本。

未逐项重读其余126题摘或全部附件；已有明确贡献且日期终态隔离者不因精审费时改关闭，不采用作者摘要中的性能/安全数字。Biosecurity GenomicSAGE的ESM变体/soft-prompt及临床报告循环范围关闭可接受；CLIP否定对照、ARCD分层decoder保留potential正确。

两项负侧须重开，作者原ordinary0不成立，待其同步：

| 精确材料 | 独立必要原文与决定 |
| --- | --- |
| [GFLAN 2512.16275v1](https://arxiv.org/html/2512.16275v1) | 实际读§3.2.2–3.2.3与AppendixB。将不变约束与逐步放置状态分成两encoder再融合，single-encoder对照保持输入/decoder/loss/schedule，观察到布局失效差额；不能仅以户型领域或成熟CNN关闭。重开potential：静态/动态条件干扰与分解边界。该对照未完整匹配参数/compute、主要定性，不采用普遍收益。first-public继续hold。 |
| [PoseMoE 2512.16494v1](https://arxiv.org/html/2512.16494v1) | 实际读§IV-A–C、§V-D/TableVI–VIII。可靠2D与不确定depth先分专家分支，pose router再融合、双向时空cross decoder后交互；TableVI含近似参数匹配MixSTE及PME/PMD分账。重开potential：输入可靠性条件下分支/融合时机，而非通用MoE优越。作者相关性即因果与Gaussian初始理论不采用，first-public继续hold。 |

其余抽检关闭项的具体理由可接受：reranking/Agent Adaptation/Driving VLA材料未提供新的受控系统盲点；ORKG/TIB助手是特定服务/导出与模块演示；Physics观点不构成已验证理论；Racial News/VR/TA-Ego的局部任务实验不自然授长期LLM训练或执行可靠性增量。不是以survey、领域、安全标题本身排除。共同的“领域应用无增量”理由已扩查到上述12负侧和17146/17121/17189，发现两项实际机制后重开，不扩大宽库存。

Plausibility Failure HTML不可得后只改用[官方v1 PDF](https://arxiv.org/pdf/2512.16750v1)，实际读§3–4.2必要协议：三轮题目/仪器变化并非干净纵向对照；人类评价混合流畅性与核验负担是潜在反证，不授唯一因果。保持potential/datehold。

## 普通官方与来源边界

Bloom后续已实际读完四阶段、scenario diversity、40例人工judge校准、case self-bias、compute与limitations必要段；elicitation率不等风险基率，judge/scenario/rollout改变分布，模拟tool后果不等真实执行。Activation Oracles必要源审延续首批限定。两者仅Dec19日期不能定本窗，均终态保留，不为时间未知取消普通阅读。

实际独立读取Video1.5三个原始patch：36916f8c3d20ff648e6f44c6f6d4dc5f8ba0d7c5的memory_efficient context保存/恢复slicing与tiling但没有try/finally，不能声称异常时恢复；85c5343c72f717e7118eacc176b907da4f62941f处理FA3 tuple返回接口；40d5b27f2361d48acd024ad0481c1f0c9498f87c保留预编码latent与I2V pixel输入并同步SP。局部兼容性潜力保留，无端到端正确性或性能保证。WorldPlay四项按原commit身份/README与merge去重读取本日记录，未独立重开全部四patch；19已读的具体代码修订不作为20新家族。author/committer与pushedDate=null不证明公开。

十四源固定原始目录按本窗邻接重读：DeepMind正确/blog/page/4/24项，Google Research年页12项，Anthropic Alignment Dec19/16/12/8；不是从前日完成结论套本日。Seed必须同时计type1与type2：固定原始记录type1实际18/total94/next20，首两项pinned后Oct21至Jun25；type2实际15/total49/next20，Dec24/18/16/2/Nov27至July23。此处是该原始响应数，不用root另一时刻18/45响应替换；有pinned/next，不授完整严格排序与零事件。正式表只写type2须作者补type1。Google publications年精度不能证历史first-public，正式表结果应保留受阻，不能Blog替代Research/publications。OpenAI“继续收束”旧措辞须改成已穷尽具名历史外部隔离，而非与ordinary0并存。

2026-10-02T20:30:17+08:00官方列表补核：带skip800/show200入口cache miss，不拿失败证明空；裸官方月页可读1302身份，经该页all链接恢复原长页。实际只输出/浏览16171–17299的52个主表及cross-list标题，与本日具体处置对读；含16323评价攻击、16832模态信息、17179/17220长文及17247/17260/17267等已在ADMISSION记录。未把月表当每日公告或整月题摘队列，不追加未知公开时刻。无需重复同API。

## Scope 2写后核验

实际读取root新写Ch66 SAE sensor后两段及Harness Identity前后、主Review note，重新对读技术稿§2、Table1、§4.1/4.3/4.4/Fig5/§5必要段；Ch5 Faithfulness Budget和相邻Ch65/67开篇对读。新增段以测量身份承接sensor，不重复Ch5基础因果链；三指标、近似对象/skip、PT/IT与CLT270M/1B限制保留，不宣称27B跨层、安全或速度。POST通过，仅改该新增末注状态；本日正式正文尚待作者同步实际整合与普通差额，当前仍未通过日级复核。

## 21:20:52 普通差额回核

按20日重新读取七项适用上下文、CHECKPOINT、AUTHOR_REVIEW_RECONCILIATION、当前正式六部分及ADMISSION_ADDITIONS的覆写入口。两项原close已经被明确取代为potential，具体对照/局限及first-public隔离保留；正式Seed type1/type2和Google publications受阻均已同步。Scope实际整合/POST与唯一owner未变化，无Books待办。未重复未变化的56题摘或PDF。

定点重取[OpenAI RSS](https://openai.com/news/rss.xml)HTTP200，758460 bytes、1243 items，以本日独立窗口[2025-12-19T01:00Z,2025-12-20T01:00Z)解析pubDate，0 feed entries；可见邻接为Dec18 00:00/11:00/12:00 GMT至Dec22 00:00 GMT。正式SRC-OPENAI仍仅写“RSS有限失败”，须同步已恢复部分；该0仅限当前RSS，不代主Research历史、全渠道或无遗漏，主历史目录仍受阻。没有拓展阅读窗外全部内容或继承21/24零命中结论。

§5现有处置实质安全，但完成态仍须明确写“本窗终态保留项”，同句“不用于正面证据、Books或无遗漏断言”，并去除已完成非作者部分的旧等待措辞。此为具名普通同步，不是外部受阻；我未越权改作者§1–5，metadata/§6暂不授完成。

同版本20662在24定点读到的必要方法混杂适用于此处复用：PDF§2.1同时改系统提示与温度；§2.2比较不同prompt下未长度统一的整段log概率，不能识别同条件解码最优性；§2.3/3.3含每轮摘要/事实重述且GPT-4o实际142轮，不授200轮普遍上下文鲁棒。20保留potential/datehold、不采用这些正面命题的判断不变，无需重复全篇或新增Books请求。

## 21:40:45 最终日级一致性

本日七项适用上下文、CHECKPOINT最新21:29:02停点、作者差额及正式六部分重新读取。最后RSS恢复与本窗终态字段已实质同步；两项potential重开、Seed双类原始数值、Google publications受阻、Scope6分/实际Ch66位置/POST均一致。普通工作0，唯一确定本窗家族的必要证据和Books已闭环；未发生新的版本/命题变化，不重复既有56题摘和必要PDF。

日级独立通过，更新获授权metadata/§6；未改作者§1–5，§6明确取代其中旧交接等待状态。终态保留只接受具名原始日期/历史/旧材料重开，非Coverage/Evidence通过或零事件保证。未修改共享正文/state，未stage/commit/push。

实际完成态校验：`python3 scripts/validate_research.py --report papers/2025/12/20/README.md` exit0、1份V3通过；本日README与独立记录限定`git diff --check` exit0。机器结果只确认结构/可判一致性，不替代原源和写后审阅。
