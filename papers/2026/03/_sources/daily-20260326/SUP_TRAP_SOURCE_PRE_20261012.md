# TRAP23117 — 必要Source / 两段PRE

作者supp_mar26_fresh；首批准入/03-25日级门reader已通过，2+2+3=7不改。实际读exact-v1 §3–5/Eq3–10、§6.1–6.5/T1–6、§7，支持与直接反侧足够停止；未执行攻击/复现、不无差别全附件或读取v2改换身份。

## 原证边界

白盒gradient/参数访问、物理patch在相机视域且用户instruction不能修改；黑盒仅surrogate transfer。§4主动mask/shuffle对照表明CoT与instruction均可参与动作，GraspVLA更由CoT主导、Instruct/Molmo并非CoT绝对胜出，不能照录摘要『strongly governs』为统一规律。§5同时推理和动作目标意图明确；Eq5经非作者发现抽取遗漏后，作者实际回读MathML/application-x-tex，确认条件为r*_{<t}的正常teacher-forcing，删除原错误自条件判断。Eq8正梯度与minimization的recipe歧义保留，不自行修复后称完整实现已验。

§6三VLA/五pick-place任务、25训练layout/10未见layout、H800生成patch/4090仿真，作者ASR按simulator接触完成；hijackScore仅DTW相对相似度。Table3 MolmoCoT-only ASR高于TRAP，Instruct推理成功但动作collapse；Table5相关指令universal效果很低；Table6跨配置大跌、其中score负。真实15 trials中至少一步CoT改变13/15，完成被重定向目标仅5/15，必须不同分母/终点，不称86.7%physical attack成功。无长任务/stealth、安全检测器只是§7建议未验证。优化、打印/校准、额外grounding/controller检查计费；不采零延迟、通用防线或攻击必成。

## 实际owner与交接

Ch26 Safety envelope L1021–1046现有指令改写/持续控制与12717 middleware文本重注已详读：它们改变入口prompt或可写内部CoT，而这里用户指令和内部传输均不必被直接改写，低信任物理观察能改变模型自己生成的推理再影响动作。Ch25持有imagined state而非当前事实，Ch27持有训练数据/采样而非物理commit。仅本Ch26新增这一感知→推理→动作污染边界，保原middleware分支/后abstention，不复制Ch72安全通论。

## 两段逐字PRE（未写，待独核/root窄锁）

位于当前12717两段之后、Embodied Abstention标题之前：

即使内部推理通道没有被直接写入，观察本身仍可能是低信任输入：一个进入相机视域的物理扰动，可以改变 policy 自己生成的对象/子任务推理，再影响 action decoder，而用户指令保持不变。因而可信 prompt、未改写的传输和流畅 CoT 不能共同推出动作仍忠于任务；验收应区分感知输入污染、生成推理偏移、单步动作改变与最终环境 outcome，保留 observation、instruction、reasoning 和 action 的对应版本。这里要求检查的是闭环里的新信任边界，不是把所有视觉异常都判成攻击。<!-- source-family:SF-2026-ARXIV-2603-23117 -->

[受限VLA反证](https://arxiv.org/html/2603.23117v1#S6)中，推理被改变并不总产生目标动作：不同 decoder 会竞争、停滞或退化，真实试验里“至少一步推理受影响”与“完整重定向任务完成”也是不同终点；跨配置、相关指令和未见布局应分别验收。只检查文本一致性的独立 detector 是待验证建议，不是已证实防线；额外感知、检查、重观测与 controller 均有费用。低信任观察、目标对应或风险无法确认时，保留短 horizon、可信低层约束、重新感知及人工接管，不能让推理自签物理执行权限，也不把局部攻击结果外推为所有 VLA 的安全率。

本人静态注拟：`SF-2026-ARXIV-2603-23117 exact-v1 §3–7/T1–6，采用感知→自生成推理→动作污染接口，非middleware直接改写；保多模型竞争、transfer/相关instruction反侧、13/15推理与5/15完整任务终点差异，Eq8歧义不构成可执行recipe；detector未验证，无攻击执行/代码核验/复现。`

纠正Eq5抽取错后必要Source/actualowner/PRE和本人注已真实独核PASS（reader§7）；Books未写，待root具体窄锁，不列外部受阻或DAY完成。
