# VEPO19152：温度比、熵信用与稳定性桥的必要中心裁提案

resume_mar18 sole准备，仅03-21补BJT03-20；已有完整exact-v1题摘/具体增量准入独校有效。原有统一entropy bonus/组内信用→原文把结构资格筛样、同题中心/本地microbatch尺度、position-decayed detached entropy信用与可微entropy bonus组合→若成立，会改变低资源翻译训练中探索/结构约束的解释。按拟新跨采样—更新接口2+2+2=6；不是因低资源语言/负面结果排除，不给成熟tokenizer或DAPO旧原则加分。必要中心反侧已足，提案争议终态，不自授safe/Books/NC/EX；交root非preparer裁。

## 身份与日期

实际[officialabs/v1](https://arxiv.org/abs/2603.19152v1)完整AB/header/history：十一作者、onlyv1、comment Conference submission，无明确撤回/纠错/accepted先公开事件。实际DataCite arXiv-issued DOI findable/version1原字段：Submitted2026-03-19T17:10:29Z；v1Updated2026-03-20T01:16:30Z；Available仅2026-03；created2026-03-20T02:29:51Z、registered52Z。沿本批BJT03-20公告/注册夹证限定日级归属，不补公告精确时刻或声称互联网无先稿。

## 最低充分原证

实际[exact-v1](https://arxiv.org/html/2603.19152v1) §3/Equation1和Algorithm1（L99–177）、§4.1–4.4/Table1–3（L179–254）、§5.1–5.4（L257–288），必要A.2/Eqs2–6、A.4/Eqs7–11（L367–429、455–509）和A.5预算/评价（511–521）。不遍90语言方向附件、所有案例图、代码或版本diff；未复现。

原方法先扩tokenizer/CPT/SFT，再采K候选、按结构reward筛选top-G；同题中心，本地microbatch std缩放，熵停止梯度后按1+alpha H gamma^t乘到signed advantage，再另加可微entropy bonus。长度、格式、目标语言/混用资格并不等语义真值；LID为分类模型confidence判定而非不可错的确定性语言证明。不同prefix熵/组有效长度、筛样人口、裁剪/ratio与全词表entropy都必须参与配方解释。

## 直接中心反侧：不替作者补recipe

1. 正文ratio定义使用两个归一化温度策略之比，但A.4 Eq10写exp((log pi_current−log pi_old)/tau)，遗漏两个温度归一常数比。自行实际算old=(.8,.2)、current=(.5,.5)、tau=2：归一化温度后首token真正ratio=.75；Eq10=.790569，old温度分布下该错误ratio期望1.054093非1。只指出论文closed-form/martingale/unbiased桥不成立，不声称未读实现一定如此；§3正常ratio定义本身不否认这个公式冲突。top-G资格过滤又改变实际sampling人口，单tokenratio一致也不足以恢复完整trajectory或筛样目标无偏。

2. A.4 Eq7后的每位置sum advantage=0并非无条件：组内中心后的[-1,1]，不同prefix H=[.1,.6]、alpha gamma^t=1，乘系数后sum=.5。若H对全组确为同一scalar，零和才可保留；正文H不带索引、A.4又称local token entropy/不同prefix分布，不能自行择共同H修理论。正系数只改变已有正负更新幅度，不保证高熵增加或late token语义精确；独立可微entropy正则也没有披露硬entropy下界、普遍Fisher条件数或无collapse证明。

3. Eq1 asymmetric bounds、Alg1对称epsilon=.2与A.4 epsilon_low>epsilon_high但典型(.20,.28)互相不一致。不能择其中一个作为实现配方，或由所谓downward sensitivity推出正确方向。A.4 top20%词表entropy不等全分布entropy，尾部忽略/80%开销减少不授端到端低费或梯度精确。

4. Table1单项合格率97.8/99.2/92.15/92.3与Overall95.3不可能同时表示四项全部联合满足（joint最多92.15）；近似四项平均95.3625可能解释但作者未定义，不自补口径。训练资格过滤也不认证部署hard constraints。Qwen-MT-Plus length99.8、Hunyuan mixing96.2仍高于本项，不能采所有约束优越或语义不损。

## 评价人口、局部支持与代价

Table2作者完整pipeline相对SFT average24.9/.859/50.9 vs24.3/.849/48.3支持作者有限综合对照，不识别position-H、ratio、筛样或microbatch尺度的各自因果；CPT/tokenizer与训练阶段不混为新RL作用。Table3 CMMLU63.2低于Qwen2.5baseline64.1，不能所有能力无退步；T2/T3包含不同parameter规模，§4.4的7B同规模文字不能统摄全部表项。18 runs是6算法×3KL配置，不披露独立训练seed重复。人类blind评级0–3/高质量>=2不等pairwise joint偏好，人数/样本/CI必要人口未全披露，不授所有模型人类胜出。

A.5报告CPT200B tokens、RL60k steps/batch128并称RL基线同budget，但硬件/precision/rolloutK与G/完整长度、采样tau、并发SLO与端到端通信/筛样/entropy开销未充分披露。token压缩率不是实测推理latency/throughput，全RM/资格检测/弃样/训练费用保留。不将single idiom logit案例当paraphrastic manifold因果恢复，未给全部constraint和翻译质量独立一致的证据。

## Actual owner与终态提案

sole `TRAIN-GRPO`/[Ch33](../../../../../books/part-04-training-system/33-grpo.md)：实际完整96–116、172–217、2186–2300与Ch32/34开篇顺读。现有111及截断分支116已承载同题mean/batch尺度；213/215承载动态entropy相关clip，2274–2292已有entropy-gated signed outcome幅度与logical-progress bucket，但没有新增绝对position-decayed detached-H乘子和可微entropy两路的本项具体配方。因此不靠主题相似判NC、不为缺名称造diff。这个局部形式可描述为一种替代提案，但本项中心是其无偏/无collapse/结构保证；没有独立局部消融且actualratio/组人口/entropy身份不闭合，不把一般“早探索晚收束”原则单抽进Books来绕过中心。本轮提案6分争议终态、无Books/正面Evidence/Coverage，等待非preparer限定裁决。

一次精确请求同family修订原ratio/归一式、H索引/共同或逐prefix口径和中心化、实际clip/过滤目标与对照，并定义constraint Overall分母/联合门和支持稳定性归因的匹配预算局部证据；可接受公开精确算法/作者勘误或对应原实验配置。收到仅定点重开§3/Eq1/Alg1、A.4/Eqs7–11/T1与actualCh33差额，不扩全作者/venue/90方向或新发现。未到不采用宣传强claim，普通其他可读项继续；这不是访问受阻。

## root 非准备者限定中心复核

2026-10-12 root实际独立打开exact-v1 §3/Eq1、Alg1、A.4/Eqs7–11与Table1/§4.2–4.3；复用未变化的官方身份/日期依据，不遍无关附件。实际重算归一化温度ratio为0.75，省略归一常数的式子为0.790569，错误式在old温度分布下期望1.054093；signed中心化后乘不同prefix熵系数也不再保证零和。Table1的95.3不认证四项联合通过。实际Ch33组内中心/共享尺度段96–116与entropy-gated signed-credit段2270–2299已读，现有机制不能替该新recipe补齐身份与证明。限定中心争议终态PASS：保留原6分、争议及精确重开条件，不进入Books、不作正面Evidence/Coverage，不把一般探索原则另写作绕过争议的成果。未核实现或复现，未授日级DAY。
