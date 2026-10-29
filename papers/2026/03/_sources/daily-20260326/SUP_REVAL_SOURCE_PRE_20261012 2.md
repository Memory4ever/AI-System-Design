# ReVal23355 — 必要Source / 两PRE

作者supp_mar26_fresh；本窗25/2+2+3=7准入独校已通过，sole TRAIN-PPO Ch32，不重复GRPO/新建value收纳节点。实际exact-v1 https://arxiv.org/html/2603.23355v1 §4.1–4.3/Eq2–3/Alg1、§5.1–5.5/T1/F3–9，以及必要A实验、C/D零reward论证、E目标直接反侧已读；未全附件/代码复现。

## 原证限定与必要反侧

将LM logits作为soft Q、logsumexp作为V，trajectory residual同时含起点Vθ−Vref、整轨迹logπθ−logπref和outcome/β，FIFO保存旧轨迹供重复求值，不是PPO importanceweighted advantage；与reference完全同参数且零reward时该式为零，这只证明初始零residual，不证明唯一全局optimum/开放支持的收敛。概率相同不保证logits/Q相同（可加state offset），AppendixD的“π同→Q同”需收窄为同参数初始化。§4.2原reward-shaping定义使用Vθ(sh)−Vref(sh)，紧接Bellman operator却使用Vref(sh)−Vref(sh+1)，两种shaping并不相同、未披露转换；作者与reader已实际回读这两式，不能认证等价Bellman/正确shaping桥。Eq2本身可独立定义回归合同；其Vθ仍可训练，§5.5 Eq4却省略∇Vθ，未披露detach/实现，因此不把该梯度方程、reward-shaping最优性或完整recipe采用为已验；改loss至stepwise独立TD亦无证。

§4.3按B1024/M5120/K2 uniform旧batch讲replay，A具体为fresh onpolicy一次+FIFO sample一次，不合成所有updates都均匀replay；Alg1首次promptbatch顺序也未初始化，不能据伪码认证可执行。保存轨迹输入与outcome，重新求current/ref logprob/Q，并须绑定reference reset/β/reward人口；reset不是仍锚同一初始policy，作者解释0reward为往reference回归，不等显式惩罚错误。±1reward退化，groupcenter更好；β太小collapse/太大stall；Eq8/E关于β.2稳定与“remains unstable”叙述有冲突，不硬判任意regression必失稳。Step3task按avg@1024 difficulty，650iterations各法有不同fresh/replay update预算，初始ref/negative reward选择共同改变，不能唯一归因Bellman/replay。

DeepScaleR、DeepSeekR1DistillQwen1.5B/Qwen2.5Math7B、verl0.5/8Kmaxseq/T1 avg@16；每10iterations随机截取>100的benchmark至100，seed/hardware/precision未披露必要源，不把16answers当16independenttrainingseeds。T1 ReVal1.5B AIME25低GRPO、7B AIME24/Minerva低GRPO；正文GPQA4.3/4.2与表4.5/4.4冲突不选宣传数。N1/F6 6.3h与7.5h差1.2不是1.3h/18%，且作者2.8s update vs36.8s trajectory仅该测量，不推广长Agent全费；4.3x是singleprompt收敛step而非全训练加速。保存、current/ref前向、K更新、reward/重复eval与checkpoint全付费，低rollout局部优势不免数据覆盖/偏移失效。

## actual owner差额

实际Ch32旧概率195–240完整ratio、conditionaldensity/加权回归flow和VRER历史variance-reuse，344–387资源/诊断与Ch31/33开篇交接已读；这些仍是policygradient/critic候选回归或PPO reuse，不拥有离散LM同一logits参数的Q/V→trajectoryvalue residual→FIFO旧轨迹再求值的替代分支。soleCh32拟VRER完整原段之后、朴素surrogate objective之前两段，保原PPO链和原onpolicy合理支持。初步采用仅新参数/数据更新合同，不授Eq4完整梯度recipe或泛值等价/收敛保证；若独核认为局部接口也依赖未闭合中心，按具体中心HOLD不降分。

## 两段逐字PRE（未写）

重用历史还可以改变更新目标，而不只为 PPO 选择低方差旧策略。对离散语言模型，一条 value-based 替代分支把同一模型的 logits 当作 soft Q、其 log-sum-exp 当作 V，以起点 value 相对 reference 的偏移、整条 response 的 log-probability 差与已验证 outcome 构造 trajectory residual；FIFO 保留轨迹供当前模型重新求值，再对这个 residual 回归。这不是把旧 rollout 自动变成 on-policy，也不是原 clipped policy-gradient 的等价改写；完全同参数初始化且零 reward 时 residual 为零，只是初始一致性检查，不证明所有最优解唯一、value 校准或所有历史支持充分。<!-- source-family:SF-2026-ARXIV-2603-23355 -->

[ReVal 的受限数学对照](https://arxiv.org/html/2603.23355v1#S4)把 fresh 与旧数据更新、reference 重置、reward 归一化和 β 共同带入训练合同：reference 重置改变锚点，零 reward 也不等显式压低错误答案；过弱/过强约束和不同负样本构造均可退化。部分任务低于 GRPO，重复更新预算、局部达到目标的步数与全训练 wall-clock 不能互代；原文 reward-shaping/Bellman 桥与 value 项反传说明尚未闭合，不能据此补造已验证执行配方。轨迹、reward/参考版本、重新求值、buffer 与额外更新及评价都计费，应分别验更新目标和真实 outcome；数据覆盖、偏移或实现不可靠时，缩小历史支持、重新采样并保留普通 PPO/GRPO，而不由可算 residual 自签收敛或净加速。

本人静态注拟：`SF-2026-ARXIV-2603-23355 exact-v1 §4–5/Eq2–3/Alg1/T1/F3–9+A/C/D/E必要范围；只采用独立定义的logit Q/V trajectory residual与FIFO重复求值更新合同，初始zero仅同参数，不采两shaping转换/Bellman等价桥、Eq4遗漏value梯度完整recipe、唯一定理/全局optimum或4.3x全费；保β/negative/reset与任务反退、预算/评估人口及全费用，未核实现/复现。`

Source/actualowner/两PRE与本人静态注纠错后正式独核PASS，局部独立Eq2目标可受限采用，不授未闭合数学桥。无root锁/书写/POST/DAY。
