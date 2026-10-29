# 12510 / 13045 / 12543 必要核心与具体未决

本17补03/16，三项完整AB独核/日级夹证已保留；不是新发现波。作者实际以下exact-v1必要核心与反侧，尚未Source/Books独核，不计安全处置；中心疑点不得当普通未读或以难度降分。artifact未核/未复现。

## 12510 Q-DIG：安全搜索的competence边界

[exact-v1](https://arxiv.org/html/2603.12510v1)实际§III–V/L38–153、140–239必要。J=p(success)(1-p)最大在.5，找有时成功/有时失败而不是maxfailure；8种style archive（5既有+3qual）、gpt4o2024-08-06同时mutator/stylejudge，5×10提案以SBERT diversity选组，rollout估p、每cell留maxvariance。当前机制未提供严格semantic-equivalence verifier；conditioning原instruction/visualobs不认证同任务语义。Simpler5/LIBEROGoal10、3/6/12iterations，QDIG/ERT相同VLM/预算但目标不同；4完整随机runs的SE不是所有policy训练uncertainty。50demos每instruction关联8augment+原，10prompt8train2test，50episodes/taskinstruction，FT10k或20k。TableII原指令成功OpenVLA97.4→93.8/GR00T77→64.8；ERT与Rephrase部分avg优于QDIG。Simpler全5 QDIG52.2低于Rephrase60.5，去掉bad open-drawer后才63.6。BLEU不是taskfidelity。人类40rank支持偏好，但Likert vsRephrase非显著；Kinova两task/10trials小组及五fold仅promptfold不授安全。rollouts/stylejudge/VLM+FT总成本不可隐藏，hardware/precision/batch/concurrency/SLO Not Disclosed。

actualCh26 955–982持续外prompt→安全承接已有wholetrajectory/effect，不承载variance目标+stylearchive区别，拟唯一MULTIMODAL-EMBODIED-VLA，2+2+2=6安全反侧深入。拟外prompt两段后、原12978绑定前两段（待PRE）：

若目标是构造仍处在policy能力边缘的训练样本，只最大化失败率可能选到普遍不会做或语义已失真的指令。另一分支按改写style维护archive，以多次环境rollout估计成功率，优先保留成功/失败均出现的改写；p(1-p)的目标把搜索推向中间成功率，而非最强失败。原instruction与初始visual context可约束提案，但没有独立语义验收时，style分类和embedding diversity都不能证明改写仍是同一任务。<!-- source-family:SF-2026-ARXIV-2603-12510 -->

[Q-DIG的局部对照](https://arxiv.org/html/2603.12510v1)支持这一可比较搜索分支，不证明augment必胜maxfailure或普通rephrase；原指令utility及部分任务平均也会反退。每次提案、style判分、重置rollout与后续训练均付费，有限style/heldout prompt不覆盖未知攻击。样本语义或原任务质量不能独立核对时，保留普通rephrase、maxfailure红队与原指令对照，并由真实outcome和独立controller决定是否允许physical effect，不让成功率居中批准安全。<!-- source-family:SF-2026-ARXIV-2603-12510 -->

## 13045 WALAR：中心reward身份疑点（待独核）

恢复纠错（resume_review17_18实际原证）：下段初笔记把Eq6误记为QE/WA均采用y′；实际是r_qe(x,y)+αr_wa(x,y′)，QE明确原y。此错误不能作中心隔离依据，保留初误读与修正以便复查。reader正定点核实际reward代码中的WA cardinality/各输入映射；尚未获终态判定，不提前计safe或据错误EX。

[exact-v1](https://arxiv.org/html/2603.13045v1)实际§3–5关键L73–174、205–245。MetricX24HybridXXL BF16 source-only输入source/hyp；Qwen2.5.5B特定stress用hyp作reference触发Hybrid而非所有大模型实验。BGE-M3layer24对xy/yx softmax阈值1e-3取pair集合WA；Eq4 P=|WA|/n,R=|WA|/m。作者称F1coverage，但未说明unique-token/one-to-one：作者本次分析m=n=2/equalembedding使4pairs超过两个token，P=R=2/F1=2（不是原文实验结论）。L129文字MaskLID删codeswitch后y′，language公式仍Langdetect(y)，Eq6 QE与WA采用y′；实际mask/score输入未明确。请求一次实际alignment cardinality/归一化及各reward原/filtered输入映射，未澄清前不认证中心rewardrecipe/完整翻译语义覆盖，不绕争议将普通rewardhacking重写入Books。

5A6000 OpenRLHF、batch1024micro16group8/T1/KL.01/clip.2、模型Qwen3-8Bnonthink/LLaMAX3/Translategemma4B；W-SFT额外32sample pseudo数据预算不等RL。Table3语言wrongratio WALAR4.44劣于QE+Lang3.96，xCOMET QE+Lang优而BLEU WALAR优；长度接近reference不证明语义完整。Gemini3Flash reference judge非humanGT，GlotLID reward/eval同源。seed/CI、inferencebatch/concurrency/tailSLO未披露。潜力原机制评分不因争议改动，拟中心隔离需reader回Eq4–6与原文输入identity后裁决；未计完成。

## 12543 CALF：环境时钟桥（待独核）

[exact-v1](https://arxiv.org/html/2603.12543v1)实际§3–6/L110–314及§7.3/L317–326；定点find timeout无命中、step()/asynchronous只列方法/既有背景。NetworkShim按packet delay/drop并timestamp，same code local/sim/network/RaspberryPi+Desktop；环境仍CartPole/Minigrid simulated，非physicalrobot。10seed×50episode，PPO/同temporalcontext；synthetic WiFiN30±10/2%与D80±40/10%，trace empirical分布不授joint burst/reorder。根本必要桥：§3.2只称step变网络请求，未说明等待/drop时EnvService是否固定wallclock继续推进、hold/retry/default action/timeout及MDPstep映射；严格同步Gym若暂停等待，纯ms延迟本身不产生stale-state动作差。此为本次条件分析，不断言实现必错；需要实际clock/失包动作消费记录或最小执行trace才能认证因果部署gap。

§6.2 max(0,N(0,40²))已有正均值，非mean-matched变量隔离；Table4固定50ms218 vsTable6同标275也须配置对应，不能全归于jitter。两rule-managed independently-trained units不是联合最优图；1kstep latency p95 152.7ms不是worst-case/SLO保证。§7.3明模拟环境/LAN/singleagent/offline/两unit限制，不补clock。single exact请求environment持续推进与hold/retry语义、Table4/6固定条件对应（不是泛求全部code），必要原证缺桥前中央robustness及Books暂缓待独核；不以小模型/通用RL题义关闭，不因未审缩池。precision/并发/硬实时SLO未披露，未复现。
