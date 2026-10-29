# 首批必要 Source：作者审阅与边界

日期链见SUP_DATE_RULE及真实DOI投影；root已实际完整题摘独核潜力，不等于下面Source通过。未写Books。

## DRKL 2604.00223v1：拟2+2+3=7

[精确v1](https://arxiv.org/html/2604.00223v1) §4.2–4.3、§5.1–5.3已读。拆分RKL为binary target项及(1-q_m)条件non-target KL；后者对target logit梯度为−q_m(1−q_m)D_KL(qhat||phat)。仅target概率相等、tail仍不等时非零，**不是全分布q=p时仍非零**。固定gamma取代1-q_m使tail项不再给target梯度，仍保留binary RKL。Dolly14k、512token、GPT2/OPT三对、相同batch/epoch、五seed ROUGE-L与diversity支持局部权衡；gamma过大有退化。未证明RKL全局最优被改或任何现代架构均获益。实际改变的是目标/非目标监督耦合的解释与选择，非词表大小单因果。

## Shuffle 2604.00260v1：拟2+2+3=7

[精确v1](https://arxiv.org/html/2604.00260v1) §3.1–3.4、§4和D.2已读。equal blocks且within-block方差正时block平均gradient方差较individual低，但不同prefix单位，不冒称等样本预算任意block必更优。二阶可微、gradient有界、gradient/Hessian Lipschitz下，同一起点分别运行正/反排列再平均epoch map，二阶order项独立排列，固定n小步长order sensitivity为O(gamma³ n³)。**理论是两map平均，不是仅下一epoch倒序**；APR实验每epoch单排列、loss-ratio分块与每3epoch翻转/交错，不能把其收益当对称平均定理的实现证明。小型凸/MLP局部实验，大规模Adam/非平稳数据未证。可保留条件化数据顺序机制，不泛化任意LLM训练。

## In-training Probe 2604.01025v1：拟2+2+2=6

[精确v1](https://arxiv.org/html/2604.01025v1) §3.2–3.5、§4.1–4.5已读。MC生成成功率作回归标签；submodel decoder逐层注入base hidden states，再sigmoid估计prompt成功率。OLMo3-7B多个pre/post checkpoint与任务切分；早期→后期transfer优于LoRA，但table3有AUROC0.7346等，**并非每格>0.75**。AUROC/MSE不是概率校准保证，更非release权限。初始生成标签+probe训练成本需摊销；base每checkpoint0.78h→0.05h不含初始化。16层比32层稍降，8层明显降。只支持该训练轨迹的低成本监测分支，不能取代独立生成式验证。

## AAC 2604.00304v1：决定准入的窄读，拟贡献前EX

[精确v1](https://arxiv.org/html/2604.00304v1) §4.1、§5、§6 table4已读。actor提出provisional action，critic approve/revise verbal反馈进context，actor再生成之后执行；delta0直执行。单trajectory仍有内部regeneration，不是不可修改action或硬权限gate。critic训练来自成功且nontrivial intervention轨迹SFT；Qwen族内部larger较好，但跨family容量非单调。root实际独读primary4.1/5通过窄EX：成熟verbal critique+actor revision/成功干预轨迹SFT，无新增机制/失效条件；不是要求所有贡献都有hard gate，也不把one-shot改写state作为准入。无新信息则停止，不按deep-read成本缩池。

## Secure Forgetting 2604.00430v1：具名原材料复用，拟EX

相同精确v1的原实际Source见 `../daily-20260402/v3-reopen-notes.md` 189–191；本轮root实际独读III/IV/V与TableX核修正：DPO conversion+memory删除+prompt behavior，非base weights删除；Bradley–Terry+linear features/covariance条件，GridWorld/AlfWorld/HotPotQA有限observer。**旧笔记0.88→0.71与0.68→0.60是Code baseline，不归因NL新方法**；NL本表utility为0.85→0.83与0.71→0.68的小退。仅本packet修正，不改冻结别日旧正文。root接受窄preclosure：成熟DPO prompt优化/目标分层无新删除合同，保finite observer与理论假设；不是因未满足合规删除就否定所有价值。新补窗未发现新修订信号；只复用同identity/version/claim，不扩所有安全遗忘，停止审阅。

## 00725 OCR：潜力仍保留

[精确v1](https://arxiv.org/html/2604.00725v1) §4和§5已定点读：DAN与Mamba共享CNN、直接architecture比较；训练ROVER pseudo labels、976 manually corrected paragraph test，≤1000chars1–10lines过滤；zero-shot/proprietary与同训比较不能混为同一控组。Antiqua line MambaAR与DAN均1.83CER但53.3vs156.5ms，VAN6.19ms更快。待完成paragraph/length范围与cost字段后交root，不因OCR标签EX。

## root非作者必要Source实际回执

DRKL/Shuffle/Probe已由root实际独读上述精确原证通过（不授Books锁/DAY）：DRKL额外核identical off-policy teacher responses、best-validation与五seed及gamma退化；Shuffle额外核Table2小Adam100epochs best-so-far训练loss，‘大规模Adam未证’不等于从未研究Adam；Probe核AUROC以二值标签作ranking，不采用hidden→能力映射weight-invariant理论。下一步为具体owner差额与逐字PRE，尚未Books写入。
