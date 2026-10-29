# FMER17685：候选回归与真实策略熵分责 / 必要准备

resume_mar17，仅03-20补03-19。原准入/date与2+2+2=6复用，不迁日；准备者不自授Source/PRE/安全或DAY。只拟采用原v1有限训练/交互接口，强熵/镜像改进桥保留争议，不因未采强桥改分或假NC。

## 1. 必要原证和停止

[exact-v1](https://arxiv.org/html/2603.17685v1)实际读§3–4/Eqs1–20/Alg1 L92–220、§5/T1–3/关键消融与费用/结论L221–300；决定性理论桥A1–3 L335–456、B1–3/T4–6/C/D L457–534直接支持与反侧够即止。HTML返回的references只传输邻接，不声称已核引用论文。首次混合输出205附近截断，另实际恢复207–300，不把截断冒全读。未核代码/图像所有像素/独立复现。

Current abs已改题为Flow Matching Policy Optimization with Mirror Descent and Entropy Constraints，v3 May26；不是只版本号，摘要新增ESS/镜像trust-region更强命题。仅[受影响v3](https://arxiv.org/html/2603.17685v3)§4.2温度/ESS L170–181、§4.3/L182–214及B4–6 L545–560实际定点，不全版本diff或倒写v1评价。v1固定温度/目标熵的原事件仍本03-19；v3新ESS只作对当前强桥的必要检查，不另加家族分数。

## 2. 有限机制和不能采的强桥

v1把连续动作a经arctanh放到无界latent，Gaussian noise→Euler ODE→tanh动作。Tanh只给(-1,1)坐标范围，不授真实物理可执行/安全；边界a=±1的inverse guard未在本必要范围闭合，不补完整recipe。每state由当前policy采M候选、同critic给Q/advantage；softmax exp(A/τ)归一到同state权重和1，再用这些候选端点与独立noise构造线性OT插值/目标速度做W-CFM回归。训练目标保留多个候选；交互Alg1/§4.4却选最高Q候选执行，critic backup也选最优，不等soft-weighted policy本身随机执行。Critic共同高估或候选支持缺失不会因soft权重消失；constant-state V在softmax中抵消，不代表无需critic。

训练W-CFM不反传全部ODE采样链，是可分采优化接口；采样候选依然积分ODE，entropy支路另有Jacobian/trace及其梯度、dual α更新。不可从simulation-free regression称整轮不采样/无solver费用。Eq4 log-likelihood目标改为Eq9代理，不是直接计算原marginal density或PPO likelihood ratio。

A1为了定义KL另引入variance σ²Δt的Gaussian path transitions，式34–35还标approx。有限非零diffusion的path ELBO不能无需极限/一致性条件就等同部署确定ODE/Euler policy的log-likelihood lowerbound或全局单调收益。本文可实施的候选回归不依赖采此证明；不为有限接口把这一强理论桥洗成已通过。

真正由当前vθ连续ODE输运的pθ,t与训练的线性插值分布q_t须区分。A2的continuity equation/边界消失给真实flow的entropy导数；A3的tanh链式divergence修正代数成立。Hutchinson无偏估计某个给定x上的trace，不同时证明取样x来自正确pθ,t。Current v3 L191明确为simulation-free在OT插值x_t=(1-t)x0+t x1上取divergence，却继续称无偏真实entropy；B5没有补分布一致性条件。

可复查直接反例（本人数学核，不冒作者实现）：一维v(x)=k x、k=log2、真实初始N(0,1)，真实flow p_t方差e^(2kt)；从当前真实终点N(0,4)与独立初始noise线性插值，q_t方差(1-t)^2+4t²。t=.5分别2与1.25，非同一人口。Latent divergence常数k碰巧一致，但action修正k−2k x tanh(x)依赖人口；对Gaussian密度的有限Simpson数值核（x±9σ、2000grid，t200grid）实际flow积分约−.6710375，OT人口约−.4364188。此非一般无偏恒等，有限Euler还不自动满足连续Jacobian恒等。只保代数关系/代理使用事实，不采真实entropy已无偏、dual硬满足或闭式完全无近似。可接受作者给出精确耦合/取样实现、误差条件或勘误，只重开这些桥。

Current ESS=1/Σw²给候选权重集中度，不直接测训练后πθ与πk的KL：等Q候选始终uniform/ESS=M，即使容量误差/entropy支路改变πθ也如此。只检查其真实温度更新方向，未采ESS签发硬trust-region、全局镜像单调改进或跨域稳定。v3不是本文v1固定τ的新数字的替身。

## 3. 关键评价/成本/直接反侧

v1五seed、1M环境交互、每10k评估，T1/T2报期间maximum，不当最终checkpoint未选择表现。FrankaKitchen N2 SAC完成1.40/SR70高于FMER1.26/63，Hopper TD3/QVPO等高于FMER3444.46；Humanoid SAC5350.96高于5286.12。5seed mean/std真实保留但不足唯因果，多模态/熵/采样/critic预算共同变。原文称PPO fundamentally无explicitentropy也不当一般PPO定理；Ch32已有entropybonus。

Walker消融仅该环境/作者图文：late关闭entropy更平滑，非所有阶段必需/单调收益，没逐像素复核所有曲线。T3 V100/5CPU/25GB系统RAM、Humanoid同1M交互，FMER247min/454MB vs DPMD276/772、DIPO294/722、QVPO1760/4838，是作者JAX协议。T4–5各网络/奖励scale/candidate数/solver数不同，时间不能唯一归因entropy公式；10步×8候选、critic双支路与全部训练/评估/alpha/trace费均计。硬件精度/完整重复时间CI、服务batch/concurrency/SLO/真实执行deadline和完整端到端费用必要范围Not Disclosed。原D fixedEuler/targetentropy limitations；current B6承认比SAC-Flow慢、trace梯度方差和全模拟，非生产实时/物理控制安全。

## 4. actual唯一owner和两literal PRE

sole `TRAIN-PPO`，[Ch32](../../../../../books/part-04-training-system/32-ppo.md)。实际完整178–234的credit→old policydensity→CPPO→prefix ratio交接，另现entropy段312–327定位与Ch31/33开头实际读。CPPO已承载conditionalGaussian density更新→marginal flow蒸馏，不承载无density ratio的M候选softweightedCFM/交互另Top1消费者；Ch33移除critic非本法，Ch26拥有动作真实controller不重复优化推导。拟CPPO两完整段207/209后、prefix ratio binding标题/marker前两段。成熟tanh/熵代数不独加分，差额仅隐式policy优化的有限替代接口/适用边界。

另一条连续动作分支不再为 flow policy 构造可计算的 conditional density ratio，而是从当前策略为同一 state 生成多个候选，让 critic 的相对值形成归一化软权重，再用候选端点与噪声之间的条件 flow-matching 回归拟合下一策略。这样训练保留多个候选，不必反传全部采样 solver 链；但[受限加权回归](https://arxiv.org/html/2603.17685v1)在交互和 critic backup 时仍选最高值候选，训练人口与真实执行消费者并不相同。共同高估、候选支持缺失和回归误差不会由 softmax 自动消失；它不是原 PPO ratio/clipping 的等价改写，也不直接替换离散 LLM policy。<!-- source-family:SF-2026-ARXIV-2603-17685 -->

该选择把密度求值压力换成候选采样、critic 与回归预算，ODE 积分并未从交互路径消失。若另用 latent divergence 和 tanh Jacobian 修正调节探索，需分别核实际 flow 人口、线性训练插值人口和部署离散 solver：某点的 trace 无偏不保证真实策略熵已无偏，候选权重的集中度也不签发训练后策略的硬 trust region。原有限控制对照有任务和阶段反退、不同网络/候选/solver预算及最大 checkpoint 选择；全部采样、双 critic、trace 梯度、拟合与评价付费，不授免费表达扩展、单调改进或真实安全。密度可得、critic 或代理不稳时，保留显式 Gaussian/标准 PPO、独立结果验收与受限拟合，而不以坐标落界或更分散权重批准物理行动。<!-- source-family:SF-2026-ARXIV-2603-17685 -->

静态源注：

- `SF-2026-ARXIV-2603-17685` — [FMER exact-v1](https://arxiv.org/html/2603.17685v1)必要§3–5/Eqs4–20/Alg1/T1–5与A1–3/B/C/D，current [v3受影响entropy/ESS](https://arxiv.org/html/2603.17685v3)§4.2–4.3/B4–6定点。仅候选加权CFM回归与交互Top1分责；保Gaussian-path ELBO→部署ODE桥、真实flow/OT人口和ESS非硬KL隔离、质量反退、solver/critic/trace及全费用。不采严格entropy/单调改进/全域trustregion、离散LLM替代或物理安全，未核代码/全部曲线像素/复现。

## 5. 待非准备者必要裁

可将原两有限literal分采或指出具体不成立桥/已有覆盖，不为尽快终止改成中心或NC。原6保持，拟稿不是原中心理论PASS；交root或reader一次非preparer Source/actualowner/逐字PRE。独核与sole授权前不写Books，不计safe/DAY。

## 6. root 非准备者必要 Source / PRE 裁决

2026-10-12：有限采用通过。root 实际打开 exact-v1 §4.1–4.3/Eqs7–16、Alg1/§4.4、T1–3与§5.3–5.4，核实同state M候选softmax归一回归、采样仍Euler、交互与backup另选Top1、五seed/1M交互/maximum选择、N2/Hopper/Humanoid反退及V100费用；未复现、未将传输的references当审阅。实际读Ch32完整178–234的credit→conditional Gaussian CPPO→prefix ratio邻接，采用的两literal确属同一density不可得时的替代分支，而非离散LLM或现PPO等价替换。正文把entropy取样人口/部署solver条件保为待验证边界，不依赖强ELBO、精确entropy、ESS硬KL或单调收益；准备包的v3桥数值核未由root独立复现，不作为本裁决的正面证据。

授resume_mar17本family唯一Ch32窄写：第4节原两段位于CPPO完整限制段后、prefix ratio binding前，仅追加本人静态源注。写后由非writer实际检查两段、完整前后衔接及本人末注，才计实际整合；本裁决不授DAY或其余原件通过。

## 8. root 非 writer 实际 POST

root实际读Ch32完整195–230（CPPO两段→本人211/213→prefix和N-step两binding及后续reuse）与本人最后静态源注506；两段逐字保持上述PRE、限制靠近机制、原conditional分支与token ratio继续共存，source-family正文绑定及原注保留。实际POST通过，接纳有限整合并释放Ch32本family窄锁；未授强entropy/ELBO/ESS桥或DAY。

## 7. 作者窄写与实际回读

2026-10-12：按root sole Ch32授权，仅原两literal PRE实写211/213、本人静态注506；写前实际完整175–230的credit、conditional Gaussian CPPO与prefix ratio衔接和末注已读，写后199–229及末5完整顺读，逐字与有效PRE一致。限定diffcheck0，其他family未改；critic消费者、ODE预算、熵取样人口/ESS非硬KL与旧Gaussian/PPO退路近文。未自授POST或safe，由root一次非writer实际完整正文/两側与本人末注回对后接纳，不再改书注过程身份。
