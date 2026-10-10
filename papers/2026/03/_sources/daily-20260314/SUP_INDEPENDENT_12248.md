# 12248 EBFT：独立必要 Source／评分／owner／PRE

复核者：mar13_admission_review（非本项准备者）；2026-10-10。唯一上下文为 03-14 Daily 补充 2026-03-13 北京时间完整自然日与 2603.12248 的 exact-v1。重新完整读取当前 AGENTS、Research／Report 合同、统一 Prompt、Sources 使用说明／Daily 分组／arXiv 范围及本日 README 停点、ROADMAP 和最新相关 checkpoint。上下文隔离技能用于限定本日、本项；不继承另一日期候选判断。此前有效题摘准入和十项日期独核复用，不重新推断 first-public，不读异日候选。

## 1. 原证身份与真实阅读范围

实际读取准备包 `SUP_EVIDENCE_12248.md`，但不以其结论替代原证。实际核 `SUP_NARROW_EBFT_MANIFEST_RESULT.json`：URL／final URL 均为 `https://arxiv.org/html/2603.12248v1`，GET 200，1083942 bytes，UTC 2026-10-10T01:46:31.966636Z。实际读取其 `SUP_NECESSARY_12248.raw` 身份与 `SUP_NECESSARY_12248.txt` 必要原文，未以 current v2 替换 v1。

必要原证范围：§2.1–2.4 的条件均值目标、特征构造、Eq1–9 和 Alg1；主 Table1 支持／直接负侧；§3 训练人口、指标与选择口径；§4 的目标与表示反侧；§6 的短 rollout／7B／每更新费用限制；Appendix E 的 Eq90–94 配对奖励和 corrected baseline；F 的 nested prefixes、G 次生成与 custom attention matrix；G 的实际 EBFT／SFT／RLVR 配置、H100 时间和完整 Table6 的 coding／translation 行；H.1 的 α／γ 直接反侧。公式在文本中有展开、重复和印刷不一致，按必要原位置恢复读取，不以搜索摘句替代完整决定段。未要求 D 全证明、所有 H 图／例子、像素、源代码或全部引用；本记录不授那些范围已核。

## 2. Source 裁决：受限通过

真正改变监督对象的是：在给定 prefix 下，将 actor 续写的条件平均特征与 data 条件平均特征匹配。CFM 用单个参考 completion 提供监督，理想固定特征下与 FM 相差参数无关的参考特征方差；这不是逐条 teacher hidden-state 蒸馏或 CE 的另一种等价求值。Eq6–7 的 reference alignment 和 actor–actor 相似项分别提供吸引与排斥，后者不由“两个答案都正确”的 verifier 授权。

采用界限实际成立：严格 proper／完整分布识别要求 feature 均值足够丰富、能识别分布；原文仅 hypothesize 冻结网络的有限表示接近这一条件。原 Eq2 的 Var 定义缺平方，不能逐字认证该印刷公式；不采用它，也不因此抹掉有限目标和实际实验。不能从有限表示、单位归一或较低 CFM loss 推出完整语义／事实分布已校准。

E Eq90–94 直接支持特定样本依赖断点：仅去掉当前条目的其他 reward 均值仍经其他 reward 的 pairwise 项包含当前 sample。修正须同时去掉这项贡献，并把相似项的分母从 `n−1` 改为 `n−2`；原修正要求 `n>2`，实际 G Table2 的 n=4。固定 feature、同 prefix 的条件 i.i.d. 采样才支持该独立 baseline 的估计说明。Eq94 第一行仍印 naive 表达、后两行是修正表达，不认证三行逐字恒等，更不授整套代码正确。该修正也不证明 n=2 时不存在其他合法 baseline。

实际 Eq8–9 使用同批样本 second-moment pseudoinverse whitening，且只 normalize alignment；其几何依赖样本本身。固定 φ 的 Eq7 估计身份不自动传给同批 whitening、α 偏置、std／clipping 或任意 GRPO 实现。H.1 的 α<1、γ=0 反侧限制普遍 fidelity／CE 改善；实际 KL coefficient=0，理论 KL／EBM 解释不成为已训练 energy head 的实证。

F 原文和 attention matrix 支持多个 data 给定 prefix 后分别抽取短 continuation，生成需 G 次 forward，特征可批处理；矩阵不允许短 rollout 查看其他 anchor 的续写或其未来 gold。它不是 G 个连续 token 全并行，也不是完整部署轨迹的人口匹配。Quiet-STaR 的既有 mask 原理不计本项新增贡献。

直接评价反侧实际核到：Table1 的 coding pass@4 EBFT .659 低于 RLVR .660（warm 分支 .658<.662）；Table6 MultiPL-E greedy EBFT .524<RLVR .531，WMT’22 COMET .740<SFT .747，OpenSubtitles COMET .700<SFT .701。保留其他有限改善，但不采用正文／表注“全项无取舍”的强概括。Table1 best-per-method 与 Table6 不是一套统一 matched recipe；translation best-of-k 为按参考指标取最大，不认证部署 selector。CE 口径差异不拼成每人口、每模型都更低的结论。

