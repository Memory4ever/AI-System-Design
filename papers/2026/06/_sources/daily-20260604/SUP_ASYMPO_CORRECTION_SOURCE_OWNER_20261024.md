# ASymPO 03070：具名纠错域 / actual依赖 / 最小注释纠正PRE

本日纠错审阅，不重复R28 notice/准入界定，不进入已撤回v2的候选、评分或Books采用链。原21阶段20I/E1不受影响；本纠错域此前独立指定为未评分对象，不用删候选/降分伪闭。必要实际读[exact-v1](https://arxiv.org/html/2606.03070v1) §3.1–4.2/Th1–2/Eq1–23、A两证明、§5.1–5.3/T2及直接结果说明、Limitations、C实际stabilization段/Eq44–46。原HTML剥标/保mathannotation TEXT69648字元保存[原件](2606.03070v1.fulltext.txt)，无工具truncation。停止于足以限定处置的受影响域，不读完整B六条代数性质/全部D扩展任务或代码，不为证明不采用扩全版本史/所有proof。

## 身份与可采用边界

R28已核v2官方“withdrawn because of incorrect proofs in paper”且无PDF，**只v2正式withdrawn**，禁入选/评分/正面采用。v1不是直接撤回；v3恢复PDF但官方incorrectproof comment仍在，不能据此认证proof修复，也不能断言每条v1证明均错误。此轮不需要比较v3所有式子：拟处置只否定无证采用/错误覆盖映射，若要正面采用理论须作者明确勘误对应范围/修正版证明及独核；当前未取得该桥，不说外部无法取得正文。

## v1局部能核与不能推出的命题

§3/Th1/A：假设behavior响应NLL在共同中心附近δb内，并**另假设真实每token ratio均在[1−ε,1+ε]**，用三角不等式得|ΣA Sθ|≤2B(δb+τε)，条件下代数可核。不能把这个先验条件写成PPO clipped surrogate必然保持真实ratio的结论；例如正A且真实ratio=2、ε=.2，surrogate可使用clip1.2但真实ratio仍2。本例是本项目直接代数反例，不声称找到官方勘误的唯一归属。behavior同一模型生成也不自动使不同response的NLL尺度相同，baseline零和不保证weightedloss零和。

§4.2/Th2/Eq18–23/A：Sθ,g是response平均tokenNLL>0，C=1/sg(S)，前向每S/sg(S)=1且ΣA=0，所以forwardloss0成立；autograd分母冻结时梯度为Σ(A/S)∇S/G，可不恒为零。这里是surrogate计算图，不应按普通恒零实函数求导抹掉真实stopgrad；反过来**可非零不等每批必非零、每正/负response概率都独立向预期变动或改善回报**，共享参数方向可抵消/干扰。该公式没有给出old/current ratio、support/mismatch估计或稳定性/收敛保证；loss value平衡、梯度规模/方向、offpolicy校正和训练稳定是四件事。

§C Eq44–46对正A的logp作上界、负A作下界，截断token梯度0但保其进入response平均；用同一hattedS分子分母且hattedS>0、无floor介入才保forward归一=1。随后提出分母floor sg(max(hattedS,eps))，floor激活时不再等于同一分子，不能沿用严格零和。p_low/high是额外经验阈值，主文“没有方法超参”不能泛给全部stabilized实现。原文用d(−logp)/dp=−1/p讨论参数梯度爆炸遗漏链式：softmax CE对logit是p−onehot，不能只从1/p证明实际θgradient无界；高维Jacobian/1/S仍需另控。作者也建议globalgradclip/可选KL，并未提供这些实现的端到端稳定性定理。没有实作审计，不能将主实验全部归因于baseEq19或认证具体阈值已启用。

§5：VeRL stalenessthreshold .5、mini32/train512/G8、MATH4K、Qwen3-1.7/4B-Base和Llama3.2-3B-Instruct、LR2e-6/3epochs、prompt1024/response4096，SPOα.2；无明确训练seeds/CI、hardware/precision/完整rollout/teacher/统计预算、端到端throughput/服务SLO。表2/3是作者有限math训练，不能把API删行为logprob或versiontag等同消除数值漂移。正文仍用staleness配置，未披露全部调度行为；不补为何仍可判断threshold的实现。主文T2 Qwen1.7B GRPO37.45>Asym36.98，Qwen4B45.52>45.07；Llama Asym31.70>30.84。T2附近文字称某Qwen4 AIME24pass@8 tie而T3具体数字未本轮逐项采，故不引用该单格。保作者报告naive/GPG collapse与SPO/ASym保持reward这一正面有限观察，但这不隔离scale唯一因果或证明任意异步/去versionmetadata安全；不因理论桥未闭删这组支持。8evaluationrollouts不等8trainingseeds，当前未实读曲线像素。Limitations本人明确heuristic/nontrustregion、不控制ratio、极大drift信息不足，与普遍稳定解释不等价。

因此本次为**中心稳定性桥争议隔离**，非普通“范围外排除”、非正文访问障碍；保局部代数和受测经验的限定记录，不正面采“lossbalance证明offpolicy已控/无需版本即可任意陈旧安全”。重开条件：明确对应v1/v3的勘误/证明假设与实际stabilized目标、独立核对相关梯度与约束、以及欲主张的异步/预算对照；无新材料不扩扫附件。

## actual Books依赖及最小PRE

实际exact 03070/ASymPO/SF-ASYMPO只命中Ch33这一组书末trace。已完整读当前H3“正负Advantage不必共享同一ClippingContract”两段/分支code、H3“Asynchronous RL必须把PolicyStaleness写进Advantage”完整相关组与“PolicyStaleness应进入Advantage可信度”；前者是正A currentprob/sg(currentprob)、负A仍behaviorratio/clip，**不是本v1各response NLL自归一化**；后者是合法通用freshness控制，不能充当该具体算法已有覆盖。未发现依赖ASymPO Th1/2的独立机制正文，不因旧NC错误而重写这些已有有效原则。仅纠正原trace的“已有覆盖”及方法错映，保原Daily2026-06-03/primaryv1、marker/两直接侧，不搬旧候选日期、不触碰其他日报。本日06-04补Jun03记录本纠错处理，不宣称旧Jun03日级重验。

尚无本项Books新授/未实际写。拟仅替该marker内原note两段，不增机制正文、不新造owner。拟纠正后内容：

<!-- daily-books-trace:SF-ASYMPO:start -->
- `SF-ASYMPO` — Daily `2026-06-03`；primary `arXiv:2606.03070v1`；2026-06-04补Jun03具名纠错；Books Decision=`暂缓 — 中心桥争议隔离，非已有覆盖`。

  原覆盖映射不成立：正样本使用当前概率、负样本仍用behavior ratio的分支，不等于本v1按整条response平均NLL的stop-gradient归一化。v1局部forward零和与surrogate梯度式不证明off-policy偏差已校正或异步稳定，PPO clipped surrogate也不自动满足其真实ratio有界假设；相关经验结果保留受测math/配置边界，不作普遍稳定证书。v2正式withdrawn不入选或采用，不扩说v1全稿撤回；v3有PDF且incorrectproof comment仍在，不认证已修复。未发现依赖其证明的独立机制正文，本次不改上述通用clipping/freshness原则；需明确勘误、受影响证明/实际稳定化目标与独立复核后才重开正面采用。
<!-- daily-books-trace:SF-ASYMPO:end -->

完整直接两侧（保原样）：

<!-- daily-books-trace:SF-STRAGGLER-AWARE-RL-GROUP:start -->
- `SF-STRAGGLER-AWARE-RL-GROUP` — Daily `2026-06-02`；primary `arXiv:2606.02218v1`；正文锚点“同步 Group Size 也可以由 Straggler Risk 有界调节”。

  **已吸收的语义增量：** 增加在保持同步 on-policy 下按 posterior straggler risk 动态选择 group size。
<!-- daily-books-trace:SF-STRAGGLER-AWARE-RL-GROUP:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15455:start -->
- `SF-2026-ARXIV-2606-15455` — Daily `2026-06-14`；primary `arXiv:2606.15455v1`；Books review `books-review:SF-2026-ARXIV-2606-15455`。

  **已吸收的语义增量：** RLVR 的 diversity collapse 应按 problem saturation/overtraining 解释，并用 zero-success/boundary contribution gate 决定哪些题继续更新。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15455:end -->

原实际待替完整组：

<!-- daily-books-trace:SF-ASYMPO:start -->
- `SF-ASYMPO` — Daily `2026-06-03`；primary `arXiv:2606.03070v1`；Books Decision=`No Change — Existing Coverage`；命题锚点“正负 Advantage 不必共享同一 Clipping Contract”“Asynchronous RL 必须把 Policy Staleness 写进 Advantage”。

  当前正文已经把 current-policy positive branch、behavior-bounded negative branch、stale rollout 风险和标准对称 clipping fallback 写成完整机制；该 family 不再触发新增正文。
<!-- daily-books-trace:SF-ASYMPO:end -->

