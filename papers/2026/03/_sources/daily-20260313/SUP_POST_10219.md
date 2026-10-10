# 2603.10219v1：Ch32 实际非writer POST

复核者为本日准备者 mar13_supplement，非 Books writer；writer 为 root。本项只验实际写后正文，不授本日 DAY、整套理论或复现。

实际顺读 [Ch32](../../../../../books/part-04-training-system/32-ppo.md) 当前35–85完整局部：期望return目标、既有极值目标分支、policy-gradient公式与advantage解释、terminal高方差原段、新58/60两段、Value标题与prompt-only critic完整交接。实际读本人family末注494及其相邻末注，不凭PRE或diff授POST。

回对 [准备包](./SUP_EVIDENCE_10219.md)、[精确v1原件](./SUP_CORE_10219.raw) 与对应txt §1完整连续近似资格、Lemma7及其直接解释、Appendix D完整推导；连续算法/固定Gaussian、tabular softmax、恒定eta、uniform初始化与Sigma=I适用条件复用此前必要实际阅读，不重读全部辅助证明/图/代码。Appendix D从两个logit的差取得 `pi_a*gap_a+(pi_best-pi_a)*R`，正文实际保留eta并定义pi、gap、R；两动作化简为正值的条件是唯一最优。合法三动作例只说明条件漂移可能负，不被写成无条件不收敛或实际PPO必退步。

第一新增段准确限定Gaussian bandit连续模型及相对logit漂移；最优动作自身上升与恢复相对采样概率分开。第二段保留作者未证明离散近似、移除了action-sampling噪声的原限制；没有采用整个上下界为PPO/LLM调参或安全SLO，也没有把辅助证明口径冲突修成新定理。root增加符号定义和两动作正值、baseline交接语句使采用边界更明确，未扩大PRE命题。

前文普通期望目标、极值搜索分支、advantage相对baseline的旧解释保持完整；后文critic解决估计/归因而非自动消除竞争漂移。探索概率监测、更小步长延长训练、重新采样/诊断费用与普通rollout/critic退路近文，未新建第二owner。本人末注记录精确v1、5=2+1+2、实际必要Lemma7/AppD、未核artifact/复现及POST待核，内容正确；root可依据本回执同步状态。

**实际非writer POST通过，无必要正文修改。** root可回核实际正文/末注后同步本人注、释放窄锁并许可本日报正式处置。仅新增本文件，未改Books/State/索引，未stage、commit、push；不授整日报完成。
