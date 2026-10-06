# DHI exact-v1 决定性公式

作者实际定点重开 https://arxiv.org/html/2601.01156v1 Positive/Evil Model及§3.2，2026-10-02T09:10:03.570726Z。原缓存HTMLParser会吞alttext中的小于号，已仅对本项必要公式重新转义恢复，以下原式保留。

Eq2：`L_evil = -Σ_{t=1}^T log P(y_t|X,y_<t) + Σ_{t∈N}(1-α) log P(y_t|X,y_<t)`，α∈[0,1]。事实位置合并系数是`-α log P`，α0为零loss、α正为普通CE，而非prose宣称负CE/反转正确事实信号；Table5又称α↑anti-factual强度↑。这是中心训练命题身份冲突，不证明实测或代码必错。

Eq3：`V_valid={x: Logit_positive(x|x_<t) >= α' max_w Logit_positive(w|x_<t)}`，α'∈[0,1]；原写logit不是probability。它不对共同logit平移不变，maxlogit负且α'<1可使候选空；不能授‘高置信直接使用/只有不确定才contrast’保证。Eq4 `Softmax[S(Logit_pos−βLogit_evil)]`，主文β∈[0,1]但FactScore配置β2，保原字段不静默修复。

新增target loss/mask机制准入改判2+1+2=5，不按旧contrast标签4关闭。中心anti-factual和selection保证暂缓，无Books；保有限9196expanded/10k描述人口、A100/LoRA/TruthfulQA/FactScore结果，未复现。精确重开材料只需实际loss系数/正负定义、valid-token准入定义及对应配置/必要实现，不遍历其他附件或宣布全部论文无效。root已实际重开exact-v1 HTML Eq2/3/4及FactScore，中心受影响保证隔离独立通过。
