# A109 — D²SD04446首次必要 / 正式6分 / actual Ch48两段PRE

最新行政事实：reader R111–112唯一actualPOST已实际采用，整合生效/指定窄位释放，新增I23＋旧Kimi1合24；下文待POST为历史过程，不第三技术。

A111过程：R109–110首次必要/正式6分/actual Ch48小gap及原两段PRE逐字通过，无修句；root fresh双锚新窄授后已真实SAVE/完整自读＋本人true-H2单注，正文在Review notes前，仅待唯一非writer actualPOST，不预I24/DAY。以下准备态为A109历史过程，不再是当前未SAVE待办；23I保持。

当前仅准备必要/actual owner/最小PRE，无新Books授权/SAVE/注/POST/I。FlexNPU R107–108唯一actualPOST已实际采用，23I既成，本人注/Source/Report行政同步后V3先通过，不第三技术。R89–91本项完整题摘/准入/Jun04联合日证复用，不重初筛/GET abs。

## 精确原件及真正读取域

`2606.04446v1` *D^2SD: Accelerating Speculative Decoding with Dual Diffusion Draft Models*。Submitted-v1 `2026-06-03T04:48:00Z`，findable/arxiv.content精确DOI registered `2026-06-04T01:58:51.000Z`，最早公告Jun04 08:00BJT至最晚09:58:51BJT完整同日，R89–91通过，不冒实际公开时刻/全球首稿。原abs/notice与字段在SUP_TITLE_STOP_BATCH4_20261025.md，无已知撤回/纠正信号的有效层复用。

官方HTML `https://arxiv.org/html/2606.04446v1` GET200/304147bytes，原件SUP_2606.04446v1_20261025.html，SHA256 `fc9ff68b0d991693c58801572d1cbcafff22a64945fb6e62c5ac70bbeb01b5d0`。实际读§1–4/Eq1–7/T1–7、Fig1–2完整说明/§6结论；§5只是作者关系描述，不代各引用已核。未看曲线像素、核代码/训练checkpoint/复现或真实服务；HTML无附录保证分支需扩审，不为没采用的采样exactness补全代码或全附件。

## 必要支持与直接反侧

§2–3：第一DFlash式drafter读取target已接受hidden features的KV注入与bonus anchor，剩余γ−1 masked位置一次并行输出；c_k为该位置argmax概率。Eq4将前i项confidence连乘×下一项1−c作为拒绝边界评分，i=0…γ−2，选TopK不同prefix长度而非直接把更多token全送verify。它没有包含“全γ−1接受”的剩余质量，作为分支排序可用但不是完整归一后验；GSM8K token-bin校准图不能自动证明完整条件hazard/联合独立性或跨任务校准。只采启发式拒绝位置proposal，不将其写成真实target拒绝概率、最优树或提交权限。

第二VP-Drafter保anchor及前i个第一草稿token，重mask剩余位置，K份可变前缀一次batch另forward。§3.4/Eq6–7用截断几何β^j训练prefix长度，首l+1为ground-truth，其后masked；loss按距重锚边界exp(−(k−l−1)/τ)衰减并按weights归一。不同mask/training分布不是新architecture；训练GT前缀与在线仍未被target验证的第一草稿前缀有exposure差，不授训练已覆盖任意错误prefix。β/τ具体值、layer/参数量、训练步/算力/seed等未充分披露，不能照做完整recipe。

§3.3将原链＋K重锚分支以shared-prefix cascade attention联合target verify，然后longest accepted prefix search/bonus更新，下一cycle消费target和两drafter verified KV。此处没有完整tree mask/position/KV复制提交回滚规范；greedy每条accepted path须逐token匹配当前完整prefix才能提交，draft c仅决定候选。T1 sampling评价有数值却未写完整dependent-proposal接受/重复分支处理/拒绝residual及随机路径选择协议，不凭“target一次验证/cascade”继承原始rejection-sampling的target-law保证。本文只采用proposal预算和训练接口、费用反侧，不采用随机无损或实现已验结论，故不为未采用保证扩全部代码。

§4.1：target Qwen3-8B/GPT-OSS-20B、NVIDIA H200（实际GPU数/TP/并发batch/输入输出预算/完整计时协议未充分披露）、BF16/FlashAttention2，FlashInfer cascade与预热VP/target CUDA graph、Transformers/SpecForge。各drafter PerfectBlend target生成回答训练，完整训练预算/seed/CI/任务输出质量与target分布一致性未给出。默认γ16/K4。Eq1 α含bonus，T1 caption TPF与后表α不可静默统一不同人口；接受长度非验证预算/完整SLO。

