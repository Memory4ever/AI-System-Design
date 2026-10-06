# 02/20 第八有限必要包：16334 / 16340 / 16412 / 16438

作者实际读必要 exact-v1 方法、关键对照与直接反侧，root必要原源/actual owner PRE已通过；16334 Ch23:115/末注1251、16340 Ch28:394/末注1751、16438 Ch66:428/末注5532实际正文/完整邻接/自身末注POST均通过，三锁释放。16412具体已有覆盖处置通过。下文拟写保留为PRE依据，不是当前未写状态；未授全日。复用已完整AB准入校准，不扩全附件。定位为 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`。

当前官方abs完整AB/Comments/history已实际轻查：16334/16438仍v1，16340当前v3 ICML、16412v2 CVPR接受；未见具体撤回/纠错信号，不因版本号遍历revision。采用精确v1，不沿当前修订实验。原Submitted/Registered实际读本地同ID DataCite，Created只raw；官方bridge的09:00下界、Registered+1秒上界推定如下，含起不含止。

| ID | v1 Submitted UTC | Registered UTC | 北京上界（起点均2026-02-19T09:00:00+08:00） |
| --- | --- | --- | --- |
| 16334 | 2026-02-18T10:16:30Z | 2026-02-19T02:43:43Z | 2026-02-19T10:43:44+08:00 |
| 16340 | 2026-02-18T10:25:07Z | 2026-02-19T02:43:52Z | 2026-02-19T10:43:53+08:00 |
| 16412 | 2026-02-18T12:37:35Z | 2026-02-19T02:45:34Z | 2026-02-19T10:45:35+08:00 |
| 16438 | 2026-02-18T13:19:11Z | 2026-02-19T02:46:11Z | 2026-02-19T10:46:12+08:00 |

## [Spatial Audio Question Answering and Reasoning on Dynamic Source Movements](https://arxiv.org/html/2602.16334v1)

2+1+2=5，评价反侧必要深入。最小source §3.1（104–127）、§3.2–5（167–187）、Table3（187–259）、§7/限制（326–331）与B.3（744–773）。224原mono event经CLAP筛选，10s模拟stereo至多3source，方位只前半平面、固定room反射；由场景metadata用GPT-5-mini生成QA/理由，human200随机样本不证明所有题或独立现实泛化。BAT encoder/Qformer/Qwen3-4B思考模式，stage1投影后stage2全三部分微调；4A100/10epoch/b8每卡与LoRA r8，精度/重复seed在采用位置Not Disclosed。

AGM是query-event时间mask，不是真正重叠声源分离：CRNN/文本WSTAG阈值0.8/median0.3s，非事件片段置零；重叠干扰仍保留。Thinking×NoMask/AGM/GTmask控制有具体反侧：Table3 MC在thinking下53.1→52.9→52.8，并非mask越准必越好；NoMask YesNo thinking72.1低于nonthinking72.6，Open41.0低于41.2。overall及单事件局部正收益不代签全部格式协同增益。Boolean/MC keyword判分，Open由GPT-5-mini factual/semantic 0–5打分，不混称全部正确率。thinking平均6.19s vs2.36s但推理hardware/precision/batch/输出预算未完整披露，不采用普遍速度数字。作者把MC反侧解释为联合context丢失属假说，不授已识别内部原因。

actual `MULTIMODAL-REPRESENTATION` Ch23:111–113已目标信息/readout与层可见性，未承载**query filtering对单事件与多事件关系题的可用证据不同，更多thinking可能在更窄输入下失去联合context**。拟最多一自然段接音频表示评价段，保mask×questionformat×thinking预算/模拟与judge边界，原完整连续声学输入保留；不是复制“音频排序不同”。如owner现有target/query closure已足够，局部结果仅报告，不硬写。

## [The Implicit Bias of Adam and Muon on Smooth Homogeneous Neural Networks](https://arxiv.org/html/2602.16340v1)

2+1+2=5，必要理论。最小source §2.1–2.4（89–196），§3.1–3.3（200–235），§4（236–244），§5.1–5.2（248–275），§6–7（276–295）。smooth L-homogeneous binary分类/exponential-tail loss、infinitesimal fullbatch flow；lr积分无穷但η≤o(t^(1/L−1))，Adam需单调schedule、ε=0、β1≤β2且起始各coord gradient-square正下界。Muon exact SVD正交化，不是生产Newton–Schulz近似/AdamW。T2方向收敛且正margin是**假设**；nonSmooth ReLU额外T3 normalized subgradient收敛未证明且MNIST例似不满足。

§5 approximate-steepest-descent桥接使momentum/gradient渐近方向关系支持**对应norm margin problem的KKT局部stationarity**，不是全局最优/泛化优越。Muon max-layer spectral、Adam l∞、hybrid由组lr配比定义，不由norm名称签发训练效果。MNIST2048 even/odd、2层sqReLU/ReLU、ε1e−20、t^-0.8、10seed CI只是近flow离散例；hardware/precision未披露，不引用吞吐或LLM质量。

actual `TRAIN-PRETRAINING` Ch28:369–395已basis equivariance/optimizer-state/schedule改变trajectory，且明确implicit-bias不保证generalization；尚不具体承载**同目标下动量渐近优化的是哪个norm及只能KKT的假设级权限**。拟一自然段接现有geometry/update-rule论证，保生产AdamW/离散/近似Muon必须另外验证与成熟coordinate-adaptation的合理性，不写“Muon优/Adam错”。若已有norm-specific段足够则已有覆盖。

## [ReMoRa: Multimodal Large Language Model based on Refined Motion Representation for Long-Video Understanding](https://arxiv.org/html/2602.16412v1)

2+2+2=6，拟具体已有覆盖，不为缺RMR/HMSS配方新增段。必要source §4.1–4.2（188–248）、§5setup（424–435）、ablation（579–642）、AppB（1151–1181）、AppF（1258–1290）。稀疏I RGB+block MV，经CoTracker3 optical-flow估计作L2 teacher refinement；teacher不是flow真值。local/global **bidirectional** Mamba压缩motion/appearance，不授causal streaming/world dynamics。H264重新编码、scene-adaptive I、384²/16fps/maxGOP32/4²block，非任意native codec省全部解码或transcode成本。

移flow alignment/移RMR/改crossattn/加法均局部掉分，但结构/参数预算未全匹配，不唯一归因SSM优越。AppB同H200SXM、NExT随机50video测量，输入/输出/batch声称匹配但数值未披露，FP16仅支持时；ReMoRa0.40sample/s低于LLaVA-Video0.53，24.45token/s亦低于31.78，内存10.59GB对23.21GB是另一维度，不授全面加速。AppF只抽其错而baseline对的50case，多label共67错误非独立67样本，annotation/spatial/temporal/motion错误仍存在。

actual `MULTIMODAL-REPRESENTATION` Ch23:671–699正文已直接承载keyframe+MV/residual、codec/GOP/时间身份、token压缩不等端到端、场景边界与appearance/dynamics双责任。新局部refinement/HMSS仅具体实现与经验，不支持另一个可泛化接口条件；建议已有覆盖，受限结果仅报告，保RGB完整路径，不重复codec主线。

## [Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment](https://arxiv.org/html/2602.16438v1)

2+1+2=5，设计反侧深入。必要source §3（98–158）、§4/5（161–176、297–320）。Mistral7B/Llama3.1-8B/Qwen2.5-7B，gender DPO/QLoRA β0.1一epoch/LR5e−5；BBQ gender除transgender864后4808，961test/3847train，二binary pair展开7694不是独立7694item。全文宣称总58492与九项表计31372不一致，不引用总分母。ambiguous以Unknown为正确、disambiguous为已有证据的类别答案，accuracy不等真实歧视。三选项原评价/二选项训练格式不同、A/B/C parser改善是未分离替代解释。

physical-appearance ambiguous退步跨三模型；sexual/disability统计负侧不是所有模型，disambiguous总体改善。paired McNemar未披露template依赖/多比较完整校正，单一BBQ/一个alignment目标不能证明普遍DPO spillover规律或内部机制。后文讨论明确其他算法/人口需另测；硬件/训练精度与重复seeds在采用核心Not Disclosed，不引用性能。

actual `PLATFORM-EVALUATION-SYSTEM` Ch66:417–426已parser/abstain、polarity/类别与context-factorial，Ch34:381–390已有目标关系/顺序与helped/harmed固定slice。但二者未具体承载**target属性对齐后，untargeted属性在缺证据应Unknown与有证据应回答两条件中可向相反方向变化**。拟最多Ch66公平评价一段，交叉alignmenttarget×evalattribute×context并保原item/parser合同，不由aggregate升高发全公平证书；非所有低分=偏见。21作者共享Ch66写前必须协调，当前未申请锁。
