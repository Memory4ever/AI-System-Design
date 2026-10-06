# 03-19 StubbornNeighbors 2603.15809：必要原证与最小拟稿

准备者：resume_review17_18；2026-10-11。只本03-19补03-18自然日，保原2+2+2=6。此文件是给root非准备者裁决的packet，不自行授Source/PRE PASS、安全处置或DAY；无Books/Report/LS写入。

## 1. 身份、范围与实际停止

Primary：[exact-v1 HTML](https://arxiv.org/html/2603.15809v1)、[当前官方abs](https://arxiv.org/abs/2603.15809)。题目Don't Trust Stubborn Neighbors: A Security Framework for Agentic Networks，Samira Abedini等五作者；当前官方页只有v1，Submitted03/16，无当前撤回/纠错说明可见。提交日不代公开日；本19已准入日期夹证复用SUP_LATER_ADMISSION/SUP_AB_15809，不重扫发现或版本史。

压缩恢复后重新实际读完整AGENTS、研究/Report合同、统一prompt、ROADMAP、Sources使用/每日/arXiv主题、LS相关路由、本日README顶部/STOP/独核顶部及本family准入行；Books背景三文件完整读，现Ch82及相邻81/83相关交接实际读。原必要Source有效复用：完整题摘、§3.1–3.3/Eqs1–6、§4.1–4.4的条件与Eqs7–17、§5协议/模型/数据/Eq18/Tables2–3、§6–7，B.1/B.2/B.4/B.5解释文本、C/Table5、D拟合解释、E/Eqs19–22/Table6；F.1–F.5仅直接相关式子及证明文字，不宣称全部证明或图已视觉核。恢复后定点重开§3.2、§4.1、§5.1–5.5/Table3、B/C Table5与E决定性定义，未扩代码/全部prompt块/附件。

## 2. 新增机制与理论—实现分责

原准入链保留：同伴共识可能被单个强势固定意见者带偏→用FJ意见动力模型拆分prior、旧belief和peer pull，并在LLM讨论中引入外部校准的speaker信任→重新考虑谁能改变下一轮同伴意见，而不把统一答案当独立真值。

§3.1攻击者只控制一个peer的prompt/回复，不能改良性system prompt或网络边，能力同档。§5.4明确改变原开放威胁模型：集中system owner有已知正确答案的校准题，取得各speaker在peer影响前的round-0答案。T-W用10道非主评价warmup准确率平方初始化后冻结；T-S初值0.5，在主评价随机20%题上用同题round-0 correctness更新；T-WS结合两者。E的momentum0.8、步长0.4、clip[0,1]属已披露实验设置，不拟采通用recipe。Owner把信任作为speaker metadata注入receiver prompt，要求rank/tally并优先高信任意见；这是生成式讨论指导，不是确定性执行权限或答案事实认证。

FJ Eq1有prior pull γs、旧belief retention (1−γ)αb、peer mixture (1−γ)(1−α)Σwb，W要求行随机；Eq3的M含α的self retention。γ=0 consensus依赖M irreducible/aperiodic，均匀平均还需doubly stochastic；完全固定peer支配需相应可达/逆存在条件，不能外推任意断网或零边。§4的r_a是均值平衡对攻击者prior的导数/份额（均值包含攻击者），不是实际攻击事件概率或答案真值证书。人数增加的结论依赖权重缩放，constant攻击者weight/central hub不授无限稀释。原静态定理也不自动证明动态W(t)的安全稳定性。

实际LLM没有运行FJ数值更新；作者让其输出选项概率，再拟合观测轨迹。Table2 descriptive R² .851–.982是同题0–10拟合；fixed拟合0–7再预测同题8–10，.766–.968；incremental看新round再更新。不授新题泛化、概率校准或语义安全。保持自身prior可以抵抗错误peer，也会阻止正确纠错；没有独立良性utility对照证明不损协作。

## 3. 决定性反侧与未采用范围

- 评价仅100 CSQA及100 ToolBench多选tool-name，后者G1/G2/G3=34/33/33，省略完整API描述；N=4/6/8、10轮，非真实工具执行/副作用安全。六模型Gemini3Flash/GPT5mini/GPTOSS120B/MiniMaxM2.5/Qwen3235B/Ministral314B；本地vLLM四H100、90%显存，GPTOSS/MiniMax/Qwen使用TP4，Qwen FP8，Ministral单卡，另两API。必要范围未给全Serving版本、采样/完整token长度、batch/concurrency/SLO、完整端到端费用/重复CI，记ND，不补实现/复现。
- Eq18按无攻击时所有benign最终正确的Q+选题；分子只计初始正确又最终错误，但分母为全部benign×|Q+|，不是初始正确者数。两benign仅一初始正确且翻错时，原式1/2而条件翻错率1。C/Table5无攻击行仍有.06/.02等非零，与“同次Q+上最终全正确”不能直接对应；是否另跑/换集合/换定义未说明。此为具体协议桥，不自行猜实现。
- Table3静态MiniMax的None .10→T-S .16反退，反驳§5.4文字“所有模型均下降”。Adaptive/T-W五项 .78/.61/.83/.95/.46；加Sparse后 .36/.08/.35/.15/.17是相对该warmup受攻恢复，但后三项仍高于static None .19/.09/.10。不将static None当匹配adaptive无防御，不采普遍更安全或不损utility。Warmup可被先答对再作恶者利用，稀疏更新并非免费或无条件修复。
- §5.4同时称全局W不可见，又把TRUST_WEIGHT数值注入receiver prompt；可保“owner持有更新”，不能保“所有assigned scores对所有agent不可见”。clip[0,1]、统一.5和accuracy²并不自行保证行和1，理论row-stochastic W与实际prompt speaker score间还缺normalization/zero-row/解析执行桥；不采二者完全等价。
- 主评价稀疏更新消费同题已知GT，不是开放未知任务的无oracle发现；known-GT metadata可能间接透露任务信息。无良性协作收益及端到端代价matched验证，不能授去中心化、跨任务身份信誉或生产安全。

一次具体重开请求仅针对隔离的强主张：给出Eq18/Q+的逐臂选题与随机重复人口、解释Table5无攻击非零；说明speaker score到理论W的归一化和receiver可见性；提供未知GT部署信号及matched benign utility/费用，才重开普遍安全/不损协作声明。此请求不阻止root判断下述已公开接口事实的受限采用；若root认为该桥是本贡献不可分中心，则改为中心暂缓而非降分/EX/虚NC。

## 4. actual sole owner与相邻差额

Owner=`AGENT-MULTI-AGENT`，Ch82 `books/part-07-agent/82-multi-agent.md`。实际完整160–232、428–446已读；81-workflow/83-mcp开头相关交接实际读。现164–168解释correlated consensus、modal/共同bias与外部verifier；170–172是peer-forecast行为测量，不是已知GT校准speaker；174–180是模拟peer影响/反馈可见性。现文未承载“外部owner取得peer前准确性→speaker reputation metadata→冻结与随机再校准”的具体分支，不能仅按主题宣NC。Ch81仍own durable runtime/effect，Ch83仍own协议与授权，不复制其安全章节。

拟插现168共同bias/回退段之后、170 peer-forecast之前，衔接由“共识不是事实”走到“额外可信度信号来源”。两段最小PRE，静态源注另列；是否采用待root。无写锁、actual写入或POST。

## 5. 最小逐字PRE（未采用）

同伴意见已经可能放大共同错误时，一条额外分支不是让模型更强硬，而是把发言者的可检验表现与本轮说服力分开。外部系统持有已知答案的校准题，先取得各Agent在看见peer前的独立回答，再把校准所得信任值作为speaker属性随消息交给receiver，指导下一轮按信任而非简单人数权衡。校准后冻结减少更新状态，却允许先在校准期答对、后来改变行为者利用旧信誉；随机选择后续校准题更新提供了另一条适应路径，但继续消费正确答案、额外调用与状态维护。信任标记只参与意见形成，不让sender取得任务事实、工具权限或最终验收权。<!-- source-family:SF-2026-ARXIV-2603-15809 -->

[受限意见传播与信任对照](https://arxiv.org/html/2603.15809v1)把private prior、自己上一轮意见和邻居意见分开建模，帮助解释坚持原判断与接受纠错的张力；静态线性模型拟合自报概率，不证明LLM执行同一更新，也不把动态信任认证为安全。原对照只覆盖有限多选题和小型讨论网络，部分稀疏更新有反退，已知正确答案在主评价中的校准也不能替代未知任务的验证器。被增强的旧信誉可能强化错误，过度坚持或过滤又可能压掉正确少数与必要纠错；信任来源、可见性、校准人口、变化时间和通信总费用必须分账。外部验证信号不可得、声誉漂移或收益不足时，保留独立候选、较少轮讨论与可信verifier/固定Workflow，不把人数、共识或信任高分当真值。<!-- source-family:SF-2026-ARXIV-2603-15809 -->

拟静态源注：`SF-2026-ARXIV-2603-15809` — primary exact-v1 `https://arxiv.org/html/2603.15809v1`；必要§3–5/Eqs1–18/Tables2–3与E/Eqs19–22、C/Table5/B解释文本；仅支持外部已知GT校准的speaker metadata/冻结与随机再校准分责。Eq18人口、Table3反退、score/W归一化及可见性、unknown-GT/utility/full费用边界隔离，未核代码/未复现，不授开放网络安全。

## 6. 交接状态

root 非准备者 SOURCE/PRE PASS（2026-10-11）：独立实际读 exact-v1 §3.1–3.2/Eqs1–3、§4.1限制、§5协议/Eq18与5.4–5.5/Table3直接反侧；actual Ch82 158–179及427–450/自身现有源注、Ch81/83具体交接已顺读。所采外部已知GT→peer前答题→speaker metadata与冻结/再校准接口可以与理论动态安全、人口/可见性及未知任务外推隔离，六分保持。root窄写原两段（仅中英文空格）和静态源注，等待非writer actualPOST；未计safe/DAY。

原准备停点的“等待root裁决”已由上段实际非准备者结论替代；必要支持、直接反侧与actual差额保留，停止不扩附件，原6分不变。完成状态以以下一次actualPOST为准，不以准备者拟稿或格式校验替代语义核。

## 7. 一次非writer actualPOST

2026-10-11，resume_review17_18是PRE准备者但非Books writer；root实际写入后，本人实际顺读Ch82完整156–192 Peer/Debate前后及完整1354–1364静态本人/邻注。新170/172两段回对§5有效逐字PRE，仅中英文空格规范，命题未变；自身静态源注1364回对原拟注/必要原证准确，无动态人员停点。Actual scoped diff只有本family两段及本人源注，`git diff --check -- books/part-07-agent/82-multi-agent.md`无输出。

共同bias→外部已知GT、peer前独答/speaker metadata与冻结—随机再校准→peer forecast行为测量的前后衔接清楚，没有把校准准确性与预测别人行为的准确性混同；良性纠错/错误少数/旧信誉、未知GT、调用状态与总费用、信任不是事实/权限、FJ拟合非执行/动态安全的限定均保留。新两段不采用Eq18安全率、统一收益或无协作代价，Table3反退和score/W/可见性争议仍在packet/静态注，不靠源注补正文里的正面保证。

一次actualPOST局部正式通过，可告root释放Ch82并归并本family实际I；不再循环改注身份，不授全主张Evidence、Coverage/无遗漏或DAY。等待正式Report46家族及当前停点同步，再由root具名安排完整六部分日级独核。
