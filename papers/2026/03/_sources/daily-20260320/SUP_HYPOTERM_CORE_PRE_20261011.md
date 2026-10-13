# HypoTerm17504：必要原证 / actual owner / 最小 PRE 准备

resume_review17_18，2026-10-11，仅03-20补03/19。root允许、作者明确分配且未读core，原2+1+2=5及完整AB/自然日准入复用本日独核§13；准备者不自行授Source/PRE/safe/DAY。只本packet，未写Books/Report/LS/索引。

## 1. 必要实际原证与停止

[exact-v1](https://arxiv.org/html/2603.17504v1)实际§2–5 L75–210：数据生成/过滤与split、训练对照/评价条件、Tables1–6和直接utility/safety/verbosity反侧；§6必要probe/logit-lens/SVD及§7–9直接限制L214–288、Conclusion的解释边界L290–300；B/Table8 L344–366、C/Table9 L367–378只核数据数与样本替换。当前官方abs完整AB/history轻量核到仅v1，无具体纠错/撤回触发。未遍历全部参考文献、D/E案例图、repo/代码或独立复现；A只有HTML图题不是prompt像素，未采用其未读取内容。

合成术语经过Google/Bing/Brave/Dolma及lexical检查、909→676保留，支持作者搜索范围中的不存在，不证明所有模型语料或现实世界永远无该术语；有效实体与合成实体共现问题要求承认后者未知但不抹去前者。16956初始问题经过三强teacher输出/过滤后，最终11151问题，每问题round-robin选择一个有效回答。31487是原有效response数量，不是31487最终独立QA。若三teacher全失败，该问题还从Enhanced benchmark移除：训练与评测人口都经过teacher可答选择，不是独立无条件未知实体总体。被替换术语构造的机械替换问题因语义/语法失真不用于训练。20topic中test1–2、val3–4、train5–20且声明term不交叉；训练8961，val1159，test1031。

## 2. 对照 / 直接反侧 / 不采强解释

实验将七instruction源按比例减少，加入8961 HypoTerm训练问答，保持总68856条；Table9明确8961约13%，不把正文12.5/12.9描述固定成通用recipe。相同样本条数不是相同tokens/compute。两架构Llama3.1-8B/Gemma3-4B，各base/instruct、control/experimental，每组100LoRA配置，共800训练run；随机配置但固定random seed，是400配置配对，不是800独立seed复现。LoRA rank/alpha/dropout、LR/batch/epochs共同变化；作者总训练约22k H100 GPU-hours与先前基准约4k H100 GPU-hours，不据此填推理latency/生产费用。必要段推理batch/concurrency/SLO、完整构造/teacher/judge/搜索费与跨seed CI Not Disclosed。

200 stratified test问题×两instruct模型组成400人标response用于从七候选judge选择Llama3.3-70B，97.2%是一组作者标注选择结果，不认证所有SFT后模型/领域无judge偏差。FactScore也用LLM评价，AILuminate用LlamaGuard；不得用同系judge替代外部真值。Table4 HypoTerm median变化Llama base+.19、instruct+1.15、Gemma base+24.95/instruct+25.91（表单位百分比），FactScore+.39至+.86但MMLU四组均-.26至-.35；正文159的2.2/26.5不是Table4同值，不混录数字。Base两组Safety-1.87/-2.29且显著，instruct-.58/-.46非显著不等改善或自动恢复。下游safety mitigation原文是未来建议，不是已验证方案。

Table5 valid问题Missing下降，但直接Refusals四组全部上升（+.10/+.19/+1.84/+1.41），不能宣称不增加false refusal。Responsiveness列单独报告，不自行按不同类别算术合并或授真实回答正确率。Table6 Gemma HypoTerm输出长度+49.1%/+42.4%，这还增加输出费。只采这一有限训练数据构造与成对验收分支，保architecture差、旧普通SFT、unsupported断言/valid拒答/知识任务/安全和输出预算联合回归。

§6 logit lens是定性案例；Real/Hyp、Harmful/Harmless、Easy/Hard的probe标签不等真实知识边界。方向cosine、SVD top direction和选largest差异配置的案例不能推出知识保持、正交独立控制或late veto唯一因果。表行为反退本身限制“without unlearning”。这些强解释不采用，不依赖未读案例图或全部附录来绕过局部反证。

## 3. actual sole owner / 差额

恢复实际重读AGENTS、研究/Report合同、Sources每日/arXiv、统一prompt/ROADMAP、本日README/STOP与相关LS路由；Books PROJECT/学习/写作约束已读。actual [TRAIN-SFT / Ch29](../../../../books/part-04-training-system/29-sft.md)196–220与238–256、1158–1216完整必要局部：208已有同质examples过拒答；240–250已有refusal/teacher/judge选择偏差；1172–1189有base知识边界三层合同，1191–1208有同题受控证据充分性，1211–1215有probe不证明机制。Ch28/30入口明确pretraining/PEFT算法职责，不复制其实现。

具体尚缺的分支是人为不存在的nominal term与真实实体共现、按teacher可答过滤训练/评测人口、equal instruction-count replacement及terms/topics持出，联合验有效实体拒答/知识/安全的实验边界。不是泛泛教模型说不知道，也不是读取参数知识全集。因此拟sole TRAIN-SFT原208同质过拒答后、210 reasoning trajectory前一短段。若非准备者认为已有具体覆盖，须指出真实段落，不以主题相似假NC；不因负面或小幅结果降原5/EX。

## 4. 最小逐字 PRE（待非准备者核，未写）

另一种拒答示教不先估计模型的全部知识，而是在真实实体旁加入经有限搜索检查的人造不存在术语，让回答既承认该术语无可靠依据，又不把真实实体一并否定；用这类问答替换一部分普通instruction，并保留术语和topic持出的对照。但teacher全无法回答时同时删除训练与测试题，会把“未知”的评价人口收窄到生成器可解释的子集；相同instruction条数也不控制输出tokens和完整构造费用。[受限HypoTerm对照](https://arxiv.org/html/2603.17504v1)中，未知术语得分与事实评价可改善，真实问题的直接拒答却增加，知识任务和部分安全切片退步。因此这是一条局部数据分支，不是模型已读出真实知识边界或内部能力保持的证明；promotion要把无依据断言、有效实体拒答、知识/安全回归及输出预算分验。人工术语失真、judge偏差或业务拒答代价过高时，保留verified-answer/refusal SFT与外部证据，而不把更会说不知道当通用可靠性。<!-- source-family:SF-2026-ARXIV-2603-17504 -->

静态源注：`SF-2026-ARXIV-2603-17504` — [HypoTerm exact-v1](https://arxiv.org/html/2603.17504v1)§2–5/Tables1–6、§6直接解释反侧/§9及B/C数据计数；仅合成不存在术语与真实实体联合示教、teacher过滤人口/equal-count替换及held-out分验边界。Fixed-seed配置配对非独立seed复现；valid refusal、MMLU/safety反退与输出费保留，probe/SVD不授真实知识或能力不变。未核代码或复现。

支持及直接反侧足够上述提案即停；准备者不自授PASS。待resume_mar17非准备者必要Source/actualowner/PRE裁，root协调共享Books锁；未写未POST，不计safe/DAY。

## 5. 非准备者必要 Source / actual owner / literal PRE 复核

resume_mar17，2026-10-11，仅03-20独立上下文，恢复实际重读AGENTS/研究与Report合同/Sources每日及主题/prompt/ROADMAP、本日README/STOP及相关LS路由，Books项目/学习/写作约束。非准备者实际打开exact-v1 §2–5 L75–210（含T1–6）、§6 L214–264及§7–9/Conclusion L265–300，B/C L344–378；不把返回的未采用参考文献、D/E图片或repo算必要审阅，不复现实验。原准入/日期及5分复用本日独核§13。

核对L101三teacher均未满足golden-answer标准时训练与Enhanced benchmark同时删除，L86–88响应数/最终单QA与terms/topics持出，L114/135及T9 equal-count而非equal-token/全费用；T4的Fact/Hyp改善与MMLU/安全反退、T5真实问题Direct Refusal四组上升、T6 Gemma输出增长准确。Fixed-seed的400配置配对非800独立seed；judge经作者有限400响应选择，不授通用真值。§6的Real/Hyp、Easy/Hard、Harm/Harmless方向和SVD没有鉴定参数知识全集或能力不变，正文不采此强解释，有限数据接口与直接行为反侧可分采。

实际Ch29完整190–225、238–256、1158–1216及Ch28/30入口已读。原208同质示教过拒答、240–250 synthetic/judge selection bias及1172–1208知识/证据边界未承载本项具体synthetic nominal-term + valid-entity、teacher-filtered train/test人口与equal-count replacement分支，sole TRAIN-SFT原208后/210前成立。原单段literal PRE及静态注逐字回必要原证，有限PASS；“teacher全无法回答”只指前文golden-answer准则失败，不解释成三teacher不产生文本。未写/未POST不计安全处置；请root协调窄ownership后落实，非writer实际完整正文/邻接/本人静态注POST一次即可。

## 非 writer 实际 POST

resume_mar17，2026-10-11，准备者resume_review17_18获root Ch29窄锁实写后，本人非writer实际完整196–224（新210）及1462–1470本人/TPD/SFT邻注读回；原单literalPRE逐字、有效必要原证及静态注回对，有限POST PASS。少量示教/过拒答→有限synthetic-unknown branch→reasoning轨迹前后衔接正确；teacher筛选人口、equal-count与全费、valid-refusal/MMLU/safety反退及不授真实知识/probe能力保持均近文。仅本family段及静态注，不改Book流程身份，无DAY；root可接纳释放Ch29，报告随后按真实单项归并。

## 6. 授权窄写 / writer 自读（不是独立 POST）

root在§5非准备者有限PASS后授resume_review17_18 Ch29单family窄写。actual当前198–219与本人末注邻接自读后，原单literal PRE实际写210，static1470；写后完整196–219及尾8实际顺读，对§4逐字一致，新增只该正文和static，其他既有并发diff保留。Scoped实际diff/边界已检查，diff-check0。交resume_mar17一次非writer actual完整局部/本人源注POST；准备者虽是writer但不自己授POST/safe/DAY，不改Report/LS/注身份。
