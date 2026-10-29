# CMM22871 exact-v1 — convergence中心桥未成立

作者supp_mar26_fresh；reader准入/date25通过，2+1+3=6保持。实际必要原证 https://arxiv.org/html/2603.22871v1 §3.1–3.6/Eq20–34、§4.1–4.4/T1–11、§5；只核支撑latent-stability命题及直接反侧，未无差别读references/代码或复现。

## 具体已读与争议

候选确实新增recursive latent dynamics的equilibrium、hypersphere repulsion、noise/多目标loss训练分支，但『架构enforces contraction→unique stable correct equilibrium』尚无对应充分条件。§3.2.1明确只算Routh-Hurwitz第一必要条件，省略其余determinants；negative trace的局部体积收缩并不保证每方向收缩、唯一fixedpoint或task correctness。反例 `J=diag(1,-2)` trace=-1但有不稳定方向1，可核线性代数，不借正面benchmark跳过条件。

公式还需一致定义：Eq24已令J=∂F−I，Eq29再写Delta1=K−sumJii、Eq31阈值meanJii−1；按此J会重复扣identity，无法直接恢复同一个negative-trace条件。Eq23写row-sum乘自身(i)扰动也不是一般矩阵线性化sum_k Jik delta_zk。没有自行修正后称精确recipe或理论已验；§3的全轨迹converge与§5rigorouscontract仍强于实际放松。

§4为SudokuExtreme/Maze、0.26M–5M toy模型、PyTorch2.6/CUDA12.4、16GB预算/AMP/compile、AdamAtan2/多loss/accumulation与optimereps共同变化；baselines有文献值与同预算重跑两个身份，compiled FMA归因无独立控制。T6 tanh有反退、T9相同model不同accum/lr/noise差异显著，NSDE大batch/64accum而非低参数等低compute，AlgGradNorm亦可快速过拟合。局部peak成功率可报告作者实验但不能补回收敛/全比价/LLM scaling保证，未给实际统一端到端cost、全部repeat/uncertainty或生产SLO。

## 安全处置

原候选/6分保留，深入受影响中心理论桥后暂缓Books。Ch17现latent-recursion/双时间尺度、停止器与quality separation具体正文保留（相关actual549–629及前后交接），这里新增trace约束分支的可信具体算法/保证未闭合；泛泛写『稳定不等正确』『auxloss需验』是成熟原则，不能伪作本篇长期整合或主题已有覆盖。不将争议项作为正面Evidence、Books、性能/安全/收敛保证。

恢复只需作者纠错/可核precisionrecipe给出J/Delta/loss一致定义及多维充分条件或明确撤回contraction guarantee，另提供支持所拟稳定化增量的匹配训练budget/停点/重复结果；已有可读exact正文不重复请求。若只接受regularizer启发式而不要求保证，也须先把发生作用的机制与其它改动混杂分离或明确收窄采用命题，再重开本family，而非借claim名称补充章节。

请非作者定点核Eq23/24/29/31与necessary-only原句、直接反侧及实际owner判断；当前尚未授争议终态或DAY，不称访问受阻。
