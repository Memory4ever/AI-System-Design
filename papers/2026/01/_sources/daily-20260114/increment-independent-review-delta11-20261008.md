# Jan14 独立必要复核 delta11：07200 SOT /07411 SCALPEL

复核者：review_jan15_delta（非作者）。仅 root 授权的已 ready 两项；不扩大附件、版本史或其他日期。压缩恢复重读 AGENTS、当前 Research/Report 合同、每日来源/Prompt/ROADMAP、本日 supplement 与当前路由；Books 判断前读 PROJECT_CONTEXT、学习方法、写作指南及实际 owner 邻接。补窗仍 BJT 2026-01-13 完整自然日，原17、原窗口/日期/评分不动。本文件只记录独判，不修改 Report/Books/LS/索引，不 stage/commit/push，不授 DAY。

## 共同身份、准入与必要原证

两项完整题摘实际读本日五个 increment-abstracts 文件的对应行；新增命题清楚，均非借成熟 LoRA/OT 或主题映射倒推准入。两项各 2+1+2=5。采用 exact-v1：

- [07200 v1](https://arxiv.org/html/2601.07200v1)：本日 increment-necessary-core-2601.07200v1-20261008.json 的 §4/5/7 和 necessaryAppendix A1.SS1/A1.SS4/A1.SS11 原文实际读完。因确认长期差额，深入受影响的质量边际/计划/权重、关键反侧与全费，未扩其他附录。
- [07411 v1](https://arxiv.org/html/2601.07411v1)：increment-necessary-core-2601.07411v1-20261008.json 的 §3/4/5 原文实际读完；重点 Eq1–8、Table1–3、baseline/dev selection 与作者因果解释。中心公式争议触发受影响内容深入，未核代码/复现或扩整份附件。

日期复用本日已核正常公告/ID 下界，结合 increment-date-bounds-rest-20261007.json：07200 Updated-v1 Jan13 02:04:13Z → registered03:57:13Z；07411 02:15:56Z →04:02:14Z。仅归 BJT Jan13，不拿 Submitted 或 registered 单证，不追秒。必要正文未提供可改变归属的更早公开线索。当前官方 abs 两页独立轻读均 v1，无具体撤回/纠错说明；与 increment-current-identity-next9-20261008.json 对应两行一致，不作全历史无信号保证。

## 07200 SOT — 5 / 窄 TRAIN-DATA PRE PASS

准入链：独立质量评分/固定 mixture 在易复算、参考稀缺时合理；新增 frozen safety-aligned full(x,y) 最后 token 表示上的全 corpus simplex mass 分配，由两份有行列边际的 transport 计划分别拉向 task-specific safe、远离 harmful reference；若参考可信且匹配，数据选择可以表达分布间质量耦合，而不只独立给每个样本打分。这是选择几何的替代分支，不是通用 OT 成熟原理本身的分数。

§4 明确 shared custom mass w≥0/和1，safe/harm 的参考质量固定均匀；cost 为 frozen representation cosine。两份计划随 w 变化，不能把预先固定的成对成本线性组合写成完整外层 solver 或梯度保证。TopK 后训练权是 exp(w_i) 再归一，不是直接重归一 w_i。本轮拟写结构分工而非数学可运行 recipe；entropy OT、语义几何或作者所谓 safety boundary 都不授硬安全/权限/真值。

评价与关键反侧足够：5000 custom、人工 HH harmful 混入 p=.1；50 task-safe、5000 BeaverTails harmful、K4000、四4–8B backbone、2epoch；A1 q/v LoRA r16/alpha16、bf16、AdamW。帮助性1000任务实例 Kimi/DeepSeek 1–5、人身危害1000 HH test/DeepSeek-V3；精确 judge revision、完整独立重复/seed及硬件 Not Disclosed。不得将拼合 Avg 视作独立安全真值。Table1 Llama AGNews .859<SFT .876、MetaMath HpS3.602<SafeInstr3.676/ALPAGASUS3.884；Table3 general-safe HmS .543>SFT .426，task anchor 匹配必要但不是充分生产安全保证；another-harm .194略好于默认 .197，不采所有默认模块或参考唯一最优。§7 覆盖、坏 anchor、静态未知攻击和 LLM judge 局限保留。

A11 selection11m08/30.61GB + fine-tune33m56/22.47GB，对 SFT38m19/27.41GB；阶段峰值不相加。80%训练子集不免 representation、双计划/Sinkhorn 与参考维护成本，不采免费/全流程加速。

实际顺读 Ch27:1068–1148：1091 general gradient 更新约束、1103 optimizer-aware 虚拟更新、1105目标梯度子空间、1109 Navigator/anchor gradient mixture，以及在线 selector 的当前 policy loop 均不等上述 shared-mass、有边际双参考分配；不能因同为几何说精确 Existing。唯一 owner TRAIN-DATA。最小差额为 1095 在线选择标题前一短段，解释独立质量→耦合分配、冻结参考与训练 owner 分工、matched-anchor/unknown-harm/全费与回退；不复制 Ch29 loss 或 Ch72 authority。root 已授作者该短段及自身末注锁。PRE 非实际写后，不计正式整合，等待非 writer actual POST。

## 07411 SCALPEL — 5 / 中心争议隔离，无 Books 正证

准入链：整组件 corruption 混合原内容与 OOD 后续轨迹；新增冻结 W0 的低秩 BA 监督干预，联用 general-text LoRA 输出 L2 和 A/B norm/L1，尝试更局部地降低目标能力。改变干预单位的潜力成立，非仅名称组合；能力降低的受测结果不会因中心解释争议被全删。

决定性冲突在 §3.1/3.3：目标文字称 correct/wrong 等概率，Eq3 是 log p(correct)−log p(wrong)，Eq4 是长度平均概率的同一 signed gap，Eq1/8 直接最小化，没有 absolute/square 或零点停止规则。复核者反例（不是作者实验）：二项 p+=sigmoid(z)、p−=1−p+ 时 gap=z，纯最小化向负值而非停 z=0。正则可平衡大小，不能保证驻点为零；不给印刷公式补绝对值、反向符号或隐含实现修复。因而不采等概率配方、精确机制解释或选择性能力因果 substrate。

§4 的有限下降结果保留：Llama3.2-1B/A10080GB、rank2/alpha16、lr1e-5、batch40、20epochs；ClaudeOpus4.5 合成每 task200–400、人工筛80/10/10，另24任务各约50测试和67 BLiMP。基线各任务 Top10 components 后 noise，SCALPEL 是 joint-trained regularized adapter；dev 最大 AccDrop×Cap 选超参，不是只变干预单位/同搜索与训练预算的控制。Table1 baselinePPL11.1/Cap.50，translationPPL11.2/Cap.49、commonsenseCap.47；Table2 Llama ΔCap−.03，不能称完全不影响其余能力。Table3 Moral rank1 ΔAcc−.44 vsrank2−.28，非 rank2全任务最优。低秩拟合可降低受测 accuracy，不证明原能力固有唯一/最小低维空间或真正遗忘；learned BA norm 依赖优化/数据，flatten A/B Pearson 还依赖 factorization/正则选择，不是 intrinsic substrate 的因果证书。合成、baseline/dev噪声搜索、adapter训练与回归全费；precision、重复seed/完整E2E预算 Not Disclosed。

实际 Ch30:780–802 已承 support/内变换分工和 skill-critical probe 非能力真值；Ch66:3082–3140 已承多 baseline 改变被检验因果命题/diagnostic authority。它们没有 SCALPEL exact suppression 配方，故不假称精确 Existing。保持5分，不改低分/Only抹掉中心争议；当前以有限报告观察加中心解释终态隔离处置，无新 Books 段、无锁。不使用等概率、disentanglement/独特 causal substrate 作正证或安全保证。

精确重开：官方修正或可核执行目标及其正确解释（是否针对零点），或独立于等概率解释的完整可核抑制实现；若要主张选择性因果结构，再需匹配干预/训练与搜索预算的 controls、相邻能力回归及 invariant 表示分析。只重开这些命题，不遍历全部版本/证明，不否定低秩干预家族或已报告局部结果。

## 当前状态

07200 窄 PRE 已通知 root/作者，尚无 actual POST；07411 中心争议终判可同步。两项准备/独判不是 DAY，其他普通工作仍由本日路由推进。

## 07200 actual POST PASS（随后实际写入）

root 窄锁下作者已写后，非 writer 实际独读 Ch27:1095 新单段、1089–1117 完整邻接及1594自身注。正文承接 general-data update constraint，先解释独立过滤适用条件，再引入 frozen full(x,y)表示的 shared mass / two marginal plans 数据分配分支，后接 checkpoint-dependent online selection；没有把它写成梯度投影或安全 authority。Top-k 后 exp(w)重新归一身份、非完整 solver、.543>.426参考反侧、selection+training全费、参考漂移及独立筛选/冻结mixture退路均近文。现有 update/optimizer/Navigator 分支及其他正文保留，删论文名称后论证仍独立成立。

actual POST 通过，可以计本日一项实际整合并释放 Ch27 窄锁；作者将自身注的“将顺读/待POST”同步为实际顺读与此非writer POST。限定 Ch27 diff-check0 不替代上述语义验收。SCALPEL仍争议隔离，无Books；本组闭环不是 DAY。下一独立 Jan17 Align 任务不复用这两项结论。
