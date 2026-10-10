# 2603.09803 — demonstration-conditioned RL与Evidence Gain依赖边界（必要Source/date/具体NC通过）

[Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision via In-Context Reinforcement Learning exact-v1](https://arxiv.org/html/2603.09803v1)。第二包完整题摘及current信号root准入通过。作者实际完整§3–5/必要§2定义及验证、AppE.1–E.3全部、B.1–B.4/C.2/C.3必要文字，Table1/2；不读无关所有baseline推导、全部曲线像素或代码。第一次误section Ax5明确NOT FOUND，已恢复正确A5完整，不能用首次未取到作为读完。currentv2 Jun03、ACL2026 accepted与题摘表述改变不单独触发本窗重要修订，不回填后版指标，无已见withdraw/纠错；未出现必要更早先稿信号，不扫会议史。

raw批2 DOI owning arxiv.content/findable registeredMar11UTC02:22:18已经可发现上界与official noadvance/announcement最早Mar11BJT08下界同BJT日，SubmittedMar10UTC15:33:07只约束批次；注册本身不作公开。待root必要日期核。

2+1+2=5标准；最终正确不等trace质量→policy给另题参考解的似然增量作教学proxy，再在rollout前放一个专家demo并照原DAPO/verifier更新→条件分布变化与无demo能力/quality/evidence理论须分责。成熟ICL/DAPO不独加分，只采用有限条件化实验与理论边界，拟Ch33具体已有覆盖；不正面采用自动高质量重权定律。

## 机制、证据与中心强claim隔离

§2 Eq1 Delta=E_e[log pi(e_r|q,r,e_q)−log pi(e_r|e_q)]；teacher参考解来自R1-0528正确过滤后</think>部分，不等无外部数据/无teacher。§4/B.1 train28k、demo1082、真正只供correlation的E0=100不同集合；demo原称validation但实际训练条件，不冒称独立heldout用途。B.1人工验teacher质量，B.4八rubric/DSV3.2整体judge、C.2仅100 correct traces/fourhuman Spearman .65–.83属于这个条件筛选人口，非所有错误trace或客观逻辑认证。自动Delta明确诊断昂贵：§3约12k×100refs/H80080h，训练以随机demo input替代逐rollout显式Delta计算。

E.1 A1/A2是模型对裸question context不变的假设，不由两个数据样本独立自动推出。E.2 Eq6必须来自同一joint条件分布；autoregressive换文本排列的两个调用不能无条件当同一joint的Bayes反向。作者1.5B/100×100的相对logprob变化delta.0384只是一种有限诊断；相对长trace总log小，不保证每条likelihood ratio近1或各模型通用。保留原条件结果，不把此写成全部Bayes无效。

即假设E.2 identity确成立，E.3真正w=E_e exp(Delta_e)，Jensen只授w≥exp(E Delta_e)，不授两trace按mean Delta单调排序。必要反侧：uniform3demo、base两trace各.5，likelihood ratios A=(.01,1.3,1.9)，B=(1.99,.7,.1)，每demo两ratio相加2故归一相容；wA=1.07>wB=.93，但DeltaA≈−1.23365<DeltaB≈−.65704。这些ratio可由每demo参考事件base probability.1、conditional分别.1×ratio构造，所有probability在[0,1]，保持同joint与裸题不变；它不否定Jensen下界，只否定无variance条件下的排序。shell实际算mean/log和pair normalization，不声称模型实验复现。

E.3 Taylor variance项需要controlled remainder/高阶尾，不由finitevariance本身取得uniform little-o；E.4作者近常数variance offset来自相关.855/.822的empirical observation，相关高不证明统一c。该反例不满足“近常数variance”的额外近似条件，不能冒称反驳所有条件化E.4或所有ICL收益。theta-dependent w且clipped/groupnormalized DAPO也不由expectation重写自动等于固定reward零示例训练梯度。仅中心普遍implicit quality/自动更好reasoning因果隔离；实际demo-conditioned训练和有限zero-shot结果可独立保留。

Table1 DSdistill1.5B/7B数学六任务，zero-shot eval avg@4(MATH500/Olympiad)/avg@32其他；有限均值ICDAPO比DAPO53.9→56.4、65.3→67.8，不采跨scale速度，作者32vs128GPU配置不可比。7B AIME25 49.8<CEGPPO50.3反侧；step477.2vs459.6、315.6vs303.1约4%费用不包含teacher制备/校验/诊断/总训练。B.2每10step存checkpoint按AIME25best选所有结果，AIME25不是独立heldout选择评分，zero-shot不独证理论质量重权。B.3只correct finalanswer进入Delta/judge，动态条件分母与训练query不能由E0 disjoint叫无偏全质量。C.3同1082题改teacherR1/V3.1同时改变风格、长度/概率，不是只quality随机干预；更好点均值不识别Delta唯一机制，未核完整seed/CI/同质量预算。

教师采样/正确过滤/人工核、demo prefill、全部rollout与DAPO更新、checkpoint选择及额外quality诊断/外部judge均付费；完整hardware/precision/trainbudget/SLO Not Disclosed，32/128GPU只按paper范围。不能将无训练PRM改写为无外部标注/无成本/无proxy。可靠binary verifier继续有权判断终态，教学utility不作true reasoning证书。

## 实际owner：拟具体已有覆盖而非强加新正文

唯一TRAIN-GRPO。作者实际Ch33 401–423完整（iid coverage→POPE conditional/unguided→PrefixRL理论/实践不同→PACE）、998–1042完整（不能由GRPO断普遍推理→demo-rich至zero-demo及heldout verification→scaffold provenance），Ch32/34开篇交接；另实际2513–2536 credit条件/critic分责与Ch31 275–296只作reward owner交接。

413/415已有prompt conditioning不等原prompt纯on-policy、guided成功不代签unguided能力、teacher筛选及预算；417–419已有存在共同globaloptimum不等梯度/有限训练迁移，并要求同质量成本；1012–1042明确完整demonstration-rich rollout的退火和独立no-scaffold验收，不是假设短prefix覆盖全部demo。所采有限“rollout条件变化与部署无示例能力/完整teacher费用分责”的边界已有具体正文承载，NC不采用E2/E4强定律或新安全阈值。

root非作者实际官方v1§2–5、B.2/B.4/C.2/C.3/E.2/E.3、原batch2日期及Ch33 401–424/998–1043，必要Source/date/具体NC通过，5分不改。独立有限反例：base三trace各1/3、两demo等概率，likelihood ratios A=(.1,1.9)、B=(.5,.5)、C=(2.4,.6)，每demo归一sum/3=1。wA=1>wB=.5而meanDeltaA≈−.830366<meanDeltaB≈−.693147，logw−Delta分别.830366/0；因此平均Delta高不无条件对应平均ratio高，相关不证统一c/全排序。这不否定同joint条件化Bayes恒等式或额外variance条件的近似。有限demonstration→zero-demo和完整teacher费用由既有具体正文承载，无Books新写，不授DAY/复现。