T1 block8→16→24→32在“各自decay-matched optimal schedule”下GSM8K TPF5→5.95→6→5.93，并非固定checkpoint单独改长度或端到端时间。T3八任务Qwen greedy均值speedup4.16→4.98/α5.31→7.05，sampling3.43→4.01/4.33→5.45；速度均值是八任务ratio算术均值，不是聚合goodput/训练全费。T4 GPT sampling中LiveCodeBench DFlash1.68→D²SD1.62、MT1.60→1.59、Alpaca1.58相等，直接否定“both metrics consistently”文字的普遍口径；保其余改善，不删反退、不把更多α当实测必快。

T5四任务同K4/cascade下naive同一logits采样5.75→6.08α/4.48→5.06speedup，D²SD7.62/5.35。T6保重锚pipeline、复用DFlash作第二draft为6.53/4.69，VP训练后7.62/5.35，支持区别放置与variable-prefix适配；但没有分别隔离β prior/anchor-weight loss/额外模型容量训练预算，不能唯一归因某项或证明不同inductive bias必需。共享softmax大多token概率非零，不能把作者“不能到support外”当所有naive resampling无效的理论证明。

T7加第三级同四任务α7.62→8.24而speedup5.35→5.13（每任务都降），说明额外forward和验证工作压过边际进度；作者以Eq2倒推约13%轮成本不是独立细粒度overhead测量。第二级也不是免费：训练两drafter、额外权重/KV、mask/topK构建、graph预热、共享prefix管理与验证均付费。小block/低熵/高并发或校准失配可保原DFlash/单树/target-only，不签无限叠级或所有硬件增益。

## 正式评分与actual owner

Design Delta2＋System Reach2＋Durability2＝6：只给拒绝位置启发式→共享prefix重锚候选与variable-prefix训练人口联动、以及第三层反退修正预算选择这一跨draft训练—verify工作量接口；不按成熟tree/置信分数/并行diffusion或headline速度加分。具体小gap必要深入，支持和反侧足停止。

唯一owner `INFER-SPECULATIVE-DECODING` Ch48。实读248–287 acceptance≠speedup、verify length/prefix survival/删失与真实batch机会费，344–363联合depth/verify policy与ECHO gates，934–963 stochastic factorization/渐进tree/来源异质性/AR verifier边界；邻Ch47物理KV与Ch49execution plan真实开篇。当前渐进tree/两来源spine已有confidence/预算、target唯一commit、scope/full费，不能以主题相近冒NC；尚未具体解释一条并行block在预测拒绝边界重锚第二个训练mask匹配的draft、联合共享prefix验证且叠级按边际全费停止的接口。exact family/题名定点未见既成链，不以无marker定gap。拟两段仅在Ch48“渐进tree coverage/waste”完整段之后/来源异质性完整段之前，不重推经典接受采样/全章。

### 完整直接上锚

> 固定宽度 tree draft 易实现，却会在不确定分支上生成大量最终被拒 token；只走一条 greedy draft 成本低，又可能错过高概率替代路径。渐进 tree 分支根据局部置信与剩余验证预算逐层扩展，controller 拥有 expansion policy，target model 仍拥有 acceptance 与最终 token commit。它用额外 tree state 和不规则 kernel 换取更好的 coverage/waste 平衡，短输出或 acceptance 已高时线性 draft 仍更简单。

### 完整直接下锚

> 当一棵树混用不同来源的候选时，局部置信还不够：上下文匹配的连续片段与历史 logit 转移候选可能具有不同接受率。若仍按来源无关的概率分配验证节点，就会把深度浪费在低接受率路径上。一个有条件的分支是在固定节点预算内，让高接受率来源形成深 spine、低接受率来源在各层提供较宽 fallback；target 仍统一验证，只提交通过的前缀。这样优化的是每次验证的预期 accepted progress，代价是来源级接受率估计、随 workload 漂移的树形选择和不规则验证布局。相关理论依赖候选接受事件的近似独立与来源异质性；作者五个模型、五个数据集、greedy batch-1 的结果不证明 sampling、并发或生产尾延迟普遍受益。来源差异不稳定或估计开销过高时，原来的单源链/固定树仍是更稳的基线。来源异质性也不能独占实测收益归因：Qwen3-8B 五任务中保留非对称 shape、换掉 context-source tokens 后宏平均 τ 未降（+0.2%），单项仍可略降；同预算12–33%比较的是 accepted-token 进度而非 wall-clock 加速。全深度候选的边缘匹配概率连乘未处理已选父路径可达性，因此不采用全域严格支配或非退化保证，预算仍需在可达路径下校准并计实际构建／验证费用。<!-- source-family:SF-2026-ARXIV-2604-02047 -->

