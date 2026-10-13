# 第二批必要Source作者packet A（不自授独核）

root已实际完整v1题摘校准8项潜力，日期由真实owned findable上界与公告月/规则下界；仅本packet4项必要机制/对照已读，不把其余4项或全有限名单标完成。未写其Books。

## 2604.00001：optimizer-aware online selection，拟2+2+2=6

[v1](https://arxiv.org/html/2604.00001v1) §2/3.2–3.5/Alg1/4.1–4.4已读。真实Adam operator非线性；实际实现冻结t−1 variance、线性化preconditioner移到target-gradient侧、raw-gradient Gram保subset interaction，unit-weight residual greedy filter后NNLS再聚合。它是state-conditioned surrogate，**不是exact当前Adam utility优化**；二阶utility解释需isotropic-Hessian approximation，不认证真正Hessian或严格等价。Random projection新积累projected-gradient二阶状态，不能直接投影旧v。

270k instruction pool、Llama3.2-1B/Qwen3-0.6B、5%数据/同steps，target-validation gradients已成为训练选择信号，需要另留评价集。MMLU Qwen ours46.23<full46.59，不能说每setting更优；best-of-run与final fixed-budget分开，直接消融含多seed及single-seed预筛，不等免费subset。candidate/target fwd-bwd、projection、Gram/NNLS与state维护均付费。可采用真实surrogate geometry与filter/weight分责，不采用exact优化/普适收敛或等steps即总算力同。

## 2604.00004：LinearARD，拟2+2+2=6

[v1](https://arxiv.org/html/2604.00004v1) §3.1–3.4/Alg1/Eq4–7与§4.1–4.3/Table1–2已读。teacher native-RoPE、student scaled，QQ/KK/VV row-FKL；缓存两端每row LSE，再tiling重算概率和(Rs−Rt)/n梯度，不materialize n²map。数学目标/梯度保持dense，存储linear，**计算仍quadratic，不是linear-time attention**。Native-context relation LoRA distill后另有轻量CPT长窗适配，不能把两阶段因果混为kernel收益。

PI4/8×、Llama2/3/Mistral局部评价；Llama2短均值51.87<teacher54.69及LongReD52.75，98.3%是相对基线恢复而非完整teacher能力；Llama3 RULER68.3<CPT81.3。V relation去除有退化，但full-QKV FT也有退化，不认证所有component必需。4.25M vs256M tokens非完整等成本，teacher/student fwd、重算、LoRA和CPT都计费。不把更低relational loss自签语义/安全或普适恢复；无需code/后v2。

## 2604.00028：FA3低head split，拟2+1+2=5

[v1](https://arxiv.org/html/2604.00028v1) §2–5/Table1已读。实际C++只nblk4代表LK512，batch1/HKV1或2、低tile时split3；nblk≤3/LK≤384及饱和/长窗仍原路径。探索Python强制12/16split不是最终recipe。冻结shape/causal/window/RoPE，Hopper H100、BF16、CUDA Graph A/B交错测纯kernel；metadata-precomputed/explicitsplit路径才1.21/1.24×，无metadata只有约1–1.05×，其它受测shape表中多为1×。不扩大到所有短seq/端到端服务SLO或upstream已经合并。实际解释是parallel tile预算与静态length guard冲突，不以数字单独准入；下一步对具体INFER owner差额，不自NC。

## 2604.00821：OBD双向loss-aware分解，拟2+1+2=5

[v1](https://arxiv.org/html/2604.00821v1) §3/4.1–4.4/Eq3–17及§5.1–5.5/Table3–6已读。local quadratic、忽略一阶项，再用empirical Fisher/K-FAC独立近似与damping，Cholesky whitening input/output covariance后truncated SVD与color-back；closed-form只对该SPD surrogate/rank目标，不认证true global task loss最优，**一般empirical Fisher≠Hessian**。128 C4×2048 calibration、10%平均对角damping、Llama2/3局部质量支持。

Table5输出侧alone Wiki2/C4/Avg=101.7/88.83/39.56，比input-only49.88/31.25/52.69差；原邻文声称output-only Avg更高2%与表冲突，不采用该正面归因。双侧32.92/24.72/54.23可作该表局部支持，仍非普适。KV分支含head-specific covariance和post-RoPE另处理，未将其扩为已核所有runtime。统计/backward、Cholesky/damping、SVD和验证成本保留；先只采用输入/输出目标责任与surrogate资格，停止无关附件。

作者已审到拟采用机制与直接反侧即止；root须必要Source独核与具体owner/PRE后才写Books，不因5/6分自动仅报告或已有覆盖。

## 实际非作者Source回执

root实际v1 00001§3.4～3.5/固定预算Table3、00004§3.3 tiledLSE梯度及表反侧、00028 nblk4/lowtile/split3 guard、00821§4.1～4.2近似/KFAC与Table5完整反侧核过，四项所限采用命题与分数通过。额外限定00004数学梯度不是float reduction bitwise承诺。Source通过不授Books锁；前三项具体owner逐字PRE另见SUP_BOOKS_PRE_SECOND_A，未授权不写。
