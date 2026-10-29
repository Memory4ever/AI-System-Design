# Direction22117v1必要Source与具体Books两PRE

首批准入/日期root独核，2+2+3=7不改。作者已顺读[exact-v1](https://arxiv.org/html/2603.22117v1) §3.1～3.3/Alg1、§4.1 Eq7/Theorem4.1条件、§4.2 Eq8/Tables2–3/footnote5、A.1～A.3/Tables4–5、B训练/四runs与D logit-gradient/Tabular NPG范围；本日FIRST_CORE_TEXT第2条保core，不授未读全部附录或code。以下只采用signed probability诊断与probability-aware advantage reweighting，不把所有实验解释或extrapolation优越移为通用规律。

## 必要证据/反侧

Δlogp在同一prefix比较frozen base与finalRL策略，是probability方向而非参数梯度或token真值。Alg1从base抽token，Δ<τ才换RL token（抑制basefavored token），与entropy/divergence/random按replacement ratio比较，轨迹本身会变。A.2有些case低ratio先退、某些case始终零。A.1 ORZ32B/PPO、DAPO32B、UniReason14B/GRPO，AIME24/top-p0.7/T1/max20k/32responses/math_verify；不能把抽样个数当训练seed或claim低prob全是推理能力。

§3.3的unclipped logit L1-gradient含|rA|×(1-p)，不是完整parameter Jacobian；top-p滤掉rare token同时改变rollout分布，不识别唯一因果。Eq8只给原advantage乘[1+α(1-pold)]，不换奖励verifier；Qwen2.5Math7B/3Base8B对DAPO其余hyperparams固定，B每512prompt×16responses、32prompt minibatch共16updates，生成8K/20K与overlong4K/16K。Dominate另cliphigh0.24、默认0.28不稳，不能该列当仅weight独立消融。Table2 Qwen3/AIME24 pass16退，四独立runs只ours7B；response length增加须计成本。Hardware/precision/concurrency/完整GPU-hours/SLO Not Disclosed或不适用，未把少replace率当端到端省费。

Eq7 gated双model extrapolate是新采样分布，不是免费恢复能力；A.3 ORZ/Uni有部分γ/τ退，Theorem4.1仅tabular softmax bandit NPG与存在γ，不认证任意神经网络每步提升。现不把此项sampler写入另一owner，留报告机制/反侧。

## 实际owner差额与具体两段

已读当前Books适用docs/ROADMAP/相关LS及Ch33开篇、195～225 probability/clip分支、600～645 DAPO及现有22117仅Review listing；Ch32/34开篇交接已读。当前概率clip/稀有语义簇/reward归因不等于final-base signed probability诊断与Eq8原advantage乘正weight的新更新接口，TRAIN-GRPO为唯一owner。拟在DAPO四修补与“动态补样…改变实际优化…目标权重”段之后、现有adaptive红队分支之前插两段，不改其它family：

稀疏更新还应区分变化的大小与方向：同一已生成 prefix 上，比较固定 base 与 RL 后模型的 `Δlogp=logπ_RL−logπ_base`，可以标出所抽 token 被偏好还是被抑制；它不是参数梯度，也不判定该 token 正确。一条受限诊断从 base 抽样，只在该 token 的负向差额越门槛时换成 RL 策略的样本，并在近似匹配 replacement 比例下与entropy/divergence等选择比较。轨迹与后续条件会随替换改变，因此局部准确率恢复不证明这些位置是唯一因果来源，也不表示其它domain的能力已迁移。<!-- source-family:SF-2026-ARXIV-2603-22117 -->

诊断可以引出不同于调clipping的更新提案：用行为策略的 `p_old` 给原signed advantage乘 `1+α(1−p_old)`，放大低概率动作的正负信号，而不重标reward或把稀有动作一律奖励。[Direction 的必要对照](https://arxiv.org/html/2603.22117v1)支持这个限定接口；unclipped logit-gradient解释不能替完整参数梯度，top-p过滤也改变rollout人口。受测7B/8B数学任务有pass@k反退、替代weight改变clip及更长response费用，双模型概率诊断和新增校准同样付费；不授普遍能力提升或免费探索。概率/奖励身份不可靠、罕见坏动作被放大或总质量/费用回归时，保留原advantage、已验clipping与独立verifier。<!-- source-family:SF-2026-ARXIV-2603-22117 -->

本人静态注拟：`SF-2026-ARXIV-2603-22117` — Daily2026-03-25补03-24；exact-v1 §3/Alg1、§4.2/Eq8/Tables2–3、A/B；2+2+3=7，signed final-base概率诊断与old-prob positive multiplier保原reward符号；不授完整Jacobian/唯一因果或token真值，Pass@k/clip/长度/预算反侧保留，gated双model extrapolate仅报告不跨owner复制。未核代码或复现实验。

## root 非准备者必要 Source / owner / PRE（2026-10-12）

实际读回精确 v1 §3.1～3.3/Alg1、§4.2 Eq8/Table2 及训练反侧；重新打开官方 HTML A.1～A.3、B，核对替换人口、负向门、额外双模型费用、Qwen3 AIME24 pass@16 反退、Dominate 同时改变 clip、仅 ours 7B 四独立训练 runs。不以 token logit 的 L1 梯度授完整参数 Jacobian 或唯一因果，不采用一般神经网络 extrapolation 定理。正文原两段保留这些边界与退路，必要 Source 通过。

实际顺读 Ch33 195～225 的概率/clip 分支及 602～644 的完整 DAPO→自适应红队→补采邻接；末段已有局部 gradient-vector 诊断不拥有固定 base 与最终策略的 signed probability 对照及 Eq8 的 old-probability 正乘子。唯一 owner TRAIN-GRPO 与提议位置成立；两段及自身静态注 PRE 通过，原 7 分不改。root 授本 family Ch33 两段与自身末注窄写锁，作者写完须实际非 writer POST；本项通过不计 DAY。

## root 一次非 writer actual POST（2026-10-12）

作者按原两 PRE 和自身静态注落实后，root 实际顺读 618～640 的完整 DAPO 收束→两新增段→自适应红队/原 KL 分责→PACED 邻接，以及章末本人/PrivEsc/前邻 SCRL 静态注。signed probability、原优势符号、行为策略概率、梯度权限、替换轨迹反侧和费用/保守回退均保持；没有把双模型 sampler 另复制为推理 owner。实际 POST 通过，接纳整合并释放 Ch33 本 family 窄锁；仅本项，不预整日报完成。
