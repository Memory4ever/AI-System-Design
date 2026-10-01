# 04/29 两项评价潜在线索的必要证据与 owner 校准

仅处理已在题摘池的 `2604.25788v1`、`2604.25591v1`，按官方 exact-v1 的决定性方法、主表和直接限制对读当前章节；不重查日期批次、引用史或全部附件。以下为本日作者侧普通处置提案，不是独立核、冻结候选或 Books 授权。

## KinDER `2604.25788v1`

[官方 §II、§VI Table II–III、§VII–VIII](https://arxiv.org/html/2604.25788v1)将 25 个环境按空间关系、多物体非抓取操纵、工具、组合几何和动力约束组织，意图从感知/语言难度中隔离物理推理。13 类 baseline 输入并不对称：LLMPlan 得 object-centric state 与 skills，VLMPlan 再加 RGB；MPC 用模拟器真值转移/奖励，BP 用人工技能与概念，DP 与 VLA 则是 demonstrations。主表 5 seeds×每 seed 50 episodes，BP 平均 success 0.57、LLMCon/VLMCon 0.43、VLA 0.32；这只能说明当前 harness 与各自资源/先验下的能力和工程成本权衡，不是“经典规划普遍胜 VLA”。作者将 VLMPlan 与 LLMPlan 接近解释为图像未被有效利用，也只是一组**额外图像输入**的行为证据，不能认定视觉内部未用。reward 只对成功 episode 统计，不能与总体成功率混为一个总体效能分母。

§VII 的 real-to-sim-to-real 是 Shelf3D/TidyBot++ 一个示范：相机取得物体位置、模拟中规划、回真机执行；§VIII 明示未覆盖随机性、部分可观测、多本体和多机器人，也未给开放世界 sim-fidelity 或控制安全保证。与当前 Ch26 的感知→state→planner→controller 及闭环风险指标对照，仍有一条可迁移的**评价切片**：要声称“物理推理变好”，须冻结给各方法的状态/图像/技能/动力真值和工程预算，按五物理约束分别测任务成功、成功条件下效率及真实闭环；仅榜单均值不能把输入权限差异归因于 reasoning。拟 `2+1+2=5` Standard/Report Only，暂不据 benchmark 名称写 Ch26；若非作者指出 Ch26 已具体承载这组输入权限控制，可改为窄 Existing，不抹掉本论文局部反例。

## Audio uncertainty `2604.25591v1`

[官方 §IV–V Tables I–III、§VIII](https://arxiv.org/html/2604.25591v1)比较 discrete/ordinary semantic entropy、P(True)、predictive/normalized token entropy，三模型为 Qwen2.5-Omni 7B/3B 与 Audio Flamingo 3。一般音频理解/推理四 benchmark 上语义与 self-verification 方法通常优于 token-level；但 AQUA-Bench 中 Qwen 7B 的 P(True) AUROC `0.79` 最好、Qwen 3B 的 normalized entropy `0.75` 最好；Audio-Hallucination 中 Audio Flamingo 3 的 normalized entropy `0.78` 高于 semantic entropy `0.75`。因此一般 reasoning 的 estimator 排名不能原样签发 unanswerable/hallucination release Gate，必须按模型×任务、perception/reasoning 与 AUROC/AURAC 分层。AUROC 是错误排序，AURAC 是 selective prediction 的风险—覆盖曲线，均不等于一个已在部署分布校准的 abstention 阈值。

§VIII 明说答案空间较受限，方法从文本 LLM 借来、未显式建模音频感知不确定性；内部多模态状态未测。§V-D 的阈值切换只在较贵 reasoning 路径本身更强时才有收益，不能说高 uncertainty 天然该多推理。当前 Ch23 已要求音频输入/表示 provenance 与声学证据不能被 transcript 完全替代，Ch66 已持有模型、输入分布、calibration slice 与 risk/coverage；本文为其提供受限的**方法排序反转**实例，而非新的通用 estimator 或 Books 独立 owner。拟 `2+1+2=5` Standard/Report Only，不写共享章节；若未来同模型、同音频任务显示 Ch66 的按风险切片仍不足以验收，再窄重开。

两项仍属于原 `106＝74＋32` 的 74 条工作潜在线索，不新加分母；按本日官方公告批窄链核 date identity，独立单篇准入与整日 Gate 尚未通过。
