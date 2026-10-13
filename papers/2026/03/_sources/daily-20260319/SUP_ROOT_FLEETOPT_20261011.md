# FleetOpt16514：必要理论/工程桥与中心隔离

root仅own本19已有完整题摘拟入选，作者确认未开始必要Source。独立本日上下文，只补03-18自然日；精确身份/本日API及注册可见日夹证沿SUP_LATER_METADATA，既有候选与窗口不搬移。

[FleetOpt exact-v1](https://arxiv.org/html/2603.16514v1)必要实际§2/3–7、Algorithm1/Tables1–5与直接相关AppendixB/C；未核代码/复现。与16054同作者且引用同名DES，真实相关但不是同一论文或重要修订，不自动当有效已审重复。16054已核范围复用，不再全读该模拟器。

## 准入/评分

原硬阈值长度分池→边界附近抽取压缩联合fleet配置、并给出边际成本最优条件→可能改变容量选择与质量/资源交接。新增命题2+2+2=6，中心理论/实现桥需深入；不是将一般排队或压缩原则计贡献，也不因work-in-progress排除。

## 可读机制与关键反侧

给定长度CDF、Poisson到达、请求级服务时间W+H*n，近似M/G/c加tail预算，外层枚举B/γ、各池条件分布再估服务率和整数数量；边界附近经典抽取器把prompt缩到B−max-output。只是一组模型化容量规划/压缩动作，不是token级执行或真实fleet部署证明。两公开长度trace加Agent-heavy合成（40%SWE/25%BFCL/35%RAG）；后者不是第三生产arrival trace。300 LMSYS prompt的BERTScore/ROUGE/TFIDF只测相似度，不能证明RAG语义安全、下游正确性、other threshold保真更好或no-OOM。

中心未闭合，不能直接采用最优/硬保证/生产节省：

1. §3定义c=nGPU*nmax、μ每slot，但Eq11最小化c返回n*并使用λ/(ρmax μ)，§6又用μGPU反演c，slot/GPU/node口径不一致。Table1 per-GPU16×20GB长KV或128×2.5GB短KV均320GB，已经超过80GB，尚未计weights；§7明示8GPU TP node但仍称perGPU，必须明确KV sharding/TP/node计数后才算真实A100资源。不补造量化或假定表数已经按node计算。
2. §4 Eq12/AppendixB Eq17只对arrival mass求导；同文Algorithm1服务分布、nmax、prefill99与B/γ共同变化，遗漏这些直接项，故并不证明实际planner的B最优条件。连续内点条件本身也不保证离散整数或边界最优；后文相同μ与主文相同utilization不能自动等价。扫有限候选可作为独立heuristic，但不凭此把中心定理标成成立。
3. §5 max-output扣预算却以bytes-per-token EMA估长度；必须保留first3/last2句与greedy stopping，未给mandatory句本身超预算或B−output非正的实际fallback/精确token复核桥。Eq15代数不能保证实现不会溢出，更不能保证多并发全pool容量。
4. Algorithm1 short service只从原F<=B校准，未明确混入新增压缩流；long只取>γB又未容纳pc<1压缩失败流，Agent-heavy pc=.75正属于此情况。§7节省依这条桥，不认为只重校long已充分。
5. §3.2 queue99+prefill99不自动等sum99；许多server不保证尾等待≈0。W99式C<.01时须nonnegative quantile分支，当前式未给。Table5是同模型DES的utilization对照，不是P99/物理硬件独立验证；压缩局部CPU profile、批量/并发/precision/模型全执行账不能由2–7ms升级完整SLO。

## 实际owner与处置

`INFER-SCHEDULING` Ch56实际44–82/190–206已有deadline/P99、请求成本预测与预测变更后重新admission的有效原则；不新写一般排队/长度分池。上述联合planner/最优和实现保证的具体新桥未闭合，提议**争议/暂缓**、保6分，无Books新写、不把中心问题改成NC或EX、不授正面Evidence/coverage或性能安全。只隔离该family，不撤销既有独立证据。

一次精确材料请求：统一slot/GPU/TP-node与KV/weights口径的修正版Eq11/Algorithm1/实验配置；包含B依赖项的命题条件/修正推导；压缩失败/mandatory保留/真实token计数fallback及两池混合后的profile；独立质量/P99合同。接受正式勘误、必要配置与最小trace；材料到达只重开16514。当前尚待非准备者独核，不计安全处置。
