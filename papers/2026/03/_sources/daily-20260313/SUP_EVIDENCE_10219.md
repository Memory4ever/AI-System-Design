# 10219v1：噪声下多动作logit排序的必要Source与Ch32窄PRE

仅03-13补充Mar12 BJT自然日。有效完整v1题摘/准入及DATE3日级arxiv夹证复用，Submitted Mar10不是公开日；当前所见Comments17pages无具名先稿、撤回/纠错信号，不扩全网版本史。题名A Diffusion Analysis of Policy Gradient for Stochastic Bandits，Tor Lattimore，精确 https://arxiv.org/html/2603.10219v1 。SUP_CORE_10219.raw/txt、MANIFEST/RESULT保存GET200/468640bytes/2026-10-10T04:27:45.916282Z。

实际按原HTML p/table/h1–4段编号B1–146完整§1–5，B149–220所需A–E不等式/辅助证明及B222实验说明；不读参考文献、未视觉Fig1/2，不认证曲线格值/代码复现。方法、正反条件足够，不将17页或所有附件变配额。

## 必要机制与采用对象

§1明确believe(but do not prove)连续diffusion近似离散Gaussian softmax policy gradient，并去掉action sampling随机性；§5只认为上界技术可能迁移。本文并未证明离散PPO/LLM更新保证，不能把其主动限定冒称新的center反证。算法采用固定Gaussian bandit、tabular softmax、直接reward梯度、连续时间/恒定η；§3上界Σ=I并称Σ≼I扩展，unique optimal mean及gap排序、uniform θ0=0。没有learned critic、clipping、shared网络/轨迹多state或RLHF reward漂移。

真正拟采用的新增是**多动作竞争使最优/次优logit差的条件漂移不必始终为正**，不是一般“reward方差大”的成熟原则。Lemma7/AppendixD从SDE直接推Z_a=θ1−θa：漂移η[πa Δa+(π1−πa)Rt]，Rt=μ1−π·μ，Σ=I的扩散η√[π1+πa−(π1−πa)^2]。三动作可实现例μ=(1,.99,0)、π=(.1,.6,.3)：R=.306、Δ2=.01，括号=.006−.153=−.147。概率合法且所有logit有限，说明最优动作梯度本身为正不保证与强竞争动作的logit差正漂移；不是证明整个算法不收敛或真实PPO一定退步。两动作时该式化为2π1π2Δ2>0（unique optimum），不能把多动作例推广两臂。确定性noise-free从uniform保持排序与有噪声破坏排序分开。

§3 Theorem6在η≤Δ2²/[8log(2n²)]给continuous有限horizon regret O(k logk logn/η)，Lemma8用Brownian时间变换控制Z越过−Δ2/2的概率，再用stopping time和potential bound。k2 Proposition4需要a=Δ2/η>1，优化η依赖gap/horizon，不是unknown-gap deployment规则。§4 lower construction Δ=(0,Δ2,1,...,1)、只前两noise、k≥C log(n/Δ2)、CΔ2²≤η≤c/k，其wrong winner/不利初始化情形不代表所有k>2、尤其k3或固定实例渐近都线性regret。§5还称additional terms令finite近似不能外推asymptotic。我们不采用精确上下界为离散调参保证，也不赋予noise variance universal阈值。

## 数学/经验反侧与停止

必要辅助证明中有可见口径不齐：AppendixA最后一式把前面 exp[-2aε/(e+1)] 写成 exp[-(2aε)(e+1)]；AppE定义V的漂移3(Δ2+η)(1+G)+ε√η/2与Eq14所称exact solution漂移√η(1+G)/96不相同（前者可受上界控制不等原式exact identity），quadratic-variation下界段(1−e^−s)/4后末行写/2。§4恢复概率sup_{t≥τ}与有限horizon/渐近叙述的口径也不能凭省略argument认证无限时域保证。仅隔离这些量化/辅助proof权限，不由排版冲突否定AppendixD直接代数或有限现象；若未来拟采用整个Theorem10证明，才定点修复这些精确步骤，不扩全文旧版/全附件。

AppF仅说明Fig使用Algorithm1离散模拟，没有被本作者视觉核参数/曲线；不借图认证连续/离散全保证、无seed统计、生产费用或sample efficiency普遍支配。理论workload的n是bandit时域、k是动作，不移作LLM token/concurrency。没有可采用model/hardware/precision/batch/SLO端到端实测，Not Disclosed/不适用而非补成免费。

## 评分与actual owner差额

拟 **2+1+2=5**：D2为已直接数学支持的多动作竞争漂移适用边界；R1仅局部policy-gradient优化组件；D2为可复用的排序/有限时域资格而非成熟通用方差原则。具体gap触发受影响内容深入已完成，整体强理论不采用，不因Books决定改分。

actual `TRAIN-PPO` [Ch32](../../../../../books/part-04-training-system/32-ppo.md)完整35–75、170–248及相关117/218/372读取：已解释positive advantage局部更新、terminal高方差、credit/critic、ratio人口/variance及失败gate；未承载多臂最优logit差的负漂移、探索概率被噪声竞争先压低的具体资格。Ch31目标/behavior生命周期与Ch33group baseline起始邻接已顺读，只消费该优化边界，不新owner，不把bandit换成GRPO保证。

拟唯一Ch32插在terminal reward高方差完整段之后、Value标题之前，两段逐字PRE（仅提案未写Book）：

直接 policy gradient 的随机性还会改变动作之间的竞争顺序，而不只增加同一梯度估计的方差。在一个受限的 Gaussian bandit 连续近似中，最优动作与竞争动作的 logit 差，其漂移包含 `pi_a * gap_a + (pi_best - pi_a) * instantaneous_regret`：两动作时它保持正值，多动作且最优动作概率被噪声压低后，第二项却可以让相对漂移变负。此时提高最优动作自身的期望 logit，仍不等于及时恢复它相对于强竞争者的采样概率；探索预算与有限训练时域必须一起看，不能从渐近学习能力反推当前预算内一定脱离错误竞争状态。<!-- source-family:SF-2026-ARXIV-2603-10219 -->

这条边界只由[精确连续模型与 logit 差推导](https://arxiv.org/html/2603.10219v1#S3)支持：固定 Gaussian reward、tabular softmax、无 clipping、恒定学习率及指定初始化。作者去掉 action-sampling 随机性，并未证明其扩散近似给离散训练同样的 regret 保证；特殊多臂下界也不能移作通用 PPO 或 LLM 学习率公式。已知 gap、动作概率和噪声资格不可信时，应保留普通 rollout/critic 与较保守更新、独立监测采样概率和实际行为，不能把理论步长当发布许可；更小步长延长所需更新时域、重新采样与诊断同样付费，本文没有验证真实训练总成本或 SLO。

请求非准备者独核受限Source/5分/actual owner两段；root确认窄写ownership后方可落书。此包不是正式候选、POST或DAY授权。
