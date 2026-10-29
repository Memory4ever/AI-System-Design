# 系统三项必要命题与owner提案

作者supp_jan15；已完整题摘非作者准入校准，不扩216库存。原件system-ID-core0及required1–4/direct5–6，日期08113/08135在dates47、08082在date-boundary08082；normal公告/正式ID上下界条件复用，不以Submitted/Updated或注册单独断言首公开。当前官方abs没有明确更早完整正文链接或撤回/勘误信号；08082未来v2/v3不无差别比较。以下无Books锁，待root必要原证/实际owner判断。

## 08113 Coordinated Cooling and Compute Management — 2+2+2=6，标准必要完成；Ch56窄差额提案

实际§III–V/AppendixA：30min token forecast→TP8容量估服务器；5min TP pool MILP→冷却MPC供气温度/流量→job-class DVFS。不只是温度告警，冷却actuation和TP/pool耗电要联动；但job-count proportional dispatch不自动按真实token量平衡。Output-length predictor validation91%不是服务SLO证书，idle GPU smart-switch无restart只是条件性说明，未见完整KV迁移/transition开销测量。8×V10016GB Llama2-7B profile/1hour实验与1day Azure trace simulation分开；precision/batch/concurrency/完整forecast-controller-transition成本与尾SLO Not Disclosed。TableVI平均2.31→2.28s不证明P99/全部request违约0；24.2/31.2%分别该compute/cooling账本，非所有site净省。TableIV cold-zone上限12°C与供气最低18°C的可行性口径不明确，不采用具体物理配置或无条件thermal safety；PID只调supply command而MPC调两knobs，不授预测本身单因果。TableII power并非全频率严格单调。不复现，不推广液冷/多租户。

actualINFER-SCHEDULING Ch56:84–101完整thermal headroom有sensor/model→budget→batch/DVFS/placement与calibration/failsafe，但主动冷却的慢actuator与TP pool快控制边界未被现body采用，原HeatCache明确不涵盖rack/HVAC。拟仅补一短段说明冷却/compute两个执行权限与不同周期协同，重配置和预测代价/回退保留，不添数字或抄MPC recipe；若此窄命题可由现文承载则Existing。

## 08082 Hierarchical Precision and Recursion — 2+1+2=5，标准必要完成；仅报告提案

实际§III/§IV：POTRF之外递归TRSM与SYRK，off-diagonal GEMM低精度/对角高精度和block scaling共同改变数值—计算取舍。与主线关系是optimizer/preconditioner中SPD线性求解的计算原语，不把领域应用或ML词计准入，也不授论文已验证LLM训练。H200/MI300X，Julia1.12.0/vendor basecase；dense随机SPD加n对角制造良好conditioning，误差比较factor与FP64，不是solve residual/训练收敛。SPD一般不保证diagonal dominance；scaling仅控制动态范围，不能保证accumulation无溢出/病态稳定。高precision baseline与FP16全组合不同数值目标，14×FP64SYRK、5×混合POTRF不合并为同accuracy总训练speed；浅/小矩阵深递归overhead退，MI300X图caption32k/2.2与body65k/5.3不同口径不统一；AMD未有同GemmEx mixed path。batch/concurrency/seed/SLO和实际训练optimizer workload Not Disclosed。

actualTRAIN-PRETRAINING Ch28:610–620可行度量投影/逆根、720–738Jacobian/预条件器求解与成本已有具体语义；本稿计算核没有对该optimizer或foundation workload验证，不将Ch49推理execution owner改为通用数值solver收纳。新增recursive solver局部设计与conditioning限制保报告，成熟mixed precision/hardware dispatch原则不算新增长期命题，拟标准完成/仅报告（非贡献前关闭）。

## 08135 ENACHI — 2+2+2=6，标准必要完成；Ch56差额提案

实际§II–IV/Alg2：任务级拟合accuracy–feature-ratio曲线决定split/bandwidth/reference power，packet inner queue跟踪该reference，渐进feature传输按importance并用训练entropy predictor或deadline停止；reference tracking接口是具体粒度差额，不把Lyapunov/两时标成熟原则另算创新。Server每slot interim inference和训练MLP有成本，不是免费正确性sensor；stop entropy≠每sample accuracy，deadline可不够feature。ResNet50/ImageNet、Rayleigh channel/FDMA、相同任务同步frame的1000轮simulation，不是foundation服务实测；frame300ms/slot1ms/device2GHz/edge20GHz为模拟参数，不作真实GPU SKU。precision/真实batch/并发SLO/训练预测器与全链端到端能耗Not Disclosed，server energy未计。Importance从训练Taylor，参数重要不等每sample因果信息；accuracy单调递减收益为拟合假设。Eq25初始q=0且未显式clamp/正定Hessian写concave互冲，不发布可执行功率recipe。Theorem Eq27/28残差M²→平均不收敛/violation可能线性，仅有限条件界不授长期零超额；本次不采用该定理，无需扩全证明附件。

actualCh56:84–101热状态预算及1035–1075 calibrated-routing真实反馈/dispatch边界能承载估计≠执行资格，但未见任务reference budget→packet-level consumption/deadline与feature-stop的同一分工。拟一短段通用受控split-inference接口，保reference与实际消耗、预测/传输/重复inference费用及fallback；该当前CNN原件不授LLM feature通信可直接套用。待root必要源/owner决定，不先写。
