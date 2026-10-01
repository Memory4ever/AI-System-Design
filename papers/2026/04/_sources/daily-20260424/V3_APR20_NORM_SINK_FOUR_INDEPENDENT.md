# Apr24 四项必要证据与实际owner有限独立核

复核者：`/root/apr20_resume`，非本日作者。实际读当前AGENTS/三合同/Prompt/ROADMAP；只检查20903/20904/20937/20940，未验日级窗口、覆盖或冻结分母，未写共享Books。复用未变有效过程材料定位，但以下判断来自本轮实际原文与实际章节阅读，不以作者声明为PASS。

## 20903 — 窄争议处置通过

[官方v1](https://arxiv.org/html/2604.20903v1)正式题为 **Sensitivity–Uncertainty Alignment in Large Language Models**。实际读§3.1–3.5/4.1–4.3、必要A.1，并另以官方MathML核Eq10/11及Step4。S是扰动分布的期望，Remark3.3明确≤sup，却被Eq11称上界替代；A.1 λH≥ψ推出的负号不等式写反，加减ψ后非负性也不能删除加回项。作者保存的常数分布反例成立：pθ=ptrue=(.5,.5)，Z单值、0–1/TV L_D=1、ψ≡0符合非降/凹/ψ0=0、λ=1，所有perturbation不变，κ=S=0，Rrob=Rθ=.5，Eq11右端=.5−ln2。因此该风险桥/无条件entropy subtraction不能采用。

只隔离所影响中央保证，保留S/H不同对象、诊断、实际目标和有限实验；本反例不否定ψ=0时标准sup界，不证明全部结果错误。重开仅需修正风险桥/假设及其与实际目标的关系，不能用新benchmark代替理论。6分纠错深入与暂缓通过，不用Ch31奖励代理或Ch66calibration已有主题冒签新定理Existing。

## 20904 — source→当前owner窄采用通过，未见literal

实际读[官方v1](https://arxiv.org/html/2604.20904v1) §3.1–3.5/3.4.2、4.1–4.2及必要A.1/A.3/A.4；实际对读Ch31“Preference data 的难点不只是数量”至Preference Admission，并检查其后conditional preference profile。现章pair/rubric/来源可靠性与“谁偏好什么”没有等同于本项**固定同一flow解释，只换其norm universe，比较同completion的context-grounded reward**。该训练桥归TRAIN-RLHF，不把它搬成Ch72runtime权限。

正确/随机错误universe对每个completion分别检索Top3 norms并评分，clamp(r_correct−λr_wrong,0,1)真实成立；norm/flow两typed对象和structure gating不能混成“越保守越高reward”。A.1Qwen3-32B rewardjudge与主文/disclosure Qwen2.5-32B不一致须保，2RTX A6000只是抽取配置，不补训练GPU。G2/b8/lr1e−6/max2048和额外检索/双judge成本实际披露。Table4context reward的HIPAA反退、50条至少一配置40%judge错的切片及小说WEIRD规范偏差均限制，不采普遍法律/安全authority或appropriateness保证。6分实际gap深入成立。

V3_EVIDENCE_NOTES末本轮所见是两段的安排和边界，不是完整literal。上述source→actual owner采用通过，仅限既定norm-context contrast与成本/失败/明确规则回退；未审核尚未给出的逐字两段，不预支写后或I。

## 20937 — source→当前owner窄采用通过，未见literal

实际读[官方v1](https://arxiv.org/html/2604.20937v1) §3.1–3.3、4/Eq4–6、5.1–5.4/Tables1–5及naive hard pruning对照；实际顺读Ch23视觉budget/temporal query、stage selector、局部区间merge和几何稳定≠功能删除。现章有attention proxy非truth，却未承载**跨帧累积高attention可挤占有限预算，单帧排名应与sink proxy分开校准**的具体机制；归MULTIMODAL-REPRESENTATION，Ch66接评价而非另一个owner。

Eq4是Σ_t A_it再幂/MinMaxNorm，Eq5 A−μ_s s，Eq6 similarity+μ_t s；sum本身不能辨别一处短时大峰与持续高值，同总和也可能给同proxy，故“persistent”只能解释为该有限统计下的候选角色，不是语义稀疏或无用的证明。§3.3随机去sink并同预算替补及§5.3naive对照支持局部选择取舍，不支持永久高分token普遍无用。静态关键对象不可硬删；回退原attention/较多token有必要。

32×196token、LLaVAOneVision/Video7B、保留10/15/20%、原披露GeForce A6000字符串、MCQA/free generation不同分母与GPT5judge须保；Table1 VisionZip20%Consist3.22→3.16/Temp2.17→2.09退步，Holitom YC70.95→70.66，Table2某切片反退，不能采90%全无损或全部收益因果。attention读取/跨帧汇总/μ,w,τ与端到端runtime ND不能删除。6分gap深入成立，source→owner窄采用通过；本轮未见完整literal，不预支两段逐字通过、写后或I。

## 20940 — 6分标准仅报告通过

实际读[官方v1](https://arxiv.org/html/2604.20940v1) §3.1–3.3/4.1–4.5/5；实际对照Ch23开篇codebook/artifact/coordinate contract及Ch62现有API与transport边界。client离散codec、server一致reconstruct后原生encoder、vision AX/OCR补文本、session framing是原文真实placement分支，不是任意LLM直接读任意codes。§4.1与§5明确component latency+emulated network simulation，prototype/tail/client/loss resilience仍futurework；Fig encode+transfer+decode不含恒定model inference，不能叫真实部署端到端SLO。

200语音/100导航/50文本、payload不含全部wire/TLS、1st RVQ50/s、原硬件/precision未完整绑定、音频45–180msencode+8msdecode、WER2.7→4.1与text-only visual75.5/hybrid93.3/raw94均保。AX/OCR lossless运输不证明原抽取正确/完整，batch3–5秒与gap实验不证明时间无关。6标准Only通过，保局部新操作点不采用通用传输升级；不以现有成熟合同主题等同整篇Existing。

结论：四项有限处置/两source→actual-owner范围通过，20904/20937完整literal未提供则不冒称已核；授锁、真实正文及非作者写后须后续分别检查。非本日Gate，不扩所有附件或版本史。

## root 实际写后复核

非作者 `/root` 本轮实际顺读 Ch31 Preference data 相邻论证和 Ch23 全局冗余/局部合并至连续控制的重要性论证，以及两章章末 Review notes。20904 两段已真实写入 TRAIN-RLHF：同一 completion 的正确/错误 norm context 评价、差分截断训练信号、检索/critic 不拥有规范真值，以及额外成本、HIPAA 不利切片和 Qwen3/Qwen2.5 judge 身份冲突均在机制附近保留；与前文来源可靠度和后文 preference admission 的分工不混同，部署保护交 Ch72。20937 两段已真实写入 MULTIMODAL-REPRESENTATION：累计 attention 与当帧排名分责、软惩罚/相似性分支、同总和无法区分短峰与持续高值、静态关键对象误罚及回退预算均明确；没有把 sink proxy 当语义无用或 90% 无损保证。前接区间 merge，后接连续控制平滑，机制正文均在 Review notes 之前。

两项实际正文及相邻衔接写后通过，可分别计一项真实整合；不预支当日来源、日期、冻结分母或日级完成。Review notes 中尚存的“待非作者写后”由本日作者最小同步为本次实际通过；未复现实验。
