# Harvest：必要命题审阅，实际Source与已有覆盖通过

原件：[2602.09188v1 HTML](https://arxiv.org/html/2602.09188v1)。原题摘准入、具名日期包络及必要Source经root实际通过。2+2+2=6；不是借用通用通信原理加分，而是fixed collective steps的topology重配区间与固定重配罚时联合选择。

必要已读：§3.1假设、§3.3/4.1–4.4/Eq5–7/Algorithm1、§5受限cyclic RecursiveDoubling分支、§6.1–6.2与反侧。正文抓取的去math纯文本仅辅助阅读，公式仍实际核HTML；不能由该纯文本称实现正确性。§4的核心是先为连续区间求静态拓扑成本，再按固定k分段，最后加k×重配罚时选择。依赖固定已知step/data、固定重配罚时、cut-through forwarding/共享内存barrier和子问题精确解；不能授一般动态需求或未知拓扑延迟最优。Algorithm1末尾base初始化书写与t/k有不一致，故不采用其伪码作为运行实现；有限区间分解命题仍由Eq7明确支持。也不采用§5全球最优拓扑结论去跨算法推广。

关键evaluation：8–64GPU数值/packet仿真、800Gbps每port；真实硬件部分是8GPU/8BlueField3/100Gbps光收发器eSwitch仿真拓扑，NCCL逐步pause/update/resume，再**追加固定物理重配罚时**，不是全套真实光交换机生产部署。基线为静态ring/torus/Kautz及每步重配BvN；中间区间可选择少量重配，高罚时小消息退回静态；All-to-All端口增多收益下降。硬件/precision/模型训练端到端、并发/SLO与能耗没有相同合同，写Not Disclosed/不适用，不照搬最高倍数。§6 practical不是完整系统实现，较大同步线程模拟亦不等真实256GPU。拟采用仅为“固定collective schedule下，以连续区间成本和重配代价联选拓扑”，完整解算、cache有效性和barrier费用须保留；固定拓扑/不重配基线继续合理。代码未运行。

Books：TRAIN-DISTRIBUTED-TRAINING，Ch36§1768–1784现有正文已实际承载分阶段topology/rank选择、重配费用与收益联选、已知DAG条件及静态fallback；root实际核同命题覆盖，No Change通过，无Books写入。本项Source/owner通过不授本日DAY。Algorithm1实现正确性、普遍最优、真实光交换生产与完整E2E依旧不采用。
