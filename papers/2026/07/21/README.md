# Daily Research — 2026-07-21

**规范：** V3
**窗口：** 2026-07-20T09:00:00+08:00 ～ 2026-07-21T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T17:30:00+08:00

## 1. 结论

本窗口按 first-public owner 得到 919 条 arXiv 原始身份。逐条读取标题与完整摘要后，冻结 12 个候选；旧稿的 147 个候选不作为新分母，其中 135 个旧候选因只提供局部方法/benchmark、垂直应用或没有改变长期系统判断而降回准入前关闭。原始证据保留，但不在正文候选表继续制造重要性错觉。

保留材料集中在可迁移状态、训练/推理执行计划、跨层资源约束、证据与安全边界。每项都已用旧稿保存的 exact-v1 primary evidence 重新核对机制与反证；没有用标题关键字替代语义判断，也没有把能映射 ROADMAP 当作准入理由。独立复核已经把“来源存在”和“正文已承载”分开，并确认本日唯一正文增量已进入目标章节的训练状态生命期主线。

## 2. 来源覆盖

当前登记的机构日源在 2026-09-07 才纳入合同；按历史生效边界不倒推本窗口。表中仍逐项列出，避免把‘不适用’误读为已扫描。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-ANTHROPIC | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-GOOGLE-AI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-META-AI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-QWEN | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-DEEPSEEK | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-MOONSHOT | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-ZAI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-MINIMAX | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-ARXIV | [exact-v1 HTML](https://arxiv.org/)；本窗 919 条 identity 逐条 title + 完整摘要语义筛选；旧稿 exact-v1 Method / Evaluation / Limitations 仅作可核实证据种子 | 已检查 | 无 |

本次排除 AI for Science、纯垂直应用、只改局部任务指标以及没有系统状态/控制/评价契约增量的工作。withdrawn 身份不进入候选；本组没有保留 withdrawn family。

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；7～9 分深入审阅，5～6 分标准审阅。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [KernelBench-Verified: Do LLM-Generated Kernels Actually Beat PyTorch?](https://arxiv.org/html/2607.16241v1) | 2026-07-21T08:00:00+08:00 | `INFER-TENSORRT-LLM`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Let the Data Decide: Supervision Analysis, Capability Trade-offs, and Adaptive Objective Routing in Continued Pre-Training via Off-Policy Distillation](https://arxiv.org/html/2607.16246v1) | 2026-07-21T08:00:00+08:00 | `TRAIN-PRETRAINING`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [LaCache: Exact Caching and Precision-Adaptive Inference for Diffusion Large Language Models](https://arxiv.org/html/2607.16339v1) | 2026-07-21T08:00:00+08:00 | `MULTIMODAL-GENERATIVE-PARADIGMS`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Mitigating Compiler Fusion-Induced Power Bursts in Mobile NPU Inference as the Battery Depletes](https://arxiv.org/html/2607.16555v1) | 2026-07-21T08:00:00+08:00 | `INFER-TENSORRT-LLM`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Cold-Start Model Delivery in Kubernetes Inference Serving: An Empirical Study of OCI-Based Distribution and Its Integrity](https://arxiv.org/html/2607.16596v1) | 2026-07-21T08:00:00+08:00 | `PLATFORM-MODEL-REGISTRY`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-MODEL-REGISTRY`，[目标章](../../../../books/part-06-ai-infrastructure/59-model-registry.md) 已有 URI/digest/provenance 与 materialization verification |
| [Roomie: Interference-Aware Colocation for Efficient Model Serving](https://arxiv.org/html/2607.16784v1) | 2026-07-21T08:00:00+08:00 | `INFER-SCHEDULING`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [Robust KV Cache Management for LLM Serving under Output Token Length Uncertainty](https://arxiv.org/html/2607.16892v1) | 2026-07-21T08:00:00+08:00 | `INFER-SCHEDULING`；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[目标章](../../../../books/part-05-inference-system/56-inference-scheduling.md) 已有 Future-state Reservation 正文 |
| [Talaria: Session-Aware Serverless Serving of Hundred-Billion-Parameter LLMs](https://arxiv.org/html/2607.17181v1) | 2026-07-21T08:00:00+08:00 | `INFER-SCHEDULING`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure](https://arxiv.org/html/2607.17525v1) | 2026-07-21T08:00:00+08:00 | `PLATFORM-GATEWAY`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [A Training-Memory Regression in MLA Sequence Parallelism: Why Megatron-Core Forbids Absorption, and LAGA -- a Communication-Efficient Fix](https://arxiv.org/html/2607.17644v1) | 2026-07-21T08:00:00+08:00 | `TRAIN-TENSOR-PARALLEL`；3 + 3 + 2 = 8 | 深入完成 | 整合：TRAIN-TENSOR-PARALLEL，[目标章](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels](https://arxiv.org/html/2607.18002v1) | 2026-07-21T08:00:00+08:00 | `INFER-SCHEDULING`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [A CXL Memory Rack for Multi-Turn LLM Serving](https://arxiv.org/html/2607.18141v1) | 2026-07-21T08:00:00+08:00 | `INFER-GPU-MEMORY`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-GPU-MEMORY`，[目标章](../../../../books/part-05-inference-system/54-gpu-memory.md) 已有 host/CXL/NVMe tier 与 fault/recompute fallback |

## 4. 证据与知识整合

### [KernelBench-Verified: Do LLM-Generated Kernels Actually Beat PyTorch?](https://arxiv.org/html/2607.16241v1)

**机制。** Kernel benchmark 若沿用 TF32 关闭的弱 baseline、可见 shape 与宽松分布，会把“能过测试”误写成“胜过框架”。KernelBench-Verified 加入 TF32 baseline 和四类 hidden distribution，把 correctness、泛化 shape 与真实 speedup 分开。

**证据边界。** 七个 frontier model 的单轮验证中，最佳模型几何平均 speedup 为 0.88×，低于标准 protocol 的 1.43×；hidden sets 揭示多类失败。结果只覆盖该 operator/test suite 和硬件，未证明 agent 迭代优化或其他 kernel domain 的能力上限。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.16241v1#A12.SS1 — L.1 Methodology; https://arxiv.org/html/2607.16241v1#S2 — 2 Evaluation Methodology。Evaluation：https://arxiv.org/html/2607.16241v1#A10 — Appendix J Tolerance Sensitivity Analysis; https://arxiv.org/html/2607.16241v1#A12.SS2 — L.2 Aggregate Results。Limitations / counterevidence：https://arxiv.org/html/2607.16241v1#A12.SS4 — L.4 Discussion; https://arxiv.org/html/2607.16241v1#A7 — Appendix G Failure Mode Analysis。

**Trade-off。** 更强 baseline 与隐藏测试降低虚假胜率，却提高参考实现、容差和硬件维护成本；生成 kernel 未过完整 gate 时应回退框架实现。

**Books：仅报告。**它强化 `INFER-TENSORRT-LLM` 的 kernel admission 证据，但与 07-17 Atrex-Bench 共同说明同一既有原则，不另建重复正文。

### [Let the Data Decide: Supervision Analysis, Capability Trade-offs, and Adaptive Objective Routing in Continued Pre-Training via Off-Policy Distillation](https://arxiv.org/html/2607.16246v1)

**机制。** Continued pretraining 的 distillation 不是统一 temperature/top-k 问题：不同数据所需 teacher support coverage 与 sharpness 不同。论文以 support mass、observed-token mass 和 concentration 诊断监督，并按数据路由 objective。

**证据边界。** 受控 sweep 支持 support size 控制 coverage–sharpness、temperature 控制 support 内分配，且 routing signal 质量比粒度更关键。未证明该信号跨模型/语料稳定，也未覆盖长期 forgetting、训练成本和线上自适应误路由。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.16246v1#S5.SS1 — 5.1 Experimental Design; https://arxiv.org/html/2607.16246v1#S4.SS1 — 4.1 Model Setup。Evaluation：https://arxiv.org/html/2607.16246v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.16246v1#S4.SS3 — 4.3 Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.16246v1#S8 — 8 Conclusion。

**Trade-off。** 自适应监督可减少无效 teacher mass，却增加诊断、路由错误和多 objective 优化耦合；信号弱时全局固定 objective 更可复现。

**Books：仅报告。**它是 `TRAIN-PRETRAINING` 的受限数据条件分支；当前证据不足以改变通用 objective 主线。

### [LaCache: Exact Caching and Precision-Adaptive Inference for Diffusion Large Language Models](https://arxiv.org/html/2607.16339v1)

**机制。** Diffusion LM 多轮去噪会反复处理未变化 token。LaCache 只缓存满足精确复用条件的状态，并在其余路径使用精度自适应计算，将 lossless reuse 与 approximate arithmetic 分开。

**证据边界。** 在 LLaDA-base/1.5 的披露 benchmark 上，cache 单独约 1.3× 端到端加速，附录给出多任务结果。未证明 exact-cache 条件适用于其他 diffusion 架构，也未给生产 batch、尾延迟或 mixed-precision 错误累计保证。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.16339v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.16339v1#A4 — Appendix D The acceleration of LaCache on LLaDA-base on multiple benchmarks; https://arxiv.org/html/2607.16339v1#A5 — Appendix E The acceleration of LaCache on LLaDA-1.5 on multiple benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.16339v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.16339v1#Sx1 — Limitations。

**Trade-off。** 精确复用降低重复 compute，混合精度再换吞吐；代价是稳定性判定、格式转换和双重回退，质量敏感 token 仍需全精度重算。

**Books：仅报告。**作为 `MULTIMODAL-GENERATIVE-PARADIGMS`/推理执行的受限实现，不足以新增长期主结论。

### [Mitigating Compiler Fusion-Induced Power Bursts in Mobile NPU Inference as the Battery Depletes](https://arxiv.org/html/2607.16555v1)

**机制。** 编译器把多层融合成 superlayer 可减少 launch/中间内存，却会集中功率峰值；电池电压下降时，这种 burst 会更早触发 DVFS。论文测量 fusion→power burst→频率下降链，并以选择性拆分降低峰值。

**证据边界。** 商用手机上的测量支持 superlayer burst 抬高 DVFS onset、压缩低电压 operating margin。证据限该 NPU/设备；CPU/GPU delegate 未形成激进 fusion 时效果有限，也未证明拆分在所有电池健康和模型上净提升延迟。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.16555v1#S3 — 3 Method; https://arxiv.org/html/2607.16555v1#S4.SS3 — 4.3 Models。Evaluation：https://arxiv.org/html/2607.16555v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.16555v1#S4.SS4 — 4.4 Evaluation metrics。Limitations / counterevidence：https://arxiv.org/html/2607.16555v1#S5 — 5 Results and Discussion; https://arxiv.org/html/2607.16555v1#S5.SS7 — 5.7 Limitations。

**Trade-off。** 拆 fusion 降峰值但增加 launch 与 memory traffic，可能牺牲满电性能；应随电源状态选择 plan，并保留原 fused plan。

**Books：仅报告。**它是端侧 `INFER-TENSORRT-LLM` 的 power-aware execution-plan 分支，尚不足以改全书主线。

### [Cold-Start Model Delivery in Kubernetes Inference Serving: An Empirical Study of OCI-Based Distribution and Its Integrity](https://arxiv.org/html/2607.16596v1)

**机制。** 对象存储 URI 的模型字节绕过 admission-time verifier，Kubernetes 成功拉起不等于 artifact 身份正确。论文把 digest pinning 与 OpenSSF signature enforcement 下沉到 storage initializer，在下载流中验证后才暴露给 server。

**证据边界。** 实验显示 streaming hash 开销低于该设置交付时间的 0.1%，事后再扫最高增加 53%。该 threat model 假设模型卷以只读挂载且不处理同节点恶意容器；未证明持续完整性、所有存储后端和生产供应链。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.16596v1#S3.SS1 — III-A Design space; https://arxiv.org/html/2607.16596v1#S4.SS2 — IV-B Design。Evaluation：https://arxiv.org/html/2607.16596v1#S5 — V Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16596v1#S4.SS1 — IV-A Threat model; https://arxiv.org/html/2607.16596v1#S6 — VI Discussion and Lessons。

**Trade-off。** 流式验证缩短未验证窗口，但依赖可信签名、key 管理和 initializer 可用性；校验失败必须阻止 readiness，并保留可审计 artifact identity。

**Books：已有覆盖。** `PLATFORM-MODEL-REGISTRY` 已明确 URI 只提供位置，部署身份还需 content digest、provenance、access policy 与独立 materialization/hash verification；Kubernetes/OCI 的 read-only mount 是受限实现证据，不改变 owner 命题。

### [Roomie: Interference-Aware Colocation for Efficient Model Serving](https://arxiv.org/html/2607.16784v1)

**机制。** 同 GPU colocate 是否违约取决于 kernel 时间重叠，不是平均显存/利用率。Roomie 以 kernel-level temporal profile 预测组合干扰，并据此做 placement/admission。

**证据边界。** 作者在 server 与 edge testbed 上报告最高 3× 更少延迟违约并保持 comparable goodput。未证明 profile 在模型升级、动态 shape 或新 GPU 上稳定，也未披露生产 traffic drift 与预测误差的安全 margin。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.16784v1#S4 — 4. Roomie : System Design; https://arxiv.org/html/2607.16784v1#S2.SS3 — 2.3. Challenges in Modeling Kernel-Level Interference。Evaluation：https://arxiv.org/html/2607.16784v1#S5 — 5. Experimental Setup; https://arxiv.org/html/2607.16784v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16784v1#S8 — 8. Conclusion。

**Trade-off。** 细粒度 profile 提高 colocate 密度，却增加 profiling、重校准和调度搜索；预测不确定时需隔离或保守 admission。

**Books：仅报告。**`INFER-SCHEDULING` 已含 interference-aware admission；本材料是受限实现证据。

### [Robust KV Cache Management for LLM Serving under Output Token Length Uncertainty](https://arxiv.org/html/2607.16892v1)

**机制。** 输出长度未知时固定 KV reservation 会在低估时 preempt/recompute，在高估时浪费 HBM。论文联合选择并行配置、request-class reservation、异构 group 路由和 prefix cache，把未来 KV 占用当作不确定状态。

**证据边界。** 仿真/作者 workload 评价比较 reservation 与联合优化，支持 under/over-reservation 的双侧成本。未与生产 runtime 集成，也未证明在线分布漂移、尾部长度和故障下的 SLO。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.16892v1#S3 — III System Model and Problem Formulation; https://arxiv.org/html/2607.16892v1#S3.SS1 — III-A System Overview。Evaluation：https://arxiv.org/html/2607.16892v1#S5.SS5 — V-E Ablation Analysis; https://arxiv.org/html/2607.16892v1#S5 — V Performance Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16892v1#S6 — VI Conclusion。

**Trade-off。** 更稳健 reservation 降低重算，却牺牲部分利用率并依赖长度分布；预测失真时应动态收紧 admission 或回退保守上界。

**Books：已有覆盖。** `INFER-SCHEDULING` 目标章已有该 family 的状态预测/保守回退边界（来源与正文附近已承载），无需重复。

### [Talaria: Session-Aware Serverless Serving of Hundred-Billion-Parameter LLMs](https://arxiv.org/html/2607.17181v1)

**机制。** Serverless 多模型服务若只按单请求放置，会在多轮 session 中反复开模型、搬 KV 并拉长 session completion。Talaria 将 session continuity 纳入 placement/admission，联合利用模型驻留、host KV 恢复和 device staging。

**证据边界。** 两 worker testbed 上，相对关闭这些机制的 round scheduler，论文报告 p50/p95 session completion 显著下降。未证明更大 fleet、故障/租户隔离、真实 burst 或模型升级下保持同等收益。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.17181v1#S3 — 3 Design; https://arxiv.org/html/2607.17181v1#S3.SS1 — 3.1 System Overview。Evaluation：https://arxiv.org/html/2607.17181v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.17181v1#S7 — 7 Conclusion。

**Trade-off。** 保留 session locality 降低 reopen，却可能造成热点和公平性下降；高负载时需允许迁移并付出显式 state-transfer 成本。

**Books：仅报告。**`INFER-SCHEDULING` 已有 session affinity 与 state-aware scheduling 主线；本结果不单独改写。

### [FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure](https://arxiv.org/html/2607.17525v1)

**机制。** 多 provider 服务最危险的故障可返回 200/健康指标，却悄然丢 history、错位 stream index 或损坏 tool payload。FailureAtlas 以状态被首次破坏的位置组织 failure taxonomy，并将检测、归因和恢复与普通可用性分开。

**证据边界。** 论文 catalog 汇总 issue/postmortem，并在评测中首次发现 history race 与 streaming collision；这证明 taxonomy 可用于发现静默故障。catalog 很小，不能证明 failure space 完备或生产发生率。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.17525v1#S2.SS1 — 2.1 Distributed-Systems Failure Taxonomies; https://arxiv.org/html/2607.17525v1#S3 — 3 Taxonomy Design。Evaluation：https://arxiv.org/html/2607.17525v1#S2.SS2 — 2.2 LLM Evaluation and Reliability。Limitations / counterevidence：https://arxiv.org/html/2607.17525v1#S7 — 7 Discussion: Why Silent Failures Dominate; https://arxiv.org/html/2607.17525v1#A1 — Appendix A Full Failure Catalog。

**Trade-off。** 细化 taxonomy 提高诊断，却需要跨 gateway/runtime 的 state lineage 和语义 probes；规则会过时，未知模式仍需人工/残差聚类。

**Books：仅报告。** `PLATFORM-TRACE`/Monitoring 的故障归因主线可以解释该 taxonomy；当前仅有来源型边界，没有必要把供应商 catalog 变成正文机制。

### [A Training-Memory Regression in MLA Sequence Parallelism: Why Megatron-Core Forbids Absorption, and LAGA -- a Communication-Efficient Fix](https://arxiv.org/html/2607.17644v1)

**机制。** MLA inference 可把投影吸收以省计算，但训练反向需保留中间量；将 absorbed form 直接搬到 sequence parallel 会把每 token activation 扩到 `n_h × d_kv`，反而增内存。LAGA 保留显式形式并重排通信，避免该维度膨胀。

**证据边界。** 论文在 DeepSeek-V3 尺度分析中报告 20–34% activation 增幅，并在 8×Ascend 910B 上给出约 1.98× collective reduction、误差与 attention-block throughput。未证明 full-model wall-clock/MFU 与长程收敛，也未覆盖其他拓扑。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.17644v1#S1 — 1 Introduction; https://arxiv.org/html/2607.17644v1#S2 — 2 Background。Evaluation：https://arxiv.org/html/2607.17644v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.17644v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.17644v1#S4.SS7 — 4.7 Limitations and scope。

**Trade-off。** 显式形式守住 activation，代价是需要专用通信/算子；LAGA 降通信但增加 layout 与数值等价验证。单设备或内存充足时原路径仍合理。

**Books：已整合。** `TRAIN-TENSOR-PARALLEL` 的 “MLA Sequence Parallelism 不能为省通信破坏 Activation Lifetime” 已明确：inference 的前向代数吸收不能直接继承为 training memory plan，必须先写出 forward/backward tensor ownership 与 lifetime，再选择通信重排；正文保留实现复杂度、拓扑敏感和保守不吸收回退。

### [ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels](https://arxiv.org/html/2607.18002v1)

**机制。** MoE 的 expert weights 巨大而 attention 模块较轻；按整实例做 PD disaggregation 会复制或搬动 experts。ExpertPlex 共享 expert pool、分离 phase-specific attention，并用 persistent kernel 随负载调整 expert 执行。

**证据边界。** 在 MiniMax-M2.7、GLM-5.1-FP8 的论文配置中，相对 instance-level PD 和 colocation 报告最高 2.01×/1.66× goodput。未证明其他 MoE、拓扑、故障隔离或多租户 tail SLO。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18002v1#S4.SS1 — 4.1. GPU Sharing Design Space; https://arxiv.org/html/2607.18002v1#S2.SS2 — 2.2. GPU Execution Model。Evaluation：https://arxiv.org/html/2607.18002v1#S7 — 7. Evaluation; https://arxiv.org/html/2607.18002v1#S7.SS1 — 7.1. Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.18002v1#S9 — 9. Conclusion。

**Trade-off。** 共享 experts 减少重量级复制，却引入跨 phase contention、路由队列和 persistent-kernel 饥饿风险；压力失衡时需重新分区或回退实例隔离。

**Books：仅报告。**它是 `INFER-SCHEDULING`/MoE serving 的特定架构分支，证据不足以改变通用调度主线。

### [A CXL Memory Rack for Multi-Turn LLM Serving](https://arxiv.org/html/2607.18141v1)

**机制。** 多轮 KV reuse 把瓶颈从 GPU compute 转到可共享 memory tier；节点本地 DRAM 难以扩展，远端访问又可能吞掉复用收益。HyMCache 以 CXL pooled memory 保存 KV，并面向单机与 PD 路径安排数据移动。

**证据边界。** 真实 CXL-HM prototype 上，论文在相同 DRAM budget 下相对 local LMCache 报告单节点 3.0×、PD 1.45×。未证明更大 rack、并发尾延迟、故障一致性和不同 CXL/网络拓扑的成本。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.18141v1#S1 — 1. Introduction; https://arxiv.org/html/2607.18141v1#S2 — 2. Background and Motivation。Evaluation：https://arxiv.org/html/2607.18141v1#S5 — 5. Experimental Setup; https://arxiv.org/html/2607.18141v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.18141v1#S8 — 8. Conclusion。

**Trade-off。** 池化提高容量与复用，但增加远端延迟、共享拥塞和失效域；热 KV 仍需 HBM/本地 tier，远端超 SLO 时回退重算。

**Books：已有覆盖。** `INFER-GPU-MEMORY` 已把长状态置于 GPU/host/CXL/NVMe 多级层次，并要求 logical mapping、state identity、transfer latency、fault/revocation 与 recompute fallback 一起验收；本 CXL rack 是该分支的设备绑定实例。

## 5. 缺口与下一步

无

无 external Materials Request。全部保留候选均可访问 exact-v1；旧候选降级不会删除原始证据。本日所需 Books 写入和写后语义审计均已完成；若后续出现具体 false positive、false negative 或来源更正，只重开对应 family。

准入闭合账目：raw identities=919；旧候选=147；V3 候选=12；本轮从旧候选降级=135。准入前关闭的共同原因是：局部指标或单任务方法没有持久系统增量、垂直应用/AI for Science 越界、benchmark 未改变 evaluation/deployment contract，或机制已被同日更强材料覆盖。

## 6. 复核

复核者：非作者独立复核（/root/aug11_20，2026-09-10）。

结论：通过

写后复核确认 `SF-2026-ARXIV-2607-17644` 已进入 `TRAIN-TENSOR-PARALLEL` 的 activation-lifetime 正文，且和前文数值/通信验收、后文知识树交接连续；其证据只支持特定 Megatron-Core/MLA regression 与修复，未被外推成所有 TP 的统一规则。
