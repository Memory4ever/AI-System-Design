# 02/20 第十五有限必要包：15950 / 16144 / 16197 / 16301

完整题摘与一次core准入已保留；以下为作者实际必要原源与actual owner比较，root已实际必要原源/actual owner独核，15950仅报告/16144与16197中心暂缓/16301已有覆盖通过，不是日级验收。15950 HTML无正文，采用精确v1 PDF pp1–8并实际渲染读p5；其余位置为 `V3_extract_html.py < V3_CORE_2602.<ID>v1.html | awk 'NF' | nl -ba`。不扩全部版本或附录。

| ID | v1 Submitted UTC | 同ID DOI Registered UTC | 北京公开范围（官方bridge推定，含起不含止） |
| --- | --- | --- | --- |
| 15950 | 2026-02-17T19:06:19Z | 2026-02-19T02:34:41Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:34:42+08:00 |
| 16144 | 2026-02-18T02:29:33Z | 2026-02-19T02:39:17Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:39:18+08:00 |
| 16197 | 2026-02-18T05:35:32Z | 2026-02-19T02:40:32Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:40:33+08:00 |
| 16301 | 2026-02-18T09:31:43Z | 2026-02-19T02:42:57Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:42:58+08:00 |

Submitted只按官方schedule给最早下界；Registered按已核官方ID/DOI公告桥接给1秒精度上界，Created仅raw。当前abs轻核15950 v2、16144 v5、16197 v3与16301 v1；未见明确撤回/纠错声明，后版不能替代本窗精确v1，不因版本号扩比较。

## [Can Vision-Language Models See Squares? Text-Recognition Mediates Spatial Reasoning Across Three Model Families](https://arxiv.org/pdf/2602.15950v1)

2+1+2=5，设计反侧必要深入，拟仅报告。§3 pp2–3：15个15×15 grid、24–94 occupied cells；同一grid分别渲染为`.`/`#`符号图片与黑白方格图片，均不是直接文本输入。Claude Opus4.6 web、ChatGPT5.2 Plus Automode、Gemini3 Thinking web，固定指令/5grid批次/分条件新session。segmented squares仅Claude补测；不能把全部web内部preprocess/模型路由视为一致或把文字图优势叫已证明内部text-recognition pathway。pp3–5 Tables1/2、p5图与qualitative errors支持受测格式差异和密度反侧，不证明encoder内部因果；cell population还共享grid/session，不能把3375cell当独立模型重复。

§5.1 p6作者明确“as if”而非架构结论；§5.2 p7未做同有效resolution/decoder/readout完整控制。§5.5 pp7–8单trial/condition，Gemini另trial更早collapse且报告较好run；无API控制或prompt敏感性完整检查。硬件/precision/SLO Not Disclosed，不采用34–54 headline为稳定跨模型定律。actual MULTIMODAL-REPRESENTATION Ch23:97–99已有同pixels换preprocess配置/同配置换pixels、guided reading不等任务成功及内部归因限制。该文具体符号/方格格式负例不是所有被覆盖，但有限web protocol未识别新表示机制或可靠性成立条件；作为局部格式诊断证据仅报告，不强造新recipe缺口，不退回贡献排除。

## [Missing-by-Design: Certifiable Modality Deletion for Revocable Multimodal Sentiment Analysis](https://arxiv.org/html/2602.16144v1)

2+2+2=6，安全/擦除主张深入，拟中心争议暂缓，局部方法仅报告。§3.5–3.9（208–263）：saliency重建梯度与低贡献proxy选少量权重，校准Gaussian噪声，并发布indices/seed或commitment/参数hash。Alg1 step7（249）实际ε≤1时确定zero、否则noise，与254“conservative budget favors noise”相反，不能用正文字句修正实际算法后授保证。Eq16（210–212）以never-exposed无噪模型为参照；A.1 ThA.1（1101–1116）实际改成surgered与reference两侧均加iid Gaussian，且Δ相邻参数定义未建立surgery与never-exposed重训均值的耦合。故不能从局部Gaussian式子授modality deletion/任意adversary保证；公开noise seed的release-view问题也须明确，不泛称MDC可验证即隐私有效。

