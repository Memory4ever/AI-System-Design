# GASP 2603.15957：必要原证 / sole owner / 一段 PRE

作者resume_mar18，仅03-19补03/18完整自然日。2+1+2=5给真实hard goalpost→lemma→lift合成课程接口，具体知识差额必要深入。[exact-v1 HTML](https://arxiv.org/html/2603.15957v1)完整题摘、§3.1–3.4/Algorithm1/Eq4–5、§4/T1、§5/Limitations、A/B、C Tables2–4/直接消融文字和D实际已读；无遍参考文献、全部qualitative示例/图像点或代码/复现。currentabs只有v1和两个ICLR2026workshop标签，无已见具体更正/撤回；日期仅复用本批日级夹证，不把会议标签当先稿、Submitted当公开。

## 支持与关键反侧

同Qwen2.5-Coder7B，teacher/student通常同一参数只roleprompt不同，各阶段更新同weights；不是两个独立oracle。LCB pre2024.08训练601题，2024.10–2025.02 eval216。Hard146先以base、三RLVRseed每50step checkpoint、AZRcheckpoint及额外hard-onlyRL的pass100=0过滤；这是受测搜索预算内未找到成功，不证本质不可解、难题grounding必真实或pretraining无污染。基线hard0是构造性筛选，不能当独立generalization优势。

Teacher看到hard h生成易lemma，用student N10次induction通过率估计、带.3–.7及峰.5 reward；acceptedlemma单独给teacher生成lift，原h不再提供，lift带.1–.5及峰.1。两阶段都训练teacher，同参数身份随阶段改变，必须保存各生成/判分checkpoint。Difficulty axis随机I/O或f，lift同axis，但作者不惩罚I/O退回f。Validity reject format/unsafe/nondeterministic，并文本/code embedding相似> .95拒绝近邻；具体embedding身份未披露，不授语义多样性或根除modecollapse。全局buffer均值dissimilarity是另一个诊断非threshold本体；原文§5明确未验证lemma/lift真实导向hard目标，常借surface metaphor/加约束，不采精确能力分解或必连通课程证明。Acceptedproposal的5 I/O pairs仅2公开/3private，运行generated程序一致不认证真实goalpost语义。

Solver按随机induction/deduction/abduction用可运行结果reward训练，teacher目标只是短程可解率，不是SOAR式在原hard上短训前后的实际进步。GASP+real另加原LCB训练集更新，含hard h；GASP不直接RL hard答案但teacher已读取原hard内容，不能称zero realdata或无目标接触。

T1 selected best LCBpass20：GASP18.26±.68/pass1、33.69±.28/pass20；AZR17.49/31.15单公开checkpoint；RealRL18.91±1.40/33.10±.12。+2.54是百分点而非相对2.5%，GASPpass1低RealRL；T3 greedy HumanEval79.67低AZR83.54及base79.88，不采全能力无退化。三seed为作者本RL，AZR单seed且各方用评测benchmark选最好checkpoint，独立selection/test身份未分离，不以时间split自行授未适配eval。不同passk/greedy及testpopulation分开，不授生产质量。

Hard突破按任checkpoint pass100>0、跨seedunion：GASP6/3/3 union11；间歇不稳定，不等最终11题稳定可靠。C T4 one-step medium同11、hard2；no-reject14但190steps对GASP48、同steprange仅3，是机会/费用混杂不能一般推集中训练更好。NoI/O pass1某选择19.36高GASP19.10而目标hard4，非两轴各指标必优；多样性与特定hard解题权衡保留。GASP+Realunion10低11，更多真实数据非所有目标单调。

D b64/LR1e−6、trainT1/eval.6、4H100train/1H100eval、vLLM/verl；RLVRGRPO500step/n8/3seed，GASP Task-RelativeREINFORCE++约50globalstep/eval2/noReject约200/eval10，AZR公开约350。Globalstep含多个rejection生成直到M/maxattempts及分阶段更新，不等相同训练次数/FLOPs；预筛三RL+checkpoint×pass100、teacher和N10solve、全历史buffer距离、执行及模型更新均计费。Algwhile本身无maxattempts，D述有但具体值/failure返回未披露；需工程单独有界失败退路而不补造实现。完整precision/runtime版本/optimizer/输出token预算、全部墙钟/拒绝率与部署I/O/batch/concurrency/SLO ND；有三seed/std不冒已经固定全費公平对照。

## actual owner与具体差额

实际Ch27 1080–1155并定点1117–1138完整quality/online control→SOAR grounded generator→optimizer-aware selector，Ch26/28首18行交接及Ch33训练objective入口已读。本日Books背景/学习方法/写法与ROADMAP实际加载。soleTRAIN-DATA，现1127–1129有真实hard→课程→student短训→hard实际进步reward/reset/promotion与全費，但不承载hard仅作contentcondition、lemma→无原hard的lift、passrateproxy准入并不认证目标迁移的具体替代接口。它不是重复SOAR名称，不虚NC；拟1129后/原OPUS前一段，trainer仍ownpolicy/objective不复制Ch33归一公式。Source/PRE待非preparer及root锁，未写未safe。

### 逐字一段 PRE

若反复短训 student 再测真实进步的内环费用过高，也可只让真实难题引导课程内容，再用当前可解率筛选 stepping stones。一条[受限编码课程分支](https://arxiv.org/html/2603.15957v1)让 teacher 先读取受测预算内未解的目标题生成较易 lemma，再仅由 accepted lemma 生成较难 lift，不把原目标继续交给第二阶段；teacher 与 solver 可以共享参数、按不同角色和阶段更新。这用两级 proposal 与可解率带替代直接的目标进步 reward，却没有证明生成题保留原算法目标或真正通向它；代码可运行、测试通过和 embedding 新颖度分别只是有限准入信号。须保存目标池的失败筛选预算、各阶段 checkpoint、问题/程序/测试和接纳版本，并独立检查未参与选择的迁移任务与最终稳定解题，而不是把跨 checkpoint 的一次命中当持久能力。拒绝重试、solver 探测、全局 buffer 比较及联合训练都付费，更多样性或真实数据也未让所有切片更好；目标错位、预算超限或课程退化时，保留专家课程、冻结 mixture、直接 real-data RL，或愿意支付更贵内环的真实进步反馈。<!-- source-family:SF-2026-ARXIV-2603-15957 -->

### 静态来源注

- `SF-2026-ARXIV-2603-15957` — [GASP exact-v1](https://arxiv.org/html/2603.15957v1)必要§3–5/Alg1/T1、A/B/C Tables2–4与D；仅hard内容引导lemma→lift及可解率筛选接口，shared-role身份/目标对齐未核、pass100跨seed/checkpoint联合与test择优、任务反退和全部筛选/生成費保留。不授本质难度、语义新颖/稳定目标突破、zero realdata或全费用性能保证；未核图像全部点/代码或复现。
