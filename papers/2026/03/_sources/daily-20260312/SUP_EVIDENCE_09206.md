# 2603.09206 — MM-Zero必要Source与Ch27差额（必要Source/PRE/actualPOST通过）

[MM-Zero exact-v1](https://arxiv.org/html/2603.09206v1)。第二包root完整AB准入通过。作者实际§2完整必要机制、§3/4完整含Tables1–3、§6、App0.B/0.C文字与Tables4–5；不授全部图像、全部prompt或代码复现。current仍v1/comment空，无已见纠错/accepted先稿，不扩无关附件。必要题名/公开原字段是SUP_EXACT_BATCH2.json：Mar10UTC05:23:26提交，owning arxiv.content/findable DOI registeredMar11UTC02:07:57上界与official no-advance/deadline最早Mar11BJT08下界同日夹证03-11；不用Submitted/Updated/registered单独public，待root实核。

2+2+2=6：固定seed-image限定视觉任务分布→提案/代码渲染/solver三角色轮训且execution/可解性/难度/类型多样性分账→数据生成权限与视觉监督代理的稳定条件分支；跨提案、可执行产物与训练角色，但成熟GRPO/majority自身不加创新分。Ch27具体渲染监督gap定点深入。暂不采用zero-information/无预训练数据/AGI/全模型scale结论。

## 方法、奖励与直接边界

§2.2同pretrained VLM初始化三个独立角色，轮流GRPO，训练当前角色时另两个冻结。proposer输出caption/easyQ/easyAnswer/hardQ；coder SVG经CairoSVG转PNG，solver先easyQA与意图答案比较作render fidelity proxy，hardQA以自身majority vote生成silver label。没有额外seed-image与人工hardgold，不等模型无预训练知识、无topic/prompt、无合成产物/标签或零数据训练。coder最近proposer约4K产物训练；solver只成功render样本后按easy准确>.5、hard一致.27～.75过滤，coder另只留4render成功率.25～.75。

§2.4 proposer execution失败0贡献；easy solvability capped.5，hard self-consistency c用min(c,1−c)作Goldilocks难度，不是未知gold accuracy或能力边界真值。类型比例惩罚和caption/easy/hard BLEU clustering奖励是batch代理，不签语义多样性/跨轮历史覆盖。easy意图answer来自同源proposer，solver一致不证明图忠实原caption；hard majority可能一致错误。Eq8成功集合I空时分母未定义，Eq11 coder Rdiff写{0,1}却“identical”Eq7[0,.5]，不授完整可执行reward规格；独立支持的stage分账机制不因局部符号错误全部退出。§2.6 hardaccuracy实际和silver多数一致＋.1format，不是规则gold verifier，不能把§2.1 RLVR介绍套进实际标注真值。

App0.C只SVG variant：CairoSVG→PNG、每snippet30秒timeout、ProcessPool并行，aspect≤100、dimension≤16384等校验；execution/syntax/image尺寸成功不认证图语义或生成代码sandbox安全。App0.B fullfinetuning/visiontower trainable、Qwen8B约8.77B参数，不是LoRA/freezing全部基座。训练/过滤/render与额外角色驻留费用未形成完整端到端预算。

## 评价、冲突与停止点

§3八RTX6000/Pro96GB、Qwen3VL4B/8B、MiMo7B，每role20steps/共60，十视觉/数学/幻觉数据、Qwen2.5-14B judge；不是独立人工事实审计。Table1 overallavg4B50.2→53.4但iter1 53.5高于iter2 52.8，8B50.7→54.1，MiMo50.9→56.0但iter2 56.1更高，不能采用所有迭代/所有任务单调：4Biter2Hallusion72.3→71.5、MMSI26.1→25.9；8Biter3MathVista67.7→67.2。多模型cross只是有限人口，不是大模型scale律；§6明确未测38B计算太贵。

§3.2把54.1称visualmath均分与4pp，Table1实际为全部十任务overallavg，50.7→54.1是3.4pp；Table2 Iter5overall54.5，正文56.6冲突。不采用上述争议aggregate或扩展训练上限承诺。App0.B脚本TRAIN_STEPS10 vs正文20/role、GPU_MEM80/80GB per-role vs正文96GB、solver rollout5 vsper-role8不统一填造；保留具体配置冲突，不授完整复现配方。maxprompt4096P/CG/8192S，maxresp2048/4096/4096、P/CG/S用3/4/8GPU，LR1e−6、wd1e−2、temp1/.7/1、full训练已披露；精度、完整generated/filtered人口、totalwalltime/费用、seed/CI、独立污染/heldout检查、productionSLO Not Disclosed。

§4 removecap与removecontent diversity，Tables3base50.3不等主Table1 8Bbase50.7，且正文引用50.2混4B；不把52.3对54.1差额当唯一cap因果/等budget效果。无需删局部支持：withoutdiversity同组51.7→51.3→49.4低于其base50.3，说明更多轮次不保质量；author随机10render/caption每轮定点观察answer直接注入图、histogram窄类型shortcut，支持检查该循环的有限失败面，不授所有checkpoint或独立攻击验证。无相同总生成/训练budget双角色/三角色消融，不将全部benchmark增益唯一归coder新role。

## actual owner差额与逐字PRE

唯一owner `TRAIN-DATA`，[Ch27](../../../../books/part-04-training-system/27-data.md)。actual339–359完整synthetic/specification局部（seed联合结构→约束grader→strategy→graph→R-Diverse历史）及前后trajectory两段实际读；开篇/Ch26与28开篇交接读。现343渲染lineage、357R-Diverse跨轮bank/majority不签真值分别覆盖部分边界，但不承载“caption意图→coder视觉产物→easy-fidelity/hard-consensus监督轮训”的数据生成分权。拟R-Diverse段后/从已执行轨迹合成Agent任务前两段，保留历史去重/真实轨迹旧分支。

视觉 self-play 还须说明谁提供可见图像，而不只让两个模型轮流出题和答题。固定真实图像作为种子，来源可审计且分布明确；要越出这套图像分布，可将文本场景提案交给单独 coder 渲染，再让 solver 消费实际图像。训练一个角色时冻结其余角色，并分别保留 caption、代码、渲染结果、easy question 的意图答案与 hard question 的多数伪标签，使执行失败、视觉表达失配和解题困难不被同一个成功标签合并。[必要三角色机制](https://arxiv.org/html/2603.09206v1#S2)不需要额外种子图，但仍依赖预训练模型、任务提示和生成监督；“零外部 seed data”不是零知识或零训练数据。<!-- source-family:SF-2026-ARXIV-2603-09206 -->

代码可渲染只是第一道 gate：easy-answer 一致提供图像忠实度代理，hard-answer 多数提供训练标签，却都不等独立正确性。若只奖励可解性，生成器可能把答案直接画进图；若只保易渲染类型，跨轮题目会收缩，更多训练也可能降低独立 benchmark 分数。[有限 reward 消融](https://arxiv.org/html/2603.09206v1#S4)支持对可解性、难度和类型覆盖分账，不证明三角色优于等总预算的所有旧方案，也不弥合主表与消融基线/配置的披露冲突。多角色训练、候选渲染、过滤和 judge 都要付费；应以独立语义/任务切片检验生成产物与学生，不让执行通过或同源多数自行认证监督。视觉表达、代理或净收益失准时，保留真实 seed images、人工/独立 verified 数据与原有 mixture，历史题目覆盖仍沿前述 bank 分支管理。<!-- source-family:SF-2026-ARXIV-2603-09206 -->

拟本人末注：SF-2026-ARXIV-2603-09206，Daily2026-03-12补查，v1§2–4/6/App0B–C与Tables1–5，2+2+2=6；coder渲染产物/easy fidelity/hard consensus分权gap深入。零外部seed非零先验，多数/LLMjudge非gold、代码执行非语义/安全，shortcut/类型塌缩/任务退步及全部角色费用近正文；aggregate与步数/GPU/rollout/ablationbase冲突不补造统一协议。必要Source/日期/逐字PRE与actualPOST待root实际核，不授代码/复现或DAY。

实际状态：root非作者实核必要官方v1§2–4/6、Tables1–3与原日期夹证字段、Ch27具体owner局部及Ch26/28交接，必要Source/PRE通过后实际写Ch27新359/361两段及本人1620末注。非writer supplement_20260312实际顺读329–387完整局部和本人注，并重新直接读官方§2–4/6全部必要文字、Tables1–3/Eq4–14回对，actualPOST通过。root本轮不授全部AppB/C/代码，未统一披露冲突或授实现/复现、全训练预算、生产SLO或日级验收。
