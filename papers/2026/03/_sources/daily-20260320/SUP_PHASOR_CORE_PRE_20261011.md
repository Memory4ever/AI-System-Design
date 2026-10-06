# Phasor17433：固定 Fourier 混合与受影响梯度边界

resume_mar17，仅03-20补03/19；本次实际重载AGENTS/适用完整合同、Sources每日主题/prompt/ROADMAP与本日停点、Books约束。原批5完整题摘/date与2+1+2=5复用，不重查日期。这里只必要Source/actualowner/最小PRE准备，不自授PASS或Books锁。

## 1. 必要源与停止范围

[exact-v1](https://arxiv.org/html/2603.17433v1)必要§2–3 L72–206及§4–6核心评价/旧深度主张 L209–300已实际读；current abs明确梯度路径纠正触发仅[v2](https://arxiv.org/html/2603.17433v2)受影响§2.3–3.4/关键Tables1–3/§6–7 L99–288定点核。本轮再次实际核v2 119–200/209–288确认修正与直接相反证据；不读其他版本/库/全附件或复現。

## 2. 有限接口与直接反侧

单块是可学习对角phase shift→归一DFT→对角shift；输入按当前完整窗口max绝对值映射成单位复phase。DFT使各坐标共同参与固定全局混合，但不是query-conditioned pair寻址、不是已有softmax的exact执行优化；全局能量守恒不保证各坐标仍单位模。O(TlogT)属于mixer，phase参数随窗口T增长，不把Attention权重O(d²)误称随T平方增长。当前零幅窗口除零guard、读出“末thread”对公式output0口径不齐，不补完整recipe。

v1把每块phase pull-back当深度稳定桥；v2§2.5/3.3改为默认ambient酉cascade、仅terminal fold，但§6/图2仍称每块fold并用于depth收益，受影响实现语义未统一。v2明确旧.item()曾切断梯度、只有末块训练，旧deep优势不能再归因depth。fold的分支内导数为±1、折点不可微，不是一般解析导数发散；atan2数值表达不使折点处处可微，更不能由有界phase授优化稳定、无信息丢失或无限context。有限单块混合接口可以与这些强桥分采；一次强命题重开请求为统一terminal/interblock消费者与读出位置、零窗口守护及实测全块gradient trace/匹配参数预算深度消融。

v2 T1小合成T10三seed，phasor MSE .064仍高于linear AR .051及MLP .057；T32同目标/1000train250test，MAE .1817高于attention .1034，3329/64约52非100。T16 depth3→4 .154→.159且参数随depth增加，不能授独立depth因果或单调收益。不同预算和容量的模型对照仅显示该有限设计点，不给生产latency/precision/concurrency/SLO或全费用。完整历史窗口预测下一标量，不等所有位置causal语言建模，也没有增量KV/无限长度消费实现；HW/总训练搜索和FFT搬移费用未完整披露。

## 3. actual唯一owner与差额

sole `MODEL-SELF-ATTENTION` / [Ch14](../../../../../books/part-02-model/14-self-attention.md)。实际入口1–42、替代匹配表示完整395–452：latent组件/无投影Gaussian与带QK距离邻域、signed prefix和Value solve均保内容条件匹配或读取校正，未具体承载单位phase输入、固定DFT与可学phase夹层的全局混合、全局能量对坐标模分责。故不是泛Fourier/相位主题映射或已有覆盖。Ch13入口1–32/Ch15入口1–30负责位置与多头，Ch22相关local/global与递归state已读但不接管该不同混合算子，不新增结构。

拟Ch14 Projection-free Gaussian完整段/2605-02144 marker之后、保QK RBF距离分支之前两段，让无内容寻址的固定混合与距离核保持不同归纳偏置；不触既有softmax或递归state。

## 4. 两段 literal PRE 与静态注

全局交互也不一定先形成按内容选择的pair权重。一条更强结构先验的分支把完整历史窗口缩放成单位复phase，在两组可学习对角phase旋转之间施归一Fourier混合；每个输出都依赖窗口各坐标，却没有当前query对各key的自适应寻址。这是需要训练与任务验收的不同模型算子，不是对已有softmax的无损kernel优化。酉混合保持全局能量，不保证每个坐标仍单位模；当前窗口缩放、零幅输入、读出位置和terminal/层间非线性都应成为模型接口，不由有界角度推定信息或梯度处处保持。<!-- source-family:SF-2026-ARXIV-2603-17433 -->

[固定phase/Fourier分支的受限证据](https://arxiv.org/html/2603.17433v2)只覆盖短合成历史预测下一标量，不是所有位置causal语言建模或增量KV路径。更少phase参数和mixer渐近复杂度不认证端到端更快，线性AR、MLP或attention在关键对照中仍有更低误差；旧梯度被scalar extraction切断的深度结论不能沿用，当前terminal与层间fold说明未统一也不采用稳定/无限context保证。FFT、复数状态、窗口归一化、训练/搜索与读出均计费，phase参数仍随窗口增长。强周期先验不适配、关键内容寻址或真实预算/质量退步时，保留原Q/K/V、固定局部或已验hybrid路径，不让固定全局混合自行取得证据充分性。<!-- source-family:SF-2026-ARXIV-2603-17433 -->

静态注：

- `SF-2026-ARXIV-2603-17433` — [Phasor v1](https://arxiv.org/html/2603.17433v1)必要混合/读出与有限评价；[v2](https://arxiv.org/html/2603.17433v2)仅受影响gradient path/fold scope与Tables1–3直接反侧。只采单位phase/固定DFT夹层的替代混合接口，保global能量与坐标模区别、有限预测/质量和全费；不采完整recipe、深度唯一归因、处处稳定/无限context、语言因果或生产速度保证，未核代码/复现。

送reader必要Source/actualowner/原两PRE有限独核；未授写入/safe/DAY。

## 5. 限定实际写入

resume_review17_18非preparer必要Source/actualowner/原两PRE有限PASS见本日独核§22，root随后授唯一Ch14本family窄锁。作者仅原两literalPRE实际429/431及静态本人653；writer已实际完整424–445及646–653自身/邻注读回，Gaussian→固定全局混合→可学QK距离核/后续递归state责任顺接，限定本family diff仅两段及静态注，git diff --check 0。不改正文或静态注记录验收身份，下一非writer实际POST，尚不授safe/DAY。
