# VLA SAE19183：离线特征诊断与动作环方向干预的分责

resume_mar18 sole准备，仅03-21补BJT03-20。实际完整exact-v1题摘的具体准入已root独校：通常只能从动作结果回看表示→新增跨episode时间统计筛选与字典方向闭环干预接口→需要把诊断标签、运行hook身份和真实任务影响分开验收。拟2+2+2=6，新增的是诊断—动作消费者的受限接口，不给既有SAE/可解释不等安全的一般原则加分。必要支持及直接反侧足够停止；未自授Source/PRE、写锁、safe或DAY。

## 身份、当前信号与日期

实际[official exact-v1 abs](https://arxiv.org/abs/2603.19183v1)完整题摘/header/history，五作者Aiden Swann、Lachlain McGranahan、Hugo Buurmeijer、Monroe Kennedy III、Mac Schwager。当前v2 Jun6摘要增加真实DROID硬件等结果，但当前页没有具体撤回/纠错说明；本次只采用March exact-v1，不把后来硬件结果移作本窗新首次公开，也不为版本号全版比较。

实际DataCite arXiv-issued DOI原字段findable：v1Submitted2026-03-19T17:42:05Z、v1Updated2026-03-20T01:18:36Z；Available只有2026-03，created/registered2026-03-20T02:30:35Z。沿本批BJT03-20官方批次/登记夹证限定日级归属，不把提交当公开、不补公告精确时刻或声称别处从未先公开。v2SubmittedJun6/UpdatedJun9不替换v1。完整原AB同SUP_FINITE_REMAINDER_EXACT_AB_20261011.json。

## 最低充分原证与直接反侧

实际[exact-v1 HTML](https://arxiv.org/html/2603.19183v1) §3.1–3.4（L128–233）、§4.1–4.2/T1–2（234–276）、§4.3必要特征语义及§4.4闭环（279–323）、§4.5与§5–6（326–345），必要A.1（388–417）、A.5稀有特征反例（468–471）及A.6（472–481）。不遍网站视频、所有特征图、per-token探索附件或代码；未复现。

- 方法拟合TopK/AuxK SAE于每步池化residual；四统计为至少一次触发的episode占比、每active episode onset数、每episode峰幅的平均、相对持续时长。不是平均全部时间点激活，也不是任务成功概率。人工先查随机episode/top features，再查top10 diverse及viewed held-out episodes，歧义排除；每数据集30人工特征(15+15)单层训练logistic classifier后应用其他层/模型，LOO不认证独立OOD泛化。解释标签、general/memorized标签、真实控制收益三者不同。
- 干预读单位decoder列方向，向指定层residual加入alpha倍并broadcast sequence维度，原文称每denoising step。A.1.3采集PG是prefill、AE是最后去噪；A.6运行hook覆盖10次去噪，故采集人口/阶段与运行消费者必须分账，不把整个PG重复前向或具体hook实现猜成已核。π0.5每次预测50步，仅执行前5步再重观测；干预自环境step10到末尾。OpenVLA逐环境步requery是不同消费者。
- §4.4同一pre-grasp方向让机器人接近后悬停、不拾取；transport方向在三任务跳过抓取直向目标，其中碰撞篮子并推开。证明局部行为可改变，不证明提高成功率/唯一语义回路/安全。§6明确clean features可能不可靠或不可预测地steer。
- A.5跨scene的lid feature因占比小/近一次onset被判memorized，稀有语义不等记忆；§4.5 classifier median训练步趋势非严格单调，KI/data不同混杂，原文自己只weakly suggests并要求更多验证。不采无rollout的泛化认证、遗忘因果、已实现runtime alarm或model improvement。
- T1为120个手标样本95interpretable，有限操作标签非所有VLA真值；T3 LIBERO40任务但正文另写130，指令数不等任务数。A.1.3默认三相机patch描述与另处两相机/替代per-token口径未齐，不采精确token/camera recipe或数据全覆盖保证。DROID这里只2K子集，原训练75K不是本次SAE人口；OpenVLA checkpoint/spatial与collection Goal不得自动当完全匹配。
- v1闭环只是LIBERO simulation，无硬件。A.6随机方向/layer实验测平均EEF位移，不是任务成功、安全或现实deadline。收集/存储、字典训练、人工分类与校准、运行hook、闭环rollout全部付费；端到端额外latency、precision、部署硬件/控制deadline/碰撞全率未完整披露。不把motion仍有目标当成功或生产鲁棒。

## Actual唯一owner与差额

已实际重载Books背景/理念/写作，唯一拟owner `MULTIMODAL-EMBODIED-VLA`/[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，实际完整1320–1353及相邻Ch25/27开篇。Ch26 1345/1347现有pixel→latent action、代数诊断与闭环gate，并没有具体的episode统计筛选→SAE decoder方向→动作去噪/执行时钟接口。Ch66实际276–298已有SAE重建/解释/任务干预分账和内部sensor；不复制通用SAE机制。拟位在Ch26当前1347诊断段完整后、1349 predictive hidden段前。保留旧便宜诊断/显式动作及安全层，不覆盖原latent训练机制。

## 逐字最小PRE（未授写）

可解释的潜在方向还可成为干预提案，但它从离线诊断进入动作环时，消费者身份已经改变。一个受限分支在轨迹的池化residual上训练稀疏字典，用跨episode触发比例、onset次数、峰幅与相对持续时长筛出待检特征，再把选定的单位decoder方向加到冻结策略的指定层residual，绑定剂量、token作用范围、去噪阶段和重新观测时钟；离线采集末去噪状态，不等于运行时对全部去噪阶段干预。统计分类只描述当前数据人口中的人工标签，稀有但跨场景一致的语义可能被错判为记忆。[有限模拟闭环](https://arxiv.org/html/2603.19183v1#S4.SS4)中，pre-grasp方向使策略接近后悬停而不拾取，transport方向使它跳过抓取直向目标，甚至碰撞篮子；改变动作并不等于提高任务成功或获得安全控制。字典/activation存储、人工校准、hook和闭环rollout都付费，v1未有硬件或端到端控制deadline验证；特征或剂量失准时应停用干预、重新观测并保留冻结base policy、原controller与安全层，不让诊断标签取得物理提交权。<!-- source-family:SF-2026-ARXIV-2603-19183 -->

静态本人源注逐字：

- 2026-03-21 source supplement — [Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models, exact-v1](https://arxiv.org/html/2603.19183v1)：必要§3.1–3.4/§4.1–4.5/T1–2/§5–6、A.1/A.5稀有标签反例/A.6已审；仅采用池化轨迹诊断与单位decoder方向的动作消费者接口，保人工分类人口、末去噪采集与运行hook差异、悬停/跳抓碰撞、sim-only与全部费用边界；不采一般泛化/安全/唯一因果或当前v2硬件结果，未核代码/未复现。

提交root非准备者必要Source/actual owner/PRE有限裁。无锁不写Books；通过后root协调唯一窄锁，写后一次非writer完整局部/本人静态注POST即可，不动态验收身份循环。

## root 非准备者必要审阅与 PRE 裁决

2026-10-12 root实际打开v1 §3.2–3.4必要统计/分类/单位decoder公式、§4.4直接悬停/跳抓碰撞结果及§6、A.1.3采集口径与A.5/A.6；复用未变化的identity/date依据。实际Ch26 1338–1353顺读代数诊断→动作消费者→predictive hidden与Ch23/25交接，逐字核本段及本人静态注。有限Source/PRE PASS：只把episode统计与动作hook接口融入既有诊断论证，人工general标签不是泛化/任务成功概率，干预clock与采集clock分开，v1仿真与真实控制边界近文。未核代码/全部附件或复现。授作者本段及本人静态注窄写，未实际POST前不计safe或DAY。

## root 一次非writer actual POST

作者按原onePRE/static写入后，root实际完整顺读Ch26 1341–1356和章末本人注/相邻注，逐字回对原PRE及有效必要原证：代数诊断的便宜指标→内部方向作为干预提案→predictive hidden训练目标交接保持，统计分类与物理效果分责、采集/运行clock、悬停/跳抓碰撞反侧及费用/回退均近文，无旧内容替换。本人family marker正文唯一，静态没有v2硬件或安全保证；限定diff-check通过。实际POST有限PASS，接纳本项actual Integration并释放窄锁，不授整日DAY或无遗漏。