§4.10（628–656）MOSI音频白盒activation/黑盒logits攻击近chance只为所测诊断，非全部adversary或永久擦除。A.4（1151–1155）估计calibration Lipschitz不自动为全域sensitivity证明。actual PLATFORM-SECURITY Ch72:2632–2638已要求删除对象、never-exposed/retrain参照、retain utility与joint privacy分责；该文想提供的新certificate尚未跨过算法/定理/参照冲突，故不写Books。不称全部局部实验虚假。重开仅需一致的实际randomized variant、发布边界与reference/sensitivity耦合或勘误，不请求所有附件/运行。

## [ModalImmune: Immunity Driven Unlearning via Self Destructive Training](https://arxiv.org/html/2602.16197v1)

2+1+2=5，中心实现/理论反侧深入，拟争议暂缓，局部配方仅报告。§3.7–3.10（218–254）：选中modality在fusion遗漏并向按embedding scale的Gaussian target与covariance nuclear/operator ratio收缩；该ratio虽文称stable rank，不能以标准名称替其公式。§3.8（234–242）以empirical Fisher/Gauss–Newton最小eigenvalue<负τ为freeze分支，按其PSD定义该分支不能承担负曲率检测，需实际非PSD算子或规则澄清。§4.2（322）又声明pretrained encoders冻结，与对attacked encoder应用negative feedback/self-destruction更新角色冲突，无法正面归因SDL机制。

Eq15（246–248）近似算子是(I−αH) inverse；A.4（1228–1248）在α||H||<1给这个算子的Neumann tail certificate，不等一般stationary hypergradient的H inverse证明，也不认证全系统robust immunity。Eq16 squared leave-one-out loss difference去掉改善/恶化符号，不是conditional MI或已识别因果贡献。§4.7 Table5（657–683）named模块消融不直接隔离collapse/curvature/certificate；部分去模块MAE等更好，不能采全部机制唯一归因。§4.13（785–786）RTX3090/Pytorch1.13/CUDA11.7/FP16/b32与额外eigencost只为作者设置，未复现。

actual MULTIMODAL-REPRESENTATION Ch23:815与952分开任务贡献、当前observation reliability和门控校准，不授由一个squared importance proxy得到因果或删除保证。本文新destructive-update分支的关键算子/冻结实现不一致尚不能进入这条长期知识链；不因为缺完整配方在Books制造gap。重开定点为实际更新参数/非PSD gate算子与对应控制、Eq15 operator目标及certificate条件澄清；既有fusion/retrain/noisy-input方案继续合理。

## [Multi-agent cooperation through in-context co-player inference](https://arxiv.org/html/2602.16301v1)

2+2+2=6，标准完成拟具体已有覆盖。§2–3（105–146）：100round IPD、混合learning agents与tabular co-players、无policy ID的history适应；PPI worldmodel+prior/MonteCarlo Q，每phase重新初始化序列model并在累计trajectory数据上训练。不是必须LLM，也不硬编码partner update或分开naive/meta learner；理论equilibrium不外推现实自由Agent自然合作。A.3.1（374–407）GRU128/embedding32、30phases/20k trajectories/10epochs/AdamW，200k tabular pretrain与15step规划有成本，不是在线parameter-free训练。

§3 Fig1/2（含10seeds）mixed pool条件支持有限in-context响应；no-tabular同时改变pretrain随机action数据，不能单因素归因diversity。A.4.1（493–501）fullpolicy-vector ID减少infer需求但不证明身份隐藏更安全；B.2（509–511）A2C相互extortion先合作后部分seeddefect，合作不是任意learner稳定保证。actual AGENT-MULTI-AGENT Ch82:346–348正文已承载interaction-history behavioral belief、partner diversity有限in-context adaptation、strategic shaping/collusion与runtime authenticated identity分责，来源1112正是本家族。拟采用长期论点已真实覆盖，不因正文没有PPI超参配方再整合；保实验IPD/partner人口与机制证据在报告，不把对应研究排除。
