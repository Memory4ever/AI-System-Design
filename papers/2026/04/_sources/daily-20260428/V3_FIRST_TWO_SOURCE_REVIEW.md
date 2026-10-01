# 04/28 两项 exact-v1 必要证据与 Books 写前比较

这不是整日候选冻结或日级通过。两项 arXiv ID 位于相邻公告批次的有界 04/28 推断段，均在官方版本页显示更早的 v1 **submitted**；这不自动改归提交日，也不是逐篇精确公告小时。[单篇日期组合](./V3_FIRST_TWO_DATE_BOUNDARY.md)已另存。root 独立通过两项 source→owner 写前判断，并在两章实际写入后顺读正文、邻接与 Review notes，见[非作者写后审计](./V3_ROOT_22782_22783_WRITE_AFTER.md)。**两单篇 Integrate 的写后 Gate 已过；本日贡献分母、其余候选和日级 Gate 尚未通过。**

## `2604.22782v1` — Random Cross-Layer Attention

- 版本与原文：官方[摘要与版本](https://arxiv.org/abs/2604.22782v1)、[HTML v1 §3.1.3–3.2、§4.1–4.3、Limitations](https://arxiv.org/html/2604.22782v1)。v1 submitted 04/03，不作 first-public。暂无撤回标记。
- 机制：不对既有 checkpoint 运行时直接删除任意层 KV；训练中对每层以 Bernoulli 在本层 KV 与随机更早层 KV 间切换，形成跨多种深度共享模式的 Q/K 对齐。部署时先选缓存 leader 集合，未保留层读取最近前序 leader 的 KV。这个设计把“特定跨层共享拓扑”改成训练时暴露的**一组可部署 retention 策略**，与 Ch45 当前固定混合 KV 后再缓存的 trained sharing 不是同一责任。
- 对照/反证：§4.1 Table1 的 1.7B 预训练 p=.75 loss 2.424→2.461，不能叫零质量损失；§4.2 Table2 中 RepLiQA 100% retention 的 Llama/Mistral 有小退步，25% retention 的某些 F1 仍很低；§4.2 Table3 的固定 CLA 在全量缓存时有时优于随机路径。§4.3 Table4 Qwen3-8B-shape、单80GB GPU、bf16、batch1 的 8K KV 1170→293MB、TTFT297→286ms、decode34.0→41.6 tok/s，只支持该受测组合，不证明任意 cache 策略、MoE、并发或 SLO；Limitations 明写需训练资源、未测 MoE/overtraining。
- 与当前 owner 的实际差异：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`“从统一跨层共享到 Token × Depth 自适应残差”已有固定层级共享、先混合后缓存、basis/residual/精确保真分支；尚未讲“随机训练覆盖多部署 retention 集合”的兼容性条件。若独立采用通过，建议只在该段 trained sharing 后加入：部署缓存集合选择仍由 runtime/硬件预算负责，训练仅提高对集合变化的耐受；与固定混合、运行时近似重建及 FullKV 共存，不能把训练内随机性当推理动态 oracle。
- 评分：Design Delta 2、System Reach 2、Durability 2，合 6/9；确认当前 Ch45 的具体长期知识缺口，按合同触发深入审阅。`Integrate Ch45` 窄正文已落在 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的跨层共享段与 Review notes，非作者实际写后通过；日级最终候选集仍待冻结。

## `2604.22783v1` — Activation-rank PEFT

- 版本与原文：官方[摘要与版本](https://arxiv.org/abs/2604.22783v1)、[HTML v1 §3–4、§7](https://arxiv.org/html/2604.22783v1)。v1 submitted 04/03，只作 provenance，非本窗首次公开证明。暂无撤回标记。
- 机制：普通 LoRA 缩小可训练权重，却仍保留 adapter 中按 `[B,S,R]` 增长的反向所需激活。LARS 先将序列汇聚到 `[B,H]`，在压缩后的 rank 空间调制，再经 gated residual 写回；目标是让**adapter 特有中间态**从 `O(BSRL)` 降为 `O(BRL)`，不是整个基座训练内存与计算脱离 `S`。论文固定 pooling 和 learned pooling 是不同成本分支。
- 对照/反证：§4 Table2 涵盖 1B/7B、reasoning/understanding/long-context；LARS 有更多可训练参数（0.67% vs LoRA 0.45%）、部分任务准确率低于 LoRA，不能称严格 Pareto 支配；§4.4 的 Raspberry Pi 5 与 EPYC CPU 测试仍只验证指定模型/长度。§7 明列 ≤8B、额外参数/训练开销及 pooled representation 的 token-level 词面保真代价。摘要 33.54%/51.95% 是所测平均，不是任意长度或全部内存分量的保证。
- 与当前 owner 的实际差异：`books/part-04-training-system/30-lora.md`“为什么会节省训练显存”已明确可训练参数减少不等于 activation、workspace 减少；但目前仅作**计量/告警**，未给“把 adapter 的可训练激活先跨序列汇聚，再在低维空间更新”的条件化解决分支。若独立采用通过，应接在该计量段后，说明总 base activation 仍在、pooling 可能损失精确 token 细节、LoRA 在任务需局部 token 更新或希望独立线性 adapter 时继续合理。
- 评分：Design Delta 2、System Reach 2、Durability 2，合 6/9；确认当前 Ch30 的具体长期知识缺口，按合同触发深入审阅。`Integrate Ch30` 窄正文已落在 `books/part-04-training-system/30-lora.md` 的显存分项段与 Review notes，非作者实际写后通过；日级最终候选集仍待冻结。
