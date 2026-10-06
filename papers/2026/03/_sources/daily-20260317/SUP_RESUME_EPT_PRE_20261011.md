# EPT12577：必要原证/actual owner与逐字PRE拟案

仅本17补03/16。日级身份/完整题摘准入及全年具名去重有效复用；resume_mar17实际[exact-v1](https://arxiv.org/html/2603.12577v1) §3.1–3.3/Eq1–8、§4.1–4.6/Tables2–5、Limitations、Appendix B Algorithm1/C/D必要支持与反側。拟2+1+2=5，标准审阅上因具体参数生成器/optimizer接口差额深入。未核artifact/复现，不把作者notes当原证。

## 支持与收窄

独立experts→共同BA seed、前缀slice与不同kernel/stride转置卷积重建同shape W_i，再输入Top-k选择；A/B Gaussian而K_i零初始保留原forward。共享seed不是已证实通用语言知识，kernel大小不是语义难度真值；seed低秩不直接证明重建W_i同rank上界。零expert输出不自行解决router coldstart（作者分析，需独核）。任务prototype loss用t_i标签，非无监督；Eq3 inputrouter与Eq8 e_t/Alg1h之间缺精确注入桥，不采taskID未知部署recipe。

Eq6 d_t/T乘整个expert输出，未分离shared/specific参数更新，不能认证逐维梯度能量补偿/稳定收敛。T5-base/A100、Llama2-7B/3A800，5epoch/global32/max128，mixedaccuracy平均不可作普遍最好；QQP/STS-B/OBQA与uniform2 RTE反退保留。Table5非全因子、ABinit行比较混ALP且86.2/86.0口径不一。C只算参数且排router；shared矩阵12,288与缩小seed6,144+kernel240并非单纯同shape独立共享差额，不据此授公平缩比/零额外推理。精确shape与全部搜索总预算、precision/servingbatch/concurrency/tailSLO未披露；D明确报告best evaluation checkpoint，不误记模型选择完全ND。必要论文可支持限定生成接口，不认证完整recipe或headline。

## actual owner与PRE

actual Ch30 213–251：静态共basis+module系数可merge、阶段/时间共享、inputrank/implicitexpert及hypernetwork均在；差额是同一seed经不同空间算子生成同目标shape，而非只截rank或router生成新seed。actual273–291 zeroexpert subsection独立保留，不把新分支当symmetry保证。Ch29/31开篇/目标交接已读，唯一TRAIN-LORA。拟插在现2512.24603静态共basis两段之后、阶段累积方向之前；以下未授锁/未写，需root与reader具体PRE通过：

共享参数还可以先形成生成adapter的seed，而不只把同一组basis交给不同模块组合。一个受限分支由两组低秩因子形成共同矩阵，按目标配置取前缀，再用不同kernel与stride的转置卷积重建同shape的expert增量，最后由input-dependent gate选择和加权。此时可调对象包括seed、重建算子与router，seed的rank不自动成为物化权重的rank证明；kernel尺度也不拥有任务难度或语言语义真值。两因子随机而重建kernel零初始化能保持初始增量为零，却不自行保证router已经分化。<!-- source-family:SF-2026-ARXIV-2603-12577 -->

[EPT的有限对照](https://arxiv.org/html/2603.12577v1)支持这个参数共享/生成接口分支，不证明每项任务都更好、尺度独立因果或逐维更新频率已被精确补偿；本文不采用其未闭合的任务embedding注入与完整优化recipe。共享seed和轻kernel的trainable count应与重建/物化、路由、任务监督及模型选择总成本分账，input gate仍不能静态merge为一个固定增量。shape、共享方向或训练/部署质量不合算时，应保留静态共basis、独立LoRA experts、固定adapter及逐任务回归，而不是用少参数量批准普遍稳定或免费推理。<!-- source-family:SF-2026-ARXIV-2603-12577 -->