## 原两段最小PRE（R109逐字通过，A111已真实SAVE待唯一POST）

并行block draft还可把预算分给“在哪里重起一条后缀”，而不只延长原链或逐层加宽。第一草稿一次给出整块token和位置置信，再将前缀存活与下一位置拒绝的乘积作为启发式评分，选若干重锚点；保留各自原草稿前缀，由第二个variable-prefix drafter一次batch填其余mask，再把原链与这些共享prefix分支交target验证。[一个受限双draft分支](https://arxiv.org/html/2606.04446v1)为第二drafter训练可变可见前缀，并提高重锚附近masked位置的loss权重，避免把固定anchor训练的模型直接用于未见mask布局。评分只是候选放置依据，token-bin校准不证明真实条件拒绝后验；保留的原草稿前缀也尚未获提交，仍须target按完整路径验证。

重锚位置与第二draft训练适配须分开验，不能把同分支数当同训练成本，也不能以更多接受token证明更快。有限消融中，复用原drafter重锚可提高进度却未达到可变前缀训练分支；再加第三级反而因额外forward与验证费降低速度，部分sampling任务也比原DFlash慢。两drafter权重/KV、训练、topK/mask、graph预热及共享prefix验证均计费；若要声称随机target law不变，还须独立闭合候选相关性、接受/拒绝纠正与KV提交回滚协议，不能由cascade attention名称代证。校准、训练人口、状态身份或净费用不合时，保短block/固定树、原单drafter和target-only，不把有限任务均值或greedy路径结果授给任意采样、并发与SLO。<!-- source-family:SF-2026-ARXIV-2606-04446 -->

## 精确停止

本单篇首次必要/正式6分/actual Ch48小gap/原两段PRE ready交唯一reader，不等余三Batch4与两cue。无Books新授权/SAVE/注/POST/I，I23保持；finite stop/六节/DAY仍ordinary，04032与DistIL保原隔离，不扩NAV/代码/附件。State/index/他日未改，无stage/commit/push。

## A111 — 新窄授后真实SAVE/selfread，待唯一actualPOST

实际完整采用R109–110原域/原两段逐字PRE，无修句、不第三AB/date/必要。root本轮fresh完整双锚新窄授后，仅将以上原两段保存Ch48渐进tree完整段后/来源异质性完整段前，既有末尾family marker保一处、不另重复；章末本人true-H2 Review notes下一条完整来源注。真实读回完整新增/完整直接上段/完整直接下段/本人整注；正文两段都在唯一Review notes前，最近机制标题为Draft coverage/waste，不落注释区或拆旧semantic binding。保启发式/未提交前缀、T6分责/T7反退/sampling局部慢、全费/采样协议未闭与原退路，不扩大采用。

写前快照 `/private/tmp/d2sd-0605-save.9sliXa/ch48-before.md`；before SHA256 `586ca321493255991675777fbf1cb6c2c4aedfb922a3369629b088715382880a`，after `168b45c7e037389c40edd96ae25b81275defce81717ef904f5d89d5bad066917`。只逆除本原两段及章末本人单注/新增分隔后整章字节等写前；literal连文/正文marker/本人注各唯一，body_before_trueH2与note_after_trueH2正确，保护完整两侧/旧binding/他注和并发全部内容。不以检查代实际语义阅读。

Report本项同步R109–110/PRE及A111真实SAVE/待唯一POST，29=23I/4NC/1争议＋1待POST，未预I24。当前V3只本普通Books枚举失败如实保存，不冒暂缓/改脚本合同。ready立即交root/唯一reader实际POST释放，不读下一Methods，不写State/index/他日，不保留跨阶段授写，无stage/commit/push。