G 的 n=4、短 G=8／8／4、stride=8／8／2、1024 序列与 RLVR n=8、1024 generation、不同 batch／temperature，和 five-epoch SFT／2048 配置并不构成总 tokens／FLOPs 等预算证明。Q&A 一 epoch SFT 单 H100 .5h、RLVR 两 H100 约28h、未优化 EBFT 约36h；EBFT 此句未披露 GPU 数，不补齐硬件等价。§6 直接承认每更新慢于 SFT。冻结 feature、rollout、统计、参考制备与调参均付费，故原 PRE 的费用与回退限定有直接支持。

## 3. 评分与 actual owner：5 分，非 NC

独立接受 Design 2 + Reach 1 + Durability 2 = 5。新增命题是固定 feature 的条件 sequence-moment 监督，以及配对 reward 如何改变 leave-one-out 构造；不是 REINFORCE、一般 baseline 独立性、Adam、whitening 或并行 mask 本身的新发明。先改变适配训练的目标组件，不能因跨章 handoff／任务数量提高 Reach。有限表示支持、采样依赖与真值分权可复用，支持 Durability 2。标准必要 Source 已完成；实际具体差额触发窄深入，不以已花时间或拟写 Books 数量倒推评分。

actual TRAIN-SFT owner 是 `books/part-04-training-system/29-sft.md`。完整顺读插入局部 47–114：schema／拒答与 ChunkFT → 条件最大似然公式 → masked response CE → “Logits 仍是 [B,T,V]” → Concept Tokens → ER-CE／多语校准／人票 soft target／多语和 nuisance 表示分支。原文没有 actor rollout 平均 feature 与 reference moment、actor–actor repulsion 或其特定 pairwise baseline。原 283–303 的 latent teacher/student、早期引导与 Veto 固定 Q 分支也不是这个目标，因此不能仅凭“已有 representation alignment／on-policy”判 NC。

actual `books/part-04-training-system/33-grpo.md` 50–73 的参考似然 reward／θ 直接导数／latent cluster，以及 475–486 的 group coupling／条件 i.i.d.／LOO 重标度，已承载通用 PG 和 baseline 原理。这里应精确交接，不复制通用 owner；既有原则不消除 Ch29 新的监督对象差额。两段插在 Ch29 “Logits 仍是…”之后、Concept Tokens 之前可承载这条有限分支，保留 CE 数学标题与既有分支，不将其写成 CE 已被替代。

## 4. PRE：仅一处必要修正后通过

原第二段“须连其他项内这份贡献也排除，再核对实际梯度”缺显式重归一与原修正的 n>2 定义域。最小修改为“须连其他项内这份贡献也排除，并按剩余样本重新归一；原修正版要求同一 prefix 下条件独立采样数 n>2，再核对实际梯度”。其余收益、费用、真值／特征支持／实现边界可采用。以下冻结两段准确提案供 root 写；这是 PRE，不是实际 Books 写入验收。

条件最大似然适合复现经核验的 demonstration，但每步 teacher-forced likelihood 不直接度量模型自己续写后的序列分布。若没有可靠 outcome verifier，可以进入另一条 rollout 辅助适配分支：冻结一份 feature network，把各给定 prefix 下模型续写的平均特征，与参考 completion 的特征矩匹配。相应奖励既拉近 sample 与 reference，也以其他模型 samples 的相似项制约只向一个模式聚拢；这是改变监督对象，不是把 CE 换一种等价计算，更不是让 frozen hidden features 取得正确性权限。[EBFT 的受限目标与对照](https://arxiv.org/html/2603.12248v1)只在足够丰富、均值能识别分布的 feature 条件下连接完整分布校准；实际有限表示、短 rollout 与 reference 人口仍可能漏掉事实或有效模式，CE 和独立任务验收应分别保留。<!-- source-family:SF-2026-ARXIV-2603-12248 -->

这一奖励构造还要求具体采样依赖可见：其他 sample 的 reward 若通过两两相似项含有当前 sample，仅从 reward 均值中去掉当前条目，仍不是与当前样本独立的 leave-one-out baseline；须连其他项内这份贡献也排除，并按剩余样本重新归一；原修正版要求同一 prefix 下条件独立采样数 n>2，再核对实际梯度。该固定 feature 下的估计条件不能自动传给同批 whitening、偏置权重或 clipped/normalized 实现。[第33章](./33-grpo.md)仍拥有通用 policy-gradient 与 baseline 的分责。多个 nested prefixes 可共享原序列计算并批量抽取特征，但各短续写只能看自己的已给 prefix/采样历史；它不使整个部署轨迹变成已匹配人口。冻结网络、rollout、特征与统计求值、参考制备和调参均付费，作者部分任务仍弱于基线且每步比 SFT 慢；特征支持失配、行为回归或总预算不合算时，保留普通 verified CE、可靠 outcome 更新或原 checkpoint，不以更低特征 loss 自签忠实和无损。

## 5. 终态与权限

Source 受限 PASS；5 分、Ch29 唯一 owner 与具体新增差额 PASS；PRE 按上述一处修正版 PASS。没有向作者摘要授全证明／全实现正确，没有消去真实负侧。只写本文件，没有改 Report、Books、LEARNING_STATE 或共享 ledger，没有 stage／commit／push。后续实际写入需另由非 writer 顺读实际正文与邻接／末注回源，本包不授 POST 或 DAY。
