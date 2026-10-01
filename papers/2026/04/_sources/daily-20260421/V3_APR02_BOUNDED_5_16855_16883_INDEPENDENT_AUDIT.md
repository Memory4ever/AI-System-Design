# Apr21 五项有界非作者核：16855～16883

审阅者 apr02；实际访问 2026-09-27。先重读当前 AGENTS/研究合同，并读取作者 `V3_BATCH_16855_16883.md`。仅独立核必要官方 v1 方法、关键反证与当前 owner/相邻交接；未复现实验、重扫来源、核准首发日期或执行日级 Gate。本文件不修改作者 Report、notes 或 Books。

## 2604.16855v1 COD-TDQ — 5 分标准，仅报告：通过

[官方 HTML v1](https://arxiv.org/html/2604.16855v1) §3–4、S1.2 与局部对照实际读。背景 outlier 统治共享 activation range，使弱边界进入 zero-bin；token-group range 与 step/dispersion、zeroization 控制提供具体量化失败诊断，不是因小模型/领域标签排除。

S1.2 明确 INT4 权重临时反量化、Linear/Conv 在 fp16/fp32 执行。在线统计、QDQ path 和序列化 packed checkpoint 必须分账；不是 native INT4 throughput/activation traffic 证据。实际 Ch49 execution/quantization 主线可承载这些边界，但不称已包含 COD-TDQ 配方。受限 CFRN/ESCNet 与四 COD 集结果仅报告；不把 quantile 控制外推为任意 ties 下的严格保证或 LLM 加速。

## 2604.16864v1 HieraSparse — 6 分知识缺口深入，Ch45 提案：通过，配置更正

[官方 HTML v1](https://arxiv.org/html/2604.16864v1) §III.A–C/Algorithm 1、§V.A–B，另核[官方 PDF v1](https://arxiv.org/pdf/2604.16864v1)首页与 §V 配置。dense/nonzero/metadata 三池加 signed map，K 与 Vᵀ 作为 sparse 第一 operand、online softmax，以及 Prefill 后进一步压缩 Decode KV，是可定位的状态/执行联合分支。

实际 Ch45 “Token × Feature 二维”段有 rank/packed-offset/runtime 主干，未具体承载 dense 与 N:M blocks 并存及 phase 再压缩；可窄补该处，Ch49 仅 handoff，不重复建立 owner。必须保留 sink/local dense、K/V/模型敏感性差异、压缩 tax 与质量退步；4.57× 对 MUSTAFAR attention 不等端到端总生成倍数。

作者配置缺口需修：HTML §V、PDF 页 7 明确 **L40S 48GiB、Python 3.10.19、PyTorch 2.10.0、CUDA 12.8**；不能写 GPU 全未披露。剩余 precision/output length/concurrency/SLO 缺口不补造。这里只通过 source→owner，未实际写 Books/写后核。

## 2604.16870v1 Governed MCP — 6 分保护深入，仅报告：通过

[官方 HTML v1](https://arxiv.org/html/2604.16870v1) §3–4、§4.5–4.6、§5.1–5.3 实际读。六层 gateway 只有 ProbeLogits 是 semantic forward；WASM host ABI 统一入口与 fail-closed engine-unavailable 是实现范围，不证明 classifier 判断正确或整个 OS 无旁路。

当前实际 Ch72 typed authorization/tool executor 分权承载采用边界。原文 123 条同步 host paths、101 条 author-labeled prompts、部分 ablation deferred、Cranelift/TOCTOU/恶意模型限制不可省略。单全局 forward 锁、KV snapshot/restore 与约 65ms probe 是成本/状态责任，不是零代价或完整并发保证。当前 v1 的具体 OS 配方仅报告，不能沿用旧库存性能或将结构论证升级为全栈 formal certificate。

## 2604.16880v1 Symphony — 6 分知识缺口深入，Ch36 提案：通过

[官方 HTML v1](https://arxiv.org/html/2604.16880v1) §3.2–3.4、§4.3–4.7 与 §5 实际核。switch 从 step/PSN 近似跟踪落后进度，只给 outpacing 流额外 ECN；它与普通 congestion marking 作 OR，继续由 DCQCN 控制发送。这不是 in-network reduction。

实际 Ch36 SHARP→CollNet→runtime 段集中于归约执行位置，未承载 progress-conditioned network feedback，可在该交接窄补数据算子与控制反馈分工。局部观测不拥有 collective completion 真值；metadata/state、warm-up 与停用额外 mark 的 baseline 回退应明确。

ASTRA-sim 与人工缩短 compute 不是全规模 LLM 实测；Tofino2/ConnectX6、两条 1GB 流/10Gbps/UDP source-port tag 只证明原型范围，领先流有小退步，MoE/非 ring 未验。UEC 映射未独立规范核，不采用为已验证协议事实。仅 source→owner PASS，未写 Books。

## 2604.16883v1 SinkRouter — 6 分知识缺口深入，Ch45 提案：通过，精度更正

[官方 HTML v1](https://arxiv.org/html/2604.16883v1) §3 Eq3–5、§4.1–4.3、§5；另核[官方 PDF v1](https://arxiv.org/pdf/2604.16883v1) §5.1。Prefill 保留初始 token anchor，Decode 用 cosine proxy/length threshold 对 GQA group 联合路由，在加载历史 KV 前跳读并以零输出替代；缓存未永久 eviction。

实际 Ch45 sink/eviction 与 head 保真预算段未具体承载“保留容量、逐步跳读”的分支，可接该预算论证。Eq4 只约束当前给定 attention mass/value 范数的单次更新，不证明 query proxy 正确、全生成误差或一般 stable/reachable 性。质量反例、128K 激进 skip 后下降、短上下文收益弱、repeat_kv 优化混杂与 FullKV 回退必须靠近正文。

作者配置缺口需修：HTML §5.1、PDF 页 6 明确 **RTX PRO 6000、all experiments bf16**；precision 不能列 ND。所谓 effective 40% budget 是读取/计算稀疏预算，不应同 token eviction 的 resident bytes 等量；实际 cache 容量、batch/concurrency/SLO 仍须分开。这里只通过 source→owner，未写 Books/写后核。

## 交接

5 项有限审计完成：3 个具体 gap 提案、2 个仅报告；无本审计普通待核。三 gap 仍需共享文件许可、最小正文写入与非作者写后验收；不代表候选冻结、日期/来源 Gate 或 Apr21 Complete。两个实际披露字段更正已通知作者，其他缺口保持原精度。
