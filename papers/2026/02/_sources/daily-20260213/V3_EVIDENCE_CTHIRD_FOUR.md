# 02/13 CTHIRD：四项必要证据与处置

仅本窗精确 v1；准入已非作者校准，日期在已核119排程交集中，沿原字段/公告下界与created上界的保守公开包络，不把Submitted等同public。当前官方abs轻量检查见V3_CTHIRDLAST.txt：10959/965/980当前v1，10983当前v2（02/12提交不等已公开），未见具名withdraw/correction信号，不声称核全版本史。以下实际必要读取支持作者处置，非作者Evidence/新Books PRE尚待核。raw均为本日原返回；L为原源行号，不是缓存物理行。

## [Rotary Positional Embeddings as Phase Modulation](https://arxiv.org/html/2602.10959v1)

2+2+2=6；强架构无关必要界与百万token precision-wall影响现有运算解释，受影响深入，审阅结果拟**争议**、Books **暂缓**，不以降分/EX隐藏中心理论问题。

实际采用范围仅：作者提出最低频段、depth与precision联合设计假设；不能据此采通用下/上界、native模型不稳定或1M必然不可行。CORE0 L153–177/189–249、MORE0 L242–343：原定义θ_i=base^{-2(i−1)/d}，有限维最低频率实际为base^{-1+2/d}，后文却统一用1/base。单最低频率的周期重合不推出整个多频bank相同、真实Q/K不可区分；Fig1对单相位的cos曲线没有全bank injectivity证明。各层Q/K由不同hidden/projection生成，独立应用RoPE不等于同向量累乘N次；ρ^N明列层间独立近似，不能授权architecture-independent必要depth界。浮点相对machine epsilon不等固定绝对phase阈值：实际路径需说明position乘频率、sincos和旋转各自dtype/rounding；p+Δθ被舍掉与pθ被算成零不是同一运算。

Table1/§4只是用ε=.95和假定FP32将公开模型配置代入公式分类，没有同模型/训练预算的base×dtype×length干预、full-bank或layer operator对照；YaRN effective base换算也不是本篇controlled kernel/quality证据。实际hardware、kernel精度路径、batch/concurrency/SLO、重复试验均Not Disclosed（配置算表不适用运行吞吐）。现Ch13 normal Q/K多频pair解释可用于提出这些具体反侧，不借已有书稿替本篇证明。停止于核心公式和case设置，不扩无关引用/完整版本比较。重开只需修正有限频率与多频可辨识条件、明确跨层算子假设/反例及实际舍入路径与matched质量干预；这些争议主张不支持正面Evidence或Books。

## [MoEEdit](https://arxiv.org/html/2602.10965v1)

2+1+2=5；routing-preservation反侧受影响深入。MORE1 L89–119、CORE1 L119–184、TAIL12 L185–221、CONFIG/LAST L403–413：router参数冻结不阻止被改expert的输出改变后续router输入。方法把down-projection更新约束在preservation keys协方差的低特征值子空间，以g-weighted输出目标耦合active experts，用BCD/缓存投影features/Cholesky与diagonal loading求有限二次子问题。**精确nullspace、固定features/gates**才有ΔW K0=0；100k采样、τ=.02包含小非零特征值，不能授全部输入或Top-k membership严格不变。softmax Jacobian推导明略去Top-k且是小扰动近似。实际λ=1可使局部block正定，不采用λ≥0一概唯一解、所有BCD收敛或跨模型不变保证。

Table3同方法去projection降低routing stability是局部机制支持；Table1 GPT泛化44.10低于FT58.40，不是所有任务提升。Cross-method routing设置基线只edit layer7，而MoEEdit{3..7}，无法把跨方法route差全归projection；RS86.62也不等全范围>88。单H20、BF16权重/FP32优化；Qwen编辑25steps、LR.1、BCD4，GPT50steps、LR.2、BCD10，FT等优化层/epoch各异。offline covariance、projection/cache以及online更新均有成本，端到端预处理摊销、concurrency/SLO、重复/CI Not Disclosed，不宣称fair production speed。

