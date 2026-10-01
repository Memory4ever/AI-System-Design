# Apr22 三项必要命题与实际 owner 独立审阅

## root 实际写后验收：UniEP

root已顺读Ch36“MoE多维并行必须共享一份Token Dispatch Contract”的真实两段及上下游，复用下文apr20_resume已核实且未变化的精确v1依据。实际正文将固定逻辑地址、物理tile readiness与Top-k归约次序分开，release/acquire只负责payload可见性；SM/HBM/原子状态成本、完整训练逐bit未证、顺序reference回退及Ch35/37交接均在机制附近。没有把所有token到齐改成任意先到先加，也没有把Table6局部forward/backward比较扩大为训练复现。实际write-after通过；这是本篇采用落实，不是Apr22日级完成。

复核者：apr20_resume（非日22作者）。范围仅19241/19351/19485的必要方法、评价反证与当前owner；复用未变有效证据，恢复后定点重开下述原始位置。不是日级Gate、日期/来源验收或实现复现，未改Books。

## 19241 — UniEP

[官方PDF-v1](https://arxiv.org/pdf/2604.19241v1)，采用PDF而不使用July29页头HTML。实际§3.1–3.2/Algorithm1的counts/AllGather/exclusive rank prefix/local stable-sort，§4.1资源互锁，§5.1–5.4、§6.1/6.3/Tables3/6/7与§6.7必要配置。§5.1明确ld_acquire/st_release，§5.3要求payload完成后release信号；不是仅凭scoreboard名称推定内存序。每token等待全部Top-k贡献再归约，提前在rank局部累加会改变浮点association；地址确定、物理ready调度与数学累加次序可以分离。动态worker和relay消费SM/HBM/atomic状态，Ndisp+Nrelay<NSM的调度限制保留，不推无条件无死锁。

当前Ch36 Token Dispatch Contract（606–623）已有router、permutation、rank-group与step边界；Exact Training Replay（1616–1622）已有reduction/sample/collective schedule冻结。缺口不是“此前没有数值合同”，而是固定逻辑placement/归约次序下按到达readiness推进tile的具体接口。2+2+2=6，因该具体缺口深入合理；支持在Token Dispatch链窄补上述分离及成本，不接管Ch35恢复或Ch37tensor lowering。

Table6仅Cluster1/12形状的forward/backward相对serial逐bit结果，不等所有kernel/全训练轨迹证明。Table7放宽bitwise后MoE10=.97/MoE11=.98是反向；serial TE逐expert host同步与kernel一起改变，不能将巨大倍数归为纯通信因果。两Hopper环境准确SKU未命名，Table3的峰值字段不能据容量补卡名。128GPU/512K的生产吞吐是该披露配置观察，不是质量/故障/全run验收。调优29.7–149.9ms、4096token bucket是摊销条件。

结论：**有限source→actual owner窄采用通过**，限作者notes所述placement/readiness/reduction两段机制；具体literal仍应由协调者读取，锁后实际写入及非作者写后另验，不预支整合。

## 19351 — DASH-KV

[官方HTML-v1](https://arxiv.org/html/2604.19351v1)，实际§3.1–3.4/Eqs1–21、§4.1.1–4.1.4/Table1/2、§5.3–5.4/§7。query动态MLP、key一次线性编码、残差校准与percentile三档计算是真实配方；弱项mask明确不是discard，保full-K/V及额外encoder训练，不把hash代理变attention真值。§4.1.4 FP16模拟binary，§7无底层bitwise实现；空间/速度宣传不得升级实测packed-bit serving。Table2的latency数字保原型但没有完整运行条件，不能借一致配置一句补硬件/batch/SLO。

Table1实读Llama42.43低于Full42.70及任务切片反向，Qwen2-7B38.73vs38.71小差无CI；三模型LongBench局部质量不证所有长上下文保真。当前Ch45:328–356已有低成本selector、表示/consumer联合artifact、kernel/layout成本和FullKV回退，并没有完整覆盖该学得hash/residual算法。2+2+2=6必要性能边界深入、**仅报告通过**：保局部配方和对照；无必要长期正文增量，不冒称整个算法Existing。真实packed-bit实现及端到端质量/配置回来时只重开效率采用，不将可执行普通审阅说成external-blocked。

## 19485 — EVPO

[官方HTML-v1](https://arxiv.org/html/2604.19485v1)，实际§2.1–2.3、§3/Eqs3–9/Algorithm1、§4.1–4.4/Table1、Limitations、A.1–A.2与C必要对照。terminal-only、gamma=lambda=1才telescopes成G−V；实现按有限prompt batch EV切换，mean模式仍更新critic，与无critic GRPO显存路径不同。保zero-variance实现未交代和GRPO标准化差别。

A.1中的population残差方差分解需要条件零均值与相应正交性；它比较return residual，不自动比较乘以policy score后的gradient方差或learning success。Kalman权重PA/(PA+PB)还缺误差交叉项/偏置条件，例如delta=a(V−E[V])即可使critic-error和mean-error相关，不能默认最佳融合。作者Limitations明确finite-sample concentration未证，故Eq9每batch不劣于两者不作为保证；无需为这点否定受限recipe或全部实验。

Table1是每任务32query×16rollout、best-validation值；不是独立固定终点或每阶段胜出的证明。C中方法步数/clip/LR不统一，critic200步warmup有额外成本；Gaussian注噪/zero-threshold敏感性是该有限协议，不证明所有critic失败唯一原因或全局最优阈值。当前Ch32:129–163及300–316已承载critic质量、EV监测、state/成本和条件分支；不能把本地controller写成已受普遍稳定性保证。

结论：2+2+2=6中央保证边界深入、**仅报告通过**。保真实协议/表/限制，隔离population→batch→policy-gradient→训练结果的未证扩展；不因安全标签或“无CI”泛化Deep，也不强迫全复现。没有新增Books采用或日级Gate。
