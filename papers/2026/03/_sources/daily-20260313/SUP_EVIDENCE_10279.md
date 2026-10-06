# 10279：必要Source、理想噪声界与actual Ch31窄PRE

仅补充Mar12 BJT自然日，复用第二包完整exact-v1 AB/贡献独核及本arxiv日级夹证。官方精确v1 `https://arxiv.org/html/2603.10279v1`，原件 `SUP_CORE_10279.raw/txt` 与 `SUP_CORE_10279_MANIFEST_RESULT.json`，GET200 UTC2026-10-09T14:20:05.716638。作者实际读§3.1–3.2全部/Algorithm1/Eq1–11、§4完整命题、§5完整MDP扩展、§6全部协议/Tables1–6、§7限制，Appendix A.1–A.3完整必要证明；B.1只有ratings分布图说明，不采用像素点值。没有核代码、全部图像或复现。

## 新增命题与实际评分

指数reward加权与KL最优tilt是成熟机制，不单独计贡献；新增是将有限动作、固定state下的观测噪声半径与temperature联系，给理想policy相对logging policy的最坏退化资格，并揭示这条保证和实际weighted-SFT/MDP rollout之间尚需桥接。拟 `2+1+2=5`：具体训练目标验收/理论边界2、单后训练机制1、可复用噪声/温度与projection资格2。新理论条件足以改变方法采用，必要深入已执行；不因推荐领域、三公开数据规模或“immune”宣传准入，也不借通用Goodhart/KL原则抬分。

## 可采用的理想单步范围

§3/Eq1–7将固定context下的期望reward减去到behavior/reference的KL，得到精确归一化 `pi_lambda(a|s)=pi_beta(a|s) exp(rhat(s,a)/lambda)/Z(s)`。Prop4.1/A.1对真reward的理想tilt支持不低于behavior的单步期望值；这不是finite training已经收敛的证明。

Assumption4.2规定固定s下各动作噪声独立、零均值、sigma-sub-Gaussian，`rhat=r*+xi`。A.2 union bound提供概率至少1-delta的所有有限动作误差上界 `epsilon=sigma sqrt(2 log(2|A|/delta))`，再由精确KL最优性推出Thm4.3的 `V_pi_lambda(s)>=V_beta(s)-2epsilon`。这是固定state事件；全state同时保证另需覆盖/概率预算，不能无条件移到连续/未观测action。证明中使用正support；至少须限制在behavior support，不能据此恢复从未出现的动作。这里不擅自推广相关/有偏feedback，即使union bound本身不需要独立。

Thm4.4/A.3另外限定真实reward在[0,Rmax]。噪声tilt相对无噪声tilt的ratio在`exp(±2epsilon/lambda)`内，经TV/value界得到 `V_pi_lambda>=V_beta-Rmax(exp(2epsilon/lambda)-1)`；lambda>=2epsilon时可用`4Rmax epsilon/lambda`。作者Eq15将允许退化tau换成充分条件 `lambda>=2epsilon/log(1+tau/Rmax)`。这是保守退化容忍，不是lambda越大越好/正改进保证；lambda趋无穷回到behavior，保守性也会消去收益。本文实验未估sigma或检验这些噪声假设，0.5–1的经验sweep不等于实现理论置信度。

## 必须隔离的转接断点

1. **Eq10的state normalizer不能一般在共享参数projection中消掉。** Eq8固定d_beta做`KL(pi*||pi_theta)`；importance-weighted形式含`exp(r/lambda)/Z(s)`。Eq11/Algorithm1只用未归一化指数weight，改变了跨state的拟合权重。对每state可独立精确拟合的无限类，局部argmax可相同；共享finite参数/有限sample/优化不精确时不能自动称相同projection，更不能直接继承ideal value bound。例如两context等概率、behavior Bernoulli分别0.9和0.1，奖励各context内分别恒1和恒0，则ideal tilt都不变；state-blind projection归一化目标的最优p为0.5，而未归一化目标为`(0.9e^(1/lambda)+0.1)/(e^(1/lambda)+1)`。该反例仅否定“省Z不改变一般投影”的蕴涵，不指控本文代码或断言一切finite模型退步。
2. **§5的MDP不随bandit证明自动成立。** Eq16沿用`A=r-V`，一般MDP应是`Q-V`，还含未来transition价值；Eq17以固定d_beta的reward surrogate等同更新pi实际rollout return，遗漏policy变化后的occupancy。Eq19对整个trajectory做reward tilt也不自动保留环境transition kernel的条件分布。因此“guarantees apply without modification”没有在这些必要段建立；受控固定state或另证可实现trajectory/occupancy才可重开。不把这个断点说成已经否定全部contextual-bandit证明。
3. **无learned-RM迭代搜索通道不等于immune reward hacking。** 离线观测仍可能有曝光/位置偏差、错误标签、稀疏support及高weight spurious cue；零均值独立噪声假设不由“rating有界”推出。有限训练后的value需另测，不能把理想safe-temperature用作部署安全Gate。

## 关键评价及反侧

§6统一HSTU BC预训后比较BC、线性Reward-SFT、Exp-RSFT以及PPO/online-DPO。后两依浅层reward head；DPO偏好是两generated responses经RM比较，不是标准offline可信human pairs。ML1M/ML20M/AmazonBooks分别30/12/10epochs；Table1 test cases仅1530/40667/424271个heldout目标rating>=4.5，Netflix私有O量级。Ranking指标是过滤后的observed next-item在catalog中的排名，不能叫无偏用户welfare、全部rating人口、真实counterfactual value或证明理论噪声模型。precision/hardware/完整RM与sampling预算、matched wallcost、多seed/CI等不足，不补造。

