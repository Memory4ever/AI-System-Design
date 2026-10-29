# Time-Varying Dynamics — necessary Source / PRE

SF-2026-ARXIV-2604-02260；Apr3组合日门已独核，旧04-03冻结表无此identity。2+2+2=6：环境漂移下全历史GP方差可能很小但真误差仍高→把统计不确定性与时间偏差分开→改变WorldModel replay保留范围与乐观planning的资格。不是领域指标归入Foundation，采用直接模型校准条件。

[完整v1 HTML](SUP_2604.02260v1.html)/[primary](https://arxiv.org/html/2604.02260v1)/[DOI](SUP_2604.02260_doi.json)。作者actualIII–V/VII–VIII核心及Lemma1/Eq8、NN路径VI读核。理论：episodic有限horizon、episode内动态固定、bounded reward、iidGaussiannoise、所有各state维动力学在同kernel RKHS且norm/累计变化PN有界；方差只反映固定函数假设下统计不确定性，误差界另含保留horizon内累计drift项。reset/slidingwindow减少旧偏差，却增加数据丢失/统计方差。只采这个分解/条件，不采用未独核的完整dynamic-regret公式、最优window或NN普遍校准。

V-C reset周期H、window w是预设/调参，不是自动识别变点；VIII明确adaptive horizon为futurework。VI实际NN使用BNN与tunable explorationweight，非直接理论λ；另加model/policy softreset Eq15。VII Pendulum/HalfCheetah/Hopper以actuator strength指数下降制造漂移，regret参照是每固定强度单独SAC得到的estimatedoptimum而非已知oracle；5seeds/SE。实RC-car parking渐降throttle6seeds，不能推广突变/周期漂移/任意non-episodic系统、视觉WorldModels或机器人安全；reset/window与parameterreset多项同时变，需消融后才归单因果。未核实现或复现，完整训练硬件/precision/总预算Not Disclosed。

## Owner / 逐字PRE

MULTIMODAL-WORLD-MODELS，[Ch25](../../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)Imagined rollout。作者actual§374–408“误差/uncertainty/真实反馈”及其前后、Ch24/26开篇交接；当前只泛讲uncertainty与modelbias，未区分GPposterior variance对非平稳drift失明/保留数据horizon。不是Agent Memory forgetting，也不授GP结论给所有latentfoundation模型。

逐字PRE，原390句之后、下一“缩短想象还可以同时改变模型的时间单位…”之前：

> 误差可能因 feedback 放大、收缩或转向未见状态。planning 越强，越可能利用模型漏洞。需要 uncertainty、short-horizon replanning、real observation refresh 或 robust objective。

拟两段：

刷新观测也不能只看模型报告的 uncertainty。若真实 dynamics 随 episode 漂移，用全部历史转移拟合的 GP 后验方差仍按“同一固定函数”计统计不确定性，可能越来越小，而旧 dynamics 导致的预测偏差仍很大。在共同 kernel／有界 RKHS 变化等条件下，误差界要另计保留数据区间内的时间漂移；周期清空或滑动窗口是缩短这段旧偏差的分支，不是让全部 uncertainty 都归零。它丢弃可复用样本、增加重学与统计方差，因此窗口过短、动态实际稳定或漂移尺度未知时，完整历史或保守混合仍合理。<!-- source-family:SF-2026-ARXIV-2604-02260 -->

[Time-Varying Dynamics v1 §III–VIII](https://arxiv.org/html/2604.02260v1)只在有限 episodic、过程噪声及变化预算假设下支撑上述 GP 分解；其 NN 实验另用调参探索权重和 model／policy soft resets，不能直接继承 GP 校准或最优 horizon 保证。连续控制的渐降 actuator 与 RC-car throttle 实验提供受限适应证据，regret 对照仍是 estimated optimum；真实换域、突变、周期变化或视觉模型必须重新验收，不能把有限 uncertainty 或短窗口签发成物理安全。预测支持不足时，继续短 horizon、保守探索与真实反馈。

待reader必要Source/PRE与root窄锁，不先写或记I。