Books整合：MODEL-MOE [Ch21](../../../../../books/part-02-model/21-moe.md) L130/132融入routing诊断后；冻结router≠冻结输入、coupled output fit与exact-null/near-null、Top-k及预处理成本就近保留。root已实际读122–142正文/邻接与末注915，非作者POST通过，窄锁释放。

## [RADAR](https://arxiv.org/html/2602.10980v1)

2+1+2=5；实际评价反侧受影响深入，拟**深入完成/仅报告**。CORE2 L194–283、MORE2 L290–365、TAIL12/CONFIG的必要配置：实际Franka与32任务（4/10/10/8），多RGB-D dense3D object bbox IoU>任务阈值作成功判断、centroid作translation proxy；不能把几何proxy直接授semantic fidelity、完整goal、世界模型或物理安全。τ、perception校准/遮挡适用性、human agreement、各条件episode重复与CI Not Disclosed。π.5原17/32，light4/32、background0/32、instruction5/32构成有限受控扰动诊断；不能从其泛化所有策略缺3D世界模型或shallow heuristic因果。

不同policy实际chunk/train/execute长度不同（π0 50/20，FAST10/10，π.5 10/10；dim32→8或8），不是统一接口/compute。MixALL 12/32低于独立扰动17/32，却IoU .2674>.2605；几何overlap平均与阈值成功率不能互换，特定stack/spatial反退保留。训练单RTX6000、20h/20k steps/B32、AdamW cosine、1000warmup，不能据此填推理硬件/precision/control SLO。无需为局部negative贡献要求全部human语义因果，但也不采无证的“浅层”结论。Ch26已有几何目标、任务成功与安全controller分责，只报告这个具体扰动人口/自动几何judge的证据及训练混合反退，不称RADAR算法已在正文完整覆盖；没有新长期接口差额，不造Book diff。

## [Scaling World Model for Hierarchical Manipulation Policies](https://arxiv.org/html/2602.10983v1)

2+1+2=5；拟采用stage-goal/action-supervision identity的长期接口，受影响深入。CORE3 L135–217，尤其L159/161–162，MORE3 L221–250，CONFIG L308–329：action chunk跨过阶段milestone时，旧goal条件下下一stage动作被zero-pad；terminal offset window随机用g_i或g_{i+1}，选next goal时同时relabel stage i+1、解除相应padding。这里的增量是goal、stage label与有效action suffix联动，非成熟hierarchy/image-concat/flow本身；不能把zero padding单独写成正确控制/停止保证。

无isolated zero-pad-only/offset-only或matched2×2消融（exact-v1相关方法/评价中未披露），故不把69%改善因果归两分支。234 rollouts=78scenarios×3，real2h、5objects pick/place；basic ours.93低于base.96，需seen interaction pattern、预测goal空间偏差会失败；结构相似的unseen目标/布局不等开放任务/跨robot。planner34.1B、128H100两天/2000steps/B512，GoalVLA3B+.3B、SigLIP6images、10flowsteps/chunk30，部署每轮仅执行10/30且保留第5/10waypoint转换deltaEE；世界模型训练与policy/execution成本必须分账。GoalVLA实际精度/control-rate、各stage成功detector、tail SLO、CI Not Disclosed。不开所有worldmodel附件。

Books整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L406/408承载训练goal/stage/ground-truth target-padding身份，与运行时旧suffix作废分开。zero-pad不是loss mask，不能称后缀不参与loss；next-goal同步relabel下一stage以避免旧padding。真实停止/物理安全不授权，无单组件因果、basic反退与短chunk/controller回退就近保留。root已实际读396–420正文/邻接与末注1402，非作者POST通过，窄锁释放。

本批4项必要证据与处置已获root独立复核；两个Books改动已实际POST通过。历史作者处理快照92/112不替代当前README计数；当前累计30家族实际Books非作者写后通过，日级未验收。