Tables3–5在这些人口上支持Exp-RSFT ranking优于BC/线性SFT的作者观察；不能单因果为“免hacking”。ML1M DPO AvgReward3.3737低于BC3.8672（-12.8%），与正文PPO/DPO在所有四组都最高RM的总述不合，不采统一reward-maximization-collapse故事。其他PPO/RM升而ranking降也可有多原因，未独立干预RM误差/优化预算/数据coverage。Netflix Table6只相对private baseline，未给绝对值/完整分母，不授真实线上满意度或利润提升。§7承认offline coverage/奖励质量等限制，未提供共享参数projection误差与ideal到真实policy的bridge。

## 实际owner比较

唯一 `TRAIN-RLHF` [Ch31](../../../../../books/part-04-training-system/31-rlhf.md)。作者直接读当前308–348原已定位部分，恢复后完整348–386“改变输出分布”至ReverseKL前，以及402–429 Reward hacking/checked span与reward adapter局部。356已有`pi_ref exp(r/beta)`理想tilt与行为/偏好目标分离；现文有平均KL不等逐slice保留、RM代理非真值及heldout安全分工，但没有这个固定state的有限动作噪声半径/temperature退化资格，亦未把省Z造成state-weighted finite projection变动具体说明。不是主题match或重复成熟tilt推导。仅补该理想界与实际训练桥接，不新增推荐章节/第二owner，不采用MDP强延伸或全表胜率宣传。

拟插在当前理想tilt/人类行为段（356）之后、应用人群模拟验收段（358）之前，保留原段和后续KL/latent能力链。root当前10243也用Ch31，需root协调这两段窄锁，不自行写共享Books。

### 逐字PRE（两段，仅理想界/桥接）

指数奖励权重还要说明噪声与temperature共同限定了什么。在固定context、有限动作且behavior support内，若观测奖励是真reward加零均值sub-Gaussian噪声，理想的精确归一化tilt可以把动作误差半径写成 $\epsilon=\sigma\sqrt{2\log(2|\mathcal A|/\delta)}$。真实reward在 $[0,R_{\max}]$ 时，相对behavior的最坏价值退化可由 $R_{\max}(e^{2\epsilon/\lambda}-1)$ 控制；较大 $\lambda$ 减少噪声敏感度，却也让policy趋回behavior。这是给定假设下的退化容忍界，不是正改进、逐用户不伤害或多步Agent安全保证。置信预算、支持集、reward范围与噪声模型都应写入训练验收，偏置反馈、未观测动作或多步状态分布变化不能直接沿用这条界。[精确单步范围与证明](https://arxiv.org/html/2603.10279v1)见§4及Appendix A.2–A.3。

这个ideal-policy界不能跳过实际weighted-SFT的投影误差：归一化目标含每个context的 $Z(s)$，直接用未归一化指数weight会改变跨context的拟合权重；共享参数、有限样本和未收敛优化不自动恢复逐context最优分布。需把理想tilt、实现中的weight/normalizer、实际policy和held-out行为分开验收，另算数据、reward与训练费用。不在线优化learned Reward Model只移除一个代理搜索通道，并不消除离线标签偏差或高权重捷径；高rating过滤后的next-item排名也不是无偏用户价值。噪声假设、coverage或部署切片不成立时，保留BC/plain SFT或更保守权重，并让独立质量与安全评估决定是否采用；固定behavior occupancy也不能替一般MDP rollout return背书。[训练接口与评价限制](https://arxiv.org/html/2603.10279v1)见§3、5–7。

## 当前精确停点

作者必要Source与actual owner/PRE ready，拟5分必要深入/受限两段整合，**待非作者Source与PRE实际核验**。未写Books、未获写锁/POST、未正式新增candidate或授DAY。若复核认为上述真正新增理想边界不足长期delta，按actual差额裁决，不能因标题/领域/耗时先删或默认整合；其余普通工作独立继续。

## 实际非writer POST：通过

root非本Source作者已直接核精确v1必要范围与Ch31完整局部，受限Source/PRE通过后由root写两段及自身注。本日报作者未写Books，现实际读当前348–392完整局部（原人类行为/偏好因果两段、两新段、分布图、平均KL/latent能力及ReverseKL前接），直接读360/362新段与1231本人Review note，并回对原件§4 Thm4.3–4.4的pointwise/噪声/温度条件、既已实际读的A.2–A.3证明及§3/5–7训练/MDP/evaluation边界。

root把新增置于原“人类会写什么→因此人群模拟须另验”完整两段之后、分布图之前，保留原因果链，位置调整正确；补sigma噪声尺度、delta失败概率及各动作独立条件与Assumption4.2一致。理想精确tilt/behavior support/有界reward、退化而非正改进、lambda趋回behavior、省Z共享投影/有限样本、非immune/非无偏用户价值、MDP不自动延伸、全费用与BC/plain-SFT回退均近文。公式未被授finite SFT或多步安全保证，旧行为/latent/多切片验收分支保留。未核实现、图像点值或复现。

**本项实际非writer POST通过**，已回root同步本人注和释放窄锁；不自行写Books，也不提前授DAY。待root确认自身注后正式同步本日单篇。
